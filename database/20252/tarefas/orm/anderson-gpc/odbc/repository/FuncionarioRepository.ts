export class FuncionarioRepository {
    private conexao: any | null;
    private codigo: number;

    constructor(conexao: any, codigo: number) {
        this.conexao = conexao;
        this.codigo = codigo;
    }

    async fucionarioExiste(): Promise<any> {
        const [funcionario] = await this.conexao.query(
            "SELECT 1 FROM funcionario WHERE codigo = ?",
            [this.codigo]
        );
        return funcionario;
    }
}
