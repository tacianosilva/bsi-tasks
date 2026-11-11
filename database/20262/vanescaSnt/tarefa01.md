**Tarefa 01 \- Conceitos de BD, ACID e SGBD**

**Q1.** Descreva o que é um Banco de Dados e o que é um Sistema Gerenciador de Banco de Dados. Cite exemplos de Bancos de Dados e seus SGBDs.

Um Banco de Dados é um conjunto organizado de dados relacionados entre si, armazenados de forma estruturada para representar informações de um contexto do mundo real, como os alunos e as notas de uma universidade ou os produtos e as vendas de uma loja. Já o Sistema Gerenciador de Banco de Dados é o software responsável por criar, manter e controlar o acesso ao banco de dados. Ele fica entre os usuários e os dados, armazenando e recuperando as informações com eficiência, permitindo consultas por meio de uma linguagem como o SQL.
Alguns exemplos dos bancos mais conhecidos de SGBD são MySQL, PostgreSQL, Oracle Database e SQL Server.

**Q2.** Quais os principais problemas de utilizar Sistemas de Arquivos para armazenagem de dados?

Nos sistemas de arquivos, cada aplicação guarda e manipula seus próprios arquivos, o que gera vários problemas. O principal é a redundância e inconsistência, já que a mesma informação fica repetida em vários arquivos e pode ser atualizada em um e esquecida em outro. Há também a dependência entre programas e dados, já que o formato do arquivo está embutido no código e qualquer mudança obriga a alterar todos os programas, além da dificuldade de acesso, pois cada nova consulta exige um programa específico, sem uma linguagem como o SQL.

