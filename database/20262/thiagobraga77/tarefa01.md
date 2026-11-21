# Tarefa 01 - Conceitos de BD, ACID e SGBD
**Q1.  Descreva o que é um Banco de Dados e o que é um Sistema Gerenciador de Banco de Dados. Cite exemplos de Bancos de Dados e seus SGBDs..**
Banco de Dados é uma coleção de dados relacionados e armazenados em algum dispostivio que permite consultar, armazenar e manipular informações. Exemplo: Banco de Dados de uma escola: Professores, Alunos, Turmas, Notas.

SGBD é um conjunto de dados associado a um conjunto de programas para acesso a esses dados. Ou seja, é o softare responsável por gerenciar o banco de dados. Alguns exemplos de SGBDs são MySQL, PostgreSQL, Oracle Database e SQL Server.

**Q2. Quais são os principais problemas da utilização de Sistemas de Arquivos para armazenamento de dados?**
Os principais problemas são:

* Inconsistência e redundância de dados
* Dificuldade de acesso aos dados
* Isolamento de dados
* Problemas de integridade
* Problemas de segurança

**Q3. Explique as propriedades ACID: atomicidade, consistência, isolamento e durabilidade. Para cada propriedade, descreva um exemplo prático no contexto de uma transferência bancária e explique o que aconteceria se o SGBD não garantisse essa propriedade.**  
* Atomicidade significa que uma transação deve ser finalizada completamente ou não ser realizada; 
* Consistência significa que o banco de dados deve permanecer em um estado válido após uma transação;
* Isolamento significa que transações executadas simultaneamente não devem interferir de maneira incorreta umas nas outras;
* Durabilidade significa que, após uma transação ser confirmada, seus dados
devem permanecer armazenados mesmo após uma falha do sistema.


**Q4. Para cada cenário abaixo, indique qual(is) propriedade(s) ACID está(ão) em jogo e justifique sua resposta: a) Queda de energia no meio de uma transferência deixou o valor debitado da conta de origem, mas não creditado na conta de destino. b) Dois atendentes debitam, ao mesmo tempo, o mesmo saldo de uma conta. c) O sistema confirma a operação, mas após reiniciar o servidor o dado foi perdido. d) Uma transferência que levaria o saldo abaixo do limite permitido é rejeitada pelo banco.**

a) Atomicidade: uma transferência bancária deve acontecer completamente
ou não acontecer.

b) Isolamento: duas operações realizadas ao mesmo tempo não devem causar
um resultado incorreto.

c) Durabilidade: após uma operação ser confirmada, seus dados não devem
ser perdidos mesmo que o servidor seja reiniciado.

d) Consistência: uma operação que viole uma regra do banco de dados deve
ser rejeitada.


**Q5. Explique como um SGBD trata recuperação, integridade, redundância e inconsistência.**

A recuperação permite restaurar os dados após falhas.

A integridade garante que os dados armazenados sigam as regras definidas
no banco de dados.

A redundância é reduzida através de uma boa organização dos dados.

A inconsistência é evitada através de regras de integridade e do controle
das transações.

**Q6. Considere o cenário de uma empresa de desenvolvimento de software que atende outras empresas como clientes. A empresa organiza seu trabalho em squads (equipes) compostas por desenvolvedores, testadores, líder técnico, supervisor e gerente de produto. Cada squad resolve tarefas (issues) e planeja releases, testes e o cronograma de sprints (iterações) dos projetos de cada cliente.**

**Sem utilizar SQL, elabore um mini-projeto conceitual do banco de dados dessa empresa, deixando claro: a) As principais entidades envolvidas (clientes, squads, membros, tarefas, projetos, sprints, releases). b) Os principais atributos de cada entidade. c) Os relacionamentos entre as entidades (com a cardinalidade, ex.: "um cliente pode ter vários projetos"). d) Em linguagem natural, as regras de integridade (restrições) que o banco de dados deveria garantir, ex.: "apenas um líder por squad", "toda tarefa precisa estar vinculada a um projeto".**

### a) Principais entidades

As principais entidades são: Cliente, Projeto, Squad, Membro, Tarefa, Sprint e Release.

### b) Principais atributos

**Cliente**
- id
- nome
- email
- telefone

**Projeto**
- id
- nome
- descrição
- data_inicio
- data_fim

**Squad**
- id
- nome

**Membro**
- id
- nome
- email
- cargo

**Tarefa**
- id
- título
- descrição
- status
- prioridade

**Sprint**
- id
- nome
- data_inicio
- data_fim

**Release**
- id
- versão
- data
- descrição

### c) Relacionamentos e cardinalidades

Um cliente pode ter vários projetos, mas cada projeto pertence a um único cliente.

Um projeto pode possuir várias squads, e uma squad pode participar de vários projetos.

Uma squad pode possuir vários membros, mas cada membro pertence a uma única squad.

Um projeto pode possuir várias tarefas, mas cada tarefa pertence a um único projeto.

Um projeto pode possuir várias sprints, mas cada sprint pertence a um único projeto.

Uma sprint pode possuir várias tarefas, e uma tarefa pode participar de uma sprint.

Um projeto pode possuir várias releases, mas cada release pertence a um único projeto.

### d) Regras de integridade

- Todo projeto deve estar vinculado a um cliente.
- Toda tarefa deve estar vinculada a um projeto.
- Todo membro deve estar vinculado a uma squad.
- Cada squad deve possuir apenas um líder técnico.
- Toda sprint deve estar vinculada a um projeto.
- Toda release deve estar vinculada a um projeto.
- A data de fim de uma sprint deve ser posterior à data de início.
- Toda tarefa deve possuir um status válido.
- Toda release deve possuir uma versão identificável.