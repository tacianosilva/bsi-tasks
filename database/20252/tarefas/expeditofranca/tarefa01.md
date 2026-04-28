# **Tarefa 01 - Conceitos BD e MER**
### Nome: Expedito Luiz de França Neto
### Usuário GitHub: expeditofranca
### E-mail: expedito.franca.123@ufrn.edu.br

### Questão 7
#### Item a
Um Banco de Dados é um conjunto organizado de dados relacionados entre si, que são armazenados de forma estruturada e com o objetivo de facilitar o acesso, a atualização e a gestão da informação.
Um SGBD (ou DBMS — Database Management System) é o software responsável por criar, manter, gerenciar e controlar o acesso aos bancos de dados. O SGBD pode criar tabelas, inserir, alterar e excluir dados, controlar o acesso, além de garatir a segurança dos dados.

Bancos de Dados não-relacionais/SGBDs
Orientados a documentos: MongoDB e Couchbase
Orientados a colunas: Cassandra e HBase
Chave-valor e memória: Redis e Memcached

Bancos de Dados relacionais: MySQL, PostgreSQL, Microsoft SQL Server, Oracle Database, IBM Db2

### Questão 7
#### Item b

Inconsistência e redundância: os dados podem aparecer diferentes e repetidos ao longo do tempo.
Acesso concorrente: atualizações simultâneas podem gerar inconsistências e isso é difícil de supervisionar udsando sistemas de arquivos.
Restrição de acesso: Os dados não devem estar abertos a todos os usuários, difícil garatir isso em um sistema de arquivos

### Questão 7
#### Item c

Entidades: São objetos/coisas/ideias do mundo real concretas ou abstratas que queremos representar no banco.
Relacionamentos: São as ligações entre entidades, explicam como elas se relacionam e suas cardinalidades(quantas entidades A se relacionam com quantas entidades B)
Atributos: São as características da entidade ou relacionamento, pode ser simples, composto(endereço: número, rua, bairro), multivalorado(um indivíduo com mais de um e-mail)