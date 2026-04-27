package br.bsi.ismael.parte2_orm.repository;

import br.bsi.ismael.parte2_orm.model.Atividade;
import org.springframework.data.jpa.repository.JpaRepository;

public interface AtividadeRepository extends JpaRepository<Atividade, Integer> {
}
