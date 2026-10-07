### a) Entidades principais

As principais entidades seriam:

- **Cliente**
- **Projeto**
- **Squad**
- **Membro**
- **Tarefa**
- **Sprint**
- **Release**

### b) Principais atributos

#### Cliente

id_cliente
nome
CNPJ
email
telefone

#### Projeto

id_projeto
nome
descrição
data_inicio
data_fim
status

#### Squad

id_squad
nome
descrição
data_criação

#### Membro

id_membro
nome
email
cargo
data_entrada

#### Tarefa

id_tarefa
título
descrição
status
prioridade
data_criação
data_conclusão

#### Sprint

id_sprint
nome
data_inicio
data_fim
objetivo
status

#### Release

id_release
versão
data_prevista
data_lançamento
status

### c) Relacionamentos e cardinalidades

Cliente → Projeto: um cliente pode possuir vários projetos, mas cada projeto pertence a um cliente.
1:N
Projeto → Squad: um projeto pode utilizar um ou vários squads, e um squad pode atuar em um ou vários projetos.
N:N
Squad → Membro: um squad possui vários membros, e um membro pode participar de um ou vários squads ao longo do tempo.
N:N
Projeto → Tarefa: um projeto possui várias tarefas, mas cada tarefa pertence a um projeto.
1:N
Sprint → Tarefa: uma sprint pode conter várias tarefas, e uma tarefa pode estar associada a uma sprint.
1:N
Projeto → Sprint: um projeto possui várias sprints, mas cada sprint pertence a um projeto.
1:N
Projeto → Release: um projeto pode possuir várias releases, mas cada release pertence a um projeto.
1:N
Release → Tarefa: uma release pode conter várias tarefas, e uma tarefa pode ser incluída em uma release.
1:N

### d) Regras de integridade

O banco de dados deveria garantir que:

Todo projeto deve estar vinculado a um cliente.
Um cliente pode possuir vários projetos.
Toda tarefa deve estar vinculada a um projeto.
Toda sprint deve pertencer a um projeto.
Toda release deve pertencer a um projeto.
Um squad deve possuir pelo menos um membro.
Cada squad deve possuir apenas um líder técnico responsável.
Um membro não pode ocupar dois cargos incompatíveis dentro do mesmo squad.
A data de término de uma sprint não pode ser anterior à sua data de início.
Uma tarefa concluída deve possuir status compatível com sua conclusão.
Uma release não pode ser lançada antes de sua data de início do projeto.
Clientes, projetos, squads e membros devem possuir identificadores únicos.
Não devem existir tarefas, sprints ou releases vinculadas a projetos inexistentes.