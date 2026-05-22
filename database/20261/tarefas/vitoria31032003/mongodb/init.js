db = db.getSiblingDB("AtividadesProj");

db.projetos.insertMany([
  {
    nome: "Sistema Complementar de Gestão de Atividade de Extensão (SIGAEX)",
    lider: "Diêgo Axel"
  }
]);

db.empregados.insertMany([
  {
    nome: "Vitória Geovanna",
    cargo: "Desenvolvedora"
  },
  {
    nome: "Hildenberg",
    cargo: "Analistar"
  },
  {
    nome: "Diêgo Axel",
    cargo: "Testador"
  },
  {
    nome: "Nathan Lopes",
    cargo: "Desenvolvedor"
  },
  {
    nome: "Tomé",
    cargo: "Desenvolvedor"
  }
]);

db.atividades.insertMany([
  {
    nome: "User Stories - Módulo: Cadastro de Eventos",
    projeto: "Sistema Complementar de Gestão de Atividade de Extensão (SIGAEX)",
    responsavel: "Diêgo Axel"
  },
  {
    nome: "User Story: Gestão de Palestras e Ministrantes",
    projeto: "Sistema Complementar de Gestão de Atividade de Extensão (SIGAEX)",
    responsavel: "Tomé"
  },
  {
    nome: "Documento de Visão",
    projeto: "Sistema Complementar de Gestão de Atividade de Extensão (SIGAEX)",
    responsavel: "Hildenberg"
  }
]);

print("Banco de dados inicializado com sucesso!");
