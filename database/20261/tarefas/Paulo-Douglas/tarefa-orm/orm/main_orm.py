"""
=============================================================
Conexão com o banco usando SQLAlchemy ORM
=============================================================
SQLAlchemy é um dos frameworks ORM mais usados em Python.
Aqui ele faz o mapeamento objeto-relacional: cada tabela
vira uma classe e cada linha vira um objeto Python, sem
escrever SQL bruto na maioria das operações.
"""

import os
from datetime import date

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session, selectinload

from models import Base, Funcionario, Departamento, Projeto, Atividade


def build_engine():
    """Cria o engine SQLAlchemy a partir das variáveis de ambiente."""
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5432")
    db = os.getenv("DB_NAME", "atividade_db")
    user = os.getenv("DB_USER", "admin_atividades")
    pwd = os.getenv("DB_PASSWORD", "senha123")
    url = f"postgresql+psycopg2://{user}:{pwd}@{host}:{port}/{db}"
    return create_engine(url, echo=False, future=True)


def inserir_atividade_orm(session: Session):
    """5.1 - Inserir uma atividade em algum projeto via ORM."""
    print("\n" + "=" * 60)
    print("5.1 - INSERINDO NOVA ATIVIDADE (ORM)")
    print("=" * 60)

    # Pega o projeto APF (ou o primeiro projeto disponível)
    projeto = session.scalars(
        select(Projeto).where(Projeto.nome == "APF")
    ).first()

    if projeto is None:
        print("Projeto 'APF' não encontrado.")
        return

    nova = Atividade(
        descricao="APF - Atividade 7 (inserida via SQLAlchemy ORM)",
        projeto=projeto.codigo,
        data_inicio=date(2024, 4, 1),
        data_fim=date(2024, 6, 1),
    )
    session.add(nova)
    session.commit()
    session.refresh(nova)

    print(f"Atividade inserida com sucesso:")
    print(f"  codigo={nova.codigo}, descricao='{nova.descricao}'")
    print(f"  projeto={nova.projeto}, inicio={nova.data_inicio}, fim={nova.data_fim}")


def atualizar_lider_orm(session: Session):
    """5.2 - Atualizar o líder (responsável) de algum projeto via ORM."""
    print("\n" + "=" * 60)
    print("5.2 - ATUALIZANDO LÍDER DO PROJETO (ORM)")
    print("=" * 60)

    # Pega o projeto Monitoria
    projeto = session.scalars(
        select(Projeto).where(Projeto.nome == "Monitoria")
    ).first()
    if projeto is None:
        print("Projeto 'Monitoria' não encontrado.")
        return

    print(f"Antes: projeto '{projeto.nome}' com responsavel={projeto.responsavel}")

    # Pega um novo líder (Funcionario codigo=3 - Maria)
    novo_lider = session.get(Funcionario, 3)
    if novo_lider is None:
        print("Funcionário escolhido como novo líder não encontrado.")
        return

    projeto.responsavel = novo_lider.codigo
    session.commit()
    session.refresh(projeto)

    print(
        f"Depois: projeto '{projeto.nome}' com responsavel={projeto.responsavel} "
        f"({novo_lider.nome})"
    )


def listar_projetos_orm(session: Session):
    """5.3 - Listar todos os projetos e suas atividades via ORM."""
    print("\n" + "=" * 60)
    print("5.3 - LISTANDO TODOS OS PROJETOS E SUAS ATIVIDADES (ORM)")
    print("=" * 60)

    # selectinload faz eager loading das atividades em uma segunda query,
    # evitando o problema de N+1 queries.
    stmt = (
        select(Projeto)
        .options(
            selectinload(Projeto.atividades),
            selectinload(Projeto.responsavel_obj),
        )
        .order_by(Projeto.codigo)
    )
    projetos = session.scalars(stmt).all()

    for p in projetos:
        resp_nome = p.responsavel_obj.nome if p.responsavel_obj else "(sem responsável)"
        print(f"\nProjeto [{p.codigo}] {p.nome} - {p.descricao}")
        print(f"  Responsável: {resp_nome}")
        print(f"  Atividades:")
        if not p.atividades:
            print(f"    (sem atividades)")
        for a in sorted(p.atividades, key=lambda x: x.codigo):
            print(f"    - [{a.codigo}] {a.descricao} ({a.data_inicio} -> {a.data_fim})")


def main():
    print("Conectando ao banco com SQLAlchemy ORM...")
    engine = build_engine()
    print("Conexão estabelecida com sucesso!")

    with Session(engine) as session:
        inserir_atividade_orm(session)
        atualizar_lider_orm(session)
        listar_projetos_orm(session)

    print("\nSessão encerrada.")


if __name__ == "__main__":
    main()
