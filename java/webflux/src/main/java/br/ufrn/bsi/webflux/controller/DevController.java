package br.ufrn.bsi.webflux.controller;

import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

import br.ufrn.bsi.webflux.model.Devs;
import br.ufrn.bsi.webflux.repository.DevRepository;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

@RestController
public class DevController {

    @Autowired
    private DevRepository devRepository;

    @PostMapping("/devs")
    @ResponseStatus(HttpStatus.CREATED)
    public Mono<Devs> createDev(@Valid @RequestBody Devs dev) {
        return devRepository.save(dev);
    }

    @GetMapping("/devs")
    @ResponseStatus(HttpStatus.OK)
    public Flux<Devs> getAllDevs() {
        return devRepository.findAll();
    }

    @GetMapping("/devs/{id}")
    @ResponseStatus(HttpStatus.OK)
    public Mono<ResponseEntity<Devs>> getDevById(@PathVariable(value = "id") String devId) {
        return devRepository.findById(devId)
            .map(savedDev -> ResponseEntity.ok(savedDev))
            .defaultIfEmpty(ResponseEntity.notFound().build());
    }

    @PutMapping("/devs/{id}")
    @ResponseStatus(HttpStatus.NO_CONTENT)
    public Mono<ResponseEntity<Devs>> updateDev(@PathVariable(value = "id") String devId,
                                               @Valid @RequestBody Devs dev) {
        return devRepository.findById(devId)
            .flatMap(existingDev -> {
                existingDev.setName(dev.getName());
                return devRepository.save(existingDev);
            }).map(updateDev -> new ResponseEntity<>(updateDev, HttpStatus.OK))
            .defaultIfEmpty(ResponseEntity.notFound().build());
    }

    @DeleteMapping("/devs/{id}")
    @ResponseStatus(HttpStatus.NO_CONTENT)
    public Mono<ResponseEntity<Void>> deleteDev(@PathVariable(value = "id") String devId) {
        return devRepository.findById(devId)
            .flatMap(existingDev -> 
                devRepository.delete(existingDev)
                    .then(Mono.just(new ResponseEntity<Void>(HttpStatus.OK)))
            )
            .defaultIfEmpty(ResponseEntity.notFound().build());
    }

    @GetMapping(value = "/stream/devs", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
    @ResponseStatus(HttpStatus.OK)
    public Flux<Devs> streamAllDevs() {
        return devRepository.findAll();
    }
}