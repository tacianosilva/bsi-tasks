## Q1. O modelo de dados entidade-relacionamento foi desenvolvido para facilitar o projeto de banco de dados, permitindo especificação de um esquema que representa a estrutura lógica geral de um banco de dados. Descreva os três elementos básicos de um Modelo Entidade Relacionamento (MER).
**R:** Os três elementos básicos são Entidade, Atributos e Relacionamentos.

- Entidades: representam objetos ou elementos do mundo real que possuem existência própria e sobre os quais se deseja armazena informações.
Exemplos: ``Cliente``, ``Produto``, ``Funcionário``.

- Atributos: representam as características ou propriedades das entidades.
Exemplos: a entidade ``Cliente`` pode possuir os atributos id, nome, email, cpf e telefone.

- Relacionamentos: representam as associações existentes entre duas ou mais entidades.
Exemplos: um ``Cliente`` realiza um ``Pedido``.

## Q2. Pesquise sobre as várias notações possíveis para Diagramas ER e cite alguns exemplos de notações diferentes para o mesmo conceito (ex.: cardinalidade, entidade subordinada, etc.).

**R**: Existem várias notações utilizadas para representar Diagramas Entidade-Relacionamento (DER), sendo algumas das mais conhecidas as notações **Chen, Crow's Foot, IDEF1X e UML**. Apesar de utilizarem símbolos diferentes, elas podem representar os mesmos conceitos de um modelo de dados.

Na **notação Chen**, as entidades são representadas por retângulos, os atributos por elipses e os relacionamentos por losangos. A cardinalidade costuma ser representada por números ou letras, como `1`, `N` e `M`. Uma entidade fraca é representada por um retângulo duplo.

Na **notação Crow's Foot**, as entidades são representadas por caixas e os relacionamentos por linhas. A cardinalidade é indicada por símbolos nas extremidades das linhas: uma barra representa "um", um círculo representa "zero" e o símbolo de pé de galinha representa "muitos".

Na **notação IDEF1X**, há maior destaque para as chaves e para a dependência entre entidades. Os relacionamentos podem ser identificadores ou não identificadores, sendo representados por diferentes tipos de linhas.

A **UML** também pode ser utilizada para representar estruturas semelhantes às de um DER, principalmente por meio de diagramas de classes. Nesse caso, as multiplicidades são representadas por valores como `1`, `0..1`, `1..*` e `*`.

Assim, um mesmo conceito pode possuir representações diferentes dependendo da notação. Por exemplo, uma cardinalidade **um para muitos** pode ser representada como `1:N` na notação Chen, por uma barra e um pé de galinha na notação Crow's Foot, ou como `1..*` em UML. Dessa forma, as diferentes notações modificam principalmente a forma visual de representar o modelo, mantendo a mesma informação conceitual.
