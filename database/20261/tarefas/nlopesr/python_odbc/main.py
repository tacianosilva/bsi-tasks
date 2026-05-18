import os
import pyodbc
from dotenv import load_dotenv

load_dotenv()

CONN_STR = (
    "DRIVER={" + os.getenv("ODBC_DRIVER", "PostgreSQL Unicode(x64)") + "};"
    "SERVER=" + os.getenv("DB_HOST", "localhost") + ";"
    "PORT=" + os.getenv("DB_PORT", "5432") + ";"
    "DATABASE=" + os.getenv("DB_NAME", "AtividadesBD") + ";"
    "UID=" + os.getenv("DB_USER", "atividades_user") + ";"
    "PWD=" + os.getenv("DB_PASSWORD", "atividades_pass") + ";"
)


def main() -> None:
    with pyodbc.connect(CONN_STR, autocommit=False) as conn:
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO atividade (descricao, projeto, data_inicio, data_fim)
            VALUES (?, ?, ?, ?)
            """,
            "Atividade criada via ODBC",
            1,
            "2026-04-28",
            "2026-05-15",
        )

        cursor.execute(
            """
            UPDATE projeto
            SET responsavel = ?
            WHERE codigo = ?
            """,
            1,
            2,
        )

        cursor.execute(
            """
            SELECT p.codigo, p.nome, a.codigo, a.descricao
            FROM projeto p
            LEFT JOIN atividade a ON a.projeto = p.codigo
            ORDER BY p.codigo, a.codigo
            """
        )

        print("Projetos e atividades (ODBC):")
        for row in cursor.fetchall():
            print(f"Projeto {row[0]} - {row[1]} | Atividade {row[2]} - {row[3]}")

        conn.commit()


if __name__ == "__main__":
    main()
