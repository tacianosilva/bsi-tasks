# Tarefa - ODBC e ORM

## 1. Scripts SQL

- Script de criação das tabelas: ../esquema_atividades_creates_table.sql
- Script de inserção de dados: ../esquema_atividades_inserts.sql

---

## 2. Ambiente do Banco de Dados

O banco de dados AtividadesBD foi configurado utilizando Docker com PostgreSQL e PgAdmin. Foi criado um banco, usuário e senha para acesso, conforme solicitado na atividade.

---

## 3. Programa utilizando ODBC

Foi desenvolvido um programa em Python utilizando a biblioteca `pyodbc` para conexão com o banco de dados PostgreSQL via ODBC.

### Operações realizadas:

- Inserção de uma nova atividade  
- Atualização do responsável de um projeto  
- Listagem de projetos e suas atividades  

Código: [conexao_odbc.py](conexao_odbc.py)

---

## 4. Programa utilizando ORM

Foi utilizado o framework SQLAlchemy em Python para realizar o acesso ao banco de dados.

### Operações realizadas:

- Inserção de uma nova atividade  
- Atualização do responsável de um projeto  
- Listagem de projetos e suas atividades  

Código: [conexao_orm.py](conexao_orm.py)

---

## 5. Execução e Validação

Os programas foram executados com sucesso, realizando inserção, atualização e consulta de dados no banco.

A validação foi feita no PgAdmin, onde foi possível confirmar:

- Inserção de novas atividades via ODBC e ORM
- Atualização de dados na tabela de projetos
- Listagem correta de projetos e suas atividades

### Exemplo de consulta utilizada para validação

```sql
SELECT p.nome, a.descricao
FROM projeto p
JOIN atividade a ON p.codigo = a.projeto;
```
---

## 6. Resumo sobre ODBC

ODBC (Open Database Connectivity) é uma API padrão que permite que aplicações se conectem a diferentes sistemas de banco de dados de forma independente do SGBD utilizado.

Na linguagem Python, foi utilizada a biblioteca `pyodbc`, permitindo executar comandos SQL diretamente no banco de dados.

---

## 7. Resumo sobre ORM

ORM (Object-Relational Mapping) é uma técnica que permite mapear tabelas do banco de dados para objetos em uma linguagem de programação.

Foi utilizado o framework SQLAlchemy, que facilita o gerenciamento de conexões e execução de operações no banco de dados, tornando o código mais organizado.

Embora seja um ORM, neste trabalho ainda foram utilizados comandos SQL por meio do SQLAlchemy.