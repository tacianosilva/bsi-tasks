# Guia 1: Dev Containers Oficial (VS Code + Extensão Dev Containers)

Este guia documenta a **Abordagem Principal e Recomendada** para desenvolvimento em containers Docker no ecossistema de disciplinas do BSI/UFRN.

---

## 1. Visão Geral da Arquitetura Cliente-Servidor

A especificação de **Dev Containers** (desenvolvida pela Microsoft e padronizada pela *Development Containers Specification*) utiliza uma arquitetura cliente-servidor distribuída que separa a interface gráfica do ambiente de execução:

```text
┌─────────────────────────────────────────────────────────┐
│                      MÁQUINA HOST                       │
│                                                         │
│   ┌─────────────────────────────────────────────────┐   │
│   │             VS Code Client (UI)                 │   │
│   │  • Renderização gráfica nativa                  │   │
│   │  • Captura de teclado, atalhos e temas          │   │
│   │  • Aceleração de hardware local                 │   │
│   └───────────────────────▲─────────────────────────┘   │
│                           │ Comunicação IPC / RPC       │
│                           │ via Socket Local / SSH      │
│   ┌───────────────────────▼─────────────────────────┐   │
│   │           Docker Engine / Daemon                │   │
│   └───────────────────────▲─────────────────────────┘   │
└───────────────────────────┼─────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────┐
│                    CONTAINER DOCKER                     │
│                                                         │
│   ┌─────────────────────────────────────────────────┐   │
│   │             VS Code Server (Backend)            │   │
│   │  • Extensões de linguagem (Python, Pylance)     │   │
│   │  • Language Server Protocol (LSP) e Linters     │   │
│   │  • Debugger (Debugpy, GDB, Delve, etc.)         │   │
│   │  • Terminal Integrado (Bash, Zsh)               │   │
│   │  • Runtimes e Ferramentas (Python, asdf, Git)   │   │
│   │  • Código-fonte montado em /workspaces          │   │
│   └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

### Por que esta abordagem é superior?
1. **Desempenho da Interface:** A interface do usuário roda diretamente no sistema operacional do host, garantindo latência zero de digitação e renderização fluida sem sobrecarga de servidores de exibição virtualizados.
2. **Isolamento Completo:** Interpretadores, compiladores, bibliotecas de sistema e extensões de análise estática são instalados exclusivamente no container, não poluindo o sistema operacional do estudante.
3. **Reprodutibilidade:** Toda a equipe e o professor compartilham exatamente o mesmo sistema operacional base, versões de linguagens e extensões do editor definidas no código.

---

## 2. Segurança e Permissões do Git

Um dos maiores desafios no uso de containers para desenvolvimento é o gerenciamento de credenciais do Git sem expor chaves privadas ou deixar resíduos no disco:

- **SSH Agent Forwarding:** O VS Code detecta o agente SSH do host (`ssh-agent`) e repassa o socket de autenticação (`SSH_AUTH_SOCK`) para o container em memória. Suas chaves privadas (`~/.ssh/id_rsa`, `~/.ssh/id_ed25519`) **nunca** são copiadas para a imagem ou filesystem do container.
- **Git Credential Helper Forwarding:** Caso utilize autenticação HTTPS com GitHub, o VS Code repassa os tokens do gerenciador de credenciais do host de forma transparente.
- **Mapeamento de Usuário Não-Root (`vscode`):** A imagem oficial define o usuário `vscode` com UID `1000` e GID `1000`. Isso garante que arquivos criados ou modificados dentro do container pertençam ao seu usuário no host Linux, evitando erros de permissão (`root:root`).

---

## 3. Estrutura de Arquivos do Projeto

Na raiz do seu projeto, deve existir o diretório `.devcontainer/` com dois arquivos fundamentais:

```text
meu-projeto/
├── .devcontainer/
│   ├── Dockerfile
│   └── devcontainer.json
├── src/
├── tests/
└── README.md
```

### 3.1. `Dockerfile` de Referência
Define a base do sistema operacional (Ubuntu 22.04 LTS) e o runtime Python 3.14 via PPA oficial deadsnakes:

```dockerfile
FROM mcr.microsoft.com/devcontainers/base:ubuntu-22.04

ENV DEBIAN_FRONTEND=noninteractive

