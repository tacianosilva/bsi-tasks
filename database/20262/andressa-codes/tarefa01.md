**Tarefa 01 \- Conceitos de BD, ACID e SGBD**

**Q1.** Descreva o que é um Banco de Dados e o que é um Sistema Gerenciador de Banco de Dados. Cite exemplos de Bancos de Dados e seus SGBDs.

Banco de dados é o local onde as informações geradas por um determinado sistema são armazenadas, organizadas e relacionadas entre si, para que posteriormente essas informações possam ser recuperadas e reutilizadas com um intuito específico. Já um Sistema Gerenciador de Banco de Dados (SGBD) é o intermediário entre os dados (grandes volumes) em sua forma bruta e os usuários (ou programas) que precisam acessar esses dados, além de eventualmente atuar como uma proteção a esse dados, como por exemplo filtrando quem pode ou não acessar as informações, entre outros. Existem muitos tipos de banco de dados, mas atualmente o mais utilizado é o relacional, onde os dados são organizados em tabelas (ex: MySQL, Oracle, SQLite).

**Q2.** Quais os principais problemas de utilizar Sistemas de Arquivos para armazenagem de dados?

Inconsistência e redundância de dados, dificuldade ao acessar dados, isolamento de dados, problemas de integridade e atomicidade, anomalias no acesso concorrente e problemas de segurança.

**Q3.** Explique as propriedades **ACID**: atomicidade, consistência, isolamento e durabilidade. Para cada propriedade, descreva um exemplo prático no contexto de uma transferência bancária e explique o que aconteceria se o SGBD não garantisse essa propriedade.

A atomicidade é o processo onde duas ou mais operações devem acontecer em conjunto, ou seja, se uma não for realizada a outra também não deve. Ex: Em uma transferência bancária de um determinado valor, esse valor deve ser retirado da conta A para a conta B, caso o valor seja retirado da conta A, porém não depositado na conta B devido a uma falha, essa transferência deve ser desfeita. Se o SGBD não garantisse a atomicidade essa falha não seria desfeita.

Já a consistência é o que garante que os dados permaneçam corretos e respeitem as regras definidas no banco de dados. Ex: Um determinado banco possui a regra onde a conta não pode ficar com saldo negativo e um usuário quer fazer uma transferência de 500 reais tendo somente 400 disponíveis na conta, o SGBD deve impedir essa transferência. Caso o SGBD não garantisse a consistência essa transferência ocorreria e o usuário ficaria com um saldo de -100.

O isolamento por sua vez garante que operações realizadas simultaneamente não interfiram umas nas outras de forma incorreta. Ex: duas transferências podem ser realizadas ao mesmo tempo em uma conta e o SGBD deve garantir que as duas sejam processadas corretamente. Se não garantisse o isolamento uma operação poderia interferir na outra e o saldo final ficaria incorreto.

E por fim a durabilidade é onde uma vez que o SGBD confirma uma operação, essa confirmação permanece salva mesmo que aconteça alguma falha posteriormente. Ex: Um usuário faz uma transferência de 100 reais para outra conta e o banco confirma a transação, porém em algum determinado momento o sistema cai, quando o sistema voltar a funcionar a transferência ainda deverá estar registrada e os saldos deverão continuar atualizados. Se o SGBD não garantisse a durabilidade, uma transferência que já foi confirmada poderia ser perdida após uma falha no sistema.

**Q4.** Para cada cenário abaixo, indique qual(is) propriedade(s) ACID está(ão) em jogo e **justifique** sua resposta:
a) Queda de energia no meio de uma transferência deixou o valor debitado da conta de origem, mas não creditado na conta de destino: **Atomicidade, porque são necessárias que as duas operações ocorram, então a operação citada deveria ser desfeita.**
b) Dois atendentes debitam, ao mesmo tempo, o mesmo saldo de uma conta: **Isolamento, pois as duas operações acontecem ao mesmo tempo em uma mesma conta e, caso o SGBD não intervenha, podem consequentemente causar conflito no saldo.**
c) O sistema confirma a operação, mas após reiniciar o servidor o dado foi perdido: **Durabilidade, já que o dado foi perdido mesmo após a confirmação.**
d) Uma transferência que levaria o saldo abaixo do limite permitido é rejeitada pelo banco: **Consistência, pois a operação foi rejeitada porque violaria uma regra do banco (saldo abaixo do limite permitido).**

