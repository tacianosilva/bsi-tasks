## Q1. Descreva o que é um Banco de Dados e o que é um Sistema Gerenciador de Banco de Dados. Cite exemplos de Bancos de Dados e seus SGBDs. 

Um banco de dados é uma coleção de dados estruturados logicamente e inter relacionados, referente a algum aspecto do mundo real. 

SGBD é um sistema de software que permite gerenciar o banco de dados, essa gerência inclui a capacidade de, definição, manipulação, construção(organização das tabelas e dados), segurança, integridade,  e compartilhamento entre diferentes usuários e aplicações.

Exemplo: Um caixa de uma lanchonete vai efetuar uma venda de um produto x, venda essa que será registrada no banco de dados. Para esse processo acontecer, primeiro é preciso que exista uma banco de dados já estruturado de forma lógica, onde haveria um tabela para os produtos, relacionada a tabela de vendas, supondo que o SGBD seja o MYSQL ele vai vai ser responsável por fazer a ponte entre a aplicação e o banco de dados, processando e gerenciando esse novo dado, depois por fim, atualizando o banco de dados armazenado e o metadados.


## Q2. Quais os principais problemas de utilizar Sistemas de Arquivos para armazenagem de dados? 

Como o salvamento em arquivos não usufrui das funcionalidades do SGBD, ele apresenta diversos problemas. Dados duplicados em diferentes arquivos, arquivos podem apresentar diversos erros e inconsistências ao longo do tempo, conforme a aplicação cresce. Há falta de funcionalidades para aplicar filtros de pesquisa, edição e exclusão com filtros, sendo necessário que o desenvolvedor crie a lógica do zero, o que dá bem mais trabalho e consome tempo. Em casos em que as consultas já foram previamente estipuladas, no meio do desenvolvimento podem aparecer novos tipos de buscas que vão precisar ser implementadas toda vez, e em alguns casos é preciso criar uma aplicação nova para lidar com isso. Os arquivos de dados podem estar em formatos diferentes, e essa falta de padronização dificulta a construção de aplicações, pois o desenvolvedor precisa traduzi-los para que um se relacione com o outro. É difícil criar novas restrições ou editá-las, uma vez que estão diretamente inseridas dentro do código da aplicação, sendo preciso encontrar essa parte do código, modificá-la e depois testar toda vez que for necessário. Como os dados podem se repetir e diferentes pessoas podem manipulá-los sem restrições, isso por si só já é um problema de segurança, além de provocar divergências na hora de atualizar ou editar esses dados

## Q3. Explique as propriedades ACID: atomicidade, consistência, isolamento e durabilidade. Para cada propriedade, descreva um exemplo prático no contexto de uma transferência bancária e explique o que aconteceria se o SGBD não garantisse essa propriedade. 

Atomicidade: É quando a operação do banco de dados deve acontecer ou simplesmente não deve acontecer, o famoso 8 ou 80, não existe meio termo, em caso de falha, o banco de dados deve apenas permanecer em seu estado original sem alteração. Numa transferência bancária, onde eu vou retirar dinheiro de um conta A e passar para uma conta B, está ocorrendo duas operações, onde o dinheiro precisa ser debitado da conta A e depositado da conta B, num cenário que ele chega a conta B e não é debitado da A, também estaria errado, assim como se ele fosse debitado da A e não chegasse a conta B. 

Consistência: É quando um banco de dados já válido passa por uma transação e continua válido, de acordo com as restrições já predefinidas do banco. Em um caso que eu tenha 100 reais na conta e deposite apenas mais 100, um caso de inconsistência poderia acarretar que o depósito, no final, fosse efetuado como 1000, totalizando 1100 na minha conta bancária, ou, se eu tentar sacar uma quantia maior do que eu já tenho presente na minha conta, o sistema não deverá permitir para poder manter a consistência. 

isolamento: em um banco de dados, é comum que diversas transações ocorram sobre a mesma tabela; o isolamento garante que o banco de dados se mantenha estável mesmo diante de tantas transações simultâneas. Em um caso onde duas pessoas têm uma conta compartilhada em um banco, pessoa A e B vão debitar, ao mesmo tempo, o valor total presente na conta, o isolamento garante que a transação que chegar primeiro vai ocorrer e debitar o valor para quem a fez, e a transação da outra pessoa será cancelada. 

durabilidade: garante que uma transação feita se mantenha no seu estado de conclusão, mesmo que o sistema apresente algum problema, isso se torna possível através do salvamento em dispositivos de memória, como HD e SSD. um sistema bancário onde uma pessoa debite todo o valor de sua conta e após esse débito, aconteça uma falha no sistema, mesmo após o sistema voltar a funcionar, o valor que foi debitado deve permanecer. 

## Q4. Para cada cenário abaixo, indique qual(is) propriedade(s) ACID está(ão) em jogo e justifique sua resposta: a) Queda de energia no meio de uma transferência deixou o valor debitado da conta de origem, mas não creditado na conta de destino. b) Dois atendentes debitam, ao mesmo tempo, o mesmo saldo de uma conta. c) O sistema confirma a operação, mas após reiniciar o servidor o dado foi perdido. d) Uma transferência que levaria o saldo abaixo do limite permitido é rejeitada pelo banco. 

A) Atomicidade: diz que a transação ou deve ocorrer 100% certa ou não ocorrer, nesse caso ela foi violada pois, o banco deveria se manter no estado original antes de qualquer debitação.

B)Isolamento: Não deveria ser possível ocorrer, pois o isolamento através do gerenciamento de bloqueio garante que as transações ocorram como uma fila, só pode passar uma por vez, e não duas juntas.

C)Durabilidade: Após a efetivação completa da operação o sistema deve manter o estado válido, mesmo que ocorra alguma gravidade que afete o sistema, através do salvamento em dispositivos de memórias como SSD ou HD.

D)Consistência: O banco de dados em estado válido deve permanecer válido após cada transação. Como tentou debitar um valor que não existia, o princípio da consistência não permite que a transação aconteça, mantendo o banco em seu estado original. 

## Q5. Um SGBD trata dos seguintes aspectos: recuperação, integridade, redundância e inconsistência. Explique cada um deles e descreva como o SGBD os gerencia.

Recuperação: O SGBD garante uma recuperação do estado anterior do banco de dados após uma transação que ocorreu de forma falha, ou mantém o estado do banco caso ocorra algum problema no sistema, através do salvamento em dispositivos de memória, através de um checkpoint que o SGBD cria. O SGBD também utiliza um log de transação(arquivo binário gravado no dispositivo de memória), onde se registram todas as alterações mesmo sem ter aplicado elas ao banco, e em caso de falha, ele consulta esse log para saber se deu certo ou não. 

integridade: É a gerência que o SGBD faz para verificar se os dados que vão para o banco de dados são válidos. Ele faz essa verificação através de restrições predefinidas, que devem ser atendidas quando um dado vai ser inserido, alterado, excluído ou consultado. Garante também que os relacionamentos entre tabelas sejam logicamente estruturados para que se tornem válidos. 

redundância: O SGBD usa da normalização para dividir os dados em diferentes tabelas relacionadas entre si. No caso em que uma pessoa realiza uma compra em algum site, vai haver a tabela Compra e a tabela Cliente, em vez de armazenar tudo em uma tabela só. Chaves primárias também servem para evitar redundância, pois só pode haver um registro com a mesma chave primária, garantindo que cada linha seja única. 

inconsistência: É quando banco de dados válido passa para o estado invalido, o SGBD lida com isso utilizando sistemas de rollbacks por salvamento em log de transação, restaurando o banco de dados ao seu estado original, em casos de transação inválidas.
