# Relatório Técnico: Persistência de Dados (Tarefa 02)

Este documento detalha as implementações dos módulos JDBC e ORM, cumprindo os requisitos teóricos e práticos da disciplina.

## 📎 Links para os Arquivos do Projeto

### Configurações e Scripts
* [Script SQL de Inicialização (01-init.sql)](./init-db/01_init.sql)
* [Configuração Docker Compose](./docker-compose.yml)
* [Arquivo de Configuração Spring (YAML)](./orm/src/main/resources/application.yaml)

### Módulo JDBC (Nativo)
* [Classe Principal JDBC](./jdbc/src/main/java/br/ufrn/dct/Main.java)

### Módulo ORM (Spring Data JPA)
* **Entidades (Model):**
  * [Projeto.java](./orm/src/main/java/br/ufrn/dct/model/Projeto.java)
  * [Atividade.java](./orm/src/main/java/br/ufrn/dct/model/Atividade.java)
  * [Funcionario.java](./orm/src/main/java/br/ufrn/dct/model/Funcionario.java)
  * [Departamento.java](./orm/src/main/java/br/ufrn/dct/model/Departamento.java)
* **Serviços (Business Logic):**
  * [TarefaService (Coordenador)](./orm/src/main/java/br/ufrn/dct/service/TarefaService.java)
  * [ProjetoService](./orm/src/main/java/br/ufrn/dct/service/ProjetoService.java)
* **Repositórios:**
  * [ProjetoRepository.java](./orm/src/main/java/br/ufrn/dct/repository/ProjetoRepository.java)
* **Ponto de Entrada:**
  * [Main ORM Spring Boot](./orm/src/main/java/br/ufrn/dct/Main.java)

---

## 📚 Fundamentação Teórica

### Resumo sobre ODBC em Java
O **ODBC (Open Database Connectivity)** é um padrão de interface para acesso a bancos de dados. No ecossistema Java, utilizava-se a ponte JDBC-ODBC para permitir que o Java conversasse com drivers ODBC nativos do sistema operacional.
* **Situação Atual:** Essa ponte foi descontinuada a partir do Java 8. Hoje, a prática recomendada é o uso de drivers JDBC nativos (Tipo 4), que são escritos 100% em Java, oferecendo maior segurança, performance e eliminando dependências de software externo ao ambiente Java.

### Resumo sobre ORM e Framework Utilizado
O **ORM (Object-Relational Mapping)** é uma técnica que permite mapear as tabelas de um banco de dados relacional para classes e objetos em uma linguagem orientada a objetos. Isso elimina a necessidade de escrever SQL manualmente para operações básicas de CRUD.

**Framework Utilizado:** Neste projeto, utilizamos o **Spring Data JPA** com o **Hibernate**.
* O **Spring Data JPA** simplifica a criação de repositórios através de interfaces.
* O **Hibernate** atua como o motor de persistência, convertendo as entidades Java em comandos SQL compatíveis com o PostgreSQL e gerenciando as transações de forma automatizada.

---

## 📊 Análise Comparativa (Questão 7)

| Característica | JDBC Nativo | ORM (Spring Data JPA) |
| :--- | :--- | :--- |
| **Complexidade** | Alta: Escrita de SQL manual e manipulação de ResultSet. | Baixa: Manipulação de objetos e métodos de interface. |
| **Manutenção** | Difícil: SQL hardcoded exige refatoração constante. | Simples: Alterações nas classes refletem no banco. |
| **Performance** | Alta: Sem camadas de abstração adicionais. | Excelente: Otimizado por cache e controle de transações. |

---
**Desenvolvedor:** Kaique Vieira Soares | **Instituição:** UFRN | **Ano:** 2026
