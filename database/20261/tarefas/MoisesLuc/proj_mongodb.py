import pymongo

client = pymongo.MongoClient("mongodb://user:pass@localhost:27017/")

db = client["AtividadesProj"]

dep = db["departamentos"]
proj = db["projetos"]
emp = db["empregados"]
task = db["tarefas"]

if ("departamentos" not in db.list_collection_names()):
    departamentos = [ { "name": 'Departamento1' },
                    { "name": 'Departamento2' },
                    { "name": 'Departamento3' }
    ]
    x = dep.insert_many(departamentos)

if ("projetos" not in db.list_collection_names()):
    projetos = [ { "name": "Projeto1", "department_id": 1, "lider_id": 1 },
                { "name": "Projeto2", "department_id": 2, "lider_id": 2 }, 
                { "name": "Projeto3", "department_id": 3, "lider_id": 3 } 
    ]
    x = proj.insert_many(projetos)

if ("empregados" not in db.list_collection_names()):
    empregados = [ { "name": 'Empregado1' },
                    { "name": 'Empregado2' },
                    { "name": 'Empregado3' }
    ]
    x = dep.insert_many(empregados)

# --------------------------------------------------------------------
# ----------------------------- CRUD ---------------------------------
# --------------------------------------------------------------------

def insert(id):
    task_nome = input("Nome: ")

    task_desc = input("Descricao: ")
    
    new_task = { "name": task_nome, "description": task_desc, "project_id": id}
    x = task.insert_one(new_task)

def read():
    pipeline = [
        {
            "$lookup": {
                "from": "tarefas",
                "localField": "_id",
                "foreignField": "project_id",
                "as": "tarefas"
            }
        },
        {
            "$sort": {"name": 1}
        }
    ]

    projects = list(proj.aggregate(pipeline))

    for project in projects:
        print(f"\nProjeto: {project['name']}")

        tarefas = project.get("tarefas", [])
        if not tarefas:
            print("  Nenhuma atividade cadastrada.")
            continue

        for tarefa in tarefas:
            print(f"  - {tarefa['name']}: {tarefa['description']}")

def search_projects():
    projects = list(proj.find())
    for i, x in enumerate(projects, 1):
        print(f"{i} - {x['name']} (ID: {x['_id']})")
    return projects

def search_tasks():
    tasks = list(task.find())
    for i, x in enumerate(tasks, 1):
        print(f"{i} - {x['name']} (ID: {x['_id']})")
    return tasks

def update(id):
    proj_lider = input("Digite o id do novo líder: ")

    selected_proj = { "_id": id}
    new_info = { "$set": { "lider_id": proj_lider } }

    proj.update_one(selected_proj, new_info)

def delete(id):
    del_task = { "_id": id }

    task.delete_one(del_task)




op = -1

while (op != 0):
    print("Selecione a operação desejada:")
    print("1 - Inserir tarefa")
    print("2 - Listar")
    print("3 - Atualizar")
    print("4 - Deletar")
    print("0 - Sair")
    op = int(input("--> "))

    if (op != 0):
        match op:
            case 1:
                print("Selecione o projeto: ")
                projects = search_projects()
                option = int(input("--> "))
                proj_id = projects[option - 1]["_id"]
                insert(proj_id)
            case 2:
                read()
            case 3:
                print("Selecione o projeto: ")
                projects = search_projects()
                option = int(input("--> "))
                proj_id = projects[option - 1]["_id"]
                update(proj_id)
            case 4:
                print("Selecione uma tarefa: ")
                tasks = search_tasks()
                option = int(input("--> "))
                task_id = tasks[option - 1]["_id"]
                delete(task_id)

    