# Tarefa Individual - ODBC e ORM

**Matéria:** Banco de Dados / Taciano  
**Aluno:** Diêgo Axel  

**E-mail:** diegoaxelbsr@gmail.com

## 2

### 2.a 

**Link para projeto no GitHub:** https://github.com/Diego-Axel/CRUD_Cliente  

### 2.b

#### ODBC em Python com PostgreSQL

ODBC (Open Database Connectivity) é uma API padrão para acesso a bancos de dados de forma independente do gerenciador. Em Python, a principal biblioteca para trabalhar com ODBC é `pyodbc`.

**Características principais:**

- **Conectividade universal:** Funciona com múltiplos bancos de dados (SQL Server, PostgreSQL, MySQL, Oracle, etc.)
- **Interface padrão:** Utiliza a mesma sintaxe SQL independente do banco
- **Drivers:** Requer drivers ODBC específicos do banco de dados instalados no sistema
- **Conexão simples:** Através de connection strings com informações do servidor, autenticação e banco

**Instalação para PostgreSQL:**

```bash
# Instalar pyodbc
pip install pyodbc

# Linux/Mac: Instalar driver ODBC para PostgreSQL
# Ubuntu/Debian
sudo apt-get install odbc-postgresql unixodbc-dev

# macOS
brew install psqlodbc
```

**Exemplo com PostgreSQL:**

```python
import pyodbc

# Conectar ao PostgreSQL via ODBC
connection_string = 'Driver={PostgreSQL Unicode};Server=localhost;Port=5432;Database=meubd;UID=usuario;PWD=senha'
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

# Executar query
cursor.execute('SELECT * FROM clientes')
resultados = cursor.fetchall()

for linha in resultados:
    print(linha)

# Fechar conexão
cursor.close()
conn.close()
```

**Alternativa: Usar psycopg2 (mais nativo para PostgreSQL):**

```python
import psycopg2

# Conectar direto ao PostgreSQL (sem ODBC)
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="meubd",
    user="usuario",
    password="senha"
)
cursor = conn.cursor()
cursor.execute('SELECT * FROM clientes')
resultados = cursor.fetchall()
cursor.close()
conn.close()
```

**Vantagens do ODBC com PostgreSQL:**
- Compatibilidade com código que usa múltiplos bancos
- Interface padrão e consistente
- Facilita migração entre bancos

**Desvantagens:**
- Requer instalação de drivers ODBC
- psycopg2 é mais nativo e geralmente mais eficiente para PostgreSQL
- Mais uma camada de abstração

### 2.c

ORM (Object-Relational Mapping) é uma técnica que mapeia objetos da aplicação para tabelas do banco de dados, eliminando a necessidade de escrever SQL manualmente. As principais ORMs para Python são **SQLAlchemy** e **Peewee**.

**Características principais:**

- **Abstração SQL:** Escreve consultas usando objetos Python em vez de SQL
- **Relacionamentos automáticos:** Gerencia relacionamentos entre tabelas (1:N, N:N)
- **Migrations:** Facilitam versionamento e mudanças no schema
- **Type safety:** Validação de tipos e constraints no nível da aplicação
- **Query builder:** Construção dinâmica de queries complexas

**SQLAlchemy (mais popular e robusto):**

```python
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configurar conexão com PostgreSQL
DATABASE_URL = "postgresql://usuario:senha@localhost:5432/meubd"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

Base = declarative_base()

# Definir modelo
class Cliente(Base):
    __tablename__ = "clientes"
    
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)

# Criar tabelas
Base.metadata.create_all(engine)

# Usar a ORM
session = Session()

# Inserir
novo_cliente = Cliente(nome="João Silva", email="joao@email.com")
session.add(novo_cliente)
session.commit()

# Consultar
clientes = session.query(Cliente).filter(Cliente.nome.like("%Silva%")).all()

# Atualizar
cliente = session.query(Cliente).filter_by(id=1).first()
cliente.email = "novo@email.com"
session.commit()

# Deletar
session.delete(cliente)
session.commit()

session.close()
```

**Peewee (mais simples e leve):**

```python
from peewee import *

# Configurar conexão com PostgreSQL
db = PostgresqlDatabase('meubd', user='usuario', password='senha', host='localhost')

# Definir modelo
class Cliente(Model):
    nome = CharField()
    email = CharField(unique=True)
    
    class Meta:
        database = db

# Criar tabelas
db.create_tables([Cliente])

# Inserir
Cliente.create(nome="João Silva", email="joao@email.com")

# Consultar
clientes = Cliente.select().where(Cliente.nome.contains("Silva"))
for cliente in clientes:
    print(cliente.nome, cliente.email)

# Atualizar
cliente = Cliente.get_by_id(1)
cliente.email = "novo@email.com"
cliente.save()

# Deletar
cliente.delete_instance()
```

**Comparação: SQLAlchemy vs Peewee**

| Aspecto | SQLAlchemy | Peewee |
|--------|-----------|--------|
| **Complexidade** | Mais robusto, curva de aprendizado maior | Mais simples, intuitivo |
| **Features** | Muito completo (migrations, async, etc) | Essencial e direto |
| **Performance** | Excelente | Muito bom |
| **Comunidade** | Gigante, muita documentação | Menor, mas ativa |
| **Projetos** | Grandes aplicações, startups | Projetos pequenos/médios |

**Vantagens de usar ORM:**
- Código mais legível e manutenível
- Menos vulnerável a SQL injection
- Relacionamentos entre tabelas automáticos
- Migrations facilitam versionamento
- Abstração do banco específico

**Desvantagens:**
- Queries complexas podem ser mais lentas
- Curva de aprendizado (especialmente SQLAlchemy)
- Menos controle fino sobre o SQL gerado