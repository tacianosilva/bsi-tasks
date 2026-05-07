package br.ufrn.dct.service;

import br.ufrn.dct.model.Funcionario;
import br.ufrn.dct.repository.FuncionarioRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class FuncionarioService {
    private final FuncionarioRepository repository;

    public Funcionario buscarPorId(Integer id) {
        return repository.findById(id).orElseThrow(() -> new RuntimeException("Funcionário não encontrado"));
    }
}