# Instala pré-requisitos, adiciona PPA deadsnakes e instala Python 3.14
RUN apt-get update && apt-get install -y --no-install-recommends \
    software-properties-common \
    ca-certificates \
    curl \
    gnupg \
    && add-apt-repository ppa:deadsnakes/ppa -y \
    && apt-get update && apt-get install -y --no-install-recommends \
    python3.14-dev \
    python3.14-dbg \
    python3.14-doc \
    python3.14-venv \
    python3-pip \
    && update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.14 1 \
    && update-alternatives --install /usr/bin/python python /usr/bin/python3.14 1 \
    && (python3.14 -m pip --version >/dev/null 2>&1 || curl -sS https://bootstrap.pypa.io/get-pip.py | python3.14) \
    && python3.14 -m pip install --no-cache-dir --upgrade "pip>=25.0,<26.0" \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

USER vscode
```

### 3.2. `devcontainer.json` de Referência
Declara as Dev Container Features (`git` e `asdf`), as extensões recomendadas do VS Code e as configurações do editor:

```json
{
  "name": "Python 3.14 & asdf Dev Container",
  "build": {
    "dockerfile": "Dockerfile"
  },
  "features": {
    "ghcr.io/devcontainers/features/git:1": {},
    "ghcr.io/devcontainers-contrib/features/asdf:1": {}
  },
  "customizations": {
    "vscode": {
      "settings": {
        "python.defaultInterpreterPath": "/usr/bin/python3.14"
      },
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "eamodio.gitlens"
      ]
    }
  },
  "remoteUser": "vscode"
}
```

---

## 4. Passo a Passo: Abrindo o Projeto no Dev Container

### Pré-requisitos no Host
1. **Docker Engine** ou **Docker Desktop** instalado e rodando.
2. **VS Code** instalado.
3. Extensão **Dev Containers** (`ms-vscode-remote.remote-containers`) instalada no VS Code.

### Procedimento
1. Abra o VS Code e clone ou abra a pasta do projeto localmente (`File > Open Folder...`).
2. Uma notificação no canto inferior direito aparecerá:
   > *"Folder contains a Dev Container configuration file. Reopen to run in a container."*
   Clique no botão **Reopen in Container**.
3. Caso a notificação não apareça, pressione `F1` (ou `Ctrl+Shift+P` no Linux/Windows, `Cmd+Shift+P` no macOS) e digite:
   ```text
   Dev Containers: Reopen in Container
   ```
4. O VS Code iniciará a compilação do `Dockerfile` e a injeção das features e do VS Code Server. O progresso detalhado pode ser acompanhado clicando em *Show Log*.
5. Ao concluir, o canto inferior esquerdo do VS Code exibirá uma etiqueta verde indicando:
   `Dev Container: Python 3.14 & asdf Dev Container`.
6. Abra o terminal integrado (`Ctrl+\``) e comprove o ambiente:
   ```bash
   python --version
   pip --version
   asdf --version
   git status
   ```

---

## 5. Gerenciando Plugins do `asdf` sob Demanda

O `asdf` é um gerenciador de múltiplas versões de runtimes extensível por plugins (Node.js, Go, Java, Ruby, etc.).

### 5.1. Instalação Manual Interativa (dentro do container)
Para instalar uma nova linguagem ou ferramenta durante o desenvolvimento:

```bash
# 1. Adicionar o plugin desejado
asdf plugin add nodejs https://github.com/asdf-vm/asdf-nodejs.git

# 2. Listar versões disponíveis
asdf list all nodejs

# 3. Instalar uma versão específica
asdf install nodejs 20.18.0

# 4. Definir a versão como padrão local para o repositório
asdf local nodejs 20.18.0
```

Isso gerará o arquivo `.tool-versions` na raiz do repositório:
```text
nodejs 20.18.0
```
Faça commit do arquivo `.tool-versions` para que todos os membros da equipe utilizem a mesma versão.

### 5.2. Automatizando a Instalação no `devcontainer.json`
Para que novos membros da equipe recebam os plugins e versões automaticamente ao abrir o container, utilize o hook `postCreateCommand` no `devcontainer.json`:

```json
{
  "name": "Python 3.14 & asdf Dev Container",
  "build": {
    "dockerfile": "Dockerfile"
  },
  "features": {
    "ghcr.io/devcontainers/features/git:1": {},
    "ghcr.io/devcontainers-contrib/features/asdf:1": {}
  },
  "postCreateCommand": "asdf plugin add nodejs || true && asdf install nodejs 20.18.0 && asdf global nodejs 20.18.0",
  "customizations": {
    "vscode": {
      "settings": {
        "python.defaultInterpreterPath": "/usr/bin/python3.14"
      },
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "eamodio.gitlens"
      ]
    }
  },
  "remoteUser": "vscode"
}
```

---

## 6. Recompilando o Container após Alterações

Caso modifique o `Dockerfile` ou adicione novas features no `devcontainer.json`:
1. Pressione `F1` (`Ctrl+Shift+P`).
2. Digite e selecione:
   ```text
   Dev Containers: Rebuild Container
   ```
3. Se desejar limpar caches antigos da imagem:
   ```text
   Dev Containers: Rebuild Container Without Cache
   ```
