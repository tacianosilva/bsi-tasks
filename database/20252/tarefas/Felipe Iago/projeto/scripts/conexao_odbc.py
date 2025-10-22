import pyodbc

# Conexão ODBC com PostgreSQL
conn = pyodbc.connect(
    'DRIVER={PostgreSQL Unicode};'
    'SERVER=localhost;'
    'PORT=5432;'
    'DATABASE=AtividadesBD;'
    'UID=usuario;'
    'PWD=senha'
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM projeto;")
print("Projetos cadastrados:")
for row in cursor.fetchall():
    print(row)

conn.close()
