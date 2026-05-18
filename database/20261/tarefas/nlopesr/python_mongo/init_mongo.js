// Conecta/Cria o banco de dados AtividadesProj
db = db.getSiblingDB('AtividadesProj');

// Cria usuário (a ser executado apenas se precisar, o docker-compose cuidará do root, mas podemos criar para a app)
// O Docker vai criar o DB e user root pelas variáveis de ambiente, então aqui só populamos.

// Coleção Projetos
db.projetos.insertMany([
  {
    "nome": "Projeto Alfa",
    "descricao": "Desenvolvimento do novo sistema interno",
    "lider": "João Silva",
    "dataInicio": new Date("2026-01-10"),
    "dataFim": new Date("2026-06-30")
  },
  {
    "nome": "Projeto Beta",
    "descricao": "Migração de infraestrutura para nuvem",
    "lider": "Maria Souza",
    "dataInicio": new Date("2026-03-15"),
    "dataFim": new Date("2026-10-10")
  },
  {
    "nome": "Projeto Gama",
    "descricao": "Auditoria de segurança",
    "lider": "Carlos Oliveira",
    "dataInicio": new Date("2026-02-01"),
    "dataFim": new Date("2026-05-20")
  }
]);

// Coleção Atividades
db.atividades.insertMany([
  {
    "projetoId": db.projetos.findOne({"nome": "Projeto Alfa"})._id,
    "titulo": "Levantamento de Requisitos",
    "descricao": "Entrevistar stakeholders",
    "responsavel": "Ana Costa",
    "status": "Concluído",
    "dataPrevista": new Date("2026-01-20")
  },
  {
    "projetoId": db.projetos.findOne({"nome": "Projeto Alfa"})._id,
    "titulo": "Desenvolvimento Backend",
    "descricao": "Criar as APIs",
    "responsavel": "Marcos Paulo",
    "status": "Em Progresso",
    "dataPrevista": new Date("2026-04-15")
  },
  {
    "projetoId": db.projetos.findOne({"nome": "Projeto Beta"})._id,
    "titulo": "Provisionar Servidores AWS",
    "descricao": "Configurar EC2 e RDS",
    "responsavel": "Lucas Mendes",
    "status": "Pendente",
    "dataPrevista": new Date("2026-04-01")
  }
]);

print("Dados iniciais inseridos com sucesso!");
