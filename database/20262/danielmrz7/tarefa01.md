# Tarefa 01 - Conceitos de BD, ACID e SGBD

**Aluno:** Daniel Mariz da Silva  
**GitHub Username:** danielmrz7  

---

## 📌 Guia de Conceitos do Git e GitHub

- **Branchs:** Linhas paralelas de desenvolvimento. Permitem criar, testar e isolar novas funcionalidades sem afetar o código principal (`main`).
- **Pull Request (ou Merge Request):** Solicitação formal para integrar as alterações de uma branch (ou fork) para o repositório/branch de destino. Permite revisão de código (*code review*) e execução de testes automatizados.
- **Merge:** Operação que combina o histórico e os commits de duas branchs, criando tipicamente um commit de mesclagem (*merge commit*).
- **Rebase:** Reescreve o histórico de commits, aplicando as alterações de uma branch no topo de outra. Resulta em um histórico linear e sem commits de merge adicionais.
- **Conflitos:** Ocorrem quando o Git não consegue mesclar automaticamente alterações feitas no mesmo trecho de um arquivo em branchs diferentes. Exigem resolução manual por parte do desenvolvedor.

---

## Q1. Conceito de BD, SGBD e Exemplos

- **Banco de Dados (BD):** Coleção organizada de dados inter-relacionados que representam aspectos do mundo real e são armazenados eletronicamente para posterior consulta, processamento e recuperação.
- **Sistema Gerenciador de Banco de Dados (SGBD):** Software ou conjunto de programas encarregado de criar, gerenciar, manipular, consultar e controlar o acesso de segurança ao banco de dados, atuando como interface entre as aplicações e os dados físicos.

### Exemplos de BDs e seus SGBDs

| Tipo de Banco de Dados | Exemplo de BD | SGBD Correspondente |
| :--- | :--- | :--- |
| **Relacional (RDBMS)** | Sistema de Gestão Acadêmica | PostgreSQL / MySQL / Oracle Database |
| **NoSQL (Documentos)** | Catálogo de Produtos E-commerce | MongoDB |
| **NoSQL (Chave-Valor)** | Sessões de Usuário em Cache | Redis |

---

## Q2. Problemas do uso de Sistemas de Arquivos para Armazenagem de Dados

1. **Redundância e Inconsistência de Dados:** O mesmo dado pode ser duplicado em vários arquivos de formatos distintos, gerando divergências e desperdício de armazenamento.
2. **Dificuldade no Acesso aos Dados:** Consultas não ad hoc exigem a escrita de novos programas para extrair informações específicas.
3. **Isolamento de Dados:** Dados espalhados em múltiplos arquivos e formatos tornam difícil a criação de consultas integradas.
4. **Problemas de Atomicidade:** Falhas no meio de uma operação deixam o sistema em estado parcial e inconsistente.
5. **Anomalias no Acesso Concorrente:** Múltiplos acessos simultâneos sem controle de concorrência causam sobrescrita indesejada (*lost update*).
6. **Problemas de Segurança e Integridade:** Difícil aplicação de restrições de segurança por perfil e validações de integridade complexas.

---

## Q3. Propriedades ACID

### 1. Atomicidade (*Atomicity*)
- **Explicação:** Trata a transação como uma unidade indivisível: ou **todas** as operações são executadas com sucesso, ou **nenhuma** é aplicada (*all or nothing*).
- **Exemplo Prático (Transferência Bancária):** Debitar R$ 100 da conta A e creditar R$ 100 na conta B.
- **Sem a garantia do SGBD:** Se o sistema falhar após o débito na conta A mas antes do crédito na conta B, o dinheiro "desaparece" do sistema, deixando o saldo inconsistente.

### 2. Consistência (*Consistency*)
- **Explicação:** Garante que a transação levará o banco de dados de um estado válido a outro estado válido, respeitando todas as regras de integridade e restrições impostas pelo esquema.
- **Exemplo Prático:** A soma dos saldos da conta A e B deve permanecer constante após a transferência, e a conta A não pode ter saldo negativo se houver restrição para tal.
- **Sem a garantia do SGBD:** Transações poderiam violar chaves estrangeiras, limites de saldo ou constraints de validação, corrompendo a integridade estrutural das tabelas.

### 3. Isolamento (*Isolation*)
- **Explicação:** Garante que a execução simultânea de múltiplas transações resulte no mesmo estado que ocorreria se fossem executadas sequencialmente. Uma transação em andamento não vê dados intermediários de outra.
- **Exemplo Prático:** Se a transferência da conta A para a conta B ocorre ao mesmo tempo em que a conta A gera um extrato, o extrato deve ver o saldo de A totalmente antes ou totalmente depois da transferência.
- **Sem a garantia do SGBD:** Ocorreriam problemas de leitura suja (*dirty read*), leituras não repetíveis (*non-repeatable read*) ou dados fantasmas (*phantom read*).

### 4. Durabilidade (*Durability*)
- **Explicação:** Garante que, uma vez confirmada (*committed*), o resultado de uma transação é permanente e persistido no armazenamento não volátil, mesmo em caso de falha física ou operacional do servidor.
- **Exemplo Prático:** Quando a mensagem de "Transferência realizada com sucesso" é exibida, os novos saldos das contas A e B são salvos no disco.
- **Sem a garantia do SGBD:** Uma queda de energia imediatamente após o término da transação faria o banco perder os dados salvos apenas em memória RAM.

---

## Q4. Análise de Cenários e Propriedades ACID

