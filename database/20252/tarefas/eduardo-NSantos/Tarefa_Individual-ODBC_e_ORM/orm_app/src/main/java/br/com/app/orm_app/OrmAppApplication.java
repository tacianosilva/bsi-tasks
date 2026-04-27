package br.com.app.orm_app;

import br.com.app.orm_app.service.ProjetoService;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class OrmAppApplication {

    public static void main(String[] args) {
        SpringApplication.run(OrmAppApplication.class, args);
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
