import { Funcionario } from "../database/model/funcionario.model";

export class FuncionarioRepository {
    async funcinarioExiste(codigo: number) {
        const funcionario = await Funcionario.findByPk(codigo);
        if (funcionario?.dataValues) return true;
        return false;
    } 
}