import conexaoODBC from "../service/server";
import { FuncionarioRepository } from "./FuncionarioRepository";

class ProjetoRepository {
    private conexao: any | null = null;

    private async getConexao() {
        if (!this.conexao) {
            this.conexao = await conexaoODBC();
        }
        return this.conexao;
    }

    async mudarLiderProjeto(codigo: number, responsavel: number) {
        const conexao = await this.getConexao();

        try {
            await conexao.beginTransaction();

            const projeto = await this.projetoExiste(codigo);
            if (!projeto) throw new Error("Projeto não encontrado.");

            const funcionario = await this.funcionarioExiste(responsavel);
            if (!funcionario) throw new Error("Responsável não encontrado.");

            await conexao.query(
                "UPDATE projeto SET responsavel = ? WHERE codigo = ?",
                [responsavel, codigo]
            );

            await conexao.commit();
            return { success: true, message: "Líder atualizado com sucesso!" };
        } catch (error: any) {
            await conexao.rollback();
            console.error("Erro ao mudar líder:", error.message);
            return { success: false, message: error.message };
        } finally {
            if (this.conexao) await this.conexao.close();
            this.conexao = null;
        }
    }

    async projetoExiste(codigo: number): Promise<any> {
        const conexao = await this.getConexao();
        const [projeto] = await conexao.query(
            "SELECT 1 FROM projeto WHERE codigo = ?",
            [codigo]
        );
        return projeto;
    }

    private async funcionarioExiste(responsavel: number): Promise<any> {
        const conexao = await this.getConexao();
        const funcionarioRepo = new FuncionarioRepository(conexao, responsavel);
        const funcionario = await funcionarioRepo.fucionarioExiste();
        return funcionario;
    }
}

export default new ProjetoRepository();
