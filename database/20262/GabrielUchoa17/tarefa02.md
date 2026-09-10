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

## Q2. Notações para Diagramas ER

Não existe uma notação única para Diagramas ER. As mais difundidas são:

| Notação | Origem / uso típico | Como representa |
|---|---|---|
| **Chen** | Peter Chen (1976); ensino e modelagem conceitual | Entidade = retângulo, relacionamento = **losango**, atributo = **elipse** ligada por linha |
| **Pé de Galinha** (*Crow's Foot* / Martin / IE) | Ferramentas CASE, ERwin, Lucidchart, Mermaid | Entidade = retângulo com atributos **listados dentro**; cardinalidade em **símbolos na ponta da linha** |
| **Barker** | Oracle Designer | Entidade = retângulo arredondado; linha **tracejada** = opcional, **contínua** = obrigatória |
| **IDEF1X** | Padrão do governo dos EUA / modelagem de dados | Entidade dependente = retângulo **arredondado**; usa bolinhas e chaves de identificação |
| **Min-Max (ISO)** | Academia europeia | Rotula cada ponta com o par **(mín, máx)**, ex.: `(1,n)` |
| **UML — Diagrama de Classes** | Engenharia de software / ORM | Classe = retângulo com 3 divisões; cardinalidade escrita como **multiplicidade** (`1`, `0..1`, `1..*`, `*`) |
| **Bachman** | Notação histórica | Setas simples/duplas indicando o lado "muitos" |

### Exemplos: mesmo conceito, notações diferentes

**a) Cardinalidade "um cliente contrata muitos projetos" (1:N)**

| Notação | Representação |
|---|---|
| Chen | `CLIENTE ──1── ⟨contrata⟩ ──N── PROJETO` (rótulos `1` e `N` sobre as linhas) |
| Min-Max | `CLIENTE (0,n) ── contrata ── (1,1) PROJETO` |
| Pé de Galinha | `CLIENTE ‖———<€ PROJETO` (traço duplo de um lado, "pé de galinha" do outro) |
| UML | `CLIENTE 1 ────── 0..* PROJETO` |
| Mermaid | `CLIENTE \|\|--o{ PROJETO : contrata` |

> Atenção a uma **divergência conceitual clássica**: em Chen, o rótulo indica a
> cardinalidade **máxima do lado oposto** (*look-across*); na notação Min-Max, o par
> `(mín,máx)` descreve a participação da entidade **daquele lado** (*look-here*). Por isso
> `1` em Chen e `(1,1)` em Min-Max podem aparecer em pontas opostas da mesma linha.

**b) Obrigatoriedade / opcionalidade (participação)**

| Notação | Participação total (obrigatória) | Participação parcial (opcional) |
|---|---|---|
| Chen | Linha **dupla** entre entidade e losango | Linha simples |
| Min-Max | `(1,n)` — mínimo 1 | `(0,n)` — mínimo 0 |
| Pé de Galinha | Traço perpendicular `\|` junto à entidade | Círculo `o` junto à entidade |
| Barker | Linha **contínua** | Linha **tracejada** |
| UML | `1..*` | `0..*` |

**c) Entidade fraca / subordinada (dependente)**

| Notação | Representação |
|---|---|
| Chen | Entidade em **retângulo duplo** e relacionamento identificador em **losango duplo**; chave parcial **sublinhada tracejada** |
| IDEF1X | Entidade dependente com **cantos arredondados** |
| Pé de Galinha | Relacionamento **identificador** com linha **contínua**; a chave da entidade dona entra na PK composta |
| UML | Composição (**losango preenchido**) no lado do "todo" |

**d) Atributos**

| Notação | Representação |
|---|---|
| Chen | **Elipses** ligadas por linha (multivalorado = elipse dupla; derivado = elipse tracejada; identificador = **sublinhado**) |
| Pé de Galinha / IDEF1X / UML | **Listados dentro do retângulo**, com marcadores `PK`, `FK`, `UK` |

### Ilustração: notação de Chen (fragmento)

```mermaid
flowchart LR
    cod(("<u>codigo</u>")) --- CLIENTE
    nome((nome)) --- CLIENTE
    email((email_contato)) --- CLIENTE

    CLIENTE[CLIENTE] --- R{contrata}
    R --- PROJETO[PROJETO]

    PROJETO --- pcod(("<u>codigo</u>"))
    PROJETO --- pnome((nome))

    linkStyle default stroke-width:1px
```

