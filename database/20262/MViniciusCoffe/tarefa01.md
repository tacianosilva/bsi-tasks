# Tarefa 01 - Conceitos de Banco de Dados

## Q1. Banco de Dados e SGBD
- Descreva o que é um Banco de Dados e o que é um Sistema Gerenciador de Banco de Dados. Cite exemplos de Bancos de Dados e seus SGBDs.

**Resposta**: Um banco de dados é qualquer organização de dados interrelacionados, armazenados e com contexto. Um SGBD é uma aplicação comercial que gerencia, esquematiza, manipula e armazena os dados. Exemplos: PostgresSQL, MongoDB, Oracle, MariaDB etc

## Q2. Sistemas de Arquivos
- Quais os principais problemas de utilizar Sistemas de Arquivos para armazenagem de dados?

**Resposta**: Os principais problemas são: Operações sobre um mesmo arquivo de dois ou mais programas diferentes podia causa inconsistências, o sistema devia ter um estado anterior para consertar, os dados eram duplicados constantemente, você tinha que saber onde estavam os dados por que cada aplicação tinha seu padrão, além de que qualquer usuário podia ter acesso a dados. Esse e outros problemas que vieram acarretar no surgimento dos SGBDs

## Q3. Propriedades ACID
- Explique as propriedades ACID: atomicidade, consistência, isolamento e durabilidade. Para cada propriedade, descreva um exemplo prático no contexto de uma transferência bancária e explique o que aconteceria se o SGBD não garantisse essa propriedade.

**Resposta**: Essas propriedades são fundamentais para o funcionamento pleno não só de bancos de dados, mas para grande parte das operações de softwares. Para elucidar esses conceitos, vou tratar do seguinte caso: **SGBD Debita os R$ 100 da conta A e deposita o mesmo valor na conta B**
- Atomicidade (Tudo ou nada): Uma transação é uma unidade indivisível, ou as operações rodam, ou o banco não sai de seu estado atual. Se o SGBD falhar nessa parte, pode acontecer que o SGBD debite os 100 reais de uma conta, e, por uma falha subsequente, não deposite o mesmo valor na conta B, fazendo com que o dinheiro sumisse.
- Consistência: Garante que uma transação leve o banco de um estado válido para outro, respeitando regras, restrições e a integridade do sistema. Se o sistema falhasse nessa regra, o SGBD Poderia debitar 100 reais da conta A, mesmo só tendo 10 reais, violando a regra de negócio que diz que não pode ter saldo negativo.
- Isolamento: Garante que múltiplas transações concorrentes ocorram de tal forma que uma não interfira na outra, para a transação 2 ocorrer, a 1 tem que encerrar. Se o SGBD Falhasse nessa operação, o banco poderia sofrer dois débitos de 100 simultâneos, deixando a conta final com um saldo incompatível (Ou negativo)
- Durabilidade: Se a operação já tiver sido feita, ela deve ser permanentemente salva em um meio não-volátil, como SSD ou HDs. Se o sistema falhasse, o SGBD Poderia encerrar uma operação, ela ainda estar na memória RAM e os dados logo voltarem ao estado anterior, ou serem perdidos/corrompidos.

## Q4. Cenários ACID
- Para cada cenário abaixo, indique qual(is) propriedade(s) ACID está(ão) em jogo e justifique sua resposta:

### a) Queda de energia no meio de uma transferência deixou o valor debitado da conta de origem, mas não creditado na conta de destino.

**Resposta**: Atomicidade, pois a operação de débito foi cortada no meio do caminho, fazendo com que o dinheiro sumisse

### b) Dois atendentes debitam, ao mesmo tempo, o mesmo saldo de uma conta.

**Resposta**: Isolamento, pois a operação duplicada pode causar inconsistências. Primeiro uma operação deve ocorrer, depois a outra

### c) O sistema confirma a operação, mas após reiniciar o servidor o dado foi perdido.

**Resposta**: Durabilidade, Pois os dados que estavam na memória primária do servidor foram perdidos, e eles deveriam estar salvos no SSD/HD

### d) Uma transferência que levaria o saldo abaixo do limite permitido é rejeitada pelo banco.

**Resposta**: Consistência, pois as operações devem seguir as regras de negócio (Não deve haver saldo negativo). Portanto, a operação foi rejeitada por ausência de saldo

## Q5. Aspectos tratados por um SGBD
- Um SGBD trata dos seguintes aspectos: recuperação, integridade, redundância e inconsistência. Explique cada um deles e descreva como o SGBD os gerencia.

**Resposta**:

## Q6. Mini-projeto conceitual
- Considere o cenário de uma empresa de desenvolvimento de software que atende outras empresas como clientes. A empresa organiza seu trabalho em squads (equipes) compostas por desenvolvedores, testadores, líder técnico, supervisor e gerente de produto. Cada squad resolve tarefas (issues) e planeja releases, testes e o cronograma de sprints (iterações) dos projetos de cada cliente.

- Sem utilizar SQL, elabore um mini-projeto conceitual do banco de dados dessa empresa, deixando claro: a) As principais entidades envolvidas (clientes, squads, membros, tarefas, projetos, sprints, releases). b) Os principais atributos de cada entidade. c) Os relacionamentos entre as entidades (com a cardinalidade, ex.: "um cliente pode ter vários projetos"). d) Em linguagem natural, as regras de integridade (restrições) que o banco de dados deveria garantir, ex.: "apenas um líder por squad", "toda tarefa precisa estar vinculada a um projeto".


### a) Entidades

**Resposta**:

### b) Atributos

**Resposta**:

### c) Relacionamentos e cardinalidades

**Resposta**:

### d) Regras de integridade

**Resposta**:
