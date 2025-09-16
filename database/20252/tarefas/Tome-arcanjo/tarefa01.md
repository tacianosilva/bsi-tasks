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

### d. Diversidades das notações para Diagramas ER

- **Chen**: Entidades em retângulos, atributos em elipses, relacionamentos em losangos.
- **Crow's Foot/IE**: Entidades em retângulos, cardinalidade mostrada por fork + anéis/traços para opcionalidade/obrigatoriedade.
- **UML**: Classes/atributos em retângulos divididos e multiplicidade (0..*, 1..1, etc.) para cardinalidade. Usada quando deseja alinhar modelo de dados com OO.
- **Barker / Arrow / outras variantes**: Pequenas diferenças gráficas (setas, traços, símbolos) usadas em ambientes corporativos ou por ferramenta.

  **Mesmos conceitos diferentes notações**
  **Cardinalidade**
  - **Chen**: normalmente indica (min,max) ou anota texto ao lado da linha; menos visual que pé-de-corvo.
  - **Crow's foot**: Crow’s Foot: usa o pé-de-corvo para “many”, um traço para “one”; um círculo (“o”) indica 0 (opcional), traço indica 1 (obrigatório)
  - **UML**: usa multiplicidade numérica ao lado das associações: 0..* (zero ou muitos), 1 (um só), 1..* (um ou muitos).

  **Entidade Fraca/Subordinada**
  - **Chen**: representa entidade fraca com retângulo duplo; relacionamento identificador em losango duplo.
  - **Crow's foot/Barker**: representam entid. fraca com símbolo ou rótulo e relacionamento identificador (linha com traço especial); às vezes usam chave parcial indicada       dentro da entidade.
  - IDEF1X: marca claramente entidades dependentes e relacionamentos identificadores (chaves explícitas e linhas de identificação).

  **Atributos**
  - **Chen (clássico)**: atributos em elipses; elipse dupla = multivalorado; elipse ramificada = atributo composto. Ex.: Endereço com sub-elipses Rua, Cidade.
  - **Crow’s Foot / UML**: geralmente colocam atributos dentro do retângulo da entidade (lista); multivalorados / compostos são anotados textualmente ou com notação específica da ferramenta (menos diagramática que Chen).

**e. Código do mermaid.js para o ER**
```mermaid
erDiagram
    EMPREGADO {
        string codigo
        string nome
        string email
    }

    EMPREGADO_HORARIO_LIVRE {
        int horas_mensais
        int horas_min_diarias
    }

    EMPREGADO_HORARIO_FIXO {
    }

    DIA_SEMANA {
        string codigo
        string nome
    }

    TURNO {
        time hora_inicio
        time hora_fim
    }

    PONTO {
        datetime hora_entrada
        datetime hora_saida
    }

    %% Relacionamentos e Cardinalidades
    EMPREGADO ||--o{ EMPREGADO_HORARIO_LIVRE : "especialização"
    EMPREGADO ||--o{ EMPREGADO_HORARIO_FIXO : "especialização"

    EMPREGADO_HORARIO_FIXO ||--o{ TURNO : "trabalha_em"
    TURNO }o--|| DIA_SEMANA : "ocorre_em"

    EMPREGADO ||--o{ PONTO : "bate"
    PONTO }o--|| TURNO : "refere_a"

 
