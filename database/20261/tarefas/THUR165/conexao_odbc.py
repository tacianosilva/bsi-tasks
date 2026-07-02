import pyodbc

def conectar_banco():
    string_conexao = (
        "DRIVER={PostgreSQL Unicode};"
        "SERVER=localhost;"
        "DATABASE=atividadesbd;"
        "UID=admin;"
        "PWD=adminpassword;"
        "PORT=5432;"
    )

    try:
        conexao = pyodbc.connect(string_conexao)
        cursor = conexao.cursor()
        
        print("Conexão ao banco AtividadesBD realizada com sucesso via ODBC!\n")

        cursor.execute("SELECT codigo, nome FROM departamento;")
        departamentos = cursor.fetchall()
        
        print("--- Departamentos Cadastrados ---")
        for depto in departamentos:
            print(f"Código: {depto.codigo} | Nome: {depto.nome}")

    except Exception as e:
        print(f"Erro ao conectar ou executar a consulta: {e}")
        
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()
            print("\nConexão encerrada.")

if __name__ == "__main__":
    conectar_banco()