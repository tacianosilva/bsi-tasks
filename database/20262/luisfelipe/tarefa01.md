Q1
**Banco de Dados (BD)**
Um banco de dados é uma coleção organizada de informações ou dados estruturados armazenados eletronicamente em um sistema computacional. Sua função principal é consolidar registros para que possam ser facilmente acessados, gerenciados, atualizados e consultados.

**Sistema Gerenciador de Banco de Dados (SGBD)**
O SGBD (*Database Management System* - DBMS) é o software responsável por criar, manipular, gerenciar e controlar o acesso ao banco de dados. Ele atua como uma interface entre o banco de dados físico e os usuários ou aplicações, garantindo a segurança das informações, a integridade dos dados, o controle de concorrência e a execução de operações CRUD (Criar, Ler, Atualizar e Deletar).

**Exemplos de SGBDs e Seus Respectivos Modelos**

| SGBD | Tipo / Modelo de Banco de Dados | Linguagem Principal | Casos de Uso Comuns |
| --- | --- | --- | --- |
| **PostgreSQL** | Relacional (SQL) | SQL / PL/pgSQL | Sistemas empresariais, análise de dados e geoprocessamento |
| **MySQL** | Relacional (SQL) | SQL | Aplicações web, plataformas de e-commerce e WordPress |
| **MongoDB** | Não-relacional (NoSQL - Documentos) | MQL (JSON/BSON) | Aplicações com esquemas flexíveis, Big Data e APIs |
| **Redis** | Não-relacional (NoSQL - Chave-Valor) | Comandos Redis | Mecanismos de *cache*, gerenciamento de sessões e filas |
| **Oracle Database** | Relacional (SQL) | SQL / PL/SQL | Ambientes corporativos de grande porte e sistemas bancários |
| **SQLite** | Relacional Embutido (SQL) | SQL | Aplicativos móveis (Android/iOS) e navegadores web |
Q2. 
Quais os principais problemas de utilizar Sistemas de Arquivos para armazenagem de dados?
Antes do surgimento dos SGBDs, os dados eram mantidos diretamente em arquivos do sistema operacional. As principais limitações dessa abordagem incluem:

Redundância e Inconsistência de Dados: O mesmo dado pode ser duplicado em vários arquivos de diferentes formatos. Quando um dado é alterado em um local e não nos outros, ocorre a inconsistência de dados.

Dificuldade no Acesso aos Dados: Consultar informações exige a escrita de programas de computador específicos em linguagens de programação. Não há uma linguagem de consulta declarativa (como o SQL).

Isolamento dos Dados: Como os dados estão espalhados em vários arquivos com formatos diferentes, torna-se complexo escrever novas aplicações para extrair dados combinados.

Problemas de Integridade: As regras de negócio (como "o saldo não pode ser negativo") precisam ser codificadas manualmente em cada programa de aplicação. Se a regra mudar, todos os programas precisam ser atualizados.

Acesso Concorrente e Anomalias: Se múltiplos usuários ou programas tentarem atualizar o mesmo arquivo ao mesmo tempo, dados podem ser sobrescritos ou corrompidos, pois sistemas de arquivos não possuem controle refinado de concorrência.

Problemas de Segurança: Dificuldade em conceder permissões granulares de acesso a partes específicas dos dados para usuários distintos.

Dificuldade de Recuperação de Falhas: Se o sistema falhar (ex.: queda de energia) durante a escrita de um arquivo, o arquivo pode ficar num estado parcial ou corrompido, sem um mecanismo automático de rollback (restauração).

Q3. Explique as propriedades ACID
As propriedades ACID garantem que as transações em um banco de dados sejam processadas de forma confiável.

1. Atomicidade (Atomicity)
Conceito: A regra do "tudo ou nada". Uma transação é tratada como uma unidade de trabalho indivisível. Ou todas as operações da transação são executadas com sucesso, ou nenhuma é mantida no banco.

Exemplo Prático (Transferência Bancária): Transferir R$ 100 de A para B envolve duas etapas: debitar R$ 100 de A e creditar R$ 100 em B. Se a transação iniciar, ambos os passos devem ser efetuados.

Sem a Garantia: Se o sistema falhar após o débito em A e antes do crédito em B, os R$ 100 sumiriam da conta de A sem chegar na conta de B.

2. Consistência (Consistency)
Conceito: A transação deve levar o banco de dados de um estado válido a outro estado válido, respeitando todas as regras, restrições e invariantes do sistema (restrições de integridade, chaves primárias/estrangeiras, etc.).

Exemplo Prático (Transferência Bancária): A soma total dos saldos das contas A e B antes da transferência deve ser exatamente igual à soma total dos saldos após a transferência.

Sem a Garantia: O banco aceitaria saldo negativo na conta de origem caso a regra do banco proibisse saldo negativo, criando dinheiro "do nada" ou violando regras do negócio.

3. Isolamento (Isolation)
Conceito: Transações concorrentes devem ser executadas de modo que o resultado final seja idêntico ao de uma execução sequencial (uma após a outra). O estado intermediário de uma transação não deve ser visível para outras transações em andamento.

Exemplo Prático (Transferência Bancária): Se A transfere dinheiro para B ao mesmo tempo que C consulta o saldo de A, C deve ver o saldo de A antes da transferência ou depois de finalizada, mas nunca um saldo intermediário inconsistente.

Sem a Garantia: Duas transferências simultâneas poderiam ler o mesmo saldo inicial da conta de A, sobrescrevendo a alteração uma da outra (leitura suja ou atualização perdida).