# Tarefa 1

## Git e Github: Conceitos Básicos

* **Branches:** São linhas de desenvolvimento paralelas que permitem trabalhar em novas funcionalidades ou correções sem afetar a versão principal (`main`).
* **Pull Request (ou Merge Request):** É uma solicitação formal para integrar as alterações feitas em uma branch (ou fork) de volta para a branch principal do repositório original, permitindo revisão de código.
* **Merge:** Ação de unir o histórico e as alterações de duas branches diferentes.
* **Rebase:** Reescreve o histórico, aplicando os commits da branch atual sobre a versão mais recente da branch de destino, mantendo um histórico linear.
* **Conflitos:** Ocorrem quando alterações conflitantes são feitas nas mesmas linhas de um mesmo arquivo em branches diferentes, exigindo resolução manual.

## Questão 01 - Conceitos de Banco de Dados e SGBD

* **Banco de Dados:** É uma coleção organizada de dados estruturados e relacionados, armazenados de forma persistente para facilitar a consulta, recuperação e atualização de informações.
* **SGBD (Sistema Gerenciador de Banco de Dados):** É o software responsável por gerenciar a criação, manutenção, consulta, segurança e integridade do Banco de Dados, servindo como interface entre o usuário/aplicação e os dados armazenados.

**Exemplos:**
1. **Banco de Dados:** Sistema de Gestão de Vendas / **SGBD:** PostgreSQL (Relacional)
2. **Banco de Dados:** Catálogo de Produtos e Logs / **SGBD:** MongoDB (NoSQL - Documentos)
3. **Banco de Dados:** Sistema Bancário Corporativo / **SGBD:** Oracle Database (Relacional)

# Questão 02

## Questão 02 - Problemas do Uso de Sistemas de Arquivos

1. **Redundância e Inconsistência de Dados:** O mesmo dado pode ser duplicado em vários arquivos e ser atualizado em um local sem que os outros sejam atualizados.
2. **Dificuldade de Acesso:** Exige a escrita de novos programas para cada tipo diferente de consulta ou relatório necessário.
3. **Isolamento de Dados:** Dados dispersos em múltiplos arquivos e formatos dificultam o cruzamento e integração de informações.
4. **Problemas de Atomicidade:** Falhas técnicas durante a atualização de um arquivo deixam o sistema em estado parcialmente modificado.
5. **Anomalias de Acesso Concorrente:** Edições simultâneas por múltiplos usuários podem sobrescrever ou corromper informações.
6. **Problemas de Segurança e Controle de Acesso:** Dificuldade em conceder permissões granulares (por linha, coluna ou tabela) para diferentes usuários.

## Questão 03

### Atomicidade
* **Conceito:** A transação é tratada como uma unidade indivisível ("tudo ou nada"). Ou todas as operações são executadas com sucesso, ou nenhuma é mantida.
* **Exemplo:** Transferência bancária de R$ 100 de A para B (composta por débito em A e crédito em B).
* **Sem a garantia:** Se houver uma falha após o débito em A e antes do crédito em B, o dinheiro sumirá da conta de origem sem chegar à conta de destino.

### Consistência
* **Conceito:** A transação deve levar o banco de um estado válido a outro estado válido, respeitando todas as regras de integridade.
* **Exemplo:** Uma conta não pode ficar com saldo menor que zero se não houver limite de crédito contratado.
* **Sem a garantia:** A conta ficaria com saldo negativo sem autorização, violando as regras do banco.

### Isolamento
* **Conceito:** Transações executadas concorrentemente não devem interferir umas nas outras, comportando-se como se fossem executadas sequencialmente.
* **Exemplo:** Duas transferências simultâneas envolvendo a mesma conta A ocorrem sem que um cálculo de saldo sobrescreva o outro incorretamente.
* **Sem a garantia:** Ocorreriam leituras de dados desatualizados/incompletos e perda de atualizações de saldo.

### Durabilidade
* **Conceito:** Após a confirmação (*commit*) da transação, suas alterações persistem de forma permanente no banco de dados, mesmo em caso de falha de energia ou servidor.
* **Exemplo:** Após a mensagem de "transferência realizada", o novo saldo permanece salvo no disco.
* **Sem a garantia:** Se o servidor reiniciar logo após o comprovante emitido, a transferência poderia sumir e o saldo retornar ao estado antigo.

## Questão 04 - Análise de Cenários ACID

* ** Queda de energia no meio de uma transferência deixou o valor debitado da conta de origem, mas não creditado na conta de destino.**
  * **Propriedade violada:** **Atomicidade**.
  * **Justificativa:** A transação foi executada apenas pela metade. Sem a atomicidade, o sistema não desfez (*rollback*) o débito quando ocorreu a falha.

