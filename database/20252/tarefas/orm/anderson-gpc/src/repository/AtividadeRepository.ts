import { Atividade } from "../database/model/atividade.model";
import { Projeto } from "../database/model/projeto.model";

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
}
