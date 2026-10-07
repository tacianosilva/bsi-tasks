# Tarefa 01 - Conceitos de Banco de Dados

### Q1. Descreva o que é um Banco de Dados e o que é um Sistema Gerenciador de Banco de Dados. Cite exemplos de Bancos de Dados e seus SGBDs.
* **Banco de Dados (BD):** É a coleção organizada de dados logicamente relacionados, armazenados de forma estruturada (geralmente em arquivos físicos no disco) para permitir fácil acesso, gerenciamento e atualização.
* **Sistema Gerenciador de Banco de Dados (SGBD):** É o software (ou conjunto de softwares) que serve como interface entre o banco de dados, os usuários e as aplicações. Ele gerencia o armazenamento, a segurança, a integridade e o acesso aos dados.
* **Exemplos:** 
  * *SGBDs:* MySQL, PostgreSQL, Oracle Database, Microsoft SQL Server.
  * *Bancos de Dados:* O arquivo físico de dados gerado por um sistema de RH, o arquivo `.mdf` do SQL Server de um sistema de vendas, ou o banco de dados interno de um aplicativo de celular (gerenciado via SQLite).

### Q2. Quais os principais problemas de utilizar Sistemas de Arquivos para armazenagem de dados?
Antes dos SGBDs, os dados eram salvos em sistemas de arquivos comuns do sistema operacional. Os principais problemas eram:
1. **Redundância e inconsistência de dados:** O mesmo dado (ex: endereço de um cliente) salvo em vários arquivos diferentes, correndo o risco de ser atualizado em um e esquecido no outro.
2. **Dificuldade de acesso:** Cada nova consulta exigia que um programador escrevesse um código específico para ler o arquivo.
3. **Isolamento de dados:** Dados espalhados em diferentes arquivos e formatos, dificultando o cruzamento de informações.
4. **Problemas de integridade:** Dificuldade em aplicar regras de negócio (ex: "o saldo não pode ser negativo") diretamente no arquivo.
5. **Acesso concorrente:** Se dois usuários tentassem editar o mesmo arquivo de texto simultaneamente, os dados de um deles seriam sobrescritos e perdidos.
6. **Falta de atomicidade:** Se o sistema caísse no meio de uma gravação, o arquivo poderia corromper e ficar pela metade.

### Q3. Explique as propriedades ACID: atomicidade, consistência, isolamento e durabilidade. Para cada propriedade, descreva um exemplo prático no contexto de uma transferência bancária e explique o que aconteceria se o SGBD não garantisse essa propriedade.
* **Atomicidade (Tudo ou Nada):** Uma transação deve ser executada por completo ou não ser executada. 
  * *Exemplo:* Transferir R$ 100 de A para B exige duas ações: debitar de A e creditar em B. 
  * *Se falhar:* Se o sistema cair após debitar de A, a atomicidade garante o desfazimento (*rollback*) da operação. Sem ela, o dinheiro de A sumiria e não chegaria em B.
* **Consistência:** A transação deve levar o banco de dados de um estado válido para outro estado válido, respeitando todas as regras.
  * *Exemplo:* A soma total do dinheiro de A e B antes e depois da transferência deve ser a mesma.
  * *Se falhar:* O banco poderia criar dinheiro do nada ou permitir que uma conta ficasse com saldo negativo mesmo que a regra de negócio proibisse.
* **Isolamento:** Transações simultâneas não devem interferir umas nas outras.
  * *Exemplo:* Se você transfere R$ 100 para a conta B no exato milissegundo em que outra pessoa deposita R$ 50 na mesma conta. 
  * *Se falhar:* Uma operação poderia ler o saldo da conta B antes da outra terminar, sobrescrevendo o valor e fazendo um dos depósitos "desaparecer" (leitura suja ou atualização perdida).
* **Durabilidade:** Uma vez confirmada (*commit*), a transação é permanente, mesmo em caso de falha do sistema.
  * *Exemplo:* O caixa eletrônico emite o comprovante da transferência e, um segundo depois, acaba a energia do data center.
  * *Se falhar:* Ao reiniciar, a transferência confirmada não estaria no banco de dados. Com durabilidade garantida, o dado já estará salvo no disco físico.

