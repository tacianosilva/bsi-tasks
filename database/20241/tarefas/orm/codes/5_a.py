import psycopg2
from psycopg2 import sql

conn_params = {
    "dbname": "atividade_db",
    "user": "myuser",
    "password": "mypassword",
    "host": "localhost",
    "port": "5432"
}

try:
    conn = psycopg2.connect(**conn_params)
    cursor = conn.cursor()
    
    descricao = "Nova Atividade"
    projeto_id = 1  
    data_inicio = "2024-08-01"
    data_fim = "2024-08-31"
    
    insert_query = sql.SQL("""
        INSERT INTO atividade (descricao, projeto, data_inicio, data_fim)
        VALUES (%s, %s, %s, %s)
    """)
    
    cursor.execute(insert_query, (descricao, projeto_id, data_inicio, data_fim))

    conn.commit()
    
    print("Atividade inserida com sucesso.")

except Exception as error:
    print(f"Erro ao inserir atividade: {error}")

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
