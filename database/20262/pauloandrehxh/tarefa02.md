# Resposta da Tarefa 2 — Modelagem de Banco de Dados (MER e Relacional)
*Aluno: Paulo André Alves de Moura*


## Q1. Descreva os três elementos básicos de um Modelo Entidade Relacionamento (MER).

O Modelo Entidade-Relacionamento é fundamentado em três conceitos estruturais básicos:
1. **Entidades:** Representam objetos, coisas ou conceitos do mundo real sobre os quais se deseja manter informações (ex: `Funcionario`, `Cliente`, `Projeto`).
2. **Atributos:** São as propriedades ou características descritivas que definem as entidades (ex: `código`, `nome`, `e-mail`).
3. **Relacionamentos:** Representam as associações lógicas e estruturais entre as entidades, descrevendo como elas interagem (ex: um funcionário *trabalha* em uma squad).

## Q2. Notações para Diagramas ER
Existem várias formas de representar um Modelo Entidade-Relacionamento (MER). Embora todas tenham como objetivo representar **entidades, atributos, relacionamentos e restrições**, a simbologia pode variar.

### 1. Notação de Chen

A notação de **Peter Chen** é uma das formas clássicas de representar modelos ER.

- **Entidade:** retângulo.
- **Relacionamento:** losango.
- **Atributo:** elipse.
- **Identificador (chave):** atributo geralmente sublinhado.
- **Entidade fraca:** retângulo duplo.
- **Relacionamento identificador:** losango duplo.
- **Cardinalidade:** pode ser representada por números, como `1:1`, `1:N` e `N:N`.

Exemplo conceitual:

```text
[CLIENTE] ---- <CONTRATA> ---- [PROJETO]
                    |
               relacionamento
```

Uma entidade fraca pode ser representada por um **retângulo duplo**, indicando que sua identificação depende de outra entidade.

---

### 2. Notação Crow's Foot (Pé de Galinha)

É muito utilizada em ferramentas de modelagem e sistemas de banco de dados.

A cardinalidade é representada graficamente nas extremidades dos relacionamentos:

- `|` = exatamente um;
- `O` = zero (opcional);
- `<` ou a "pata de galinha" = muitos.

Algumas combinações:

| Representação | Significado |
|---|---|
| `\|—\|` | exatamente 1 para exatamente 1 |
| `O—\|` | zero ou 1 |
| `\|—<` | 1 para muitos |
| `O—<` | zero ou muitos |

Exemplo:

```text
CLIENTE ||--o{ PROJETO
```

Significa que um cliente pode possuir **zero ou vários projetos**, enquanto cada projeto está associado a **exatamente um cliente**.

---

### 3. Notação UML

A UML também pode ser utilizada para representar estruturas semelhantes às de um modelo ER, principalmente por meio de **diagramas de classes**.

- **Classe/entidade:** retângulo dividido em seções.
- **Atributos:** aparecem dentro da classe.
- **Relacionamentos:** linhas entre as classes.
- **Multiplicidade:** representada por valores como `1`, `0..1`, `1..*` e `0..*`.

Exemplo:

```text
CLIENTE 1 -------- 0..* PROJETO
```

Nesse caso:

- um `CLIENTE` pode estar relacionado a zero ou vários `PROJETOS`;
- cada `PROJETO` está relacionado a um cliente.

---

### 4. Notação IDEF1X

A IDEF1X é outra notação utilizada para modelagem de dados, especialmente em projetos de bancos de dados relacionais.

Ela diferencia, entre outros elementos:

- entidades independentes;
- entidades dependentes;
- atributos identificadores;
- atributos não identificadores;
- relacionamentos identificadores e não identificadores.

A representação visual das entidades e dos relacionamentos possui regras próprias, diferentes da notação Chen e da Crow's Foot.

---

### Comparação de alguns conceitos

| Conceito | Chen | Crow's Foot | UML |
|---|---|---|---|
| Entidade | Retângulo | Caixa/entidade | Classe |
| Relacionamento | Losango | Linha entre entidades | Associação |
| Atributo | Elipse | Dentro da entidade | Dentro da classe |
| Identificador | Atributo sublinhado | Atributo marcado como PK | Atributo com indicação de chave |
| 1:1 | `1:1` | `\|—\|` | `1 — 1` |
| 1:N | `1:N` | `\|—<` | `1 — 1..*` |
| 0:N | `0:N` | `O—<` | `0 — 0..*` |
| Entidade fraca/subordinada | Retângulo duplo | Entidade dependente, conforme a convenção | Pode ser modelada por composição/dependência |

