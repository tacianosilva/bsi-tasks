# Tarefa 01 - Conceitos de BD - Jezreel-Asaias

## Q1. Banco de Dados x SGBD

Um **Banco de Dados (BD)** é um conjunto organizado de dados relacionados entre si, armazenados de forma estruturada para representar informações sobre um domínio do mundo real (uma empresa, uma escola, um sistema de vendas, etc.). O banco de dados por si só é apenas a coleção de dados — ele não sabe como ler, gravar ou proteger essas informações.

Um **Sistema Gerenciador de Banco de Dados (SGBD)** é o software responsável por criar, manipular, controlar e proteger esses dados. É o SGBD que oferece uma linguagem de consulta (como SQL), controla o acesso concorrente, garante integridade e segurança, faz backup/recuperação e evita redundância desnecessária.


## Q2. Problemas de usar Sistemas de Arquivos para armazenar dados

- **Redundância e inconsistência de dados**: a mesma informação pode ficar duplicada em vários arquivos diferentes, mantidos por programas distintos, e quando um é atualizado o outro pode não ser, gerando dados inconsistentes.
- **Dificuldade de acesso aos dados**: para cada nova consulta ou relatório é preciso escrever um novo programa, pois não existe uma linguagem de consulta genérica.
- **Isolamento dos dados**: os dados ficam espalhados em vários arquivos com formatos diferentes, dificultando a escrita de programas que precisam combinar informações de fontes distintas.
- **Problemas de integridade**: é difícil (ou trabalhoso) impor regras de negócio (ex.: saldo não pode ficar negativo) sem um mecanismo central que valide essas restrições.
- **Problemas de atomicidade**: se o sistema falhar no meio de uma operação composta por vários passos, não há garantia de que tudo será desfeito ou tudo será concluído, deixando os dados em estado inconsistente.
- **Anomalias de acesso concorrente**: quando vários usuários/programas acessam e alteram os mesmos arquivos ao mesmo tempo, sem controle, podem ocorrer condições de corrida e sobrescrita de dados.
- **Problemas de segurança**: é difícil restringir o acesso apenas a partes específicas dos dados (ex.: permitir que um usuário veja só alguns campos de um arquivo).

## Q3. Propriedades ACID

**A — Atomicidade**: uma transação é tratada como uma unidade "tudo ou nada": ou todas as suas operações são executadas com sucesso, ou nenhuma é.
- *Exemplo*: em uma transferência bancária, debitar R$100 da conta A e creditar R$100 na conta B deve ser uma única operação atômica.
- *Sem essa garantia*: se o sistema falhar depois de debitar de A mas antes de creditar em B, o dinheiro simplesmente desaparece — nem o banco nem o cliente sabem onde ele está.

**C — Consistência**: a transação deve levar o banco de dados de um estado válido para outro estado válido, respeitando todas as regras de integridade (restrições, chaves, saldo mínimo, etc.).
- *Exemplo*: a soma dos saldos de A e B antes e depois da transferência deve ser a mesma; nenhuma regra de negócio (como saldo negativo, se não permitido) pode ser violada.
- *Sem essa garantia*: uma transferência poderia, por exemplo, criar dinheiro do nada ou permitir saldo negativo em uma conta que não tem limite de cheque especial, corrompendo o significado dos dados.

**I — Isolamento**: transações concorrentes não devem interferir umas nas outras; o resultado deve ser o mesmo que se as transações fossem executadas uma de cada vez, em sequência.
- *Exemplo*: se duas transferências para a mesma conta ocorrem ao mesmo tempo, uma não pode "sobrescrever" o efeito da outra ao ler um saldo desatualizado.
- *Sem essa garantia*: pode ocorrer o problema clássico de "leitura suja" ou "atualização perdida", onde uma transação lê um saldo antes de outra terminar de atualizá-lo, causando cálculos errados (ex.: dois saques simultâneos deixando a conta com saldo indevido).

**D — Durabilidade**: uma vez que a transação é confirmada (commit), suas alterações persistem mesmo que o sistema caia logo em seguida (queda de energia, crash do servidor, etc.).
- *Exemplo*: depois que a transferência é confirmada e o cliente recebe o comprovante, o novo saldo deve continuar valendo mesmo se o servidor reiniciar um segundo depois.
- *Sem essa garantia*: o cliente veria a confirmação da operação, mas ao reiniciar o sistema o saldo voltaria ao valor anterior, quebrando a confiança no banco.

## Q4. Identificando propriedades ACID em cada cenário

**a) Queda de energia deixou o valor debitado, mas não creditado.**
→ Viola a **Atomicidade**. A transação era composta por duas operações (débito + crédito) que deveriam ser tratadas como uma unidade indivisível; o sistema executou parte dela e não desfez o restante quando falhou.

