import conexaoODBC from "../service/server";
import { FuncionarioRepository } from "./FuncionarioRepository";

class ProjetoRepository {
    private conexao: any | null = null;

    async mudarLiderProjeto(codigo: number, responsavel: number) {
        this.conexao = await conexaoODBC();

        try {
            await this.conexao.beginTransaction();

            const projeto = await this.projetoExiste(codigo);
            if (!projeto) throw new Error("Projeto não encontrado.");

            const funcionario = await this.funcionarioExiste(responsavel);
            if (!funcionario) throw new Error("Responsável não encontrado.");

            await this.conexao.query(
                "UPDATE projeto SET responsavel = ? WHERE codigo = ?",
                [responsavel, codigo]
            );

            await this.conexao.commit();
            return { success: true, message: "Líder atualizado com sucesso!" };
        } catch (error: any) {
            await this.conexao.rollback();
            console.error("Erro ao mudar líder:", error.message);
            return { success: false, message: error.message };
        }
    }

    private async projetoExiste(codigo: number): Promise<any> {
        const [projeto] = await this.conexao.query(
            "SELECT 1 FROM projeto WHERE codigo = ?",
            [codigo]
        );
        return projeto;
    }

    private async funcionarioExiste(responsavel: number): Promise<any>{
        const funcionarioRepo = new FuncionarioRepository(this.conexao, responsavel);
        const funcionario = await funcionarioRepo.fucionarioExiste();
        return funcionario;
    }
}

export default new ProjetoRepository();
