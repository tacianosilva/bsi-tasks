package br.ufrn.bsi.webflux.repository;

import org.springframework.data.mongodb.repository.ReactiveMongoRepository;
import org.springframework.stereotype.Repository;

import br.ufrn.bsi.webflux.model.Devs;

@Repository
public interface DevRepository extends ReactiveMongoRepository<Devs, String> {
    
}
