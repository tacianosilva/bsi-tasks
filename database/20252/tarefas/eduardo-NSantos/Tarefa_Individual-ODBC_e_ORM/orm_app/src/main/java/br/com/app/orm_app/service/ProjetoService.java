package br.com.app.orm_app.service;

import br.com.app.orm_app.entity.Atividade;
import br.com.app.orm_app.entity.Projeto;
import br.com.app.orm_app.repository.AtividadeRepository;
import br.com.app.orm_app.repository.ProjetoRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
@RequiredArgsConstructor
public class ProjetoService {

    private final ProjetoRepository projetoRepo;
    private final AtividadeRepository atividadeRepo;

    public void inserirAtividade() {
        Projeto projeto = projetoRepo.findById(1).orElseThrow();

        Atividade atividade = new Atividade();
        atividade.setDescricao("Atividade via ORM");
        atividade.setProjeto(projeto);

        atividadeRepo.save(atividade);

        System.out.println("Atividade inserida!");
    }

    public void atualizarProjeto() {
        Projeto projeto = projetoRepo.findById(1).orElseThrow();

        projeto.setResponsavel(1);

        projetoRepo.save(projeto);

        System.out.println("Projeto atualizado!");
    }

    @Transactional
    public void listarProjetos() {
        List<Projeto> projetos = projetoRepo.findAll();

        for (Projeto p : projetos) {
            System.out.println("Projeto: " + p.getNome());

            if (p.getAtividades() != null) {
                p.getAtividades().forEach(a ->
                    System.out.println("Atividade: " + a.getDescricao())
                );
            }

            System.out.println("----------------------");
        }
    }
}
