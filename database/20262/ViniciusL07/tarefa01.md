# Tarefa 01 - Conceitos de BD, ACID e SGBD

## Questão 01 - Banco de Dados vs. SGBD

### Definições

* **Banco de Dados (BD):** Uma coleção organizada, lógica e estruturada de dados relacionados entre si, projetada para armazenar informações que representam um domínio do mundo real.
* **Sistema Gerenciador de Banco de Dados (SGBD):** Pacote de software com ferramentas especializadas para criar, manipular, consultar, gerenciar a integridade e controlar o acesso a esses bancos de dados.

### Exemplos de Aplicação e SGBDs

| Domínio do Banco de Dados | Tipo de Banco | SGBD Utilizado |
| :--- | :--- | :--- |
| **E-commerce / Vendas** | Relacional (SQL) | `PostgreSQL` ou `MySQL` |
| **Prontuário Hospitalar** | Relacional Corporativo | `Oracle Database` ou `SQL Server` |
| **Catálogo de Streaming** | Não-Relacional (NoSQL Documentos) | `MongoDB` |

---

## Questão 02 - Problemas dos Sistemas de Arquivos

O uso de sistemas de arquivos convencionais (pastas e arquivos como `.txt`, `.csv` ou `.dat`) para armazenar informações críticas gera problemas graves:

1. **Redundância e Inconsistência:** O mesmo dado acaba duplicado em formatos ou locais diferentes. Se um arquivo for atualizado e o outro não, os dados entram em desacordo.
2. **Dificuldade de Acesso:** Qualquer relatório ou busca nova exige a criação de um novo script ou programa de computador para ler e filtrar os dados.
3. **Isolamento dos Dados:** Arquivos gravados em formatos e extensões distintas dificultam cruzamentos e junções de informações.
4. **Problemas de Integridade:** Regras de negócio (ex.: *saldo nunca pode ser menor que zero*) precisam ser programadas manualmente dentro de cada sistema, abrindo brechas para gravações incorretas.
5. **Anomalias de Acesso Concorrente:** Se dois usuários ou programas abrirem e tentarem gravar no mesmo arquivo ao mesmo tempo, dados serão sobrescritos ou corrompidos.
6. **Problemas de Segurança:** Faltam permissões granulares; o sistema geralmente só permite liberar ou bloquear o arquivo inteiro, não permitindo filtrar colunas ou registros confidenciais.

---

## Questão 03 - As Propriedades ACID

As propriedades **ACID** garantem a confiabilidade de transações em um SGBD relacional:

### Atomicidade
* **Conceito:** A transação é tratada como uma unidade única e indivisível. Ou todas as suas operações são concluídas com sucesso, ou nada é gravado (ocorre o *rollback*).
* **Exemplo Bancário:** Transferência de R$ 200 de Alice para Bob. O sistema precisa **debitar** de Alice e **creditar** em Bob.
* **Se o SGBD falhar:** Caso falte energia após o débito em Alice, o dinheiro sumirá da conta dela sem nunca chegar à conta de Bob.

### Consistência
* **Conceito:** A transação deve respeitar rigorosamente todas as restrições, tipos e regras do sistema, levando o banco de dados de um estado válido a outro estado válido.
* **Exemplo Bancário:** Alice possui saldo de R$ 50 e o banco não permite cheque especial. Uma tentativa de saque de R$ 100 é abortada.
* **Se o SGBD falhar:** O banco permitiria o saldo negativo, violando as regras contábeis e gerando registros inválidos.

### Isolamento
* **Conceito:** Transações concorrentes são executadas sem interferir no andamento uma da outra, de modo que o resultado final seja idêntico ao de execuções sequenciais.
* **Exemplo Bancário:** Dois saques simultâneos de R$ 100 acontecem em uma conta conjunta que possui exatamente R$ 100 de saldo.
* **Se o SGBD falhar:** Ambas as operações leriam o saldo de R$ 100 ao mesmo instante e liberariam o saque, resultando em um rombo de saldo (*lost update*).

### Durabilidade
* **Conceito:** Uma vez que a transação é confirmada (*commit*), as alterações tornam-se definitivas e persistem mesmo diante de quedas de energia ou reinicializações do servidor.
* **Exemplo Bancário:** Após o aplicativo exibir o comprovante de transferência realizada, os dados já foram salvos em disco seguro.
* **Se o SGBD falhar:** Uma reinicialização imediata do servidor apagaria o registro da operação, devolvendo o dinheiro para a conta de origem.

---

## Questão 04 - Análise de Cenários ACID

* **a) Queda de energia no meio de uma transferência deixou o valor debitado da conta de origem, mas não creditado na conta de destino.**
  * **Propriedade violada:** **Atomicidade**.
  * **Justificativa:** A operação foi executada pela metade, violando o princípio do "tudo ou nada". O sistema deveria ter desfeito o débito (*rollback*).
* **b) Dois atendentes debitam, ao mesmo tempo, o mesmo saldo de uma conta.**
  * **Propriedade em jogo:** **Isolamento**.
  * **Justificativa:** Trata-se de concorrência simultânea sobre o mesmo registro. O SGBD precisa bloquear ou enfileirar as transações para evitar leitura suja ou perda de atualização.
* **c) O sistema confirma a operação, mas após reiniciar o servidor o dado foi perdido.**
  * **Propriedade violada:** **Durabilidade**.
  * **Justificativa:** Se o cliente recebeu a confirmação do *commit*, o dado deveria ter sido persistido em memória não-volátil (disco/log WAL).
