# Tarefa 01 - Conceitos de BD, ACID e SGBD

## Q1. O que é um Banco de Dados e o que é um SGBD? Exemplos.

Um **Banco de Dados (BD)** é um conjunto organizado de dados relacionados entre si,
armazenados de forma estruturada para representar informações sobre um domínio do
mundo real. O objetivo é permitir que
esses dados sejam armazenados, consultados, atualizados e compartilhados de forma
eficiente e confiável.

Um **Sistema Gerenciador de Banco de Dados (SGBD)** é o software responsável por
criar, manter e controlar o acesso ao banco de dados. Ele fica entre as aplicações
e os dados propriamente ditos, oferecendo funcionalidades como: definição da
estrutura dos dados (schema), linguagens de consulta (ex.: SQL), controle de
concorrência, segurança, backup/recuperação e garantia das propriedades ACID.

**Exemplos:**

| Exemplo de uso do Banco de Dados | SGBD utilizado |
|---|---|
| Banco de dados de um e-commerce | PostgreSQL, MySQL |
| Banco de dados de uma rede social | MongoDB (NoSQL) |
| Sistema bancário | Oracle Database, SQL Server |
| Aplicativo mobile local | SQLite |
| Cache/sessões de alta performance | Redis |

## Q2. Principais problemas de usar Sistemas de Arquivos para armazenar dados

Antes dos SGBDs, os dados eram armazenados diretamente em arquivos manipulados por
programas. Isso trazia vários problemas, entre eles:

- **Redundância e inconsistência de dados**: o mesmo dado pode ser repetido em
  vários arquivos por aplicações diferentes; se um for atualizado e outro não,
  os dados ficam inconsistentes.
- **Dificuldade de acesso aos dados**: qualquer nova forma de consulta exige
  escrever um novo programa específico.
- **Isolamento dos dados**: os dados ficam espalhados em arquivos com formatos
  diferentes, dificultando integração.
- **Problemas de integridade**: regras de negócio (ex.: "saldo não pode ser
  negativo") precisam ser codificadas manualmente em cada programa, sem garantia
  centralizada.
- **Problemas de atomicidade em falhas**: se o sistema falhar no meio de uma
  operação, não há garantia de que o arquivo fique em um estado consistente.
- **Anomalias de acesso concorrente**: quando múltiplos usuários/programas
  acessam o mesmo arquivo ao mesmo tempo, podem ocorrer condições de corrida e
  sobrescrita de dados.
- **Problemas de segurança**: é difícil definir permissões refinadas (quem pode
  ler/escrever o quê) apenas com permissões de arquivos do sistema operacional.

## Q3. Propriedades ACID (com exemplo de transferência bancária)

Considere uma transferência de R$100 da **Conta A** para a **Conta B**.

### Atomicidade
A transação é tratada como uma unidade indivisível: ou todas as suas operações
são executadas, ou nenhuma é. Na transferência, isso significa debitar da Conta A
**e** creditar na Conta B. As duas ações acontecem juntas ou nenhuma acontece.

*Sem atomicidade*: se o sistema falhar depois do débito e antes do crédito, o
dinheiro "desaparece". Sai da Conta A mas nunca chega à Conta B.

### Consistência
A transação leva o banco de dados de um estado válido para outro estado válido,
respeitando todas as regras/restrições definidas (saldo não pode ficar negativo,
soma total do dinheiro no sistema deve se manter, etc.).

*Sem consistência*: uma transferência poderia deixar o saldo de uma conta negativo
além do limite permitido, ou fazer com que o total de dinheiro do banco "aumente"
ou "diminua" sem explicação, violando as regras de negócio.

### Isolamento
Transações concorrentes não devem interferir umas nas outras; o resultado deve
ser equivalente a executá-las em alguma ordem sequencial. Se duas transferências
envolvendo a Conta A acontecem ao mesmo tempo, uma não deve enxergar um estado
"parcial" da outra.

*Sem isolamento*: dois débitos simultâneos na mesma conta poderiam ler o mesmo
saldo inicial antes de qualquer atualização e ambos descontarem o valor a partir
do saldo antigo, fazendo a conta perder menos dinheiro do que deveria (ou permitir
saldo negativo indevido).

### Durabilidade
Uma vez que a transação é confirmada, suas alterações persistem mesmo em
caso de falhas subsequentes.

*Sem durabilidade*: o sistema poderia confirmar a transferência para o cliente,
mas, se o servidor reiniciasse logo depois, o crédito na Conta B poderia ser
perdido, mesmo o cliente tendo recebido a confirmação de sucesso.

## Q4. Identificação da propriedade ACID em cada cenário

**a) Queda de energia deixou o valor debitado, mas não creditado.**
Propriedade violada: **Atomicidade**. A transação foi executada parcialmente
(só o débito), quando deveria ser "tudo ou nada". Um SGBD com atomicidade
garantida faria o retorno ao débito caso o crédito não pudesse ser concluído.

**b) Dois atendentes debitam ao mesmo tempo o mesmo saldo.**
Propriedade violada: **Isolamento**. O problema é de concorrência: as duas
transações provavelmente leram o mesmo saldo inicial antes de qualquer commit e
cada uma aplicou seu débito sobre esse valor desatualizado,
gerando um resultado diferente do que se fossem executadas em sequência.

