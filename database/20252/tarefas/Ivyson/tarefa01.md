# Tarefa 01 - Conceitos BD e MER

### Nome: Ivyson Wanderson Nunes Martins
### Usuário: Ivyson0
### email: ivyson.nunes.707@ufrn.edu.br


---
# Questão 7a: Definição de Banco de Dados e SGBD com exemplos

Um banco de dados é um sistema de armazenamento de informações que permite
coleta, armazenamento, recuperação e manipulação de dados de forma controlada,
rápida, estruturada e eficiente.

Um SGBD é um software que aprimora integridade, segurança, concorrência,
recuperação e tolerância a falhas, permitindo gerenciar bases de dados, 
incluindo inserção, alteração e remoção de dados.

Exemplos de bancos de dados: data warehouses, NoSQL, relacionais, orientados
a objetos, distribuídos e gráficos.

Exemplos de SGBDs: MySQL, PostgreSQL, Oracle, SQL Server, MongoDB, Redis,
Cassandra, SQLite, Elasticsearch, Neo4j e Amazon RDS.

---
# Questão 7b: Problemas de usar sistemas de arquivos para armazenamento  

Sistemas de arquivos são adequados para armazenamento simples ou quando há poucos dados.
No entanto, para gerenciar dados de forma mais complexa e estruturada, bancos de dados
se sobressaem, pois sistemas de arquivos enfrentam problemas como redundância e
inconsistência de dados, dificuldades de acesso e recuperação, além da ausência de
escalabilidade, manutenção adequada, segurança e controle de concorrência limitado.

---
# Questão 7c: Três elementos básicos do Modelo Entidade-Relacionamento (MER)

O MER foi desenvolvido para facilitar o projeto de banco de dados, permitindo a
especificação de um esquema que representa a estrutura lógica geral de um banco
de dados.

1. Entidades: objetos físicos (cliente, empresa, produto, veículo) ou lógicos
(venda, sistema, interface, ID do produto). Podem ser fortes, fracas ou
associativas e devem ser nomeadas com substantivos concretos ou abstratos.

2. Atributos: características que descrevem cada entidade. Podem ser simples
(nome, CPF, email, data de nascimento) ou compostos (por exemplo, endereço,
composto por rua, bairro, cidade, etc).

3. Relacionamentos: representam como as entidades estão relacionadas. Tipos:
   - Um para um (1:1): cada unidade de uma entidade se relaciona com uma da outra.
   - Zero ou muitos (0:N): uma unidade pode não se relacionar com nenhuma ou com
várias unidades da outra entidade.
   - Um para muitos (1:N): uma unidade se relaciona com várias da outra entidade.
   - Muitos para muitos (N:M): cada unidade pode se relacionar com várias unidades
     da outra entidade e vice-versa.