### Q4. Identificação das Propriedades ACID nos Cenários
* **a)** Queda de energia no meio de uma transferência deixou o valor debitado, mas não creditado.
  * **Propriedade:** **Atomicidade**. Justificativa: A transação foi interrompida pela metade e não desfez (rollback) as etapas parciais.
* **b)** Dois atendentes debitam, ao mesmo tempo, o mesmo saldo de uma conta.
  * **Propriedade:** **Isolamento**. Justificativa: Falta de controle de concorrência. Uma transação enxergou o estado incompleto ou não bloqueado da outra.
* **c)** O sistema confirma a operação, mas após reiniciar o servidor o dado foi perdido.
  * **Propriedade:** **Durabilidade**. Justificativa: A garantia de que um dado "commitado" sobreviveria a falhas (sendo gravado em disco) não foi cumprida.
* **d)** Uma transferência que levaria o saldo abaixo do limite permitido é rejeitada pelo banco.
  * **Propriedade:** **Consistência**. Justificativa: O SGBD impediu a operação porque ela violava uma restrição de integridade (regra de negócio de limite de saldo).

### Q5. Um SGBD trata dos seguintes aspectos: recuperação, integridade, redundância e inconsistência. Explique cada um deles e descreva como o SGBD os gerencia.
* **Recuperação (Recovery):** É a capacidade do SGBD de restaurar o banco para um estado consistente após falhas de hardware ou software. O SGBD gerencia isso usando *Logs* de transações (que registram cada passo antes de alterar o dado real) e rotinas de *Backup*, permitindo refazer (Redo) ou desfazer (Undo) operações.
* **Integridade:** Garantia de que os dados estão corretos e seguem as regras. O SGBD gerencia isso através de restrições (Constraints) como chaves primárias, chaves estrangeiras, verificação de tipos de dados e triggers, bloqueando inserções inválidas na raiz.
* **Redundância:** É a duplicação desnecessária de dados. O SGBD (em um modelo relacional bem feito) minimiza a redundância usando a normalização, garantindo que um dado seja armazenado em apenas um lugar e referenciado por IDs em outras tabelas.
* **Inconsistência:** É o resultado da redundância descontrolada (o mesmo dado com valores diferentes em locais diferentes). O SGBD evita isso ao centralizar o dado; se o nome do cliente muda na tabela de clientes, todas as consultas que cruzam com essa tabela passam a ver o nome novo instantaneamente.

### Q6. Mini-projeto Conceitual de Banco de Dados (Empresa de Software)

Este modelo conceitual descreve a estrutura de dados necessária para gerenciar o fluxo de trabalho ágil da empresa de desenvolvimento de software, garantindo o rastreamento desde o cliente até a entrega final (release).

**a) Entidades Principais e b) Seus Atributos**

* **Cliente:** 
  * `ID_Cliente` (Identificador único)
  * `Razao_Social` e `Nome_Fantasia`
  * `CNPJ` 
  * `Email_Contato` e `Telefone`
  * `Data_Cadastro`
* **Projeto:** 
  * `ID_Projeto` (Identificador único)
  * `Nome_Projeto`
  * `Descricao_Escopo`
  * `Data_Inicio` e `Data_Previsao_Fim`
  * `Status` (Ex: Planejamento, Em Andamento, Pausado, Concluído)
* **Squad (Equipe):** 
  * `ID_Squad` (Identificador único)
  * `Nome_Squad` (Ex: "Esquadrão Alpha", "Team Mobile")
  * `Foco_Atuacao` (Ex: Front-end, Back-end, Fullstack)
* **Membro (Colaborador):** 
  * `ID_Membro` (Identificador único)
  * `Nome_Completo`
  * `Email_Corporativo`
  * `Papel` (Desenvolvedor, Testador, Líder Técnico, Supervisor, Gerente de Produto)
  * `Nivel_Senioridade` (Junior, Pleno, Sênior)
