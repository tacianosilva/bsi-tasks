---
name: docker-sgbd
description: Use ao executar SGBDs com Docker nas disciplinas de Banco de Dados e Programação Web do BSI/UFRN.
---

# Docker para SGBDs

## Perfil

Execução de Sistemas Gerenciadores de Banco de Dados via containers Docker
para atividades de desenvolvimento e aprendizado.

## SGBDs disponíveis no repositório

| SGBD | Diretório |
|---|---|
| PostgreSQL | `database/docker/postgres/` |
| MySQL | `database/docker/mysql/` |
| MariaDB | `database/docker/mariadb/` |
| MongoDB | `database/docker/mongodb/` |

## Comandos básicos

```bash
docker compose up -d
docker compose down
docker compose logs
docker ps
```

## Conexão

Após iniciar o container, conectar usando as credenciais definidas no
arquivo `docker-compose.yml` de cada SGBD.

Exemplos de conexão em:
- `database/connections/java/jdbc/`
- `database/connections/java/spring-data-jpa/`
- `database/connections/python/peewee_postgres/`
- `database/connections/python/mongodb/`

## Referências

- `database/docker/` — tutoriais por SGBD
- `lessons/dev-web-django.md` — aula 02 sobre Docker
