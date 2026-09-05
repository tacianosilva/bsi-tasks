Tarefa 01 - Conceitos De BD
Q1. Banco De Dados e SGBD

Um banco de dados (BD) e um conjunto organizado de dados relacionados entre si
armazenados de forma que possam ser consultados, inseridos,alterados e ultilizados
por sistemas e usuarios.

Um exemplo e o banco de dados de uma empresa que pode armazenar dados/informações
sobre clientes,funcionarios,produtos e pedidos.

Um SGBD ou Sistema Gerenciador de Banco de Dados e o software responsavel por
gerenciar o banco de dados.

Ele fornece recursos para armazenar,consultar,alterar e excluir o banco de dados
tambem auxilia no controle de segurança,integridade,concorrencia e recuperação das informações.

Exemplos de SGBDs:
    MySQL, PostgreSQL, Oracle Database, Microsoft SQL Server e SQLite.

uma empresa pode possuiro um banco de dados contendo os dados dos clientes e pedidos e utilizar o PostgreSQL para gerenciar essas informações.

Q2. Problemas dos Sistemas de Arquivos

Os sistemas de arquivos podem apresentar varios problemas quando usados para armazenar muitos dados.

Um dos principais problemas e a redundancia de dados, pois a mesma informação pode aparecer em varios arquivos.

Tambem pode acontecer a inconsistencia dos dados, quando uma informação e alterada em um arquivo mas continua diferente em outro arquivo.

Outro problema e a dificuldade para controlar o acesso de varios usuarios ao mesmo tempo, pois duas pessoas podem tentar alterar o mesmo dado ao mesmo tempo.

Tambem existem problemas de segurança, recuperação dos dados depois de falhas e dificuldade para realizar consultas e alterações mais complexas.

Por esses motivos os SGBDs sao utilizados para facilitar a organização, segurança, integridade e recuperação dos dados.

Q3. Propriedades ACID

Atomicidade

A atomicidade significa que uma operação deve acontecer por completo ou nao acontecer.

Em uma transferencia bancaria, primeiro o valor e retirado da conta de origem e depois colocado na conta de destino.

As duas operações devem acontecer juntas.

Se o SGBD nao garantir a atomicidade, pode acontecer de o dinheiro ser retirado da conta de origem mas nao chegar na conta de destino.

Consistencia

A consistencia significa que os dados devem continuar seguindo as regras definidas pelo banco de dados.

Em uma transferencia bancaria, o banco pode ter uma regra que impede que o saldo fique abaixo de um determinado limite.

Se uma transferencia fizer o saldo ficar abaixo desse limite, a operação deve ser recusada.

Se o SGBD nao garantir a consistencia, poderiam existir dados que nao seguem as regras do sistema.

Isolamento

O isolamento significa que operações realizadas ao mesmo tempo nao devem causar problemas umas nas outras.

Por exemplo, dois atendentes podem tentar realizar uma transferencia ou retirar dinheiro da mesma conta ao mesmo tempo.

O SGBD deve controlar essas operações para que o saldo final fique correto.

Se o SGBD nao garantir o isolamento, duas operações simultaneas poderiam usar o mesmo saldo e causar um valor incorreto.

Durabilidade

A durabilidade significa que depois que uma operação for confirmada, seus dados devem continuar armazenados mesmo que aconteça uma falha no sistema.

Em uma transferencia bancaria, depois que o banco confirmar a operação, o resultado deve continuar salvo mesmo se o servidor desligar logo depois.

Se o SGBD nao garantir a durabilidade, uma transferencia poderia ser confirmada e depois desaparecer quando o servidor fosse reiniciado.