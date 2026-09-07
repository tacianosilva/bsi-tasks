# Tarefa 01 - Conceitos de BD, ACID e SGBD

## Q1. Banco de Dados e SGBD

Um **Banco de Dados (BD)** é uma coleção organizada de dados relacionados, armazenados de forma que possam ser consultados, alterados e utilizados por diferentes aplicações. Ele permite representar informações de um determinado domínio, como clientes, produtos, contas bancárias ou alunos.

Um **Sistema Gerenciador de Banco de Dados (SGBD)** é o software responsável por criar, armazenar, organizar, consultar, alterar e controlar o acesso aos dados de um banco de dados. Além disso, o SGBD oferece mecanismos para garantir segurança, integridade, controle de concorrência, recuperação de dados e gerenciamento de transações.

### Exemplos

| Banco de Dados | SGBD |
|---|---|
| Banco de dados de uma loja virtual | PostgreSQL |
| Banco de dados de um sistema bancário | Oracle Database |
| Banco de dados de uma aplicação web | MySQL |
| Banco de dados de uma aplicação corporativa | Microsoft SQL Server |
| Banco de dados de uma aplicação que necessita de documentos flexíveis | MongoDB |

A principal diferença entre os dois conceitos: o **banco de dados corresponde aos dados armazenados e organizados**, enquanto o **SGBD é o software utilizado para gerenciar esses dados**.


## Q2. Problemas dos Sistemas de Arquivos

A utilização de sistemas de arquivos para armazenar dados pode causar diversos problemas, principalmente quando a quantidade de informações e de usuários aumenta.

Os principais problemas são:

- **Redundância de dados:** a mesma informação pode ser armazenada várias vezes em arquivos diferentes.
- **Inconsistência:** quando uma informação duplicada é alterada em um arquivo, mas não em outro, os dados podem ficar diferentes.
- **Dificuldade de compartilhamento:** vários sistemas podem ter dificuldade para acessar e utilizar os mesmos dados de forma organizada.
- **Problemas de segurança:** o controle de acesso aos arquivos pode ser limitado ou difícil de administrar.
- **Dificuldade de controle de concorrência:** dois usuários podem tentar alterar o mesmo dado simultaneamente e causar conflitos.
- **Dificuldade de recuperação:** em caso de falhas, pode ser difícil recuperar os dados para um estado consistente.
- **Dependência entre programas e dados:** alterações na estrutura dos arquivos podem exigir alterações nos programas que os utilizam.
- **Dificuldade de garantir integridade:** torna-se mais difícil garantir que os dados sigam determinadas regras e restrições.


## Q3. Propriedades ACID

As propriedades **ACID** são características que garantem maior confiabilidade às transações realizadas em um banco de dados. ACID significa **Atomicidade, Consistência, Isolamento e Durabilidade**.

### Atomicidade

Atomicidade significa que uma transação deve ser tratada como uma operação única: ela é realizada completamente ou não é realizada.

Em uma transferência bancária, suponha que uma pessoa transfira R$ 500,00 da conta A para a conta B. A operação envolve duas ações:

1. Retirar R$ 500,00 da conta A.
2. Adicionar R$ 500,00 na conta B.

As duas operações devem ocorrer juntas.

Se o SGBD não garantisse atomicidade e ocorresse uma falha depois do débito, mas antes do crédito, o dinheiro poderia ser retirado da conta A sem aparecer na conta B.

### Consistência

Consistência significa que uma transação deve levar o banco de dados de um estado válido para outro estado válido, respeitando as regras e restrições definidas.

Por exemplo, se uma conta não pode ficar com saldo negativo, uma transferência não deve permitir que o saldo da conta de origem fique abaixo desse limite.

Se a consistência não fosse garantida, uma transferência poderia deixar a conta com um saldo inválido, violando as regras estabelecidas pelo banco.

### Isolamento

Isolamento significa que transações executadas simultaneamente não devem interferir de maneira incorreta umas nas outras. O resultado deve ser equivalente a uma execução controlada das operações.

Por exemplo, imagine que duas transferências sejam realizadas simultaneamente usando o mesmo saldo. O SGBD deve controlar essas operações para que as duas transações não utilizem incorretamente o mesmo saldo disponível.

Sem isolamento, duas operações poderiam ler o mesmo saldo antes que uma delas fosse efetivada, causando um resultado incorreto.

### Durabilidade

Durabilidade significa que, depois que uma transação é confirmada, seus efeitos devem permanecer armazenados mesmo que ocorra uma falha posteriormente.

Por exemplo, depois que uma transferência bancária é confirmada, o débito e o crédito devem continuar registrados mesmo se ocorrer uma queda de energia ou o servidor precisar ser reiniciado.

Sem durabilidade, uma operação poderia ser confirmada para o usuário e posteriormente desaparecer, fazendo com que o banco retornasse a um estado anterior.

