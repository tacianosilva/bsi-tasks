import os
from datetime import date

from dotenv import load_dotenv
from sqlalchemy import Date, ForeignKey, Integer, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

load_dotenv()


class Base(DeclarativeBase):
    pass


class Projeto(Base):
    __tablename__ = "projeto"

    codigo: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50))
    responsavel: Mapped[int | None] = mapped_column(ForeignKey("funcionario.codigo"))


class Atividade(Base):
    __tablename__ = "atividade"

    codigo: Mapped[int] = mapped_column(Integer, primary_key=True)
    descricao: Mapped[str] = mapped_column(String(250))
    projeto: Mapped[int | None] = mapped_column(ForeignKey("projeto.codigo"))
    data_inicio: Mapped[date | None] = mapped_column(Date)
    data_fim: Mapped[date | None] = mapped_column(Date)


def get_engine():
    user = os.getenv("DB_USER", "atividades_user")
    password = os.getenv("DB_PASSWORD", "atividades_pass")
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5432")
    db = os.getenv("DB_NAME", "AtividadesBD")
    return create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}")


def main() -> None:
    engine = get_engine()

    with Session(engine) as session:
        session.add(
            Atividade(
                descricao="Atividade criada via ORM",
                projeto=1,
                data_inicio=date(2026, 4, 28),
                data_fim=date(2026, 5, 20),
            )
        )

        projeto = session.get(Projeto, 3)
        if projeto:
            projeto.responsavel = 2

        stmt = (
            select(Projeto.codigo, Projeto.nome, Atividade.codigo, Atividade.descricao)
            .outerjoin(Atividade, Atividade.projeto == Projeto.codigo)
            .order_by(Projeto.codigo, Atividade.codigo)
        )

        print("Projetos e atividades (ORM):")
        for row in session.execute(stmt):
            print(f"Projeto {row[0]} - {row[1]} | Atividade {row[2]} - {row[3]}")

        session.commit()


if __name__ == "__main__":
    main()
