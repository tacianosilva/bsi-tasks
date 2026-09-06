# Q1 - Descreva o que é um Banco de Dados e o que é um Sistema Gerenciador de Banco de Dados. Cite exemplos de Bancos de Dados e seus SGBDs.

Um banco de dados é um armazém de informações, dados organizados e estruturados. Esses dados são logicamente relacionados, armazenados de forma persistente para representar aspectos do mundo real e atender a diferentes aplicações. Um Sistema de Gerenciamento de Banco de Dados (SGBD) é o software intermediário responsável por criar, consultar, atualizar e administrar essa base, garantindo segurança, controle de concorrência e integridade das informações

Como exemplos práticos, em um sistema bancário o banco de dados é a coleção de tabelas com dados de contas, clientes e transações, gerenciada por um SGBD como o PostgreSQL ou o Oracle Database. Em um aplicativo de streaming, o banco de dados com catálogos de músicas e perfis de usuários pode ser gerenciado por um SGBD NoSQL como o MongoDB.

---

# Q2 - Quais os principais problemas de utilizar Sistemas de Arquivos para armazenagem de dados?

O uso de sistemas de arquivos convencionais para gerenciar dados corporativos gera redundância e inconsistência, pois o mesmo dado costuma ser replicado em arquivos distintos com formatos diferentes, dificultando atualizações sincronizadas. Além disso, há forte dependência entre dados e programas, exigindo reescrever aplicações inteiras a cada alteração na estrutura do arquivo.

Outros problemas críticos envolvem a dificuldade de acesso e isolamento dos dados, exigindo a criação contínua de novos programas para consultas simples, além da falta de controle de concorrência, que causa perda de dados em acessos simultâneos. Sistemas de arquivos também não garantem atomicidade em caso de falhas durante transações e possuem mecanismos frágeis de segurança e integridade.

---

# Q3 - Explique as propriedades ACID: atomicidade, consistência, isolamento e durabilidade. Para cada propriedade, descreva um exemplo prático no contexto de uma transferência bancária e explique o que aconteceria se o SGBD não garantisse essa propriedade.

A **Atomicidade** garante que todas as etapas de uma transação sejam executadas com sucesso ou nenhuma seja aplicada (tudo ou nada). Por exemlo, um PIX de uma conta A para uma conta B, se o SGBD falhar nessa garantia e o sistema travar no meio da operação, o dinheiro sumiria: a conta A teria o valor descontado, mas a conta B jamais o receberia.

A **Consistência** assegura que a transação leve o banco de um estado válido a outro, respeitando regras de negócio e restrições de integridade, como saldo não negativo por exemplo. Se uma regra proíbe saldo negativo e o cliente tenta transferir mais do que possui, a transação deve ser abortada. Sem essa garantia, o banco permitiria saldos inválidos e violações nas regras de negócio financeiras.

O **Isolamento** dita que transações concorrentes ocorram sem interferir umas nas outras, como se fossem executadas em sequência. Se a conta A tem R$ 100 e duas transferências de R$ 100 tentam debitar ao mesmo tempo, o isolamento impede que ambas leiam o saldo antigo simultaneamente. Sem isso, ocorreria leitura suja ou perda de atualização, permitindo que R$ 200 fossem sacados de um saldo de R$ 100.

A **Durabilidade** certifica que, após a confirmação da transferência, as mudanças persistam de forma definitiva no banco, mesmo diante de falhas de energia ou quedas do servidor. Se o SGBD não garantisse essa persistência, o cliente veria a transferência confirmada na tela, mas um reinício repentino do servidor apagaria o registro, desfazendo o crédito já validado.

---