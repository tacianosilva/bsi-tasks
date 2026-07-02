import pyodbc

def executar_comandos():
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
        
        print("Conectado ao banco de dados com sucesso!\n")

        # 1. Inserir uma atividade em algum projeto (Ex: Projeto 1 - APF)
        cursor.execute("""
            INSERT INTO atividade (descricao, projeto, data_inicio, data_fim)
            VALUES ('APF - Nova Atividade Extra', 1, '2026-05-01', '2026-05-30');
        """)
        print("[OK] Nova atividade inserida no projeto 1.")

        # 2. Atualizar o líder (responsável) de algum projeto (Ex: Atualizando o responsável do Projeto 1)
        # O responsável precisa ser o código de um funcionário válido (ex: funcionário 3)
        cursor.execute("""
            UPDATE projeto
            SET responsavel = 3
            WHERE codigo = 1;
        """)
        print("[OK] Líder do projeto 1 atualizado.")

        # Confirmar (comitar) as alterações de INSERT e UPDATE no banco de dados
        conexao.commit()

        # 3. Listar todos os projetos e suas atividades
        # Usando LEFT JOIN para garantir que projetos sem atividades também apareçam
        cursor.execute("""
            SELECT p.nome AS nome_projeto, a.descricao AS desc_atividade
            FROM projeto p
            LEFT JOIN atividade a ON p.codigo = a.projeto
            ORDER BY p.nome;
        """)
        resultados = cursor.fetchall()

        print("\n--- Lista de Projetos e Atividades ---")
        for linha in resultados:
            projeto = linha.nome_projeto
            # Se não houver atividade (NULL no banco), exibe uma mensagem padrão
            atividade = linha.desc_atividade if linha.desc_atividade else "Nenhuma atividade registrada"
            print(f"Projeto: {projeto} | Atividade: {atividade}")

    except Exception as e:
        print(f"Erro durante a execução: {e}")
        # Em caso de erro nas execuções, desfaz as alterações não concluídas
        if 'conexao' in locals():
            conexao.rollback()
            
    finally:
        # Fechar cursor e conexão
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()
            print("\nConexão encerrada.")

if __name__ == "__main__":
    executar_comandos()