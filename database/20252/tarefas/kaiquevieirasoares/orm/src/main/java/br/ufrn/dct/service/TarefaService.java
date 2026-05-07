package br.ufrn.dct.service;

import br.ufrn.dct.model.Atividade;
import br.ufrn.dct.model.Funcionario;
import br.ufrn.dct.model.Projeto;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDate;
import java.util.List;

@Slf4j
@Service
@RequiredArgsConstructor
public class TarefaService {

    private final ProjetoService projetoService;
    private final AtividadeService atividadeService;
    private final FuncionarioService funcionarioService;

    @Transactional
    public void executarFluxoTarefa() {
        log.info("### Iniciando Processamento da Tarefa 02 ###");

        registrarNovaAtividade(2, "Implementação de Camada de Persistência");
        alterarLiderProjeto(3, 4);
        gerarRelatorioExecutivo();

        log.info("### Processamento Finalizado com Sucesso ###");
    }

    /**
     * Questão 6.a: Encapsula a criação de novas atividades.
     */
    private void registrarNovaAtividade(Integer projetoId, String descricao) {
        Projeto projeto = projetoService.buscarPorId(projetoId);

        Atividade novaAtiv = Atividade.builder()
            .descricao(descricao)
            .projeto(projeto)
            .dataInicio(LocalDate.now())
            .dataFim(LocalDate.now().plusDays(15))
            .build();

        atividadeService.salvar(novaAtiv);
        log.info("-> Atividade '{}' registrada no projeto: {}", descricao, projeto.getNome());
    }

    /**
     * Questão 6.b: Centraliza a troca de responsabilidade de projetos.
     */
    private void alterarLiderProjeto(Integer projetoId, Integer funcionarioId) {
        Projeto projeto = projetoService.buscarPorId(projetoId);
        Funcionario novoLider = funcionarioService.buscarPorId(funcionarioId);

        projeto.setResponsavel(novoLider);
        projetoService.salvar(projeto);

        log.info("-> Liderança do projeto '{}' transferida para: {}", projeto.getNome(), novoLider.getNome());
    }

    /**
     * Questão 6.c: Gera o log estruturado do estado atual do banco.
     */
    private void gerarRelatorioExecutivo() {
        List<Projeto> projetos = projetoService.listarTodos();

        System.out.println("\n" + "=".repeat(50));
        System.out.println("      RELATÓRIO DE PROJETOS E ATIVIDADES");
        System.out.println("=".repeat(50));

        projetos.forEach(p -> {
            String lider = (p.getResponsavel() != null) ? p.getResponsavel().getNome() : "N/A";
            System.out.printf("PROJETO: %-15s | LÍDER: %s%n", p.getNome(), lider);

            if (p.getAtividades().isEmpty()) {
                System.out.println("   [!] Sem atividades cadastradas");
            } else {
                p.getAtividades().forEach(a -> System.out.println("   • " + a.getDescricao()));
            }
            System.out.println("-".repeat(50));
        });
    }
}