Legenda do fragmento: retângulos = entidades, losango = relacionamento, elipses =
atributos, sublinhado = identificador. O mesmo fragmento aparece a seguir, na Q3, em
notação **pé de galinha** (a que o Mermaid `erDiagram` implementa nativamente).

---

## Q3. Diagrama ER — Empresa de desenvolvimento de software

### Minimundo considerado

Uma empresa presta serviços de desenvolvimento de software para **empresas clientes**. Os
**funcionários** se organizam em **squads**, cada um com um **papel** definido dentro da
equipe. Uma squad conduz os **projetos** de seus clientes; cada projeto se organiza em
**sprints**, compreende **tarefas** e planeja **releases**, que passam por **testes** de
validação.

### Diagrama ER (notação pé de galinha, nível conceitual)

> Conforme o enunciado, o diagrama está no **nível conceitual**: são exibidos apenas
> atributos próprios e **identificadores** (`PK`); **nenhuma chave estrangeira** foi
> incluída — as associações aparecem como relacionamentos, não como colunas.

```mermaid
erDiagram
    CLIENTE      ||--o{ PROJETO : "contrata"
    SQUAD        ||--o{ PROJETO : "conduz"
    FUNCIONARIO  }|--|{ SQUAD   : "participa-de (papel, periodo)"

    PROJETO      ||--o{ SPRINT  : "organiza-se-em"
    PROJETO      ||--o{ TAREFA  : "compreende"
    PROJETO      ||--o{ RELEASE : "planeja"

    SPRINT       |o--o{ TAREFA  : "aloca"
    RELEASE      |o--o{ TAREFA  : "agrupa"
    RELEASE      ||--o{ TESTE   : "e-validada-por"

    FUNCIONARIO  |o--o{ TAREFA  : "responsabiliza-se-por"
    FUNCIONARIO  |o--o{ TESTE   : "executa"

    CLIENTE {
        string codigo PK "identificador"
        string nome
        string email_contato
    }

    FUNCIONARIO {
        string codigo PK "identificador"
        string nome
        string email "unico"
    }

    SQUAD {
        string codigo PK "identificador"
        string nome "unico"
        date   data_criacao
    }

    PROJETO {
        string codigo PK "identificador"
        string nome
        string descricao
        date   data_inicio
        date   data_prevista_fim
        string situacao "em analise-ativo-pausado-concluido-cancelado"
    }

    SPRINT {
        int    numero PK "chave parcial (entidade fraca de PROJETO)"
        date   data_inicio
        date   data_fim
        string objetivo
        string situacao "planejada-em andamento-encerrada"
    }

    TAREFA {
        string codigo PK "identificador"
        string descricao
        string prioridade "baixa-media-alta-critica"
        string situacao "aberta-em andamento-em teste-concluida"
        int    estimativa_horas
    }

    RELEASE {
        string versao PK "chave parcial (entidade fraca de PROJETO)"
        date   data_planejada
        date   data_lancamento
        string notas
        string situacao "planejada-em homologacao-lancada"
    }

    TESTE {
        string codigo PK "identificador"
        string titulo
        string tipo "unitario-integracao-sistema-aceitacao-regressao"
        string resultado "nao executado-passou-falhou-bloqueado"
        date   data_execucao
    }
```

### Leitura das restrições de cardinalidade

