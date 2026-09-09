# Tarefa 01 - Conceitos de Banco de Dados

## Q1. Banco de Dados e SGBD
- Descreva o que é um Banco de Dados e o que é um Sistema Gerenciador de Banco de Dados. Cite exemplos de Bancos de Dados e seus SGBDs.

**Resposta**: Um banco de dados é qualquer organização de dados interrelacionados, armazenados e com contexto. Um SGBD é uma aplicação comercial que gerencia, esquematiza, manipula e armazena os dados. Exemplos: PostgresSQL, MongoDB, Oracle, MariaDB etc

## Q2. Sistemas de Arquivos
- Quais os principais problemas de utilizar Sistemas de Arquivos para armazenagem de dados?

**Resposta**:

## Q3. Propriedades ACID
- Explique as propriedades ACID: atomicidade, consistência, isolamento e durabilidade. Para cada propriedade, descreva um exemplo prático no contexto de uma transferência bancária e explique o que aconteceria se o SGBD não garantisse essa propriedade.

**Resposta**:

## Q4. Cenários ACID
- Para cada cenário abaixo, indique qual(is) propriedade(s) ACID está(ão) em jogo e justifique sua resposta:

### a) Queda de energia no meio de uma transferência deixou o valor debitado da conta de origem, mas não creditado na conta de destino.

**Resposta**:

### b) Dois atendentes debitam, ao mesmo tempo, o mesmo saldo de uma conta.

**Resposta**:

### c) O sistema confirma a operação, mas após reiniciar o servidor o dado foi perdido.

**Resposta**:

### d) Uma transferência que levaria o saldo abaixo do limite permitido é rejeitada pelo banco.

**Resposta**:

## Q5. Aspectos tratados por um SGBD
- Um SGBD trata dos seguintes aspectos: recuperação, integridade, redundância e inconsistência. Explique cada um deles e descreva como o SGBD os gerencia.

**Resposta**:

## Q6. Mini-projeto conceitual
- Considere o cenário de uma empresa de desenvolvimento de software que atende outras empresas como clientes. A empresa organiza seu trabalho em squads (equipes) compostas por desenvolvedores, testadores, líder técnico, supervisor e gerente de produto. Cada squad resolve tarefas (issues) e planeja releases, testes e o cronograma de sprints (iterações) dos projetos de cada cliente.

- Sem utilizar SQL, elabore um mini-projeto conceitual do banco de dados dessa empresa, deixando claro: a) As principais entidades envolvidas (clientes, squads, membros, tarefas, projetos, sprints, releases). b) Os principais atributos de cada entidade. c) Os relacionamentos entre as entidades (com a cardinalidade, ex.: "um cliente pode ter vários projetos"). d) Em linguagem natural, as regras de integridade (restrições) que o banco de dados deveria garantir, ex.: "apenas um líder por squad", "toda tarefa precisa estar vinculada a um projeto".


### a) Entidades

**Resposta**:

### b) Atributos

**Resposta**:

### c) Relacionamentos e cardinalidades

**Resposta**:

### d) Regras de integridade

**Resposta**:
