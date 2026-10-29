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

# Q4 - Para cada cenário abaixo, indique qual(is) propriedade(s) ACID está(ão) em jogo e justifique sua resposta: 

## a) Queda de energia no meio de uma transferência deixou o valor debitado da conta de origem, mas não creditado na conta de destino. 

Atomicidade. A transferência bancária é uma transação indivisível composta por débito e crédito; ao falhar no meio do caminho, o SGBD deveria ter desfeito o débito para manter o princípio do "tudo ou nada".

## b) Dois atendentes debitam, ao mesmo tempo, o mesmo saldo de uma conta. 

Isolamento. O cenário envolve concorrência entre duas transações simultâneas sobre o mesmo recurso; o SGBD deve isolar as execuções para que uma não sobrescreva ou tome decisões com base no estado não finalizado da outra (evitando perda de atualização).

## c) O sistema confirma a operação, mas após reiniciar o servidor o dado foi perdido. 

Durabilidade. Uma vez que a transação foi confirmada (commit), os dados alterados devem resistir a falhas e reinicializações do sistema, sendo gravados de forma permanente no armazenamento não volátil (geralmente por meio de logs de transação).

## d) Uma transferência que levaria o saldo abaixo do limite permitido é rejeitada pelo banco.

Consistência. SGBD e a aplicação devem garantir que o banco passe de um estado válido a outro, respeitando todas as regras de negócio e restrições de integridade definidas, como a proibição de ultrapassar o limite permitido de saldo.

---

# Q5 - Um SGBD trata dos seguintes aspectos: recuperação, integridade, redundância e inconsistência. Explique cada um deles e descreva como o SGBD os gerencia. 

A recuperação trata da capacidade de restaurar o banco a um estado consistente após falhas de hardware, software ou interrupções de energia. O SGBD gerencia isso mantendo um arquivo de log de transações (Write-Ahead Logging), o que permite refazer operações confirmadas (redo) e desfazer operações incompletas (undo) durante o reinício do sistema.

A integridade garante a precisão, validade e confiabilidade dos dados armazenados em conformidade com as regras do negócio e do modelo relacional. O SGBD a gerencia aplicando restrições automáticas declaradas no esquema, como chaves primárias (integridade de entidade), chaves estrangeiras (integridade referencial), valores não nulos (NOT NULL) e regras de checagem (CHECK).

A redundância refere-se à duplicação desnecessária de um mesmo dado em diferentes tabelas ou registros do banco. O SGBD mitiga esse problema por meio de técnicas de normalização e estruturas relacionais bem modeladas, assegurando que cada dado possua um local único de armazenamento lógico, utilizando referências (chaves estrangeiras) em vez de cópias.

A inconsistência ocorre quando cópias de um mesmo dado assumem valores divergentes devido a falhas em atualizações simultâneas ou redundância descontrolada. O SGBD a gerencia integrando o controle de redundância com mecanismos de controle de concorrência e transações ACID, garantindo que toda modificação seja propagada de forma atômica e coordenada em todo o sistema.

---

# Q6 - Considere o cenário de uma empresa de desenvolvimento de software que atende outras empresas como clientes. A empresa organiza seu trabalho em squads (equipes) compostas por desenvolvedores, testadores, líder técnico, supervisor e gerente de produto. Cada squad resolve tarefas (issues) e planeja releases, testes e o cronograma de sprints (iterações) dos projetos de cada cliente. 

# Sem utilizar SQL, elabore um mini-projeto conceitual do banco de dados dessa empresa, deixando claro: 

## a) As principais entidades envolvidas (clientes, squads, membros, tarefas, projetos, sprints, releases). 

* Cliente: representa a empresa contratante que demanda e financia as soluções de software.
* Projeto: representa o escopo de software contratado por um cliente a ser desenvolvido.
* Squad: representa a equipe multidisciplinar de colaboradores alocada para executar projetos.
* Membro: representa os profissionais individuais que integram as equipes técnicas e de gestão.
* Sprint: representa a iteração ou ciclo de tempo fixo de trabalho planejado para o projeto.
* Tarefa (Issue): representa a unidade de trabalho, funcionalidade ou correção a ser realizada.
* Release: representa o pacote de entrega ou versão finalizada do software publicada para o cliente.
* Teste: representa os procedimentos de validação e garantia de qualidade aplicados às tarefas.