| Relacionamento | Cardinalidade | Leitura |
|---|---|---|
| `CLIENTE` — contrata — `PROJETO` | 1 : N | Um cliente contrata **zero ou vários** projetos; todo projeto pertence a **exatamente um** cliente (participação total do projeto). |
| `SQUAD` — conduz — `PROJETO` | 1 : N | Uma squad conduz **zero ou vários** projetos; todo projeto é conduzido por **exatamente uma** squad. |
| `FUNCIONARIO` — participa-de — `SQUAD` | N : M | Um funcionário participa de **uma ou mais** squads; toda squad é formada por **um ou mais** funcionários. |
| `PROJETO` — organiza-se-em — `SPRINT` | 1 : N | Um projeto tem **zero ou várias** sprints; toda sprint pertence a **exatamente um** projeto (**dependência existencial**). |
| `PROJETO` — compreende — `TAREFA` | 1 : N | Um projeto reúne **zero ou várias** tarefas; toda tarefa pertence a **exatamente um** projeto. |
| `PROJETO` — planeja — `RELEASE` | 1 : N | Um projeto planeja **zero ou várias** releases; toda release pertence a **exatamente um** projeto (**dependência existencial**). |
| `SPRINT` — aloca — `TAREFA` | 1 : N opcional | Uma sprint aloca **zero ou várias** tarefas; uma tarefa está em **no máximo uma** sprint (pode ficar no *backlog*). |
| `RELEASE` — agrupa — `TAREFA` | 1 : N opcional | Uma release agrupa **zero ou várias** tarefas; uma tarefa é entregue em **no máximo uma** release. |
| `RELEASE` — é-validada-por — `TESTE` | 1 : N | Uma release passa por **zero ou vários** testes; todo teste valida **exatamente uma** release. |
| `FUNCIONARIO` — responsabiliza-se-por — `TAREFA` | 1 : N opcional | Um funcionário pode ser responsável por **várias** tarefas; uma tarefa tem **no máximo um** responsável. |
| `FUNCIONARIO` — executa — `TESTE` | 1 : N opcional | Um funcionário executa **vários** testes; um teste é executado por **no máximo um** funcionário. |

### Atributo de relacionamento

O **papel** exercido na equipe (`desenvolvedor`, `testador`, `líder técnico`, `supervisor`,
`gerente de produto`) **não é atributo de `FUNCIONARIO` nem de `SQUAD`**: ele só faz
sentido no contexto da associação entre os dois, pois o mesmo funcionário pode exercer
papéis diferentes em squads diferentes. Por isso `papel` — junto de `data_entrada` e
`data_saida` — é **atributo do relacionamento `participa-de` (N:M)**.

Como a notação pé de galinha do Mermaid não permite anexar atributos a uma linha de
relacionamento, esses atributos aparecem no **rótulo** do relacionamento. Na Q4 eles passam
a compor a relação associativa `PARTICIPACAO`.

### Entidades fracas (subordinadas)

`SPRINT` e `RELEASE` são **entidades fracas**: não possuem identificador próprio suficiente.

- Uma sprint é o "número 3 **do projeto X**" — `numero` é apenas a **chave parcial**.
- Uma release é a "versão 1.4.0 **do projeto X**" — `versao` é a **chave parcial**.

A identificação completa só ocorre pela combinação com o identificador de `PROJETO`, por
meio do **relacionamento identificador**. Isso se materializa como **chave primária
composta** no mapeamento relacional da Q4.

### Decisões de projeto para evitar redundância

O enunciado exige que **não haja redundância de dados**. As decisões abaixo garantem que
cada fato seja armazenado **uma única vez**:

1. **A squad que resolve uma tarefa não é armazenada na tarefa.** O enunciado diz que a
   squad resolve tarefas e que as tarefas pertencem a projetos de um cliente. Como cada
   projeto é conduzido por **exatamente uma** squad, a squad responsável por uma tarefa é
   **derivável** pelo caminho `TAREFA → PROJETO → SQUAD`. Um vínculo direto
   `SQUAD—TAREFA` duplicaria o dado e permitiria contradição (tarefa apontando para uma
   squad diferente da squad do seu projeto).

2. **O cliente não é armazenado na tarefa, na sprint nem na release.** Ele é obtido por
   `PROJETO → CLIENTE`. Do mesmo modo, "a squad planeja releases *para seus clientes*" é
   atendido por `RELEASE → PROJETO → CLIENTE`.

3. **`TESTE` se liga a `RELEASE`, e não também a `PROJETO`.** O projeto do teste vem de
   `TESTE → RELEASE → PROJETO`.

4. **O papel foi retirado de `FUNCIONARIO`** e colocado no relacionamento, como explicado
   acima — evitando repetir ou contradizer o papel quando o funcionário atua em mais de uma
   squad.

5. **Nenhum atributo derivado é armazenado** (ex.: total de horas estimadas de uma sprint,
   quantidade de tarefas concluídas de uma release): todos são obtidos por agregação.

---
