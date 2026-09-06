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