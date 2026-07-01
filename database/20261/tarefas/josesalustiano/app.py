from pymongo import MongoClient

# 1. CONEXÃO COM O BANCO DE DADOS
print("Conectando ao MongoDB...")
client = MongoClient('mongodb://adminjose:password@localhost:27017/')
db = client['Atividades_Proj'] 

projetos_col = db['projetos']
empregados_col = db['empregados']
atividades_col = db['atividades']

projetos_col.drop()
empregados_col.drop()
atividades_col.drop()

# ==============================================================================
# PARTE 1: SCRIPT DE INICIALIZAÇÃO (Item 4 da Tarefa)
# Inserindo pelo menos 3 documentos em cada coleção principal
# ==============================================================================
print("\n--- INICIALIZANDO DADOS ---")

empregados = [
    {"_id": 1, "nome": "José Salustiano", "cargo": "Desenvolvedor Sênior"},
    {"_id": 2, "nome": "Maria Silva", "cargo": "Gerente de Projetos"},
    {"_id": 3, "nome": "João Carlos", "cargo": "Analista de Dados"}
]
empregados_col.insert_many(empregados)
print("3 Empregados inseridos.")

projetos = [
    {"_id": 101, "nome": "Sistema de Gestão Escolar", "lider_id": 2},
    {"_id": 102, "nome": "App de Entregas", "lider_id": 1},
    {"_id": 103, "nome": "Dashboard de Vendas", "lider_id": 3}
]
projetos_col.insert_many(projetos)
print("3 Projetos inseridos.")

atividades = [
    {"_id": 1001, "descricao": "Criar modelagem do banco de dados", "projeto_id": 101, "status": "Concluído"},
    {"_id": 1002, "descricao": "Desenvolver API de pagamentos", "projeto_id": 102, "status": "Em andamento"},
    {"_id": 1003, "descricao": "Levantamento de requisitos com o cliente", "projeto_id": 103, "status": "Pendente"}
]
atividades_col.insert_many(atividades)
print("3 Atividades inseridas.")

# ==============================================================================
# PARTE 2: OPERAÇÕES CRUD (Item 5 da Tarefa)
# ==============================================================================
print("\n--- INICIANDO OPERAÇÕES CRUD ---")

# a) CREATE: Inserir uma nova atividade em algum projeto existente
print("\n[CREATE] Inserindo nova atividade no projeto 'App de Entregas' (ID 102)...")
nova_atividade = {
    "_id": 1004, 
    "descricao": "Criar interface do usuário (Frontend)", 
    "projeto_id": 102, 
    "status": "Pendente"
}
atividades_col.insert_one(nova_atividade)
print("Nova atividade inserida com sucesso!")

# c) UPDATE: Atualizar o líder de um projeto específico
# Vamos mudar o líder do projeto 101 da Maria (ID 2) para o João (ID 3)
print("\n[UPDATE] Atualizando o líder do projeto 101...")
projetos_col.update_one({"_id": 101}, {"$set": {"lider_id": 3}})
print("Líder do projeto 101 atualizado para o empregado ID 3.")

# d) DELETE: Remover uma atividade de um projeto
# Vamos remover a atividade 1003 do projeto 103
print("\n[DELETE] Removendo a atividade ID 1003...")
atividades_col.delete_one({"_id": 1003})
print("Atividade 1003 removida com sucesso!")

# b) READ: Listar todos os projetos e, para cada projeto, listar suas atividades
print("\n[READ] Listando todos os Projetos e suas respectivas Atividades:")
print("-" * 50)

todos_projetos = projetos_col.find()

for projeto in todos_projetos:
    lider = empregados_col.find_one({"_id": projeto["lider_id"]})
    nome_lider = lider["nome"] if lider else "Sem líder"
    
    print(f"📁 PROJETO: {projeto['nome']} (Líder: {nome_lider})")
    
    atividades_do_projeto = atividades_col.find({"projeto_id": projeto["_id"]})
    
    lista_atividades = list(atividades_do_projeto)
    
    if len(lista_atividades) == 0:
        print("   -> Nenhuma atividade registrada.")
    else:
        for atividade in lista_atividades:
            print(f"   -> 📝 Atividade: {atividade['descricao']} | Status: {atividade['status']}")
    print("-" * 50)

print("\nFim da execução. Tudo funcionando perfeitamente!")