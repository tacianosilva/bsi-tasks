# Tarefa 02 - Banco de Dados
## Q1. O modelo de dados entidade-relacionamento foi desenvolvido para facilitar o projeto de banco de dados, permitindo especificação de um esquema que representa a estrutura lógica geral de um banco de dados. Descreva os três elementos básicos de um Modelo Entidade Relacionamento (MER).

Os três elementos básicos do MER são:

### Entidades

As **entidades** representam objetos ou conceitos que possuem existência relevante para o sistema e sobre os quais é necessário armazenar informações. Uma entidade pode representar, por exemplo, uma pessoa, empresa, produto ou projeto.

No contexto de uma empresa de desenvolvimento de software, exemplos de entidades seriam `Cliente`, `Funcionário`, `Squad`, `Projeto` e `Tarefa`.

### Atributos

Os **atributos** representam as características ou propriedades de uma entidade. Eles descrevem as informações que devem ser armazenadas sobre cada ocorrência da entidade.

Por exemplo, a entidade `Cliente` pode possuir os atributos `código`, `nome` e `e-mail`. O atributo `código` pode ser utilizado como identificador da entidade, permitindo distinguir um cliente dos demais.

### Relacionamentos

Os **relacionamentos** representam as associações existentes entre duas ou mais entidades. Eles indicam como as entidades estão relacionadas dentro do contexto do sistema.

Por exemplo, um `Cliente` pode possuir vários `Projetos`, estabelecendo um relacionamento entre as entidades `Cliente` e `Projeto`. Os relacionamentos também podem possuir restrições de cardinalidade, indicando quantas ocorrências de uma entidade podem estar associadas a ocorrências de outra.

Assim, as entidades representam **o que existe no domínio**, os atributos representam **as características desses elementos** e os relacionamentos representam **como esses elementos se associam**.


## Q2. Pesquise sobre as várias notações possíveis para Diagramas ER e cite alguns exemplos de notações diferentes para o mesmo conceito (ex.: cardinalidade, entidade subordinada, etc.).

Entre as mais conhecidas estão as notações **Chen**, **Crow's Foot** e **UML**. Elas utilizam símbolos diferentes para representar os elementos do modelo.

### Notação de Chen

A **notação de Chen** foi proposta por Peter Chen e utiliza símbolos específicos para cada elemento do diagrama. As entidades são representadas por **retângulos**, os atributos por **elipses** e os relacionamentos por **losangos**. As linhas conectam esses elementos.

A cardinalidade é indicada próxima às linhas dos relacionamentos, utilizando valores como `1`, `N` ou `M`. Por exemplo, uma relação em que um cliente possui vários projetos pode ser representada por `1:N`.

Uma entidade subordinada, também chamada de entidade fraca, é representada por um **retângulo com borda dupla**. Seus atributos podem ser representados normalmente por elipses.

### Notação Crow's Foot

A **notação Crow's Foot**, também conhecida como notação de pé de galinha, representa as entidades em caixas que apresentam seus atributos. Os relacionamentos são mostrados por linhas que conectam as entidades.

A cardinalidade é representada por símbolos nas extremidades dessas linhas. O símbolo semelhante a um **pé de galinha** indica o lado que pode possuir várias ocorrências. Assim, uma relação em que um cliente possui vários projetos pode ser representada colocando o símbolo de pé de galinha no lado de `Projeto`.

Diferentemente da notação de Chen, uma entidade subordinada não é identificada por um retângulo com borda dupla. Sua dependência é indicada por meio do relacionamento com a entidade da qual depende.

### Notação UML

A **UML (Unified Modeling Language)** pode ser utilizada para representar estruturas de dados por meio de diagramas de classes. As entidades são representadas por caixas semelhantes às classes, contendo seus atributos. Os relacionamentos são representados por linhas entre essas caixas.

A cardinalidade é indicada por meio de multiplicidades, como `1`, `0..1`, `1..*` e `0..*`. Por exemplo, em uma relação de um para muitos, pode-se utilizar `1` no lado de `Cliente` e `1..*` no lado de `Projeto`.

Uma entidade subordinada pode ser representada como uma classe relacionada à entidade da qual depende, utilizando uma associação que represente essa dependência.

### Exemplos de diferentes representações para o mesmo conceito

