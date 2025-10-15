import conexaoODBC from "../service/server";

class AtividadeRepository {
    private conexao: any | null;

    async pegarTodasAtividades() {
        this.conexao = await conexaoODBC();
        try {
            const resultado = await this.conexao.query(`SELECT 
                a.codigo,
                a.descricao AS atividade_descricao,
                a.projeto AS projeto_codigo,
                a.data_inicio,
                a.data_fim,
                p.nome AS projeto_nome,
                p.descricao AS projeto_descricao
                FROM atividade a
                JOIN projeto p ON p.codigo = a.projeto;`
            );
            return resultado.filter((key: any) => key != 'columns');
        } catch (error) {
            console.error("Erro de conexão ou query:", error);
            return [];
        } finally {
            if (this.conexao) await this.conexao.close();
        }
    }

    async criarAtividade() {

    }
}

export default new AtividadeRepository();