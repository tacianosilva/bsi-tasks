package br.ufrn.bsi.database.empresa.repositories;

import org.springframework.stereotype.Repository;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;
import br.ufrn.bsi.database.empresa.entities.Empregado;

@Repository
public interface EmpregadoRepository extends JpaRepository<Empregado, Integer> {
    // Você pode criar métodos customizados aqui se precisar
    List<Empregado> findByNomeContaining(String nome);
}
