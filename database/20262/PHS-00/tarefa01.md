# Tarefa 01 - Conceitos de BD - PHS-00

## Q1. Banco de Dados e SGBD

Um Banco de Dados é um conjunto de dados organizados de uma forma que facilite o armazenamento, a consulta e a alteração dessas informações. Ele pode guardar, por exemplo, dados de clientes, produtos, funcionários, vendas, entre outros.

Já o SGBD (Sistema Gerenciador de Banco de Dados) é o software responsável por gerenciar o banco de dados. Ele permite criar tabelas, inserir e consultar dados, além de controlar segurança, integridade, concorrência e recuperação das informações.

Alguns exemplos de bancos de dados são:

* **MySQL** - utiliza o SGBD MySQL.
* **PostgreSQL** - utiliza o SGBD PostgreSQL.
* **Oracle Database** - utiliza o SGBD Oracle.
* **SQL Server** - utiliza o SGBD Microsoft SQL Server.
* **SQLite** - utiliza o SGBD SQLite.

Na prática, muitas vezes usamos o nome do próprio SGBD para falar do banco de dados, mas os dois conceitos não são exatamente a mesma coisa.

## Q2. Problemas dos Sistemas de Arquivos

Utilizar sistemas de arquivos para armazenar grandes quantidades de dados pode gerar vários problemas. Alguns deles são:

* **Redundância de dados:** a mesma informação pode acabar sendo armazenada várias vezes.
* **Inconsistência:** quando uma informação é alterada em um arquivo e não é alterada em outro, os dados ficam diferentes.
* **Dificuldade de acesso:** consultas mais complexas podem ser difíceis de realizar.
* **Problemas de segurança:** pode ser mais difícil controlar quem pode acessar ou modificar cada informação.
* **Falta de controle de concorrência:** dois usuários podem tentar alterar o mesmo dado ao mesmo tempo.
* **Dificuldade de recuperação:** se um arquivo for perdido ou corrompido, recuperar os dados pode ser complicado.
* **Pouca organização:** conforme a quantidade de informações aumenta, fica mais difícil manter os dados organizados.

Por causa desses problemas, os SGBDs foram criados para facilitar o gerenciamento e aumentar a confiabilidade dos dados.

## Q3. Propriedades ACID

As propriedades ACID são características importantes das transações realizadas em um banco de dados. ACID significa Atomicidade, Consistência, Isolamento e Durabilidade.

### Atomicidade

Atomicidade significa que uma transação deve ser realizada por completo ou não ser realizada. Não pode acontecer de apenas uma parte da operação ser concluída.

**Exemplo:** em uma transferência de R$ 100,00, o banco precisa retirar os R$ 100,00 da conta de origem e adicionar os R$ 100,00 na conta de destino.

Se o SGBD não garantisse atomicidade, poderia acontecer de o dinheiro ser retirado da primeira conta, mas não chegar na segunda.

### Consistência

Consistência significa que uma transação deve manter o banco de dados em um estado válido, respeitando as regras definidas.

**Exemplo:** se uma conta não pode ficar com saldo abaixo de -R$ 500,00, uma transferência que ultrapasse esse limite deve ser rejeitada.

Sem consistência, o banco poderia permitir operações que deixassem os dados em uma situação inválida.

### Isolamento

Isolamento significa que transações executadas ao mesmo tempo não devem causar problemas umas nas outras.

**Exemplo:** dois atendentes tentam realizar uma transferência usando o mesmo saldo ao mesmo tempo. O banco precisa controlar essas operações para que o saldo não seja utilizado de forma incorreta.

Sem isolamento, as duas operações poderiam ler o mesmo saldo antes de uma delas ser atualizada e acabar causando um saldo incorreto.

### Durabilidade

Durabilidade significa que, depois que uma transação é confirmada, seus dados devem continuar armazenados mesmo que ocorra uma falha no sistema.

**Exemplo:** depois que uma transferência é confirmada, o resultado precisa continuar registrado mesmo que o servidor seja desligado logo depois.

Sem durabilidade, uma transferência poderia aparecer como concluída e depois desaparecer quando o servidor fosse reiniciado.