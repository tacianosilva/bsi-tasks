# Resposta da Tarefa 1 — Banco de Dados (2026.2)
*Aluno: Paulo André Alves de Moura*

## Q1. Descreva o que é um Banco de Dados e o que é um Sistema Gerenciador de Banco de Dados. Cite exemplos de Bancos de Dados e seus SGBDs.

**Banco de Dados (BD):** É uma coleção organizada de dados logicamente relacionados, projetada para armazenar, gerenciar e recuperar informações de maneira eficiente. O banco de dados em si é o repositório onde os dados físicos residem (os arquivos estruturados no disco).

**Sistema Gerenciador de Banco de Dados (SGBD):** É o software complexo que atua como interface entre os usuários, as aplicações e o banco de dados propriamente dito. O SGBD é responsável por criar, ler, atualizar e apagar (CRUD) os dados, além de garantir segurança, controle de concorrência e integridade das informações.

**Exemplos:**
*   **SGBDs (O software):** PostgreSQL, MySQL, Oracle Database, Microsoft SQL Server, MongoDB (NoSQL).
*   **Bancos de Dados (O repositório gerado):** O banco de dados de alunos do SIGAA na UFRN, o banco de dados do catálogo de produtos de um e-commerce, o banco de dados de transações de um aplicativo bancário.

## Q2. Quais os principais problemas de utilizar Sistemas de Arquivos para armazenagem de dados?

Antes dos SGBDs, os dados eram frequentemente armazenados em sistemas de arquivos tradicionais do sistema operacional. Isso gera diversos problemas:

1.  **Redundância e Inconsistência de Dados:** O mesmo dado pode ser armazenado em vários arquivos diferentes (ex: o endereço de um cliente no arquivo de cobrança e no arquivo de entregas). Se o endereço mudar, é necessário atualizar em todos os locais. Se um for esquecido, gera-se uma inconsistência.
2.  **Dificuldade no Acesso aos Dados:** Para cada nova consulta ou relatório não previsto, é necessário escrever um novo programa de computador para extrair os dados dos arquivos.
3.  **Isolamento de Dados:** Dados espalhados em vários arquivos com formatos diferentes (CSV, TXT, binários) dificultam o cruzamento de informações.
4.  **Problemas de Integridade:** É complexo garantir que regras de negócio sejam cumpridas (ex: garantir que um saldo não fique negativo) sem ter que espalhar essas validações pelo código de todas as aplicações que acessam o arquivo.
5.  **Anomalias de Acesso Concorrente:** Se dois usuários tentam editar o mesmo arquivo simultaneamente, o sistema operacional pode bloquear o arquivo para um deles ou as edições de um usuário podem sobrescrever as do outro.
6.  **Problemas de Segurança:** Dificuldade em conceder permissões granulares.

