# Tarefa 01 - Conceitos de Banco de Dados

## Q1. Descreva o que é um Banco de Dados e o que é um Sistema Gerenciador de Banco de Dados. Cite exemplos de Bancos de Dados e seus SGBDs.

Um **Banco de Dados (BD)** é um conjunto de dados organizados e armazenados de forma que possam ser consultados, alterados e utilizados quando necessário. Ele pode armazenar informações como clientes, produtos, funcionários, pedidos e outras informações de uma empresa ou sistema.

Um **Sistema Gerenciador de Banco de Dados (SGBD)** é o software responsável por gerenciar o Banco de Dados. Ele permite que os dados sejam armazenados, consultados, alterados e excluídos. Também ajuda a controlar o acesso aos dados e a evitar problemas durante seu uso.

Alguns exemplos de Bancos de Dados são um banco de dados de clientes de uma loja, um banco de dados de alunos de uma universidade ou um banco de dados de produtos de uma empresa.

Alguns exemplos de SGBDs são:

- **MySQL**
- **PostgreSQL**
- **Oracle Database**
- **Microsoft SQL Server**
- **SQLite**

Por exemplo, uma empresa pode ter um banco de dados contendo informações de seus clientes e utilizar o **MySQL** como SGBD para gerenciar essas informações.

## Q2. Quais os principais problemas de utilizar Sistemas de Arquivos para armazenagem de dados?

O uso de sistemas de arquivos para armazenar dados pode causar problemas como a redundância de informações, quando os mesmos dados são armazenados em diferentes arquivos, ocupando espaço desnecessário. Também pode ocorrer inconsistência, caso uma informação seja alterada em um arquivo e permaneça desatualizada em outro. Além disso, o acesso aos dados pode se tornar mais difícil conforme a quantidade de arquivos aumenta. Quando várias pessoas precisam alterar os mesmos arquivos ao mesmo tempo, podem ocorrer conflitos ou perda de informações. Outro problema está relacionado à segurança, pois pode ser difícil controlar quais usuários podem acessar ou modificar determinados dados. Em caso de falhas, a recuperação das informações também pode ser complicada.


## Q3. Explique as propriedades ACID: atomicidade, consistência, isolamento e durabilidade. Para cada propriedade, descreva um exemplo prático no contexto de uma transferência bancária e explique o que aconteceria se o SGBD não garantisse essa propriedade.

As propriedades ACID garantem que as transações realizadas no banco de dados sejam executadas de forma segura.

**Atomicidade** significa que uma transação deve ser concluída por inteiro ou não ser realizada. Em uma transferência bancária, o valor deve ser retirado da conta de origem e creditado na conta de destino. Se ocorrer uma falha depois do débito, a operação deve ser desfeita. Sem atomicidade, o dinheiro poderia ser retirado da conta de origem sem chegar à conta de destino.

**Consistência** significa que os dados devem continuar seguindo as regras definidas pelo banco de dados após uma transação. Em uma transferência, o saldo das contas deve continuar correto e dentro das regras estabelecidas. Sem consistência, uma operação poderia deixar dados inválidos, como um saldo abaixo do limite permitido.

**Isolamento** significa que transações realizadas ao mesmo tempo não devem interferir umas nas outras de forma incorreta. Por exemplo, se duas transferências forem realizadas ao mesmo tempo na mesma conta, cada uma deve considerar corretamente o saldo disponível. Sem isolamento, as duas operações poderiam usar o mesmo saldo e permitir um valor maior do que o disponível.

**Durabilidade** significa que, depois que uma transação é confirmada, seus dados devem permanecer armazenados mesmo que ocorra uma falha no sistema. Em uma transferência, depois que o banco confirmar a operação, o débito e o crédito devem continuar registrados mesmo após uma queda de energia ou reinicialização do servidor. Sem durabilidade, uma transferência confirmada poderia desaparecer após uma falha.


## Q4. Para cada cenário abaixo, indique qual(is) propriedade(s) ACID está(ão) em jogo e justifique sua resposta: 

