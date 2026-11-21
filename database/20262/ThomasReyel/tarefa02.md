## Questão 1
**Resposta:**

Entidade: É um objeto que existe e é parte do negócio seja ele um objeto real ou abstrato (ex: carro ou venda). Uma entidade é um conjunto de atributos

Atributos: São características comuns a instâncias das entidades. São divididas em 2 tipos
- Simples: É atômico (ex: Idade: numérico; Nome: cadeia de caracteres).
- Composto: Contém sub atributos que compõem o atributo (ex: Endereço: (rua, número, bairro, cidade)).

Relacionamento: são a forma e a quantidade na qual as entidades se relacionam entre si. pra ver a cardinalidade sempre se pergunte "1 instância dessa está em quantas instâncias da outra". OBS: Na cardinalidade a relação só é total quando não existe a opção de uma instância de relacionar. E parcial se possuir a opção de uma instância se relacionar.

## Questão 2
**Resposta:**

- Notação de Chen: Criada por Peter Chen (o pioneiro do modelo), utiliza formas geométricas distintas para cada elemento.
- Notação Pé de Galinha (Crow's Foot): Focada na legibilidade, posiciona os atributos dentro do bloco da entidade e utiliza símbolos 
na extremidade das linhas. Essa é a notação utilizada no mermaid, por exemplo.
- Notação UML: Adaptada da orientação a objetos, utiliza caixas de classes para representar entidades e multiplicidades numéricas.

## Questão 3
**Resposta: **

```mermaid
erDiagram

CLIENTE{

  int id
  string código
  string nome
  string email
}

FUNCIONÁRIO{

  int id
  string código
  string nome
  string email
  string função
}

TAREFA{

  int id
  string código
  string descrição
  string prioridade
  string situação
  string horas
}

SPRINT {

  int id
  int numero
  date data_inicio
  date data_final
}

RELEASE {

  int id
  string versão
  date data_planejada
}
EQUIPE{

  int id
  string nome
}

PROJETO{

  int id
  string código
  date data_inicio
  date data_final
}

FUNCIONÁRIO }|--|| EQUIPE : trabalha
TAREFA }|--|| EQUIPE : resolve
TAREFA }|--|| PROJETO : pertence
EQUIPE ||--|{ SPRINT : possui
TAREFA }|--|| RELEASE : agrupa
RELEASE }|--|| PROJETO : possui
CLIENTE ||--|{ PROJETO : possui
SPRINT ||--|{ TAREFA : contém
PROJETO ||--|{ SPRINT : possui
```

## Questão 04
**Resposta:**

```mermaid
erDiagram

CLIENTE{
  int id PK
  string código
  string nome
  string email
}

FUNCIONÁRIO{
  int id PK
  int id_equipe FK
  string código
  string nome
  string email
  string função
}

TAREFA{
  int id PK
  int id_equipe FK
  int id_projeto FK
  int id_release FK
  int id_sprint FK
  string código
  string descrição
  string prioridade
  string situação
  string horas
}

SPRINT {
  int id PK
  int id_equipe FK
  int id_projeto FK
  int numero
  date data_inicio
  date data_final
}

RELEASE {
  int id PK
  int id_projeto FK
  string versão
  date data_planejada
}

EQUIPE{
  int id PK
  string nome
}

PROJETO{
  int id PK
  int id_cliente FK
  string código
  date data_inicio
  date data_final
}

FUNCIONÁRIO }|--|| EQUIPE : trabalha
TAREFA }|--|| EQUIPE : resolve
TAREFA }|--|| PROJETO : pertence
EQUIPE ||--|{ SPRINT : possui
TAREFA }|--|| RELEASE : agrupa
RELEASE }|--|| PROJETO : possui
CLIENTE ||--|{ PROJETO : possui
SPRINT ||--|{ TAREFA : contém
PROJETO ||--|{ SPRINT : possui
```

## Questão 05
**Resposta:**

- Um cliente não pode ser excluído se ainda houver projetos ativos vinculados a ele.
- Uma tarefa não pode ser excluída se já estiver associada a uma release publicada.
- Uma release só pode ser publicada se todas as tarefas vinculadas a ela estiverem concluídas.
- Toda squad deve ter exatamente um líder técnico e um gerente de produto.
- Um funcionário só pode estar em uma equipe por vez.
- Um sprint deve ter data de início anterior à data de término.
- uma tarefa só pode existir vinculada a um projeto de cliente existente.
- O id_projeto de TAREFA deve ser consistente com a id_projeto de RELEASE referenciada pela mesma tarefa (ou seja, uma tarefa não pode estar associada a uma release de um projeto diferente do associado a release).