* **d) Uma transferência que levaria o saldo abaixo do limite permitido é rejeitada pelo banco.**
  * **Propriedade garantida:** **Consistência**.
  * **Justificativa:** O sistema interceptou e bloqueou a transação com base nas regras de integridade pré-definidas para a conta.

---

## Questão 05 - Aspectos de Gerenciamento do SGBD

* **Recuperação:**
  * **Definição:** Capacidade do sistema de retornar a um estado consistente após travamentos, falhas de sistema ou falhas de energia.
  * **Como gerencia:** Utiliza **Write-Ahead Logging (WAL)**, onde toda alteração é gravada em um log antes do arquivo de dados final, permitindo rotinas de `redo` (refazer) e `undo` (desfazer).
* **Integridade:**
  * **Definição:** Garantia de que os dados armazenados estejam corretos, válidos e dentro das restrições de negócio.
  * **Como gerencia:** Aplicação forçada de chaves primárias (`PRIMARY KEY`), chaves estrangeiras (`FOREIGN KEY`), restrições de nulidade (`NOT NULL`), checagens (`CHECK`) e tipos de dados.
* **Redundância:**
  * **Definição:** Repetição desnecessária da mesma informação em diferentes tabelas ou campos.
  * **Como gerencia:** Através de técnicas de **normalização** de dados. Quando a redundância é necessária (como em índices para ganho de velocidade), o próprio motor se encarrega de sincronizá-la automaticamente.
* **Inconsistência:**
  * **Definição:** Presença de dados divergentes ou conflitantes para descrever um mesmo registro real.
  * **Como gerencia:** Controla transações simultâneas via mecanismos de concorrência (como travas de leitura/escrita e MVCC) e mantém as restrições relacionais ativas.

---

## Questão 06 - Mini-Projeto Conceitual (Empresa de Software)

### a) Entidades Principais
1. `Cliente`: Empresa contratante dos serviços de software.
2. `Projeto`: Produto de software contratado por um cliente específico.
3. `Squad`: Equipe multidisciplinar de desenvolvimento.
4. `Membro`: Profissional pertencente a uma equipe (desenvolvedores, testadores, líderes, etc.).
5. `Sprint`: Intervalo de tempo delimitado (iteração) para entrega de tarefas.
6. `Tarefa (Issue)`: Demanda ou funcionalidade a ser construída ou corrigida.
7. `Release`: Versão empacotada, homologada e entregue ao cliente.

### b) Atributos por Entidade

* **Cliente:** `id_cliente`, `nome_empresa`, `cnpj`, `email_contato`, `telefone`.
* **Projeto:** `id_projeto`, `nome_projeto`, `descricao`, `data_inicio`, `data_previsao_fim`, `status`.
* **Squad:** `id_squad`, `nome_squad`, `data_criacao`.
* **Membro:** `id_membro`, `nome`, `email`, `cargo_papel` (desenvolvedor, testador, líder técnico, supervisor, gerente de produto), `status_ativo`.
* **Sprint:** `id_sprint`, `numero_sprint`, `data_inicio`, `data_fim`, `meta_sprint`.
* **Tarefa:** `id_tarefa`, `titulo`, `descricao`, `tipo` (bug, feature, melhoria), `prioridade`, `status` (a fazer, em andamento, concluído), `estimativa_horas`.
* **Release:** `id_release`, `versao` (ex.: `v1.2.0`), `data_lancamento`, `notas_versao`.

### c) Relacionamentos e Cardinalidades

| Entidade Origem | Relação | Entidade Destino | Cardinalidade | Descrição |
| :--- | :---: | :--- | :---: | :--- |
| **Cliente** | *possui* | **Projeto** | `1 : N` | Um cliente contrata vários projetos; cada projeto pertence a um único cliente. |
| **Squad** | *aloca* | **Membro** | `1 : N` | Uma squad possui vários membros; cada membro atua em uma squad por vez. |
| **Squad** | *trabalha em* | **Projeto** | `N : M` | Uma squad pode atuar em múltiplos projetos; projetos podem receber mais de uma squad. |
| **Projeto** | *divide-se em* | **Sprint** | `1 : N` | O projeto é organizado em sprints; a sprint pertence a um único projeto. |
| **Sprint** | *contém* | **Tarefa** | `0 : N` | A sprint contém várias tarefas; a tarefa pode ou não estar alocada em uma sprint. |
| **Projeto** | *possui* | **Tarefa** | `1 : N` | Toda tarefa pertence obrigatoriamente a um projeto. |
| **Membro** | *executa* | **Tarefa** | `0 : N` | Um membro pode ser responsável por várias tarefas; uma tarefa tem até um responsável direto. |
| **Release** | *agrupa* | **Tarefa** | `1 : N` | A release agrupa tarefas concluídas; uma tarefa entregue pertence a uma release. |

### d) Regras de Integridade do Sistema

1. **Liderança Exclusiva:** Cada `Squad` deve possuir **exatamente um** `Membro` com a atribuição de Líder Técnico.
2. **Vinculação Obrigatória:** Nenhuma `Tarefa` pode existir de forma isolada; ela deve estar obrigatoriamente vinculada a um `Projeto` ativo.
3. **Consistência de Escopo:** Uma `Tarefa` só pode ser associada a uma `Sprint` que pertença ao mesmo `Projeto` ao qual a tarefa está vinculada.
4. **Unicidade de Versão:** O identificador da `versao` de uma `Release` deve ser único dentro do escopo de um mesmo projeto.
5. **Consistência Cronológica:** A `data_inicio` de uma `Sprint` deve ser estritamente anterior à sua `data_fim`.
6. **Fechamento de Versão:** Uma `Release` só pode ser marcada como lançada quando todas as tarefas vinculadas a ela estiverem com o status "concluído".