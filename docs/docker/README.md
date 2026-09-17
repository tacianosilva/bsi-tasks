# Ambientes de Desenvolvimento com Docker e Dev Containers

Este diretório contém a documentação e os guias práticos para utilização de containers Docker no desenvolvimento de projetos e atividades acadêmicas do curso de Bacharelado em Sistemas de Informação (BSI/UFRN — CERES/Caicó).

O objetivo é assegurar ambientes de execução padronizados, reprodutíveis, seguros e isolados para as diversas disciplinas (Teste de Software, Banco de Dados, Linguagens de Programação, etc.), eliminando problemas de divergência entre sistemas operacionais e versões de interpretadores.

---

## 📚 Guias Disponíveis

Disponibilizamos **três abordagens complementares** para atender a diferentes perfis de desenvolvimento, ferramentas e restrições de infraestrutura:

| Guia | Abordagem | Ferramentas | Cenário de Uso Recomendado |
| :--- | :--- | :--- | :--- |
| **[Guia 1: Dev Containers Oficial](guia-devcontainers-oficial.md)** | **Principal (Recomendada)** | VS Code + Dev Containers | Padrão da indústria. Interface nativa no host, backend e ferramentas isolados no container. Encaminhamento seguro de credenciais Git (SSH Agent / Credential Helper). |
| **[Guia 2: Docker CLI Local](guia-docker-cli-local.md)** | **Híbrida** | Terminal + Docker Volumes (`-v`) | Para desenvolvedores que utilizam terminal puro, Neovim, Vim, Emacs ou scripts de CI/CD locais. Edição de código no host e execução sob demanda. |
| **[Guia 3: Docker com Interface Gráfica X11](guia-docker-x11-gui.md)** | **GUI no Container** | X11 / GTK + VS Code no container | Ambientes de laboratório ou máquinas compartilhadas com permissões restritas no host onde não é viável instalar IDEs localmente. |

---

## 🤖 Prompt para Assistentes de IA

Para gerar novos ambientes personalizados para outras linguagens e stacks utilizando assistentes de IA (ChatGPT, Claude, Gemini, Opencode), consulte o:
- **[Prompt Mestre para Dev Containers](prompt-devcontainer.md)**: Prompt pronto e estruturado que gera o `Dockerfile` e `devcontainer.json` solicitando informações da stack e aplicando as regras de segurança e permissões Git.

---

## 🛠️ Templates e Modelos Executáveis

Os arquivos de configuração e `Dockerfiles` prontos para cópia ou uso direto em seus projetos estão organizados na pasta raiz [`docker/`](../../docker/):

- **[`docker/devcontainer/`](../../docker/devcontainer/)**: Template pronto contendo `Dockerfile` e `devcontainer.json`. Pode ser copiado diretamente para a raiz de qualquer projeto como `.devcontainer/`. Inclui Python 3.14, `pip>=25`, `asdf` e suporte a extensões do VS Code.
- **[`docker/cli-local/`](../../docker/cli-local/)**: `Dockerfile` simplificado e otimizado para compilação e execução via linha de comando sem sobrecarga de IDE.
- **[`docker/x11-gui/`](../../docker/x11-gui/)**: `Dockerfile` com suporte completo ao servidor de exibição X11, bibliotecas GTK e pacote oficial do VS Code instalado.

---

## 🔒 Boas Práticas de Segurança com Git

Em todas as abordagens:
1. **Nunca grave credenciais na imagem:** Chaves privadas SSH e tokens de acesso pessoal (PAT) **jamais** devem ser copiados para dentro de `Dockerfiles` ou comitados no repositório.
2. **Utilize repasse de credenciais em memória:** O VS Code Dev Containers utiliza SSH Agent Forwarding e Credential Helper de forma transparente, mantendo as chaves na memória do host.
3. **Mapeamento de Usuário Não-Root:** Todos os templates configuram usuário não-root (`vscode` ou `developer`) com UID/GID `1000`, evitando que arquivos gerados dentro do container fiquem travados como `root` no host Linux.