### a) Queda de energia no meio de uma transferência deixou o valor debitado da conta de origem, mas não creditado na conta de destino. 
### b) Dois atendentes debitam, ao mesmo tempo, o mesmo saldo de uma conta. 
### c) O sistema confirma a operação, mas após reiniciar o servidor o dado foi perdido. 
### d) Uma transferência que levaria o saldo abaixo do limite permitido é rejeitada pelo banco.

**a)** A propriedade envolvida é a **atomicidade**, pois a transferência deveria realizar o débito e o crédito como uma única operação. Como houve uma queda de energia depois do débito, o SGBD deveria desfazer a operação para que o valor não ficasse apenas retirado da conta de origem.

**b)** A propriedade envolvida é o **isolamento**, pois duas operações estão acontecendo ao mesmo tempo sobre a mesma conta. O SGBD deve garantir que uma operação não interfira de forma incorreta na outra, evitando que as duas utilizem o mesmo saldo disponível.

**c)** A propriedade envolvida é a **durabilidade**, pois uma operação confirmada deve continuar registrada mesmo depois de uma falha ou reinicialização do servidor. Se o dado foi perdido, essa propriedade não foi garantida.

**d)** A propriedade envolvida é a **consistência**, pois o banco deve manter suas regras após uma operação. Como a transferência faria o saldo ficar abaixo do limite permitido, ela deve ser rejeitada para manter os dados dentro das regras definidas.


## Q5. Um SGBD trata dos seguintes aspectos: recuperação, integridade, redundância e inconsistência. Explique cada um deles e descreva como o SGBD os gerencia.

A **recuperação** está relacionada à capacidade de recuperar os dados após uma falha no sistema, evitando que as informações sejam perdidas. A **integridade** garante que os dados permaneçam corretos e sigam as regras definidas no banco. A **redundância** ocorre quando uma mesma informação é armazenada mais de uma vez, e o SGBD busca reduzir essa repetição para evitar desperdício e problemas nos dados. A **inconsistência** acontece quando existem informações diferentes para um mesmo dado. O SGBD ajuda a evitar esse problema mantendo os dados atualizados e seguindo as regras de integridade.


## Q6. Considere o cenário de uma empresa de desenvolvimento de software que atende outras empresas como clientes. A empresa organiza seu trabalho em squads (equipes) compostas por desenvolvedores, testadores, líder técnico, supervisor e gerente de produto. Cada squad resolve tarefas (issues) e planeja releases, testes e o cronograma de sprints (iterações) dos projetos de cada cliente.

## Sem utilizar SQL, elabore um mini-projeto conceitual do banco de dados dessa empresa, deixando claro: 
## a) As principais entidades envolvidas (clientes, squads, membros, tarefas, projetos, sprints, releases). 
## b) Os principais atributos de cada entidade. 
## c) Os relacionamentos entre as entidades (com a cardinalidade, ex.: "um cliente pode ter vários projetos"). 
## d) Em linguagem natural, as regras de integridade (restrições) que o banco de dados deveria garantir, ex.: "apenas um líder por squad", "toda tarefa precisa estar vinculada a um projeto".

### a) e b) Entidades principais e seus atributos

**Cliente**
- id_cliente (identificador)
- razão_social
- CNPJ
- contato_principal (nome, e-mail, telefone)
- data_início_contrato

**Projeto**
- id_projeto
- nome_projeto
- descrição
- data_início
- data_previsão_fim
- status (planejado, em andamento, concluído, cancelado)

**Squad**
- id_squad
- nome_squad
- data_formação
- área_foco (ex.: mobile, backend, dados)

**Membro** (pessoa da equipe)
- id_membro
- nome
- e-mail
- cargo/função (desenvolvedor, testador, líder técnico, supervisor, gerente de produto)
- data_admissão

**Tarefa (Issue)**
- id_tarefa
- título
- descrição
- tipo (bug, melhoria, nova funcionalidade)
- prioridade
- status (aberta, em progresso, em teste, concluída)
- data_criação
- data_conclusão

**Sprint**
- id_sprint
- número_sprint
- data_início
- data_fim
- objetivo_sprint

**Release**
- id_release
- versão
- data_planejada
- data_efetiva
- notas_de_release
- status (planejada, em teste, publicada)

