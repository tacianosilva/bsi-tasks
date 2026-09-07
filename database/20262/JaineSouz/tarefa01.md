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
