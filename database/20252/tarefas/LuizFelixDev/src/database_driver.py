import psycopg2

conn = psycopg2.connect(
    dbname="AtividadesBD",
    user="luiz_admin",
    password="password123",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

cur.execute("INSERT INTO atividade (descricao, projeto_id) VALUES (%s, %s)", ('Atividade via Driver', 1))

cur.execute("UPDATE projeto SET lider_id = %s WHERE id = %s", (2, 1))

cur.execute("""
    SELECT p.nome, a.descricao 
    FROM projeto p 
    LEFT JOIN atividade a ON a.projeto_id = p.id
""")

for row in cur.fetchall():
    print(f"Projeto: {row[0]} | Atividade: {row[1]}")

conn.commit()
cur.close()
conn.close()