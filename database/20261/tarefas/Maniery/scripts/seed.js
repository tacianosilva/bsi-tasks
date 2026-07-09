db = db.getSiblingDB("AtividadesProj")

db.empregados.insertMany([
  { nome: "Ana" },
  { nome: "Carlos" },
  { nome: "Maria" }
])

db.projetos.insertMany([
  { nome: "Sistema BD", lider: "Ana" },
  { nome: "API", lider: "Carlos" },
  { nome: "Web App", lider: "Maria" }
])

db.atividades.insertMany([
  { descricao: "Modelar BD", projeto: "Sistema BD" },
  { descricao: "Criar API", projeto: "API" },
  { descricao: "Frontend", projeto: "Web App" }
])