# Tarefa 01 - Conceitos de Banco de Dados

## Q1. Banco de Dados e SGBD
- Descreva o que é um Banco de Dados e o que é um Sistema Gerenciador de Banco de Dados. Cite exemplos de Bancos de Dados e seus SGBDs.

**Resposta**: Um banco de dados é qualquer organização de dados interrelacionados, armazenados e com contexto. Um SGBD é uma aplicação comercial que gerencia, esquematiza, manipula e armazena os dados. Exemplos: PostgresSQL, MongoDB, Oracle, MariaDB etc

## Q2. Sistemas de Arquivos
- Quais os principais problemas de utilizar Sistemas de Arquivos para armazenagem de dados?

**Resposta**: Os principais problemas são: Operações sobre um mesmo arquivo de dois ou mais programas diferentes podia causa inconsistências, o sistema devia ter um estado anterior para consertar, os dados eram duplicados constantemente, você tinha que saber onde estavam os dados por que cada aplicação tinha seu padrão, além de que qualquer usuário podia ter acesso a dados. Esse e outros problemas que vieram acarretar no surgimento dos SGBDs

## Q3. Propriedades ACID
- Explique as propriedades ACID: atomicidade, consistência, isolamento e durabilidade. Para cada propriedade, descreva um exemplo prático no contexto de uma transferência bancária e explique o que aconteceria se o SGBD não garantisse essa propriedade.

**Resposta**: Essas propriedades são fundamentais para o funcionamento pleno não só de bancos de dados, mas para grande parte das operações de softwares. Para elucidar esses conceitos, vou tratar do seguinte caso: **SGBD Debita os R$ 100 da conta A e deposita o mesmo valor na conta B**
- Atomicidade (Tudo ou nada): Uma transação é uma unidade indivisível, ou as operações rodam, ou o banco não sai de seu estado atual. Se o SGBD falhar nessa parte, pode acontecer que o SGBD debite os 100 reais de uma conta, e, por uma falha subsequente, não deposite o mesmo valor na conta B, fazendo com que o dinheiro sumisse.
- Consistência: Garante que uma transação leve o banco de um estado válido para outro, respeitando regras, restrições e a integridade do sistema. Se o sistema falhasse nessa regra, o SGBD Poderia debitar 100 reais da conta A, mesmo só tendo 10 reais, violando a regra de negócio que diz que não pode ter saldo negativo.
- Isolamento: Garante que múltiplas transações concorrentes ocorram de tal forma que uma não interfira na outra, para a transação 2 ocorrer, a 1 tem que encerrar. Se o SGBD Falhasse nessa operação, o banco poderia sofrer dois débitos de 100 simultâneos, deixando a conta final com um saldo incompatível (Ou negativo)
- Durabilidade: Se a operação já tiver sido feita, ela deve ser permanentemente salva em um meio não-volátil, como SSD ou HDs. Se o sistema falhasse, o SGBD Poderia encerrar uma operação, ela ainda estar na memória RAM e os dados logo voltarem ao estado anterior, ou serem perdidos/corrompidos.

## Q4. Cenários ACID
- Para cada cenário abaixo, indique qual(is) propriedade(s) ACID está(ão) em jogo e justifique sua resposta:

### a) Queda de energia no meio de uma transferência deixou o valor debitado da conta de origem, mas não creditado na conta de destino.

**Resposta**: Atomicidade, pois a operação de débito foi cortada no meio do caminho, fazendo com que o dinheiro sumisse

### b) Dois atendentes debitam, ao mesmo tempo, o mesmo saldo de uma conta.

**Resposta**: Isolamento, pois a operação duplicada pode causar inconsistências. Primeiro uma operação deve ocorrer, depois a outra

### c) O sistema confirma a operação, mas após reiniciar o servidor o dado foi perdido.

**Resposta**: Durabilidade, Pois os dados que estavam na memória primária do servidor foram perdidos, e eles deveriam estar salvos no SSD/HD

### d) Uma transferência que levaria o saldo abaixo do limite permitido é rejeitada pelo banco.

**Resposta**: Consistência, pois as operações devem seguir as regras de negócio (Não deve haver saldo negativo). Portanto, a operação foi rejeitada por ausência de saldo

## Q5. Aspectos tratados por um SGBD
- Um SGBD trata dos seguintes aspectos: recuperação, integridade, redundância e inconsistência. Explique cada um deles e descreva como o SGBD os gerencia.

**Resposta**:

## Q6. Mini-projeto conceitual
- Considere o cenário de uma empresa de desenvolvimento de software que atende outras empresas como clientes. A empresa organiza seu trabalho em squads (equipes) compostas por desenvolvedores, testadores, líder técnico, supervisor e gerente de produto. Cada squad resolve tarefas (issues) e planeja releases, testes e o cronograma de sprints (iterações) dos projetos de cada cliente.

