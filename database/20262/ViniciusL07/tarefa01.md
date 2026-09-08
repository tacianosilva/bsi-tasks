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