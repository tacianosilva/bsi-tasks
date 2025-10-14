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

---
# Questão 7d: Notações diferentes para conceitos de Diagramas ER

1. Entidade forte
   - Chen: retângulo simples
   - IDEF1X: entidade independente

2. Entidade fraca
   - Chen: retângulo duplo
   - IDEF1X: entidade dependente

3. Relacionamento um para muitos (1:N)
   - Chen: losango com linha conectando "1" e "N"
   - Martin / Pé de galinha: linha com "pé de galinha" indicando "muitos"
   - IDEF1X: linha com indicação "um ou muitos"

4. Relacionamento um para um (1:1)
   - Chen: losango com linha conectando "1" e "1"
   - Martin / Pé de galinha: linha com "1" em ambas as pontas
   - IDEF1X: linha com "1 para 1"

5. Cardinalidade / Multiplicidade
   - Chen: números próximos às linhas (0..1, 1..N)
   - Martin / Pé de galinha: símbolos de "pé de galinha" ou notação textual (1, N)
   - IDEF1X: indica restrições dentro da entidade ou da linha do relacionamento

---
# Questão 7e: Diagrama ER de um sistema de frequência

Diagrama criado utilizando a ferramenta online gratuita: Mermaid Live Editor

```mermaid
---
title: Tarefa 01 (Banco de Dados)
---

erDiagram
    EMPREGADO {
        int codigoEmpregado
        string nome
        string email
    }

    HORARIOLIVRE {
        int cargaMensal
        int menorPeriodo
    }

    HORARIOFIXO {
        time horaInicio
        time horaFim
        int numeroTurno
    }

    DIASEMANA {
        string codigoDia
        string nomeDia
    }

    ESCALA {
        date dataInicio
        date dataFim
    }

    REGISTROPONTO {
        date dataPonto
        time horaEntrada
        time horaSaida
    }

    EMPREGADO ||--|| HORARIOLIVRE : "1:1"
    EMPREGADO ||--o{ ESCALA : "1:N"
    ESCALA }o--|| HORARIOFIXO : "N:1"
    HORARIOFIXO }o--|| DIASEMANA : "N:1"
    EMPREGADO ||--o{ REGISTROPONTO : "1:N"
