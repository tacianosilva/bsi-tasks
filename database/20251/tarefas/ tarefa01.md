Tarefa 01 - Conceitos BD e MER 
Jonas Jeronimo Cirilo Silva 
xonazz
jonas.silva.702@ufrn.edu.br 


7- a 

Um banco de dados (ou BD) é um conjunto organizado de informações que pode ser facilmente acessado, gerenciado e atualizado. Ele serve para armazenar dados de forma estruturada, permitindo consultas rápidas, modificações seguras e manutenção eficiente dessas informações. Um Sistema Gerenciador de Banco de Dados (SGBD) é um software responsável por criar, organizar, gerenciar e acessar um banco de dados. Ele serve como intermediário entre o usuário e o banco de dados em si, permitindo que a gente insira, altere, consulte e remova dados de forma segura e eficiente. 

MySQL
É um dos SGBDs mais populares do mundo. Ele gerencia bancos de dados relacionais, ou seja, dados organizados em tabelas com colunas e linhas.
Usado em: sites, sistemas web, aplicações de e-commerce. 

PostgreSQL
Outro SGBD relacional muito poderoso e gratuito, com suporte a operações complexas e muita confiabilidade.
Usado em: sistemas corporativos, bancos de dados científicos e aplicações web robustas. 

SQLite
Um SGBD relacional leve, que salva os dados em um único arquivo no disco. Não precisa instalar servidor, por isso é ótimo para aplicativos móveis ou sistemas embarcados.
Usado em: aplicativos Android, iOS, navegadores, programas simples. 


b - 

O uso de sistemas de arquivos para armazenar dados apresenta várias limitações, como a busca lenta por informações, falta de estrutura e validação, além de dificuldade para lidar com múltiplos acessos ao mesmo tempo. Também há baixo nível de segurança, pois os dados podem ser facilmente acessados ou modificados. As operações de atualizar ou excluir registros são complicadas e pouco eficientes. Além disso, esse método não escala bem para grandes volumes de dados e dificulta a realização de análises e relatórios. Por isso, para sistemas mais complexos, o ideal é utilizar um Sistema Gerenciador de Banco de Dados (SGBD), que oferece controle, segurança e desempenho superiores.

c - 

O Modelo Entidade-Relacionamento (MER) é utilizado para representar a estrutura lógica de um banco de dados. Ele é composto por três elementos básicos:

Entidade: Representa objetos ou conceitos do mundo real, como "Aluno" ou "Produto". Cada entidade possui atributos, como nome ou idade.

Relacionamento: Define a associação entre duas ou mais entidades. Pode ser de tipo um para um (1:1), um para muitos (1:N) ou muitos para muitos (N:N).

Atributo: Características das entidades ou relacionamentos. Pode ser simples, composto, chave (identificador único), multivalorado (com múltiplos valores) ou derivado (calculado de outros atributos). 

d - 

Cardinalidade
A cardinalidade descreve a quantidade de instâncias de uma entidade que podem se relacionar com instâncias de outra entidade. Existem diversas formas de representá-la:​
Data Science Central

Notação de Chen: Utiliza números próximos às linhas de relacionamento para indicar a cardinalidade. Por exemplo, "1" e "N" indicam um para um e um para muitos, respectivamente. 
Gleek
​

Notação de Crow's Foot: Representa a cardinalidade com símbolos como uma linha reta para "um", uma linha com três ramificações para "muitos" e uma linha com um círculo para "zero". 
Data Science Central
​

Notação de Barker: Utiliza símbolos semelhantes aos da notação de Crow's Foot, mas com algumas variações específicas para representar a cardinalidade e a participação. 
Wikipedia
​

Entidade Subordinada (ou Entidade Fraca)
Entidades subordinadas são aquelas que não possuem uma chave primária própria e dependem de outra entidade para sua identificação. Sua representação varia conforme a notação:​

Notação de Chen: Representa entidades subordinadas com um retângulo duplo.​

Notação de Crow's Foot: Representa entidades subordinadas com um retângulo simples, mas a dependência é indicada pela presença de um relacionamento obrigatório.​

Notação de Barker: Representa entidades subordinadas com um retângulo simples, similar à notação de Crow's Foot, mas com convenções específicas para indicar a dependência. ​
Wikipedia

Participação
A participação descreve se a presença de uma instância de uma entidade em um relacionamento é obrigatória ou opcional:​

Notação de Chen: Utiliza linhas duplas para indicar participação obrigatória e linhas simples para participação opcional.​

Notação de Crow's Foot: A participação obrigatória é indicada pela ausência de um círculo (representando "zero") na extremidade do relacionamento.​

Notação de Barker: Utiliza símbolos específicos para indicar a participação obrigatória ou opcional, dependendo da convenção adotada. ​






Código do diagrama: 



erDiagram
    EMPREGADO ||--|| TIPO_EMPREGRADO : é
    EMPREGADO ||--o{ PONTO : registra
    EMPREGADO ||--o{ TRABALHA_EM : trabalha_em
    TRABALHA_EM }o--|| TURNO : em
    TURNO }o--|| DIA_SEMANA : ocorre_em

    EMPREGADO {
        string cod_emp PK
        string nome
        string email
    }

    TIPO_EMPREGRADO {
        string cod_emp PK
        string tipo
        int horas_mes
        int min_horas_dia
    }

    TURNO {
        string id_turno PK
        time hora_inicio
        time hora_fim
    }

    DIA_SEMANA {
        string cod_dia PK
        string nome_dia
    }

    PONTO {
        string cod_emp PK
        string id_turno PK
        string cod_dia PK
        datetime hora_entrada
        datetime hora_saida
    }





