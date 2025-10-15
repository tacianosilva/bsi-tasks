import { Atividade } from "../database/model/atividade.model";
import { Projeto } from "../database/model/projeto.model";
import { EsquemaCriarAtividade as AtividadeSchemaInput } from "../schema/atividade.schema";
import { ProjetoRepository } from "./ProjetoRepository";

const projetoRepo = new ProjetoRepository();

export class AtividadeRepository {
    async pegarTodas() {
        const atividades = await Atividade.findAll({
            include: {
                model: Projeto,
                as: "projetoAssociado",
                attributes: ["nome", "descricao"],
            },
        });
        return atividades.map((a) => a.toJSON());
    }

    async criarAtividade(data: unknown) {
        const parsed = AtividadeSchemaInput.safeParse(data);
        if (!parsed.success) throw new Error("Erro no formato da query!");
        const result = parsed.data;

        const existeProjeto = result.projeto
            ? await projetoRepo.projetoExiste(result.projeto)
            : false;

        if (!existeProjeto) result.projeto = null;

        await Atividade.create(result);
    }
}
