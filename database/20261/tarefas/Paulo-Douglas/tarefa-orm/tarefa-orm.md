# Tarefa ORM — AtividadesBD

Trabalho de acesso a banco de dados em **Python**, usando duas abordagens contra o mesmo banco PostgreSQL:

1. Acesso por **driver direto** (psycopg2 — equivalente ao papel do ODBC/JDBC).
2. Acesso por **framework ORM** (SQLAlchemy).

Toda a infraestrutura (PostgreSQL, PgAdmin e a aplicação Python) sobe via Docker Compose.

---

## Estrutura do projeto

```
tarefa-orm/
├── docker-compose.yml          # PostgreSQL + PgAdmin + app Python
├── Dockerfile                  # imagem da aplicação Python
├── requirements.txt            # dependências Python
├── tarefa-orm.md               # este arquivo
├── sql/
│   ├── 01_create_tables.sql    # DDL do esquema AtividadesBD
│   └── 02_inserts.sql          # povoamento inicial
├── scripts/
│   └── conexao_psycopg2.py     # programa com driver direto
└── orm/
    ├── models.py               # modelos SQLAlchemy
    └── main_orm.py             # programa com ORM
```

## Links para os scripts e programas

- Scripts SQL
  - [sql/01_create_tables.sql](./sql/01_create_tables.sql) — criação das tabelas
  - [sql/02_inserts.sql](./sql/02_inserts.sql) — povoamento inicial
- Programa com driver direto (questão 3 e 4)
  - [scripts/conexao_psycopg2.py](./scripts/conexao_psycopg2.py)
- Programa com ORM (questão 5)
  - [orm/models.py](./orm/models.py) — modelos
  - [orm/main_orm.py](./orm/main_orm.py) — execução das operações
- Infraestrutura
  - [docker-compose.yml](./docker-compose.yml)
  - [Dockerfile](./Dockerfile)
  - [requirements.txt](./requirements.txt)

---

## Resumo sobre ODBC em Python

ODBC (*Open Database Connectivity*) é uma API padrão criada pela Microsoft no início dos anos 90 para que aplicações possam acessar diferentes SGBDs — PostgreSQL, MySQL, SQL Server, Oracle, etc. — usando uma única interface. O programa fala com um *driver manager*, que carrega o driver específico do banco. Trocar o banco passa a ser, idealmente, só trocar a *connection string*.

