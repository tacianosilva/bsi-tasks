package br.ufrn.bsi.database.empresa.repositories;

import org.springframework.stereotype.Repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import br.ufrn.bsi.database.empresa.entities.Departamento;

@Repository
public interface DepartamentoRepository extends JpaRepository<Departamento, Integer> {

    List<Departamento> findByNomeContaining(String nome);

    Departamento findByNome(String nome);
}
