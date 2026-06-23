# Relatório de Atividade: ODBC e ORM

## Links para Artefatos produzidos
- [Código Fonte: Conexão ODBC (Questão 5)](./questao5.py)
- [Código Fonte: Conexão ORM (Questão 6)](./questao6.py)

## Resumo sobre ODBC (Open Database Connectivity) em Python
O ODBC é um padrão de interface (API) que permite que aplicações acessem diferentes sistemas de gerenciamento de banco de dados (SGBD) de forma uniforme, independentemente do software ou sistema operacional. Em Python, o uso do ODBC é comumente realizado através da biblioteca `pyodbc`.

**Funcionamento:**
O ODBC atua como uma camada intermediária. A aplicação Python envia comandos SQL através de um Driver Manager, que utiliza um Driver específico para o banco de dados (como o driver do PostgreSQL) para traduzir e executar a consulta. É ideal para situações onde a aplicação precisa de alta performance em consultas brutas ou precisa se conectar a bancos legados.

## Resumo sobre ORM (Object-Relational Mapping) em Python
O ORM é uma técnica de desenvolvimento que permite abstrair a camada de banco de dados, transformando tabelas em classes e registros em objetos da linguagem de programação. Isso elimina a necessidade de escrever SQL manualmente para a maioria das operações de CRUD (Create, Read, Update, Delete).

**Framework Utilizado: SQLAlchemy**
Para esta atividade, foi utilizado o **SQLAlchemy**, um dos frameworks ORM mais robustos e flexíveis do ecossistema Python.
- **Vantagens:** Aumenta a produtividade, facilita a manutenção, oferece proteção nativa contra SQL Injection e permite a troca de SGBD com mudanças mínimas de configuração. Diferente de escrever strings de SQL puro (como no ODBC), o SQLAlchemy permite manipular os dados diretamente através de atributos de objetos Python.
- **Exemplo Prático:** Em vez de executar `cursor.execute("UPDATE projeto SET responsavel = 1")`, buscamos o objeto e alteramos sua propriedade diretamente com `projeto_alvo.responsavel = 1` seguido de um `session.commit()`.