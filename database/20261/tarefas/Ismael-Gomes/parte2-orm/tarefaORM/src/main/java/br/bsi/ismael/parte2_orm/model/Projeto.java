package br.bsi.ismael.parte2_orm.model; // Ajuste para o seu pacote

import jakarta.persistence.*;
import lombok.Data;
import java.time.LocalDate;
import java.util.List;

@Data
@Entity
@Table(name = "projeto")
public class Projeto {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer codigo;

    private String nome;
    private String descricao;

    // Mapeamento simplificado do ID do responsável para focarmos na atualização
    @Column(name = "responsavel")
    private Integer responsavel;

    @Column(name = "depto")
    private Integer depto;

    @Column(name = "data_inicio")
    private LocalDate dataInicio;

    @Column(name = "data_fim")
    private LocalDate dataFim;

    // Relacionamento: Um Projeto tem Várias Atividades
    @OneToMany(mappedBy = "projeto", fetch = FetchType.EAGER)
    private List<Atividade> atividades;
}
