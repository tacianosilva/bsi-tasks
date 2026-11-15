# Tarefa 02 - MER e Projeto de Banco de Dados Relacional

**Aluno:** `PHS-00`

---

## Q1. Elementos Básicos do Modelo Entidade-Relacionamento (MER)

O Modelo Entidade-Relacionamento (MER) representa a estrutura lógica conceitual de um banco de dados por meio de três elementos fundamentais:

1. **Entidades:** Representam objetos, pessoas, locais ou conceitos do mundo real com existência independente (física ou abstrata) sobre os quais se deseja armazenar informações (ex.: `Cliente`, `Funcionario`, `Tarefa`). Dividem-se em *entidades fortes* (possuem identificador próprio) e *entidades fracas* (dependem de uma entidade proprietária para existir e ser identificada).
2. **Atributos:** São as propriedades ou características que descrevem uma entidade ou um relacionamento (ex.: `codigo`, `nome`, `email`). Podem ser classificados como simples ou compostos, monovalorados ou multivalorados, armazenados ou derivados, além dos **atributos identificadores (chave)**, que distinguem unicamente cada instância da entidade.
3. **Relacionamentos:** Representam as associações semânticas entre duas ou mais entidades (ex.: uma `Squad` *resolve* uma `Tarefa`). Possuem grau (unário, binário, ternário) e restrições estruturais definidas pela **cardinalidade** (`1:1`, `1:N`, `N:M`) e pela **participação** (total/obrigatória ou parcial/opcional).

---

