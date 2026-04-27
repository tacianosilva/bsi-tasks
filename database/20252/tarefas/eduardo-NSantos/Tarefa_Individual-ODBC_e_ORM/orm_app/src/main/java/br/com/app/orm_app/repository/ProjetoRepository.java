package br.com.app.orm_app.repository;

import br.com.app.orm_app.entity.Projeto;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ProjetoRepository extends JpaRepository<Projeto, Integer> {
}
