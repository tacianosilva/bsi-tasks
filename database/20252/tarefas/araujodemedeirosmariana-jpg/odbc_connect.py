import pyodbc

def connect_odbc():
    """ Conectar ao banco de dados AtividadesBD usando ODBC """
    try:
        # String de conexão ODBC para PostgreSQL
        conn_str = (
            "DRIVER={PostgreSQL Unicode};"
            "SERVER=localhost;"
            "PORT=5432;"
            "DATABASE=atividade_db;"
            "UID=postgres;"
            "PWD=123456;"
        )

        print('Conectando ao banco de dados PostgreSQL via ODBC...')
        conn = pyodbc.connect(conn_str)

        # Criar um cursor
        cursor = conn.cursor()

        # Executar uma consulta para verificar a versão
        cursor.execute("SELECT version()")
        db_version = cursor.fetchone()
        print(f'Versão do PostgreSQL: {db_version[0]}')

        # Consultar a tabela funcionario
        print('\nConsultando a tabela funcionario:')
        cursor.execute("SELECT codigo, nome, sexo, salario FROM funcionario")
        rows = cursor.fetchall()

        print(f'Total de linhas: {len(rows)}')
        for row in rows:
            print(f'Código: {row[0]}, Nome: {row[1]}, Sexo: {row[2]}, Salário: {row[3]}')

        # Inserir um projeto (se não existir)
        print('\nInserindo um projeto...')
        cursor.execute("""
            INSERT INTO projeto (nome, descricao, codResponsavel, codDepto, dataInicio, dataFim)
            VALUES ('Projeto A', 'Descrição do Projeto A', 1, 1, '2024-01-01', '2024-12-31')
            ON CONFLICT (nome) DO NOTHING
        """)
        conn.commit()
        print('Projeto inserido (ou já existe).')

        # Inserir uma atividade em algum projeto
        print('\nInserindo uma atividade no projeto...')
        cursor.execute("""
            INSERT INTO atividade (descricao, codProjeto, dataInicio, dataFim)
            VALUES ('Atividade 1 do Projeto A', 1, '2024-02-01', '2024-02-28')
        """)
        conn.commit()
        print('Atividade inserida.')

        # Atualizar o líder de algum projeto
        print('\nAtualizando o líder do projeto...')
        cursor.execute("""
            UPDATE projeto SET codResponsavel = 2 WHERE codigo = 1
        """)
        conn.commit()
        print('Líder do projeto atualizado.')

        # Listar todos os projetos e suas atividades
        print('\nListando todos os projetos e suas atividades:')
        cursor.execute("""
            SELECT p.nome AS projeto_nome, p.descricao AS projeto_desc, a.descricao AS atividade_desc
            FROM projeto p
            LEFT JOIN atividade a ON p.codigo = a.codProjeto
            ORDER BY p.nome, a.descricao
        """)
        rows = cursor.fetchall()
        for row in rows:
            print(f'Projeto: {row[0]} - {row[1]}, Atividade: {row[2] or "Nenhuma"}')

        # Fechar cursor e conexão
        cursor.close()
        conn.close()
        print('\nConexão fechada com sucesso.')

    except pyodbc.Error as e:
        print(f'Erro ao conectar via ODBC: {e}')

if __name__ == "__main__":
    connect_odbc()