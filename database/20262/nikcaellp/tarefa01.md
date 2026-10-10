## Q1-Descreva o que é um Banco de Dados e o que é um Sistema Gerenciador de Banco de Dados. Cite exemplos de Bancos de Dados e seus SGBDs.
Resposta: Banco de dados seria um "local" (geralmente um servidor em nuvem) dedicado ao armazenamento de dados, é utilizado no intuito de centralizar e organizar dados em um ambiente preparado para isso.

SGBDs: São sistemas de gerenciamento de banco de dados, utilizados para gerenciar os dados de uma maneira padronizada para criar, organizar, manipular e proteger. exemplos de SGBDs e Seus Bancos de dados:
- mySQL: Banco de dados relacional de uma empresa
- mongoDB: Banco de dados orientado a documentos
- oracleDB: Banco de dados relacional de uma empresa
- postgreSQL: Banco de dados de uma aplicação

## Q2. Quais os principais problemas de utilizar Sistemas de Arquivos para armazenagem de dados?
Os principais seriam a organização dos dados, evitar inconsistências, reduzir redundâncias, dificuldades de acessos e consultas, segurança, dificuldades de compartilhamento, concorrência e problemas de integridade

## Q3. Explique as propriedades ACID: atomicidade, consistência, isolamento e durabilidade. Para cada propriedade, descreva um exemplo prático no contexto de uma transferência bancária e explique o que aconteceria se o SGBD não garantisse essa propriedade.
As propriedades ACID garentem confiabilidade e padronização de armazenamento e gerenciamento dos dados, a uma maneira que garante que os dados só possam ser alterados se seguirem as observações da ACID.
exemplos para cada propriedade em uma transferência bancária: 

* Atomicidade: exige que cada transação seja restaurada ao estado anterior se houver alguma falha em qualquer parte do processo. 
Uma transferência de R$ 100 deve retirar o valor da conta A e adicionar à conta B. Se ocorrer uma falha no meio, toda a transação deve ser desfeita.

* Consistência: assegura que os dados obedecem a todas as regras e restrições do sistema. 
Após a transferência, as regras do banco devem continuar válidas, como não permitir que uma conta fique com um saldo inválido. Sem consistência, os dados poderiam ficar em um estado que viola as regras do sistema.

* Isolamento: Transações executadas ao mesmo tempo não interferem umas nas outras.
Duas transferências ocorrendo simultaneamente não devem causar interferência entre si.

*Durabilidade: Depois que uma transação é confirmada (salva), os dados ficam garantidos permanentemente.
Depois que a transferência for confirmada, ela deve continuar registrada mesmo se o servidor ou sistema for reiniciado.

## Q4. Para cada cenário abaixo, indique qual(is) propriedade(s) ACID está(ão) em jogo e justifique sua resposta: 
a) Queda de energia no meio de uma transferência deixou o valor debitado da conta de origem, mas não creditado na conta de destino:  
Atomicidade: nesse cenário a atomicidade iria garantir que após a queda de energia o valor não seria debitado da conta de origem, pós a transação não foi encerrada, por isso o processo todo teria que ser cancelado.

b) Dois atendentes debitam, ao mesmo tempo, o mesmo saldo de uma conta. 
Isolamento: As duas operações ocorrem simultaneamente e precisam ser isoladas para que uma não interfira nos dados utilizados pela outra.

c) O sistema confirma a operação, mas após reiniciar o servidor o dado foi perdido.
Durabilidade: a propriedade nessa situação teria que garantir que após o servidor fosse reiniciado, os dados ainda estariam salvos e armazenados

d) Uma transferência que levaria o saldo abaixo do limite permitido é rejeitada pelo banco.
Consistência: impede que uma regra do sistema seja quebrada, já que sem saldo suficeinte a transação não seria permitida

## Q5. Um SGBD trata dos seguintes aspectos: recuperação, integridade, redundância e inconsistência. Explique cada um deles e descreva como o SGBD os gerencia.
Um SGBD tem como objetivo facilitar o gerenciamento dos dados, garantindo sua organização, segurança e confiabilidade. 
A recuperação permite restaurar os dados após falhas, utilizando mecanismos como backups e registros das transações. A integridade garante que os dados permaneçam corretos e respeitem as regras estabelecidas pelo sistema. 
A redundância é controlada para evitar a duplicação desnecessária de informações, reduzindo o desperdício de espaço e possíveis conflitos. 
Já a inconsistência é evitada por meio de mecanismos que garantem que os dados permaneçam corretos e coerentes durante as operações realizadas no banco.

## Q6.
Principais Entidades e Atributos

Entidade: Cliente
Atributos:
id_cliente
nome
CNPJ
email
telefone

Entidade: Projeto
Atributos:
id_projeto
nome
descricao
data_inicio
data_fim
status

entidade: Equipes
Atributos: 
id_squad
nome
descricao

Entidade: Membro
Atributos: 
id_membro
nome
email
cargo

Entidade: Tarefa
Atributos: 
id_tarefa
titulo
descricao
status
prioridade
data_criacao
data_conclusao

Entidade: Sprint
Atributos: 
id_sprint
nome
data_inicio
data_fim
objetivo

Entidade: Release
Atributos: 
id_release
versao
data_lancamento
descricao
status

Relacionamentos e cardinalidades
Cliente → Projeto: um cliente pode ter vários projetos, mas cada projeto pertence a um único cliente. (1,n)(1,1)
Projeto → Squad: um projeto pode ser atendido por um ou vários squads, e um squad pode trabalhar em um ou vários projetos.(1,n)(1,n)
Squad → Membro: um squad possui vários membros, e um membro pode participar de um ou vários squads.(1,n)(1,n)
Projeto → Tarefa: um projeto pode possuir várias tarefas, e cada tarefa pertence a um único projeto.(1,n) (1,1)
Projeto → Sprint: um projeto pode possuir várias sprints, e cada sprint pertence a um projeto.(1,n)(1,1)
Sprint → Tarefa: uma sprint pode conter várias tarefas, e uma tarefa pode ser planejada em uma sprint.(1,n)(0,1)
Projeto → Release: um projeto pode possuir várias releases, e cada release pertence a um projeto.(1,n) (1,1)
Release → Tarefa: uma release pode incluir várias tarefas, e uma tarefa pode estar associada a uma release.(1,n) (0,1)

Regras de integridade
O banco de dados deve garantir que:

Todo projeto esteja vinculado a um cliente existente.
Toda tarefa esteja vinculada a um projeto.
Toda sprint esteja vinculada a um projeto.
Toda release esteja vinculada a um projeto.
Um squad deve possuir pelo menos um membro.
Cada squad deve possuir apenas um líder técnico, um supervisor e um gerente de produto.
Um membro não pode ocupar simultaneamente cargos incompatíveis dentro do mesmo squad.
A data de término de uma sprint não pode ser anterior à sua data de início.
Uma release deve possuir uma versão e estar vinculada a um projeto válido.
Uma tarefa não pode ser atribuída a uma sprint de outro projeto.

[Diagrama da Q6](https://app.brmodeloweb.com/publicview/6a9d94904aef6b43c180c202)
