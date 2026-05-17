package br.ufrn.bsi.database.empresa;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;
import java.sql.Connection;
import javax.sql.DataSource;

@Component
public class DatabaseTestConfig implements CommandLineRunner {

    @Value("${spring.datasource.url}")
    private String dbUrl;

    private final DataSource dataSource;

    public DatabaseTestConfig(DataSource dataSource) {
        this.dataSource = dataSource;
    }

    @Override
    public void run(String... args) throws Exception {
        System.out.println("--- Verificando Configurações ---");
        System.out.println("URL de Conexão: " + dbUrl);

        try (Connection conn = dataSource.getConnection()) {
            System.out.println("Conexão JDBC estabelecida com sucesso: " + conn.getMetaData().getDatabaseProductName());
        } catch (Exception e) {
            System.err.println("ERRO AO CONECTAR NO BANCO: " + e.getMessage());
        }
    }
}
