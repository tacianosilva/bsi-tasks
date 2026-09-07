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



## Q4. Cenários envolvendo ACID

### a) Queda de energia no meio de uma transferência deixou o valor debitado da conta de origem, mas não creditado na conta de destino.

A propriedade diretamente envolvida é a **atomicidade**.

A transferência deveria ser tratada como uma única transação. O débito e o crédito precisam ocorrer juntos. Se ocorrer uma falha no meio da operação, o SGBD deve desfazer o débito ou completar corretamente a transação, evitando que apenas uma parte seja efetivada.

Também existe relação com a **durabilidade**, pois o SGBD precisa manter corretamente o estado recuperado após a falha.

### b) Dois atendentes debitam, ao mesmo tempo, o mesmo saldo de uma conta.

A propriedade diretamente envolvida é o **isolamento**.

As duas transações estão acontecendo simultaneamente e precisam ser controladas para evitar que ambas utilizem o mesmo estado do saldo de maneira incorreta.

Sem isolamento, as duas operações poderiam ler o mesmo saldo e realizar débitos que ultrapassassem o valor realmente disponível.

### c) O sistema confirma a operação, mas após reiniciar o servidor o dado foi perdido.

A propriedade diretamente envolvida é a **durabilidade**.

Depois de uma transação ser confirmada, seus efeitos precisam permanecer armazenados mesmo depois de uma falha ou reinicialização do servidor.

Se o dado fosse perdido, a operação que havia sido confirmada deixaria de existir.

### d) Uma transferência que levaria o saldo abaixo do limite permitido é rejeitada pelo banco.

A propriedade diretamente envolvida é a **consistência**.

O banco possui uma regra que determina que o saldo não pode ficar abaixo de determinado limite. A transação deve respeitar essa regra.

Nesse caso, o SGBD deve impedir que uma operação inválida seja confirmada e, consequentemente, manter o banco de dados em um estado consistente.


## Q5. Recuperação, integridade, redundância e inconsistência

### Recuperação

Recuperação é a capacidade de restaurar o banco de dados para um estado correto depois de uma falha, como queda de energia, erro do sistema ou falha do servidor.

O SGBD pode utilizar mecanismos como logs de transações, backups e operações de recuperação para desfazer transações incompletas ou recuperar transações que foram confirmadas.

### Integridade

Integridade está relacionada à garantia de que os dados armazenados sejam válidos, corretos e respeitem as regras estabelecidas para o banco.

O SGBD pode utilizar restrições de integridade, como chaves primárias, chaves estrangeiras, valores obrigatórios e regras de domínio, para impedir dados inválidos.

### Redundância

Redundância ocorre quando a mesma informação é armazenada desnecessariamente em vários lugares.

O SGBD pode reduzir a redundância por meio da organização adequada dos dados e da modelagem do banco, evitando que a mesma informação precise ser repetida em diversas estruturas.

### Inconsistência

Inconsistência ocorre quando existem informações conflitantes ou incorretas no banco de dados.

Por exemplo, se o endereço de um cliente estiver atualizado em um local, mas continuar antigo em outro, os dados estarão inconsistentes.

O SGBD ajuda a evitar inconsistências por meio de restrições de integridade, controle de transações e controle de concorrência.
