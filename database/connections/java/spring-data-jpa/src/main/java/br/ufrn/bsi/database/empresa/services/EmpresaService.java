package br.ufrn.bsi.database.empresa.services;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import br.ufrn.bsi.database.empresa.entities.Departamento;
import br.ufrn.bsi.database.empresa.entities.Empregado;
import br.ufrn.bsi.database.empresa.repositories.DepartamentoRepository;
import br.ufrn.bsi.database.empresa.repositories.EmpregadoRepository;

import java.time.LocalDate;
import java.util.List;

@Service
@RequiredArgsConstructor
public class EmpresaService {

    private final EmpregadoRepository empregadoRepository;
    private final DepartamentoRepository departamentoRepository;

    public List<Empregado> listarTodosEmpregados() {
        return empregadoRepository.findAll();
    }

    public List<Departamento> listarTodosDepartamentos() {
        return departamentoRepository.findAll();
    }

    @Transactional
    public void atualizarDados(Integer matricula, LocalDate novaData, String novoEndereco) {
        empregadoRepository.findById(matricula).ifPresent(emp -> {
            emp.setDataNascimento(novaData);
            emp.setEndereco(novoEndereco);
            // O save() não é estritamente necessário dentro de @Transactional se o objeto já é "managed"
            empregadoRepository.save(emp);
        });
    }

    @Transactional
    public Empregado criarNovoSetorEFuncionario(String nomeDepto, Empregado novoEmp) {
        // 1. Criar e salvar o novo departamento
        Departamento depto = departamentoRepository.findByNome(nomeDepto);
        if (depto == null) {
            depto = new Departamento();
            depto.setNome(nomeDepto);
        }

        depto.setDataInicioGerencia(LocalDate.now());
        depto.setGerente(novoEmp); // O novo empregado será o gerente do departamento
        Departamento deptoSalvo = departamentoRepository.save(depto);

        // 2. Associar o empregado ao departamento criado e salvar
        novoEmp.setDepartamento(deptoSalvo);
        return empregadoRepository.save(novoEmp);
    }

    public Empregado buscarEmpregadoCompleto(Integer matricula) {
        return empregadoRepository.findById(matricula).orElse(null);
    }

    public Departamento buscarDepartamentoCompleto(String nomeDepto) {
        return departamentoRepository.findByNome(nomeDepto);
    }

}
