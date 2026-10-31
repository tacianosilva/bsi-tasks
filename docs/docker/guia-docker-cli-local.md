# Guia 2: Docker CLI Local (Abordagem Híbrida Host + Container)

Este guia documenta a **Abordagem Híbrida**, na qual o estudante ou desenvolvedor utiliza seu editor de texto local (VS Code, Neovim, Sublime Text, IntelliJ, etc.) instalado diretamente na máquina host, enquanto todo o ambiente de compilação, execução e testes roda isoladamente dentro de um container Docker gerenciado via linha de comando (CLI).

---

## 1. Como Funciona a Abordagem Híbrida

Neste modelo, o desenvolvimento ocorre com separação clara de responsabilidades:
- **Host (Máquina Local):** Responsável pela edição de código, navegação no sistema de arquivos local e interface gráfica do editor.
- **Container Docker:** Responsável pela instalação de dependências do sistema operacional, execução de testes unitários, servidores web e comandos de build.
- **Sincronização Bidirecional via Bind Mount (`-v`):** A pasta do projeto no host é montada dentro do container. Qualquer arquivo salvo no editor do host é imediatamente refletido dentro do container e vice-versa.

```text
┌────────────────────────────────────────────────────────┐
│                      MÁQUINA HOST                      │
│                                                        │
│   [ VS Code / Neovim / Editor Local ]                  │
│               │                                        │
│   Edita arquivos no disco local: ~/meu-projeto/        │
│               │                                        │
│               ▼  Bind Mount (-v $(pwd):/app)           │
│   ┌────────────────────────────────────────────────┐   │
│   │               CONTAINER DOCKER                 │   │
│   │                                                │   │
│   │   Executa comandos em /app:                    │   │
│   │   • pytest                                     │   │
│   │   • python main.py                             │   │
│   │   • pip install ...                            │   │
│   │                                                │   │
│   └────────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────┘
```

---

## 2. Dockerfile Simplificado para Execução

Diferente do Dev Containers da Microsoft, esta imagem não necessita de pacotes do VS Code Server, agentes auxiliares ou bibliotecas gráficas. Ela foca exclusivamente nas dependências mínimas do runtime.

### Arquivo: `Dockerfile`
```dockerfile
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# Instala ferramentas básicas e Python 3
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    ca-certificates \
    curl \
    git \
    software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa -y \
    && apt-get update && apt-get install -y --no-install-recommends \
    python3.14-dev \
    python3.14-venv \
    python3-pip \
    && update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.14 1 \
    && update-alternatives --install /usr/bin/python python /usr/bin/python3.14 1 \
    && python3.14 -m pip install --no-cache-dir --upgrade "pip>=25.0,<26.0" \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Cria usuário não-root com UID configurável
ARG USERNAME=developer
ARG USER_UID=1000
ARG USER_GID=1000

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m -s /bin/bash $USERNAME

WORKDIR /app

USER $USERNAME

CMD ["bash"]
```

---

## 3. Comandos de Build e Execução

### 3.1. Construindo a Imagem Docker
Na raiz do projeto (onde está localizado o `Dockerfile`):

```bash
docker build \
  --build-arg USER_UID=$(id -u) \
  --build-arg USER_GID=$(id -g) \
  -t meu-projeto-cli:latest .
```

> **Por que usar `--build-arg USER_UID=$(id -u)`?**
> Isso garante que o usuário interno do container tenha o mesmo UID numérico do seu usuário no Linux/macOS. Assim, qualquer arquivo, cache (`__pycache__`) ou relatório de testes gerado dentro do container pertencerá a você no host, sem conflitos de permissão de `root`.

---

### 3.2. Abrindo uma Sessão Interativa de Terminal
Para abrir um shell interativo conectado ao container com a pasta do projeto montada:

```bash
docker run -it --rm \
  -v "$(pwd):/app" \
  -w /app \
  meu-projeto-cli:latest
```

Parâmetros utilizados:
- `-it`: Aloca um terminal pseudo-TTY interativo.
- `--rm`: Remove o container temporário automaticamente ao finalizar a sessão (evita acúmulo de containers parados).
- `-v "$(pwd):/app"`: Mapeia o diretório atual do host para `/app` no container.
- `-w /app`: Define `/app` como diretório inicial de trabalho.

---

### 3.3. Executando Comandos Diretamente (Sem Abrir o Shell)
Você pode executar comandos pontuais sem manter um terminal aberto, ideal para scripts ou atalhos:

```bash
# Executar a suíte de testes
docker run --rm -v "$(pwd):/app" -w /app meu-projeto-cli:latest pytest tests/

# Executar verificação de cobertura
docker run --rm -v "$(pwd):/app" -w /app meu-projeto-cli:latest pytest --cov=src tests/

# Executar a aplicação
docker run --rm -v "$(pwd):/app" -w /app meu-projeto-cli:latest python main.py
```

---

### 3.4. Expondo Portas de Redes (para APIs e Aplicações Web)
Caso sua aplicação execute um servidor HTTP (ex.: FastAPI, Flask, Django):

```bash
docker run -it --rm \
  -p 8000:8000 \
  -v "$(pwd):/app" \
  -w /app \
  meu-projeto-cli:latest python -m uvicorn app:main --host 0.0.0.0 --port 8000 --reload
```

Acesse no navegador da máquina host em `http://localhost:8000`.

---

### 3.5. Encaminhamento de Credenciais Git no Terminal Docker
Se precisar fazer `git push` ou `git pull` a partir de dentro do container:

```bash
docker run -it --rm \
  -v "$(pwd):/app" \
  -w /app \
  -v "$SSH_AUTH_SOCK:/ssh-agent" \
  -e SSH_AUTH_SOCK=/ssh-agent \
  meu-projeto-cli:latest
```

Isso repassa o socket do seu agente SSH local para dentro do container de forma temporária, sem que a chave privada seja exposta ou gravada em disco.

---

## 4. Comparativo: Vantagens e Limitações

| Vantagens | Limitações |
| :--- | :--- |
| **Leveza:** Não consome recursos com servidores de extensão do VS Code dentro do container. | **Sem integração visual direta:** Linters e autocomplete do editor local exigem interpretador local ou configuração de LSP remoto. |
| **Independência de Editor:** O desenvolvedor pode usar qualquer editor (Vim, Helix, Emacs, VS Code, Fleet). | **Depuração:** Para usar breakpoints gráficos no VS Code, requer configuração de *Remote Debugging* (ex.: `debugpy.listen()`). |
| **Fidelidade com CI/CD:** Os comandos executados no container reproduzem exatamente os passos de um workflow do GitHub Actions. | **Comandos manuais:** Exige que o usuário execute comandos `docker run` no terminal. |
