package br.com.app.jdbc_app;

import br.com.app.jdbc_app.service.ProjetoService;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class JdbcAppApplication {

    public static void main(String[] args) {
        SpringApplication.run(JdbcAppApplication.class, args);
    }

    @Bean
    CommandLineRunner run(ProjetoService service) {
        return args -> {
            service.inserirAtividade();
            service.atualizarProjeto();
            service.listarProjetos();
        };
    }
}
