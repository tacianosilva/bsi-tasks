## Q1. Banco de Dados e SGBD

### Banco de Dados

Um Banco de Dados é uma coleção organizada de dados que são armazenados de forma estruturada, permitindo que as informações sejam consultadas, atualizadas e gerenciadas de maneira eficiente.

Por exemplo, um sistema de uma universidade pode possuir um banco de dados contendo informações sobre alunos, cursos, professores, disciplinas e matrículas.

### Sistema Gerenciador de Banco de Dados (SGBD)

Um Sistema Gerenciador de Banco de Dados (SGBD) é um software responsável por permitir a criação, armazenamento, consulta, alteração e gerenciamento dos dados de um banco de dados. Ele também fornece recursos para controlar o acesso aos dados, garantir sua integridade, segurança e realizar operações de forma confiável.

Alguns exemplos de SGBDs são:

- PostgreSQL;
- MySQL;
- Oracle Database;
- Microsoft SQL Server;
- SQLite.

### Exemplos de Bancos de Dados e seus SGBDs

| Banco de Dados | SGBD |
|---|---|
| Banco de dados de uma universidade | PostgreSQL |
| Banco de dados de uma loja virtual | MySQL |
| Banco de dados de uma instituição financeira | Oracle Database |
| Banco de dados de uma empresa | Microsoft SQL Server |
| Banco de dados de um aplicativo | SQLite |

## Q2. Problemas dos Sistemas de Arquivos

A utilização de sistemas de arquivos para armazenar dados pode apresentar diversos problemas, principalmente quando há uma grande quantidade de informações ou vários usuários acessando os dados simultaneamente.

Os principais problemas são:

- **Redundância de dados:** as mesmas informações podem ser armazenadas em diferentes arquivos, causando duplicação desnecessária.
- **Inconsistência dos dados:** quando uma informação duplicada é alterada em um arquivo, mas não em outro, os dados podem ficar diferentes entre si.
- **Dificuldade de acesso:** encontrar e consultar informações pode ser mais trabalhoso, principalmente quando os dados estão espalhados em vários arquivos.
- **Problemas de segurança:** pode ser difícil controlar quais usuários podem visualizar ou modificar determinadas informações.
- **Dificuldade de compartilhamento:** vários usuários ou programas podem ter dificuldade para acessar e modificar os mesmos dados de forma segura.
- **Problemas de concorrência:** quando duas pessoas ou sistemas tentam alterar o mesmo arquivo ao mesmo tempo, podem ocorrer conflitos ou perda de informações.
- **Dificuldade de recuperação:** em caso de falhas, como queda de energia ou corrupção de arquivos, pode ser difícil recuperar os dados corretamente.
- **Falta de integridade:** o sistema de arquivos não possui mecanismos próprios suficientes para garantir que os dados armazenados sigam regras e sejam válidos.

Os SGBDs foram desenvolvidos para solucionar grande parte desses problemas, oferecendo mecanismos de controle de acesso, integridade, concorrência, recuperação e gerenciamento dos dados.

## Q3. Propriedades ACID

As propriedades ACID são características que garantem que as transações realizadas em um banco de dados sejam executadas de maneira confiável. ACID significa Atomicidade, Consistência, Isolamento e Durabilidade.

### Atomicidade

A atomicidade garante que uma transação seja realizada completamente ou não seja realizada. Ou seja, todas as operações de uma transação devem ser concluídas com sucesso; caso contrário, todas devem ser desfeitas.

Em uma transferência bancária, por exemplo, é necessário debitar R$ 100,00 da conta de origem e creditar R$ 100,00 na conta de destino. Se ocorrer uma falha depois do débito, mas antes do crédito, a operação deve ser desfeita e o valor deve retornar à conta de origem.

Sem atomicidade, poderia ocorrer uma situação em que o dinheiro fosse retirado da conta de origem, mas não chegasse à conta de destino.

### Consistência

A consistência garante que o banco de dados permaneça em um estado válido antes e depois de uma transação. As regras e restrições definidas no banco de dados devem continuar sendo respeitadas.

Em uma transferência bancária, por exemplo, se uma conta possui R$ 500,00 e uma transferência de R$ 100,00 é realizada, o saldo deve passar para R$ 400,00. O banco também deve garantir que regras como limite de saldo e existência das contas sejam respeitadas.

Sem consistência, uma transferência poderia deixar o banco de dados com informações inválidas, como um saldo incorreto ou uma transferência para uma conta inexistente.

### Isolamento

O isolamento garante que transações executadas simultaneamente não interfiram de maneira incorreta umas nas outras. Cada transação deve funcionar como se estivesse sendo executada de forma independente.

Em uma transferência bancária, imagine que duas operações tentem utilizar o saldo de uma mesma conta ao mesmo tempo. O SGBD deve controlar essas operações para que ambas não utilizem o mesmo saldo antigo e causem um resultado incorreto.

