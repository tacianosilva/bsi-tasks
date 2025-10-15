import { Funcionario } from "../database/model/funcionario.model";

export class FuncionarioRepository {
    async getUnique(codigo: number) {
        const funcionario = await Funcionario.findByPk(codigo);
        return funcionario?.dataValues;
    } 
}