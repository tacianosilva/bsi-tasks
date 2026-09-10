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

---

## Questão 02 - Notações em Diagramas Entidade-Relacionamento (DER)

Ao longo da evolução da Engenharia de Software e Banco de Dados, surgiram diversas notações gráficas para expressar os mesmos conceitos de modelagem:

| Conceito / Elemento | Notação de Peter Chen (1976) | Notação Pé de Galinha (*Crow's Foot* / Martin) | Notação UML (*Class Diagram*) |
| :--- | :--- | :--- | :--- |
| **Entidade** | Retângulo com o nome da entidade. | Retângulo dividido em seções (Nome, Chaves, Atributos). | Retângulo com três compartimentos (Nome, Atributos, Operações). |
| **Relacionamento** | Losango conectado às entidades por linhas retas. | Linha conectando as entidades com conectores nas pontas. | Linha de associação com nome do papel ou multiplicidade. |
| **Atributos** | Elipses (ovais) ligadas à entidade por linhas. | Listados dentro da caixa da própria entidade. | Listados como propriedades dentro da classe. |
| **Cardinalidade** | Rótulos nas linhas (ex.: `(1,1)`, `(0,n)`, `(1,n)`). | Símbolos gráficos nas pontas: anel (`0`), traço (`1`), tridente/pé de galinha (`N`). | Notação intervalar nas extremidades: `0..1`, `1..1`, `0..*`, `1..*`. |
| **Entidade Fraca** | Retângulo duplo ligado por losango duplo. | Retângulo com cantos arredondados ou linha de relacionamento contínua (*identificadora*). | Composição (linha terminada em losango preenchido preto). |

---

## Questão 03 — Diagrama ER Conceitual (Mermaid.js)

```mermaid
erDiagram
    CLIENTE ||--o{ PROJETO : contrata
    PROJETO ||--|{ SPRINT : "e dividido em"
    PROJETO ||--|{ TAREFA : contem
    PROJETO ||--o{ RELEASE : entrega

    SQUAD ||--|{ FUNCIONARIO : aloca
    SQUAD ||--o{ PROJETO : "atua em"
    SQUAD ||--o{ RELEASE : planeja

    SPRINT ||--o{ TAREFA : "inclui no ciclo"
    RELEASE ||--o{ TAREFA : agrupa

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
        string descricao
    }

    SPRINT {
        int codigo PK
        int numero
        date data_inicio
        date data_fim
    }

    TAREFA {
        int codigo PK
        string descricao
        string prioridade
        string situacao
        float estimativa_horas
    }

    RELEASE {
        int codigo PK
        string versao
        date data_lancamento
        string resultado_testes
    }

    