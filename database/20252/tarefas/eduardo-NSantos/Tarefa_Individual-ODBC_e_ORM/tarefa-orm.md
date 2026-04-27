# Tarefa – ODBC e ORM

## Links dos Artefatos

* Scripts SQL:
   - [atualizar projeto](jdbc-app/src/main/resources/sql/atualizar_projeto.sql)
   - [inserir atividade](jdbc-app/src/main/resources/sql/inserir_atividade.sql)
   - [listar projetos](jdbc-app/src/main/resources/sql/listar_projetos.sql)
* Programa com [JDBC/ODBC](jdbc-app/src/main/java/br/com/app/jdbc_app/JdbcAppApplication.java)
* Programa com [ORM](orm_app/src/main/java/br/com/app/orm_app/OrmAppApplication.java)

---

## Resumo sobre ODBC/JDBC

ODBC (Open Database Connectivity) e JDBC (Java Database Connectivity) são APIs utilizadas para permitir que aplicações se conectem a bancos de dados relacionais.

Essas APIs possibilitam o envio de comandos SQL diretamente ao banco de dados, permitindo operações como inserção, atualização e consulta de dados. No caso do JDBC, utilizado em Java, a conexão é realizada por meio de um driver específico do banco de dados.

O uso de ODBC/JDBC exige que o desenvolvedor escreva explicitamente as instruções SQL, oferecendo maior controle sobre as operações, porém tornando o código mais detalhado.

---

## Resumo sobre ORM

ORM (Object-Relational Mapping) é uma técnica que permite mapear tabelas do banco de dados para objetos na aplicação.

Com ORM, o desenvolvedor interage com o banco utilizando objetos e métodos da linguagem de programação, enquanto o framework é responsável por traduzir essas operações para comandos SQL.

Framework utilizado: Spring Data JPA, com Hibernate como implementação do ORM.

O uso de ORM reduz a necessidade de escrever SQL manualmente, tornando o desenvolvimento mais produtivo e organizado.