* ** Dois atendentes debitam, ao mesmo tempo, o mesmo saldo de uma conta.**
  * **Propriedade envolvida:** **Isolamento**.
  * **Justificativa:** Trata-se do controle de concorrência. O isolamento garante que o segundo débito aguarde ou leia o saldo atualizado após a execução do primeiro.

* ** O sistema confirma a operação, mas após reiniciar o servidor o dado foi perdido.**
  * **Propriedade violada:** **Durabilidade**.
  * **Justificativa:** Uma vez realizada a confirmação (*commit*), os dados deveriam estar salvos em meio não volátil de forma permanente.

* ** Uma transferência que levaria o saldo abaixo do limite permitido é rejeitada pelo banco.**
  * **Propriedade atuando:** **Consistência**.
  * **Justificativa:** O SGBD barrou a transação para impedir a violação de uma regra de negócio / restrição de integridade do sistema.

  ## Questão 05 - Aspectos Tratados pelo SGBD

* **Recuperação (*Recovery*):** É a capacidade de restaurar o banco de dados a um estado consistente em caso de falhas de hardware ou software. O SGBD gerencia através de *logs* de transações (técnicas de UNDO/REDO) e *checkpoints*.
* **Integridade (*Integrity*):** Garante a exatidão e confiabilidade dos dados armazenados. O SGBD gerencia aplicando restrições (*constraints*) na criação de tabelas (ex: Chave Primária, Chave Estrangeira, NOT NULL, CHECK).
* **Redundância (*Redundancy*):** É a duplicação desnecessária de dados em vários locais. O SGBD gerencia através do processo de Normalização de Dados, garantindo que cada dado fique em seu devido local.
* **Inconsistência (*Inconsistency*):** Ocorre quando cópias do mesmo dado apresentam valores divergentes. O SGBD gerencia eliminando a redundância e controlando transações através das regras ACID.

## Questão 06 - Mini-Projeto Conceitual (Empresa de Software)

### Entidades Principais
1. **Cliente:** Empresas contratantes.
2. **Projeto:** Projetos desenvolvidos para cada cliente.
3. **Squad:** Equipes multifuncionais.
4. **Membro:** Integrantes da empresa (devs, testadores, líderes, etc.).
5. **Sprint:** Iterações do projeto.
6. **Tarefa (Issue):** Atividades e demandas de desenvolvimento.
7. **Release:** Versões entregáveis do software.

### Atributos das Entidades
* **Cliente:** `id_cliente`, `razao_social`, `cnpj`, `email`.
* **Projeto:** `id_projeto`, `nome`, `descricao`, `data_inicio`.
* **Squad:** `id_squad`, `nome_squad`.
* **Membro:** `id_membro`, `nome`, `email`, `papel` (Dev, Testador, Líder Técnico, Supervisor, Gerente de Produto).
* **Sprint:** `id_sprint`, `numero`, `data_inicio`, `data_fim`, `objetivo`.
* **Tarefa:** `id_tarefa`, `titulo`, `descricao`, `status` (A Fazer, Em Andamento, Concluída), `horas_estimadas`.
* **Release:** `id_release`, `versao`, `data_lancamento`.

### Relacionamentos e Cardinalidades
* **Cliente -> Projeto (1:N):** Um cliente pode ter vários projetos, mas cada projeto pertence a apenas um cliente.
* **Squad -> Membro (1:N):** Uma squad possui vários membros, e cada membro pertence a apenas uma squad por vez.
* **Squad -> Projeto (N:M):** Uma squad pode atuar em vários projetos, e um projeto pode ter várias squads envolvidas.
* **Projeto -> Sprint (1:N):** Um projeto é dividido em várias sprints, e cada sprint pertence a apenas um projeto.
* **Sprint -> Tarefa (1:N):** Uma sprint agrupa várias tarefas, e uma tarefa é planejada para uma sprint.
* **Membro -> Tarefa (1:N):** Um membro pode ser responsável por várias tarefas, e uma tarefa é atribuída a um membro.
* **Projeto -> Release (1:N):** Um projeto possui várias releases, e cada release pertence a um projeto.
* **Release -> Tarefa (1:N):** Uma release inclui várias tarefas concluídas.

### Regras de Integridade (Restrições)
1. Toda squad deve possuir exatamente um membro com a função de "Líder Técnico".
2. Toda tarefa precisa estar obrigatoriamente vinculada a um projeto ativo.
3. Uma tarefa só pode ser atribuída a um membro pertencente à squad alocada naquele projeto.
4. A data de término de uma sprint deve ser estritamente posterior à sua data de início.
5. Uma tarefa só pode ser vinculada a uma release se o seu status for "Concluída".