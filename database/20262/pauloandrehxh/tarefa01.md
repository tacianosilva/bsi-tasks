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

## Q3. Explique as propriedades ACID: atomicidade, consistência, isolamento e durabilidade. Para cada propriedade, descreva um exemplo prático no contexto de uma transferência bancária e explique o que aconteceria se o SGBD não garantisse essa propriedade.

| Propriedade | Descrição | Exemplo na Transferência de R$ 100 de A para B | O que acontece se o SGBD falhar? |
| :--- | :--- | :--- | :--- |
| **Atomicidade** | A transação é "tudo ou nada". Todas as operações da transação ocorrem com sucesso ou nenhuma delas ocorre. | O SGBD debita R$ 100 da conta A e credita R$ 100 na conta B. Ambas as ações formam uma unidade. | O dinheiro é debitado de A, ocorre um erro, e não é creditado em B. O dinheiro "desaparece" do sistema. |
| **Consistência** | A transação deve levar o banco de um estado válido para outro estado válido, respeitando todas as regras e restrições. | A soma total dos saldos do banco antes e depois da transferência deve ser a mesma. O saldo de A não pode ficar negativo se a regra impedir. | A transferência é concluída, mas deixa a conta A com saldo negativo não permitido, violando as regras do negócio. |
| **Isolamento** | Transações simultâneas não devem interferir umas nas outras. Cada uma deve ocorrer como se fosse a única no sistema. | O usuário A tenta transferir para B, e simultaneamente para C, usando seu saldo de R$ 100. | Ambas as transferências leem o saldo inicial de R$ 100 ao mesmo tempo e ambas são aprovadas. O usuário gasta o mesmo dinheiro duas vezes (anomalia de concorrência). |
| **Durabilidade** | Uma vez que a transação é concluída (commit), seus efeitos são permanentes, mesmo em caso de falha de sistema. | O sistema confirma a transferência na tela do usuário. O dado já está salvo em disco de forma definitiva. | O sistema confirma a transferência, mas cai logo em seguida antes de escrever no disco físico. Ao reiniciar, a transferência sumiu como se nunca tivesse ocorrido. |

## Q4. Para cada cenário abaixo, indique qual(is) propriedade(s) ACID está(ão) em jogo e justifique sua resposta:

*   **a) Queda de energia no meio de uma transferência deixou o valor debitado da conta de origem, mas não creditado na conta de destino.**
    *   **Propriedade violada:** **Atomicidade**. A transação foi dividida ao meio, contrariando a regra de que ela deve ser executada por completo ou totalmente desfeita (rollback).
*   **b) Dois atendentes debitam, ao mesmo tempo, o mesmo saldo de uma conta.**
    *   **Propriedade violada:** **Isolamento**. As transações concorrentes enxergaram estados intermediários umas das outras (ou o mesmo estado inicial simultaneamente), gerando uma condição de corrida (*race condition*).
*   **c) O sistema confirma a operação, mas após reiniciar o servidor o dado foi perdido.**
    *   **Propriedade violada:** **Durabilidade**. A garantia de que uma transação comutada (*committed*) sobrevive a falhas de hardware ou software falhou.
*   **d) Uma transferência que levaria o saldo abaixo do limite permitido é rejeitada pelo banco.**
    *   **Propriedade em ação:** **Consistência**. O SGBD impediu que a transação fosse concluída porque ela violaria uma regra de integridade do sistema (saldo >= limite).

## Q5. Um SGBD trata dos seguintes aspectos: recuperação, integridade, redundância e inconsistência. Explique cada um deles e descreva como o SGBD os gerencia.

1.  **Recuperação (Recovery):** É a capacidade de restaurar o banco de dados para um estado consistente após uma falha. O SGBD gerencia isso através de *logs de transações* que registram todas as mudanças antes que elas sejam efetivadas no disco, permitindo refazer ou desfazer operações.
2.  **Integridade (Integrity):** É a garantia da correção e validade dos dados. O SGBD gerencia isso através da aplicação de *constraints* (restrições), como Chaves Primárias, Chaves Estrangeiras e regras de domínio.
3.  **Redundância (Redundancy):** É o armazenamento repetido da mesma informação. O SGBD (em conjunto com um bom design relacional) ajuda a minimizar a redundância centralizando as tabelas e usando chaves estrangeiras.
4.  **Inconsistência (Inconsistency):** É uma consequência direta da redundância descontrolada. O SGBD evita isso mantendo uma única fonte de verdade.

