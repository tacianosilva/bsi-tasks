# Tarefa 02 - MER e Projeto de Banco de Dados Relacional

## Q1. O Mer:
- O modelo de dados entidade-relacionamento foi desenvolvido para facilitar o projeto de banco de dados, permitindo especificação de um esquema que representa a estrutura lógica geral de um banco de dados. Descreva os três elementos básicos de um Modelo Entidade Relacionamento (MER).

**Resposta**: Os tres elementos básicos que compõem o MER são:
1. Entidade: Representa um objeto do mundo real (físico ou lógico) que é distinguível de outros objetos e sobre o qual o sistema precisa armazenar dados. Exemplos: Cliente, Funcionário, Produto.

2. Relacionamento: É a associação ou ligação entre duas ou mais entidades, representando como esses objetos interagem no contexto do negócio. Exemplos: Um funcionário trabalha em um departamento; um cliente solicita um projeto.

3. Atributo: É a propriedade ou característica que descreve uma entidade ou um relacionamento. Representa os dados específicos que serão armazenados. Exemplos: O nome e CPF de um cliente; a data de início de um projeto.

## Q2. Notaçoes DER
- Pesquise sobre as várias notações possíveis para Diagramas ER e cite alguns exemplos de notações diferentes para o mesmo conceito (ex.: cardinalidade, entidade subordinada, etc.).

**Resposta**: Existem diversas abordagens visuais para representar o Modelo ER, criadas para facilitar a comunicação entre projetistas e stakeholders. As principais são:

- Notação de Peter Chen (Original): É a mais clássica para modelagem puramente conceitual.
  1. Entidade: Retângulo.
  2. Relacionamento: Losango.
  3. Atributos: Elipses (ou balões) ligadas às entidades.
  4. Cardinalidade: Escrita nas linhas conectoras no formato (min, max) como (1,1) ou (0,n), ou ainda 1 e N soltos.

Notação Pé de Galinha (Crow's Foot / Martin): Muito utilizada em ferramentas modernas e modelagem lógica.
  1. Entidade: Caixa (tabela) com os atributos listados dentro.
  2. Relacionamento: Linhas conectando as caixas. O losango desaparece (ou vira uma entidade associativa).
  3. Cardinalidade: Desenhada diretamente nas extremidades da linha. Um traço reto indica "1", um círculo indica "0" (opcional), e três traços abertos (o pé de galinha) indicam "Muitos" (N).

Notação UML (Diagrama de Classes): Focada em orientação a objetos, mas muito adaptada para banco de dados.
  1. Entidade: Retângulo dividido em seções (Nome, Atributos, Operações).
  2. Relacionamento: Linha simples ou setas entre as classes.
  3. Cardinalidade: Expressa em texto próximo à extremidade da linha como 1..1 ou 0..*.

## Q3. Prática
- Construa um Diagrama ER para projetar a base de dados de uma empresa de desenvolvimento de software com outras empresas como clientes. A base de dados não deve conter redundância de dados. O modelo ER deve ser representado com um diagrama usando Mermaid.js. O modelo deve apresentar, ao menos, entidades, relacionamentos, atributos, identificadores e restrições de cardinalidade. O modelo deve ser feito no nível conceitual, sem incluir chaves estrangeiras.

a) A empresa presta serviços de desenvolvimento de software para outras empresas (clientes). Cada cliente é identificado por um código, um nome e um e-mail de contato.
b) Os funcionários da empresa trabalham em squads (equipes). Cada funcionário é identificado por um código, um nome e um e-mail, e possui um papel na equipe: desenvolvedor, testador, líder técnico, supervisor ou gerente de produto.
c) Cada squad é formada por vários funcionários e resolve tarefas (issues). Uma tarefa tem código, descrição, prioridade, situação e uma estimativa em horas. As tarefas pertencem a projetos de um cliente.
d) O trabalho é organizado em iterações (sprints). Uma squad planeja releases para seus clientes; uma release agrupa um conjunto de tarefas e passa por testes de validação.

**Resposta**: Abaixo está a representação conceitual do cenário proposto usando a notação do Mermaid. (Note que não existem chaves estrangeiras -> foco apenas no nível conceitual) e que foi criada uma entidade PROJETO para atender ao requisito de que as tarefas "pertencem a projetos de um cliente".

``` mermaid
erDiagram
    CLIENTE ||--|{ PROJETO : solicita
    PROJETO ||--o{ TAREFA : possui
    SQUAD ||--|{ FUNCIONARIO : "é formada por"
    SQUAD ||--o{ SPRINT : organiza
    SQUAD ||--o{ RELEASE : planeja
    SQUAD ||--o{ TAREFA : resolve
    SPRINT ||--o{ TAREFA : contem
    RELEASE ||--o{ TAREFA : agrupa

    CLIENTE {
        int codigo PK
        string nome
        string email_contato
    }
    FUNCIONARIO {
        int codigo PK
        string nome
        string email
        string papel
    }
    SQUAD {
        int codigo PK
        string nome
    }
    PROJETO {
        int codigo PK
        string nome
    }
    TAREFA {
        int codigo PK
        string descricao
        string prioridade
        string situacao
        float estimativa_horas
    }
    SPRINT {
        int codigo PK
        string nome
    }
    RELEASE {
        int codigo PK
        string nome
    }
```

## Q4. Prática 2
A partir do Diagrama ER da questão anterior, faça o mapeamento para o Modelo Relacional: liste as relações (tabelas), com seus atributos, e identifique as chaves primárias e as chaves estrangeiras de cada relação.

**Resposta**:

## Q5. Prática 3
Descreva, em linguagem natural, as restrições de integridade referencial que devem ser garantidas no esquema projetado (ex.: "uma tarefa só pode existir vinculada a um projeto de cliente existente", "toda squad deve possuir um líder técnico").

**Resposta**:
