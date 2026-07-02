db = db.getSiblingDB('AtividadesProj');

db.createUser({
    user: 'usuarioApp',
    pwd: 'senha123',
    roles: [
        {
            role: 'readWrite',
            db: 'AtividadesProj'
        }
    ]
});

db.createCollection('empregados');
db.createCollection('projetos');
db.createCollection('atividades');

const empregados = [
    {
        matricula: 1001,
        nome: "Carlos Silva",
        email: "carlos.silva@empresa.com",
        cargo: "Desenvolvedor Backend",
        salario: 4500
    },
    {
        matricula: 1002,
        nome: "Ana Souza",
        email: "ana.souza@empresa.com",
        cargo: "Gerente de Projetos",
        salario: 7000
    },
    {
        matricula: 1003,
        nome: "Marcos Lima",
        email: "marcos.lima@empresa.com",
        cargo: "Analista de Sistemas",
        salario: 5000
    }
];

db.empregados.insertMany(empregados);

const projetos = [
    {
        codigo: 1,
        nome: "Sistema Acadêmico",
        descricao: "Sistema para gerenciamento acadêmico",
        lider: "Ana Souza",
        dataInicio: new Date("2026-01-10")
    },
    {
        codigo: 2,
        nome: "Portal Financeiro",
        descricao: "Sistema financeiro interno",
        lider: "Carlos Silva",
        dataInicio: new Date("2026-02-05")
    },
    {
        codigo: 3,
        nome: "Aplicativo Mobile",
        descricao: "Aplicativo mobile institucional",
        lider: "Marcos Lima",
        dataInicio: new Date("2026-03-01")
    }
];

db.projetos.insertMany(projetos);

const atividades = [
    {
        titulo: "Criar API REST",
        descricao: "Desenvolver endpoints principais",
        responsavel: "Carlos Silva",
        projeto: "Sistema Acadêmico",
        status: "Em andamento",
        prazo: new Date("2026-06-10")
    },
    {
        titulo: "Modelar Banco de Dados",
        descricao: "Criar estrutura inicial do banco",
        responsavel: "Ana Souza",
        projeto: "Portal Financeiro",
        status: "Concluído",
        prazo: new Date("2026-05-20")
    },
    {
        titulo: "Desenvolver Interface Mobile",
        descricao: "Criar telas do aplicativo",
        responsavel: "Marcos Lima",
        projeto: "Aplicativo Mobile",
        status: "Pendente",
        prazo: new Date("2026-07-15")
    }
];

db.atividades.insertMany(atividades);

print("Banco de dados AtividadesProj inicializado com sucesso!");