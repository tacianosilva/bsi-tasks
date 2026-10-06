# Guia 4: Ambiente opencode no Container (Agente de IA + Toolchain)

Este guia documenta o uso do [opencode](https://opencode.ai) — agente de código aberto de inteligência artificial que roda no terminal — como ambiente de desenvolvimento completo dentro de um container Docker.

A imagem é construída a partir do **Ubuntu** e o **opencode é instalado como mais um passe** do `Dockerfile`, junto com as ferramentas necessárias para programar: **Git**, **GitHub CLI** e a stack **Python/Django** (`python3`, `python3-dev`, `python3-venv`).

É a abordagem indicada para **laboratórios multiusuário** e máquinas com permissões restritas, onde não é possível (nem desejável) instalar ferramentas na máquina host: o container é montado na pasta do projeto e o opencode fica responsável por editar, executar e versionar o código.

---

## 1. Cenário de Uso e Arquitetura

```text
┌─────────────────────────────────────────────────────────────┐
│                       MÁQUINA HOST                          │
│                                                             │
│   [ Terminal do Laboratório / Estação Local ]               │
│               │                                             │
│   Apenas Docker instalado: tudo o mais roda no container     │
│               │                                             │
│               ▼  Bind Mount (-v $(pwd):/workspace)           │
│   ┌─────────────────────────────────────────────────────┐   │
│   │                  CONTAINER DOCKER                   │   │
│   │                                                     │   │
│   │   opencode (agente de IA no TUI)                    │   │
│   │   • git + github-cli (gh)                           │   │
│   │   • python3 + python3-dev + python3-venv            │   │
│   │   • executa: pytest, django runserver, git push ... │   │
│   │                                                     │   │
│   └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

- **Host:** apenas o Docker. O código vive no host, na pasta montada em `/workspace`.
- **Container:** o opencode e toda a toolchain (Git, gh, Python). É efêmero (`--rm`): ao fechar, nada sobrevive dentro dele.
- **Sincronização:** qualquer alteração feita pelo opencode dentro do container é gravada imediatamente no host (e vice-versa).

A imagem oficial `ghcr.io/anomalyco/opencode` é mínima (baseada em Alpine Linux) e não traz Git, GitHub CLI nem Python. Por isso construímos a nossa própria imagem — veja a Seção 2.

---

## 2. Dockerfile de Referência

### Arquivo: `docker/opencode/Dockerfile`

```dockerfile
FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1

# 1. Ferramentas básicas, Git e GitHub CLI (repositório oficial do gh)
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    git \
    && curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg \
        -o /usr/share/keyrings/githubcli-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" \
        > /etc/apt/sources.list.d/github-cli.list \
    && apt-get update && apt-get install -y --no-install-recommends gh \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# 2. Stack Python/Django: interpretador, headers de desenvolvimento e venv
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-dev \
    python3-venv \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# 3. Usuário não-root com UID/GID do host
ARG USERNAME=developer
ARG USER_UID=1000
ARG USER_GID=1000

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m -s /bin/bash $USERNAME

# 4. Instalação do opencode (mais um passe da imagem)
USER $USERNAME
RUN curl -fsSL https://opencode.ai/install | bash -s -- --no-modify-path

USER root
RUN ln -s /home/$USERNAME/.opencode/bin/opencode /usr/local/bin/opencode

USER $USERNAME

WORKDIR /workspace

CMD ["opencode"]
```

Notas sobre os passes:

1. **Git + gh:** o GitHub CLI vem do repositório oficial da GitHub (`cli.github.com`), evitando versões desatualizadas dos pacotes do Ubuntu.
2. **Stack Django:** `python3` (interpretador), `python3-dev` (headers para compilar extensões C como `psycopg2` e `Pillow`) e `python3-venv` (ambientes virtuais isolados por projeto).
3. **Usuário não-root:** o `UID`/`GID` do container é igual ao do usuário no host, evitando arquivos "travados" como `root`.
4. **opencode:** script oficial de instalação, mais um passe da imagem. O binário é vinculado em `/usr/local/bin` e definido como comando padrão (`CMD`).

---

## 3. Build e Execução

### 3.1. Construindo a Imagem

Na raiz do repositório:

```bash
docker build \
  --build-arg USER_UID=$(id -u) \
  --build-arg USER_GID=$(id -g) \
  -t opencode-dev:latest ./docker/opencode
```

> **Por que `USER_UID=$(id -u)`?** Garante que os arquivos gerados dentro do container (venv, `__pycache__`, bancos de dados) pertençam ao seu usuário no host.

### 3.2. Iniciando o opencode no Projeto

```bash
docker run -it --rm \
  -v "$(pwd)":/workspace \
  -w /workspace \
  opencode-dev:latest
```

Parâmetros:

- `-it`: terminal interativo (TUI do opencode).
- `--rm`: remove o container ao sair (ambiente efêmero).
- `-v "$(pwd)":/workspace`: monta a pasta atual do host em `/workspace`.
- `-w /workspace`: diretório de trabalho inicial.

Como o `CMD` da imagem é `opencode`, o agente inicia automaticamente. Na raiz do projeto, use `/init` para gerar o `AGENTS.md` e as Skills de `.opencode/skills/` ficam disponíveis (veja [docs/opencode](../opencode/README.md)).

### 3.3. Abrindo um Shell (Sem Iniciar o opencode)

Útil para instalar pacotes extras ou comandos pontuais:

```bash
docker run -it --rm \
  -v "$(pwd)":/workspace \
  -w /workspace \
  opencode-dev:latest bash
```

### 3.4. Executando a Aplicação Django (Porta Exposta)

```bash
docker run -it --rm \
  -p 8000:8000 \
  -v "$(pwd)":/workspace \
  -w /workspace \
  opencode-dev:latest bash
```

Dentro do container:

```bash
python manage.py runserver 0.0.0.0:8000
```

Acesse `http://localhost:8000` no navegador do host.

---

## 4. Passo a Passo do Ambiente de Desenvolvimento

### 4.1. Git

O Git já vem instalado na imagem. Verifique:

```bash
git --version
```

Se estiver usando a imagem oficial do opencode (Alpine Linux), instale sob demanda:

```bash
apk add git
```

Ou, em qualquer imagem Ubuntu sem o Git:

```bash
apt-get update && apt-get install -y git
```

### 4.2. GitHub CLI (gh)

Também já instalado na imagem:

```bash
gh --version
```

Instalação sob demanda (repositório oficial), se necessário:

```bash
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg \
  -o /usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" \
  > /etc/apt/sources.list.d/github-cli.list
apt-get update && apt-get install -y gh
```

Autenticação interativa (o `gh` passa a ser o *credential helper* do Git):

```bash
gh auth login
```

Escolha **GitHub.com → HTTPS → Paste an authentication token** e informe o PAT criado na Seção 4.3. A partir daí, `git push` e `git pull` funcionam sem digitar credenciais.

### 4.3. Criar o Personal Access Token (PAT)

1. No GitHub: avatar → **Settings** → **Developer settings** → **Personal access tokens** → **Fine-grained tokens** → **Generate new token**
   (ou acesse diretamente <https://github.com/settings/personal-access-tokens/new>).
2. **Expiration:** escolha um prazo curto (ex.: 7 dias) — o token é temporário por natureza.
3. **Repository access:** *Only select repositories* → selecione o repositório da disciplina.
4. **Permissions** → *Repository permissions* → **Contents**: **Read and write** (única permissão necessária para commits).
5. **Generate token** e copie o valor (exibido uma única vez).

**Uso temporário e seguro do token:**

```bash
# grave FORA da pasta do repositório, com permissões restritas
umask 077 && printf '%s' 'COLE_O_TOKEN_AQUI' > /workspace/.pat
```

- Nunca copie o token para dentro de um `Dockerfile`, de um arquivo versionado ou do histórico do Git.
- Ao terminar o push, apague o arquivo (`shred -u /workspace/.pat`) e **revogue o token** na página do GitHub.

### 4.4. Identidade do Git (Nome e E-mail)

```bash
cd /workspace/meu-repositorio
git config user.name "Seu Nome"
git config user.email "seu@email.com"
```

Configure **por repositório** (sem `--global`) em máquinas compartilhadas: os dados ficam apenas no `.git/config` daquele projeto.

### 4.5. Commit e Push Seguros

```bash
# 1. Trabalhe sempre sobre o histórico oficial (clone, não ZIP)
git clone https://github.com/<usuario>/<repositorio>.git
cd <repositorio>

# 2. Sincronize e revise antes de commitar
git pull --rebase origin main
git status
git add -p
git diff --cached

# 3. Commits atômicos no padrão Conventional Commits
git commit -m "docs: mensagem descritiva"

# 4. Push com o PAT temporário (o token nunca aparece em argv, URL ou .git/config)
GIT_TERMINAL_PROMPT=0 git -c 'credential.helper=!f() { if test "$1" = get; then printf "username=x-access-token\n"; printf "password=%s\n" "$(cat /workspace/.pat)"; fi; }; f' push origin main
```

Convenção de commits deste repositório (veja [`.opencode/skills/git-github-workflow/SKILL.md`](../../.opencode/skills/git-github-workflow/SKILL.md)):

```
feat: adiciona endpoint de login com JWT
fix: corrige validação de CPF no formulário
docs: atualiza README com instruções de instalação
```

> Se você autenticou com `gh auth login` (Seção 4.2), o passo 4 é apenas `git push origin main`.

### 4.6. Stack Django (python3, python3-dev, python3-venv)

```bash
python3 --version

# ambiente virtual isolado do projeto
python3 -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install django djangorestframework

django-admin startproject projeto .
python manage.py runserver 0.0.0.0:8000
```

- `python3-venv` mantém as dependências de cada projeto separadas do sistema — nada de `pip install` global.
- `python3-dev` é necessário para pacotes com extensões C (`psycopg2-binary`/`psycopg2`, `Pillow`, `lxml`). Para compilá-los, instale também as ferramentas de build:

```bash
apt-get update && apt-get install -y build-essential
```

- Fixe as dependências do projeto em `requirements.txt`:

```bash
pip freeze > requirements.txt
```

---

## 5. Boas Práticas de Segurança

1. **Nunca grave credenciais na imagem:** PAT e chaves privadas jamais entram em `Dockerfiles` nem no repositório.
2. **PAT de escopo mínimo e expiração curta:** apenas permissão de escrita em `Contents`, só no repositório da disciplina, revogado após o uso.
3. **Container efêmero (`--rm`):** credenciais colocadas dentro do container desaparecem com ele; o código permanece no host via bind mount.
4. **Usuário não-root com UID do host:** arquivos gerados no container pertencem ao seu usuário.

---

## 6. Referências

- [Introdução ao opencode](../opencode/README.md) — Skills por disciplina
- [Documentação oficial do opencode](https://opencode.ai/docs)
- [Guia 1: Dev Containers Oficial](guia-devcontainers-oficial.md)
- [Guia 2: Docker CLI Local](guia-docker-cli-local.md)
- [Guia 3: Docker com Interface Gráfica X11](guia-docker-x11-gui.md)
- [GitHub CLI](https://cli.github.com/manual/)
- [Criando fine-grained PATs](https://docs.github.com/pt/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)
