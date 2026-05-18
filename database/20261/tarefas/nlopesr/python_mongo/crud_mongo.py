from pymongo import MongoClient
from bson.objectid import ObjectId
import datetime

# Conexão com o servidor MongoDB no Docker
# Utilizando as credenciais definidas no docker-compose
client = MongoClient('mongodb://admin_mongo:senha_mongo@localhost:27017/')
db = client['AtividadesProj']

colecao_projetos = db['projetos']
colecao_atividades = db['atividades']

def create_atividade(nome_projeto, titulo, descricao, responsavel):
    """Create: Inserir uma nova atividade em algum projeto existente"""
    projeto = colecao_projetos.find_one({"nome": nome_projeto})
    if not projeto:
        print(f"Projeto '{nome_projeto}' não encontrado!")
        return
    
    nova_atividade = {
        "projetoId": projeto["_id"],
        "titulo": titulo,
        "descricao": descricao,
        "responsavel": responsavel,
        "status": "Pendente",
        "dataPrevista": datetime.datetime.now() + datetime.timedelta(days=7)
    }
    
    resultado = colecao_atividades.insert_one(nova_atividade)
    print(f"Atividade '{titulo}' inserida com sucesso com ID: {resultado.inserted_id} no projeto '{nome_projeto}'.")


def read_projetos_e_atividades():
    """Read: Listar todos os projetos e, para cada projeto, listar suas atividades"""
    projetos = list(colecao_projetos.find())
    print("\n--- Lista de Projetos e Atividades ---")
    if not projetos:
        print("Nenhum projeto encontrado.")
        return

    for proj in projetos:
        print(f"\nProjeto: {proj.get('nome')} | Líder: {proj.get('lider')}")
        atividades = list(colecao_atividades.find({"projetoId": proj["_id"]}))
        if atividades:
            for ativ in atividades:
                print(f"  - Atividade: {ativ.get('titulo')} | Responsável: {ativ.get('responsavel')} | Status: {ativ.get('status')}")
        else:
            print("  - Nenhuma atividade para este projeto.")
    print("--------------------------------------\n")


def update_lider_projeto(nome_projeto, novo_lider):
    """Update: Atualizar o líder de um projeto específico"""
    resultado = colecao_projetos.update_one(
        {"nome": nome_projeto},
        {"$set": {"lider": novo_lider}}
    )
    if resultado.modified_count > 0:
        print(f"Líder do projeto '{nome_projeto}' atualizado para '{novo_lider}' com sucesso.")
    else:
        print(f"Projeto '{nome_projeto}' não encontrado ou o líder já é '{novo_lider}'.")


def delete_atividade(titulo_atividade):
    """Delete: Remover uma atividade de um projeto"""
    resultado = colecao_atividades.delete_one({"titulo": titulo_atividade})
    if resultado.deleted_count > 0:
        print(f"Atividade '{titulo_atividade}' removida com sucesso.")
    else:
        print(f"Atividade '{titulo_atividade}' não encontrada.")


# ==========================================
# Execução das operações CRUD para teste
# ==========================================
if __name__ == "__main__":
    print("=== Iniciando Operações CRUD no MongoDB ===")

    # Read Inicial
    print("1. Lendo estado inicial:")
    read_projetos_e_atividades()

    # Create
    print("2. Criando nova atividade:")
    create_atividade("Projeto Alfa", "Testes Unitários", "Implementar testes para o backend", "Carlos Silva")
    
    # Read após Create
    read_projetos_e_atividades()

    # Update
    print("3. Atualizando líder do Projeto Beta:")
    update_lider_projeto("Projeto Beta", "Fernanda Lima")

    # Delete
    print("4. Removendo atividade 'Desenvolvimento Backend':")
    delete_atividade("Desenvolvimento Backend")

    # Read Final
    print("5. Lendo estado final após atualizações e remoções:")
    read_projetos_e_atividades()
