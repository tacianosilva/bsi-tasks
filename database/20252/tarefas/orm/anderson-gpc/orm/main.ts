import readline from "readline";
import { AtividadeRepository } from "./repository/AtividadeRepository";
import { FuncionarioRepository } from "./repository/FuncionarioRepository";
import { ProjetoRepository } from "./repository/ProjetoRepository";

const atividadeRepo = new AtividadeRepository();
const projetoRepo = new ProjetoRepository();
const funcionarioRepo = new FuncionarioRepository();

async function pegarTodasAtividade() {
    const todas = await atividadeRepo.pegarTodas();
    console.log("\n📋 Todas as atividades:");
    console.table(todas);
}

async function criarUmaAtividade() {
    const data = {
        descricao: "Atividade 1",
        data_inicio: "2025-10-15",
        data_fim: "2025-10-20",
    };
    await atividadeRepo.criarAtividade(data);
    console.log("✅ Atividade criada com sucesso!");
}

async function verificarCodigoProjeto() {
    const codigo = 10;
    const existe = await projetoRepo.projetoExiste(codigo);
    console.log(`🔎 Projeto com código ${codigo}:`, existe ? "Existe" : "Não existe");
}

async function verificarCodigoFuncionario() {
    const codigo = 1;
    const existe = await funcionarioRepo.funcinarioExiste(codigo);
    console.log(`👤 Funcionário com código ${codigo}:`, existe ? "Existe" : "Não existe");
}

async function mudarLiderDoProjeto() {
    const data = { codigo: 3, responsavel: 1 };
    const projeto = await projetoRepo.mudarLiderDoProjeto(data);
    console.log("👑 Novo líder do projeto definido:", projeto);
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

function mostrarMenu() {
    console.log(`
==============================
     MENU DE OPERAÇÕES
==============================
1 - Listar todas as atividades
2 - Criar uma nova atividade
3 - Verificar código de projeto
4 - Verificar código de funcionário
5 - Mudar líder de projeto
0 - Sair
`);
}

async function executarOpcao(opcao: string) {
    switch (opcao) {
        case "1":
            await pegarTodasAtividade();
            break;
        case "2":
            await criarUmaAtividade();
            break;
        case "3":
            await verificarCodigoProjeto();
            break;
        case "4":
            await verificarCodigoFuncionario();
            break;
        case "5":
            await mudarLiderDoProjeto();
            break;
        case "0":
            console.log("👋 Encerrando...");
            rl.close();
            return;
        default:
            console.log("❌ Opção inválida!");
    }
    exibirMenu();
}

function exibirMenu() {
    mostrarMenu();
    rl.question("Escolha uma opção: ", (opcao) => executarOpcao(opcao));
}

// Inicialização
console.clear();
console.log("🚀 Mini Sistema de Gestão de Projetos");
exibirMenu();
