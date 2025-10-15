import { Projeto } from "../database/model/projeto.model";
import { EsquemaMudarLiderProjeto } from "../schema/projeto.schema";
import { FuncionarioRepository } from "./FuncionarioRepository";

const funcionarioRepo = new FuncionarioRepository();

export class ProjetoRepository {
    async getUnique(codigo: number): Promise<boolean> {
        const projeto = await Projeto.findOne({
            where: { codigo: codigo },
        });
        if (projeto) return true;
        return false;
    }

    async mudarLiderDoProjeto(data: unknown) {
        const parsed = EsquemaMudarLiderProjeto.safeParse(data);
        if (!parsed.success) throw new Error("Erro no formato da query");

        const { codigo, responsavel } = parsed.data;

        const funcionarioExiste = await funcionarioRepo.funcinarioExiste(
            responsavel
        );
        if (!funcionarioExiste) throw new Error("Funcionário não encontrado.");

        const projetoExixts = await this.getUnique(codigo);
        if (!projetoExixts) throw new Error("Projeto não encontrado.");

        try {
            await Projeto.update({ responsavel }, { where: { codigo } });
            return true;
        } catch (error) {
            console.error(`Erro ao atualizar: ${data}`);
        }
    }
}
