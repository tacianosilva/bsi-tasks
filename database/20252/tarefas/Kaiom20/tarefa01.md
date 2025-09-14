# Tarefa 01 - Conceitos BD e MER

**Nome:** Kaio Márcio Araújo Cavalcante Lira  
**GitHub:** [Kaiom20](https://github.com/Kaiom20)  
**E-mail:** kaiomacl.20@gmail.com

---
## Questão A

- Um **banco de dados** é uma coleção organizada de informações ou dados estruturadas, normalmente armazenadas eletronicamente em um sistema de computador para facilitar seu acesso.

    - Exemplo:
        
        |  ID  | Produto          | Quantidade |
        |------|------------------|------------|
        | 001  | Farinha de Trigo | 23         |
        | 002  | Arroz Parbolizado| 35         |
        | 003  | Feijão Preto     | 26         |
        | 004  | Macarrão Parafuso| 35         |
        | 005  | Milho de Pipoca  | 35         |

- Um **Sistema gerenciador de banco de dados (SGBD)** é um conjunto de programas que permite criar, visualizar, modificar e excluir informações de um banco de dados.

    - Exemplos: Oracle Database, MySQL, SQL Server, PostgreSQL, IBM DB2 e
Microsoft Access.

## Questão B
- Os principais problemas de utilizar **sistemas de arquivos** para armazenar dados envolvem:

    - Consulta lenta;
    - Falta de segurança e controle de acesso;
    - Dificuldade de Acesso aos Dados;
    - Dificuldade de Manutenção;
    - Problemas de Atomicidade.

    Entre outros... Em resumo, é como usar um bloquinho de notas para gerir uma empresa grande. Para dados importantes, um banco de dados é sempre melhor.

## Questão C
Os três elementos básicos de um Modelo de **Entidade-Relacionamento (MER)** são:
- **Entidades:**
    
    - Os objetos, conceitos ou coisas do mundo real sobre os quais se deseja armazenar dados. 
- **Atributos:** 

    - As propriedades ou características que descrevem uma entidade. 
- **Relacionamentos:**

    - As associações ou ligações entre duas ou mais entidades, indicando como elas se interagem no sistema. 

## Questão D
### Principais Notações para Diagramas ER

### 1. Notação de Chen (1976)
- **Entidade:** Retângulo
- **Atributo:** Elipse, conectada à entidade por uma linha. O identificador (PK) é sublinhado
- **Relacionamento:** Losango
- **Cardinalidade:** Números (1, N) escritos diretamente nas linhas entre entidades e relacionamentos

### 2. Notação Crow's Foot (Pé de Galinha)
- **Entidade:** Retângulo com atributos listados internamente. A PK é destacada com "(PK)" ou sublinhada
- **Atributo:** Listado dentro do retângulo da entidade
- **Relacionamento:** Linha conectando duas entidades, com o nome do relacionamento escrito ao lado da linha
- **Cardinalidade:** Símbolos gráficos nas extremidades das linhas:
  - `|` (uma linha): Um (obrigatório)
  - `0>` (círculo + linha): Zero ou um
  - `<` (pé de galinha): Muitos

### 3. Notação UML (Diagrama de Classe)
- **Entidade:** Classe (retângulo com três divisões: Nome, Atributos, Métodos)
- **Atributo:** Listado na seção de atributos com o tipo (ex: `nome : String`). A PK é marcada com `{PK}`
- **Relacionamento:** Associação (linha reta conectando classes), com o nome escrito junto à linha
- **Cardinalidade:** Multiplicidades escritas nas extremidades da linha:
  - `1`: Um
  - `0..1`: Zero ou um
  - `*`: Muitos (zero ou mais)
  - `1..*`: Um ou muitos