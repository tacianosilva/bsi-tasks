**Q1.** Um banco de dados é uma coleção organizada de dados relacionados, armazenados de forma que possam ser consultados
utilizados. Já o Sistema Gerenciador de Banco de Dados (SGBD) é um conjunto de programas que permite criar, armazenar,
consultar, alterar e gerenciar os dados de um banco de dados.

Exemplos de bancos de dados são um banco de dados de uma biblioteca, contendo informações sobre livros e usuários, e um banco de
dados de uma loja, contendo informações sobre produtos e clientes. Exemplos de SGBDs são PostgreSQL, MySQL, Oracle Database e
Microsoft SQL Server.

**Q2.** Os principais problemas são:

* **Inconsistência e redundância de dados:** Informações podem ser repetidas em diferentes arquivos, e as cópias dos dados podem
divergir ao longo do tempo.

* **Dificuldade de acesso aos dados:** É necessário desenvolver programas específicos para realizar consultas e acessar os
dados, tornando o processo mais trabalhoso.

* **Isolamento de dados:** Os dados podem estar armazenados em diferentes arquivos e formatos, dificultando a construção de
aplicações que precisem acessar essas informações.

* **Problemas de integridade:** É difícil garantir e adicionar novas restrições de integridade, pois essas regras precisam ser
implementadas diretamente no código das aplicações.

* **Problemas de atomicidade:** É difícil garantir que uma operação seja realizada completamente ou que o sistema retorne ao seu
estado anterior caso alguma etapa da operação falhe.

* **Anomalias no acesso concorrente:** Como os dados podem ser acessados simultaneamente por diferentes programas ou usuários, é
difícil controlar possíveis conflitos entre esses acessos.

* **Problemas de segurança:** Como nem todos os usuários devem ter acesso a todos os dados, é necessário controlar as permissões
de acesso. Em sistemas de arquivos, esse controle pode ser mais difícil de implementar e gerenciar.

**Q3.**

* **Atomicidade:** Garante que uma transação seja executada completamente ou que nenhuma de suas operações seja aplicada. Em
outras palavras, uma transação não pode ser parcialmente concluída.

  **Exemplo:** Em uma transferência bancária, é necessário retirar o valor da conta de origem e adicioná-lo à conta de destino.
  Se ocorrer uma falha durante a operação, todas as alterações devem ser desfeitas.

  **Sem atomicidade:** O dinheiro poderia ser retirado da conta de origem, mas não ser adicionado à conta de destino.

* **Consistência:** Garante que uma transação mantenha o banco de dados em um estado válido, respeitando as regras e restrições
definidas.

  **Exemplo:** Se uma conta possui R$ 500,00 e é realizada uma transferência de R$ 100,00, ao final da operação o saldo deve ser
  atualizado corretamente para R$ 400,00.

  **Sem consistência:** O banco de dados poderia apresentar informações inválidas ou que não respeitem suas regras, como um
  saldo incorreto.

* **Isolamento:** Garante que transações executadas simultaneamente não interfiram umas nas outras de forma incorreta. Cada
transação deve funcionar como se estivesse sendo executada de maneira independente.

  **Exemplo:** Se duas transferências são realizadas ao mesmo tempo a partir da mesma conta, o SGBD deve controlar essas
  operações para que ambas considerem os valores corretos.

  **Sem isolamento:** Uma transação poderia acessar dados que ainda estão sendo modificados por outra, causando resultados
  incorretos.

* **Durabilidade:** Garante que, após uma transação ser concluída com sucesso, suas alterações sejam permanentemente armazenadas
no banco de dados, mesmo que ocorra uma falha no sistema.

  **Exemplo:** Após uma transferência bancária ser confirmada, os novos saldos devem continuar registrados mesmo que o servidor
  seja desligado ou ocorra uma falha no sistema.

  **Sem durabilidade:** Uma transferência poderia ser confirmada, mas suas alterações poderiam ser perdidas após uma falha do
  sistema.

**Q4.**

**a) Queda de energia no meio de uma transferência deixou o valor debitado da conta de origem, mas não creditado na conta de
destino.**

**R: Atomicidade.** A transação foi executada apenas parcialmente: o valor foi debitado da conta de origem, mas não foi
creditado na conta de destino. A atomicidade garante que a transação seja totalmente concluída ou que todas as alterações sejam
desfeitas.

**b) Dois atendentes debitam, ao mesmo tempo, o mesmo saldo de uma conta.**

**R: Isolamento.** Como duas transações estão sendo executadas simultaneamente, o SGBD precisa garantir que uma não interfira
incorretamente na outra. O isolamento evita que as operações concorrentes produzam um resultado inconsistente.

**c) O sistema confirma a operação, mas após reiniciar o servidor o dado foi perdido.**

**R: Durabilidade.** Depois que uma transação é confirmada, suas alterações devem permanecer armazenadas mesmo que ocorra uma
falha ou reinicialização do servidor. Nesse caso, a durabilidade não foi garantida.