* **Sprint (Iteração):** 
  * `ID_Sprint` (Identificador único)
  * `Numero_Sprint` (Ex: Sprint 1, Sprint 2)
  * `Objetivo_Sprint` (Meta da iteração)
  * `Data_Inicio` e `Data_Fim`
  * `Status` (Planejada, Ativa, Finalizada)
* **Tarefa (Issue):** 
  * `ID_Tarefa` (Identificador único)
  * `Titulo` e `Descricao_Detalhada`
  * `Tipo` (Bug, Nova Funcionalidade, Melhoria técnica)
  * `Prioridade` (Baixa, Média, Alta, Crítica)
  * `Status` (Backlog, A Fazer, Em Progresso, Em Teste, Concluído)
  * `Pontos_Esforco` (Estimativa de complexidade)
* **Release (Entrega):** 
  * `ID_Release` (Identificador único)
  * `Versao_Tag` (Ex: v1.0.0, v1.1.2)
  * `Data_Lancamento`
  * `Notas_Versao` (Release Notes detalhando o que foi entregue)

---

**c) Relacionamentos e Cardinalidade**

* **Cliente ↔ Projeto (1:N):** Um cliente pode solicitar um ou vários projetos ao longo do tempo. No entanto, um projeto pertence exclusivamente a um único cliente.
* **Squad ↔ Membro (1:N):** Uma squad é composta por vários membros colaboradores. Para garantir o foco, cada membro está alocado em apenas uma squad por vez.
* **Projeto ↔ Sprint (1:N):** O ciclo de vida de um projeto é dividido em várias sprints. Uma sprint, por sua vez, está vinculada a um único projeto.
* **Squad ↔ Tarefa (1:N):** Uma squad assume a responsabilidade de resolver múltiplas tarefas. Cada tarefa no sistema é designada para a fila de uma única squad.
* **Membro ↔ Tarefa (1:N):** Um membro pode ser designado como o "responsável técnico" por várias tarefas, mas uma tarefa específica tem apenas um membro executando-a em determinado momento.
* **Sprint ↔ Tarefa (1:N):** Durante o planejamento, uma sprint agrupa diversas tarefas a serem executadas. Uma vez planejada, a tarefa pertence àquela sprint específica.
* **Projeto ↔ Release (1:N):** Um projeto gera diversas entregas (releases) incrementais ao longo do seu desenvolvimento.
* **Release ↔ Tarefa (1:N):** Uma release é composta por um conjunto de tarefas concluídas. Uma tarefa que foi entregue fica registrada no histórico de uma única release.

---

**d) Regras de Integridade e Restrições de Negócio**

Para garantir a qualidade e a consistência dos dados (evitando anomalias), o banco de dados deve aplicar as seguintes regras em linguagem natural:

1. **Regra de Composição Estrutural da Squad:** Toda squad deve ser formada obrigatoriamente por pelo menos um desenvolvedor e um testador, e possuir uma estrutura de gestão com **exatamente** um (1) Líder Técnico, um (1) Supervisor e um (1) Gerente de Produto.
2. **Integridade de Atribuição (Dependência Lógica):** Uma tarefa só pode ser atribuída a um `Membro` se este membro pertencer à `Squad` responsável por aquela tarefa.
3. **Integridade de Lançamento (Release):** O sistema deve bloquear a inclusão de uma tarefa em uma Release caso o `Status` da tarefa seja diferente de "Concluído". Não se pode entregar código não finalizado.
4. **Integridade Temporal e Cronológica:** A `Data_Fim` de uma Sprint deve ser obrigatoriamente posterior à sua `Data_Inicio`. Da mesma forma, a `Data_Lancamento` de uma Release não pode ser anterior à data de início do respectivo projeto.
5. **Integridade Referencial Estrita:** Nenhuma tarefa pode ficar "órfã" no sistema. Ela deve obrigatoriamente estar associada a um Projeto (diretamente no backlog ou através de uma Sprint ativa).
6. **Unicidade de Identificação:** O atributo `CNPJ` na entidade Cliente e o `Email_Corporativo` na entidade Membro não podem se repetir, impedindo duplicidade de cadastros no sistema.