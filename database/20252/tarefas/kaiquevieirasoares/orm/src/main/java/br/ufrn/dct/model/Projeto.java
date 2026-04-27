package br.ufrn.dct.model;

import jakarta.persistence.*;
import lombok.*;
import java.time.LocalDate;
import java.util.List;

@Entity
@Table(name = "projeto")
@Getter @Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
@ToString(exclude = {"responsavel", "departamento", "atividades"})
public class Projeto {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer codigo;

    @Column(unique = true)
    private String nome;

    private String descricao;

    @ManyToOne
    @JoinColumn(name = "responsavel")
    private Funcionario responsavel;

    @ManyToOne
    @JoinColumn(name = "depto")
    private Departamento departamento;

    @Column(name = "data_inicio")
    private LocalDate dataInicio;

    @Column(name = "data_fim")
    private LocalDate dataFim;

    @OneToMany(mappedBy = "projeto", fetch = FetchType.EAGER)
    private List<Atividade> atividades;
}
