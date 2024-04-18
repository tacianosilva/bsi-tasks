import psycopg2
import os
import dotenv

dotenv.load_dotenv()

host = os.getenv('HOST')
dataBase = os.getenv('DATABASE')
port = os.getenv('PORT')
user = os.getenv('USERDB')
password = os.getenv('PASSWORD')

conexao = psycopg2.connect(
    dbname = dataBase,
    user = user,
    password = password,
    host = host,
    port = port
)

cursor = conexao.cursor()

# a)
cursor.execute(
    '''
        INSERT INTO atividade(descricao, projeto, data_inicio, data_fim)
        VALUES('Monitoria - Atividade 5', 2, '2024-02-26', '2024-04-17')
    '''
)
conexao.commit()


# b)
cursor.execute(
    '''
    UPDATE projeto SET responsavel = 7 WHERE codigo = 1
    '''
)
conexao.commit()

# c)
cursor.execute("SELECT * FROM projeto ORDER BY codigo")
rows = cursor.fetchall()
print('\nProjetos')
for row in rows:
    print(row)

cursor.execute("SELECT * FROM atividade ORDER BY codigo")
rows = cursor.fetchall()
print("\nAtividades")
for row in rows:
    print(row)


cursor.close()
conexao.close()