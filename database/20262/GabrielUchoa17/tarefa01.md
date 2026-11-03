# Tarefa 01 - Conceitos de BD, ACID e SGBD

**Aluno (GitHub):** GabrielUchoa17
**Disciplina:** Banco de Dados - BSI
**Issue relacionada:** #393

---

## Sobre o fluxo de trabalho com Git e GitHub

Antes das respostas, um resumo dos conceitos de versionamento usados nesta entrega.

### Branches (ramos)

Uma **branch** é uma linha independente de desenvolvimento dentro do repositório. Ela
funciona como um ponteiro móvel para um commit; a cada novo commit na branch, o ponteiro
avança. A branch `main` guarda a versão estável do projeto, enquanto branches de
funcionalidade (ex.: `tarefa01/GabrielUchoa17`) isolam um trabalho em andamento sem afetar
a `main`. Isso permite desenvolver, revisar e testar mudanças de forma segura e paralela.

### Pull Request / Merge Request

O **Pull Request** (nome usado no GitHub) ou **Merge Request** (GitLab) é o pedido formal
para incorporar as mudanças de uma branch em outra (tipicamente da *feature branch* para a
`main`). Ele abre espaço para **revisão de código**, discussão, execução de CI/testes
automatizados e registro histórico da decisão. No fluxo com *fork*, o PR parte da branch do
fork do aluno e tem como destino a branch `main` do repositório oficial.

### Merge

O **merge** combina o histórico de duas branches. No *fast-forward*, quando a branch de
destino não avançou, o ponteiro apenas "anda para a frente". Quando as duas branches
divergiram, o Git cria um **commit de merge** com dois pais, preservando o histórico
original de ambas as linhas.

### Rebase

O **rebase** reaplica os commits da sua branch a partir da ponta atual de outra branch,
reescrevendo o histórico e deixando-o linear (sem commit de merge). É útil para atualizar a
feature branch com a `main` mantendo o log limpo. Regra prática: **não fazer rebase de
commits já publicados/compartilhados**, pois isso reescreve os hashes e quebra o histórico
de quem já baixou.

### Conflitos

Um **conflito** ocorre quando o merge ou o rebase encontram alterações incompatíveis na
mesma região de um arquivo (ou arquivo removido de um lado e editado do outro). O Git marca
o trecho com `<<<<<<<`, `=======` e `>>>>>>>`; o desenvolvedor precisa editar o arquivo
escolhendo/combinando as versões, remover os marcadores, dar `git add` no arquivo
resolvido e concluir com `git commit` (merge) ou `git rebase --continue` (rebase).

---

## Q1. Banco de Dados e Sistema Gerenciador de Banco de Dados

**Banco de Dados (BD)** é uma coleção organizada de dados relacionados entre si, que
representam aspectos do mundo real (o *minimundo*) e são armazenados de forma persistente
para atender a um conjunto de aplicações e usuários. Um BD tem um propósito definido, é
estruturado segundo um modelo de dados e busca reduzir redundância e inconsistência.

**Sistema Gerenciador de Banco de Dados (SGBD)** é o software que fica entre os usuários/
aplicações e os dados físicos, permitindo **definir** (esquemas, tipos, restrições),
**construir** (armazenar), **manipular** (consultar, inserir, atualizar, remover) e
**compartilhar** o banco de dados de forma controlada. O SGBD também cuida de segurança,
controle de concorrência, controle de acesso, backup e recuperação, e garante as
propriedades das transações.

De forma resumida: o **banco de dados** é o *conjunto de dados*; o **SGBD** é o *programa
que gerencia* esse conjunto. O conjunto formado por SGBD + banco(s) de dados + aplicações
costuma ser chamado de **Sistema de Banco de Dados**.

### Exemplos

