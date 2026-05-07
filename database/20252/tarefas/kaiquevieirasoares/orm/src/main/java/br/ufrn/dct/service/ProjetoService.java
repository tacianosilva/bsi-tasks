package br.ufrn.dct.service;

import br.ufrn.dct.model.Projeto;
import br.ufrn.dct.repository.ProjetoRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import java.util.List;

@Service
@RequiredArgsConstructor
public class ProjetoService {
    private final ProjetoRepository repository;

    public Projeto buscarPorId(Integer id) {
        return repository.findById(id).orElseThrow(() -> new RuntimeException("Projeto não encontrado"));
    }

    public void salvar(Projeto projeto) {
        repository.save(projeto);
    }

    public List<Projeto> listarTodos() {
        return repository.findAll();
    }
}
