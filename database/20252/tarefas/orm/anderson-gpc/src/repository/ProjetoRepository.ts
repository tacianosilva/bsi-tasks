import { Projeto } from "../database/model/projeto.model";

export class ProjetoRepository {
    async getUnique(codigo: number): Promise<boolean> {
        const projeto = await Projeto.findOne({
            where: {codigo: codigo}
        })
        if (projeto) return true;
        return false;
    }
}
