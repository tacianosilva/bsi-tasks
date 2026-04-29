from sqlalchemy import create_engine, text

# conexão com o banco via ORM
engine = create_engine(
    "postgresql+psycopg2://admin:admin123@localhost:5432/atividadesbd"
)

# =========================
# 1. INSERIR ATIVIDADE
# =========================
with engine.begin() as conn:
    conn.execute(text("""
        INSERT INTO atividade (descricao, projeto, data_inicio, data_fim)
        VALUES ('Atividade via ORM', 1, '2024-01-01', '2024-02-01')
    """))

print("Atividade inserida via ORM!")

# =========================
# 2. ATUALIZAR LÍDER DO PROJETO
# =========================
with engine.begin() as conn:
    conn.execute(text("""
        UPDATE projeto
        SET responsavel = 2
        WHERE codigo = 1
    """))

print("Projeto atualizado via ORM!")

# =========================
# 3. LISTAR PROJETOS E ATIVIDADES
# =========================
with engine.connect() as conn:
    result = conn.execute(text("""
        SELECT p.codigo, p.nome, a.descricao
        FROM projeto p
        JOIN atividade a ON p.codigo = a.projeto
    """))

    print("\nProjetos e atividades (ORM):\n")

    for row in result:
        print(f"Projeto {row[0]} - {row[1]} | Atividade: {row[2]}")