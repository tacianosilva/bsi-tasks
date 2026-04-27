package br.com.app.orm_app.entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Entity
@Table(name = "atividade")
@Getter
@Setter
public class Atividade {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer codigo;

    private String descricao;

    @ManyToOne
    @JoinColumn(name = "projeto")
    private Projeto projeto;
}
