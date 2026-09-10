# Tarefa 02 - MER e Projeto de Banco de Dados Relacional

**Aluno:** Andriel Pereira Nogueira  
**Usuário GitHub:** @Andriel-Nogueira  
**Disciplina:** Banco de Dados  
**Issue Relacionada:** #418

---

## Questão 01: Elementos Básicos do MER

O Modelo Entidade-Relacionamento (MER) é estruturado sobre três elementos básicos primordiais:

1. **Entidades:** Representam objetos, conceitos ou coisas do mundo real sobre as quais se deseja armazenar dados.
   * *Exemplo:* `CLIENTE`, `SQUAD`, `TAREFA`.
2. **Atributos:** São as características ou propriedades que descrevem e qualificam cada entidade. Podem ser simples, compostos, multivalorados ou identificadores (chaves).
   * *Exemplo:* A entidade `CLIENTE` possui os atributos `nome`, `email` e `cnpj`.
3. **Relacionamentos:** Definem as associações e interações lógicas existentes entre duas ou mais entidades, descrevendo como elas se conectam no domínio do negócio.
   * *Exemplo:* A entidade `SQUAD` **resolve** a entidade `TAREFA`.

---

## Questão 02: Notações para Diagramas ER

Existem diversas notações gráficas para a modelagem de Diagramas Entidade-Relacionamento (DER). As mais difundidas incluem:

* **Notação de Chen (Original):** Utiliza retângulos para Entidades, losangos para Relacionamentos, elipses/ovais para Atributos e linhas com números/letras ($1:N$, $N:M$) para expressar as cardinalidades.
* **Notação Pé de Galinha (Crow's Foot):** Largamente utilizada na indústria de software (e adotada pelo Mermaid.js). Representa entidades por caixas, relacionamentos por linhas de conexão e a cardinalidade através de símbolos nas pontas das linhas (ex.: três linhas bifurcadas lembrando um pé de galinha para representação de "muitos", e um traço perpendicular para representar "um").
* **Notação UML (Diagrama de Classes para ER):** Utiliza retângulos divididos em seções (Nome da Classe, Atributos) e linhas com multiplicidade numérica explícita (ex.: `1..*`, `0..1`).
* **Notação IDEF1X:** Padrão do governo americano para modelagem de dados, diferencia entidades dependentes (cantos arredondados) de independentes (cantos retos) e usa círculos com traços para cardinalidades.

### Comparação Prática de Notações:

| Conceito | Notação de Chen | Notação Pé de Galinha (Crow's Foot) | Notação UML |
| :--- | :--- | :--- | :--- |
| **Cardinalidade "Muitos"** | Usa a letra $N$ ou $M$ no relacionamento | Símbolo de "Pé de Galinha" ($\succ$) | `*` ou `1..*` |
| **Cardinalidade "Um"** | Usa o número $1$ | Traço perpendicular ($|$) | `1` ou `0..1` |
| **Entidade Fraca / Subordinada** | Retângulo duplo | Linha tracejada no relacionamento | Classe dependente de composição |

---