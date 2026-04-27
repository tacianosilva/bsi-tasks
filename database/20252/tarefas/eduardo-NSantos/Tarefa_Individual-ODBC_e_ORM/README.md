# Projeto de Banco de Dados – Tarefa 02 (ODBC e ORM)

* **Nome:** Eduardo Nascimento Santos
* **Matrícula:** 20240043387
* **Email:** [eduardo.santos.135@ufrn.edu.br](mailto:eduardo.santos.135@ufrn.edu.br)
* [tarefa-orm.md](tarefa-orm.md)

---

## Descrição

Este projeto tem como objetivo demonstrar o acesso a banco de dados utilizando duas abordagens:

* JDBC (acesso direto com SQL)
* ORM com JPA (mapeamento objeto-relacional)

Diferente de um sistema real, este projeto **não possui interface nem entrada de dados dinâmica**.
As operações exigidas na atividade (inserção, atualização e consulta) são **executadas automaticamente ao iniciar a aplicação**, apenas para demonstrar o funcionamento e cumprir os requisitos da tarefa.

---

## Pré-requisitos

* Docker e Docker Compose instalados
* Java 21
* Maven

---

## Subindo o banco de dados

Na pasta onde está o `docker-compose.yml`, execute:

```bash
docker-compose up
```

### Possível problema

Se ocorrer erro relacionado à porta:

```text
address already in use
```

Significa que a porta **5432** já está sendo usada (geralmente por outro PostgreSQL).

Soluções:

* Parar o serviço que está usando a porta 5432
  ou
* Alterar a porta no `docker-compose.yml` (ex: `5433:5432`) Obs: Cuidado com essa abordagem, pois os programas jdbc e orm estão configuradas para localhost:5432

---

## Executando o projeto JDBC

Acesse a pasta do projeto JDBC e execute:

```bash
mvn spring-boot:run
```

O programa irá automaticamente:

* Inserir uma atividade
* Atualizar o responsável de um projeto
* Listar projetos e suas atividades

---

## Executando o projeto ORM

Acesse a pasta do projeto ORM e execute:

```bash
mvn spring-boot:run
```

O programa irá executar automaticamente as mesmas operações, porém utilizando JPA (ORM):

* Inserção via entidade
* Atualização via repositório
* Consulta utilizando relacionamento entre entidades

---

## Observação

As queries e operações foram implementadas de forma automática apenas para fins de demonstração, conforme solicitado na atividade.
Não há necessidade de interação manual com o sistema para validar os resultados.
