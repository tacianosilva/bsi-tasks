package br.ufrn.dct.service;

import br.ufrn.dct.model.Atividade;
import br.ufrn.dct.repository.AtividadeRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class AtividadeService {
    private final AtividadeRepository repository;

    public void salvar(Atividade atividade) {
        repository.save(atividade);
    }
}
