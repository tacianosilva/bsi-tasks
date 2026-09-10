# Tarefa 02 - MER e Projeto de Banco de Dados Relacional

## Q1. Elementos básicos de um Modelo Entidade-Relacionamento (MER)

O Modelo Entidade-Relacionamento é composto fundamentalmente por três elementos básicos:

1. **Entidades:** Representam objetos, seres ou conceitos do mundo real que possuem uma existência independente e sobre os quais desejamos armazenar dados (ex.: `Cliente`, `Funcionario`). No diagrama, são representadas por retângulos.
2. **Relacionamentos:** Representam associações lógicas entre duas ou mais entidades, indicando como elas interagem entre si (ex.: um `Funcionario` *trabalha em* uma `Squad`). No diagrama conceitual, são representados por losangos.
3. **Atributos:** São as propriedades ou características que descrevem as entidades ou os relacionamentos (ex.: o `nome` e o `email` de um `Funcionario`). Podem ser simples, compostos, multivalorados ou derivados.

## Q2. Notações para Diagramas ER

Existem diferentes notações padronizadas para representar Modelos Entidade-Relacionamento graficamente. Abaixo estão algumas das principais e como representam conceitos comuns:

* **Notação de Chen (Original):** Utiliza retângulos para entidades, losangos para relacionamentos e círculos (elipses) para os atributos conectados às entidades. As cardinalidades são indicadas por letras (`1:N`, `M:N`) ou pares numéricos sobre as linhas.
* **Notação de Pé de Galinha (Information Engineering / Crow's Foot):** Muito utilizada em projetos relacionais modernos e ferramentas como o Mermaid.js. As entidades são caixas contendo os atributos, e os relacionamentos são linhas com símbolos nas pontas que indicam a cardinalidade (ex.: barras verticais para "um", e ramificações em forma de pé de galinha para "muitos").
* **UML (Unified Modeling Language - Diagrama de Classes):** Utiliza classes para representar entidades, atributos dentro do corpo da classe e associações com multiplicidades explícitas (ex.: `1..*` ou `0..1`) nas pontas das linhas.

## Q3. Diagrama ER (Nível Conceitual)

```mermaid
erDiagram
    CLIENTE {
        string codigo PK
        string nome
        string email_contato
    }
    PROJETO {
        string codigo PK
        string nome
        string descricao
    }
    FUNCIONARIO {
        string codigo PK
        string nome
        string email
        string papel
    }
    SQUAD {
        string codigo PK
        string nome
    }
    TAREFA {
        string codigo PK
        string descricao
        string prioridade
        string situacao
        float estimativa_horas
    }
    RELEASE {
        string codigo PK
        string data_planejada
        string status_validacao
    }

    CLIENTE ||--o{ PROJETO : possui
    PROJETO ||--o{ TAREFA : contem
    SQUAD ||--o{ FUNCIONARIO : integra
    SQUAD ||--o{ TAREFA : resolve
    SQUAD ||--o{ RELEASE : planeja
    CLIENTE ||--o{ RELEASE : recebe
    RELEASE ||--o{ TAREFA : agrupa


## Q4. Mapeamento para o Modelo Relacional

A partir do Diagrama ER conceitual, o modelo relacional resultante é composto pelas seguintes tabelas (com chaves primárias **PK** e chaves estrangeiras **FK**):

1. **`cliente`**
   * Atributos: `codigo` (**PK**), `nome`, `email_contato`

2. **`projeto`**
   * Atributos: `codigo ` (**PK**), `nome`, `descricao`, `cliente_codigo` (**FK** referenciando `cliente(codigo)`)

3. **`funcionario`**
   * Atributos: `codigo` (**PK**), `nome`, `email`, `papel`, `squad_codigo` (**FK** referenciando `squad(codigo)`)

4. **`squad`**
   * Atributos: `codigo` (**PK**), `nome`

5. **`tarefa`**
   * Atributos: `codigo` (**PK**), `descricao`, `prioridade`, `situacao`, `estimativa_horas`, `projeto_codigo` (**FK** referenciando `projeto(codigo)`), `squad_codigo` (**FK** referenciando `squad(codigo)`), `release_codigo` (**FK** opcional referenciando `release(codigo)`)

6. **`release`**
   * Atributos: `codigo` (**PK**), `data_planejada`, `status_validacao`, `squad_codigo` (**FK** referenciando `squad(codigo)`), `cliente_codigo` (**FK** referenciando `cliente(codigo)`)



## Q5. Restrições de Integridade Referencial

As principais regras e restrições de integridade referencial que devem ser garantidas no esquema são:

* **Vínculo de Projetos:** Um projeto só pode existir se estiver associado a um cliente válido e existente.
* **Vínculo de Tarefas:** Toda tarefa deve pertencer obrigatoriamente a um projeto de cliente válido e existente.
* **Atribuição de Funcionários:** Todo funcionário deve estar alocado a exatamente uma squad ativa.
* **Responsabilidade de Tarefas:** Uma tarefa deve ser resolvida por uma squad responsável registrada.
* **Planejamento de Releases:** Uma release deve ser planejada por uma squad específica e ser destinada a um cliente válido.
* **Agrupamento em Releases:** As tarefas agrupadas em uma release devem pertencer a projetos do mesmo cliente para o qual a release foi planejada.