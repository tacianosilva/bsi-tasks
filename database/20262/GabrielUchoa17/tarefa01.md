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