| Banco de dados (o dado em si) | SGBD que o gerencia | Modelo |
|---|---|---|
| Cadastro acadêmico de uma universidade | PostgreSQL, Oracle Database, MySQL/MariaDB, SQL Server | Relacional |
| Catálogo de produtos e pedidos de um e-commerce | PostgreSQL, MySQL | Relacional |
| Coleção de documentos JSON de um app mobile | MongoDB, Couchbase | Documentos (NoSQL) |
| Carrinho de compras / cache de sessão | Redis | Chave-valor (NoSQL) |
| Rede de relacionamentos / recomendação | Neo4j | Grafos (NoSQL) |
| Métricas e séries temporais de sensores IoT | InfluxDB, TimescaleDB | Séries temporais |
| Banco local embarcado em um aplicativo desktop/mobile | SQLite | Relacional embarcado |

> Observação: nomes como "PostgreSQL", "MySQL" e "Oracle" designam, a rigor, os **SGBDs**;
> o *banco de dados* é a base específica que cada organização cria e povoa dentro deles
> (ex.: o banco `siga_ufrn` rodando sobre o SGBD PostgreSQL).

---

## Q2. Problemas de usar Sistemas de Arquivos para armazenar dados

Guardar dados em arquivos comuns (texto, planilhas, arquivos binários próprios) manipulados
diretamente pelos programas de aplicação apresenta várias limitações clássicas:

1. **Redundância e inconsistência de dados.** O mesmo dado é copiado em vários arquivos/
   formatos por equipes diferentes. Atualizar um lugar e esquecer outro gera versões
   divergentes do mesmo fato (ex.: endereço do cliente diferente em dois arquivos).

