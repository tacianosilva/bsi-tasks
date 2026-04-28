# Relatório de Atividade: ODBC e ORM

## Links para Artefatos
- [Scripts SQL de Criação e Carga](vou colocar depois)
- [Código Fonte da Aplicação (Exemplo)](vou colocar depois)

## Resumo sobre ODBC (Open Database Connectivity) em Python
O ODBC é um padrão de interface (API) que permite que aplicações acessem diferentes sistemas de gerenciamento de banco de dados (SGBD) de forma uniforme, independentemente do software ou sistema operacional. Em Python, o uso do ODBC é comumente realizado através da biblioteca `pyodbc`.

**Funcionamento:**
O ODBC atua como uma camada intermediária. A aplicação Python envia comandos SQL através de um Driver Manager, que utiliza um Driver específico para o banco de dados (como o driver do PostgreSQL) para traduzir e executar a consulta. É ideal para situações onde a aplicação precisa de alta performance em consultas brutas ou precisa se conectar a legados onde não há um driver nativo moderno.

## Resumo sobre ORM (Object-Relational Mapping) e Django
O ORM é uma técnica de desenvolvimento que permite abstrair a camada de banco de dados, transformando tabelas em classes e registros em objetos da linguagem de programação. Isso elimina a necessidade de escrever SQL manualmente para a maioria das operações de CRUD (Create, Read, Update, Delete).

**Framework Utilizado: Django ORM**
No ecossistema Python, o **Django ORM** é um dos mais robustos. Ele utiliza o padrão *Active Record*, onde cada modelo definido em `models.py` representa uma tabela.
- **Vantagens:** Aumenta a produtividade, facilita a manutenção, oferece proteção nativa contra SQL Injection e permite a troca de SGBD (ex: de SQLite para PostgreSQL) com mudanças mínimas de configuração.
- **Exemplo:** Em vez de `SELECT * FROM filmes`, utilizamos `Filme.objects.all()`.