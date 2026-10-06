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
