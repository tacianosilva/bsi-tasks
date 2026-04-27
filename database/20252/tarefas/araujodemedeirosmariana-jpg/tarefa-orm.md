# Tarefa - ODBC e ORM

## Linguagem Escolhida
Python

## Links para Scripts e Programas Criados
- [Script ODBC - Conexão com PostgreSQL via ODBC](../../../connections/python/odbc_postgres/)
- [Programa ODBC - Acesso ao AtividadesBD](odbc_connect.py)
- [Programa ORM - Uso do Peewee com AtividadesBD](orm_program.py)
- [Programa ORM - Uso do Peewee com PostgreSQL](../../../connections/python/peewee_postgres/)

## Resumo sobre ODBC
ODBC (Open Database Connectivity) é uma API padrão desenvolvida pela Microsoft para acessar bancos de dados de forma independente de plataforma e linguagem. Em Python, utilizamos bibliotecas como `pyodbc` para estabelecer conexões com bancos de dados através de drivers ODBC. Isso permite executar consultas SQL diretamente, facilitando a integração com sistemas de gerenciamento de banco de dados como PostgreSQL, sem depender de APIs específicas do banco.

## Resumo sobre ORM
ORM (Object-Relational Mapping) é uma técnica que mapeia objetos de uma linguagem de programação orientada a objetos para tabelas em um banco de dados relacional. Em Python, utilizei o framework **Peewee**, que é um ORM leve e expressivo. Ele simplifica a interação com o banco de dados, permitindo definir modelos de dados como classes Python, executar consultas de forma orientada a objetos e gerenciar migrações de esquema. O Peewee suporta vários bancos de dados, incluindo PostgreSQL, e oferece uma sintaxe intuitiva para operações CRUD (Create, Read, Update, Delete).