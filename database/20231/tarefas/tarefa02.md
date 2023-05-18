# Tarefa 02 - Modelo Relacional e Regras de Conversão
## Nome: Gabriel Lima /
## Usuário: Lima404 / 
## Email: gabriel.lima.112@ufrn.edu.br



- Q7 a: Descreva o modelo relacional: 

O Modelo Relacional é uma forma de representar dados em um Banco de Dados usando relações. Cada relação tem um nome e um conjunto de atributos. As relações são frequentemente chamadas de tabelas. Elas consistem em atributos e tuplas, onde cada atributo representa uma propriedade dos dados e cada tupla é uma instância desses dados. As relações são conectadas por chaves estrangeiras, permitindo estabelecer relacionamentos entre as tabelas. Esses relacionamentos podem ser um-para-um, um-para-muitos ou muitos-para-muitos.

- Q7 b: Descreva as restrições de integridade do Modelo Relacional.

As restrições de integridade no Modelo Relacional são regras que são aplicadas aos dados armazenados em um Banco de Dados relacional para garantir sua consistência e precisão. Essas restrições ajudam a manter a qualidade e a validade dos dados. Abaixo esta um exemplo de restrições de integridade comumente utilizadas no Modelo Relacional:

- Restrição de Integridade Referencial: Essa restrição garante que, ao estabelecer um relacionamento entre tabelas usando chaves estrangeiras, os valores correspondentes nas colunas relacionadas sejam consistentes. Por exemplo, se uma chave estrangeira em uma tabela está relacionada a uma chave primária em outra tabela, a restrição de integridade referencial garante que não haja valores órfãos ou inconsistências nos dados.

- Q7 c: Descreva as Regras de Conversão entre o Modelo Entidade-Relacionamento e o Modelo Relacional. 

1. Entidades:

Cada entidade no modelo ER é mapeada para uma tabela no modelo relacional.
Os atributos da entidade se tornam colunas na tabela correspondente.
A chave primária da tabela pode ser derivada a partir da chave primária da entidade no modelo ER.

2. Relacionamentos:

Relacionamentos um-para-um: O relacionamento é representado através da inclusão da chave primária de uma entidade como chave estrangeira na tabela da outra entidade.
Relacionamentos um-para-muitos: O lado "um" do relacionamento contém a chave primária da entidade "um" como chave estrangeira na tabela da entidade "muitos".
Relacionamentos muitos-para-muitos: É criada uma tabela intermediária, também conhecida como tabela de junção ou tabela de associação, que contém as chaves primárias das entidades relacionadas.

3. Atributos compostos:

Atributos compostos são representados como colunas individuais na tabela.
Os nomes das colunas podem incluir o nome do atributo composto e o nome do subatributo.

4. Atributos multivalorados:

Atributos multivalorados são representados através da criação de uma nova tabela, onde cada valor multivalorado é armazenado em uma nova linha.

5. Atributos derivados:

Atributos derivados não são representados como colunas nas tabelas, pois podem ser calculados a partir de outros atributos.

- Q7 d: Crie um Diagrama Entidade Relacionamento e depois crie um Esquema Relacional, usando as regras de conversão, para o seguinte projeto: A universidade que preparar um banco de dados para gravar os dados do Laboratórios de Pesquisa (Por exemplo, LABICAN, LABEPI, LABORGEO, etc). Crie um Diagrama do modelo Entidade-Relacionamento para este projeto informando atributos e cardinalidades, atendendo aos seguintes requisitos: 



mermaid
    erDiagram

    Empregado{
        int codigo_empregado PK
        string nome
        string Email
    }
