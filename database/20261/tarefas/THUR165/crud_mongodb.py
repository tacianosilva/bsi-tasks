from pymongo import MongoClient

client = MongoClient("mongodb://admin:admin123@localhost:27017/")

db = client["AtividadesProj"]

projetos = db.projetos

# ---------------- CREATE ----------------

projetos.update_one(
    {"nome": "Projeto A"},
    {
        "$push": {
            "atividades": {
                "descricao": "Criar dashboard",
                "status": "Pendente"
            }
        }
    }
)

print("Atividade inserida!")

# ---------------- READ ----------------

print("\nLISTANDO PROJETOS\n")

for projeto in projetos.find():

    print(f"Projeto: {projeto['nome']}")
    print(f"Lider: {projeto['lider']}")

    for atividade in projeto["atividades"]:
        print("-", atividade["descricao"])

# ---------------- UPDATE ----------------

projetos.update_one(
    {"nome": "Projeto A"},
    {
        "$set": {
            "lider": "Maria"
        }
    }
)

print("\nLider atualizado!")

# ---------------- DELETE ----------------

projetos.update_one(
    {"nome": "Projeto A"},
    {
        "$pull": {
            "atividades": {
                "descricao": "Criar API"
            }
        }
    }
)

print("\nAtividade removida!")