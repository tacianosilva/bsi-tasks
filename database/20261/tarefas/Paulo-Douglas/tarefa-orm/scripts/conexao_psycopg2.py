"""
=============================================================
Conexão direta com o banco usando psycopg2 (driver PostgreSQL)
=============================================================
O psycopg2 é o driver Python mais usado para PostgreSQL,
funciona de forma análoga ao ODBC/JDBC: estabelece conexão,
abre cursor, executa SQL diretamente e processa o resultado.
"""

import os
import psycopg2
from psycopg2 import sql


def get_connection():
    """Cria uma conexão com o banco de dados PostgreSQL."""
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME", "atividade_db"),
        user=os.getenv("DB_USER", "admin_atividades"),
        password=os.getenv("DB_PASSWORD", "senha123"),
    )


def inserir_atividade(conn, descricao, projeto_id, data_inicio, data_fim):
    """4.1 - Inserir uma atividade em algum projeto."""
    print("\n" + "=" * 60)
    print("4.1 - INSERINDO NOVA ATIVIDADE")
    print("=" * 60)
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO atividade (descricao, projeto, data_inicio, data_fim)
            VALUES (%s, %s, %s, %s)
            RETURNING codigo, descricao, projeto, data_inicio, data_fim;
            """,
            (descricao, projeto_id, data_inicio, data_fim),
        )
        nova = cur.fetchone()
        conn.commit()
        print(f"Atividade inserida com sucesso:")
        print(f"  codigo={nova[0]}, descricao='{nova[1]}', projeto={nova[2]}")
        print(f"  inicio={nova[3]}, fim={nova[4]}")


def atualizar_lider_projeto(conn, projeto_nome, novo_lider_id):
    """4.2 - Atualizar o líder (responsável) de algum projeto."""
    print("\n" + "=" * 60)
    print("4.2 - ATUALIZANDO LÍDER DO PROJETO")
    print("=" * 60)
    with conn.cursor() as cur:
        # Líder anterior
        cur.execute(
            "SELECT codigo, nome, responsavel FROM projeto WHERE nome = %s;",
            (projeto_nome,),
        )
        antes = cur.fetchone()
        if not antes:
            print(f"Projeto '{projeto_nome}' não encontrado.")
            return
        print(f"Antes: projeto '{antes[1]}' (cod={antes[0]}) com responsavel={antes[2]}")

        # Atualiza
        cur.execute(
            "UPDATE projeto SET responsavel = %s WHERE nome = %s RETURNING codigo, nome, responsavel;",
            (novo_lider_id, projeto_nome),
        )
        depois = cur.fetchone()
        conn.commit()

        # Busca o nome do novo líder
        cur.execute("SELECT nome FROM funcionario WHERE codigo = %s;", (novo_lider_id,))
        nome_lider = cur.fetchone()
        nome_lider = nome_lider[0] if nome_lider else "(não encontrado)"

        print(
            f"Depois: projeto '{depois[1]}' (cod={depois[0]}) com responsavel={depois[2]} ({nome_lider})"
        )


def listar_projetos_e_atividades(conn):
    """4.3 - Listar todos os projetos e suas atividades."""
    print("\n" + "=" * 60)
    print("4.3 - LISTANDO TODOS OS PROJETOS E SUAS ATIVIDADES")
    print("=" * 60)
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT p.codigo, p.nome, p.descricao, f.nome AS responsavel,
                   a.codigo AS atv_cod, a.descricao AS atv_desc,
                   a.data_inicio, a.data_fim
              FROM projeto p
              LEFT JOIN funcionario f ON f.codigo = p.responsavel
              LEFT JOIN atividade a   ON a.projeto = p.codigo
             ORDER BY p.codigo, a.codigo;
            """
        )
        rows = cur.fetchall()

        projeto_atual = None
        for r in rows:
            cod, nome, desc, resp, atv_cod, atv_desc, ini, fim = r
            if projeto_atual != cod:
                projeto_atual = cod
                print(f"\nProjeto [{cod}] {nome} - {desc}")
                print(f"  Responsável: {resp or '(sem responsável)'}")
                print(f"  Atividades:")
            if atv_cod is not None:
                print(f"    - [{atv_cod}] {atv_desc} ({ini} -> {fim})")
            else:
                print(f"    (sem atividades)")


def main():
    print("Conectando ao banco com psycopg2 (driver direto)...")
    conn = get_connection()
    print("Conexão estabelecida com sucesso!")

    try:
        # 4.1 Inserir uma atividade no projeto APF (codigo=1)
        inserir_atividade(
            conn,
            descricao="APF - Atividade 6 (inserida via psycopg2)",
            projeto_id=1,
            data_inicio="2024-01-15",
            data_fim="2024-03-15",
        )

        # 4.2 Atualizar o líder do projeto 'BD' para o funcionário codigo=4 (Josefa)
        atualizar_lider_projeto(conn, projeto_nome="BD", novo_lider_id=4)

        # 4.3 Listar todos os projetos e atividades
        listar_projetos_e_atividades(conn)

    finally:
        conn.close()
        print("\nConexão encerrada.")


if __name__ == "__main__":
    main()