Sem isolamento, duas transferências poderiam ser aprovadas utilizando o mesmo saldo disponível, fazendo com que o valor retirado fosse maior do que o saldo permitido.

### Durabilidade

A durabilidade garante que, depois que uma transação é confirmada, seus dados permaneçam armazenados mesmo que ocorra uma falha no sistema ou uma queda de energia.

Em uma transferência bancária, depois que o banco confirma a operação, o débito e o crédito devem permanecer registrados mesmo que o servidor seja reiniciado logo depois.

Sem durabilidade, uma transferência poderia ser confirmada para o usuário, mas desaparecer do banco de dados após uma falha no servidor.

## Q4. Situações envolvendo as propriedades ACID

### a Queda de energia no meio de uma transferência deixou o valor debitado da conta de origem, mas não creditado na conta de destino.

A propriedade envolvida é principalmente a **Atomicidade**.

Uma transferência bancária deve ser tratada como uma única transação: o valor deve ser debitado da conta de origem e creditado na conta de destino. Se uma queda de energia ocorrer entre essas duas operações, o SGBD deve desfazer o débito para que a transferência não fique parcialmente concluída.

Nesse caso, a atomicidade não foi garantida, pois apenas uma parte da transação foi realizada.

### b Dois atendentes debitam, ao mesmo tempo, o mesmo saldo de uma conta.

A propriedade envolvida é principalmente o **Isolamento**.

Quando duas operações são realizadas simultaneamente sobre a mesma conta, o SGBD deve controlar a execução das transações para evitar que uma operação utilize informações incorretas ou desatualizadas.

Sem isolamento adequado, as duas transações podem ler o mesmo saldo disponível e ambas realizarem o débito, causando um saldo incorreto ou permitindo que a conta seja utilizada além do limite permitido.

### c O sistema confirma a operação, mas após reiniciar o servidor o dado foi perdido.

A propriedade envolvida é a **Durabilidade**.

Depois que uma transação é confirmada, seus resultados devem permanecer armazenados mesmo após uma falha do sistema, queda de energia ou reinicialização do servidor.

Nesse caso, a durabilidade não foi garantida porque a operação foi confirmada, mas o dado foi perdido após o reinício.

### d Uma transferência que levaria o saldo abaixo do limite permitido é rejeitada pelo banco.

A propriedade envolvida é principalmente a **Consistência**.

O banco de dados possui regras que precisam ser respeitadas, como a restrição de que o saldo não pode ficar abaixo de determinado limite. Antes de confirmar a transferência, o SGBD deve verificar essas regras.

Nesse caso, a operação é rejeitada para impedir que o banco de dados fique em um estado inválido.

## Q5. Recuperação, integridade, redundância e inconsistência

### Recuperação

A recuperação é o conjunto de mecanismos utilizados para restaurar o banco de dados após uma falha, como queda de energia, erro do sistema ou falha de hardware.

O SGBD utiliza recursos como logs de transações, backups e mecanismos de recuperação para tentar garantir que os dados não sejam perdidos ou permaneçam em um estado incorreto após uma falha.

Por exemplo, se ocorrer uma queda de energia durante uma transferência bancária, o SGBD pode utilizar as informações registradas no log para desfazer uma operação incompleta ou recuperar uma transação que já havia sido confirmada.

### Integridade

A integridade está relacionada à garantia de que os dados armazenados sejam válidos, corretos e estejam de acordo com as regras definidas para o banco de dados.

O SGBD gerencia a integridade por meio de restrições e regras, como chaves primárias, chaves estrangeiras, valores obrigatórios e restrições de domínio.

Por exemplo, uma chave estrangeira pode impedir que uma venda seja cadastrada para um cliente que não existe no banco de dados.

### Redundância

A redundância ocorre quando uma mesma informação é armazenada mais de uma vez sem necessidade.

O SGBD pode reduzir a redundância por meio de uma boa organização do banco de dados, como a normalização, que busca dividir os dados em estruturas relacionadas de forma adequada.

Por exemplo, em vez de armazenar os dados completos de um cliente em todas as suas compras, os dados do cliente podem ser armazenados uma única vez e relacionados aos registros de suas compras.

### Inconsistência

A inconsistência ocorre quando existem informações diferentes ou incorretas para representar o mesmo dado.

O SGBD busca evitar inconsistências por meio do controle de integridade, das transações e do controle de concorrência.

Por exemplo, se duas partes do sistema possuem informações diferentes sobre o saldo de uma conta, existe uma inconsistência. O SGBD utiliza mecanismos de transação e controle de concorrência para evitar que operações simultâneas deixem o banco de dados em um estado incorreto.

## Q6. Mini-projeto conceitual de uma empresa de desenvolvimento de software

Considerando o cenário apresentado, pode-se elaborar um modelo conceitual para representar os principais dados utilizados pela empresa de desenvolvimento de software.

