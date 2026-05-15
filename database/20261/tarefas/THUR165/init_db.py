from pymongo import MongoClient

client = MongoClient("mongodb://admin:admin123@localhost:27017/")

db = client["AtividadesProj"]

empregados = db.empregados
projetos = db.projetos

empregados.insert_many([
    {
        "nome": "Arthur",
        "cargo": "Backend"
    },
    {
        "nome": "Maria",
        "cargo": "Frontend"
    },
    {
        "nome": "João",
        "cargo": "DBA"
    }
])

projetos.insert_many([
    {
        "nome": "Projeto A",
        "lider": "Arthur",
        "atividades": [
            {
                "descricao": "Criar API",
                "status": "Em andamento"
            }
        ]
    },
    {
        "nome": "Projeto B",
        "lider": "Maria",
        "atividades": [
            {
                "descricao": "Criar frontend",
                "status": "Pendente"
            }
        ]
    },
    {
        "nome": "Projeto C",
        "lider": "João",
        "atividades": [
            {
                "descricao": "Modelar banco",
                "status": "Concluído"
            }
        ]
    }
])

print("Dados inseridos com sucesso!")