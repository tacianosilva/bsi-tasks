# Tarefa 01 - Conceitos de BD, ACID e SGBD

**Aluno:** Andriel Pereira Nogueira  
**Usuário GitHub:** @Andriel-Nogueira  
**Disciplina:** Banco de Dados  
**Issue Relacionada:** #416

---

## Questão 01: Banco de Dados vs. SGBD

* **Banco de Dados (BD):** É uma coleção organizada de dados logicamente relacionados entre si, estruturados para representar entidades, atributos e relacionamentos do mundo real de forma a permitir o armazenamento, consulta e manipulação eficiente das informações.
* **Sistema Gerenciador de Banco de Dados (SGBD):** É o conjunto de softwares responsáveis por gerenciar o acesso, a segurança, a integridade, a concorrência e a persistência dos dados contidos no Banco de Dados, servindo como uma interface intermediária entre as aplicações/usuários e os arquivos físicos.

### Exemplos de Bancos de Dados e seus SGBDs:
1. **Banco de Dados Relacional da Loja Virtual:** Gerenciado pelo **PostgreSQL** ou **MySQL**.
2. **Banco de Dados Documental (NoSQL) de Redes Sociais:** Gerenciado pelo **MongoDB**.
3. **Banco de Dados em Memória para Caching:** Gerenciado pelo **Redis**.

---

## Questão 02: Problemas do uso de Sistemas de Arquivos para Armazenamento

A utilização de arquivos convencionais (como `.txt`, `.csv` ou planilhas) para gerenciar dados corporativos apresenta severas limitações:

1. **Redundância e Inconsistência de Dados:** As mesmas informações podem ser duplicadas em arquivos diferentes por departamentos distintos, levando a divergências quando atualizadas em um local e não no outro.
2. **Dificuldade no Acesso aos Dados:** Para realizar consultas personalizadas ou relatórios complexos, é necessário escrever novos programas específicos para ler e filtrar os arquivos.
3. **Isolamento de Dados:** Dados espalhados em diferentes arquivos e formatos tornam difícil a integração e extração de métricas consolidadas.
4. **Problemas de Concorrência e Acesso Múltiplo:** Se dois usuários tentarem alterar o mesmo arquivo simultaneamente, pode haver perda de dados ou corrupção do arquivo por falta de controle de travamento (*locking*).
5. **Anomalias de Atomicidade:** Se o sistema falhar no meio de uma gravação em arquivo, o estado intermediário fica gravado sem opção de *rollback* automático.
6. **Problemas de Segurança e Integridade:** É difícil aplicar regras de integridade (ex: proibir valores negativos) e restrições de segurança refinadas por usuário/tabela em nível de sistema operacional.

---

## Questão 03: Propriedades ACID

As propriedades ACID garantem a confiabilidade de transações em SGBDs relacionais.

### 1. Atomicidade (Atomicidade - "Tudo ou Nada")
* **Conceito:** Garante que a transação seja tratada como uma unidade indivisível de trabalho. Ou todas as operações da transação são executadas com sucesso (*commit*), ou o estado do banco é revertido totalmente (*rollback*).
* **Exemplo Prático:** Em uma transferência de R$ 100 de Ana para Bob, ocorre um débito na conta de Ana e um crédito na conta de Bob.
* **Sem a garantia do SGBD:** Se o sistema falhar após o débito na conta de Ana mas antes do crédito na conta de Bob, o dinheiro somaria do sistema (débito mantido sem a contrapartida).

### 2. Consistência (Consistency)
* **Conceito:** Garante que a transação só leve o banco de dados de um estado válido para outro estado válido, respeitando todas as restrições de integridade, chaves e regras de negócio.
* **Exemplo Prático:** Uma regra do banco impede que uma conta fique com saldo negativo abaixo de R$ 0.
* **Sem a garantia do SGBD:** Se uma transferência de R$ 500 for solicitada por alguém que só tem R$ 100, o saldo ficaria -$400, violando as regras do domínio bancário.

### 3. Isolamento (Isolation)
* **Conceito:** Garante que transações simultâneas sejam executadas de forma transparente, como se fossem sequenciais, impedindo que uma transação veja dados intermediários e não confirmados de outra.
* **Exemplo Prático:** Duas transferências simultâneas de R$ 50 são solicitadas na mesma conta que possui R$ 100 de saldo.
* **Sem a garantia do SGBD:** Ocorre a "leitura suja" ou "atualização perdida": ambas as transações leem o saldo inicial de R$ 100 ao mesmo tempo e ambas decrementam R$ 50, resultando em um saldo final de R$ 50 em vez de R$ 0.

### 4. Durabilidade (Durability)
* **Conceito:** Garante que, uma vez que a transação seja confirmada (*commit*), os dados persistirão permanentemente na memória não volátil (disco), resistindo a falhas do sistema, quedas de energia ou reinicializações.
* **Exemplo Prático:** O aplicativo exibe a mensagem "Transferência concluída com sucesso".
* **Sem a garantia do SGBD:** Se o servidor desligar segundos após o confirmação por ter mantido o dado apenas em memória RAM sem gravar no disco (ou log de transações), o valor transferido desapareceria ao religar.

--- 