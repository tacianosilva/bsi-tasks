import pyodbc

conn = pyodbc.connect(
    'DRIVER={PostgreSQL Unicode};'
    'SERVER=localhost;'
    'PORT=5432;'
    'DATABASE=AtividadesBD;'
    'UID=usuario;'
    'PWD=senha'
)
cursor = conn.cursor()

# Inserir uma atividade
cursor.execute("""
INSERT INTO atividade (descricao, projeto, data_inicio, data_fim)
VALUES (?, ?, ?, ?)
""", ('Nova Atividade', 1, '2025-10-21', '2025-11-01'))

# Atualizar líder de projeto
cursor.execute("""
UPDATE projeto SET responsavel = ? WHERE codigo = ?
""", (2, 1))

# Listar projetos e atividades
cursor.execute("""
SELECT p.nome AS projeto, a.descricao AS atividade
FROM projeto p
LEFT JOIN atividade a ON p.codigo = a.projeto
""")
for row in cursor.fetchall():
    print(row)

conn.commit()
conn.close()