**d) Uma transferência que levaria o saldo abaixo do limite permitido é rejeitada pelo banco.**

**R: Consistência.** A transação foi rejeitada porque violaria uma regra ou restrição do banco de dados. A consistência garante
que as transações não deixem o banco de dados em um estado inválido.

**Q5.**

* **Recuperação:** É a capacidade de restaurar os dados para um estado consistente após uma falha, como uma queda de energia ou
erro no sistema. O SGBD gerencia isso por meio de mecanismos como logs de transações, backups e recuperação de dados.

* **Integridade:** Refere-se à garantia de que os dados permaneçam corretos, válidos e consistentes. O SGBD utiliza regras e
restrições, como `PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL` e `UNIQUE`, para impedir a inserção de dados inválidos.

* **Redundância:** Ocorre quando a mesma informação é armazenada mais de uma vez de forma desnecessária. O SGBD pode reduzir a
redundância por meio da organização adequada das tabelas e da normalização do banco de dados.

* **Inconsistência:** Ocorre quando existem diferentes versões de uma mesma informação e elas apresentam valores diferentes. O
SGBD ajuda a evitar esse problema por meio do controle das transações, das restrições de integridade e do gerenciamento
dos acessos concorrentes.

**Q6.**

**a)** Entidades

As principais entidades identificadas no sistema são:

- **Membro:** representa os integrantes das squads, como desenvolvedores, testadores, líderes técnicos, supervisores e gerentes de produto.
- **Squad:** representa as equipes responsáveis pelo desenvolvimento dos projetos.
- **Cliente:** representa as empresas que contratam os serviços de desenvolvimento.
- **Projeto:** representa os projetos desenvolvidos para os clientes.
- **Tarefa:** representa as tarefas (issues) realizadas pelas squads.
- **Sprint:** representa as iterações utilizadas para organizar e planejar as tarefas dos projetos.
- **Release:** representa as versões ou entregas dos projetos.

**b)** Atributos

- **Membro:** `id`, `nome`, `email`, `cargo`.
- **Squad:** `id`, `nome`.
- **Cliente:** `id`, `nome`, `cnpj`, `email`, `telefone`.
- **Projeto:** `id`, `nome`, `descrição`, `status`, `data_inicio`, `data_fim`.
- **Tarefa:** `id`, `nome`, `data_inicio`, `data_termino`, `status`,  `descrição`.
- **Sprint:** `id`, `nome`, `data_inicio`, `data_fim`.
- **Release:** `id`, `versão`, `data_inicio`, `data_fim`.

**c)** Relacionamentos

- **Membro — participa — Squad:** uma squad possui de 1 a N membros, enquanto cada membro participa de exatamente uma squad.
- **Squad — atende — Cliente:** uma squad atende exatamente um cliente, enquanto um cliente pode ser atendido por uma ou várias squads.
- **Squad — realiza — Tarefa:** uma squad realiza de 1 a N tarefas, enquanto cada tarefa é realizada por uma única squad.
- **Cliente — tem — Projeto:** um cliente possui de 1 a N projetos, enquanto cada projeto pertence a um único cliente.
- **Projeto — possui — Sprint:** um projeto possui de 1 a N sprints, enquanto cada sprint pertence a um único projeto.
- **Projeto — possui — Release:** um projeto possui de 1 a N releases, enquanto cada release pertence a um único projeto.
- **Sprint — contém — Tarefa:** uma sprint pode conter várias tarefas, e uma tarefa pode estar associada a várias sprints.

**d)** Regras de integridade

O banco de dados deve garantir as seguintes regras:

- Cada membro deve estar vinculado a exatamente uma squad.

- Cada squad deve possuir pelo menos um membro.

- Cada squad deve atender exatamente um cliente.

- Um cliente pode ser atendido por uma ou várias squads.

- Cada tarefa deve estar vinculada a exatamente uma squad.

- Cada squad deve realizar pelo menos uma tarefa.

- Cada projeto deve pertencer a exatamente um cliente.

- Cada cliente deve possuir pelo menos um projeto.

- Cada sprint deve pertencer a exatamente um projeto.

- Cada projeto deve possuir pelo menos uma sprint.

- Uma tarefa pode estar associada a uma ou várias sprints, permitindo que uma tarefa não concluída seja transferida para outra sprint.

- Cada release deve pertencer a exatamente um projeto.

- Cada projeto deve possuir pelo menos uma release.

- Os identificadores (`id`) das entidades devem ser únicos, não podendo existir duas entidades do mesmo tipo com o mesmo identificador.

- O CNPJ de um cliente deve ser único, não podendo dois clientes diferentes possuir o mesmo CNPJ.

- As datas de início e término de tarefas e sprints devem ser válidas, de modo que a data de término não seja anterior à data de início.