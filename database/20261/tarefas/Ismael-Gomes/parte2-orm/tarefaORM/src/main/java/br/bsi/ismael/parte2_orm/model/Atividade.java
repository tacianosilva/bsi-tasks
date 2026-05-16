package br.bsi.ismael.parte2_orm.model; // Ajuste para o seu pacote

import jakarta.persistence.*;
import lombok.Data;
import java.time.LocalDate;

@Data
@Entity
@Table(name = "atividade")
public class Atividade {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer codigo;

    private String descricao;

    // Relacionamento: Várias Atividades pertencem a Um Projeto
    @ManyToOne
    @JoinColumn(name = "projeto")
    private Projeto projeto;

    @Column(name = "data_inicio")
    private LocalDate dataInicio;

    @Column(name = "data_fim")
    private LocalDate dataFim;
}
