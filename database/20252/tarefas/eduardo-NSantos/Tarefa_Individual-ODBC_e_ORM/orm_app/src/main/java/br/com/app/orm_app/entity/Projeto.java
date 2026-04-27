package br.com.app.orm_app.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

import java.util.List;

@Entity
@Table(name = "projeto")
@Getter
@Setter
public class Projeto {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer codigo;

    private String nome;
    private String descricao;

    @Column(name = "responsavel")
    private Integer responsavel;

    @OneToMany(mappedBy = "projeto")
    private List<Atividade> atividades;
}
