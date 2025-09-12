# Tarefa 01 - Conceitos BD e MER de Leandro Sérgio

**Nome:** Leandro Sérgio da Silva  
**GitHub:** [LeoSergio](https://github.com/LeoSergio)  
**E-mail:** leosergio.583@gmail.com


---

## 1. Introdução / Objetivo
Este documento contém as respostas da Tarefa 01 — Conceitos de Banco de Dados e Modelo Entidade-Relacionamento (MER), conforme o enunciado da disciplina. (Commit e histórico vinculados à issue #<149>).

---

## 2. (7a) O que é um Banco de Dados e o que é um Sistema Gerenciador de Banco de Dados (SGBD)
**Banco de Dados (BD):** um conjunto organizado de dados relacionados, projetado para armazenar, recuperar e gerenciar informações de forma eficiente e consistente.  
**SGBD:** software que permite criar, manipular e gerenciar bancos de dados — fornecendo mecanismos para consultas (SQL), controle de concorrência, segurança, integridade, recuperação e backup.  
**Exemplos de BD e SGBDs:**  
- BD relacional: dados tabulares — SGBDs: MySQL, PostgreSQL, MariaDB, Oracle DB, Microsoft SQL Server.  
- BD NoSQL: MongoDB (documento), Cassandra (colunar), Redis (chave-valor).

---

---

## 3. (7b) Principais problemas de utilizar sistemas de arquivos para armazenar dados
- **Redundância e inconsistência:** dados duplicados em vários arquivos podem divergir.  
- **Dificuldade em consultas complexas:** sem linguagem padronizada (SQL) as consultas e junções são mais difíceis.  
- **Falta de integridade e regras de negócio:** não há mecanismos automáticos para constraints (uniqueness, foreign keys, etc.).  
- **Controle de concorrência** e bloqueios: difícil de gerenciar acessos simultâneos.  
- **Segurança e auditoria limitadas.**  
- **Recuperação de falhas e backup** menos robustos que em SGBDs.

---
