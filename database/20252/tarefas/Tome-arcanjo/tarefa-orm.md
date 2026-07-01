# Links do Projeto

## 📌 Código
https://github.com/Tome-arcanjo/bdwork/blob/main/crud.js

## 📌 Scripts SQL
https://github.com/tacianosilva/bsi-tasks/tree/main/database/scripts/AtividadesBD/postgres



# Resumo de Tecnologias de Banco de Dados

## ODBC (Open Database Connectivity)

O ODBC é um padrão de interface (API) que permite que aplicações acessem diferentes sistemas de gerenciamento de banco de dados (SGBDs) de forma uniforme.

**Funcionamento:**  
Atua como uma camada intermediária; a aplicação se comunica com a API ODBC, que utiliza um driver específico para traduzir as requisições para o banco de dados (PostgreSQL, SQL Server, etc).

**Contexto Node.js:**  
Em JavaScript, é comumente utilizado via pacotes como `node-odbc` para conectar a bancos legados onde drivers nativos não estão disponíveis.

---

## ORM (Object-Relational Mapping)

O ORM é uma técnica de desenvolvimento que permite mapear tabelas de um banco de dados relacional para objetos em uma linguagem de programação. O objetivo é reduzir a escrita de SQL manual, tratando registros como instâncias de classes.

---

## Framework Utilizado: Prisma

O Prisma é o ORM moderno escolhido para Node.js, com foco em produtividade e segurança de tipos.

- **Schema.prisma:**  
  Utiliza um arquivo centralizado para definir modelos e conexões.

- **Introspecção:**  
  Permite ler um banco de dados já existente e gerar automaticamente os modelos de código (utilizado neste projeto via `db pull`).

- **Prisma Client:**  
  Gera uma interface de consulta que facilita operações de CRUD e o gerenciamento de relações complexas (como chaves estrangeiras entre `projeto`, `atividade` e `funcionario`).

# Docker Compose

## 📌 Arquivo
https://github.com/Tome-arcanjo/bdwork/blob/main/docker-compose.yml

  