A **cardinalidade 1:N** é representada de maneiras diferentes nessas notações. Na notação de Chen, pode ser indicada diretamente como `1:N`. Na Crow's Foot, o lado que representa muitos recebe o símbolo de pé de galinha. Na UML, podem ser utilizadas as multiplicidades `1` e `1..*`.

A **entidade subordinada** também possui representações diferentes. Na notação de Chen, ela utiliza um retângulo com borda dupla. Na Crow's Foot, sua dependência é representada pelo relacionamento com a entidade principal. Na UML, pode ser representada como uma classe relacionada à entidade da qual depende.

Os **atributos** também apresentam diferenças. Na notação de Chen, são representados por elipses ligadas às entidades. Na Crow's Foot, aparecem dentro da caixa da entidade. Na UML, ficam dentro da caixa que representa a classe.


## Q3. Construa um Diagrama ER para projetar a base de dados de uma empresa de desenvolvimento de software com outras empresas como clientes. A base de dados não deve conter redundância de dados. O modelo ER deve ser representado com um diagrama usando Mermaid.js. O modelo deve apresentar, ao menos, entidades, relacionamentos, atributos, identificadores e restrições de cardinalidade. O modelo deve ser feito no nível conceitual, sem incluir chaves estrangeiras.

O modelo proposto representa uma empresa de desenvolvimento de software e seus principais elementos. A entidade EMPRESA_CLIENTE armazena os dados das empresas atendidas, enquanto CONTATO registra as pessoas responsáveis pela comunicação com cada cliente.

A entidade CONTRATO representa os contratos firmados com as empresas clientes e está relacionada a um PROJETO, que contém as informações referentes ao desenvolvimento contratado. Cada projeto pode gerar várias FATURA.

As atividades de desenvolvimento são realizadas pelas EQUIPE, que podem atuar em vários projetos. Os FUNCIONARIO podem integrar diferentes equipes e também podem receber tarefas específicas. A entidade TAREFA registra as atividades dos projetos e pode ser atribuída a funcionários.

A entidade TECNOLOGIA registra as tecnologias utilizadas nos projetos, permitindo relacionar cada projeto às tecnologias empregadas em seu desenvolvimento.

O modelo também representa a relação de supervisão entre funcionários, permitindo registrar qual funcionário supervisiona outros funcionários.

O diagrama ER é representado em Mermaid.js abaixo:

