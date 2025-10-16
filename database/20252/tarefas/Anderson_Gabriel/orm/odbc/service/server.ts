import odbc from "odbc";

async function conexaoODBC(): Promise<odbc.Connection> {
    try {
        return await odbc.connect("DSN=MeuPostgres");
    } catch {
        throw new Error('Erro ao solicitar a conexão!');
    }
}

export default conexaoODBC;
