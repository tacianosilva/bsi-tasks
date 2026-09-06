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