import { Atividade } from "../database/model/atividade.model";
import { Projeto } from "../database/model/projeto.model";
import { AtividadeCreateInput as AtividadeSchemaInput } from "../schema/atividade.schema";
import { ProjetoRepository } from "./ProjetoRepository";

const projetoRepo = new ProjetoRepository();

export class AtividadeRepository {
    async getAll() {
        const atividades = await Atividade.findAll({
            include: {
                model: Projeto,
                as: "projetoAssociado",
            },
        });
        return atividades.map((a) => a.toJSON());
    }

    async createAtividade(data: unknown) {
        const parsed = AtividadeSchemaInput.safeParse(data);
        if (!parsed.success) throw new Error("Erro no formato da query!");
        const result = parsed.data;

        const existeProjeto = result.projeto
            ? await projetoRepo.getUnique(result.projeto)
            : false;

        if (!existeProjeto) result.projeto = null;

        await Atividade.create(result);
    }
}
