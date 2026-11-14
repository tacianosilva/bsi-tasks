# Tarefa 03: Docker Compose, MariaDB e Administração de SGBD

- **Aluno:** Daniel Mariz da Silva
- **Username GitHub:** danielmrz7
- **Repositório Pessoal:** https://github.com/danielmrz7/tarefa03-docker.git

---

## 1. Respostas Dissertativas

### 1. Quais as vantagens de utilizar Docker Compose para gerenciar um SGBD como o MariaDB?
O Docker Compose permite automatizar e padronizar o ambiente de desenvolvimento através de infraestrutura como código (IaC). Em vez de instalar o MariaDB e clientes de gerenciamento diretamente no sistema operacional, o Docker Compose gerencia a criação de containers isolados, mapeamento de redes internas, gerenciamento de volumes e execução automática de scripts de inicialização (`setup.sql`) com um único comando (`docker compose up`).

### 2. Como funciona a persistência de dados no container do MariaDB?
A persistência de dados é mantida através de **Volumes Gerenciados do Docker** (especificados na cláusula `volumes` do `docker-compose.yml`). O diretório interno `/var/lib/mysql` do container MariaDB é mapeado para um volume persistente no host (`mariadb_data`). Assim, mesmo que o container seja parado, removido ou recriado, os dados do banco de dados continuam intactos.

---

## 2. Evidências Práticas

### Status dos Containers em Execução (`docker ps`)
```text
CONTAINER ID   IMAGE                     COMMAND                  CREATED         STATUS         PORTS                    NAMES
db8f7d20f72a   dbeaver/cloudbeaver:lat…   "./launch-product.sh"    2 minutes ago   Up 2 minutes   0.0.0.0:8080->8978/tcp   cloudbeaver
fabae611faf0   mariadb:latest            "docker-entrypoint.s…"   2 minutes ago   Up 2 minutes   0.0.0.0:3306->3306/tcp   mariadb-server
