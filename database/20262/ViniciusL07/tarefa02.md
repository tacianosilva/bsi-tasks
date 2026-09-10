# Tarefa 02 - Modelo Entidade-Relacionamento e Modelo Relacional


## Questão 01 - Elementos Básicos do Modelo Entidade-Relacionamento (MER)

O Modelo Entidade-Relacionamento (proposto originalmente por Peter Chen em 1976) fundamenta-se em três elementos conceituais principais:

1. **Entidades:**
   * **Conceito:** Representam objetos, seres ou conceitos do mundo real que possuem existência própria e sobre os quais se deseja armazenar dados.
   * **Exemplo:** `CLIENTE`, `FUNCIONARIO`, `PROJETO`.
   * **Classificação:** Podem ser **fortes** (existem de forma autônoma) ou **fracas** (sua existência depende da existência de outra entidade pai).

2. **Atributos:**
   * **Conceito:** São as propriedades, características ou dados descritivos que definem e qualificam uma entidade ou um relacionamento.
   * **Exemplo:** Em `FUNCIONARIO`, os atributos podem ser `codigo`, `nome` e `email`.
   * **Identificador (Chave Primária Conceitual):** Atributo (ou conjunto de atributos) cujo valor é único para cada instância da entidade, permitindo distingui-las sem ambiguidade.

3. **Relacionamentos:**
   * **Conceito:** Associações lógicas existentes entre duas ou mais entidades, representando como interagem no domínio modelado.
   * **Exemplo:** A associação `ALOCA` entre `SQUAD` e `FUNCIONARIO`.
   * **Cardinalidade:** Restrição estrutural que define o número mínimo e máximo de ocorrências de uma entidade que podem estar associadas a ocorrências de outra entidade (ex.: `1:1`, `1:N`, `N:M`).