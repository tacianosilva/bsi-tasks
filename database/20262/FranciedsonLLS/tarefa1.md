# Tarefa 01 - Conceitos de Banco de Dados

## Q1. Descreva o que é um Banco de Dados e o que é um Sistema Gerenciador de Banco de Dados. Cite exemplos de Bancos de Dados e seus SGBDs.

### Banco de Dados (BD)

Um Banco de Dados é um conjunto organizado de dados relacionados entre si, que representam informações sobre um determinado domínio do mundo real (uma empresa, uma escola, um hospital, etc.). Esses dados são armazenados de forma persistente, estruturada e não redundante, com o objetivo de serem compartilhados por múltiplos usuários e aplicações, permitindo consulta, inserção, atualização e remoção de forma controlada.

### Sistema Gerenciador de Banco de Dados (SGBD)

O SGBD (em inglês, DBMS - *Database Management System*) é o software responsável por gerenciar o Banco de Dados. Ele funciona como uma camada intermediária entre o banco de dados físico e os usuários/aplicações, oferecendo:

- Uma linguagem para definição e manipulação dos dados (como o SQL);
- Controle de acesso e segurança (usuários, permissões);
- Garantia de integridade e consistência dos dados;
- Controle de concorrência (múltiplos usuários acessando ao mesmo tempo);
- Mecanismos de backup e recuperação em caso de falhas;
- Otimização de desempenho nas consultas.

Ou seja, o Banco de Dados é o conjunto de dados em si, enquanto o SGBD é o software que permite criar, manter e acessar esse conjunto de dados de forma segura e eficiente.

### Exemplos de Bancos de Dados e seus SGBDs

| Banco de Dados (exemplo de uso) | SGBD utilizado |
|---|---|
| Banco de dados de clientes e pedidos de um e-commerce | MySQL |
| Banco de dados acadêmico de uma universidade (alunos, matrículas, disciplinas) | PostgreSQL |
| Banco de dados financeiro de uma instituição bancária | Oracle Database |
| Banco de dados de um sistema corporativo integrado (ERP) | Microsoft SQL Server |
| Banco de dados local de um aplicativo mobile | SQLite |
| Banco de dados de catálogo de produtos com estrutura flexível (documentos) | MongoDB |

Nos exemplos relacionais (MySQL, PostgreSQL, Oracle, SQL Server), os dados são organizados em tabelas com colunas e linhas, seguindo o modelo relacional. Já o MongoDB é um exemplo de SGBD NoSQL, orientado a documentos, usado quando a estrutura dos dados é mais flexível ou variável.

---

## Q2. Quais os principais problemas de utilizar Sistemas de Arquivos para armazenagem de dados?

Antes dos SGBDs, os dados eram armazenados diretamente em arquivos manipulados por programas específicos (sistemas de arquivos). Essa abordagem apresenta diversos problemas quando comparada ao uso de um Banco de Dados:

- **Redundância e inconsistência de dados**: como cada aplicação costuma manter seus próprios arquivos, a mesma informação acaba sendo duplicada em vários lugares (ex.: o endereço de um cliente salvo em um arquivo de vendas e em outro de cobrança). Quando um dado é atualizado em um arquivo e não nos demais, surgem inconsistências.

- **Dificuldade de acesso aos dados**: para buscar uma informação específica, é necessário escrever um novo programa que leia o arquivo do início ao fim, já que não existe uma linguagem de consulta genérica (como o SQL). Qualquer nova necessidade de consulta exige código novo.

- **Isolamento dos dados**: os dados ficam espalhados em vários arquivos, muitas vezes em formatos diferentes, dificultando escrever aplicações que precisam combinar informações de mais de uma fonte.

- **Problemas de integridade**: não há um mecanismo centralizado para garantir regras de negócio (ex.: "o saldo não pode ficar negativo"). Essas restrições ficam espalhadas no código de cada aplicação, e é fácil alguma delas ser esquecida ou implementada de forma diferente em cada programa.

- **Problemas de atomicidade em falhas**: se o sistema falhar (queda de energia, travamento) no meio de uma operação que envolve vários arquivos, não há garantia de que todos os arquivos fiquem em um estado consistente entre si.

- **Anomalias de acesso concorrente**: quando múltiplos usuários/programas acessam e alteram o mesmo arquivo ao mesmo tempo, sem controle, podem ocorrer condições de corrida (*race conditions*), fazendo com que atualizações se percam ou o arquivo fique corrompido.

- **Problemas de segurança**: é difícil definir permissões refinadas (por exemplo, permitir que um usuário veja só parte dos dados de um arquivo). Geralmente o controle de acesso do sistema operacional é tudo ou nada sobre o arquivo inteiro.

