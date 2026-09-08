# Tarefa 01 - Conceitos de BD, ACID e SGBD
**Q1.  Descreva o que é um Banco de Dados e o que é um Sistema Gerenciador de Banco de Dados. Cite exemplos de Bancos de Dados e seus SGBDs..**
Banco de Dados é uma coleção de dados relacionados e armazenados em algum dispostivio que permite consultar, armazenar e manipular informações. Exemplo: Banco de Dados de uma escola: Professores, Alunos, Turmas, Notas.

SGBD é um conjunto de dados associado a um conjunto de programas para acesso a esses dados. Ou seja, é o softare responsável por gerenciar o banco de dados. Alguns exemplos de SGBDs são MySQL, PostgreSQL, Oracle Database e SQL Server.

**Q2. Quais são os principais problemas da utilização de Sistemas de Arquivos para armazenamento de dados?**
Os principais problemas são:

* Inconsistência e redundância de dados
* Dificuldade de acesso aos dados
* Isolamento de dados
* Problemas de integridade
* Problemas de segurança

**Q3. Explique as propriedades ACID: atomicidade, consistência, isolamento e durabilidade. Para cada propriedade, descreva um exemplo prático no contexto de uma transferência bancária e explique o que aconteceria se o SGBD não garantisse essa propriedade.**  
* Atomicidade significa que uma transação deve ser finalizada completamente ou não ser realizada; 
* Consistência significa que o banco de dados deve permanecer em um estado válido após uma transação;
* Isolamento significa que transações executadas simultaneamente não devem interferir de maneira incorreta umas nas outras;
* Durabilidade significa que, após uma transação ser confirmada, seus dados
devem permanecer armazenados mesmo após uma falha do sistema.



