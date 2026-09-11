# Tarefa 01 - Conceitos de Banco de Dados, ACID e SGBD

## Fundamentos de Controle de Versão (Git e GitHub)

### Branches
São ramificações independentes da linha do tempo do projeto. Permitem isolar o desenvolvimento de novas funcionalidades, experimentos ou correções de bugs sem interferir diretamente na branch principal (`main`). Isso possibilita que múltiplos desenvolvedores trabalhem em paralelo de forma segura.

### Pull Request (ou Merge Request)
Mecanismo de colaboração em plataformas como GitHub ou GitLab pelo qual um desenvolvedor solicita que as alterações realizadas em sua branch (ou fork) sejam revisadas e incorporadas à branch de destino. O Pull Request é o espaço central para code review, debates técnicos, execução de testes automatizados (CI) e validações antes da integração.

### Merge
Operação do Git que combina o histórico de duas branches distintas. Ao executar o merge, o Git junta os conjuntos de commits. Quando há divergências de histórico, ele gera um novo commit de junção (chamado de *merge commit*), preservando a história exata de como as branches foram desenvolvidas paralelamente.

### Rebase
Processo alternativo de integração que move ou reaplica uma sequência de commits de uma branch sobre a ponta mais recente de outra branch. Em vez de criar um commit de junção como o merge, o rebase reescreve o histórico de forma linear, facilitando a leitura da linha do tempo do projeto.

### Conflitos
<<<<<<< HEAD
Situação que ocorre quando dois desenvolvedores (ou branches) alteram as mesmas linhas de um mesmo arquivo — ou quando um arquivo é excluído em uma branch e modificado em outra — e o Git tenta uni-los. Como o sistema não pode decidir automaticamente qual alteração é a correta sem risco de perda de lógica, ele suspende a operação e solicita que o desenvolvedor resolva manualmente as seções conflitantes antes de concluir a integração.

---

## Q1. Banco de Dados vs. SGBD

### Banco de Dados (BD)
É uma coleção logicamente coerente e estruturada de dados relacionados, projetada para representar um aspecto específico do mundo real (minimundo) e atender às necessidades operacionais ou analíticas de usuários e sistemas. Os dados são organizados de modo a facilitar seu armazenamento, consulta e atualização, podendo estar centralizados em um servidor ou distribuídos por múltiplos nós.

### Sistema Gerenciador de Banco de Dados (SGBD / DBMS)
É o conjunto de softwares responsáveis por definir, construir, manipular, compartilhar e proteger as bases de dados. O SGBD atua como intermediário entre as aplicações usuárias e o armazenamento físico, fornecendo abstração de dados, mecanismos de controle de concorrência, recuperação após falhas, garantia de integridade e controle rígido de acesso e segurança.

### Exemplos de Bancos de Dados e seus respectivos SGBDs

| Categoria | SGBD | Exemplos Típicos de Bases de Dados |
| :--- | :--- | :--- |
| **Relacional (RDBMS)** | **PostgreSQL** | Base cadastral e financeira de um e-commerce |
| **Relacional (RDBMS)** | **MySQL / MariaDB** | Base transacional de um portal de notícias em WordPress |
| **Relacional Corporativo** | **Oracle Database** | Sistema contábil e de faturamento de uma multinacional |
| **NoSQL (Documentos)** | **MongoDB** | Catálogo de produtos com esquemas flexíveis e logs |
| **NoSQL (Chave-Valor)** | **Redis** | Armazenamento de sessões de usuários e cache de alta velocidade |

---

## Q2. Principais Problemas no Uso de Sistemas de Arquivos para Armazenamento de Dados

Antes da consolidação dos SGBDs, as aplicações armazenavam dados diretamente em arquivos do sistema operacional (como arquivos de texto, binários ou CSV). Essa abordagem apresenta limitações críticas:

1. **Redundância e Inconsistência de Dados:** Como diferentes aplicações criam seus próprios arquivos, a mesma informação acaba duplicada em locais distintos (ex.: endereço do cliente no arquivo de cobrança e no arquivo de entregas). Se um arquivo for atualizado e o outro não, os dados tornam-se contraditórios (inconsistentes).
2. **Dificuldade de Acesso aos Dados:** Consultas não previstas originalmente exigem a escrita de novos programas ou scripts manuais para varrer, filtrar e extrair as informações necessárias, tornando a recuperação de dados lenta e dependente de desenvolvimento.
3. **Isolamento de Dados:** Como os dados ficam dispersos em múltiplos arquivos com extensões e formatos heterogêneos, cruzá-los ou correlacioná-los exige esforço complexo de processamento manual.
4. **Problemas de Integridade:** As regras de negócio (como "o saldo da conta não pode ser negativo") precisam ser embutidas diretamente no código de cada aplicação cliente. Se novas aplicações forem criadas ou se a regra mudar, a integridade é facilmente violada.
5. **Falta de Atomicidade nas Operações:** Uma falha mecânica ou elétrica no meio da gravação de um arquivo deixa a base em estado parcial e corrompido, sem um mecanismo nativo de retorno ao estado anterior (*rollback*).
6. **Anomalias de Acesso Concorrente:** Se múltiplos usuários ou processos tentarem ler e gravar no mesmo arquivo simultaneamente, ocorrem problemas graves de corrida (*race conditions*), como a sobrescrita inadvertida de dados (*lost update*).
7. **Problemas de Segurança e Controle de Acesso:** Sistemas de arquivos oferecem controle de permissões em nível de arquivo ou pasta, sendo inviável restringir o acesso a colunas ou linhas específicas para perfis de usuários distintos.