---

### c) Relacionamentos e cardinalidades

1. **Cliente — Projeto**
   Um cliente pode ter vários projetos; cada projeto pertence a exatamente um cliente.
   *(1 Cliente : N Projetos)*

2. **Projeto — Squad**
   Um projeto pode ser atendido por uma ou mais squads ao longo do tempo, e uma squad pode atender vários projetos (simultaneamente ou não).
   *(N Projetos : N Squads — relacionamento muitos-para-muitos, podendo ter atributos como "data de alocação")*

3. **Squad — Membro**
   Uma squad é composta por vários membros; um membro pertence, em um dado momento, a uma única squad (podendo mudar ao longo do tempo).
   *(1 Squad : N Membros)*

4. **Squad — Membro (papel de Líder Técnico e Supervisor)**
   Dentro da squad, um membro específico ocupa a função de líder técnico e outro a de supervisor.
   *(1 Squad : 1 Líder Técnico; 1 Squad : 1 Supervisor — relacionamento especial de "papel")*

5. **Projeto — Sprint**
   Um projeto pode ter várias sprints ao longo do tempo; cada sprint pertence a exatamente um projeto.
   *(1 Projeto : N Sprints)*

6. **Sprint — Tarefa**
   Uma sprint agrupa várias tarefas planejadas para aquele período; uma tarefa pode estar associada a uma sprint por vez (mas pode não estar associada a nenhuma, se ainda não planejada).
   *(1 Sprint : N Tarefas)*

7. **Projeto — Tarefa**
   Um projeto possui várias tarefas; cada tarefa pertence a exatamente um projeto.
   *(1 Projeto : N Tarefas)*

8. **Membro — Tarefa**
   Um membro pode ser responsável por várias tarefas; uma tarefa é atribuída a um (ou eventualmente mais de um) membro responsável.
   *(1 Membro : N Tarefas, podendo ser N:N se houver múltiplos responsáveis/colaboradores por tarefa)*

9. **Projeto — Release**
   Um projeto pode ter várias releases ao longo do tempo; cada release pertence a exatamente um projeto.
   *(1 Projeto : N Releases)*

10. **Release — Tarefa**
    Uma release agrupa várias tarefas concluídas que serão entregues; uma tarefa pode estar vinculada a, no máximo, uma release.
    *(1 Release : N Tarefas)*

11. **Sprint — Release** (opcional, dependendo do processo)
    Uma release pode ser gerada ao final de uma ou mais sprints.
    *(N Sprints : 1 Release, ou N:N se uma sprint alimentar mais de uma release)*

---

### d) Regras de integridade (restrições em linguagem natural)

- Toda tarefa deve estar vinculada a exatamente um projeto (não pode existir tarefa "solta").
- Todo projeto deve estar vinculado a exatamente um cliente.
- Uma squad deve ter exatamente um líder técnico e exatamente um supervisor ativos por vez.
- Um membro não pode ocupar simultaneamente duas funções de liderança (líder técnico e supervisor) na mesma squad.
- Um membro só pode pertencer a uma squad ativa por vez (não pode estar alocado a duas squads simultaneamente).
- Toda sprint deve pertencer a um único projeto e não pode ter suas datas sobrepostas com outra sprint do mesmo projeto.
- A data de fim de uma sprint deve ser posterior à data de início.
- Uma tarefa só pode ser incluída em uma sprint se pertencer ao mesmo projeto da sprint.
- Uma tarefa só pode ser incluída em uma release se pertencer ao mesmo projeto da release.
- Uma release só pode ser marcada como "publicada" se todas as tarefas vinculadas a ela estiverem com status "concluída".
- Uma tarefa só pode ter seu status alterado para "concluída" se possuir ao menos um membro responsável atribuído.
- Todo squad deve ter pelo menos um desenvolvedor e um testador para poder ser considerado ativo.
- O CNPJ de cada cliente deve ser único no sistema (não pode haver duplicidade).
- A data de conclusão de uma tarefa, quando existir, não pode ser anterior à sua data de criação.
- Um projeto não pode ser marcado como "concluído" se ainda houver tarefas abertas ou em progresso vinculadas a ele.