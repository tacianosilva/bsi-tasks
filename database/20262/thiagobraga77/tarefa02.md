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

**Q4. A partir do Diagrama ER da questão anterior, faça o mapeamento para o Modelo Relacional: liste as relações (tabelas), com seus atributos, e identifique as chaves primárias e as chaves estrangeiras de cada relação.**

**1. CLIENTE**
* **Atributos:** `codigo_cliente`, `nome`, `email`
* **PK:** `codigo_cliente`
* **FK:** Nenhuma

**2. PROJETO**
* **Atributos:** `codigo_projeto`, `nome`, `descricao`, `codigo_cliente`
* **PK:** `codigo_projeto`
* **FK:** `codigo_cliente` (Referencia `CLIENTE.codigo_cliente`)

**3. SQUAD**
* **Atributos:** `codigo_squad`, `nome`
* **PK:** `codigo_squad`
* **FK:** Nenhuma

**4. FUNCIONARIO**
* **Atributos:** `codigo_funcionario`, `nome`, `email`
* **PK:** `codigo_funcionario`
* **FK:** Nenhuma

**5. PAPEL**
* **Atributos:** `codigo_papel`, `nome_papel`
* **PK:** `codigo_papel`
* **FK:** Nenhuma

**6. ALOCACAO_SQUAD** *(Tabela associativa)*
* **Atributos:** `codigo_squad`, `codigo_funcionario`, `codigo_papel`
* **PK:** (`codigo_squad`, `codigo_funcionario`)
* **FKs:** 
  * `codigo_squad` (Referencia `SQUAD.codigo_squad`)
  * `codigo_funcionario` (Referencia `FUNCIONARIO.codigo_funcionario`)
  * `codigo_papel` (Referencia `PAPEL.codigo_papel`)

**7. TAREFA**
* **Atributos:** `codigo_tarefa`, `descricao`, `prioridade`, `situacao`, `estimativa_horas`, `codigo_projeto`, `codigo_squad`
* **PK:** `codigo_tarefa`
* **FKs:**
  * `codigo_projeto` (Referencia `PROJETO.codigo_projeto`)
  * `codigo_squad` (Referencia `SQUAD.codigo_squad`)

**8. SPRINT**
* **Atributos:** `codigo_sprint`, `numero`, `data_inicio`, `data_fim`, `codigo_squad`
* **PK:** `codigo_sprint`
* **FK:** `codigo_squad` (Referencia `SQUAD.codigo_squad`)

**9. RELEASE**
* **Atributos:** `codigo_release`, `versao`, `data_planejada`, `codigo_sprint`
* **PK:** `codigo_release`
* **FK:** `codigo_sprint` (Referencia `SPRINT.codigo_sprint`)

**10. RELEASE_TAREFA** *(Tabela associativa)*
* **Atributos:** `codigo_release`, `codigo_tarefa`
* **PK:** (`codigo_release`, `codigo_tarefa`)
* **FKs:**
  * `codigo_release` (Referencia `RELEASE.codigo_release`)
  * `codigo_tarefa` (Referencia `TAREFA.codigo_tarefa`)


**Q5. Descreva, em linguagem natural, as restrições de integridade referencial que devem ser garantidas no esquema projetado (ex.: "uma tarefa só pode existir vinculada a um projeto de cliente existente", "toda squad deve possuir um líder técnico").**
1. **Integridade entre Projetos e Clientes:** Um projeto só pode ser cadastrado se estiver vinculado a um cliente já existente na tabela `CLIENTE` (`codigo_cliente`). Se um cliente for removido, o sistema deve impedir a exclusão caso existam projetos ativos ou realizar a remoção em cascata dos projetos vinculados.
2. **Integridade entre Tarefas, Projetos e Squads:** Uma tarefa só pode existir associada a um projeto existente (`codigo_projeto`). Da mesma forma, se uma tarefa for atribuída para resolução por uma squad, o identificador (`codigo_squad`) precisa corresponder a uma squad válida.
3. **Integridade na Alocação de Equipes:** Na tabela `ALOCACAO_SQUAD`, só é possível associar um funcionário a uma squad se ambos (`codigo_funcionario` e `codigo_squad`) já estiverem previamente cadastrados. O papel atribuído também deve corresponder a um registro existente na tabela `PAPEL` (`codigo_papel`).
4. **Integridade em Sprints e Releases:** Uma *Sprint* só pode ser criada se estiver vinculada a uma squad existente (`codigo_squad`). Igualmente, uma *Release* deve estar obrigatoriamente associada a uma *Sprint* válida (`codigo_sprint`).
5. **Integridade no Agrupamento de Tarefas por Release:** Na tabela associativa `RELEASE_TAREFA`, não é permitido vincular uma tarefa inexistente a uma *release*, tampouco incluir tarefas em uma *release* que não esteja cadastrada.
6. **Unicidade de Papel por Squad:** Devido à chave primária composta (`codigo_squad`, `codigo_funcionario`) na tabela de alocação, a integridade garante que um funcionário ocupe apenas um papel específico dentro de uma mesma squad.