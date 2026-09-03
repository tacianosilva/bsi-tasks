**Tarefa 02 \- MER e Projeto de Banco de Dados Relacional**

Para responder às questões abaixo você deve utilizar um **fork** do repositório **bsi-tasks** no github: [https://github.com/tacianosilva/bsi-tasks](https://github.com/tacianosilva/bsi-tasks).

Lembre-se que você trabalhará no seu fork e depois fará um pull request para o repositório original. Use **branchs** e commits pequenos. Pesquise e fale um pouco sobre **branches**, **pull request** (também conhecido como *merge request*), **merge**, **rebase** e **conflitos** usando git e github.

Acesse o Guia Básico de Markdown e o Guia do Mermaid:

* [https://docs.pipz.com/central-de-ajuda/learning-center/guia-basico-de-markdown](https://docs.pipz.com/central-de-ajuda/learning-center/guia-basico-de-markdown)
* [https://mermaid.js.org/syntax/entityRelationshipDiagram.html](https://mermaid.js.org/syntax/entityRelationshipDiagram.html)

Fluxo de entrega sugerido:
1. **Crie uma issue** no repositório original **bsi-tasks** com o título **"Tarefa 02 - MER e Projeto BDR - \<username\>"** (onde `<username>` é o seu nome de usuário do github). Você precisará do **ID dessa issue** para identificar os seus commits.
2. Crie uma **branch** específica para a tarefa no seu fork (ex.: `tarefa02/<username>` ou `feature/tarefa02`).
3. Desenvolva as respostas nessa branch, com commits pequenos e mensagens relevantes.
4. No final, envie (push) a branch para o seu fork e abra um **pull request** da sua **feature branch (fork)** para a **branch main (bsi-tasks)**.

Responda às questões abaixo no arquivo **`database/20262/<username>/tarefa02.md`** do seu fork, onde `<username>` é o seu nome de usuário do github:

**Q1.** O modelo de dados entidade-relacionamento foi desenvolvido para facilitar o projeto de banco de dados, permitindo especificação de um esquema que representa a estrutura lógica geral de um banco de dados. Descreva os três elementos básicos de um Modelo Entidade Relacionamento (MER).

**Q2.** Pesquise sobre as várias notações possíveis para Diagramas ER e cite alguns exemplos de notações diferentes para o mesmo conceito (ex.: cardinalidade, entidade subordinada, etc.).

**Q3.** Construa um Diagrama ER para projetar a base de dados de uma **empresa de desenvolvimento de software** com outras empresas como clientes. A base de dados não deve conter redundância de dados. O modelo ER deve ser representado com um diagrama usando **Mermaid.js**. O modelo deve apresentar, ao menos, entidades, relacionamentos, atributos, identificadores e restrições de cardinalidade. O modelo deve ser feito no nível conceitual, **sem incluir chaves estrangeiras**.
   a) A empresa presta serviços de desenvolvimento de software para outras empresas (clientes). Cada cliente é identificado por um código, um nome e um e-mail de contato.
   b) Os funcionários da empresa trabalham em squads (equipes). Cada funcionário é identificado por um código, um nome e um e-mail, e possui um papel na equipe: desenvolvedor, testador, líder técnico, supervisor ou gerente de produto.
   c) Cada squad é formada por vários funcionários e resolve tarefas (issues). Uma tarefa tem código, descrição, prioridade, situação e uma estimativa em horas. As tarefas pertencem a projetos de um cliente.
   d) O trabalho é organizado em iterações (sprints). Uma squad planeja releases para seus clientes; uma release agrupa um conjunto de tarefas e passa por testes de validação.

**Q4.** A partir do Diagrama ER da questão anterior, faça o **mapeamento para o Modelo Relacional**: liste as relações (tabelas), com seus atributos, e identifique as **chaves primárias** e as **chaves estrangeiras** de cada relação.

**Q5.** Descreva, em linguagem natural, as **restrições de integridade referencial** que devem ser garantidas no esquema projetado (ex.: "uma tarefa só pode existir vinculada a um projeto de cliente existente", "toda squad deve possuir um líder técnico").

**Instrução de commits (obrigatória):**

Antes de começar, crie a issue no repositório original com o título **"Tarefa 02 - MER e Projeto BDR - \<username\>"** e guarde o **ID** dela. Para cada questão que você resolver (Q1 a Q5), faça um **commit pequeno** com uma mensagem relevante e, ao final dela, acrescente o **ID da issue** no formato `#<id_issue>`. Ao final da atividade, envie sua **feature branch** para o seu **fork** e depois crie um **pull request** da sua **feature branch (fork)** para a **branch main (bsi-tasks)**.

Lembre-se das boas práticas do Git:

1. **criar a issue** no repositório original **bsi-tasks** com o título **"Tarefa 02 - MER e Projeto BDR - \<username\>"** e anotar o **ID da issue**
2. **atualizar seu fork** a partir do original (fetch/pull) antes de começar a desenvolver
3. faça **um clone do seu fork**: **git clone** *https://github.com/USERNAME/bsi-tasks.git*
4. crie uma **branch** para a tarefa e trabalhe nela
5. fazer git pull para atualizar sua pasta de trabalho: **git pull**
6. fazer commits pequenos e sempre colocar uma mensagem relevante e ao final da mensagem identifique a issue com **\#\<id\_issue\>**
7. enviar suas modificações para seu repositório remoto: **git push origin \<branch\>**
8. abrir um **pull request** da sua **feature branch (fork)** para a **branch main (bsi-tasks)**
