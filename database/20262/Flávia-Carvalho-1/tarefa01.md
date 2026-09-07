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