---

## Q3. Propriedades ACID

As propriedades ACID definem os requisitos essenciais que garantem que transações em um banco de dados sejam processadas com confiabilidade.

### 1. Atomicidade (*Atomicity*)
* **Conceito:** A transação é indivisível ("tudo ou nada"). Ou todas as operações que compõem a transação são concluídas com êxito, ou nenhuma alteração é aplicada, revertendo o banco ao seu estado original (*rollback*).
* **Exemplo Bancário:** Transferência de R$ 200 da Conta A para a Conta B. A transação envolve: debitar R$ 200 de A e creditar R$ 200 em B.
* **Sem a propriedade:** Se o sistema falhar logo após debitar a Conta A e antes de creditar a Conta B, o dinheiro simplesmente sumiria do sistema: o cliente A perde R$ 200 e o cliente B não recebe nada.

### 2. Consistência (*Consistency*)
* **Conceito:** A execução de uma transação deve conduzir o banco de dados de um estado válido a outro estado igualmente válido, respeitando rigorosamente todas as regras de negócio, restrições de integridade e tipos de dados definidos no esquema.
* **Exemplo Bancário:** Uma regra do banco determina que o saldo de uma conta corrente padrão nunca pode ser inferior a R$ 0.
* **Sem a propriedade:** Se uma transação tentar transferir R$ 500 de uma conta que possui saldo de apenas R$ 100 sem autorização de limite de crédito, o sistema permitiria a operação, violando a integridade contábil e deixando a conta em estado inválido perante as regras do banco.

### 3. Isolamento (*Isolation*)
* **Conceito:** A execução simultânea de múltiplas transações não deve permitir que uma transação interfira no andamento ou visualize estados intermediários incompletos de outra. O resultado final deve ser equivalente ao de uma execução estritamente sequencial.
* **Exemplo Bancário:** Uma conta possui R$ 300. Dois atendentes tentam, no mesmo segundo, debitar R$ 200 cada um em caixas diferentes.
* **Sem a propriedade:** Ambas as transações leem simultaneamente o saldo de R$ 300, consideram a operação viável e realizam o débito. O saldo final ficaria registrado como R$ 100 (uma atualização sobrescreve a outra), permitindo o saque de R$ 400 a partir de um saldo inicial de R$ 300 (*Lost Update*).

### 4. Durabilidade (*Durability*)
* **Conceito:** Uma vez que uma transação é confirmada (*committed*), suas alterações tornam-se permanentes e não serão perdidas por qualquer falha posterior do sistema, como queda de energia ou travamento do servidor.
* **Exemplo Bancário:** O cliente realiza uma transferência e o sistema exibe a mensagem de confirmação com comprovante emitido.
* **Sem a propriedade:** Caso o servidor sofra um desligamento repentino segundos após a confirmação, os dados gravados apenas em memória volátil (RAM) seriam perdidos, fazendo a transação "desaparecer" após o reinício do sistema.

---

## Q4. Análise dos Cenários e Propriedades ACID

### a) Queda de energia no meio de uma transferência deixou o valor debitado da conta de origem, mas não creditado na conta de destino.
* **Propriedade violada:** **Atomicidade**.
* **Justificativa:** A transação foi executada apenas pela metade. Em vez de aplicar a política do "tudo ou nada", o sistema registrou o débito sem o crédito correspondente. O SGBD deveria ter desfeito o débito (*rollback*) automaticamente durante o procedimento de recuperação.

### b) Dois atendentes debitam, ao mesmo tempo, o mesmo saldo de uma conta.
* **Propriedade em jogo / violada:** **Isolamento**.
* **Justificativa:** Trata-se de um problema clássico de concorrência (*lost update* ou leitura suja). Sem o devido isolamento entre transações concorrentes (por exemplo, via mecanismos de bloqueio/locks ou controle por versão - MVCC), uma operação interferiu na outra, levando a um cálculo errôneo do saldo final.