2. **Dificuldade de acesso aos dados.** Cada nova consulta ("clientes de tal cidade com
   saldo acima de X") exige escrever um novo programa, pois não há uma linguagem de
   consulta declarativa pronta.

3. **Isolamento dos dados.** Dados espalhados em muitos arquivos e formatos diferentes
   dificultam recuperar informações relacionadas de forma integrada.

4. **Problemas de integridade.** As regras de negócio (ex.: "saldo não pode ficar
   negativo") ficam espalhadas no código de cada aplicação. Adicionar novas restrições ou
   garanti-las de forma uniforme é trabalhoso e frágil.

5. **Problemas de atomicidade.** Uma falha (queda de energia, erro) no meio de uma
   operação que envolve vários arquivos pode deixar os dados num estado parcial/
   inconsistente, sem mecanismo automático para desfazer.

6. **Anomalias de acesso concorrente.** Vários usuários/programas escrevendo ao mesmo
   tempo, sem controle de concorrência, podem sobrescrever alterações uns dos outros e
   corromper os dados.

7. **Problemas de segurança e controle de acesso.** É difícil conceder a cada usuário
   acesso só à parte dos dados que lhe cabe; normalmente o controle é "tudo ou nada" no
   nível do arquivo.

8. **Dependência entre programa e dados.** Mudar o formato/layout do arquivo obriga a
   alterar todos os programas que o leem (falta de independência de dados física e
   lógica).

9. **Ausência de backup e recuperação padronizados.** Não há um mecanismo integrado de
   log, checkpoint e restauração a um estado consistente após falhas.

O SGBD surge justamente para resolver esse conjunto de problemas de forma centralizada.

---

## Q3. Propriedades ACID

As transações de um SGBD devem respeitar quatro propriedades, conhecidas pela sigla
**ACID**. O cenário usado nos exemplos é uma **transferência bancária de R$ 100 da conta A
para a conta B**, composta por dois passos: (1) debitar R$ 100 de A e (2) creditar R$ 100
em B.

### Atomicidade (Atomicity)

A transação é uma unidade **indivisível**: ou **todos** os seus passos são efetivados, ou
**nenhum** é (tudo ou nada). Se algo falha no meio, o SGBD faz *rollback* e desfaz o que já
tinha sido feito.

- **Exemplo:** o débito em A é executado; antes do crédito em B, o sistema cai. Na
  recuperação, o SGBD desfaz o débito, e A volta a ter o saldo original.
- **Sem essa propriedade:** o dinheiro sairia de A e nunca chegaria em B — R$ 100
  "desaparecem" do sistema. O estado ficaria permanentemente parcial.

### Consistência (Consistency)

Uma transação leva o banco de um **estado válido a outro estado válido**, respeitando todas
as regras de integridade (restrições de chave, checagens, regras de negócio, invariantes).
O que estava consistente antes continua consistente depois.

- **Exemplo:** invariantes "a soma dos saldos de A e B é constante" e "saldo ≥ 0". Ao
  transferir R$ 100, a transação só efetiva se, ao final, ambas as regras continuarem
  verdadeiras (ex.: A tinha saldo suficiente).
- **Sem essa propriedade:** a transferência poderia deixar A com saldo negativo ou criar/
  destruir dinheiro, violando as regras do negócio e produzindo dados sem sentido.

### Isolamento (Isolation)

Transações executando **concorrentemente** não interferem umas nas outras; o resultado
final é como se elas tivessem rodado em **alguma ordem sequencial** (serializável). Uma
transação não enxerga o estado intermediário de outra.

- **Exemplo:** enquanto a transferência de A para B está em andamento, outra transação
  consulta o saldo total. Com isolamento, ela vê o total **antes** ou **depois** da
  transferência inteira, nunca o instante em que A já foi debitada mas B ainda não foi
  creditada.
- **Sem essa propriedade:** ocorreriam anomalias como *dirty read* (ler dado não
  confirmado), *lost update* (uma atualização sobrescreve a outra) e *non-repeatable read*,
  gerando saldos incorretos.

### Durabilidade (Durability)

Depois que o SGBD **confirma** (commit) a transação, seus efeitos são **permanentes** e
sobrevivem a falhas posteriores (queda de energia, reinício, crash), normalmente por meio
de gravação em disco e *write-ahead log*.

- **Exemplo:** o cliente recebe "transferência concluída". Um segundo depois o servidor é
  desligado na tomada. Ao voltar, o débito em A e o crédito em B continuam registrados.
- **Sem essa propriedade:** a operação confirmada seria perdida no reinício; o cliente
  teria o comprovante, mas o saldo voltaria ao valor anterior.

---

## Q4. Análise de cenários

### a) Queda de energia deixou o valor debitado de A, mas não creditado em B

- **Propriedade em jogo:** **Atomicidade** (e, como consequência, **Consistência**).
- **Justificativa:** a transação (débito + crédito) foi executada pela metade. A
  atomicidade exige "tudo ou nada": o SGBD deveria, na recuperação, desfazer o débito já
  aplicado (*rollback* via log), pois a transação não chegou ao commit. O estado resultante
  também viola a consistência (a soma dos saldos mudou / dinheiro sumiu), mas a causa raiz
  é a falta de atomicidade na recuperação de falha.

### b) Dois atendentes debitam ao mesmo tempo o mesmo saldo

- **Propriedade em jogo:** **Isolamento** (e **Consistência** do resultado).
- **Justificativa:** são duas transações concorrentes sobre o mesmo dado. Sem isolamento
  adequado (bloqueios ou controle de versão), ocorre *lost update*: as duas leem o saldo
  inicial, cada uma subtrai seu valor e grava, e uma sobrescreve a outra — um dos débitos
  "some". Com isolamento serializável, uma transação espera a outra terminar, e os dois
  débitos são aplicados corretamente. O efeito final indevido (saldo maior do que deveria,
  possivelmente negativo) também é uma violação de consistência.

### c) O sistema confirma a operação, mas após reiniciar o servidor o dado foi perdido

- **Propriedade em jogo:** **Durabilidade**.
- **Justificativa:** houve *commit* (a operação foi confirmada ao usuário), portanto seus
  efeitos deveriam ser permanentes. Se um reinício apaga o dado, o SGBD não persistiu de
  forma segura (ex.: faltou *flush* do log/dos dados para armazenamento não volátil antes
  de confirmar). A durabilidade garante que o que foi confirmado resiste a falhas
  posteriores.

### d) Uma transferência que levaria o saldo abaixo do limite permitido é rejeitada

- **Propriedade em jogo:** **Consistência** (com apoio da **Atomicidade**).
- **Justificativa:** existe uma regra de integridade ("saldo não pode ficar abaixo do
  limite"). A transação que violaria essa regra **não é efetivada**: o SGBD aborta e faz
  *rollback*, mantendo o banco em estado válido. Aqui o comportamento está **correto** — é
  exatamente a consistência sendo garantida (a atomicidade assegura que o débito tentado
  seja totalmente desfeito).

---

## Q5. Aspectos tratados pelo SGBD

### Recuperação (Recovery)

Capacidade de trazer o banco de volta a um **estado consistente** após falhas (de
transação, de sistema ou de mídia).

- **Como o SGBD gerencia:** mantém um **log de transações** (*write-ahead logging* — o
  registro do log vai para disco antes da alteração dos dados). Em falhas, executa **UNDO**
  das transações não confirmadas e **REDO** das confirmadas que ainda não tinham sido
  gravadas. Usa **checkpoints** para limitar quanto do log precisa ser reprocessado e
  **backups** + log para recuperação de mídia (disco danificado).

### Integridade (Integrity)

Garantia de que os dados são **corretos, válidos e coerentes** com as regras do minimundo.

- **Como o SGBD gerencia:** aplica **restrições declarativas** — chave primária (unicidade
  e não nulo), **chave estrangeira** (integridade referencial), `NOT NULL`, `UNIQUE`,
  `CHECK`, domínios/tipos — verificadas automaticamente a cada operação. Regras mais
  complexas são impostas por **triggers**, *stored procedures* e pelo controle
  transacional (consistência do ACID). Operações que violam qualquer restrição são
  rejeitadas.

### Redundância (Redundancy)

Repetição desnecessária do mesmo dado em vários lugares, que desperdiça espaço e abre porta
para inconsistência.

- **Como o SGBD gerencia:** promove **projeto de esquema normalizado** (formas normais)
  para que cada fato seja armazenado **uma única vez**; usa **chaves estrangeiras** para
  referenciar dados em vez de copiá-los. Quando alguma redundância é introduzida de
  propósito (desnormalização por desempenho, índices, réplicas, *cache*, visões
  materializadas), o próprio SGBD se encarrega de **manter as cópias sincronizadas**.

### Inconsistência (Inconsistency)

Situação em que cópias ou partes relacionadas dos dados se contradizem (o mesmo cliente com
dois endereços diferentes, saldo que não bate com o extrato).

- **Como o SGBD gerencia:** combina os mecanismos acima — **eliminação da redundância**
  pela modelagem, **restrições de integridade** que impedem estados contraditórios,
  **controle de concorrência** (isolamento) que evita que transações simultâneas gerem
  dados incoerentes, e **recuperação** que descarta efeitos de transações incompletas.
  Assim o banco converge sempre para um único estado consistente.

---

## Q6. Mini-projeto conceitual — Empresa de desenvolvimento de software

Cenário: uma *software house* atende **empresas clientes**, organiza-se em **squads** e
executa **projetos** divididos em **sprints**, com **tarefas**, **testes** e **releases**.

### a) Principais entidades

- **Cliente** — a empresa contratante.
- **Projeto** — trabalho contratado por um cliente.
- **Squad** — equipe responsável por um ou mais projetos.
- **Membro** — pessoa que trabalha na software house (desenvolvedor, testador, líder
  técnico, supervisor, gerente de produto).
- **PapelNoSquad** (associativa) — vínculo de um membro a um squad exercendo um papel.
- **Sprint** — iteração de tempo fixo dentro de um projeto.
- **Tarefa (Issue)** — unidade de trabalho a ser resolvida.
- **Release** — versão entregável do software de um projeto.
- **Teste** — caso/execução de teste associado a tarefas e/ou releases.

### b) Principais atributos

**Cliente**
- `id_cliente` (identificador)
- `razao_social`, `nome_fantasia`
- `cnpj` (único)
- `email_contato`, `telefone`
- `data_inicio_contrato`

**Projeto**
- `id_projeto` (identificador)
- `nome`
- `descricao`
- `data_inicio`, `data_prevista_fim`, `data_fim_real`
- `status` (em análise, ativo, pausado, concluído, cancelado)
- `id_cliente` (cliente dono do projeto)
- `id_squad` (squad responsável)

**Squad**
- `id_squad` (identificador)
- `nome` (único)
- `data_criacao`
- `ativo` (sim/não)

**Membro**
- `id_membro` (identificador)
- `nome_completo`
- `email_corporativo` (único)
- `cargo` (desenvolvedor, testador, líder técnico, supervisor, gerente de produto)
- `data_admissao`
- `ativo` (sim/não)

**PapelNoSquad** (associação Membro–Squad)
- `id_membro`, `id_squad`
- `papel` (desenvolvedor, testador, líder técnico, supervisor, gerente de produto)
- `data_entrada`, `data_saida`
- `alocacao_percentual`

**Sprint**
- `id_sprint` (identificador)
- `id_projeto`
- `numero` / `nome`
- `data_inicio`, `data_fim`
- `objetivo` (meta da sprint)
- `status` (planejada, em andamento, encerrada)

**Tarefa (Issue)**
- `id_tarefa` (identificador)
- `titulo`, `descricao`
- `tipo` (feature, bug, melhoria, débito técnico)
- `prioridade` (baixa, média, alta, crítica)
- `status` (backlog, a fazer, em andamento, em teste, concluída)
- `estimativa` (pontos ou horas)
- `data_abertura`, `data_conclusao`
- `id_projeto` (obrigatório)
- `id_sprint` (opcional — tarefa pode estar no backlog)
- `id_membro_responsavel` (opcional)
- `id_release` (opcional — release em que a tarefa foi entregue)

**Release**
- `id_release` (identificador)
- `id_projeto`
- `versao` (ex.: 1.4.0) — única dentro do projeto
- `data_planejada`, `data_lancamento`
- `status` (planejada, em homologação, lançada)
- `notas_da_versao`

**Teste**
- `id_teste` (identificador)
- `id_projeto`
- `titulo`, `descricao`
- `tipo` (unitário, integração, sistema, aceitação, regressão)
- `resultado` (não executado, passou, falhou, bloqueado)
- `data_execucao`
- `id_membro_executor` (opcional)
- `id_tarefa` (opcional — teste que valida uma tarefa)
- `id_release` (opcional — teste de uma release)

### c) Relacionamentos e cardinalidade

- **Cliente (1) — (N) Projeto**: um cliente pode ter vários projetos; cada projeto pertence
  a exatamente um cliente.
- **Squad (1) — (N) Projeto**: um squad pode ser responsável por vários projetos; cada
  projeto é conduzido por um squad. *(Se a empresa permitir troca de squad ao longo do
  tempo, isso vira uma associativa Projeto–Squad com período de vigência.)*
- **Membro (N) — (M) Squad** por meio de **PapelNoSquad**: um membro pode participar de
  vários squads e um squad tem vários membros; a associação guarda o papel e o período.
- **Projeto (1) — (N) Sprint**: um projeto tem várias sprints; cada sprint pertence a um
  único projeto.
- **Projeto (1) — (N) Tarefa**: um projeto tem várias tarefas; toda tarefa pertence a um
  único projeto.
- **Sprint (1) — (N) Tarefa**: uma sprint contém várias tarefas; uma tarefa está em no
  máximo uma sprint (pode estar em nenhuma).
- **Membro (1) — (N) Tarefa** (responsável): um membro pode ser responsável por várias
  tarefas; cada tarefa tem no máximo um responsável.
- **Projeto (1) — (N) Release**: um projeto tem várias releases; cada release pertence a um
  projeto.
- **Release (1) — (N) Tarefa**: uma release agrupa várias tarefas entregues; uma tarefa é
  associada a no máximo uma release.
- **Projeto (1) — (N) Teste**: cada teste pertence a um projeto.
- **Tarefa (1) — (N) Teste** e **Release (1) — (N) Teste**: um teste pode validar uma
  tarefa e/ou uma release; cada tarefa/release pode ter vários testes.
- **Membro (1) — (N) Teste** (executor): um membro pode executar vários testes.

### d) Regras de integridade (em linguagem natural)

1. Todo **projeto** precisa estar vinculado a exatamente **um cliente**.
2. Toda **tarefa** precisa estar vinculada a exatamente **um projeto**.
3. Toda **sprint** e toda **release** pertencem a exatamente **um projeto**.
4. Se uma tarefa estiver associada a uma **sprint**, essa sprint deve ser **do mesmo
   projeto** da tarefa. A mesma regra vale para a **release** associada à tarefa.
5. Cada **squad** tem **exatamente um líder técnico ativo** por vez ("apenas um líder por
   squad").
6. Um **squad**, quando ativo, deve ter ao menos **um desenvolvedor** e **um testador**.
7. O **papel** exercido em `PapelNoSquad` deve ser compatível com o **cargo** do membro
   (ex.: quem não é testador não entra como testador).
8. Um **membro** não pode ter dois vínculos **ativos** no mesmo squad com o mesmo papel
   (sem sobreposição de períodos).
9. **CNPJ do cliente** e **e-mail corporativo do membro** são **únicos**.
10. A **versão** de uma release é **única dentro do projeto**.
11. Datas devem ser coerentes: `data_inicio` ≤ `data_fim` em sprints, projetos e contratos;
    `data_abertura` ≤ `data_conclusao` na tarefa; `data_planejada` ≤ `data_lancamento` na
    release.
12. Uma **tarefa só pode ter status "concluída"** se tiver `data_conclusao` preenchida e um
    **responsável** definido.
13. Uma **release "lançada"** só é válida se **todas as tarefas associadas** estiverem
    concluídas e seus testes de aceitação/regressão tiverem **resultado "passou"**.
14. O **responsável** por uma tarefa deve ser um membro que participe (via
    `PapelNoSquad`) do squad responsável pelo projeto da tarefa.
15. Não é permitido **excluir** um cliente que possua projetos, nem um projeto que possua
    tarefas/sprints/releases (exclusão restrita ou em cascata controlada).
16. Campos identificadores nunca são nulos; atributos obrigatórios (`nome`, `titulo`,
    `status`, chaves estrangeiras obrigatórias) não aceitam valor nulo.
17. Atributos com lista de valores (`status`, `prioridade`, `tipo`, `resultado`, `papel`,
    `cargo`) só aceitam valores do conjunto pré-definido (domínio).

### Diagrama conceitual (visão textual)

```
CLIENTE ----< PROJETO >---- SQUAD
                 |             |
                 |             |  (Membro N:M Squad via PAPEL_NO_SQUAD)
                 |             |
        +--------+--------+    MEMBRO
        |        |        |     |  \
     SPRINT   RELEASE   TESTE   |   >-- responsável por --< TAREFA
        |        |        |     |
        +---< TAREFA >----+-----+ (executor de) TESTE
```

Legenda: `----<` / `>----` indicam o lado "muitos" do relacionamento (1:N);
`N:M` indica muitos-para-muitos resolvido por entidade associativa.
