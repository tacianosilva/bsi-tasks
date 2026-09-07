# Q1. O modelo de dados entidade-relacionamento foi desenvolvido para facilitar o projeto de banco de dados, permitindo especificação de um esquema que representa a estrutura lógica geral de um banco de dados. Descreva os três elementos básicos de um Modelo Entidade Relacionamento (MER).

Os três elementos principais são **Entidades**, geralmente os objetos do mundo real que queremos representar dentro do banco, com existências independentes; **Atributos**, que são as características dessas **Entidades**, como um nome ou CPF; e por fim, **Relacionamentos**, que é a forma que essas **Entidades** se relacionam entre si. Um exemplo clássico é que "um Cliente (entidade) faz (relacionamento) uma Compra (entidade)".

---

# Q2. Pesquise sobre as várias notações possíveis para Diagramas ER e cite alguns exemplos de notações diferentes para o mesmo conceito (ex.: cardinalidade, entidade subordinada, etc.).

Duas das principais notações são a Notação de Chen e a Notação UML. Elas tem os mesmos conceitos mas de diferentes formas:

* No modelo de Chen, Entidades e Relacionamentos são representados por formas geométricas, retângulos para Entidades e losangos para Relacionamentos. que podem ter atributos e relacionamentos próprios. Já na UML, Relacionamentos não tem uma forma própria, e são representados apenas por uma linha.
* Para Chen, cardinalidades são representadas por números e letras (1, N, M) e escritos na linha da relacionamento. No UML, são usados números e ponto (0..0, 0..1).

---

# Q3. Construa um Diagrama ER para projetar a base de dados de uma empresa de desenvolvimento de software com outras empresas como clientes. A base de dados não deve conter redundância de dados. O modelo ER deve ser representado com um diagrama usando Mermaid.js. O modelo deve apresentar, ao menos, entidades, relacionamentos, atributos, identificadores e restrições de cardinalidade. O modelo deve ser feito no nível conceitual, sem incluir chaves estrangeiras.

### a) A empresa presta serviços de desenvolvimento de software para outras empresas (clientes). Cada cliente é identificado por um código, um nome e um e-mail de contato.

### b) Os funcionários da empresa trabalham em squads (equipes). Cada funcionário é identificado por um código, um nome e um e-mail, e possui um papel na equipe: desenvolvedor, testador, líder técnico, supervisor ou gerente de produto.

### c) Cada squad é formada por vários funcionários e resolve tarefas (issues). Uma tarefa tem código, descrição, prioridade, situação e uma estimativa em horas. As tarefas pertencem a projetos de um cliente.

### d) O trabalho é organizado em iterações (sprints). Uma squad planeja releases para seus clientes; uma release agrupa um conjunto de tarefas e passa por testes de validação.

![Modelo Mermaid](<./modelo mermaid.png>)

---

# Q4. A partir do Diagrama ER da questão anterior, faça o mapeamento para o Modelo Relacional: liste as relações (tabelas), com seus atributos, e identifique as chaves primárias e as chaves estrangeiras de cada relação.

### CLIENTE

| Atributo      | Tipo   | Chave |
| ------------- | ------ | ----- |
| id            | string | PK    |
| nome          | string |       |
| email_contato | string |       |

### FUNCIONARIO

| Atributo | Tipo   | Chave          |
| -------- | ------ | -------------- |
| id       | string | PK             |
| nome     | string |                |
| email    | string |                |
| papel    | string |                |
| squad_id | string | FK → SQUAD.id |

### SQUAD

| Atributo | Tipo   | Chave |
| -------- | ------ | ----- |
| id       | string | PK    |
| nome     | string |       |

### PROJETO

| Atributo   | Tipo   | Chave            |
| ---------- | ------ | ---------------- |
| id         | string | PK               |
| nome       | string |                  |
| descricao  | string |                  |
| cliente_id | string | FK → CLIENTE.id |

### SQUAD_PROJETO (tabela associativa)

| Atributo   | Tipo   | Chave                |
| ---------- | ------ | -------------------- |
| squad_id   | string | PK, FK → SQUAD.id   |
| projeto_id | string | PK, FK → PROJETO.id |

### SPRINT

| Atributo    | Tipo   | Chave            |
| ----------- | ------ | ---------------- |
| id          | string | PK               |
| numero      | int    |                  |
| data_inicio | date   |                  |
| data_fim    | date   |                  |
| squad_id    | string | FK → SQUAD.id   |
| projeto_id  | string | FK → PROJETO.id |

### RELEASE

| Atributo       | Tipo   | Chave            |
| -------------- | ------ | ---------------- |
| id             | string | PK               |
| versao         | string |                  |
| data_planejada | date   |                  |
| squad_id       | string | FK → SQUAD.id   |
| projeto_id     | string | FK → PROJETO.id |

### TAREFA

| Atributo         | Tipo   | Chave                           |
| ---------------- | ------ | ------------------------------- |
| id               | string | PK                              |
| descricao        | string |                                 |
| prioridade       | string |                                 |
| situacao         | string |                                 |
| estimativa_horas | float  |                                 |
| id_projeto       | string | FK → PROJETO.id (obrigatório) |
| id_sprint        | string | FK → SPRINT.id (opcional)      |
| id_funcionario   | string | FK → FUNCIONARIO.id (opcional) |
| id_release       | string | FK → RELEASE.id (opcional)     |

<p a<wbr>

---



<p a<wbr>

<p><wbr>

<p><wbr>

<p align="center">
  <img src="https://example.com" alt="Alternate Text">
</p>
