import os
import dotenv
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker


dotenv.load_dotenv()
url = os.getenv('URLDB')

engine = create_engine(url)

metadata_obj = MetaData()
metadata_obj.reflect(bind=engine)

tabela_projeto = Table('projeto', metadata_obj, autoload_with=engine)
tabela_atividade = Table('atividade', metadata_obj, autoload_with=engine)

# a) 
letra_a = tabela_atividade.insert().values(descricao='Monitoria - Atividade 6',projeto=2, data_inicio='2024-02-26', data_fim='2024-04-17')

# b)
letra_b = tabela_projeto.update().where(tabela_projeto.c.codigo == 4).values(responsavel = 8)

with engine.connect() as connection:
    # a)
    connection.execute(letra_a)
    connection.commit()   
    
    # b) 
    connection.execute(letra_b)
    connection.commit()
    
    # c)
    print('\nProjetos')
    for row in connection.execute(tabela_projeto.select()):
        print(row)
 
    print('\nAtividades')
    for row in connection.execute(tabela_atividade.select()):
        print(row)