## Q6. Considere o cenário de uma empresa de desenvolvimento de software que atende outras empresas como clientes. A empresa organiza seu trabalho em squads (equipes) compostas por desenvolvedores, testadores, líder técnico, supervisor e gerente de produto. Cada squad resolve tarefas (issues) e planeja releases, testes e o cronograma de sprints (iterações) dos projetos de cada cliente. 
**Sem utilizar SQL, elabore um mini-projeto conceitual do banco de dados dessa empresa, deixando claro:**
- **A) As principais entidades envolvidas (clientes, squads, membros, tarefas, projetos, sprints, releases).**
- **B) Os principais atributos de cada entidade.** 
- **C) Os relacionamentos entre as entidades (com a cardinalidade, ex.: "um cliente pode ter vários projetos").**
- **D) Em linguagem natural, as regras de integridade (restrições) que o banco de dados deveria garantir, ex.: "apenas um líder por squad", "toda tarefa precisa estar vinculada a um projeto".**



### A) Entidades e B) Principais Atributos

*   **Cliente:** 
    * `id_cliente` (PK), 
    * `nome_empresa`, 
    * `cnpj`, 
    * `setor`, 
    * `contato_principal`.

*   **Squad:** 
    * `id_squad` (PK), 
    * `nome_squad`, 
    * `especialidade`.

*   **Membro:** 
    * `id_membro` (PK), 
    * `nome_membro`, 
    * `email`, 
    * `cargo`.

*   **Projeto:** 
    * `id_projeto` (PK), 
    * `nome_projeto`, 
    * `descricao`, 
    * `data_inicio`, 
    * `data_fim_prevista`, 
    * `status`.

*   **Sprint:** `id_sprint` (PK),
    * `nome_sprint`, 
    * `data_inicio`, 
    * `data_fim`, 
    * `objetivo`.

*   **Release:** `id_release` (PK), 
    * `versao`, 
    * `data_lancamento`, 
    * `notas_release`.

*   **Tarefa (Issue):** `id_tarefa` (PK), 
    * `titulo`, 
    * `descricao`, 
    * `status`, 
    * `prioridade`, 
    * `estimativa_horas`.

### C) Relacionamentos e Cardinalidade

*   **Cliente e Projeto (1 : N):** Um *Cliente* pode possuir vários *Projetos*, mas um *Projeto* pertence a exatamente um *Cliente*.
*   **Squad e Projeto (1 : N):** Uma *Squad* pode gerenciar vários *Projetos*, mas um *Projeto* é atribuído a exatamente uma *Squad*.
*   **Squad e Membro (1 : N):** Uma *Squad* é composta por vários *Membros*, mas um *Membro* pertence a apenas uma *Squad*.
*   **Projeto e Sprint (1 : N):** Um *Projeto* possui várias *Sprints*, mas uma *Sprint* pertence a apenas um *Projeto*.
*   **Projeto e Release (1 : N):** Um *Projeto* possui várias *Releases*, mas uma *Release* pertence a apenas um *Projeto*.
*   **Sprint e Tarefa (1 : N):** Uma *Sprint* contém várias *Tarefas*, mas uma *Tarefa* pertence a, no máximo, uma *Sprint*.
*   **Release e Tarefa (1 : N):** Uma *Release* engloba várias *Tarefas*, mas uma *Tarefa* está associada a, no máximo, uma *Release*.
*   **Membro e Tarefa (1 : N):** Um *Membro* pode ser o responsável por várias *Tarefas*, mas uma *Tarefa* é alocada a apenas um *Membro*.

### D) Regras de Integridade (Restrições)

1.  **Restrição de Liderança:** Cada Squad deve possuir exatamente um (e não mais que um) membro com o cargo de "Líder Técnico" ativo.
2.  **Dependência Existencial da Tarefa:** Toda Tarefa deve, obrigatoriamente, estar vinculada a um Projeto válido.
3.  **Consistência Temporal da Sprint:** A `data_fim` de uma Sprint deve ser obrigatoriamente maior ou igual à sua `data_inicio`. Sprints do mesmo Projeto não podem ter sobreposição de datas.
4.  **Consistência Temporal da Release:** A `data_lancamento` de uma Release não pode ser anterior à `data_inicio` do Projeto ao qual ela pertence.
5.  **Regra de Atribuição:** Uma Tarefa só pode ser atribuída a um Membro que pertença à mesma Squad responsável pelo Projeto dessa Tarefa.
6.  **Integridade de Identificação:** Não podem existir dois Clientes com o mesmo `cnpj` cadastrado.