### a Entidades envolvidas

As principais entidades identificadas são:

- **Cliente:** empresa que contrata os serviços de desenvolvimento.
- **Projeto:** trabalho desenvolvido para um cliente.
- **Squad:** equipe responsável pelo desenvolvimento de um ou mais projetos.
- **Membro:** profissional que participa de uma squad.
- **Tarefa:** atividade ou issue que precisa ser realizada dentro de um projeto.
- **Sprint:** período de desenvolvimento em que um conjunto de tarefas é planejado e executado.
- **Release:** versão ou entrega do projeto disponibilizada ao cliente.

### b Principais atributos

#### Cliente

- id_cliente
- nome
- CNPJ
- email
- telefone

#### Projeto

- id_projeto
- nome
- descrição
- data_inicio
- data_fim
- status

#### Squad

- id_squad
- nome
- descrição

#### Membro

- id_membro
- nome
- email
- cargo
- data_entrada

O atributo **cargo** pode representar funções como desenvolvedor, testador, líder técnico, supervisor ou gerente de produto.

#### Tarefa

- id_tarefa
- título
- descrição
- status
- prioridade
- data_criacao
- data_conclusao

#### Sprint

- id_sprint
- nome
- data_inicio
- data_fim
- objetivo
- status

#### Release

- id_release
- versão
- data_prevista
- data_lancamento
- status
- descrição

### c Relacionamentos e cardinalidades

#### Cliente — Projeto

Um **cliente pode possuir vários projetos**, enquanto cada projeto pertence a um único cliente.

**Cardinalidade:** Cliente (1) — (N) Projeto.

#### Projeto — Squad

Um **projeto pode ser desenvolvido por uma ou várias squads**, e uma squad pode trabalhar em vários projetos.

**Cardinalidade:** Projeto (N) — (N) Squad.

#### Squad — Membro

Uma **squad é formada por vários membros**, e um membro pode participar de uma ou mais squads ao longo dos projetos.

**Cardinalidade:** Squad (N) — (N) Membro.

#### Projeto — Tarefa

Um **projeto possui várias tarefas**, enquanto cada tarefa deve estar vinculada a um único projeto.

**Cardinalidade:** Projeto (1) — (N) Tarefa.

#### Projeto — Sprint

Um **projeto pode possuir várias sprints**, e cada sprint pertence a um único projeto.

**Cardinalidade:** Projeto (1) — (N) Sprint.

#### Sprint — Tarefa

Uma **sprint pode possuir várias tarefas**, e uma tarefa pode ser planejada para uma sprint. Uma tarefa também pode existir antes de ser atribuída a uma sprint.

**Cardinalidade:** Sprint (1) — (N) Tarefa.

#### Projeto — Release

Um **projeto pode possuir várias releases**, enquanto cada release pertence a um único projeto.

**Cardinalidade:** Projeto (1) — (N) Release.

#### Membro — Tarefa

Um **membro pode ser responsável por várias tarefas**, enquanto uma tarefa pode possuir um membro responsável.

**Cardinalidade:** Membro (1) — (N) Tarefa.

### d Regras de integridade

O banco de dados deve garantir algumas regras para manter os dados corretos e consistentes:

1. Todo cliente deve possuir um identificador único.

2. Todo projeto deve estar vinculado a um cliente existente.

3. Um cliente pode possuir vários projetos, mas cada projeto deve pertencer a apenas um cliente.

4. Uma tarefa deve estar vinculada a um projeto existente.

5. Uma sprint deve estar vinculada a um projeto existente.

6. Uma release deve estar vinculada a um projeto existente.

7. Uma tarefa não pode ser atribuída a uma sprint pertencente a outro projeto.

8. Uma tarefa pode possuir apenas um membro responsável por vez.

9. Uma squad deve possuir pelo menos um membro.

10. Cada membro deve possuir uma função definida dentro da equipe.

11. Cada squad deve possuir apenas um líder técnico responsável pela equipe.

12. Uma squad pode possuir vários desenvolvedores e testadores.

13. Uma squad pode possuir apenas um supervisor responsável pela equipe.

14. Uma squad pode possuir um gerente de produto responsável pelo acompanhamento do produto.

15. As datas de uma sprint devem ser válidas, de forma que a data de início não seja posterior à data de término.

16. As datas de uma release devem ser compatíveis com o cronograma do projeto.

17. Os identificadores de clientes, projetos, squads, membros, tarefas, sprints e releases devem ser únicos.

18. Uma tarefa concluída deve possuir seu status registrado como concluído e, quando aplicável, uma data de conclusão.

19. Uma release não deve ser marcada como lançada antes de sua data de lançamento.

20. Um projeto encerrado não deve receber novas tarefas ou sprints sem uma alteração válida de seu estado.

Essas regras ajudam o SGBD a manter os dados íntegros, consistentes e relacionados corretamente, evitando registros inválidos ou informações conflitantes.