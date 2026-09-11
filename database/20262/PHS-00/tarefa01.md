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