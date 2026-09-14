# Tarefa 02 - MER e Projeto de Banco de Dados Relacional

### Q1. Elementos básicos do Modelo Entidade Relacionamento (MER)
Os três elementos básicos do MER são:
1. **Entidades:** Representam objetos do mundo real ou conceitos abstratos sobre os quais se deseja guardar informações (ex: Cliente, Funcionario, Squad).
2. **Relacionamentos:** Representam as associações lógicas e regras de negócio que ligam as entidades umas às outras (ex: um Funcionario *pertence* a uma Squad).
3. **Atributos:** São as propriedades ou características que descrevem as entidades e os relacionamentos (ex: o "nome" e o "email" de um Cliente).

### Q2. Notações para Diagramas ER
Existem diversas notações gráficas para desenhar diagramas ER, cada uma com sua forma de representar entidades, atributos e relacionamentos.
* **Notação de Chen:** Uma das mais clássicas. Usa retângulos para entidades, losangos para relacionamentos e elipses para atributos. A cardinalidade é escrita nos conectores (ex: 1, N, M).
* **Pé de Galinha (Crow's Foot / Information Engineering):** Muito usada no mercado e em ferramentas de modelagem e CASE. As entidades são caixas que já contêm os atributos dentro. A cardinalidade é representada por terminações gráficas nas linhas de relacionamento (um círculo para "zero", um traço para "um", e um desenho de três pontas, o "pé de galinha", para "muitos").
* **UML (Diagrama de Classes):** Embora seja da orientação a objetos, é amplamente adaptada para banco de dados. Usa caixas compartimentadas e anotações numéricas nas extremidades (ex: `0..1`, `1..*`) para representar multiplicidade.
* **IDEF1X:** Notação rigorosa adotada como padrão governamental nos EUA. Representa claramente chaves primárias e estrangeiras, além de diferenciar entidades independentes (cantos quadrados) de entidades dependentes/fracas (cantos arredondados).

### Q3. Diagrama ER (Conceitual) usando Mermaid.js

```mermaid
erDiagram
    CLIENTE ||--o{ PROJETO : "solicita"
    PROJETO ||--o{ TAREFA : "possui"
    SQUAD ||--|{ FUNCIONARIO : "composta_por"
    SQUAD ||--o{ SPRINT : "executa"
    SQUAD ||--o{ RELEASE : "planeja"
    RELEASE }o--|| CLIENTE : "entregue_para"
    RELEASE ||--o{ TAREFA : "agrupa"
    SPRINT ||--o{ TAREFA : "contem"

    CLIENTE {
        int codigo PK
        string nome
        string email_contato
    }
    FUNCIONARIO {
        int codigo PK
        string nome
        string email
        string papel
    }
    SQUAD {
        int codigo PK
        string nome
    }
    PROJETO {
        int codigo PK
        string nome
    }
    TAREFA {
        int codigo PK
        string descricao
        string prioridade
        string situacao
        int estimativa_horas
    }
    SPRINT {
        int codigo PK
        string nome
        date data_inicio
        date data_fim
    }
    RELEASE {
        int codigo PK
        string versao
        boolean teste_validacao
    }