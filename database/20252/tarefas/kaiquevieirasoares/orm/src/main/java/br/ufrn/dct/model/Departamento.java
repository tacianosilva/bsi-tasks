package br.ufrn.dct.model;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Table(name = "departamento")
@Getter @Setter
@NoArgsConstructor @AllArgsConstructor
@Builder
@ToString(exclude = "gerente")
public class Departamento {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer codigo;

    private String nome;

    @Column(unique = true)
    private String sigla;

    private String descricao;

    @OneToOne
    @JoinColumn(name = "gerente")
    private Funcionario gerente;
}
