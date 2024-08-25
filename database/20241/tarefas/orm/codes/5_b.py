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
    
    novo_responsavel = 4  
    projeto_id = 1  
    
    update_query = sql.SQL("""
        UPDATE projeto
        SET responsavel = %s
        WHERE codigo = %s
    """)
    
    cursor.execute(update_query, (novo_responsavel, projeto_id))
    
    conn.commit()
    
    print("Líder do projeto atualizado com sucesso.")

except Exception as error:
    print(f"Erro ao atualizar o líder do projeto: {error}")

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
