import readline from "readline";
import AtividadeRepository from "./repository/AtividadeRepository";
import ProjetoRepository from "./repository/ProjetoRepository";

async function pegarTodasAtividades() {
    const atividades = await AtividadeRepository.pegarTodasAtividades();
    console.log("\n=== Atividades ===");
    console.log(atividades);
}

async function atualizarLiderProjeto(data: { codigo: number, responsavel: number }) {
    const projeto = await ProjetoRepository.mudarLiderProjeto(data.codigo, data.responsavel);
    console.log("\n=== Projeto atualizado ===");
    console.log(projeto);
}

async function criarAtividade(data: { descricao: string, data_inicio: string, data_fim: string }) {
    const atividade = await AtividadeRepository.criarAtividade(data);
    console.log("\n=== Atividade criada ===");
    console.log(atividade);
}

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function perguntar(query: string): Promise<string> {
    return new Promise(resolve => rl.question(query, resolve));
}

async function menu() {
    console.log("\n=== Menu ===");
    console.log("1 - Ver todas as atividades");
    console.log("2 - Atualizar líder de projeto");
    console.log("3 - Criar atividade");
    console.log("0 - Sair");

    const opcao = await perguntar("Escolha uma opção: ");

    switch (opcao) {
        case "1":
            await pegarTodasAtividades();
            break;
        case "2":
            const codigo = parseInt(await perguntar("Digite o código do projeto: "));
            const responsavel = parseInt(await perguntar("Digite o ID do novo responsável: "));
            await atualizarLiderProjeto({ codigo, responsavel });
            break;
        case "3":
            const descricao = await perguntar("Digite a descrição da atividade: ");
            const data_inicio = await perguntar("Digite a data de início (YYYY-MM-DD): ");
            const data_fim = await perguntar("Digite a data de fim (YYYY-MM-DD): ");
            await criarAtividade({ descricao, data_inicio, data_fim });
            break;
        case "0":
            console.log("Saindo...");
            rl.close();
            return;
        default:
            console.log("Opção inválida!");
    }


    menu();
}

menu();