Em Python, o caminho clássico para usar ODBC é a biblioteca **pyodbc**, que implementa a [PEP 249 — Python Database API Specification v2.0](https://peps.python.org/pep-0249/). O fluxo é sempre o mesmo: abrir uma conexão, criar um cursor, executar SQL com `execute()`, recuperar resultados com `fetchone()`/`fetchall()`, e dar `commit()` ou `rollback()`. Tudo é feito com SQL escrito à mão.

Neste trabalho, em vez de pyodbc + driver ODBC do PostgreSQL, foi escolhido o **psycopg2**, que é o driver nativo PostgreSQL para Python. Ele também segue a PEP 249 (mesmo padrão `connect → cursor → execute`), porém fala diretamente o protocolo do PostgreSQL, sem passar pela camada ODBC. Para o aluno, o estilo de uso é praticamente idêntico ao de pyodbc/JDBC: SQL escrito manualmente, parâmetros passados com `%s`, controle explícito de transação. A diferença é que ele é mais rápido e mais comum no ecossistema Python para PostgreSQL.

Resumindo o paralelo:

| Mundo Java | Mundo Python (genérico) | Mundo Python + PostgreSQL |
|---|---|---|
| JDBC | ODBC + pyodbc | psycopg2 |
| `Connection` / `Statement` / `ResultSet` | `connection` / `cursor` / `fetch*` | `connection` / `cursor` / `fetch*` |

Por isso o programa em [scripts/conexao_psycopg2.py](./scripts/conexao_psycopg2.py) representa, no espírito do enunciado, o item "ODBC/JDBC" da linguagem escolhida: acesso de baixo nível, com SQL explícito.

---

## Resumo sobre ORM em Python (SQLAlchemy)

ORM (*Object-Relational Mapping*) é uma técnica que mapeia tabelas do banco de dados para classes da linguagem e linhas para objetos. Em vez de escrever `INSERT INTO atividade ...`, o programador cria uma instância `Atividade(...)` e adiciona à sessão; em vez de `SELECT * FROM projeto WHERE nome = 'APF'`, escreve `select(Projeto).where(Projeto.nome == "APF")`. O ORM cuida de gerar o SQL, executar e converter os resultados de volta em objetos.

As principais vantagens são: menos SQL repetitivo, código mais próximo do domínio, validação de tipos, navegação por relacionamentos (`projeto.atividades` em vez de um JOIN escrito manualmente) e portabilidade entre SGBDs. As principais desvantagens são: curva de aprendizado, problemas de performance escondidos como o famoso *N+1 queries*, e perda de controle fino sobre o SQL gerado em consultas mais complexas.

### Framework escolhido: SQLAlchemy

[**SQLAlchemy**](https://www.sqlalchemy.org/) é o ORM mais usado em Python. Tem duas camadas:

- **SQLAlchemy Core** — um construtor de SQL orientado a expressões (mais baixo nível).
- **SQLAlchemy ORM** — o mapeamento objeto-relacional propriamente dito, construído por cima do Core.

Foi usada a versão **2.x** com a sintaxe declarativa moderna, baseada em type hints (`Mapped[int]`, `mapped_column(...)`). Os principais conceitos aplicados no projeto:

- `DeclarativeBase` — classe base para todos os modelos (ver [orm/models.py](./orm/models.py)).
- `Mapped` + `mapped_column` — declaração tipada das colunas.
- `relationship` + `back_populates` — navegação entre `Projeto` e `Atividade`, e entre `Projeto` e `Funcionario` (responsável).
- `Session` — unidade de trabalho que agrupa as operações em uma transação.
- `select(...).options(selectinload(...))` — *eager loading* das atividades de cada projeto, para evitar o problema de N+1 queries na listagem.

A escolha do SQLAlchemy se justifica por ser o padrão de facto da comunidade Python, ter excelente documentação, suportar PostgreSQL nativamente (via psycopg2 internamente, com a URL `postgresql+psycopg2://...`) e ser a base de outras ferramentas populares como Alembic (migrations) e FastAPI (em conjunto com SQLModel).

---

## Como rodar

### 1. Subir os containers

```bash
docker compose up -d --build
```

Isto sobe três containers:
- `atividades_postgres` — PostgreSQL 16 na porta `5432`, já com o esquema e os dados criados (os scripts em `sql/` são executados automaticamente na primeira inicialização pelo *initdb* do PostgreSQL).
- `atividades_pgadmin` — PgAdmin 4 acessível em `http://localhost:5050` (login `admin@atividades.com` / senha `senha123`).
- `atividades_app` — container Python com `psycopg2` e `SQLAlchemy` prontos.

### 2. Acessar o PgAdmin (opcional)

Abrir `http://localhost:5050`, fazer login e cadastrar um servidor com:

- Host: `postgres`
- Porta: `5432`
- Banco: `atividade_db`
- Usuário: `admin_atividades`
- Senha: `senha123`

### 3. Executar o programa com driver direto (questões 3 e 4)

```bash
docker compose exec app python /app/scripts/conexao_psycopg2.py
```

Saída esperada (resumida):
- Insere uma nova atividade no projeto APF.
- Atualiza o líder do projeto BD para o funcionário de código 4 (Josefa).
- Lista todos os projetos e suas atividades.

### 4. Executar o programa com ORM (questão 5)

```bash
docker compose exec app python /app/orm/main_orm.py
```

Saída esperada (resumida):
- Insere outra atividade no projeto APF (via objeto `Atividade(...)`).
- Atualiza o responsável do projeto Monitoria para o funcionário de código 3 (Maria).
- Lista todos os projetos e suas atividades, com nome do responsável.

### 5. Derrubar tudo

```bash
docker compose down            # mantém os dados
docker compose down -v         # apaga o volume do PostgreSQL também
```

---

## Credenciais (resumo)

| Recurso | Valor |
|---|---|
| Banco | `atividade_db` |
| Usuário do banco | `admin_atividades` |
| Senha do banco | `senha123` |
| Host (de fora do Docker) | `localhost:5432` |
| Host (dentro do Docker) | `postgres:5432` |
| PgAdmin | `http://localhost:5050` |
| Login PgAdmin | `admin@atividades.com` / `senha123` |
