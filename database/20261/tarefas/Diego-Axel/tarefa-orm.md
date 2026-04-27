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
