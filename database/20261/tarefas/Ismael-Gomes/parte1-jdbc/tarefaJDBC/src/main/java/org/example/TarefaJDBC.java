package org.example;

import java.sql.Connection;
import java.sql.Date;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class TarefaJDBC {

    private static final String URL = "jdbc:postgresql://localhost:5433/atividade_db";
    private static final String USER = "postgres";
    private static final String PASSWORD = "admin";

    public static void main(String[] args) {
        try (Connection conn = DriverManager.getConnection(URL, USER, PASSWORD)) {
            System.out.println("Conexão com o banco estabelecida com sucesso!\n");

            inserirAtividade(conn, "BD - Atividade Extra JDBC", 3, Date.valueOf("2024-05-01"), Date.valueOf("2024-05-15"));

            atualizarLiderProjeto(conn, 1, 4);

            listarProjetosEAtividades(conn);

        } catch (SQLException e) {
            System.err.println("❌ Erro ao conectar ou executar no banco de dados.");
            e.printStackTrace();
        }
    }

    // Questão 5 - a. Inserir uma atividade
    private static void inserirAtividade(Connection conn, String descricao, int projetoId, Date dataInicio, Date dataFim) throws SQLException {
        String sql = "INSERT INTO atividade (descricao, projeto, data_inicio, data_fim) VALUES (?, ?, ?, ?)";
        try (PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setString(1, descricao);
            stmt.setInt(2, projetoId);
            stmt.setDate(3, dataInicio);
            stmt.setDate(4, dataFim);
            int linhasAfetadas = stmt.executeUpdate();
            System.out.println("Sucesso: " + linhasAfetadas + " atividade(s) inserida(s).");
        }
    }

    // Questão 5 - b. Atualizar o líder
    private static void atualizarLiderProjeto(Connection conn, int projetoId, int novoResponsavelId) throws SQLException {
        String sql = "UPDATE projeto SET responsavel = ? WHERE codigo = ?";
        try (PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setInt(1, novoResponsavelId);
            stmt.setInt(2, projetoId);
            int linhasAfetadas = stmt.executeUpdate();
            System.out.println("Sucesso: Líder do projeto " + projetoId + " atualizado (" + linhasAfetadas + " linha afetada).");
        }
    }

    // Questão 5 - c. Listar projetos e atividades
    private static void listarProjetosEAtividades(Connection conn) throws SQLException {
        System.out.println("\n--- Lista de Projetos e Atividades ---");
        String sql = "SELECT p.nome AS projeto_nome, a.descricao AS atividade_desc " +
            "FROM projeto p " +
            "LEFT JOIN atividade a ON p.codigo = a.projeto " +
            "ORDER BY p.codigo, a.codigo";

        try (PreparedStatement stmt = conn.prepareStatement(sql);
             ResultSet rs = stmt.executeQuery()) {

            String projetoAtual = "";
            while (rs.next()) {
                String projeto = rs.getString("projeto_nome");
                String atividade = rs.getString("atividade_desc");

                if (!projeto.equals(projetoAtual)) {
                    System.out.println("\nProjeto: " + projeto);
                    projetoAtual = projeto;
                }

                if (atividade != null) {
                    System.out.println("  -> Atividade: " + atividade);
                } else {
                    System.out.println("  -> (Nenhuma atividade cadastrada)");
                }
            }
            System.out.println("--------------------------------------\n");
        }
    }
}
