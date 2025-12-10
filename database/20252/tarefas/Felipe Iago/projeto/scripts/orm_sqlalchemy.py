from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Funcionario(Base):
    __tablename__ = 'funcionario'
    codigo = Column(Integer, primary_key=True)
    nome = Column(String(150))

class Projeto(Base):
    __tablename__ = 'projeto'
    codigo = Column(Integer, primary_key=True)
    nome = Column(String(50))
    descricao = Column(String(250))
    responsavel = Column(Integer, ForeignKey('funcionario.codigo'))
    atividades = relationship('Atividade', backref='projeto_rel')

class Atividade(Base):
    __tablename__ = 'atividade'
    codigo = Column(Integer, primary_key=True)
    descricao = Column(String(250))
    projeto = Column(Integer, ForeignKey('projeto.codigo'))
    data_inicio = Column(Date)
    data_fim = Column(Date)

# Conexão com o banco
engine = create_engine('postgresql+psycopg2://usuario:senha@localhost:5432/AtividadesBD')
Session = sessionmaker(bind=engine)
session = Session()

# Inserir atividade
nova = Atividade(descricao='Nova Atividade', projeto=1, data_inicio='2025-10-21', data_fim='2025-11-01')
session.add(nova)
session.commit()

# Atualizar líder de projeto
projeto = session.query(Projeto).filter_by(codigo=1).first()
projeto.responsavel = 2
session.commit()

# Listar projetos e atividades
for p in session.query(Projeto).all():
    print(p.nome)
    for a in p.atividades:
        print(' -', a.descricao)
