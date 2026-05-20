const databaseName = "AtividadesProj";

db = db.getSiblingDB(databaseName);

db.createUser({
  user: "atividades_user",
  pwd: "atividades123",
  roles: [
    {
      role: "readWrite",
      db: databaseName
    }
  ]
});

db.createCollection("empregados", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["nome", "email", "cargo", "departamento"],
      properties: {
        nome: { bsonType: "string" },
        email: { bsonType: "string" },
        cargo: { bsonType: "string" },
        departamento: { bsonType: "string" }
      }
    }
  }
});

db.createCollection("projetos", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["nome", "descricao", "liderId", "status"],
      properties: {
        nome: { bsonType: "string" },
        descricao: { bsonType: "string" },
        liderId: { bsonType: "objectId" },
        membrosIds: {
          bsonType: "array",
          items: { bsonType: "objectId" }
        },
        status: { bsonType: "string" }
      }
    }
  }
});

db.createCollection("atividades", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["titulo", "descricao", "projetoId", "responsavelId", "status"],
      properties: {
        titulo: { bsonType: "string" },
        descricao: { bsonType: "string" },
        projetoId: { bsonType: "objectId" },
        responsavelId: { bsonType: "objectId" },
        status: { bsonType: "string" },
        prioridade: { bsonType: "string" },
        estimativaHoras: { bsonType: "number" }
      }
    }
  }
});

const emp1 = ObjectId();
const emp2 = ObjectId();
const emp3 = ObjectId();

db.empregados.insertMany([
  {
    _id: emp1,
    nome: "Ana Souza",
    email: "ana.souza@empresa.com",
    cargo: "Gerente de Projetos",
    departamento: "Tecnologia"
  },
  {
    _id: emp2,
    nome: "Carlos Lima",
    email: "carlos.lima@empresa.com",
    cargo: "Desenvolvedor Backend",
    departamento: "Tecnologia"
  },
  {
    _id: emp3,
    nome: "Marina Alves",
    email: "marina.alves@empresa.com",
    cargo: "Analista de Sistemas",
    departamento: "Tecnologia"
  }
]);

const proj1 = ObjectId();
const proj2 = ObjectId();
const proj3 = ObjectId();

db.projetos.insertMany([
  {
    _id: proj1,
    nome: "Sistema de Controle de Atividades",
    descricao: "Sistema para organizar atividades internas do departamento.",
    liderId: emp1,
    membrosIds: [emp1, emp2, emp3],
    status: "Em andamento",
    dataInicio: new Date("2026-03-01")
  },
  {
    _id: proj2,
    nome: "Portal de Relatórios",
    descricao: "Projeto para emissão de relatórios administrativos.",
    liderId: emp2,
    membrosIds: [emp2, emp3],
    status: "Planejado",
    dataInicio: new Date("2026-04-10")
  },
  {
    _id: proj3,
    nome: "Automação de Processos",
    descricao: "Automação de tarefas repetitivas do setor.",
    liderId: emp3,
    membrosIds: [emp1, emp3],
    status: "Em análise",
    dataInicio: new Date("2026-05-05")
  }
]);

db.atividades.insertMany([
  {
    titulo: "Criar modelo de dados",
    descricao: "Definir as coleções principais do sistema.",
    projetoId: proj1,
    responsavelId: emp3,
    status: "Concluída",
    prioridade: "Alta",
    estimativaHoras: 6,
    criadoEm: new Date()
  },
  {
    titulo: "Implementar autenticação",
    descricao: "Criar controle de acesso dos usuários.",
    projetoId: proj1,
    responsavelId: emp2,
    status: "Em andamento",
    prioridade: "Alta",
    estimativaHoras: 12,
    criadoEm: new Date()
  },
  {
    titulo: "Criar dashboard inicial",
    descricao: "Montar tela inicial com indicadores dos projetos.",
    projetoId: proj2,
    responsavelId: emp3,
    status: "Pendente",
    prioridade: "Média",
    estimativaHoras: 10,
    criadoEm: new Date()
  }
]);

db.empregados.createIndex({ email: 1 }, { unique: true });
db.projetos.createIndex({ nome: 1 });
db.atividades.createIndex({ projetoId: 1 });
db.atividades.createIndex({ responsavelId: 1 });
