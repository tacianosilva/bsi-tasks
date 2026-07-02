use AtividadesProj

// Projetos
db.projetos.insertMany([
  { nome: "Sistema de E-commerce", lider: "Mariana Araujo", dataInicio: new Date(), status: "ativo" },
  { nome: "App Mobile de Entregas", lider: "Joao Pedro", dataInicio: new Date(), status: "planejado" },
  { nome: "Dashboard de BI", lider: "Ana Clara", dataInicio: new Date(), status: "concluido" }
])

// Atividades
const projetoEcommerce = db.projetos.findOne({ nome: "Sistema de E-commerce" })._id
const projetoApp = db.projetos.findOne({ nome: "App Mobile de Entregas" })._id
const projetoDashboard = db.projetos.findOne({ nome: "Dashboard de BI" })._id

db.atividades.insertMany([
  { titulo: "Configurar ambiente", responsavel: "Mariana", prazo: new Date(), concluida: false, projetoId: projetoEcommerce },
  { titulo: "Desenvolver API", responsavel: "Carlos", prazo: new Date(), concluida: false, projetoId: projetoEcommerce },
  { titulo: "Implementar frontend", responsavel: "Fernanda", prazo: new Date(), concluida: true, projetoId: projetoApp },
  { titulo: "Criar graficos", responsavel: "Ana Clara", prazo: new Date(), concluida: true, projetoId: projetoDashboard }
])

// Empregados
db.empregados.insertMany([
  { nome: "Mariana Araujo", email: "mariana@empresa.com", cargo: "Gerente" },
  { nome: "Carlos Silva", email: "carlos@empresa.com", cargo: "Dev Backend" },
  { nome: "Fernanda Lima", email: "fernanda@empresa.com", cargo: "Dev Frontend" }
])

print("✅ Banco de dados inicializado com sucesso!")
