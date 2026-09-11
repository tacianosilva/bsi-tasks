## Q1. O modelo de dados entidade-relacionamento foi desenvolvido para facilitar o projeto de banco de dados, permitindo especificação de um esquema que representa a estrutura lógica geral de um banco de dados. Descreva os três elementos básicos de um Modelo Entidade Relacionamento (MER). 

entidade: São representações do banco de dados referentes a algo do mundo real, seja concreta(pessoa) ou abstrata(ex: pedidos)

atributos: São as características que vão dar personalidade a entidade, os quais, são classificados em simples(entidade-pessoa:nome, cpf, email), compostos(atributo-endereço:rua, número,cidade, simplesmente valorados, que é quando só se pode ter 1 (cpf) e multivalorados, que é quando se pode ter mais de 1(telefone).

relacionamentos: São as relações lógicas que vão ligar uma entidade a outra para construir a estrutura do banco de dados, podendo conter restrições, como cardinalidades, chaves participação e integridade

## Q2. Pesquise sobre as várias notações possíveis para Diagramas ER e cite alguns exemplos de notações diferentes para o mesmo conceito (ex.: cardinalidade, entidade subordinada, etc.). 

Notação de Chen: utiliza de retângulos para representar as entidades, elipses para atributos e losangos para relacionamentos, e N:M para representar muitos para muitos na cardinalidade.

Notação Pé de Galinha (Crow's Foot / IE): Utiliza caixas com colunas para representar as entidades e uma reta que separa o nome da entidade dos atributos, e utiliza símbolos para definir cardinalidades, como 1 barra vertical para representar 1 e 3 ramificações para representar o relacionamento de muitos. 

Notação de Barker: utiliza retângulos com bordas arredondadas para as entidades e os atributos, as cardinalidades são as mesmas da notação pé de galinha. 

Diagramas de Classe UML: serve para representar a estruturação e relações das classes que servem de modelos para objetos. 

