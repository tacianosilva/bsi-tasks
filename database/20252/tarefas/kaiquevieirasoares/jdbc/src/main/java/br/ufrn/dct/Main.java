package br.ufrn.dct;

import java.sql.*;

public class Main {

    public static void main(String[] args) {
        String url = "jdbc:postgresql://localhost:5433/atividade_db";
        String user = "postgres";
        String password = "password";

        try (Connection conn = DriverManager.getConnection(url, user, password)) {
            System.out.println("Conectado com sucesso ao PostgreSQL via JDBC!\n");

            inserirAtividade(conn, "Desenvolvimento de Testes Unitários", 1);
            atualizarLiderProjeto(conn, 3, 4);
            listarProjetosEAtividades(conn);

        } catch (SQLException e) {
            System.err.println("Erro na conexão ou execução: " + e.getMessage());
            e.printStackTrace();
        }
    }

    /**
     * Questão 5.a: Inserir uma atividade em algum projeto
     */
    private static void inserirAtividade(Connection conn, String descricao, int projetoId) throws SQLException {
        String sql = "INSERT INTO atividade (descricao, projeto, data_inicio, data_fim) VALUES (?, ?, ?, ?)";

        try (PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setString(1, descricao);
            stmt.setInt(2, projetoId);
            stmt.setDate(3, Date.valueOf("2026-04-27"));
            stmt.setDate(4, Date.valueOf("2026-05-15"));

            int rows = stmt.executeUpdate();
            if (rows > 0) {
                System.out.println("-> [JDBC] Atividade '" + descricao + "' inserida com sucesso!");
            }
        }
    }

    /**
     * Questão 5.b: Atualizar o líder de algum projeto
     */
    private static void atualizarLiderProjeto(Connection conn, int projetoId, int novoLiderId) throws SQLException {
        String sql = "UPDATE projeto SET responsavel = ? WHERE codigo = ?";

        try (PreparedStatement stmt = conn.prepareStatement(sql)) {
            stmt.setInt(1, novoLiderId);
            stmt.setInt(2, projetoId);

            int rows = stmt.executeUpdate();
            if (rows > 0) {
                System.out.println("-> [JDBC] Líder do projeto " + projetoId + " atualizado para o funcionário " + novoLiderId + "!");
            }
        }
    }

    /**
     * Questão 5.c: Listar todos os projetos e suas atividades
     */
    private static void listarProjetosEAtividades(Connection conn) throws SQLException {
        String sql = "SELECT p.nome AS nome_projeto, a.descricao AS desc_atividade " +
            "FROM projeto p " +
            "LEFT JOIN atividade a ON p.codigo = a.projeto " +
            "ORDER BY p.nome";

        try (Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {

            System.out.println("\n=== LISTAGEM DE PROJETOS E ATIVIDADES ===");
            while (rs.next()) {
                String projeto = rs.getString("nome_projeto");
                String atividade = rs.getString("desc_atividade");

                System.out.println("Projeto: " + projeto + " | Atividade: " +
                    (atividade != null ? atividade : "(Sem atividades cadastradas)"));
            }
            System.out.println("=========================================\n");
        }
    }
}
