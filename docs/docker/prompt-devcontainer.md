# Prompt Mestre para Geração de Ambientes Dev Container

Este documento contém o **prompt parametrizável** projetado para orientar assistentes de IA (ou engenheiros de DevOps) na geração da estrutura de arquivos de um ambiente de desenvolvimento padronizado utilizando a especificação **Dev Containers**.

O objetivo deste prompt é coletar as necessidades do projeto e gerar automaticamente os arquivos `.devcontainer/Dockerfile` e `.devcontainer/devcontainer.json` com boas práticas de segurança, isolamento e permissões.

---

## 1. O Prompt Mestre

Copie e utilize o prompt estruturado abaixo ao iniciar a configuração de um novo ambiente:

```text
Atue como um especialista em DevOps e Engenharia de Software.

Preciso que você crie a estrutura de arquivos para o Dev Container (.devcontainer/) de um projeto.

Antes de gerar os arquivos, considere as seguintes definições e requisitos:
1. Especificação: Usar a especificação oficial de Dev Containers (Microsoft / Development Containers).
2. Repositório e Permissões Git:
   - O projeto será baixado do GitHub via clone.
   - O ambiente deve permitir `git commit` e `git push` de forma segura.
   - Nenhuma chave privada (SSH) ou token pessoal deve ser copiado para dentro da imagem ou persistido no container/disco.
   - Deve ser utilizado o encaminhamento nativo de credenciais do VS Code (SSH Agent Forwarding e Git Credential Helper Forwarding).
   - O usuário padrão deve ser não-root (ex: `vscode`, UID 1000) para manter paridade de permissões de arquivos com o host.
3. Stack Base:
   - Sistema Operacional: Ubuntu 22.04 LTS (imagem `mcr.microsoft.com/devcontainers/base:ubuntu-22.04`).
   - Linguagem principal e runtime no Dockerfile: Python 3.14 via PPA deadsnakes, incluindo `python3.14-dev`, `python3.14-dbg`, `python3.14-doc`, `python3.14-venv` e `python3-pip`.
   - `update-alternatives` configurando `python` e `python3` para `/usr/bin/python3.14`.
   - Pip instalado e travado na versão v25 (`pip>=25.0,<26.0`).
4. Dev Container Features (`devcontainer.json`):
   - Git: `ghcr.io/devcontainers/features/git:1`
   - asdf: `ghcr.io/devcontainers-contrib/features/asdf:1` (permitindo instalação sob demanda de novos plugins).
5. Extensões e Configurações do VS Code:
   - Extensões recomendadas: `ms-python.python`, `ms-python.vscode-pylance`, `eamodio.gitlens`.
   - `python.defaultInterpreterPath`: `/usr/bin/python3.14`.
   - `remoteUser`: `vscode`.

Gere a estrutura da pasta `.devcontainer/` com:
1. `Dockerfile` completo, limpo e validado.
2. `devcontainer.json` estritamente válido em formato JSON.
```

---

## 2. Estrutura de Arquivos de Referência Gerada

A aplicação do prompt acima produz os arquivos localizados no repositório em [`docker/devcontainer/`](../../docker/devcontainer/):

### 2.1. `.devcontainer/Dockerfile`
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

### 2.2. `.devcontainer/devcontainer.json`
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

## 3. Segurança e Efemeridade

| Requisito | Como é atendido |
| :--- | :--- |
| **Clone seguro** | Realizado com as credenciais do host sem copiar dados para a imagem. |
| **Commit e Push** | Feito via socket UNIX repassado em memória (`SSH_AUTH_SOCK`). |
| **Sem resíduos locais** | Ao destruir o container (`docker rm`), nenhuma chave privada ou credencial permanece no disco. |
| **Permissões de arquivos** | O usuário `vscode` (UID 1000) evita que arquivos gerados no container fiquem com permissão de `root` no host. |