erDiagram
    EMPRESA_CLIENTE {
        string cnpj PK
        string razao_social
        string nome_fantasia
        string endereco
        string telefone
        string email
        string segmento_atuacao
    }
    CONTATO {
        int id_contato PK
        string nome
        string cargo
        string telefone
        string email
    }
    CONTRATO {
        string numero_contrato PK
        date data_assinatura
        decimal valor_total
        string tipo_contrato
        date vigencia_inicio
        date vigencia_fim
    }
    PROJETO {
        string codigo_projeto PK
        string nome
        string descricao
        date data_inicio
        date data_fim_prevista
        decimal orcamento
        string status
    }
    FATURA {
        string numero_fatura PK
        date data_emissao
        decimal valor
        date data_vencimento
        string status_pagamento
    }
    EQUIPE {
        string codigo_equipe PK
        string nome_equipe
        string area_atuacao
    }
    FUNCIONARIO {
        string matricula PK
        string nome
        string cargo
        string email
        date data_contratacao
        decimal salario
    }
    TAREFA {
        string codigo_tarefa PK
        string descricao
        date data_inicio
        date data_fim
        string status
        string prioridade
    }
    TECNOLOGIA {
        int id_tecnologia PK
        string nome
        string versao
        string categoria
    }

    EMPRESA_CLIENTE ||--o{ CONTATO : possui
    EMPRESA_CLIENTE ||--o{ CONTRATO : assina
    CONTRATO ||--|| PROJETO : formaliza
    EQUIPE ||--o{ PROJETO : executa
    PROJETO ||--o{ TAREFA : compreende
    PROJETO ||--o{ FATURA : gera
    EQUIPE }o--o{ FUNCIONARIO : integra
    TAREFA }o--o{ FUNCIONARIO : e_atribuida_a
    PROJETO }o--o{ TECNOLOGIA : utiliza
    FUNCIONARIO ||--o{ FUNCIONARIO : supervisiona


    
## Q4. A partir do Diagrama ER da questão anterior, faça o mapeamento para o Modelo Relacional: liste as relações (tabelas), com seus atributos, e identifique as chaves primárias e as chaves estrangeiras de cada relação.

A partir do Diagrama ER da questão anterior, o modelo pode ser transformado nas seguintes relações:

### EMPRESA_CLIENTE

**Atributos:**

* `cnpj`
* `razao_social`
* `nome_fantasia`
* `endereco`
* `telefone`
* `email`
* `segmento_atuacao`

**Chave primária:** `cnpj`

**Chaves estrangeiras:** nenhuma.

### CONTATO

**Atributos:**

* `id_contato`
* `nome`
* `cargo`
* `telefone`
* `email`
* `cnpj`

**Chave primária:** `id_contato`

**Chave estrangeira:** `cnpj` → `EMPRESA_CLIENTE(cnpj)`

### CONTRATO

**Atributos:**

* `numero_contrato`
* `data_assinatura`
* `valor_total`
* `tipo_contrato`
* `vigencia_inicio`
* `vigencia_fim`
* `cnpj`

**Chave primária:** `numero_contrato`

**Chave estrangeira:** `cnpj` → `EMPRESA_CLIENTE(cnpj)`

### PROJETO

**Atributos:**

* `codigo_projeto`
* `nome`
* `descricao`
* `data_inicio`
* `data_fim_prevista`
* `orcamento`
* `status`
* `numero_contrato`
* `codigo_equipe`

**Chave primária:** `codigo_projeto`

**Chaves estrangeiras:**

* `numero_contrato` → `CONTRATO(numero_contrato)`
* `codigo_equipe` → `EQUIPE(codigo_equipe)`

### FATURA

**Atributos:**

* `numero_fatura`
* `data_emissao`
* `valor`
* `data_vencimento`
* `status_pagamento`
* `codigo_projeto`

**Chave primária:** `numero_fatura`

**Chave estrangeira:** `codigo_projeto` → `PROJETO(codigo_projeto)`

### EQUIPE

**Atributos:**

* `codigo_equipe`
* `nome_equipe`
* `area_atuacao`

**Chave primária:** `codigo_equipe`

**Chaves estrangeiras:** nenhuma.

### FUNCIONARIO

**Atributos:**

* `matricula`
* `nome`
* `cargo`
* `email`
* `data_contratacao`
* `salario`

**Chave primária:** `matricula`

**Chaves estrangeiras:** nenhuma.

### TAREFA

**Atributos:**

* `codigo_tarefa`
* `descricao`
* `data_inicio`
* `data_fim`
* `status`
* `prioridade`
* `codigo_projeto`

**Chave primária:** `codigo_tarefa`

**Chave estrangeira:** `codigo_projeto` → `PROJETO(codigo_projeto)`

### TECNOLOGIA

**Atributos:**

* `id_tecnologia`
* `nome`
* `versao`
* `categoria`

**Chave primária:** `id_tecnologia`

**Chaves estrangeiras:** nenhuma.

### Relações resultantes dos relacionamentos N:N

Os relacionamentos muitos-para-muitos precisam ser representados por novas relações.

**EQUIPE_FUNCIONARIO**

* `codigo_equipe`
* `matricula`

**Chave primária:** (`codigo_equipe`, `matricula`)

**Chaves estrangeiras:**

* `codigo_equipe` → `EQUIPE(codigo_equipe)`
* `matricula` → `FUNCIONARIO(matricula)`

**TAREFA_FUNCIONARIO**

* `codigo_tarefa`
* `matricula`

**Chave primária:** (`codigo_tarefa`, `matricula`)

**Chaves estrangeiras:**

* `codigo_tarefa` → `TAREFA(codigo_tarefa)`
* `matricula` → `FUNCIONARIO(matricula)`

**PROJETO_TECNOLOGIA**

* `codigo_projeto`
* `id_tecnologia`

**Chave primária:** (`codigo_projeto`, `id_tecnologia`)

**Chaves estrangeiras:**

* `codigo_projeto` → `PROJETO(codigo_projeto)`
* `id_tecnologia` → `TECNOLOGIA(id_tecnologia)`

**SUPERVISAO**

* `matricula_supervisor`
* `matricula_supervisionado`

**Chave primária:** (`matricula_supervisor`, `matricula_supervisionado`)

**Chaves estrangeiras:**

* `matricula_supervisor` → `FUNCIONARIO(matricula)`
* `matricula_supervisionado` → `FUNCIONARIO(matricula)`
