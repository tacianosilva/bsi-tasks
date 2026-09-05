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

Q4. Propriedades ACID nos cenarios

a - Queda de energia no meio de uma transferencia deixou o valor debitado da conta de origem, mas nao creditado na conta de destino.

A propriedade envolvida e a atomicidade.

Isso acontece porque a transferencia deveria ser realizada por completo ou nao ser realizada.

Nesse caso apenas uma parte da operação aconteceu.

b - Dois atendentes debitam, ao mesmo tempo, o mesmo saldo de uma conta.

A propriedade envolvida e o isolamento.

Isso acontece porque existem duas operações acontecendo ao mesmo tempo e o SGBD precisa controlar essas operações para evitar que o saldo fique incorreto.

c - O sistema confirma a operação, mas depois de reiniciar o servidor o dado foi perdido.

A propriedade envolvida e a durabilidade.

Depois que a operação foi confirmada, o dado deveria continuar armazenado mesmo depois de uma falha ou reinicialização do servidor.

d - Uma transferencia que levaria o saldo abaixo do limite permitido e rejeitada pelo banco.

A propriedade envolvida e a consistencia.

Isso acontece porque o banco precisa garantir que os dados continuem seguindo as regras definidas, nesse caso nao permitindo que o saldo fique abaixo do limite.

Q5. Recuperação, integridade, redundancia e inconsistencia

Recuperação

A recuperação e o processo de recuperar os dados depois de uma falha no sistema, como uma queda de energia ou problema no servidor.

O SGBD possui mecanismos que permitem recuperar os dados e deixar o banco em um estado correto depois de uma falha.

Integridade

A integridade significa manter os dados corretos e de acordo com as regras definidas no banco de dados.

O SGBD pode utilizar regras e restrições para evitar dados incorretos, como valores duplicados ou informações que nao podem ficar vazias.

Redundancia

A redundancia acontece quando a mesma informação e armazenada varias vezes sem necessidade.

O SGBD ajuda a diminuir esse problema organizando os dados de forma que uma mesma informação nao precise ser repetida em varios lugares.

Inconsistencia

A inconsistencia acontece quando existem informações diferentes para o mesmo dado.

Por exemplo, se o telefone de um cliente aparece como 9999-1111 em um lugar e 8888-2222 em outro.

O SGBD ajuda a evitar esse problema mantendo os dados organizados e controlando as alterações feitas nas informações.

Q6. Mini-projeto conceitual

A empresa de desenvolvimento de software possui clientes, projetos, squads, membros, tarefas, sprints e releases.

Entidades e atributos

Cliente

id

nome

CNPJ

email

telefone

Projeto

id

nome

descricao

data de inicio

data de fim

status

Squad

id

nome

Membro

id

nome

email

cargo

Tarefa

id

titulo

descricao

status

prioridade

data de criacao

Sprint

id

nome

objetivo

data de inicio

data de fim

Release

id

versao

data

status

Relacionamentos

Um cliente pode possuir varios projetos.

Um projeto pertence a um cliente.

Um projeto pode possuir varias tarefas.

Uma tarefa deve estar vinculada a um projeto.

Um projeto pode possuir varias sprints.

Uma sprint pertence a um projeto.

Um projeto pode possuir varias releases.

Uma release pertence a um projeto.

Uma squad pode possuir varios membros.

Um membro pertence a uma squad.

Uma squad deve possuir apenas um lider tecnico.

Uma squad pode possuir varios desenvolvedores e testadores.

Uma squad pode possuir um supervisor e um gerente de produto.

Regras de integridade

Todo projeto deve estar vinculado a um cliente.

Toda tarefa deve estar vinculada a um projeto.

Toda sprint deve estar vinculada a um projeto.

Toda release deve estar vinculada a um projeto.

Cada membro deve estar vinculado a uma squad.

Uma squad deve possuir apenas um lider tecnico.

Os identificadores das entidades devem ser unicos.

Uma sprint deve possuir uma data de inicio anterior a data de fim.

Uma release deve estar vinculada a um projeto existente.
