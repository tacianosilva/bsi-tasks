"""
Modelos ORM mapeando o esquema relacional AtividadesBD
usando SQLAlchemy 2.x (estilo declarativo moderno).
"""

from datetime import date
from typing import Optional, List

from sqlalchemy import (
    Integer, String, Date, ForeignKey, CHAR, Numeric
)
from sqlalchemy.orm import (
    DeclarativeBase, Mapped, mapped_column, relationship
)


class Base(DeclarativeBase):
    pass


class Funcionario(Base):
    __tablename__ = "funcionario"

    codigo: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[Optional[str]] = mapped_column(String(150))
    sexo: Mapped[Optional[str]] = mapped_column(CHAR(1))
    dt_nasc: Mapped[Optional[date]] = mapped_column(Date)
    # O tipo `money` do PostgreSQL (OID 790) não tem mapeamento nativo no
    # SQLAlchemy e gera "Unknown PG numeric type: 790" se mapeado como Numeric.
    # Solução simples: tratar como string (psycopg2 retorna 'R$ 2.500,00').
    # Em produção o ideal é usar NUMERIC(15,2) no banco em vez de money.
    salario: Mapped[Optional[str]] = mapped_column(String)
    supervisor: Mapped[Optional[int]] = mapped_column(
        ForeignKey("funcionario.codigo", ondelete="SET NULL", onupdate="CASCADE")
    )
    depto: Mapped[Optional[int]] = mapped_column(
        ForeignKey("departamento.codigo", ondelete="SET NULL", onupdate="CASCADE")
    )

    # Relacionamentos
    projetos_responsaveis: Mapped[List["Projeto"]] = relationship(
        back_populates="responsavel_obj",
        foreign_keys="Projeto.responsavel",
    )

    def __repr__(self) -> str:
        return f"<Funcionario(codigo={self.codigo}, nome='{self.nome}')>"


class Departamento(Base):
    __tablename__ = "departamento"

    codigo: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[Optional[str]] = mapped_column(String(100))
    sigla: Mapped[Optional[str]] = mapped_column(String(10), unique=True)
    descricao: Mapped[Optional[str]] = mapped_column(String(250))
    gerente: Mapped[Optional[int]] = mapped_column(
        ForeignKey("funcionario.codigo", ondelete="SET NULL", onupdate="CASCADE")
    )

    def __repr__(self) -> str:
        return f"<Departamento(codigo={self.codigo}, sigla='{self.sigla}')>"


class Projeto(Base):
    __tablename__ = "projeto"

    codigo: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[Optional[str]] = mapped_column(String(50), unique=True)
    descricao: Mapped[Optional[str]] = mapped_column(String(250))
    responsavel: Mapped[Optional[int]] = mapped_column(
        ForeignKey("funcionario.codigo", ondelete="SET NULL", onupdate="CASCADE")
    )
    depto: Mapped[Optional[int]] = mapped_column(
        ForeignKey("departamento.codigo", ondelete="SET NULL", onupdate="CASCADE")
    )
    data_inicio: Mapped[Optional[date]] = mapped_column(Date)
    data_fim: Mapped[Optional[date]] = mapped_column(Date)

    # Relacionamentos
    responsavel_obj: Mapped[Optional["Funcionario"]] = relationship(
        back_populates="projetos_responsaveis",
        foreign_keys=[responsavel],
    )
    atividades: Mapped[List["Atividade"]] = relationship(
        back_populates="projeto_obj",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return f"<Projeto(codigo={self.codigo}, nome='{self.nome}')>"


class Atividade(Base):
    __tablename__ = "atividade"

    codigo: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    descricao: Mapped[Optional[str]] = mapped_column(String(250))
    projeto: Mapped[Optional[int]] = mapped_column(
        ForeignKey("projeto.codigo", ondelete="SET NULL", onupdate="CASCADE")
    )
    data_inicio: Mapped[Optional[date]] = mapped_column(Date)
    data_fim: Mapped[Optional[date]] = mapped_column(Date)

    projeto_obj: Mapped[Optional["Projeto"]] = relationship(
        back_populates="atividades"
    )

    def __repr__(self) -> str:
        return f"<Atividade(codigo={self.codigo}, descricao='{self.descricao}')>"