**b) Dois atendentes debitam ao mesmo tempo o mesmo saldo.**
→ Viola o **Isolamento** (e, por consequência, pode comprometer a **Consistência**). As duas transações concorrentes não foram devidamente isoladas uma da outra, permitindo que ambas lessem o mesmo saldo inicial e gerassem um resultado incorreto (ex.: só um débito é efetivamente refletido).

**c) O sistema confirma a operação, mas após reiniciar o servidor o dado foi perdido.**
→ Viola a **Durabilidade**. Uma vez que a transação recebeu commit (confirmação), o resultado deveria persistir independentemente de falhas subsequentes no servidor.

**d) Transferência que deixaria o saldo abaixo do limite é rejeitada.**
→ Este é um exemplo de **Consistência sendo corretamente garantida** (não violada): o SGBD aplicou uma regra de integridade e impediu que o banco de dados chegasse a um estado inválido.

## Q5. Aspectos tratados pelo SGBD

- **Recuperação (recovery)**: capacidade do SGBD de restaurar o banco de dados a um estado consistente após falhas (queda de energia, crash de disco, erro de software). É feita através de logs de transações, checkpoints e backups, permitindo refazer (redo) ou desfazer (undo) operações.
- **Integridade**: conjunto de regras (restrições de chave primária/estrangeira, domínios de valores, regras de negócio) que o SGBD impõe para garantir que os dados armazenados sejam válidos e façam sentido, rejeitando operações que as violem.
- **Redundância**: repetição desnecessária da mesma informação em múltiplos lugares. O SGBD ajuda a reduzi-la através de um projeto de banco de dados normalizado, onde cada dado é armazenado preferencialmente uma única vez e referenciado (não copiado) quando necessário.
- **Inconsistência**: ocorre quando cópias redundantes de um mesmo dado não são atualizadas simultaneamente, gerando divergência entre elas. O SGBD combate isso centralizando o controle dos dados e, quando a redundância é controlada (ex.: em replicação), sincronizando as cópias automaticamente.

## Q6. Mini-projeto conceitual — Empresa de desenvolvimento de software

### a) Principais entidades
- **Cliente**
- **Projeto**
- **Squad**
- **Membro** (desenvolvedor, testador, líder técnico, supervisor, gerente de produto)
- **Tarefa** (issue)
- **Sprint**
- **Release**

### b) Atributos principais de cada entidade

- **Cliente**: id, nome, razão social, contato, e-mail
- **Projeto**: id, nome, descrição, data de início, status, cliente (relacionado)
- **Squad**: id, nome, data de formação
- **Membro**: id, nome, papel/função (dev, testador, líder técnico, supervisor, gerente de produto), e-mail, squad (relacionado)
- **Tarefa (issue)**: id, título, descrição, status (aberta/em andamento/concluída), prioridade, projeto (relacionado), sprint (relacionado), responsável (membro relacionado)
- **Sprint**: id, número/nome, data de início, data de fim, projeto (relacionado)
- **Release**: id, versão, data de publicação, projeto (relacionado), notas de release

### c) Relacionamentos e cardinalidades

- Um **cliente** pode ter vários **projetos**, mas cada **projeto** pertence a um único **cliente** (1:N).
- Um **projeto** pode ser atendido por uma ou mais **squads** ao longo do tempo, e uma **squad** pode atender vários **projetos** (N:N).
- Uma **squad** possui vários **membros**, e cada **membro** pertence a uma única **squad** por vez (1:N).
- Um **projeto** possui vários **sprints**, e cada **sprint** pertence a um único **projeto** (1:N).
- Um **projeto** possui várias **releases**, e cada **release** pertence a um único **projeto** (1:N).
- Uma **sprint** contém várias **tarefas**, mas uma **tarefa** pertence a uma única **sprint** por vez (1:N).
- Uma **tarefa** pertence a um único **projeto** (1:N entre projeto e tarefa).
- Uma **tarefa** é atribuída a um **membro** responsável, mas um **membro** pode ter várias **tarefas** atribuídas (1:N).
- Uma **release** pode agrupar várias **tarefas** concluídas (as que entraram naquela versão), e uma **tarefa** pode estar associada a uma release (N:N, se uma tarefa puder aparecer em mais de uma release por retrabalho, ou 1:N se for simplificado).

### d) Regras de integridade (em linguagem natural)

- Apenas um **líder técnico** por squad.
- Apenas um **supervisor** por squad.
- Toda **tarefa** precisa estar vinculada a um **projeto**.
- Toda **tarefa** deve ter um **responsável** (membro) definido antes de entrar em uma sprint.
- Um **membro** só pode estar vinculado a uma **squad** por vez.
- Uma **sprint** não pode ter data de fim anterior à data de início.
- Uma **release** só pode ser publicada se todas as tarefas vinculadas a ela estiverem com status "concluída".
- Um **projeto** só pode ser criado se já existir um **cliente** associado a ele.
- O **nome do cliente** deve ser único no sistema (não pode haver dois clientes cadastrados com o mesmo nome).