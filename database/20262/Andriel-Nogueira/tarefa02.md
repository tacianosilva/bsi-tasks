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