O SGBD resolve esses problemas centralizando o armazenamento, oferecendo uma linguagem de consulta padronizada, controle de concorrência, mecanismos de integridade e recuperação de falhas, e controle de acesso granular.

---

## Q3. Explique as propriedades ACID: atomicidade, consistência, isolamento e durabilidade. Para cada propriedade, descreva um exemplo prático no contexto de uma transferência bancária e explique o que aconteceria se o SGBD não garantisse essa propriedade.

As propriedades ACID são um conjunto de garantias que um SGBD deve oferecer para que as transações sejam executadas de forma confiável. O exemplo usado abaixo, em todos os casos, é uma **transferência bancária de R$ 500,00 da Conta A para a Conta B**.

### Atomicidade

**O que é:** a transação é tratada como uma unidade indivisível — ou todas as suas operações são executadas com sucesso, ou nenhuma delas é aplicada (tudo ou nada).

**Exemplo prático:** a transferência envolve duas operações: (1) debitar R$ 500,00 da Conta A e (2) creditar R$ 500,00 na Conta B. A atomicidade garante que essas duas operações aconteçam juntas, como um único bloco.

**Se não houvesse atomicidade:** o sistema poderia debitar o valor da Conta A e, por uma falha, não executar o crédito na Conta B. O dinheiro simplesmente desapareceria do sistema, sem ter sido transferido para lugar nenhum.

### Consistência

**O que é:** toda transação deve levar o banco de dados de um estado válido para outro estado também válido, respeitando todas as regras de integridade e restrições de negócio definidas.

**Exemplo prático:** o sistema não permite que uma transferência deixe o saldo da Conta A abaixo do limite mínimo permitido (por exemplo, saldo negativo sem limite de cheque especial). Se a Conta A tem R$ 300,00 e não tem limite, uma transferência de R$ 500,00 é rejeitada.

**Se não houvesse consistência:** o SGBD poderia permitir que a transação fosse concluída mesmo violando essa regra, deixando o saldo da Conta A em -R$ 200,00 sem autorização, o que quebra uma regra de negócio essencial do banco.

### Isolamento

**O que é:** transações executadas de forma concorrente (ao mesmo tempo) não devem interferir umas nas outras; o resultado final deve ser equivalente ao de executá-las uma após a outra (serialmente).

**Exemplo prático:** enquanto a transferência de R$ 500,00 da Conta A para a Conta B está em andamento, outro atendente tenta fazer um saque de R$ 200,00 na Conta A ao mesmo tempo. O isolamento garante que uma operação só "enxergue" o resultado da outra depois que ela for finalizada (commit), evitando que ambas leiam o mesmo saldo desatualizado.

**Se não houvesse isolamento:** as duas operações poderiam ler o saldo original da Conta A (ex.: R$ 1.000,00) ao mesmo tempo, cada uma calculando seu novo saldo com base nesse valor desatualizado. O resultado final ignoraria uma das duas operações (problema conhecido como *lost update* — atualização perdida), fazendo a conta ficar com um saldo maior do que deveria.

### Durabilidade

**O que é:** uma vez que a transação é confirmada (commit), suas alterações devem persistir no banco de dados de forma permanente, mesmo que ocorra uma falha do sistema (queda de energia, travamento do servidor) logo em seguida.

**Exemplo prático:** o cliente recebe a confirmação de que a transferência foi concluída com sucesso. Mesmo que o servidor do banco caia um segundo depois dessa confirmação, quando o sistema voltar, o débito na Conta A e o crédito na Conta B devem continuar registrados.

**Se não houvesse durabilidade:** o cliente veria a mensagem de "transferência realizada com sucesso", mas se o servidor reiniciasse logo depois, a transação poderia simplesmente sumir do banco de dados, como se nunca tivesse acontecido — mesmo o sistema tendo confirmado a operação.

---

## Q4. Para cada cenário abaixo, indique qual(is) propriedade(s) ACID está(ão) em jogo e justifique sua resposta.

### a) Queda de energia no meio de uma transferência deixou o valor debitado da conta de origem, mas não creditado na conta de destino.

**Propriedade envolvida: Atomicidade**

Justificativa: a transferência é composta por duas operações (débito + crédito) que deveriam ser tratadas como uma única unidade indivisível. Como apenas uma parte da transação foi aplicada (o débito) e a outra não (o crédito), a transação ficou "pela metade". Com a atomicidade garantida, o SGBD teria feito um *rollback* automático do débito assim que detectasse que a transação não foi concluída, restaurando a Conta A ao estado anterior.

### b) Dois atendentes debitam, ao mesmo tempo, o mesmo saldo de uma conta.

**Propriedade envolvida: Isolamento**

