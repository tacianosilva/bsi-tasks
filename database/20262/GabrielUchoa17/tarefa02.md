# Tarefa 02 - MER e Projeto de Banco de Dados Relacional

**Aluno (GitHub):** GabrielUchoa17
**Disciplina:** Banco de Dados - BSI
**Issue relacionada:** #398

---

## Sumário

- [Q1. Elementos básicos do MER](#q1-elementos-básicos-do-modelo-entidade-relacionamento)
- [Q2. Notações para Diagramas ER](#q2-notações-para-diagramas-er)
- [Q3. Diagrama ER da empresa de desenvolvimento de software](#q3-diagrama-er--empresa-de-desenvolvimento-de-software)
- [Q4. Mapeamento para o Modelo Relacional](#q4-mapeamento-para-o-modelo-relacional)
- [Q5. Restrições de integridade referencial](#q5-restrições-de-integridade-referencial)

---

## Q1. Elementos básicos do Modelo Entidade-Relacionamento

O Modelo Entidade-Relacionamento (MER), proposto por **Peter Chen (1976)**, descreve o
minimundo em nível **conceitual** — independente de SGBD, de estruturas físicas e de
implementação. Ele se apoia em **três elementos básicos**: *entidades*, *relacionamentos* e
*atributos*.

### 1. Entidades (e conjuntos de entidades)

Uma **entidade** é um objeto do mundo real, concreto ou abstrato, que possui existência
própria e pode ser distinguido dos demais (um cliente específico, um projeto específico).
Um **conjunto de entidades** (*entity set*) agrupa todas as entidades que compartilham as
mesmas propriedades — é isso que efetivamente se desenha no diagrama e que, no mapeamento,
tende a virar uma tabela.

Variações importantes:

- **Entidade forte:** possui um identificador próprio e existe independentemente de
  qualquer outra (ex.: `CLIENTE`).
- **Entidade fraca (ou subordinada):** não possui identificador próprio suficiente e
  depende da existência de uma entidade proprietária. Identifica-se pela combinação da
  chave da proprietária com sua **chave parcial** (ex.: `SPRINT`, identificada pelo
  projeto ao qual pertence somado ao seu número).

### 2. Relacionamentos (e conjuntos de relacionamentos)

Um **relacionamento** é uma associação entre duas ou mais entidades (ex.: o cliente *X*
**contrata** o projeto *Y*). O **conjunto de relacionamentos** reúne todas as associações
do mesmo tipo.

Características que qualificam um relacionamento:

- **Grau:** número de conjuntos de entidades participantes — binário (2, o caso mais
  comum), ternário (3) ou n-ário. Um relacionamento também pode ser **recursivo**
  (*auto-relacionamento*), quando a mesma entidade participa em dois papéis diferentes
  (ex.: funcionário *supervisiona* funcionário).
- **Razão de cardinalidade:** quantas entidades de um lado podem se associar a entidades do
  outro — **1:1**, **1:N** ou **N:M**.
- **Participação (cardinalidade mínima):** **total/obrigatória** (toda entidade do conjunto
  precisa participar — dependência existencial) ou **parcial/opcional** (pode não
  participar).
- **Papéis:** o nome da função que cada entidade exerce na associação, essencial nos
  relacionamentos recursivos.
- Um relacionamento também pode ter **atributos próprios** (ex.: o `papel` que um
  funcionário exerce em uma squad pertence à associação *Funcionário × Squad*, não a
  nenhuma das duas entidades isoladamente).

### 3. Atributos

Um **atributo** é uma propriedade que descreve uma entidade ou um relacionamento (nome,
e-mail, prioridade). O conjunto de valores permitidos para um atributo é o seu **domínio**.

Classificação dos atributos:

| Tipo | Descrição | Exemplo |
|---|---|---|
| **Simples (atômico)** | Não é decomponível | `email` |
| **Composto** | Divisível em subpartes com significado próprio | `endereco` → logradouro, número, cidade, CEP |
| **Monovalorado** | Um único valor por entidade | `data_nascimento` |
| **Multivalorado** | Vários valores para a mesma entidade | `telefone` (vários por cliente) |
| **Derivado** | Calculado a partir de outros atributos | `idade`, derivada de `data_nascimento` |
| **Armazenado** | Guardado fisicamente, base para os derivados | `data_nascimento` |
| **Identificador (chave)** | Distingue univocamente cada entidade | `codigo` do cliente |
| **Chave parcial** | Identifica a entidade fraca dentro da proprietária | `numero` da sprint |

O **identificador (chave)** merece destaque: é o atributo — ou o **conjunto de atributos
(chave composta)** — cujo valor é único para cada entidade do conjunto. Quando há mais de
um candidato, escolhe-se um como **chave primária**.

> **Resumo:** *entidades* respondem "sobre o que guardamos dados", *atributos* respondem
> "o que sabemos sobre cada coisa" e *relacionamentos* respondem "como essas coisas se
> associam entre si".

---
