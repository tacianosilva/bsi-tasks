# Tarefa - ODBC e ORM (2026.1)

## Link para prepositório com os códigos em Python para conexão com banco de dados

Link do repositório: https://github.com/julia2000-git/BD-estudos-2026.git

A estrutura do repositório é a seguinte: 
* Repositório **BD-estudos-2026** -> pasta 20261 -> pasta tarefas -> pasta tarefa02
* Em /tarefa-02, encontram-se os seguintes arquivos
    * connection.py  (conexão com banco de dados por ODBC)
    * connection-orm.py  (conexão com banco de dados por ORM)
    * esquema_create_tables.sql  (criação de tabelas segundo exemplos da pasta scripts/AtividadesBD/postgres)
    * esquema_inserts_data.sql  (inserção de dados segundo exemplos da pasta scripts/AtividadesBd/postgres)


## Resumo sobre ODBC na linguagem Python
O ODBC (_Open Database Connectivity_) é um padrão que permite que aplicações em diversas linguagens (como Python, por exemplo) possam ter acesso a bancos de dados (como o PostgreSQL). Baciamente, trata-se de uma API (_Application Programming Interface_) para acessar SGBDs. Para a conexão, é necessário um _driver_ que faça a intermediação, que consege permitir que o código Python envie comandos SQL.

## Resumo sobre ORM (SQLAlchemy)
ORM (_Object-Relational Mapping_) é uma técnica que mapeia tabelas de bancos de dados relacionais, como o PostgreSQL, para classes e objetos em linguagens de programação, como Python. O SQLAlchemy é uma biblioteca Python que age justamente como uma "ponte" entre Python e PostgreSQL, implementando a técnica ORM, permitindo criação de classes e objetos, consultas e manipulação de dados usando código Python sem utilizar necessariamente o SQL puro.