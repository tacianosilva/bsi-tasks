package br.ufrn.bsi.database.empresa.entities;

import java.math.BigDecimal;
import java.time.LocalDate;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Table;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.ManyToOne;
import lombok.*;

@Entity
@Table(name = "empregado")
@Getter // Cria todos os getters
@Setter // Cria todos os setters
@NoArgsConstructor // Construtor vazio (obrigatório para JPA)
@AllArgsConstructor // Construtor com todos os campos
@EqualsAndHashCode(onlyExplicitlyIncluded = true) // Gera equals/hashCode seguro
public class Empregado {

    @Id
    @EqualsAndHashCode.Include // Usa apenas o ID para comparar objetos
    private Integer matricula;

    @Column(nullable = false)
    private String nome;

    @Column(name = "datanasc")
    private LocalDate dataNascimento;

    private String endereco;

    private Character sexo;

    private BigDecimal salario;

    // Autorrelacionamento: Um supervisor orienta vários empregados
    @ManyToOne
    @JoinColumn(name = "supervisor")
    private Empregado supervisor;

    // Relacionamento com Departamento
    @ManyToOne
    @JoinColumn(name = "depto")
    private Departamento departamento;

}
