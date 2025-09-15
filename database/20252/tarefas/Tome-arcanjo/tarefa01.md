# Tarefa 01 - Conceitos BD e MER

**Nome:** Tomé Galileu Oliveira Arcanjo  
**GitHub:** [@Tome-arcanjo](https://github.com/Tome-arcanjo)  
**E-mail:** tomearcanjo12@gmail.com


### a. O que é um banco de dados e um Sistema Gerenciador de Banco de Dados?

- **Banco de Dados**: É uma coleção sistemática de informações organizadas(dados), armazenadas eletronicamente em um sistema de computador para facilitar sua gestão, armazenamento e recuperaçao.
- **Sistema Gerenciador de banco de Dados(SGBD)**: Um SGBD é um software especializado que permite a manipulação de um banco de dados de forma segura e eficiente, dando acesso a criação, consulta e alteração desse banco. O SGBD controla o acesso aos dados, garante integridade e facilita o compartilhamento entre os usuários, previnindo redundâncias.
- **Exemplos**: MySQL, Oracle Database e SQL Server (SGBDs relacionais); MongoDB e Cassadra (SGBDs NoSQL); ObjectDB (SGBD orientado a objetos).
  
### b. Qual o problema de utilizar Sistemas de Arquivos?

- **Redundância de dados**: Cada aplicação pode criar os próprios arquivos, levando a criação de arquivos redundantes e desnecessários, gastando espaço de armazenamento.
- **Dificuldade na consulta e acesso**: É difícil acessar as informações dos arquivos de forma eficientes, pois os dados não estão inter-relacionados e o processo deve ser feito de forma manual.
- **Dificuldade com grande volume de dados**: Gerenciar grandes números de dados em arquivos é lento e ineficinete.
- **Segurança inadequada**: Arquivos comuns não possuem os mecanismos de controle de um SGBD, deixando os dados vulneráveis.

### c. Estrutura lógica geral de um MER (Modelo Entidade Relacionamento)

- **Entidades**: Uma entidade é uma "coisa" ou objeto do mundo real ou conceitual sobre o qual armazenam dados (pessoas, lugares, objetos, etc). É representada por uma tabela no modelo de banco de dados, e cada linha da tabela é uma instância.
- **Atributos**: Atributos são as características que descrevem uma entidade. Os atributos correspondem, em um modelo lógico de banco de dados, às colunas de uma tabela.
- **Relacionamentos**: Indicam as associações e interações entre as diferentes entidades. A cardinalidade descreve quantos instâncias de uma entidade podem ser relacionadas a instâncias de outra entidade. Os tipos comuns de cardinalidade são 1:1, 1:N (um-para-muitos), e N:M (muitos-para-muitos). 