Justificativa: esse é um caso clássico de concorrência mal controlada. Os dois atendentes leem o mesmo saldo inicial ao mesmo tempo e cada um calcula seu novo saldo com base nesse valor desatualizado, fazendo com que um dos débitos seja perdido (*lost update*). Com isolamento adequado (por exemplo, usando bloqueios/*locks* ou controle de concorrência multiversão), a segunda operação só enxergaria o saldo já atualizado pela primeira, evitando o conflito.

### c) O sistema confirma a operação, mas após reiniciar o servidor o dado foi perdido.

**Propriedade envolvida: Durabilidade**

Justificativa: uma vez que o SGBD confirma (commit) uma transação, ela deve persistir mesmo diante de falhas subsequentes, como reinicializações ou quedas de energia. O fato de o dado ter sumido após o reinício mostra que a confirmação não foi de fato gravada de forma persistente (por exemplo, em log de transações ou em disco), violando a garantia de durabilidade.

### d) Uma transferência que levaria o saldo abaixo do limite permitido é rejeitada pelo banco.

**Propriedade envolvida: Consistência**

Justificativa: diferente dos itens anteriores, este é um exemplo de ACID funcionando corretamente, não de uma falha. O SGBD está impedindo que a transação leve o banco de dados a um estado inválido (saldo abaixo do limite permitido), respeitando as regras de integridade/negócio definidas. Isso é exatamente o papel da consistência: garantir que toda transação termine em um estado válido, rejeitando aquelas que violariam essa regra.

---

## Q5. Um SGBD trata dos seguintes aspectos: recuperação, integridade, redundância e inconsistência. Explique cada um deles e descreva como o SGBD os gerencia.

### Recuperação (Recovery)

**O que é:** capacidade do SGBD de restaurar o banco de dados a um estado consistente após a ocorrência de falhas, como quedas de energia, travamentos do sistema ou erros de hardware/software.

**Como o SGBD gerencia:** o SGBD mantém um **log de transações**, que registra todas as operações realizadas (antes e depois de cada alteração). Em caso de falha, ele usa esse log para desfazer (*undo*) transações que não foram confirmadas e refazer (*redo*) transações que já haviam sido confirmadas, mas que ainda não tinham sido gravadas fisicamente no banco. Também são usados *checkpoints* periódicos para reduzir o tempo de recuperação.

### Integridade

**O que é:** garantia de que os dados armazenados respeitam as regras e restrições definidas para o domínio da aplicação, evitando dados inválidos ou incoerentes.

**Como o SGBD gerencia:** através de **restrições de integridade** definidas no próprio esquema do banco, como:
- Chave primária (garante que cada registro seja único e identificável);
- Chave estrangeira (garante que relacionamentos entre tabelas sejam válidos);
- Restrições de domínio/`CHECK` (ex.: idade não pode ser negativa);
- `NOT NULL` (campos obrigatórios);
- *Triggers* e regras de negócio adicionais.

O SGBD verifica essas restrições automaticamente antes de aceitar qualquer inserção, atualização ou remoção.

### Redundância

**O que é:** a repetição desnecessária do mesmo dado em múltiplos lugares do banco de dados. É um problema comum em sistemas de arquivos, onde cada aplicação mantém sua própria cópia dos dados.

**Como o SGBD gerencia:** através da **modelagem relacional e normalização**, que organiza os dados em tabelas relacionadas por chaves, evitando que a mesma informação precise ser armazenada em vários lugares. Quando alguma redundância é intencionalmente mantida (por motivos de desempenho), o SGBD oferece mecanismos para manter essas cópias sincronizadas (ex.: *triggers*, *views materializadas*).

### Inconsistência

**O que é:** ocorre quando existem cópias redundantes do mesmo dado e elas divergem entre si — por exemplo, o endereço de um cliente atualizado em um cadastro, mas não em outro.

**Como o SGBD gerencia:** a inconsistência é uma consequência direta da redundância mal controlada. Ao reduzir a redundância através da normalização e centralizar o armazenamento dos dados em um único local lógico (com relacionamentos via chaves estrangeiras), o SGBD evita que existam múltiplas versões divergentes do mesmo dado. Além disso, o controle de transações (com as propriedades ACID) garante que qualquer atualização seja aplicada de forma completa e consistente em todos os pontos relacionados.

---

## Q6. Mini-projeto conceitual do Banco de Dados da empresa de squads

Considere o cenário de uma empresa de desenvolvimento de software que atende outras empresas como clientes, organizando seu trabalho em squads (desenvolvedores, testadores, líder técnico, supervisor e gerente de produto), que resolvem tarefas (issues) e planejam releases, testes e o cronograma de sprints dos projetos de cada cliente.

Sem utilizar SQL, segue o mini-projeto conceitual do banco de dados dessa empresa.

Antes de detalhar o modelo, assumo algumas premissas de negócio para deixar o projeto conceitual sem ambiguidades:

- Cada Squad atende um ou mais Projetos, e cada Projeto é atendido por um único Squad por vez.
- Cada Membro pertence a um único Squad por vez (não trabalha simultaneamente em dois squads).
- Cada Squad tem exatamente um Líder Técnico, um Supervisor e um Gerente de Produto, além de um ou mais Desenvolvedores e Testadores.
- Uma Release agrupa um ou mais Sprints do mesmo Projeto.

### a) Principais entidades

- **Cliente**
- **Projeto**
- **Squad**
- **Membro** (desenvolvedor, testador, líder técnico, supervisor ou gerente de produto)
- **Tarefa** (issue)
- **Sprint** (iteração)
- **Release**

### b) Principais atributos de cada entidade

**Cliente**
- id_cliente (identificador)
- nome/razão social
- CNPJ
- email de contato
- telefone

**Projeto**
- id_projeto
- nome
- descrição
- data_início
- data_prevista_término
- status (em andamento, pausado, concluído)

**Squad**
- id_squad
- nome
- data_formação

**Membro**
- id_membro
- nome
- email
- função/papel (desenvolvedor, testador, líder técnico, supervisor, gerente de produto)
- data_admissão

**Tarefa (issue)**
- id_tarefa
- título
- descrição
- tipo (bug, funcionalidade, melhoria)
- prioridade (baixa, média, alta, crítica)
- status (aberta, em andamento, em teste, concluída)
- data_criação
- data_conclusão

**Sprint (iteração)**
- id_sprint
- número/nome
- data_início
- data_fim
- objetivo/meta da sprint

**Release**
- id_release
- número da versão
- data_planejada
- data_lançamento
- status (planejada, em teste, lançada)

### c) Relacionamentos entre as entidades

- **Cliente – Projeto**: um Cliente pode ter vários Projetos, mas cada Projeto pertence a um único Cliente. *(1:N)*

- **Squad – Projeto**: um Squad pode atender vários Projetos, mas cada Projeto é atendido por um único Squad. *(1:N)*

- **Squad – Membro**: um Squad é composto por vários Membros, mas cada Membro pertence a um único Squad por vez. *(1:N)*

- **Projeto – Tarefa**: um Projeto possui várias Tarefas, mas cada Tarefa pertence a um único Projeto. *(1:N)*

- **Membro – Tarefa**: um Membro pode ser responsável por várias Tarefas, mas cada Tarefa tem um único Membro responsável em um dado momento. *(1:N)*

- **Projeto – Sprint**: um Projeto possui várias Sprints ao longo do tempo, mas cada Sprint pertence a um único Projeto. *(1:N)*

- **Sprint – Tarefa**: uma Sprint pode conter várias Tarefas planejadas, e uma Tarefa pode estar em no máximo uma Sprint por vez (podendo também não estar em nenhuma, quando ainda está no backlog). *(1:N, opcional do lado da Tarefa)*

- **Projeto – Release**: um Projeto possui várias Releases, mas cada Release pertence a um único Projeto. *(1:N)*

- **Release – Sprint**: uma Release agrupa uma ou mais Sprints, e cada Sprint contribui para no máximo uma Release. *(1:N, opcional do lado da Sprint, já que uma sprint em andamento pode ainda não estar associada a nenhuma release)*

### d) Regras de integridade (em linguagem natural)

- Toda Tarefa precisa estar vinculada a um Projeto — não pode existir tarefa "solta" sem projeto associado.
- Todo Projeto precisa estar vinculado a um Cliente — não pode existir projeto sem cliente.
- Cada Squad deve ter apenas um Líder Técnico, um Supervisor e um Gerente de Produto ativos ao mesmo tempo.
- Cada Squad deve ter pelo menos um Desenvolvedor e um Testador.
- Um Membro não pode pertencer a mais de um Squad simultaneamente.
- Uma Tarefa só pode ser marcada como "concluída" se tiver um Membro responsável definido.
- A data de conclusão de uma Tarefa não pode ser anterior à sua data de criação.
- As datas de início e fim de duas Sprints do mesmo Projeto não podem se sobrepor.
- Uma Release só pode ter seu status alterado para "lançada" se todas as Tarefas vinculadas às Sprints dessa Release estiverem com status "concluída".
- Uma Sprint só pode ser associada a uma Release se pertencer ao mesmo Projeto dessa Release.
- Uma Tarefa vinculada a uma Sprint que já faz parte de uma Release "lançada" não pode mais ser removida ou ter seu Projeto alterado, para preservar o histórico da entrega.
