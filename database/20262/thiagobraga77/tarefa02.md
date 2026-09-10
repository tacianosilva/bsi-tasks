**Q1. O modelo de dados entidade-relacionamento foi desenvolvido para facilitar o projeto de banco de dados, permitindo especificação de um esquema que representa a estrutura lógica geral de um banco de dados. Descreva os três elementos básicos de um Modelo Entidade Relacionamento (MER)**

Os três elementos básicos de um Modelo Entidade-Relacionamento(MER) são entidades, atributos e relacionamentos.

* Entidades: Representam objetos ou elementos do mundo real que precisam ser armazenados no banco de dados. Exemplo, em uma empresa de desenvolvimento de software, podemos ter as entidades **Cliente**, **Funcionário**, **Squad** e **Projeto**.
* Atributos: São as características que descrevem uma entidade. Por exemplo, a entidade **Cliente** pode possuir os atributos **cpf**, **nome** e **email**.

* Relacionamentos: representam as associações entre as entidades. Por exemplo, um **Cliente** possui **Projetos**, enquanto uma **Squad** é formada por vários **Funcionários**.

**Q2. Pesquise sobre as várias notações possíveis para Diagramas ER e cite alguns exemplos de notações diferentes para o mesmo conceito (ex.: cardinalidade, entidade subordinada, etc.).**

Existem diversas notações utilizadas para representar diagramas Entidade-Relacionamento. Entre as mais conhecidas estão a **notação de Chen**, a **notação Crow's Foot(Pé de Galinha)** e a **notação UML**.

**Notação de Chen**

A notação de Chen utiliza diferentes formas geométricas para representar os elementos do modelo. As entidades são representadas por retângulos, os atributos por elipses, os relacionamentos por losangos e as linhas conectam os atributos às entidades, e as entidades aos losangos.


**Notação Crow's Foot**

A notação Crow's Foot, também conhecida como notação "Pé de Galinha", utiliza símbolos nas extremidades das linhas para representar a cardinalidade dos relacionamentos.

**Notação UML** 

A UML(Unified Modeling Language) também pode ser utilizada para representar estruturas de sistemas e banco de dados. Neste modelo, as entidades podem ser representadas como classes, contendo seus atributos e relacionamentos com outras classes.

**Q3. Construa um Diagrama ER para projetar a base de dados de uma empresa de desenvolvimento de software com outras empresas como clientes. A base de dados não deve conter redundância de dados. O modelo ER deve ser representado com um diagrama usando Mermaid.js. O modelo deve apresentar, ao menos, entidades, relacionamentos, atributos, identificadores e restrições de cardinalidade. O modelo deve ser feito no nível conceitual, sem incluir chaves estrangeiras. a) A empresa presta serviços de desenvolvimento de software para outras empresas (clientes). Cada cliente é identificado por um código, um nome e um e-mail de contato. b) Os funcionários da empresa trabalham em squads (equipes). Cada funcionário é identificado por um código, um nome e um e-mail, e possui um papel na equipe: desenvolvedor, testador, líder técnico, supervisor ou gerente de produto. c) Cada squad é formada por vários funcionários e resolve tarefas (issues). Uma tarefa tem código, descrição, prioridade, situação e uma estimativa em horas. As tarefas pertencem a projetos de um cliente. d) O trabalho é organizado em iterações (sprints). Uma squad planeja releases para seus clientes; uma release agrupa um conjunto de tarefas e passa por testes de validação.**

![Diagrama ER](<img/questao3.png>)