### c) O sistema confirma a operação, mas após reiniciar o servidor o dado foi perdido.
* **Propriedade violada:** **Durabilidade**.
* **Justificativa:** A operação já havia recebido o status de transação concluída (*commit*). O SGBD falhou em persistir as alterações em memória secundária não volátil (por exemplo, via escrita prévia em log - WAL), violando a garantia de permanência dos dados confirmados.

### d) Uma transferência que levaria o saldo abaixo do limite permitido é rejeitada pelo banco.
* **Propriedade garantida:** **Consistência**.
* **Justificativa:** O sistema impediu a transação para evitar a violação de uma restrição de integridade (regra de negócio que define o saldo mínimo). O SGBD garantiu que o banco permanecesse em um estado válido, cancelando a operação que tornaria os dados inconsistentes.

---

## Q5. Aspectos Tratados pelo SGBD

### 1. Recuperação (*Recovery*)
* **Conceito:** Capacidade de restabelecer o banco de dados a um estado íntegro e consistente após falhas de software, hardware, panes de rede ou desastres.
* **Como o SGBD gerencia:** Utiliza o mecanismo de log de transações (*Write-Ahead Logging* - WAL), checkpoints periódicos e algoritmos de recuperação (como o ARIES). Durante a reinicialização pós-falha, o SGBD executa o procedimento de **REDO** (refaz operações de transações confirmadas que não foram descarregadas no disco) e de **UNDO** (desfaz operações de transações que ficaram incompletas no momento da queda).

### 2. Integridade (*Integrity*)
* **Conceito:** Preservação da exatidão, validade e coerência dos dados em conformidade com as regras lógicas e restrições estruturais impostas pelo negócio.
* **Como o SGBD gerencia:** Através de restrições declarativas no esquema DDL, tais como:
  * Integridade de Domínio (tipos de dados, cláusulas `CHECK`, `NOT NULL`).
  * Integridade de Entidade (definição de chaves primárias - `PRIMARY KEY` e chaves candidatas - `UNIQUE`).
  * Integridade Referencial (definição de chaves estrangeiras - `FOREIGN KEY`, com regras de ação como `CASCADE` ou `RESTRICT`).
  * *Triggers* e procedimentos armazenados para regras procedimentais complexas.

### 3. Redundância (*Redundancy*)
* **Conceito:** Existência de dados repetidos desnecessariamente em múltiplos locais do banco de dados, o que consome espaço de armazenamento excessivo e amplia os pontos de falha na manutenção.
* **Como o SGBD gerencia:** Promove o controle da redundância através do processo de **Normalização de Dados** (1FN, 2FN, 3FN, BCNF), decompondo as tabelas e unindo-as logicamente via chaves estrangeiras. Quando a redundância é introduzida deliberadamente (por questões de desempenho/desnormalização ou replicação de servidores), o SGBD assume o controle para manter as cópias sincronizadas automaticamente.

### 4. Inconsistência (*Inconsistency*)
* **Conceito:** Ocorrência de dados divergentes ou contraditórios que representam o mesmo fato no mundo real, geralmente resultante de redundâncias descontroladas ou acessos concorrentes mal administrados.
* **Como o SGBD gerencia:** Elimina a raiz da inconsistência controlando a redundância e aplicando rigorosos mecanismos de **Controle de Concorrência** (como protocolo de bloqueio de duas fases - 2PL, *timestamp ordering* ou MVCC), assegurando que leituras e escritas concorrentes respeitem os níveis de isolamento estabelecidos.

---

## Q6. Mini-Projeto Conceitual: Gestão de Software por Squads

### a) Entidades Principais
1. **Cliente:** Empresa contratante dos serviços de desenvolvimento.
2. **Projeto:** Produto ou sistema contratado por um cliente e desenvolvido pela empresa.
3. **Squad:** Equipe multidisciplinar responsável pelo planejamento e execução do trabalho técnico.
4. **Membro:** Profissional que integra a empresa e atua nas squads (desenvolvedor, testador, líder técnico, supervisor ou gerente de produto).
5. **Sprint:** Iteração de tempo fixo na qual um conjunto planejado de tarefas deve ser executado.
6. **Release:** Versão entregável e estável de um projeto disponibilizada para o cliente ou ambiente de produção.
7. **Tarefa (Issue):** Unidade atômica de trabalho a ser resolvida (bug, nova feature, melhoria técnica ou teste).

### b) Atributos Principais de Cada Entidade