- **a) Queda de energia no meio de uma transferência deixou o valor debitado da conta de origem, mas não creditado na conta de destino.**
  - **Propriedade em jogo:** **Atomicidade**.
  - **Justificativa:** A transação foi executada parcialmente (débito sem o crédito). A atomicidade deveria ter revertido (*rollback*) o débito assim que a transação foi interrompida.

- **b) Dois atendentes debitam, ao mesmo tempo, o mesmo saldo de uma conta.**
  - **Propriedade em jogo:** **Isolamento**.
  - **Justificativa:** Trata-se de um conflito de concorrência (atualização perdida). O SGBD deveria isolar as duas transações utilizando mecanismos de bloqueio (*locks*) ou controle de concorrência otimista/pessimista.

- **c) O sistema confirma a operação, mas após reiniciar o servidor o dado foi perdido.**
  - **Propriedade em jogo:** **Durabilidade**.
  - **Justificativa:** Após o término (*commit*) da transação, as alterações deveriam ter sido persistidas no log de transações/disco de forma irrecuperável por reinicializações.

- **d) Uma transferência que levaria o saldo abaixo do limite permitido é rejeitada pelo banco.**
  - **Propriedade em jogo:** **Consistência**.
  - **Justificativa:** O sistema aplicou e protegeu uma regra de integridade do negócio (restrição de saldo não negativo/limite), garantindo que o banco permaneça em um estado válido.

---

## Q5. Aspectos Tratados pelo SGBD

1. **Recuperação (*Recovery*):**
   - **Conceito:** Capacidade de restaurar o banco de dados a um estado consistente após falhas de hardware, software ou sistema.
   - **Gerenciamento pelo SGBD:** Utilização de logs de transações (ex.: Write-Ahead Logging - WAL), pontos de verificação (*checkpoints*) e rotinas de *UNDO* (desfazer transações incompletas) e *REDO* (refazer transações confirmadas).

2. **Integridade (*Integrity*):**
   - **Conceito:** Garantia de que os dados armazenados sejam corretos, precisos e válidos de acordo com o modelo de dados.
   - **Gerenciamento pelo SGBD:** Imposição de restrições (chaves primárias `PRIMARY KEY`, chaves estrangeiras `FOREIGN KEY`, restrições `UNIQUE`, `NOT NULL` e `CHECK`).

3. **Redundância (*Redundancy*):**
   - **Conceito:** Duplicação desnecessária de dados armazenados no sistema.
   - **Gerenciamento pelo SGBD:** Aplicação de técnicas de **normalização** de dados na fase de projeto relacional, eliminando dados duplicados e centralizando informações em tabelas específicas.

4. **Inconsistência (*Inconsistency*):**
   - **Conceito:** Presença de informações conflitantes ou divergentes para o mesmo dado no banco.
   - **Gerenciamento pelo SGBD:** Controle rígido de concorrência (bloqueios, isolamento de transações, MVCC) e eliminação da redundância de dados descontrolada.

---

## Q6. Mini-Projeto Conceitual de Banco de Dados

### a) Entidades Principais
- **Cliente**
- **Projeto**
- **Squad**
- **Membro (Colaborador)**
- **Sprint**
- **Release**
- **Tarefa (Issue)**

### b) Atributos das Entidades
- **Cliente:** `id_cliente`, `nome_razao_social`, `cnpj`, `email_contato`, `telefone`.
- **Projeto:** `id_projeto`, `nome_projeto`, `descricao`, `data_inicio`, `status`.
- **Squad:** `id_squad`, `nome_squad`, `area_foco`.
- **Membro:** `id_membro`, `nome`, `cpf`, `email`, `cargo` (Dev, Tester, Tech Lead, Supervisor, PM).
- **Sprint:** `id_sprint`, `numero_sprint`, `data_inicio`, `data_fim`, `meta`.
- **Release:** `id_release`, `versao`, `data_planejada`, `status`.
- **Tarefa:** `id_tarefa`, `titulo`, `descricao`, `prioridade`, `status`, `estimativa_horas`.

### c) Relacionamentos e Cardinalidades
- **Cliente 1 : N Projeto** (Um cliente pode ter vários projetos; um projeto pertence a exatamente um cliente).
- **Projeto N : 1 Squad** (Vários projetos podem ser atendidos por uma squad; uma squad pode atender vários projetos).
- **Squad 1 : N Membro** (Uma squad possui vários membros; um membro pertence a uma squad).
- **Projeto 1 : N Release** (Um projeto possui várias releases; uma release pertence a um projeto).
- **Projeto 1 : N Sprint** (Um projeto é dividido em várias sprints; uma sprint pertence a um projeto).
- **Sprint 1 : N Tarefa** (Uma sprint possui várias tarefas; uma tarefa pode estar associada a uma sprint).
- **Release 1 : N Tarefa** (Uma release agrupa várias tarefas; uma tarefa pode estar vinculada a uma release).
- **Membro 1 : N Tarefa** (Um membro pode ser responsável por várias tarefas; uma tarefa possui um membro responsável).

### d) Regras de Integridade (Restrições em Linguagem Natural)
1. Cada Squad deve possuir **exatamente um único Membro** com a função de Líder Técnico (Tech Lead).
2. Toda Tarefa deve obrigatoriamente estar vinculada a **pelo menos um Projeto**.
3. O intervalo de datas de uma Sprint (`data_inicio` a `data_fim`) deve estar contido no período de vigência do seu respectivo Projeto.
4. Um Membro só pode ser alocado para responder por Tarefas da Squad da qual ele faz parte.
5. Não é permitida a exclusão de um Cliente que possua Projetos com status "Em Andamento".
6. O código identificador de cada Tarefa deve ser único dentro do mesmo Projeto.