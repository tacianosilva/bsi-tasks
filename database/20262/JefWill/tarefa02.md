# Tarefa 02 - MER e Projeto de Banco de Dados Relacional

## Q1. Elementos Básicos do Modelo Entidade-Relacionamento (MER)

O Modelo Entidade-Relacionamento (MER), proposto por Peter Chen em 1976, é um modelo conceitual de alto nível utilizado para especificar a estrutura lógica de um banco de dados de maneira independente de aspectos físicos de implementação.

O modelo é fundamentado em três conceitos básicos:

1. **Entidades:** São objetos, pessoas, conceitos ou fatos do mundo real que possuem existência própria e sobre os quais a organização deseja armazenar dados. No diagrama, são comumente representadas por retângulos (por exemplo: `Cliente`, `Projeto`, `Funcionario`). As entidades podem ser concretas (tangíveis, como um funcionário) ou abstratas (conceituais, como uma matrícula ou um projeto).
2. **Atributos:** São as propriedades, características ou descrições que qualificam cada entidade ou relacionamento, definindo os dados que serão guardados (por exemplo: a entidade `Cliente` possui atributos como `codigo`, `nome` e `email_contato`). Entre os atributos, destaca-se o identificador (ou chave primária), cujo valor identifica unicamente cada ocorrência da entidade.
3. **Relacionamentos:** São as associações ou conexões lógicas entre duas ou mais entidades, refletindo a forma como elas interagem no mundo real (por exemplo: a relação entre `Cliente` e `Projeto` através do vínculo *contrata*). Os relacionamentos definem as regras do negócio por meio de restrições estruturais, como a cardinalidade (1:1, 1:N ou N:M).\n