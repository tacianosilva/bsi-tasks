**Tarefa 01 \- Conceitos de BD, ACID e SGBD**

Para responder às questões abaixo você deve utilizar um **fork** do repositório **bsi-tasks** no github: [https://github.com/tacianosilva/bsi-tasks](https://github.com/tacianosilva/bsi-tasks).

Lembre-se que você trabalhará no seu fork e depois fará um pull request para o repositório original. Use **branchs** e commits pequenos. Pesquise e fale um pouco sobre **branches**, **pull request** (também conhecido como *merge request*), **merge**, **rebase** e **conflitos** usando git e github.

Acesse o Guia Básico de Markdown:

* [https://docs.pipz.com/central-de-ajuda/learning-center/guia-basico-de-markdown](https://docs.pipz.com/central-de-ajuda/learning-center/guia-basico-de-markdown)

Fluxo de entrega sugerido:
1. **Crie uma issue** no repositório original **bsi-tasks** com o título **"Tarefa 01 - Conceitos de BD - \<username\>"** (onde `<username>` é o seu nome de usuário do github). Você precisará do **ID dessa issue** para identificar os seus commits.
2. Crie uma **branch** específica para a tarefa no seu fork (ex.: `tarefa01/<username>` ou `feature/tarefa01`).
3. Desenvolva as respostas nessa branch, com commits pequenos e mensagens relevantes.
4. No final, envie (push) a branch para o seu fork e abra um **pull request** da sua **feature branch (fork)** para a **branch main (bsi-tasks)**.

Responda às questões abaixo no arquivo **`database/20262/<username>/tarefa01.md`** do seu fork, onde `<username>` é o seu nome de usuário do github:

**Q1.** Descreva o que é um Banco de Dados e o que é um Sistema Gerenciador de Banco de Dados. Cite exemplos de Bancos de Dados e seus SGBDs.

**Q2.** Quais os principais problemas de utilizar Sistemas de Arquivos para armazenagem de dados?

**Q3.** Explique as propriedades **ACID**: atomicidade, consistência, isolamento e durabilidade. Para cada propriedade, descreva um exemplo prático no contexto de uma transferência bancária e explique o que aconteceria se o SGBD não garantisse essa propriedade.

**Q4.** Para cada cenário abaixo, indique qual(is) propriedade(s) ACID está(ão) em jogo e **justifique** sua resposta:
   a) Queda de energia no meio de uma transferência deixou o valor debitado da conta de origem, mas não creditado na conta de destino.
   b) Dois atendentes debitam, ao mesmo tempo, o mesmo saldo de uma conta.
   c) O sistema confirma a operação, mas após reiniciar o servidor o dado foi perdido.
   d) Uma transferência que levaria o saldo abaixo do limite permitido é rejeitada pelo banco.

**Q5.** Um SGBD trata dos seguintes aspectos: **recuperação, integridade, redundância e inconsistência**. Explique cada um deles e descreva como o SGBD os gerencia.

**Q6.** Considere o cenário de uma **empresa de desenvolvimento de software** que atende outras empresas como clientes. A empresa organiza seu trabalho em **squads** (equipes) compostas por desenvolvedores, testadores, líder técnico, supervisor e gerente de produto. Cada squad resolve **tarefas** (issues) e planeja **releases**, testes e o cronograma de **sprints** (iterações) dos projetos de cada cliente.

Sem utilizar SQL, elabore um **mini-projeto conceitual** do banco de dados dessa empresa, deixando claro:
   a) As principais **entidades** envolvidas (clientes, squads, membros, tarefas, projetos, sprints, releases).
   b) Os principais **atributos** de cada entidade.
   c) Os **relacionamentos** entre as entidades (com a cardinalidade, ex.: "um cliente pode ter vários projetos").
   d) Em linguagem natural, as **regras de integridade** (restrições) que o banco de dados deveria garantir, ex.: "apenas um líder por squad", "toda tarefa precisa estar vinculada a um projeto".

**Instrução de commits (obrigatória):**

Antes de começar, crie a issue no repositório original com o título **"Tarefa 01 - Conceitos de BD - \<username\>"** e guarde o **ID** dela. Para cada questão que você resolver (Q1 a Q6), faça um **commit pequeno** com uma mensagem relevante e, ao final dela, acrescente o **ID da issue** no formato `#<id_issue>`. Ao final da atividade, envie sua **feature branch** para o seu **fork** e depois crie um **pull request** da sua **feature branch (fork)** para a **branch main (bsi-tasks)**.

Lembre-se das boas práticas do Git:

1. **criar a issue** no repositório original **bsi-tasks** com o título **"Tarefa 01 - Conceitos de BD - \<username\>"** e anotar o **ID da issue**
2. **atualizar seu fork** a partir do original (fetch/pull) antes de começar a desenvolver
3. faça **um clone do seu fork**: **git clone** *https://github.com/USERNAME/bsi-tasks.git*
4. crie uma **branch** para a tarefa e trabalhe nela
5. fazer git pull para atualizar sua pasta de trabalho: **git pull**
6. fazer commits pequenos e sempre colocar uma mensagem relevante e ao final da mensagem identifique a issue com **\#\<id\_issue\>**
7. enviar suas modificações para seu repositório remoto: **git push origin \<branch\>**
8. abrir um **pull request** da sua **feature branch (fork)** para a **branch main (bsi-tasks)**
