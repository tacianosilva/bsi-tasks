# Tarefa 01 - Conceitos de BD, ACID e SGBD

**Aluno (GitHub):** GabrielUchoa17
**Disciplina:** Banco de Dados - BSI
**Issue relacionada:** #393

---

## Sobre o fluxo de trabalho com Git e GitHub

Antes das respostas, um resumo dos conceitos de versionamento usados nesta entrega.

### Branches (ramos)

Uma **branch** é uma linha independente de desenvolvimento dentro do repositório. Ela
funciona como um ponteiro móvel para um commit; a cada novo commit na branch, o ponteiro
avança. A branch `main` guarda a versão estável do projeto, enquanto branches de
funcionalidade (ex.: `tarefa01/GabrielUchoa17`) isolam um trabalho em andamento sem afetar
a `main`. Isso permite desenvolver, revisar e testar mudanças de forma segura e paralela.

### Pull Request / Merge Request

O **Pull Request** (nome usado no GitHub) ou **Merge Request** (GitLab) é o pedido formal
para incorporar as mudanças de uma branch em outra (tipicamente da *feature branch* para a
`main`). Ele abre espaço para **revisão de código**, discussão, execução de CI/testes
automatizados e registro histórico da decisão. No fluxo com *fork*, o PR parte da branch do
fork do aluno e tem como destino a branch `main` do repositório oficial.

### Merge

O **merge** combina o histórico de duas branches. No *fast-forward*, quando a branch de
destino não avançou, o ponteiro apenas "anda para a frente". Quando as duas branches
divergiram, o Git cria um **commit de merge** com dois pais, preservando o histórico
original de ambas as linhas.

### Rebase

O **rebase** reaplica os commits da sua branch a partir da ponta atual de outra branch,
reescrevendo o histórico e deixando-o linear (sem commit de merge). É útil para atualizar a
feature branch com a `main` mantendo o log limpo. Regra prática: **não fazer rebase de
commits já publicados/compartilhados**, pois isso reescreve os hashes e quebra o histórico
de quem já baixou.

### Conflitos

Um **conflito** ocorre quando o merge ou o rebase encontram alterações incompatíveis na
mesma região de um arquivo (ou arquivo removido de um lado e editado do outro). O Git marca
o trecho com `<<<<<<<`, `=======` e `>>>>>>>`; o desenvolvedor precisa editar o arquivo
escolhendo/combinando as versões, remover os marcadores, dar `git add` no arquivo
resolvido e concluir com `git commit` (merge) ou `git rebase --continue` (rebase).

---

## Q1. Banco de Dados e Sistema Gerenciador de Banco de Dados

**Banco de Dados (BD)** é uma coleção organizada de dados relacionados entre si, que
representam aspectos do mundo real (o *minimundo*) e são armazenados de forma persistente
para atender a um conjunto de aplicações e usuários. Um BD tem um propósito definido, é
estruturado segundo um modelo de dados e busca reduzir redundância e inconsistência.

**Sistema Gerenciador de Banco de Dados (SGBD)** é o software que fica entre os usuários/
aplicações e os dados físicos, permitindo **definir** (esquemas, tipos, restrições),
**construir** (armazenar), **manipular** (consultar, inserir, atualizar, remover) e
**compartilhar** o banco de dados de forma controlada. O SGBD também cuida de segurança,
controle de concorrência, controle de acesso, backup e recuperação, e garante as
propriedades das transações.

De forma resumida: o **banco de dados** é o *conjunto de dados*; o **SGBD** é o *programa
que gerencia* esse conjunto. O conjunto formado por SGBD + banco(s) de dados + aplicações
costuma ser chamado de **Sistema de Banco de Dados**.

### Exemplos

| Banco de dados (o dado em si) | SGBD que o gerencia | Modelo |
|---|---|---|
| Cadastro acadêmico de uma universidade | PostgreSQL, Oracle Database, MySQL/MariaDB, SQL Server | Relacional |
| Catálogo de produtos e pedidos de um e-commerce | PostgreSQL, MySQL | Relacional |
| Coleção de documentos JSON de um app mobile | MongoDB, Couchbase | Documentos (NoSQL) |
| Carrinho de compras / cache de sessão | Redis | Chave-valor (NoSQL) |
| Rede de relacionamentos / recomendação | Neo4j | Grafos (NoSQL) |
| Métricas e séries temporais de sensores IoT | InfluxDB, TimescaleDB | Séries temporais |
| Banco local embarcado em um aplicativo desktop/mobile | SQLite | Relacional embarcado |

> Observação: nomes como "PostgreSQL", "MySQL" e "Oracle" designam, a rigor, os **SGBDs**;
> o *banco de dados* é a base específica que cada organização cria e povoa dentro deles
> (ex.: o banco `siga_ufrn` rodando sobre o SGBD PostgreSQL).

---
