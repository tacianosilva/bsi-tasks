import { atividadeSchema } from "../schema/atividade.shcema";
import conexaoODBC from "../service/server";
import ProjetoRepository from "./ProjetoRepository";

class AtividadeRepository {
    private conexao: any | null;

    async pegarTodasAtividades() {
        this.conexao = await conexaoODBC();
        try {
            const resultado = await this.conexao.query(`SELECT 
                a.codigo,
                a.descricao AS atividade_descricao,
                a.projeto AS projeto_codigo,
                a.data_inicio,
                a.data_fim,
                p.nome AS projeto_nome,
                p.descricao AS projeto_descricao
                FROM atividade a
                LEFT JOIN projeto p ON p.codigo = a.projeto;`);
            return resultado.filter((key: any) => key != "columns");
        } catch (error) {
            console.error("Erro de conexão ou query:", error);
            return [];
        } finally {
            if (this.conexao) await this.conexao.close();
        }
    }

    async criarAtividade(data: any) {
        const parsed = atividadeSchema.safeParse(data);
        if (!parsed.success) {
            return { success: false, message: "Dados inválidos." };
        }

        const { descricao, projeto, data_fim, data_inicio } = parsed.data;
        this.conexao = await conexaoODBC();

        try {
            let codProjeto: number | null = null;

            if (projeto !== undefined && projeto !== null) {
                const projetoExiste = await this.projetoExiste(projeto);
                if (!projetoExiste) {
                    throw new Error("Projeto informado não existe.");
                }
                codProjeto = projeto;
            }

            await this.conexao.query(
                `INSERT INTO atividade (descricao, projeto, data_fim, data_inicio)
                 VALUES (?, ?, ?, ?)`,
                [descricao, codProjeto, data_fim, data_inicio]
            );

            return { success: true, message: "Atividade criada com sucesso!" };
        } catch (error: any) {
            console.error("Erro de conexão ou query:", error);
            return { success: false, message: error.message };
        } finally {
            if (this.conexao) await this.conexao.close();
        }
    }

    async projetoExiste(projeto: number): Promise<boolean> {
        const codProjeto = await ProjetoRepository.projetoExiste(projeto);
        return !!codProjeto;
    }
}

export default new AtividadeRepository();
