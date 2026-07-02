import pyodbc

def execute_sql_file(filename):
    """ Executar um arquivo SQL via ODBC """
    try:
        conn_str = (
            "DRIVER={PostgreSQL Unicode};"
            "SERVER=localhost;"
            "PORT=5432;"
            "DATABASE=atividade_db;"
            "UID=postgres;"
            "PWD=123456;"
        )

        print(f'Executando {filename}...')
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        with open(filename, 'r') as f:
            sql_script = f.read()

        cursor.execute(sql_script)
        conn.commit()

        print(f'{filename} executado com sucesso.')

        cursor.close()
        conn.close()

    except pyodbc.Error as e:
        print(f'Erro ao executar {filename}: {e}')

if __name__ == "__main__":
    execute_sql_file('esquema_atividades_creates_tables.sql')
    execute_sql_file('esquema_atividades_inserts.sql')