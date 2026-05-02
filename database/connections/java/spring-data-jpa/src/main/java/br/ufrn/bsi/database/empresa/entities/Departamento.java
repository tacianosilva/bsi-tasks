package br.ufrn.bsi.database.empresa.entities;

import java.time.LocalDate;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Table;
import jakarta.persistence.criteria.CriteriaBuilder.In;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import jakarta.persistence.OneToOne;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import lombok.AllArgsConstructor;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Entity
@Table(name = "departamento")
@Getter // Cria todos os getters
@Setter // Cria todos os setters
@NoArgsConstructor // Construtor vazio (obrigatório para JPA)
@AllArgsConstructor // Construtor com todos os campos
@EqualsAndHashCode(onlyExplicitlyIncluded = true) // Gera equals/hashCode seguro
public class Departamento {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY) // Gera ID automaticamente
    @EqualsAndHashCode.Include // Usa apenas o ID para comparar objetos
    @Column(name = "coddep")
    private Integer codigo;

    @Column(name = "nomedep", nullable = false, unique = true)
    private String nome;

    @Column(name = "datainiciogerencia")
    private LocalDate dataInicioGerencia;

    // Autorrelacionamento: Um supervisor orienta vários empregados
    @OneToOne
    @JoinColumn(name = "gerente")
    private Empregado gerente;

}