* **Cliente:** `id_cliente` (PK), `cnpj`, `razao_social`, `nome_fantasia`, `email_contato`, `telefone`, `data_cadastro`.
* **Projeto:** `id_projeto` (PK), `nome_projeto`, `descricao`, `data_inicio`, `previsao_termino`, `status`, `id_cliente` (FK).
* **Squad:** `id_squad` (PK), `nome_squad`, `area_foco`, `data_criacao`.
* **Membro:** `id_membro` (PK), `nome_completo`, `email_corporativo`, `cpf`, `papel` (*Desenvolvedor*, *Testador*, *Líder Técnico*, *Supervisor*, *Gerente de Produto*), `data_admissao`, `id_squad` (FK).
* **Sprint:** `id_sprint` (PK), `numero_sprint`, `objetivo`, `data_inicio`, `data_fim`, `status`, `id_squad` (FK).
* **Release:** `id_release` (PK), `versao_semantica` (ex: v1.2.0), `data_lancamento`, `notas_release`, `id_projeto` (FK).
* **Tarefa (Issue):** `id_tarefa` (PK), `titulo`, `descricao`, `tipo` (*Feature*, *Bug*, *Teste*, *Melhoria*), `prioridade`, `status` (*To Do*, *Doing*, *Done*), `estimativa_horas`, `id_projeto` (FK), `id_sprint` (FK), `id_release` (FK), `id_membro_responsavel` (FK).

### c) Relacionamentos e Cardinalidades

* **Cliente - Projeto:** Um Cliente pode contratar um ou muitos Projetos (1:N). Um Projeto pertence obrigatoriamente a exatamente um Cliente (1:1).
* **Projeto - Squad:** Um Projeto pode ser atendido por uma ou mais Squads (ao longo do tempo ou por módulos) e uma Squad pode atuar em um ou muitos Projetos (N:N).
* **Squad - Membro:** Uma Squad possui muitos Membros (1:N). Um Membro atua em exatamente uma Squad por período (1:1).
* **Squad - Sprint:** Uma Squad planeja e executa muitas Sprints (1:N). Uma Sprint pertence obrigatoriamente a uma única Squad (1:1).
* **Projeto - Release:** Um Projeto possui uma ou muitas Releases ao longo do seu ciclo de vida (1:N). Uma Release pertence a apenas um Projeto (1:1).
* **Projeto - Tarefa:** Um Projeto é composto por muitas Tarefas (1:N). Uma Tarefa pertence obrigatoriamente a um único Projeto (1:1).
* **Sprint - Tarefa:** Uma Sprint contém zero ou muitas Tarefas alocadas em seu backlog (1:N). Uma Tarefa pode estar alocada em no máximo uma Sprint de cada vez, ou nenhuma se estiver no backlog geral (0:1).
* **Release - Tarefa:** Uma Release agrupa uma ou muitas Tarefas finalizadas (1:N). Uma Tarefa pode estar vinculada a no máximo uma Release (0:1).
* **Membro - Tarefa:** Um Membro pode ser responsável por zero ou muitas Tarefas (1:N). Uma Tarefa pode ter zero ou um Membro responsável atribuído (0:1).

### d) Regras de Integridade (Restrições de Negócio)

1. **Unicidade de Liderança Técnica:** Cada Squad deve possuir exatamente um Membro com o papel de *Líder Técnico* ativo por período.
2. **Exclusividade do Gerente de Produto:** Uma Squad não pode possuir mais de um *Gerente de Produto* (Product Manager) ativo simultaneamente.
3. **Vinculação Obrigatória de Tarefas:** Toda Tarefa deve estar obrigatoriamente associada a um Projeto cadastrado antes de ser movimentada ou alocada.
4. **Consistência de Atribuição da Tarefa:** Uma Tarefa só pode ser atribuída a um Membro que pertença à Squad que está atuando no Projeto correspondente ou executando a Sprint daquela Tarefa.
5. **Datas Coerentes de Sprints:** A data de início de uma Sprint deve ser estritamente anterior à sua data de término, e duas Sprints ativas da mesma Squad não podem possuir períodos sobrepostos.
6. **Fechamento de Release:** Uma Release só pode ser marcada como lançada se todas as Tarefas a ela vinculadas estiverem com status *Done* e com seus respectivos testes validados.
7. **Integridade de Documentação Fiscal:** O CNPJ de cada Cliente e o CPF de cada Membro devem ser únicos e válidos no sistema (`UNIQUE`).
=======
Situação que ocorre quando dois desenvolvedores (ou branches) alteram as mesmas linhas de um mesmo arquivo — ou quando um arquivo é excluído em uma branch e modificado em outra — e o Git tenta uni-los. Como o sistema não pode decidir automaticamente qual alteração é a correta sem risco de perda de lógica, ele suspende a operação e solicita que o desenvolvedor resolva manualmente as seções conflitantes antes de concluir a integração.
>>>>>>> 2996c4a04ca188642a74330fcdb32a1133939378
