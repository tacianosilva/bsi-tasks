package br.ufrn.dct;

import br.ufrn.dct.service.TarefaService;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class Main {
    public static void main(String[] args) {
        SpringApplication.run(Main.class, args);
    }

    @Bean
    public CommandLineRunner run(TarefaService tarefaService) {
        return args -> {
            tarefaService.executarFluxoTarefa();
        };
    }
}
