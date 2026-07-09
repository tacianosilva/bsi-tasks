import sqlite3

def executar_sql_puro():
    # Conecta ao arquivo de banco do Django
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # 5.a Inserir atividade [cite: 20]
    cursor.execute("INSERT INTO minhaapp_atividade (descricao, projeto_id) VALUES (?, ?)", ('Atividade SQL', 1))

    # 5.b Atualizar líder [cite: 21]
    cursor.execute("UPDATE minhaapp_projeto SET lider_id = ? WHERE id = ?", (2, 1))

    # 5.c Listar projetos e atividades [cite: 23]
    cursor.execute("SELECT p.nome, a.descricao FROM minhaapp_projeto p JOIN minhaapp_atividade a ON p.id = a.projeto_id")
    print(cursor.fetchall())

    conn.commit()
    conn.close()

if __name__ == "__main__":
    executar_sql_puro()