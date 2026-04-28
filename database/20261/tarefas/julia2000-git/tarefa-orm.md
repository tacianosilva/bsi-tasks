# Tarefa - ODBC e ORM (2026.1)

## Link para prepositório com os códigos em Python para conexão com banco de dados
https://github.com/julia2000-git/BD-estudos-2026

## Resumo sobre ODBC na linguagem Python
O ODBC (_Open Database Connectivity_) é um padrão que permite que aplicações em diversas linguagens (como Python, por exemplo) possam ter acesso a bancos de dados (como o PostgreSQL). Baciamente, trata-se de uma API (_Application Programming Interface_) para acessar SGBDs. Para a conexão, é necessário um _driver_ que faça a intermediação, que consege permitir que o código Python envie comandos SQL.

## Resumo sobre ORM (SQLAlchemy)
ORM (_Object-Relational Mapping_) é uma técnica que mapeia tabelas de bancos de dados relacionais, como o PostgreSQL, para classes e objetos em linguagens de programação, como Python. O SQLAlchemy é uma biblioteca Python que age justamente como uma "ponte" entre Python e PostgreSQL, implementando a técnica ORM, permitindo criação de classes e objetos, consultas e manipulação de dados usando código Python sem utilizar necessariament o SQL puro.