## Q1. O modelo de dados entidade-relacionamento foi desenvolvido para facilitar o projeto de banco de dados, permitindo especificação de um esquema que representa a estrutura lógica geral de um banco de dados. Descreva os três elementos básicos de um Modelo Entidade Relacionamento (MER). 

entidade: São representações do banco de dados referentes a algo do mundo real, seja concreta(pessoa) ou abstrata(ex: pedidos)

atributos: São as características que vão dar personalidade a entidade, os quais, são classificados em simples(entidade-pessoa:nome, cpf, email), compostos(atributo-endereço:rua, número,cidade, simplesmente valorados, que é quando só se pode ter 1 (cpf) e multivalorados, que é quando se pode ter mais de 1(telefone).

relacionamentos: São as relações lógicas que vão ligar uma entidade a outra para construir a estrutura do banco de dados, podendo conter restrições, como cardinalidades, chaves participação e integridade

## Q2. Pesquise sobre as várias notações possíveis para Diagramas ER e cite alguns exemplos de notações diferentes para o mesmo conceito (ex.: cardinalidade, entidade subordinada, etc.). 

Notação de Chen: utiliza de retângulos para representar as entidades, elipses para atributos e losangos para relacionamentos, e N:M para representar muitos para muitos na cardinalidade.

Notação Pé de Galinha (Crow's Foot / IE): Utiliza caixas com colunas para representar as entidades e uma reta que separa o nome da entidade dos atributos, e utiliza símbolos para definir cardinalidades, como 1 barra vertical para representar 1 e 3 ramificações para representar o relacionamento de muitos. 

Notação de Barker: utiliza retângulos com bordas arredondadas para as entidades e os atributos, as cardinalidades são as mesmas da notação pé de galinha. 

Diagramas de Classe UML: serve para representar a estruturação e relações das classes que servem de modelos para objetos. 

## Q3. Construa um Diagrama ER para projetar a base de dados de uma empresa de desenvolvimento de software com outras empresas como clientes. A base de dados não deve conter redundância de dados. O modelo ER deve ser representado com um diagrama usando Mermaid.js. O modelo deve apresentar, ao menos, entidades, relacionamentos, atributos, identificadores e restrições de cardinalidade. O modelo deve ser feito no nível conceitual, sem incluir chaves estrangeiras. a) A empresa presta serviços de desenvolvimento de software para outras empresas (clientes). Cada cliente é identificado por um código, um nome e um e-mail de contato. b) Os funcionários da empresa trabalham em squads (equipes). Cada funcionário é identificado por um código, um nome e um e-mail, e possui um papel na equipe: desenvolvedor, testador, líder técnico, supervisor ou gerente de produto. c) Cada squad é formada por vários funcionários e resolve tarefas (issues). Uma tarefa tem código, descrição, prioridade, situação e uma estimativa em horas. As tarefas pertencem a projetos de um cliente. d) O trabalho é organizado em iterações (sprints). Uma squad planeja releases para seus clientes; uma release agrupa um conjunto de tarefas e passa por testes de validação.


erDiagram


CLIENTE{
int codigo_cliente
String CNPJ
String nome
}




FUNCIONARIO{
int codigo_func 


string nome
string email
string funcao
}




EQUIPE{
int codigo_equipe 
string nome
}








TAREFA{
int codigo_tarefa
string descricao
string prioridade
string situacao
string horas
}




INTERACOES{
int codigo_sprint 
int numero
date data_inicio
date data_fim
}




RELEASE{
int codigo_release 
date data_planejada
string versao
}




PROJETO{
int codigo_projeto 
string nome
}


CLIENTE || -- |{ PROJETO : possui
PROJETO || -- |{ RELEASE : possui
TAREFA  }| -- || RELEASE : possui
TAREFA  }| -- || EQUIPE : possui
EQUIPE  }| -- || RELEASE : possui
EQUIPE  || -- |{ INTERACOES : possui
FUNCIONARIO }| -- || EQUIPE : possui


## Q4. A partir do Diagrama ER da questão anterior, faça o mapeamento para o Modelo Relacional: liste as relações (tabelas), com seus atributos, e identifique as chaves primárias e as chaves estrangeiras de cada relação. 

erDiagram


CLIENTE{
int codigo_cliente PK
String CNPJ
String nome
}




FUNCIONARIO{
int codigo_func PK
int codigo_equipe FK
string nome
string email
string funcao
}




EQUIPE{
int codigo_equipe PK
string nome
}








TAREFA{
int codigo_tarefa PK
int codigo_equipe FK
int codigo_release FK
string descricao
string prioridade
string situacao
string horas
}




INTERACOES{
int codigo_sprint PK
int codigo_equipe FK
int numero
date data_inicio
date data_fim
}




RELEASE{
int codigo_release PK
int codigo_projeto FK
date data_planejada
string versao
}




PROJETO{
int codigo_projeto PK
int codigo_cliente FK
string nome
}


CLIENTE || -- |{ PROJETO : possui
PROJETO || -- |{ RELEASE : possui
TAREFA  }| -- || RELEASE : possui
TAREFA  }| -- || EQUIPE : possui
EQUIPE  }| -- || RELEASE : possui
EQUIPE  || -- |{ INTERACOES : possui
FUNCIONARIO }| -- || EQUIPE : possui




## Q5. Descreva, em linguagem natural, as restrições de integridade referencial que devem ser garantidas no esquema projetado (ex.: "uma tarefa só pode existir vinculada a um projeto de cliente existente", "toda squad deve possuir um líder técnico"). 


* todo projeto deve estar relacionado a um cliente
* toda release deve estar relacionada a um projeto
* não pode existir uma tarefa com codigo_release que não exista na tabela
* Uma release pode conter várias tarefas, mas cada tarefa pertence a uma única release. 
* Todo funcionário deve estar obrigatoriamente vinculado a uma equipe existente 
* Um funcionário só estar participando de no máximo 1 equipe por vez
* Uma tarefa só pode ser atribuída a equipes que existam. 
* Uma equippe só pode existir se tiver funcionários relacionados a ela
