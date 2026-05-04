package br.bsi.ismael.parte2_orm.repository;

import br.bsi.ismael.parte2_orm.model.Projeto;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ProjetoRepository extends JpaRepository<Projeto, Integer> {
}
