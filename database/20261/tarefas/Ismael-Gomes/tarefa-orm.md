# Respostas: Tarefa - ODBC e ORM

## 1. Issue e Diretório
* **Link para a Issue:** https://github.com/Ismael-Gomes/bsi-tasks/issues/1
* Os arquivos de resposta foram alocados no diretório `database/20261/tarefas/Ismael-Gomes`.

## 2. Links para os Códigos e Scripts desenvolvidos
* **[Scripts DDL/DML e Docker (Infraestrutura)](./infraestrutura)**
* **[Projeto Questão 4 e 5: Conexão Nativa ODBC/JDBC](./parte1-jdbc)**
* **[Projeto Questão 6: Framework ORM (Spring Boot)](./parte2-orm)**

## 3. Resumo sobre ODBC (usando Java/JDBC)
Na linguagem Java, o equivalente direto ao ODBC é o **JDBC (Java Database Connectivity)**. É uma API nativa que permite conectar a aplicação ao banco de dados utilizando um driver específico do SGBD (no nosso caso, o driver do PostgreSQL).
Com o JDBC, o desenvolvedor escreve comandos SQL puros diretamente no código Java, gerenciando manualmente a abertura da conexão, a preparação do comando (`PreparedStatement`), a execução e a leitura dos resultados (`ResultSet`). Embora exija mais escrita de código (boilerplate), oferece um controle de baixo nível muito preciso sobre o banco.

## 4. Resumo sobre ORM (usando Spring Data JPA / Hibernate)
O **ORM (Object-Relational Mapping)** resolve a diferença entre o modelo de banco de dados relacional (tabelas) e o modelo da programação orientada a objetos (classes e atributos).
Nesta tarefa, foi utilizado o framework **Spring Data JPA** com o **Hibernate** (no ecossistema Spring Boot). Com ele, as tabelas foram mapeadas para classes Java usando anotações (como `@Entity` e `@OneToMany`). Em vez de escrever comandos SQL (INSERT, UPDATE) manualmente, as operações no banco são feitas manipulando os objetos Java e chamando métodos prontos de interfaces `Repository` (ex: `repository.save()`). O framework traduz isso para SQL automaticamente, aumentando a produtividade e a segurança do código.

## 5. Resumo das Operações Realizadas (Comandos Executados)
Tanto no projeto JDBC quanto no projeto ORM, o banco de dados `AtividadesBD` foi instanciado via Docker e as três operações exigidas foram executadas com sucesso:
1. **Inserção de Atividade:** Nova atividade vinculada a um projeto existente.
2. **Atualização de Líder:** Alteração do ID do funcionário responsável por um projeto.
3. **Listagem:** Retorno e impressão no console de todos os projetos e suas respectivas atividades (através de um `LEFT JOIN` no JDBC e mapeamento de lista no ORM).
