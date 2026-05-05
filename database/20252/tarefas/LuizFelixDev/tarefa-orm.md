# Tarefa - ODBC e ORM (Python)

- [Script SQL Original](../../../scripts/AtividadesBD/postgres/esquema_atividades_creates_tables.sql)
- [Conexão Driver Nativo](./src/database_driver.py)
- [Conexão ORM SQLAlchemy](./src/database_orm.py)

## ODBC em Python
Para a camada de baixo nível, foi utilizado o `psycopg2`. Ele funciona como o driver nativo para PostgreSQL em Python, permitindo a execução de queries manuais e controle direto sobre cursores e transações, assemelhando-se ao comportamento do padrão ODBC.

## ORM em Python
Utilizou-se o `SQLAlchemy`, framework que mapeia tabelas para classes. Ele abstrai a necessidade de escrever SQL para operações CRUD, permitindo que a lógica de negócio lide apenas com objetos Python e relacionamentos tipados.