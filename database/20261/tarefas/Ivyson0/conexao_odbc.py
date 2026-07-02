import pyodbc

# conexão com o banco
conn = pyodbc.connect(
    "DRIVER={PostgreSQL Unicode};"
    "SERVER=localhost;"
    "PORT=5432;"
    "DATABASE=atividadesbd;"
    "UID=admin;"
    "PWD=admin123;"
)

cursor = conn.cursor()

# -------------------------------
# 1. INSERIR UMA ATIVIDADE
# -------------------------------
cursor.execute("""
INSERT INTO atividade (descricao, projeto, data_inicio, data_fim)
VALUES ('Nova Atividade Python', 1, '2024-01-01', '2024-02-01')
""")
conn.commit()

print("Atividade inserida com sucesso!")

# -------------------------------
# 2. ATUALIZAR RESPONSÁVEL DO PROJETO
# -------------------------------
cursor.execute("""
UPDATE projeto
SET responsavel = 2
WHERE codigo = 1
""")
conn.commit()

print("Projeto atualizado com sucesso!")

# -------------------------------
# 3. LISTAR PROJETOS E ATIVIDADES
# -------------------------------
cursor.execute("""
SELECT p.codigo, p.nome, a.descricao
FROM projeto p
JOIN atividade a ON p.codigo = a.projeto
""")

print("\nProjetos e suas atividades:\n")

for row in cursor.fetchall():
    print(f"Projeto {row[0]} - {row[1]} | Atividade: {row[2]}")

# fechar conexão
conn.close()