**Q5.** Um SGBD trata dos seguintes aspectos: **recuperação, integridade, redundância e inconsistência**. Explique cada um deles e descreva como o SGBD os gerencia.

A recuperação (recovery) é a capacidade de o banco voltar a um estado consistente após uma falha. Nos sistemas de arquivos, garantir isso era difícil, especialmente por causa dos problemas de atomicidade: operações que precisam acontecer em conjunto e que, em caso de falha, exigem que o banco retorne ao estado anterior. O SGBD assume essa responsabilidade através do controle das estratégias de recuperação, uma das funções atribuídas ao DBA.

A integridade garante que os valores armazenados obedeçam a restrições que mantêm a consistência dos dados. Nos sistemas de arquivos, essas restrições ficavam soltas no código de cada aplicação, o que tornava difícil adicionar ou modificar regras. O SGBD centraliza isso através da especificação de restrições de integridade, também definida pelo DBA.

A redundância é a repetição de dados em diferentes lugares. Nos sistemas de arquivos, isso acontecia porque as informações eram armazenadas diretamente em vários arquivos, sem controle centralizado. O SGBD reduz isso ao oferecer o modelo relacional, onde os dados ficam organizados em tabelas relacionadas entre si, evitando duplicações desnecessárias.

A inconsistência ocorre quando cópias redundantes dos dados divergem ao longo do tempo, ou quando atualizações concorrentes de diferentes programas geram resultados conflitantes. O SGBD resolve isso supervisionando o acesso aos dados e controlando as anomalias de acesso concorrente, algo que era muito difícil de garantir manualmente em sistemas de arquivos.

**Q6.** Considere o cenário de uma **empresa de desenvolvimento de software** que atende outras empresas como clientes. A empresa organiza seu trabalho em **squads** (equipes) compostas por desenvolvedores, testadores, líder técnico, supervisor e gerente de produto. Cada squad resolve **tarefas** (issues) e planeja **releases**, testes e o cronograma de **sprints** (iterações) dos projetos de cada cliente.

Sem utilizar SQL, elabore um **mini-projeto conceitual** do banco de dados dessa empresa, deixando claro:
a) As principais **entidades** envolvidas (clientes, squads, membros, tarefas, projetos, sprints, releases).
b) Os principais **atributos** de cada entidade.
c) Os **relacionamentos** entre as entidades (com a cardinalidade, ex.: "um cliente pode ter vários projetos").
d) Em linguagem natural, as **regras de integridade** (restrições) que o banco de dados deveria garantir, ex.: "apenas um líder por squad", "toda tarefa precisa estar vinculada a um projeto".

**a) Principais entidades:**  
Cliente, Projeto, Squad, Membro, Tarefa, Sprint e Release.

**b) Principais atributos:**  
**Cliente:** id_cliente, nome, email e telefone;  
**Projeto:** id_projeto, nome, descrição, data_inicio e data_fim;  
**Squad:** id_squad, nome e objetivo;  
**Membro:** id_membro, nome, email, cargo e especialidade;  
**Tarefa:** id_tarefa, título, descrição, status, prioridade e prazo;  
**Sprint:** id_sprint, nome, data_inicio e data_fim;  
**Release:** id_release, versão, data_prevista e status;

**c) Relacionamentos e cardinalidades**  
Um cliente pode ter vários projetos, mas cada projeto pertence a um cliente;  
Um projeto pode ter vários squads, e um squad pode trabalhar em vários projetos;  
Um squad possui vários membros, mas cada membro pertence a um squad;  
Um projeto pode ter várias tarefas, e cada tarefa pertence a um projeto;  
Um projeto pode ter várias sprints, mas cada sprint pertence a um projeto;  
Um projeto pode ter várias releases, mas cada release pertence a um projeto;  
Uma sprint pode possuir várias tarefas, e uma tarefa pode estar vinculada a uma sprint;  
Uma release pode conter várias tarefas, e uma tarefa pode estar relacionada a uma release;

**d) Regras de integridade**
O banco deve garantir que todo projeto esteja vinculado a um cliente, além disso todo squad deve possuir membros e apenas um líder técnico, também cada membro deve possuir um cargo definido; Toda tarefa precisa estar vinculada a um projeto e deve possuir um status válido, assim como toda sprint e release devem estar vinculadas a um projeto; As datas de início e fim devem ser válidas e a data de fim não pode ser anterior à data de início, além disso não deve ser permitido cadastrar informações obrigatórias vazias ou duplicadas.
