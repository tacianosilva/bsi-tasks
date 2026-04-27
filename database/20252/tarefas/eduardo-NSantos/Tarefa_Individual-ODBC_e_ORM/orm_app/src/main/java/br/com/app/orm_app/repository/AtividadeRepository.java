package br.com.app.orm_app.repository;

import br.com.app.orm_app.entity.Atividade;
import org.springframework.data.jpa.repository.JpaRepository;

public interface AtividadeRepository extends JpaRepository<Atividade, Integer> {
}