## b) Os principais atributos de cada entidade. 

* Cliente: id_cliente (identificador único), razao_social, cnpj, email_contato, telefone.
* Projeto: id_projeto (identificador único), nome_projeto, descricao, data_inicio, data_previsao_fim, status.
* Squad: id_squad (identificador único), nome_squad, data_criacao.
* Membro: id_membro (identificador único), nome, email, cargo_papel (Desenvolvedor, Testador, Líder Técnico, Supervisor, Gerente de Produto).
* Sprint: id_sprint (identificador único), numero_sprint, data_inicio, data_fim, objetivo.
* Tarefa (Issue): id_tarefa (identificador único), titulo, descricao, tipo (Bug, Feature, Melhoria), prioridade, status (A * Fazer, Em Andamento, Concluída).
* Release: id_release (identificador único), versao_tag (ex.: v1.0.0), data_lancamento, notas_da_versao.
* Teste: id_teste (identificador único), nome_cenario, resultado (Passou, Falhou, Bloqueado), data_execucao.

## c) Os relacionamentos entre as entidades (com a cardinalidade, ex.: "um cliente pode ter vários projetos").

* Cliente – Projeto: Um Cliente pode contratar um ou muitos Projetos (1:N), e cada Projeto pertence obrigatoriamente a exatamente um Cliente (1:1).
* Squad – Projeto: Uma Squad pode atender a um ou vários Projetos ao longo do tempo (1:N), e cada Projeto é conduzido por uma Squad responsável (1:1).
* Squad – Membro: Uma Squad é composta por vários Membros (1:N), e cada Membro está alocado em exatamente uma Squad ativa por período (1:1).
* Projeto – Sprint: Um Projeto é organizado em uma ou várias Sprints (1:N), e cada Sprint pertence exclusivamente a um Projeto (1:1).
* Projeto – Release: Um Projeto planeja uma ou várias Releases (1:N), e cada Release pertence a um único Projeto (1:1).
* Sprint – Tarefa: Uma Sprint pode conter zero, uma ou várias Tarefas (1:N), e cada Tarefa planejada está associada a uma única Sprint (1:1).
* Membro – Tarefa: Um Membro pode ser responsável por zero ou várias Tarefas (1:N), e cada Tarefa possui no máximo um Membro responsável atribuído (0:1).
* Release – Tarefa: Uma Release agrupa uma ou várias Tarefas concluídas (1:N), e uma Tarefa finalizada pode compor no máximo uma Release (0:1).
* Tarefa – Teste: Uma Tarefa pode passar por um ou vários Testes de validação (1:N), e cada Teste é vinculado a uma Tarefa específica (1:1).

## d) Em linguagem natural, as regras de integridade (restrições) que o banco de dados deveria garantir, ex.: "apenas um líder por squad", "toda tarefa precisa estar vinculada a um projeto". 

* Liderança e Gestão Únicas por Squad: Cada Squad deve possuir obrigatoriamente apenas um Líder Técnico e no máximo um Gerente de Produto ativos simultaneamente.
* Consistência Cronológica das Sprints: A data de término de uma Sprint deve ser estritamente posterior à sua data de início, e duas Sprints do mesmo Projeto não podem ter intervalos de datas sobrepostos.
* Vínculo Obrigatório de Tarefas: Toda Tarefa cadastrada deve estar obrigatoriamente associada a um Projeto ativo e a uma Squad executora.
* Atribuição Consistente de Responsáveis: Um Membro só pode ser atribuído como responsável por uma Tarefa se pertencer à mesma Squad responsável pelo Projeto da referida Tarefa.
* Validação Prévia para Fechamento de Release: Uma Tarefa só pode ser vinculada a uma Release se todos os seus Testes associados tiverem status registrado como "Passou" e o status da própria Tarefa for "Done".
* Unicidade de Identificadores e Versões: Cada Cliente deve possuir um CNPJ único no sistema, e a versão de cada Release deve ser única dentro do escopo do mesmo Projeto.

---