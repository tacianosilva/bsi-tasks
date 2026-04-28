package br.ufrn.bsi.database.empresa;

import lombok.RequiredArgsConstructor;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

import br.ufrn.bsi.database.empresa.entities.Empregado;
import br.ufrn.bsi.database.empresa.services.EmpresaService;

import java.math.BigDecimal;
import java.time.LocalDate;

@Component
@RequiredArgsConstructor
public class Runner implements CommandLineRunner {

    private final EmpresaService empresaService;

    @Override
    public void run(String... args) throws Exception {
        // 1. Listar Departamentos e Empregados existentes
        System.out.println("=== LISTAGEM INICIAL ===");
        empresaService.listarTodosDepartamentos().forEach(d -> System.out.println("Depto: " + d.getNome()));
        empresaService.listarTodosEmpregados().forEach(e -> System.out.println("Emp: " + e.getNome()));

        // 2. Atualizar um empregado (Exemplo: matrícula 101)
        empresaService.atualizarDados(9491, LocalDate.of(1990, 5, 20), "Nova Rua, 123");

        // 3. Criar Novo Depto e Novo Empregado
        Empregado novo = new Empregado();
        novo.setMatricula(2026); // Como não é auto-incremento no seu caso
        novo.setNome("Novo Desenvolvedor");
        novo.setSalario(new BigDecimal("5000.00"));
        novo.setDataNascimento(LocalDate.of(1995, 8, 15));
        novo.setSupervisor(empresaService.buscarEmpregadoCompleto(9491));

        empresaService.criarNovoSetorEFuncionario("Inovação Digital", novo);

        // 4. Buscar e imprimir dados detalhados
        Empregado consultado = empresaService.buscarEmpregadoCompleto(2026);
        if (consultado != null) {
            System.out.println("=== DADOS DO NOVO EMPREGADO ===");
            System.out.println("Nome: " + consultado.getNome());
            System.out.println("Salário: " + consultado.getSalario());
            System.out.println("Supervisor: " + (consultado.getSupervisor() != null ? consultado.getSupervisor().getNome() : "Nenhum"));
            System.out.println("Departamento: " + consultado.getDepartamento().getNome());
            System.out.println("Gerente: " + consultado.getDepartamento().getGerente().getNome());
        }

        consultado = empresaService.buscarEmpregadoCompleto(9495);
        if (consultado != null) {
            System.out.println("=== DADOS EMPREGADO 9495===");
            System.out.println("Nome: " + consultado.getNome());
            System.out.println("Salário: " + consultado.getSalario());
            System.out.println("Supervisor: " + (consultado.getSupervisor() != null ? consultado.getSupervisor().getNome() : "Nenhum"));
            System.out.println("Departamento: " + consultado.getDepartamento().getNome());
            System.out.println("Gerente: " + consultado.getDepartamento().getGerente().getNome());
        }
    }
}
