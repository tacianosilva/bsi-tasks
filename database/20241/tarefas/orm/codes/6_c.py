from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.exc import SQLAlchemyError

DATABASE_URL = "postgresql+psycopg2://myuser:mypassword@localhost/atividade_db"

engine = create_engine(DATABASE_URL)

Base = declarative_base()

class Funcionario(Base):
    __tablename__ = 'funcionario'
    codigo = Column(Integer, primary_key=True)
    nome = Column(String(150))
    sexo = Column(String(1))
    dt_nasc = Column(Date)
    salario = Column(String)
    supervisor = Column(Integer, ForeignKey('funcionario.codigo'))
    depto = Column(Integer, ForeignKey('departamento.codigo'))
    
    supervisor_rel = relationship("Funcionario", remote_side=[codigo])
    departamento_rel = relationship("Departamento", foreign_keys=[depto], back_populates="funcionarios")

class Departamento(Base):
    __tablename__ = 'departamento'
    codigo = Column(Integer, primary_key=True)
    nome = Column(String(100))
    sigla = Column(String(10), unique=True)
    descricao = Column(String(250))
    gerente = Column(Integer, ForeignKey('funcionario.codigo'))
    
    gerente_rel = relationship("Funcionario", foreign_keys=[gerente])
    funcionarios = relationship("Funcionario", foreign_keys=[Funcionario.depto], back_populates="departamento_rel")

class Projeto(Base):
    __tablename__ = 'projeto'
    codigo = Column(Integer, primary_key=True)
    nome = Column(String(50), unique=True)
    descricao = Column(String(250))
    responsavel = Column(Integer, ForeignKey('funcionario.codigo'))
    depto = Column(Integer, ForeignKey('departamento.codigo'))
    data_inicio = Column(Date)
    data_fim = Column(Date)
    
    responsavel_rel = relationship("Funcionario", foreign_keys=[responsavel])
    departamento_rel = relationship("Departamento", foreign_keys=[depto])
    atividades = relationship("Atividade", back_populates="projeto_rel")

class Atividade(Base):
    __tablename__ = 'atividade'
    codigo = Column(Integer, primary_key=True)
    descricao = Column(String(250))
    projeto = Column(Integer, ForeignKey('projeto.codigo'))
    data_inicio = Column(Date)
    data_fim = Column(Date)
    
    projeto_rel = relationship("Projeto", foreign_keys=[projeto])

Session = sessionmaker(bind=engine)
session = Session()

try:
    projetos = session.query(Projeto).all()
    
    for projeto in projetos:
        print(f"Projeto: {projeto.nome} - {projeto.descricao}")
        atividades = projeto.atividades
        if atividades:
            for atividade in atividades:
                print(f"  Atividade: {atividade.descricao} - Início: {atividade.data_inicio} - Fim: {atividade.data_fim}")
        else:
            print("  Sem atividades associadas.")

except SQLAlchemyError as e:
    print(f"Erro ao listar projetos e atividades: {e}")

finally:
    session.close()
