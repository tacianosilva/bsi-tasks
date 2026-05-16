package br.bsi.ismael.parte2_orm;

import br.bsi.ismael.parte2_orm.model.Atividade;
import br.bsi.ismael.parte2_orm.model.Projeto;
import br.bsi.ismael.parte2_orm.repository.AtividadeRepository;
import br.bsi.ismael.parte2_orm.repository.ProjetoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.time.LocalDate;
import java.util.List;
import java.util.Optional;

@SpringBootApplication
public class Parte2OrmApplication implements CommandLineRunner {

    @Autowired
    private ProjetoRepository projetoRepository;

    @Autowired
    private AtividadeRepository atividadeRepository;

    public static void main(String[] args) {
        SpringApplication.run(Parte2OrmApplication.class, args);
    }

    @Override
    public void run(String... args) throws Exception {
        System.out.println("\n🚀 Iniciando operações com Spring Data JPA (ORM)...\n");

        inserirAtividadeORM();

        atualizarLiderProjetoORM();

        listarProjetosEAtividadesORM();

        System.out.println("\n✅ Operações ORM finalizadas com sucesso!");
    }

    private void inserirAtividadeORM() {
        Optional<Projeto> projetoOpt = projetoRepository.findById(2);

        if (projetoOpt.isPresent()) {
            Projeto projeto = projetoOpt.get();

            Atividade novaAtividade = new Atividade();
            novaAtividade.setDescricao("Monitoria - Atividade Extra ORM");
            novaAtividade.setProjeto(projeto); // Associamos o objeto Projeto à Atividade
            novaAtividade.setDataInicio(LocalDate.parse("2024-06-01"));
            novaAtividade.setDataFim(LocalDate.parse("2024-06-15"));

            atividadeRepository.save(novaAtividade);
            System.out.println("Sucesso: Atividade inserida no projeto " + projeto.getNome());
        }
    }

    private void atualizarLiderProjetoORM() {
        Optional<Projeto> projetoOpt = projetoRepository.findById(2);

        if (projetoOpt.isPresent()) {
            Projeto projeto = projetoOpt.get();

            projeto.setResponsavel(3);

            projetoRepository.save(projeto);
            System.out.println("Sucesso: Líder do projeto " + projeto.getNome() + " atualizado.");
        }
    }

    private void listarProjetosEAtividadesORM() {
        System.out.println("\n--- Lista de Projetos e Atividades (ORM) ---");

        List<Projeto> projetos = projetoRepository.findAll();

        for (Projeto projeto : projetos) {
            System.out.println("\nProjeto: " + projeto.getNome() + " (Líder ID: " + projeto.getResponsavel() + ")");

            // Como mapeamos @OneToMany, o Spring já traz a lista de atividades do banco pra gente!
            if (projeto.getAtividades() != null && !projeto.getAtividades().isEmpty()) {
                for (Atividade atividade : projeto.getAtividades()) {
                    System.out.println("  -> Atividade: " + atividade.getDescricao());
                }
            } else {
                System.out.println("  -> (Nenhuma atividade cadastrada)");
            }
        }
        System.out.println("--------------------------------------------\n");
    }
}
