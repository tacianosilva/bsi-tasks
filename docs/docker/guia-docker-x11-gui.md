# Guia 3: Docker com Interface Gráfica X11 (VS Code no Container)

Este guia documenta a **Abordagem com Interface Gráfica (GUI) via X11**, na qual o próprio editor (VS Code) e suas dependências gráficas são instalados e executados inteiramente dentro do container Docker, sendo renderizados na tela da máquina host através do protocolo de exibição do **X Window System (X11)**.

---

## 1. Cenário de Uso e Arquitetura

Esta abordagem é comumente utilizada quando:
1. **O host possui restrições severas de instalação:** Ambientes compartilhados (como laboratórios acadêmicos) onde o discente não possui permissão de `root`/administrador no host para instalar pacotes ou IDEs.
2. **Encapsulamento total:** Quando se deseja empacotar a IDE inteira, extensões pré-configuradas e ferramentas em uma única imagem distribuível.
3. **Ambiente padronizado de avaliação:** Para correções automatizadas ou sessões de laboratório com interface visual garantidamente idêntica.

```text
┌────────────────────────────────────────────────────────┐
│                      MÁQUINA HOST                      │
│                                                        │
│   ┌────────────────────────────────────────────────┐   │
│   │            Servidor X11 do Host                │   │
│   │  Socket UNIX: /tmp/.X11-unix/X0                │   │
│   │  Autenticação: xhost +local:docker ou Xauth    │   │
│   └───────────────────────▲────────────────────────┘   │
│                           │ Montagem de Socket         │
│                           │ (-v /tmp/.X11-unix)        │
│   ┌───────────────────────▼────────────────────────┐   │
│   │               CONTAINER DOCKER                 │   │
│   │                                                │   │
│   │   [ VS Code Binário Oficial (code) ]           │   │
│   │   • Bibliotecas GTK3, X11, Cairo, Pango        │   │
│   │   • Runtime Python, ferramentas e código       │   │
│   │   • Renderiza janelas através do socket X11    │   │
│   │                                                │   │
│   └────────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────┘
```

---

## 2. Dockerfile com Suporte a GUI e VS Code

Este `Dockerfile` adiciona as dependências de interface gráfica (X11, GTK, D-Bus, fontes e bibliotecas do Electron) e instala o pacote binário oficial do VS Code (`code`).

### Arquivo: `Dockerfile`
```dockerfile
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# 1. Instala dependências básicas, repositórios e bibliotecas gráficas para X11/Electron
RUN apt-get update && apt-get install -y --no-install-recommends \
    software-properties-common \
    ca-certificates \
    curl \
    gnupg \
    git \
    libasound2 \
    libatk1.0-0 \
    libcairo2 \
    libcups2 \
    libdbus-1-3 \
    libdrm2 \
    libgbm1 \
    libgdk-pixbuf2.0-0 \
    libglib2.0-0 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libpango-1.0-0 \
    libsecret-1-0 \
    libx11-6 \
    libx11-xcb1 \
    libxcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxi6 \
    libxkbfile1 \
    libxrandr2 \
    libxrender1 \
    libxshmfence1 \
    libxss1 \
    libxtst6 \
    fonts-liberation \
    xdg-utils \
    && rm -rf /var/lib/apt/lists/*

# 2. Adiciona o repositório oficial da Microsoft e instala o VS Code
RUN curl -sSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /etc/apt/keyrings/packages.microsoft.gpg \
    && echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list \
    && apt-get update && apt-get install -y --no-install-recommends code \
    && rm -rf /var/lib/apt/lists/*

# 3. Adiciona PPA deadsnakes e instala Python 3.14
RUN add-apt-repository ppa:deadsnakes/ppa -y \
    && apt-get update && apt-get install -y --no-install-recommends \
    python3.14-dev \
    python3.14-venv \
    python3-pip \
    && update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.14 1 \
    && update-alternatives --install /usr/bin/python python /usr/bin/python3.14 1 \
    && python3.14 -m pip install --no-cache-dir --upgrade "pip>=25.0,<26.0" \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# 4. Cria usuário não-root com UID/GID para compatibilidade com o Host
ARG USERNAME=developer
ARG USER_UID=1000
ARG USER_GID=1000

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m -s /bin/bash $USERNAME

USER $USERNAME
WORKDIR /workspace

# Comando padrão: inicia o VS Code com espera em primeiro plano
CMD ["code", "--wait", "--no-sandbox", "/workspace"]
```

---

## 3. Configuração de Permissões e Execução no Host

Para que o container consiga se conectar ao servidor X11 do host, são necessários dois passos no sistema operacional host (Linux):

### 3.1. Liberar Acesso ao Servidor X11
No terminal do host, execute:

```bash
# Permite que containers Docker locais enviem janelas para a sua tela
xhost +local:docker
```

> **Nota de Segurança:** O comando `xhost +local:docker` restringe o acesso aos processos locais pertencentes ao Docker, sendo significativamente mais seguro do que liberar acesso irrestrito (`xhost +`). Ao encerrar sua sessão de trabalho, você pode revogar a permissão com:
> ```bash
> xhost -local:docker
> ```

---

### 3.2. Construir a Imagem
```bash
docker build \
  --build-arg USER_UID=$(id -u) \
  --build-arg USER_GID=$(id -g) \
  -t vscode-x11:latest .
```

---

### 3.3. Executar o Container com Mapeamento Gráfico
Execute o comando abaixo para iniciar o VS Code dentro do container e renderizá-lo na sua área de trabalho:

```bash
docker run -it --rm \
  --net=host \
  --ipc=host \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v "$(pwd):/workspace" \
  -v "$HOME/.config/Code-Docker:/home/developer/.config/Code" \
  -w /workspace \
  vscode-x11:latest
```

### Explicação dos Parâmetros:
- `-e DISPLAY=$DISPLAY`: Passa a variável que indica qual display X11 utilizar (geralmente `:0` ou `:1`).
- `-v /tmp/.X11-unix:/tmp/.X11-unix`: Monta o socket UNIX de comunicação entre o cliente gráfico e o servidor X11.
- `--net=host` e `--ipc=host`: Melhoram a performance e a comunicação compartilhada de memória inter-processos com o servidor X11.
- `-v "$(pwd):/workspace"`: Mapeia o código do projeto para dentro do workspace do container.
- `-v "$HOME/.config/Code-Docker:..."`: Volume para persistir configurações, histórico e extensões do VS Code sem misturar com sua instalação local.

---

## 4. Comparativo: Vantagens e Limitações

| Aspecto | Dev Containers Oficial (Guia 1) | Docker CLI (Guia 2) | Docker X11 GUI (Guia 3) |
| :--- | :--- | :--- | :--- |
| **Instalação no Host** | Requer VS Code instalado no host | Requer qualquer editor no host | Apenas Docker e X11 no host |
| **Renderização Gráfica** | Nativa no Host (fluida e rápida) | Nativa no Host (fluida e rápida) | Encaminhada via socket X11 (pode ter latência) |
| **Aceleração 3D / GPU** | Nativa | Nativa | Requer flags `--device /dev/dri` adicionais |
| **Segurança do Git** | Transparente (Agent Forwarding) | Requer repasse de socket manual | Requer repasse de socket manual |
| **Consumo de Memória** | Médio | Muito Baixo | Alto (IDE gráfica inteira no container) |
