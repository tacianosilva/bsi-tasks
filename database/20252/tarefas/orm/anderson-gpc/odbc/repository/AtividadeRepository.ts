import conexaoODBC from "../service/server";
import odbc from "odbc";

class AtividadeRepository {
    async pegarTodasAtividades() {
        let conexao: odbc.Connection | null = null;
        try {
            conexao = await conexaoODBC();
            const resultado = await conexao.query(`SELECT 
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
            return resultado.filter((key) => key != 'columns');
        } catch (error) {
            console.error("Erro de conexão ou query:", error);
            return [];
        } finally {
            if (conexao) await conexao.close();
        }
    }
}

export default new AtividadeRepository();