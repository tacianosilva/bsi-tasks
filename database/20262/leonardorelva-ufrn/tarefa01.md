# Tarefa01 - Conceitos de BD, ACID, SGBD

**Aluno** Leonardo Relva   
**Usuário do GitHub** leonardorelva-ufrn

---

## Questão da Atividade

### Q1. Banco de Dados e SGBD

* **Banco de Dados (BD):** É uma coleção organizada de dados estruturados, que estão relacionados entre si, armazenados eletronicamente para facilitar o acesso, busca e atualização.
* **Sistema Gerenciador de Banco de Dados (SGBD):** É o software responsável por intermediar a comunicação entre as aplicações/usuários e o Banco de Dados físico. Ele gerencia a criação, leitura, atualização, exclusão de dados, além de garantir a segurança, concorrência e integridade.

**Exemplos de BDs e SGBDs:**
1. **SGBD Relacional:** PostgreSQL, MySQL, Oracle Database, Microsoft SQL Server.
2. **SGBD NoSQL (Documentos/Chave-Valor):** MongoDB, Redis, Cassandra.

---

### Q2. Problemas do uso de Sistemas de Arquivos
A utilização de arquivos comuns de sistema operacional (como arquivos de texto ou planilhas) para armazenar dados traz diversos problemas:
1. **Redundância e Inconsistência:** O mesmo dado pode ser duplicado em vários arquivos, gerando discrepâncias se um for atualizado e o outro não.
2. **Dificuldade de Acesso:** Necessidade de escrever código customizado para cada nova consulta ou relatório desejado.
3. **Isolamento e Formatos Incompatíveis:** Dados espalhados em arquivos com formatos diferentes tornam a integração complexa.
4. **Anomalias de Acesso Concorrente:** Múltiplos usuários editando o mesmo arquivo simultaneamente podem sobrescrever e perder dados.
5. **Problemas de Segurança:** Dificuldade em restringir o acesso a partes específicas dos dados por nível de permissão do usuário.

---

### Q3. Propriedades ACID

#### 1. Atomicidade
* **Explicação:** Garante que uma transação seja tratada como uma unidade indivisível ("tudo ou nada"). Ou todas as operações da transação são concluídas com sucesso, ou nenhuma é mantida.
* **Exemplo:** Transferir R$ 100 de A para B envolve duas etapas: debitar RS 100 de A e creditar RS 100 em B. Se a atomicidade for mantida, ambas ocorrem ou ambas falham.
* **Sem SGBD garantindo:** O valor seria debitado da conta A, o sistema falharia antes do crédito, e R$ 100 desapareceriam do sistema bancário sem chegar à conta B.

#### 2. Consistência
* **Explicação:** Garante que a transação leve o banco de dados de um estado válido para outro estado válido, respeitando todas as regras de integridade e restrições (constraints).
* **Exemplo:** O banco possui uma regra onde o saldo de uma conta não pode ser negativo sem limite contratado. A transferência só é aceita se o saldo final respeitar essa restrição.
* **Sem SGBD garantindo:** O cliente transferiria um valor maior do que possui, gerando um saldo negativo inválido violando as regras de negócio do banco.

#### 3. Isolamento
* **Explicação:** Garante que transações executadas concorrentemente (ao mesmo tempo) não interfiram umas nas outras, como se estivessem sendo executadas de forma sequencial.
* **Exemplo:** Se duas transferências ocorrerem simultaneamente na mesma conta, uma esperará o término do cálculo da outra para ler o saldo atualizado.
* **Sem SGBD garantindo:** Duas transações lendo o saldo inicial de R$ 500 juntas poderiam ambas aprovar saques de RS 400 no mesmo segundo, resultando em um saldo final incoerente.

#### 4. Durabilidade
* **Explicação:** Garante que, uma vez confirmada a transação (*commit*), os dados persistirão permanentemente no banco de dados, mesmo em caso de falhas no sistema ou queda de energia.
* **Exemplo:** Após o banco retornar "Transferência realizada com sucesso", a alteração do saldo está gravada em disco de forma definitiva.
* **Sem SGBD garantindo:** A transação seria confirmada na memória RAM e, se houvesse uma queda de energia no servidor em seguida, o dinheiro transferido reapareceria na conta de origem como se nada tivesse acontecido.

---

### Q4. Análise de Cenários e Propriedades ACID

* **a) Queda de energia no meio de uma transferência deixou o valor debitado da conta de origem, mas não creditado na conta de destino.**
  * **Propriedade:** **Atomicidade**.
  * **Justificativa:** Houve uma falha no princípio do "tudo ou nada". A operação parou pela metade e não realizou o *rollback* (desfazer) da primeira etapa.

* **b) Dois atendentes debitam, ao mesmo tempo, o mesmo saldo de uma conta.**
  * **Propriedade:** **Isolamento**.
  * **Justificativa:** Trata-se do controle de concorrência. Uma transação interferiu no estado da outra por não executarem isoladamente.

* **c) O sistema confirma a operação, mas após reiniciar o servidor o dado foi perdido.**
  * **Propriedade:** **Durabilidade**.
  * **Justificativa:** Após o término e confirmação da transação, os dados deveriam ter sido salvos em armazenamento não-volátil permanentemente.

* **d) Uma transferência que levaria o saldo abaixo do limite permitido é rejeitada pelo banco.**
  * **Propriedade:** **Consistência**.
  * **Justificativa:** O SGBD impediu a transação para manter o banco em um estado válido perante as regras de integridade predefinidas.

---

### Q5. Aspectos Tratados pelo SGBD

1. **Recuperação:**
   * **Conceito:** Capacidade de restaurar o banco de dados a um estado consistente após falhas de hardware, software ou energia.
   * **Gerenciamento:** O SGBD utiliza arquivos de *logs de transações* (write-ahead logging) e pontos de verificação (*checkpoints*) para refazer (*redo*) operações confirmadas e desfazer (*undo*) transações incompletas após uma reinicialização.

2. **Integridade:**
   * **Conceito:** Garantia de que os dados inseridos e modificados no banco estejam corretos, precisos e válidos segundo as regras do negócio.
   * **Gerenciamento:** Através do uso de restrições de integridade (*constraints*) definidas no esquema, como chaves primárias (PK), chaves estrangeiras (FK), checagens de tipos de dados (`CHECK`) e declarações de não-nulo (`NOT NULL`).

3. **Redundância:**
   * **Conceito:** Duplicação desnecessária e indesejada dos mesmos dados em diferentes partes do banco de dados.
   * **Gerenciamento:** O SGBD minimiza a redundância por meio de processos de *normalização* do modelo relacional, garantindo que cada dado seja armazenado centralizadamente em um único local e referenciado por chaves.

4. **Inconsistência:**
   * **Conceito:** Situação na qual duas cópias diferentes do mesmo dado possuem valores divergentes, gerando incerteza sobre qual informação é verdadeira.
   * **Gerenciamento:** Controlando estritamente a redundância e utilizando mecanismos de travamento de concorrência (*locks*) para que todas as atualizações sejam propagadas uniformemente em transações ACID.

---