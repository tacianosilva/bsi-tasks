<h1 align="center">Tarefa 01 - Conceitos BD e MER</h1>

| Nome do Aluno:| Usuário no Github| E-mail |
|------|---------|--------|
| Diêgo Axel Bernardo Santos Rodrigues | [Diego-Axel](https://github.com/Diego-Axel) | [Acadêmico](diego.axel.bernardo.097@ufrn.edu.br) |

<br>

# Atividade para a matéria de Banco de Dados da faculdade de Sistemas de Informação - UFRN.

# Questões: 

## Letra 🅰️: Descreva o que é um Banco de Dados e o que é um Sistema Gerenciador de Banco de Dados. Cite exemplos de Bancos de Dados e seus SGBDs.

Um **Banco de Dados** é uma **coleção organizada de dados** que podem ser acessados, gerenciados e atualizados facilmente. Pense nele como uma planilha ou um armário de arquivos. Ele apenas armazena a informação.

Já um **Sistema Gerenciador de Banco de Dados(SGBD)** É o programa (software) que você usa para controlar o banco de dados. Ele permite criar, ler, atualizar e apagar os dados, além de gerenciar a segurança e o acesso. Exemplos: MySQL, PostgreSQL, Oracle, SQL Server.

Em resumo: O **BD** é o conjunto de dados, e o **SGDB** é a ferramente que gerencia esses dados

### Exemplo de dados em um banco de dados:

| ID | Produto         | Quantidade |
|----|-----------------|------------|
| 1  | Macarrão        | 23         |
| 2  | Pacote de Arroz | 35         |
| 3  | Pipoca Doritos  | 26         |
| 4  | Pacote de Arroz | 35         |

---

## Letra  🅱️: Quais os principais problemas de utilizar Sistemas de Arquivos para armazenagem de dados.

Utilizar **sistemas de arquivos** (como pastas e arquivos .txt, .csv, ou .json) para armazenar dados em vez de um SGBD causa problemas sérios de:

1. Dificuldade de Acesso aos Dados.

2. Falta de Integridade.

3. Segurança e Controle de Acesso.

4. Problemas de Atomicidade.

Entre outros... Mas em resumo, sistemas de arquivos não oferecem mecanismos robustos para garantir que os dados sejam consistentes, seguros, íntegros e fáceis de acessar, especialmente em ambientes com múltiplos usuários e regras complexas.

---

## Letra C: O modelo de dados entidade-relacionamento foi desenvolvido para facilitar o projeto de banco de dados, permitindo especificação de um esquema que representa a estrutura lógica geral de um banco de dados. Descreva os três elementos básicos de um Modelo Entidade Relacionamento (MER)

1. **Entidades**: São os objetos ou conceitos do mundo real sobre os quais se deseja guardar informações. Pense nelas como os substantivos do sistema.
    - Exemplos: ```CLIENTE```, ```PRODUTO```, ```ALUNO```, ```PEDIDO```, ```MÉDICO```

2. **Atributos**: São as propriedades ou características que descrevem uma entidade. Pense neles como os adjetivos ou os dados específicos de uma entidade.
    - Exemplos: Para a entidade ```CLIENTE```, os atributos poderiam ser ```Nome```, ```CPF```, ```Endereço``` e ```Telefone```.

3. **Relacionamentos**: Representam a associação ou a interação que existe entre duas ou mais entidades. Pense neles como os verbos que conectam as entidades.
    - Exemplos:
        - Um ```CLIENTE``` faz um ```PEDIDO```. (Relacionamento entre as entidades ```CLIENTE``` e ```PEDIDO```).
        - Um ```ALUNO``` se matricula em uma ```TURMA```. (Relacionamento entre ```ALUNO``` e ```TURMA```).

---

## Letra D: Pesquise sobre as várias notações possíveis para Diagramas ER, cite alguns exemplos de notações diferentes para o mesmo conceito (ex: Cardinalidade, Entidade Subordinada,etc.).

As mais populares são:

1. **Notação de Chen**: Criada por Peter Chen em 1976, é a notação original e mais clássica. É muito usada em ambientes acadêmicos por ser detalhada, mas pode ser visualmente mais complexa.

2. **Notação "Pé de Galinha" (Crow's Foot)**: É a notação mais popular no mercado e em ferramentas CASE (ferramentas de engenharia de software). É considerada mais intuitiva e limpa para diagramas grandes. Variações dela incluem as notações de Information Engineering (IE) e Barker.

3. **Notação UML (Unified Modeling Language)**: Usada em engenharia de software para modelar sistemas orientados a objetos, a UML também possui uma representação para diagramas de classes que pode ser usada para modelagem de dados, sendo conceitualmente similar.

Abaixo estão alguns exemplos de como essas notações representam os mesmos conceitos de formas diferentes.

### 1. Cardinalidade do Relacionamento

A cardinalidade define o número de instâncias de uma entidade que podem se relacionar com instâncias de outra entidade. Vamos usar o exemplo: "Um ```CLIENTE``` pode fazer um ou muitos ```PEDIDOS```".

#### **Notação de Chen**

Usa números e letras (```1```, ```N```, ```M```) próximos à linha que conecta a entidade ao relacionamento (que é representado por um losango).

      (1)             (N)
+---------+      +-----------+      +---------+
| CLIENTE |------|   FAZ     |------| PEDIDO  |
+---------+      +-----------+      +---------+

* **Leitura:** Um ```CLIENTE``` para ```N``` ```PEDIDOS```.

#### **Notação Pé de Galinha (Crow's Foot)**

Usa símbolos gráficos diretamente na linha de relacionamento para representar a cardinalidade e a opcionalidade.

* ```|``` representa "um"
* ```O``` representa "zero"
* ```<``` (o "pé de galinha") representa "muitos"

+---------+         +---------+
| CLIENTE | |<------| PEDIDO  |
+---------+         +---------+

### 2. Entidade Associativa (ou Agregada)

Este conceito é usado para resolver relacionamentos "muitos-para-muitos" (N:N). Por exemplo, um ```ALUNO``` pode se inscrever em muitas ```DISCIPLINAS```, e uma ```DISCIPLINA``` pode ter muitos ```ALUNOS``` inscritos. A entidade associativa seria ```INSCRICAO```.

### 3. Entidade Fraca (ou Subordinada)

Uma entidade fraca é aquela cuja existência depende de outra entidade (chamada de entidade forte ou proprietária). Por exemplo, um ```ITEM_PEDIDO``` só existe se o ```PEDIDO``` ao qual ele pertence existir.

---

## Letra E: Construa um Diagrama ER para projetar uma base de dados de um Sistema de Controle de Freqüência de Empregados de uma organização. A base de dados não deve conter redundância de dados. O modelo ER deve ser representado com um diagrama usando Mermaid.js. O modelo deve apresentar, ao menos, entidades, relacionamentos, atributos, identificadores e restrições de cardinalidade. O modelo deve ser feito no nível conceitual, sem incluir chaves estrangeiras.
- i A base de dados deve manter dados sobre empregados. Cada empregado é identificado por um código, um nome e um e-mail. Para fins de controle de frequência, há dois tipos de empregados.
- ii Um tipo de empregado é o que tem horário livre. Empregados deste tipo podem trabalhar em qualquer horário do dia. Para estes empregados queremos saber quantas horas devem trabalhar ao longo do mês, bem como, qual é o menor período em horas que devem trabalhar. Exemplificando, há alguns empregados que não devem trabalhar menos que duas horas por dia.
- iii Empregados de segundo tipo devem trabalhar em horários fixos. A semana de trabalho do empregado deste tipo está organizada em turnos. Um turno tem horário de início e horário de fim. O empregado pode trabalhar dois turnos no mesmo dia da semana. Cada dia da semana é identificado por um código (algo como "dom", "seg", "ter", . . . ) e tem um nome (algo como "domingo", "segunda-feira", . . . ).
- iv  Todos os empregados devem bater o ponto, ou seja, informar o horário de entrada e saída do trabalho, em cada turno de cada dia da semana.

### Diagrama:

```mermaid
erDiagram
    EMPREGADO {
        string codigo PK
        string nome
        string email
        string tipo
    }

    EMPREGADO_LIVRE {
        int horas_mes
        int horas_min_dia
    }

    EMPREGADO_FIXO {
        
    }

    TURNO {
        string id_turno PK
        string hora_inicio
        string hora_fim
    }

    DIA_SEMANA {
        string codigo PK
        string nome
    }

    PONTO {
        int id_ponto PK
        string hora_entrada
        string hora_saida
    }

    EMPREGADO ||--o{ EMPREGADO_LIVRE : "especialização"
    EMPREGADO ||--o{ EMPREGADO_FIXO : "especialização"
    EMPREGADO_FIXO }o--o{ TURNO : "atua_em"
    TURNO }o--|| DIA_SEMANA : "ocorre_em"
    EMPREGADO ||--o{ PONTO : "registra"
    TURNO ||--o{ PONTO : "referencia"