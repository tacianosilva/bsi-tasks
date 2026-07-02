from pymongo import MongoClient

client = MongoClient("mongodb://admin:admin123@localhost:27017/")
db = client["AtividadesProj"]

# CREATE
db.atividades.insert_one({"descricao": "Nova tarefa"})

# READ
for p in db.projetos.find():
    print(p)

# UPDATE
db.projetos.update_one(
    {"nome": "Sistema BD"},
    {"$set": {"lider": "Novo líder"}}
)

# DELETE
db.atividades.delete_one({"descricao": "Nova tarefa"})