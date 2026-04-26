import pyodbc

def init_db():
    """ Executar o script de inicialização do banco """
    try:
        conn_str = (
            "DRIVER={PostgreSQL Unicode};"
            "SERVER=localhost;"
            "PORT=5432;"
            "DATABASE=atividade_db;"
            "UID=postgres;"
            "PWD=123456;"
        )

        print('Conectando para inicializar o banco...')
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Ler o script init.sql
        with open('init.sql', 'r') as f:
            sql_script = f.read()

        # Executar o script
        cursor.execute(sql_script)
        conn.commit()

        print('Banco inicializado com sucesso.')

        cursor.close()
        conn.close()

    except pyodbc.Error as e:
        print(f'Erro: {e}')

if __name__ == "__main__":
    init_db()