**Observação:** a forma exata dos símbolos pode variar de acordo com a ferramenta e a convenção adotada. O importante é que o modelo apresente claramente os conceitos e suas restrições.

## Q3. Diagrama ER (Empresa de Software)

O modelo deve apresentar, ao menos, entidades, relacionamentos, atributos, identificadores e restrições de cardinalidade. O modelo deve ser feito no nível conceitual, sem incluir chaves estrangeiras. 

* a) A empresa presta serviços de desenvolvimento de software para outras empresas (clientes). Cada cliente é identificado por um código, um nome e um e-mail de contato. 

* b) Os funcionários da empresa trabalham em squads (equipes). Cada funcionário é identificado por um código, um nome e um e-mail, e possui um papel na equipe: desenvolvedor, testador, líder técnico, supervisor ou gerente de produto. 

* c) Cada squad é formada por vários funcionários e resolve tarefas (issues). Uma tarefa tem código, descrição, prioridade, situação e uma estimativa em horas. As tarefas pertencem a projetos de um cliente. 

* d) O trabalho é organizado em iterações (sprints). Uma squad planeja releases para seus clientes; uma release agrupa um conjunto de tarefas e passa por testes de validação.

### Análise do problema

A empresa de desenvolvimento possui **clientes**, **funcionários**, **squads**, **projetos**, **issues**, **sprints** e **releases**.

Para evitar redundância:

- os dados de um cliente são armazenados somente em `CLIENTE`;
- os dados de um funcionário são armazenados somente em `FUNCIONARIO`;
- a associação entre funcionário e squad é representada pelo relacionamento;
- um projeto pertence a um cliente, evitando repetir os dados do cliente em cada issue;
- uma issue pertence a um projeto;
- uma release agrupa issues;
- uma sprint organiza o trabalho de uma squad;
- a validação da release é representada por um relacionamento com o processo/registro de validação, sem duplicar os dados da release.

O modelo abaixo está no nível conceitual. Portanto, não são utilizadas chaves estrangeiras (FKs).

```mermaid
erDiagram

    CLIENTE ||--o{ PROJETO : "possui"
    SQUAD ||--|{ FUNCIONARIO : "forma"
    SQUAD ||--o{ ISSUE : "resolve"
    PROJETO ||--o{ ISSUE : "possui"
    SQUAD ||--o{ SPRINT : "organiza"
    SPRINT ||--o{ ISSUE : "planeja"
    SQUAD ||--o{ RELEASE : "planeja"
    RELEASE ||--o{ ISSUE : "agrupa"
    RELEASE ||--|{ VALIDACAO : "passa por"

    CLIENTE {
        int codigo_cliente PK
        string nome
        string email_contato
    }

    FUNCIONARIO {
        int codigo_funcionario PK
        string nome
        string email
        string papel
    }

    SQUAD {
        int codigo_squad PK
        string nome
    }

    PROJETO {
        int codigo_projeto PK
        string nome
        string descricao
    }

    ISSUE {
        int codigo_issue PK
        string descricao
        string prioridade
        string situacao
        decimal estimativa_horas
    }

    SPRINT {
        int codigo_sprint PK
        string nome
        date data_inicio
        date data_fim
    }

    RELEASE {
        int codigo_release PK
        string versao
        date data_planejada
        string situacao
    }

    VALIDACAO {
        int codigo_validacao PK
        date data_validacao
        string resultado
        string observacao
    }
```

## Q4. A partir do Diagrama ER da questão anterior, faça o mapeamento para o Modelo Relacional: liste as relações (tabelas), com seus atributos, e identifique as chaves primárias e as chaves estrangeiras de cada relação.

Abaixo está o mapeamento do Diagrama ER para o Modelo Relacional, detalhando os atributos, chaves primárias e estrangeiras de cada tabela.

