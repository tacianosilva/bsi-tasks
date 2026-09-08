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
