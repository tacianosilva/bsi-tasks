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
    
    query = """
    SELECT p.nome AS projeto, a.descricao AS atividade, a.data_inicio, a.data_fim
    FROM projeto p
    LEFT JOIN atividade a ON p.codigo = a.projeto
    ORDER BY p.nome, a.data_inicio;
    """
    
    cursor.execute(query)
    
    resultados = cursor.fetchall()
    
    for row in resultados:
        projeto, atividade, data_inicio, data_fim = row
        print(f"Projeto: {projeto}, Atividade: {atividade}, Data de Início: {data_inicio}, Data de Fim: {data_fim}")

except Exception as error:
    print(f"Erro ao listar projetos e atividades: {error}")

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