### CLIENTE
* **Atributos:** <u>codigo_cliente</u>, nome, email_contato
* **Chave Primária (PK):** codigo_cliente
* **Chave Estrangeira (FK):** Nenhuma

### SQUAD
* **Atributos:** <u>codigo_squad</u>, nome
* **Chave Primária (PK):** codigo_squad
* **Chave Estrangeira (FK):** Nenhuma

### FUNCIONARIO
* **Atributos:** <u>codigo_funcionario</u>, nome, email, papel, *codigo_squad*
* **Chave Primária (PK):** codigo_funcionario
* **Chave Estrangeira (FK):** codigo_squad (referencia SQUAD)

### PROJETO
* **Atributos:** <u>codigo_projeto</u>, nome, descricao, *codigo_cliente*
* **Chave Primária (PK):** codigo_projeto
* **Chave Estrangeira (FK):** codigo_cliente (referencia CLIENTE)

### SPRINT
* **Atributos:** <u>codigo_sprint</u>, nome, data_inicio, data_fim, *codigo_squad*
* **Chave Primária (PK):** codigo_sprint
* **Chave Estrangeira (FK):** codigo_squad (referencia SQUAD)

### RELEASE
* **Atributos:** <u>codigo_release</u>, versao, data_planejada, situacao, *codigo_squad*
* **Chave Primária (PK):** codigo_release
* **Chave Estrangeira (FK):** codigo_squad (referencia SQUAD)

### VALIDACAO
* **Atributos:** <u>codigo_validacao</u>, data_validacao, resultado, observacao, *codigo_release*
* **Chave Primária (PK):** codigo_validacao
* **Chave Estrangeira (FK):** codigo_release (referencia RELEASE)

### ISSUE
* **Atributos:** <u>codigo_issue</u>, descricao, prioridade, situacao, estimativa_horas, *codigo_projeto*, *codigo_squad*, *codigo_sprint*, *codigo_release*
* **Chave Primária (PK):** codigo_issue
* **Chaves Estrangeiras (FKs):**
  * codigo_projeto (referencia PROJETO)
  * codigo_squad (referencia SQUAD)
  * codigo_sprint (referencia SPRINT)
  * codigo_release (referencia RELEASE)


## Q5. Descreva, em linguagem natural, as restrições de integridade referencial que devem ser garantidas no esquema projetado

Com base no mapeamento relacional, as restrições de integridade referencial e regras de negócio que o banco de dados deve garantir são:

1. **Integridade de Funcionários (Membros da Squad):** 
   Todo funcionário cadastrado no sistema deve, obrigatoriamente, estar vinculado a uma squad existente. O banco de dados não pode permitir a inserção de um funcionário apontando para uma squad fantasma (que não existe) e não deve deixar um funcionário "órfão" sem equipe.

2. **Integridade de Projetos e Clientes:** 
   Um projeto não pode existir de forma isolada. Ele deve sempre estar associado a um cliente válido e já cadastrado na base de dados. Se um cliente for removido do sistema, deve haver uma regra clara sobre o que acontece com seus projetos (por exemplo, impedir a exclusão do cliente se houver projetos ativos).

3. **Integridade de Tarefas (Issues):** 
   Uma tarefa só pode ser criada no sistema se for vinculada a um projeto existente. Além disso, caso essa tarefa seja alocada a uma squad para resolução, adicionada a uma sprint ou agrupada em uma release, todas essas entidades (squad, sprint e release) referenciadas devem existir previamente no banco de dados.

4. **Integridade de Sprints e Releases:** 
   As iterações de trabalho (sprints) e as entregas (releases) só podem ser planejadas e criadas no sistema se estiverem vinculadas a uma squad válida. 

5. **Integridade de Validação de Testes:** 
   Um registro de validação só pode ser inserido no sistema se fizer referência direta a uma release previamente cadastrada. Não se pode ter um resultado de teste para uma versão de software que não existe no banco.

6. **Restrições de Domínio e Negócio (Regras Adicionais):**
   * **Papel do Funcionário:** O cargo (papel) de um funcionário só pode receber valores válidos pré-determinados (Desenvolvedor, Testador, Líder técnico, Supervisor ou Gerente de produto).
   * **Liderança:** O sistema deve garantir que toda squad possua um (e apenas um) funcionário com o papel de Líder técnico.