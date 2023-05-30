# __Tarefa 02 -  Modelo Relacional e Regras de Conversão__

* __Nome__: Gabriel José de Aquino Santos.
* __Github__: gbrl08snts
* __Email:__ gabriel.aquino.069@ufrn.edu.br

## __Questões__

### __Letra A__

* __O Modelo Relacional__ é uma forma de representar e organizar os dados em forma de tabelas(relações). Uma tabela tem um nome único e 
em sua composição linhas(tuplas) e colunas(atributos). As colunas terão um nome único e todos os valores armazenados em uma coluna tem o 
mesmo tipo de dado. As tabelas do MR se relacionam umas com as outras por meio de chaves primárias e estrangeiras. Ademais o MR tem 
operações que possibilitam a manipulação das informações guardadas em tabela: Seleção, Projeção, Junção, União, Intersecção. Portanto o 
MR é um modelo muito simples, minimalista, confiável e flexivel, sendo então muito útil em mostrar relacionamentos complexos entre 
informações.

### __Letra B__

* __Integridade de Chave:__
  - Toda tupla tem um conjunto de atributos que a identifica de maneira única na relação.
* __Integridade de Entidade:__
  - Nenhum valor de chave primária poderá ser NULO.
* __Integridade Referencial:__
  - Uma relação pode ter um conjunto de atributos que contém valores com mesmo domínio de um conjunto de atributos que forma a chave 
  primária de uma outra relação. Este conjunto é chamado chave estrangeira.

### __Letra C__

* __Entidades:__ Toda entidade do Modelo Entidade Relacional (MER) será transformada em uma tabela no MR. Os nomes das tabelas serão os 
nomes de cada entidade e os atributos do MER serão as colunas de uma tabela no MR.

* __Atributos:__ Todos os atributos de uma entidade no MER será traduzida em coluna na tabela do MR. Os tipos de dados de cada uma das 
colunas será definido através do domínio do atributo do Modelo Entidade Relacional (texto, número inteiro, data, etc.)

* __Chave Primária:__ A primary key da entidade MER será transformada em uma coluna da tabela MR. Essa nova coluna vai ser a primary key 
da nossa tabela MR, garantindo assim q os dados serão únicos.

* __Relacionamentos Um_Para_Muitos:__ Relacionamentos um-para-muitos do MER serão transformados nas chaves estrangeiras MR. Uma primary 
key de uma entidade "um" virá uma chave estrangeira da tabela da entidade "muitos", criando assim a relação entre tabelas.

* __Relacionamento Muitos_Para_Muitos:__ Relacionamentos muitos-para-muitos do MER serão transformados nas tabelas adicionais, chamadas 
também de tabelas de junção ou associativas do MR. Estas tabelas terão as primary keys das entidades relacionadas e podem armazenar 
outros atributos relacionados.

* __Atributos Multivalorados:__ Uma entidade MER possui atributos multivalorados, eles serão transformados em tabelas 
separadas do MR. Essas tabelas vão possuir uma chave estrangeira ques estará relacionada à chave primária da entidade principal.


