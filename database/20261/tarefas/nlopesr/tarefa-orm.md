# Tarefa ORM - AtividadesBD

## Links dos arquivos criados

- README da tarefa: [README.md](./README.md)
- Docker e serviços: [docker-compose.yml](./docker-compose.yml)
- Variáveis de ambiente: [.env.example](./.env.example)
- Script SQL (tabelas): [sql/01_creates_tables.sql](./sql/01_creates_tables.sql)
- Script SQL (dados iniciais): [sql/02_inserts.sql](./sql/02_inserts.sql)
- Programa ODBC (Python): [python_odbc/main.py](./python_odbc/main.py)
- Dependências ODBC: [python_odbc/requirements.txt](./python_odbc/requirements.txt)
- Programa ORM (Python + SQLAlchemy): [python_orm/main.py](./python_orm/main.py)
- Dependências ORM: [python_orm/requirements.txt](./python_orm/requirements.txt)

## Resumo ODBC em Python

ODBC (Open Database Connectivity) é um padrão de acesso a bancos relacionais usando drivers. Em Python, o pacote `pyodbc` permite conectar ao PostgreSQL, MySQL e outros bancos com a mesma interface de código, mudando basicamente a string de conexão e o driver instalado no sistema operacional. Nesta tarefa, ele foi usado para executar SQL direto (INSERT, UPDATE e SELECT com JOIN), controlando transação com `commit` ao final.

## Resumo ORM em Python e framework utilizado

ORM (Object-Relational Mapping) mapeia tabelas do banco para classes da aplicação, reduzindo SQL manual e facilitando manutenção. O framework ORM utilizado foi o SQLAlchemy ORM. Nele, as entidades (`Projeto`, `Atividade`) são classes Python e as operações podem ser feitas com `Session`, `add`, `get` e consultas via `select`/`join`. Isso melhora legibilidade e reaproveitamento de código, principalmente em projetos maiores.

## Passo a passo para executar

1. Suba PostgreSQL + PgAdmin:

```bash
docker compose up -d
```

2. Acesse o PgAdmin em `http://localhost:5050`.

3. Login no PgAdmin:
- Email: `admin@atividades.local`
- Senha: `admin123`

4. No PgAdmin, adicione o servidor PostgreSQL:
- Host: `postgres` (se estiver no container) ou `localhost` (se estiver no host)
- Banco: `AtividadesBD`
- Usuário: `atividades_user`
- Senha: `atividades_pass`

5. Copie `.env.example` para `.env` no diretório `database/20261/tarefas/nlopesr`.

6. Execute o programa ODBC (questão JDBC/ODBC):

```bash
cd python_odbc
pip install -r requirements.txt
python main.py
```

7. Execute o programa ORM:

```bash
cd ../python_orm
pip install -r requirements.txt
python main.py
```

## Comandos SQL realizados pelos programas

- Inserir uma atividade em algum projeto
- Atualizar o líder (responsável) de algum projeto
- Listar todos os projetos e suas atividades

Os dois programas (`python_odbc/main.py` e `python_orm/main.py`) executam essas três operações.
