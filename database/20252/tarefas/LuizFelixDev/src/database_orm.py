from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

class Projeto(Base):
    __tablename__ = 'projeto'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    lider_id = Column(Integer)
    atividades = relationship("Atividade", back_populates="projeto")

class Atividade(Base):
    __tablename__ = 'atividade'
    id = Column(Integer, primary_key=True)
    descricao = Column(String)
    projeto_id = Column(Integer, ForeignKey('projeto.id'))
    projeto = relationship("Projeto", back_populates="atividades")

engine = create_engine('postgresql://luiz_admin:password123@localhost:5432/AtividadesBD')
Session = sessionmaker(bind=engine)
session = Session()

nova_atv = Atividade(descricao="Atividade via ORM", projeto_id=1)
session.add(nova_atv)

projeto = session.query(Projeto).get(1)
if projeto:
    projeto.lider_id = 5

resultados = session.query(Projeto).all()
for p in resultados:
    print(f"Projeto: {p.nome}")
    for a in p.atividades:
        print(f"  - {a.descricao}")

session.commit()
session.close()