from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, select
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

DATABASE_URL = "postgresql://admin:adminpassword@localhost:5432/atividadesbd"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
class Funcionario(Base):
    __tablename__ = 'funcionario'
    codigo = Column(Integer, primary_key=True)
    nome = Column(String)

class Projeto(Base):
    __tablename__ = 'projeto'
    codigo = Column(Integer, primary_key=True)
    nome = Column(String)
    responsavel = Column(Integer, ForeignKey('funcionario.codigo'))
    atividades = relationship("Atividade", back_populates="projeto_rel")

class Atividade(Base):
    __tablename__ = 'atividade'
    codigo = Column(Integer, primary_key=True)
    descricao = Column(String)
    projeto = Column(Integer, ForeignKey('projeto.codigo'))
    data_inicio = Column(Date)
    data_fim = Column(Date)
    projeto_rel = relationship("Projeto", back_populates="atividades")

def executar_tarefas_orm():
    try:
        nova_ativ = Atividade(
            descricao="Atividade Extra via ORM",
            projeto=2,
            data_inicio="2026-06-01",
            data_fim="2026-06-15"
        )
        session.add(nova_ativ)
        print("[ORM] Nova atividade adicionada.")

        projeto_alvo = session.query(Projeto).filter_by(codigo=2).first()
        if projeto_alvo:
            projeto_alvo.responsavel = 1
            print(f"[ORM] Responsável do projeto {projeto_alvo.nome} atualizado.")

        session.commit()

        print("\n--- Projetos e Atividades (Via ORM) ---")
        projetos = session.query(Projeto).all()
        for p in projetos:
            print(f"Projeto: {p.nome}")
            if p.atividades:
                for a in p.atividades:
                    print(f"  - {a.descricao}")
            else:
                print("  - Sem atividades.")

    except Exception as e:
        session.rollback()
        print(f"Erro: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    executar_tarefas_orm()