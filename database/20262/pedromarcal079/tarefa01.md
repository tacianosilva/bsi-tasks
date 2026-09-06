# Q1 - Descreva o que é um Banco de Dados e o que é um Sistema Gerenciador de Banco de Dados. Cite exemplos de Bancos de Dados e seus SGBDs.

Um banco de dados é um armazém de informações, dados organizados e estruturados. Esses dados são logicamente relacionados, armazenados de forma persistente para representar aspectos do mundo real e atender a diferentes aplicações. Um Sistema de Gerenciamento de Banco de Dados (SGBD) é o software intermediário responsável por criar, consultar, atualizar e administrar essa base, garantindo segurança, controle de concorrência e integridade das informações

Como exemplos práticos, em um sistema bancário o banco de dados é a coleção de tabelas com dados de contas, clientes e transações, gerenciada por um SGBD como o PostgreSQL ou o Oracle Database. Em um aplicativo de streaming, o banco de dados com catálogos de músicas e perfis de usuários pode ser gerenciado por um SGBD NoSQL como o MongoDB.

---

# Q2 - Quais os principais problemas de utilizar Sistemas de Arquivos para armazenagem de dados?

O uso de sistemas de arquivos convencionais para gerenciar dados corporativos gera redundância e inconsistência, pois o mesmo dado costuma ser replicado em arquivos distintos com formatos diferentes, dificultando atualizações sincronizadas. Além disso, há forte dependência entre dados e programas, exigindo reescrever aplicações inteiras a cada alteração na estrutura do arquivo.

Outros problemas críticos envolvem a dificuldade de acesso e isolamento dos dados, exigindo a criação contínua de novos programas para consultas simples, além da falta de controle de concorrência, que causa perda de dados em acessos simultâneos. Sistemas de arquivos também não garantem atomicidade em caso de falhas durante transações e possuem mecanismos frágeis de segurança e integridade.

---