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