**c) O sistema confirma a operação, mas após reiniciar o servidor o dado foi
perdido.**
Propriedade violada: **Durabilidade**. O commit foi confirmado ao usuário, mas
os dados não foram persistidos de forma resistente a falhas, sendo perdidos após o reinício.

**d) Uma transferência que deixaria o saldo abaixo do limite é rejeitada.**
Propriedade em ação: **Consistência**. O SGBD está justamente evitando a
violação da consistência. A regra de negócio "saldo não pode ficar abaixo do
limite" é uma restrição de integridade, ao rejeitar a operação, o SGBD garante
que o banco de dados permaneça em um estado válido.

## Q5. Recuperação, integridade, redundância e inconsistência

- **Recuperação**: capacidade do SGBD de restaurar o banco de dados a
  um estado consistente após falhas. É gerenciada por meio de logs de transação,
  pontos de verificação e mecanismos de backup/restore, permitindo
  refazer transações confirmadas ou desfazer transações
  incompletas.

- **Integridade**: garantia de que os dados armazenados respeitam as regras de
  negócio e as restrições definidas no schema. O SGBD
  gerencia isso validando automaticamente cada operação de escrita contra essas
  restrições e rejeitando operações que as violem.

- **Redundância**: repetição desnecessária do mesmo dado em múltiplos lugares.
  Um pouco de redundância controlada pode ser usada propositalmente, mas, em geral, o SGBD ajuda a minimizá-la por meio de técnicas de
  **normalização** do modelo relacional, centralizando os dados e evitando
  cópias divergentes.

- **Inconsistência**: ocorre quando dados redundantes ficam desatualizados entre
  si. O SGBD
  reduz esse risco centralizando o acesso aos dados, aplicando restrições de
  integridade referencial e, quando bem modelado, eliminando as
  cópias redundantes que poderiam divergir.

## Q6. Mini-projeto conceitual: empresa de desenvolvimento de software

### a) Principais entidades

- **Cliente**
- **Projeto**
- **Squad**
- **Membro**
- **Tarefa**
- **Sprint**
- **Release**

### b) Principais atributos de cada entidade

- **Cliente**: id_cliente, nome, CNPJ, contato, endereço.
- **Projeto**: id_projeto, nome, descrição, data_inicio, data_prevista_fim,
  status.
- **Squad**: id_squad, nome, data_formacao.
- **Membro**: id_membro, nome, e-mail, papel, data_entrada.
- **Tarefa**: id_tarefa, título, descrição, status, prioridade, data_criação, data_conclusão.
- **Sprint**: id_sprint, número, data_início, data_fim, meta.
- **Release**: id_release, versão, data_planejada, data_efetiva, descrição das
  mudanças.

### c) Relacionamentos entre as entidades

- Um **Cliente** pode ter vários **Projetos**, mas cada **Projeto** pertence a
  um único **Cliente** (1:N).
- Um **Projeto** é atendido por uma ou mais **Squads** ao longo do tempo, e uma
  **Squad** pode atender vários **Projetos** (N:N)
- Uma **Squad** é composta por vários **Membros**, e cada **Membro** pertence a
  uma única **Squad** por vez (1:N).
- Um **Projeto** possui várias **Tarefas**, e cada **Tarefa** pertence a um
  único **Projeto** (1:N).
- Uma **Tarefa** é atribuída a um ou mais **Membros**, e um **Membro** pode ter várias **Tarefas**.
   (N:N) se permitir múltiplos responsáveis, (1:N) se apenas um responsável por
  tarefa.
- Uma **Sprint** agrupa várias **Tarefas**, e uma **Tarefa** pertence a uma
  única **Sprint** por vez (1:N).
- Uma **Squad** planeja várias **Sprints**, e cada **Sprint** pertence a uma
  única **Squad** (1:N).
- Um **Projeto** tem várias **Releases**, e cada **Release** pertence a um
  único **Projeto** (1:N).
- Uma **Release** pode agrupar entregas de várias **Sprints**, e uma **Sprint**
  pode contribuir para uma ou mais **Releases** (N:N), dependendo do processo
  adotado.

### d) Regras de integridade (restrições), em linguagem natural

- Apenas um **líder técnico** e um **supervisor** por squad.
- Toda **tarefa** precisa estar vinculada a um **projeto**.
- Toda **tarefa** que está associada a uma **sprint** deve pertencer ao mesmo
  **projeto** atendido pela squad responsável por essa sprint.
- Um **membro** não pode estar em duas **squads** ativas ao mesmo tempo.
- Uma **release** só pode ser marcada como "efetivada" se todas as tarefas
  vinculadas a ela estiverem com status "concluída".
- Uma **sprint** não pode ter data de fim anterior à sua data de início.
- Um **projeto** só pode ser associado a squads que tenham pelo menos um membro
  com o papel de líder técnico definido.
- Um **cliente** só pode ter projetos com status "ativo" se possuir pelo menos
  uma squad alocada no momento.
