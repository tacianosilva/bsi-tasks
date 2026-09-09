# Tarefa 02 - Banco de Dados
## Q1. O modelo de dados entidade-relacionamento foi desenvolvido para facilitar o projeto de banco de dados, permitindo especificação de um esquema que representa a estrutura lógica geral de um banco de dados. Descreva os três elementos básicos de um Modelo Entidade Relacionamento (MER).

Os três elementos básicos do MER são:

### Entidades

As **entidades** representam objetos ou conceitos que possuem existência relevante para o sistema e sobre os quais é necessário armazenar informações. Uma entidade pode representar, por exemplo, uma pessoa, empresa, produto ou projeto.

No contexto de uma empresa de desenvolvimento de software, exemplos de entidades seriam `Cliente`, `Funcionário`, `Squad`, `Projeto` e `Tarefa`.

### Atributos

Os **atributos** representam as características ou propriedades de uma entidade. Eles descrevem as informações que devem ser armazenadas sobre cada ocorrência da entidade.

Por exemplo, a entidade `Cliente` pode possuir os atributos `código`, `nome` e `e-mail`. O atributo `código` pode ser utilizado como identificador da entidade, permitindo distinguir um cliente dos demais.

### Relacionamentos

Os **relacionamentos** representam as associações existentes entre duas ou mais entidades. Eles indicam como as entidades estão relacionadas dentro do contexto do sistema.

Por exemplo, um `Cliente` pode possuir vários `Projetos`, estabelecendo um relacionamento entre as entidades `Cliente` e `Projeto`. Os relacionamentos também podem possuir restrições de cardinalidade, indicando quantas ocorrências de uma entidade podem estar associadas a ocorrências de outra.

Assim, as entidades representam **o que existe no domínio**, os atributos representam **as características desses elementos** e os relacionamentos representam **como esses elementos se associam**.


## Q2. Pesquise sobre as várias notações possíveis para Diagramas ER e cite alguns exemplos de notações diferentes para o mesmo conceito (ex.: cardinalidade, entidade subordinada, etc.).

Entre as mais conhecidas estão as notações **Chen**, **Crow's Foot** e **UML**. Elas utilizam símbolos diferentes para representar os elementos do modelo.

### Notação de Chen

A **notação de Chen** foi proposta por Peter Chen e utiliza símbolos específicos para cada elemento do diagrama. As entidades são representadas por **retângulos**, os atributos por **elipses** e os relacionamentos por **losangos**. As linhas conectam esses elementos.

A cardinalidade é indicada próxima às linhas dos relacionamentos, utilizando valores como `1`, `N` ou `M`. Por exemplo, uma relação em que um cliente possui vários projetos pode ser representada por `1:N`.

Uma entidade subordinada, também chamada de entidade fraca, é representada por um **retângulo com borda dupla**. Seus atributos podem ser representados normalmente por elipses.

### Notação Crow's Foot

A **notação Crow's Foot**, também conhecida como notação de pé de galinha, representa as entidades em caixas que apresentam seus atributos. Os relacionamentos são mostrados por linhas que conectam as entidades.

A cardinalidade é representada por símbolos nas extremidades dessas linhas. O símbolo semelhante a um **pé de galinha** indica o lado que pode possuir várias ocorrências. Assim, uma relação em que um cliente possui vários projetos pode ser representada colocando o símbolo de pé de galinha no lado de `Projeto`.

Diferentemente da notação de Chen, uma entidade subordinada não é identificada por um retângulo com borda dupla. Sua dependência é indicada por meio do relacionamento com a entidade da qual depende.

### Notação UML

A **UML (Unified Modeling Language)** pode ser utilizada para representar estruturas de dados por meio de diagramas de classes. As entidades são representadas por caixas semelhantes às classes, contendo seus atributos. Os relacionamentos são representados por linhas entre essas caixas.

A cardinalidade é indicada por meio de multiplicidades, como `1`, `0..1`, `1..*` e `0..*`. Por exemplo, em uma relação de um para muitos, pode-se utilizar `1` no lado de `Cliente` e `1..*` no lado de `Projeto`.

Uma entidade subordinada pode ser representada como uma classe relacionada à entidade da qual depende, utilizando uma associação que represente essa dependência.

### Exemplos de diferentes representações para o mesmo conceito

A **cardinalidade 1:N** é representada de maneiras diferentes nessas notações. Na notação de Chen, pode ser indicada diretamente como `1:N`. Na Crow's Foot, o lado que representa muitos recebe o símbolo de pé de galinha. Na UML, podem ser utilizadas as multiplicidades `1` e `1..*`.

A **entidade subordinada** também possui representações diferentes. Na notação de Chen, ela utiliza um retângulo com borda dupla. Na Crow's Foot, sua dependência é representada pelo relacionamento com a entidade principal. Na UML, pode ser representada como uma classe relacionada à entidade da qual depende.

Os **atributos** também apresentam diferenças. Na notação de Chen, são representados por elipses ligadas às entidades. Na Crow's Foot, aparecem dentro da caixa da entidade. Na UML, ficam dentro da caixa que representa a classe.


