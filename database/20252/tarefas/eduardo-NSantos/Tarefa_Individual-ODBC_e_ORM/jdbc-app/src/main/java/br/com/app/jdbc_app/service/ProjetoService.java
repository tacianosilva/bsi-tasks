package br.com.app.jdbc_app.service;

import br.com.app.jdbc_app.util.LeitorSQL;
import lombok.RequiredArgsConstructor;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class ProjetoService {

    private final JdbcTemplate jdbcTemplate;


    public void inserirAtividade() throws Exception {
        String sql = LeitorSQL.ler("sql/inserir_atividade.sql");

        jdbcTemplate.update(sql, "Atividade via Spring JDBC", 1);

        System.out.println("Atividade inserida!");
    }

    public void atualizarProjeto() throws Exception {
        String sql = LeitorSQL.ler("sql/atualizar_projeto.sql");

        jdbcTemplate.update(sql, 1, 1);

        System.out.println("Projeto atualizado!");
    }

    public void listarProjetos() throws Exception {
        String sql = LeitorSQL.ler("sql/listar_projetos.sql");

        jdbcTemplate.query(sql, rs -> {
            System.out.println("Projeto: " + rs.getString("projeto"));
            System.out.println("Atividade: " + rs.getString("atividade"));
            System.out.println("----------------------");
        });
    }
}