- Sem utilizar SQL, elabore um mini-projeto conceitual do banco de dados dessa empresa, deixando claro: a) As principais entidades envolvidas (clientes, squads, membros, tarefas, projetos, sprints, releases). b) Os principais atributos de cada entidade. c) Os relacionamentos entre as entidades (com a cardinalidade, ex.: "um cliente pode ter vários projetos"). d) Em linguagem natural, as regras de integridade (restrições) que o banco de dados deveria garantir, ex.: "apenas um líder por squad", "toda tarefa precisa estar vinculada a um projeto".


### a) Entidades

**Resposta**: Esses aspectos surgiram no SGBD Justamente por que elas eram o problema principal dos sistemas de arquivos.
- Recuperação (Após falhas): Capacidade do sistema a retornar ao seu estado consistente após uma falha. Ele utiliza o Mecanismo de Log que registra todas as operações antes de gravá-las no disco. Quando o sistema cai, o sistema lê esse log ao reiniciar, e refaz as operações salvas e desfaz as incompletas
- Integridade: Garante que os dados armazenados sejam confiáveis, precisos e sigam as regras de negócio. O sistema gerencia através de limitações de integridade, declaradas no esquema do banco.
- Redundância: Armazenamento duplicado e desnecessário da mesma informação, o SGBD usa a Normalização para mitigar esse problema
- Inconsistência: Ocorre quando cópias diferentes do mesmo dado possuem valores distintos. Quando um dado precisa ser atualizado, ele só é modificado em um único lugar pelo SGBD, mitigando esse problema de inconsistência

### b) Atributos

**Resposta**: As entidades representam objetos do mundo real no qual o sistema precisa guardar informações. As entidades que criei foram:
- Cliente: A empresa externa que contrata os serviços de desenvolvimento.
- Projeto: O produto de software ou serviço que está sendo desenvolvido para um cliente.
- Squad: A equipe multidisciplinar responsável pela execução do trabalho.
- Membro: Os profissionais que trabalham na empresa (desenvolvedores, testadores, líderes, etc.).
- Sprint: O ciclo/iteração de tempo (ex: 2 semanas) onde as tarefas são executadas.
- Tarefa (Issue): A unidade de trabalho que precisa ser feita (um bug, uma nova funcionalidade).
- Release: O pacote de entregas de software gerado a partir de um conjunto de tarefas concluídas e testadas.
Os atributos são as características de cada entidade. Os atributos são:
- Cliente: _ID_Cliente_, Nome_Empresa, CNPJ, Telefone_Contato, Email.
- Projeto: _ID_Projeto_, Nome_Projeto, Descricao, Data_Inicio, Orcamento.
- Squad: _ID_Squad_, Nome_Squad, Foco_Atuacao (ex: mobile, backend).
- Membro: _ID_Membro_, Nome, CPF, Cargo (Dev, QA, Tech Lead, PM, Supervisor), Data_Admissao.
- Sprint: _ID_Sprint_, Numero_Sprint, Data_Inicio, Data_Fim, Objetivo.
- Tarefa (Issue): _ID_Tarefa_, Titulo, Descricao, Status (To Do, Doing, Done), Prioridade, Pontuacao_Estimada (Story Points).
- Release: _ID_Release_, Versao (ex: v1.0.0), Data_Lancamento, Notas_de_Versao.

### c) Relacionamentos e cardinalidades

**Resposta**:
- Cliente e Projeto (1:N): Um Cliente pode ter vários Projetos, mas um Projeto pertence a apenas um Cliente.
- Projeto e Squad (N:M): Um Projeto pode ser atendido por uma ou mais Squads, e uma Squad pode trabalhar em vários Projetos ao longo do tempo.
- Squad e Membro (1:N): Uma Squad possui vários Membros, mas um Membro pertence a apenas uma Squad por vez.
- Projeto e Sprint (1:N): Um Projeto possui várias Sprints cronológicas, mas uma Sprint pertence a apenas um Projeto.
- Sprint e Tarefa (1:N): Uma Sprint contém várias Tarefas, e uma Tarefa pode ser alocada em apenas uma Sprint.
- Membro e Tarefa (1:N): Um Membro (responsável) pode assumir várias Tarefas, mas uma Tarefa é atribuída a apenas um Membro responsável.
- Tarefa e Release (1:N): Uma Release agrupa várias Tarefas concluídas, e uma Tarefa concluída pode fazer parte de apenas uma Release.

### d) Regras de integridade

**Resposta**:
- Liderança Única: Cada Squad deve ter obrigatoriamente apenas um Membro com o cargo de "Líder Técnico" e apenas um "Gerente de Produto (PM)" associados ativos.
- Vínculo de Projeto: Toda Tarefa criada precisa estar obrigatoriamente vinculada a um Projeto existente.
- Consistência de Cronograma: A data de início de uma Sprint deve ser estritamente anterior à sua data de término.
- Unicidade Cadastral: Não podem existir dois Clientes com o mesmo CNPJ, nem dois Membros com o mesmo CPF.
- Fluxo de Status: Uma Tarefa só pode ser vinculada a uma Release se o seu `Status` for igual a "Done" (Concluída).
- Integridade Referencial de Exclusão: Se um Cliente for excluído do sistema, o SGBD deve impedir a ação ou remover em cascata seus Projetos e Tarefas associados para evitar dados órfãos.
