import psycopg2
from psycopg2 import extras
from decouple import config
"""
Foi necessário dar permissões ao usuário para acessar os dados.
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO empresa_user;
"""
def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(
            host=config('DATABASE_HOST'),
            database=config('DATABASE_NAME'),
            user=config('DATABASE_USER'),
            password=config('DATABASE_PASS')
        )

        # create a cursor
        cur = conn.cursor()

	# execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # Execute a query
        cur.execute("SELECT * FROM empregado")

        # Recuperando os resultados da query em uma Tupla
        records = cur.fetchall()
        print("Total number of rows:", cur.rowcount)
        for row in records:
            print(row)
            print(row[0], row[1])

        # Criar um cursor do tipo DictCursor
        cur = conn.cursor(cursor_factory=extras.DictCursor)
        # Execute a query - Cursor do tipo DictCursor
        cur.execute("SELECT matricula, nome, salario FROM empregado")

        # Recuperando os resultados da query em um DictCursor
        dicts = cur.fetchall()
        print("Total number of rows:", cur.rowcount)
        for row in dicts:
            print(row['matricula'], row['nome'], row['salario'])

	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()
