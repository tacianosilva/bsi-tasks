---
name: spring-boot-backend
description: Use ao desenvolver projetos Spring Boot nas disciplinas de Banco de Dados e Engenharia de Software do BSI/UFRN.
---

# Spring Boot Backend

## Perfil

Stack Java para exemplos de backend, conexão com bancos de dados e
desenvolvimento de APIs reativas.

## Estrutura de projeto (Maven)

```
projeto/
├── pom.xml
├── src/
│   ├── main/
│   │   ├── java/br/ufrn/...
│   │   │   ├── domain/
│   │   │   ├── repository/
│   │   │   ├── service/
│   │   │   ├── controller/
│   │   │   └── Application.java
│   │   └── resources/
│   │       └── application.yml
│   └── test/
│       └── java/br/ufrn/...
```

## Padrões adotados

- **Build** com Maven (pom.xml)
- **ORM** com Spring Data JPA/Hibernate
- **Reativo** com Spring WebFlux + MongoDB
- **Testes** com JUnit 5 + Mockito
- **Configuração** via `application.yml`

## Referências no repositório

- `database/connections/java/spring-data-jpa/`
- `languages/java/webflux/`
- `languages/java/bsi-java/`

## Comandos frequentes

```bash
mvn spring-boot:run
mvn test
mvn clean package
```
