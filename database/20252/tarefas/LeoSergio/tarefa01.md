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

---

## 4. (7c) Três elementos básicos de um Modelo Entidade-Relacionamento (MER)
1. **Entidades:** objetos do mundo real que têm existência independente (ex.: EMPREGADO, TURNO).  
2. **Atributos:** propriedades que descrevem entidades (ex.: nome, e-mail, código).  
3. **Relacionamentos:** associações entre entidades, que podem ter cardinalidades e eventual atributos próprios (ex.: EMPREGADO — bate — PONTO).

---

---

## 5. (7d) Notações para Diagramas ER (exemplos)
Existem várias notações para representar conceitos ER:
- **Chen (1976):** entidades como retângulos, relacionamentos como losangos; cardinalidade por 1:N, M:N etc.  
- **Crow's Foot (IE / Barker):** usa “pés-de-corvo” para indicar “muitos” e barras para “um”. Muito popular em modelagem prática.  
- **UML (classe/objeto):** pode ser usada para modelar banco de dados com estereótipos.  
- **IDEF1X:** notação formal, com símbolos próprios para chaves e cardinalidade.  
Exemplo de variação para cardinalidade: Chen usa (0,1), (1, n) como texto; Crow's Foot desenha graficamente.

---

