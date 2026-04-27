package br.ufrn.dct.model;

import jakarta.persistence.*;
import lombok.*;
import java.math.BigDecimal;
import java.time.LocalDate;

@Entity
@Table(name = "funcionario")
@Getter @Setter
@NoArgsConstructor @AllArgsConstructor
@Builder
@ToString(exclude = {"supervisor", "departamento"})
public class Funcionario {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer codigo;

    private String nome;
    private Character sexo;

    @Column(name = "dt_nasc")
    private LocalDate dataNascimento;

    private BigDecimal salario;

    @ManyToOne
    @JoinColumn(name = "supervisor")
    private Funcionario supervisor;

    @ManyToOne
    @JoinColumn(name = "depto")
    private Departamento departamento;
}
