<h1 align="center">Tarefa 01 - Conceitos BD e MER</h1>

| Nome | Usuário | E-mail |
|------|---------|--------|
| Paulo Douglas M. Dias | [Paulo-Douglas](https://github.com/Paulo-Douglas) | [Acadêmico](paulo.martins.132@ufrn.edu.br) |

# Banco de Dados e Sistema Gerenciador de Banco de Dados (SGBD)

## O que é um Banco de Dados?

Um **Banco de Dados** é uma **coleção organizada de dados** que podem ser acessados, gerenciados e atualizados facilmente.

- Armazena informações de forma estruturada
- Pode conter dados de clientes, vendas, produtos, etc.
- Permite fácil recuperação, inserção, atualização e exclusão de dados

### Exemplo de dados em um banco de dados:

| ID | Nome       | Idade |
|----|------------|-------|
| 1  | Ana Souza  | 23    |
| 2  | João Silva | 35    |

---

## O que é um Sistema Gerenciador de Banco de Dados (SGBD)?

Um **SGBD** é um software que permite:
- Criar e gerenciar bancos de dados
- Controlar acesso e segurança
- Realizar operações como: inserir, consultar, atualizar e excluir dados (CRUD)

Ele atua como **interface entre o usuário e o banco de dados**.

---

## 🧩 Exemplos de Bancos de Dados e seus respectivos SGBDs:

| Tipo de Banco de Dados     | SGBD Exemplo            |
|----------------------------|-------------------------|
| Relacional                 | MySQL, PostgreSQL       |
| NoSQL (documento/chave)    | MongoDB, Redis          |
| Em nuvem                   | Firebase, Amazon RDS    |
| Local/simples (arquivo)    | SQLite, Microsoft Access|

---

## Comparando: Banco de Dados vs SGBD

| Banco de Dados        | SGBD                        |
|-----------------------|-----------------------------|
| Coleção de dados      | Software que gerencia dados |
| Armazena a informação | Interage com o usuário      |
| Ex: dados de clientes | Ex: MySQL, PostgreSQL       |

---

## Exemplos populares:

- **Banco de Dados Relacional**:
  - **SGBD:** PostgreSQL, MySQL, Oracle, SQL Server
- **Banco de Dados NoSQL**:
  - **SGBD:** MongoDB, Firebase, Cassandra
- **Banco de Dados Local/Simplificado**:
  - **SGBD:** SQLite, Access

---

> **Resumo:** Banco de Dados guarda os dados, e o SGBD é o programa que faz toda a mágica acontecer com esses dados!

# Problemas ao Utilizar Sistemas de Arquivos para Armazenagem de Dados

## O que é um Sistema de Arquivos?

É a forma tradicional de armazenar dados em arquivos como `.txt`, `.csv`, etc., geralmente organizados em pastas. O acesso e manipulação desses dados são feitos diretamente pelo sistema operacional ou por programas específicos.

---

## Principais Problemas

### 1. Redundância e Inconsistência de Dados
- O mesmo dado pode ser armazenado em vários arquivos diferentes.
- Dificuldade em manter a consistência das informações.

### 2. Falta de Integração entre os Dados
- Os dados ficam espalhados e sem conexão entre si.
- Consultas e análises que exigem cruzamento de dados se tornam complexas.

### 3. Falta de Segurança e Controle de Acesso
- Poucos mecanismos para definir permissões de acesso e edição.
- Dificuldade em proteger dados sensíveis.

### 4. Ausência de Mecanismos de Backup e Recuperação
- Não há um sistema integrado de backup.
- Restauração de dados perdidos ou corrompidos é difícil e manual.

### 5. Baixa Eficiência em Consultas
- A busca por informações é lenta e ineficiente, especialmente com grandes volumes de dados.
- Não há suporte para indexação e otimização de consultas.

### 6. Dificuldade na Atualização dos Dados
- As atualizações são feitas manualmente ou por meio de scripts personalizados.
- Maior risco de erros e inconsistências.

### 7. Falta de Padronização
- Não há uma estrutura uniforme para os arquivos.
- Cada sistema pode usar formatos diferentes, dificultando a interoperabilidade.

---

## Comparação: Sistema de Arquivos vs Banco de Dados

| Característica               | Sistema de Arquivos    | Banco de Dados (SGBD)    |
|-----------------------------|------------------------|--------------------------|
| Redundância de dados        | Alta                   | Baixa                    |
| Segurança                   | Baixa                  | Alta                     |
| Consultas                   | Limitadas              | Complexas e otimizadas   |
| Recuperação de falhas       | Manual                 | Automatizada             |
| Controle de concorrência    | Inexistente            | Presente                 |

---

## Conclusão

O uso de sistemas de arquivos pode ser suficiente para aplicações simples, mas apresenta sérias limitações em termos de segurança, integridade, desempenho e escalabilidade. Para aplicações mais complexas, o uso de um Sistema Gerenciador de Banco de Dados é a solução mais adequada.

# Modelo Entidade-Relacionamento (ER)

O **Modelo Entidade-Relacionamento (ER)** foi desenvolvido para facilitar o projeto de bancos de dados, permitindo a especificação de um esquema que representa a estrutura lógica geral de um banco de dados. Ele descreve as **entidades**, os **atributos** dessas entidades e os **relacionamentos** entre elas.

---

## 1. **Entidades**
As **entidades** são objetos ou conceitos do mundo real que têm significado e que precisam ser armazenados em um banco de dados. Elas representam coisas ou objetos que podem ser identificados de maneira única.

### Exemplos:
- **Cliente**: Uma pessoa que realiza compras.
- **Produto**: Um item que está à venda no estoque.

As entidades geralmente são representadas como **retângulos** no diagrama ER.

---

## 2. **Atributos**
Os **atributos** são as propriedades ou características das entidades que fornecem informações adicionais sobre elas. Cada atributo possui um valor específico.

### Exemplos:
- **Cliente** pode ter atributos como **Nome**, **Idade**, **Endereço**.
- **Produto** pode ter atributos como **Preço**, **Quantidade em estoque**, **Descrição**.

Os atributos são representados por **elipses** conectadas à entidade no diagrama ER.

---

## 3. **Relacionamentos**
Os **relacionamentos** descrevem como as entidades se conectam entre si. Eles representam a interação entre duas ou mais entidades.

### Exemplos:
- **Compra**: Um **Cliente** pode realizar uma **Compra** de vários **Produtos**.
- **Fornecimento**: Um **Produto** pode ser fornecido por vários **Fornecedores**.

Os relacionamentos são representados por **losangos** no diagrama ER, com as entidades conectadas a eles.

---

## Conclusão
O modelo **Entidade-Relacionamento (ER)** é uma ferramenta essencial para o projeto de bancos de dados, pois permite a representação clara e visual das entidades, atributos e relacionamentos. Essa abordagem facilita o entendimento e o desenvolvimento de sistemas de gerenciamento de dados.

# Notações para Diagramas ER

Existem várias notações para representar Diagramas Entidade-Relacionamento (ER). Cada uma tem suas convenções para conceitos como cardinalidade, entidades subordinadas, etc.

---

## 1. **Notação de Chen**
- **Cardinalidade**: Representada por números próximos às extremidades das linhas de relacionamento (ex: 1..*, 0..1).
- **Entidade Subordinada**: Usada um círculo (ou elipse) conectando a entidade subordinada à principal.

---

## 2. **Notação de Crow's Foot**
- **Cardinalidade**: Usam símbolos como "pé de galinha" para "muitos", linha reta para "um", e círculo para "zero ou um".
- **Entidade Subordinada**: Representada por uma linha simples, conectando a entidade subordinada à principal.

---

## 3. **Notação UML**
- **Cardinalidade**: Usam multiplicidade nas associações (ex: 1, 0..1, 1..*, 0..*).
- **Entidade Subordinada**: Representada por herança, onde a classe subordinada herda os atributos da classe principal.

---

## 4. **Notação de Barker**
- **Cardinalidade**: Representada por números ao longo das linhas de relacionamento (semelhante à notação de Chen).
- **Entidade Subordinada**: Representada por um triângulo conectando a entidade subordinada à principal.

---

## Exemplos de Cardinalidade e Entidades Subordinadas
- **Cardinalidade**:
  - **Chen**: 1..*, 0..1
  - **Crow's Foot**: 1, ∞
  
- **Entidades Subordinadas**:
  - **Chen**: Círculo conectando entidades
  - **Crow's Foot**: Linha simples conectando entidades

# Diagrama ER - Sistema de Controle de Frequência de Empregados

## Entidades

### 1. **EMPREGADO**
- **CPF**: Identificador único do empregado (Chave Primária).
- **Nome**: Nome completo do empregado.
- **Cargo**: Cargo do empregado na organização.
- **Data de Admissão**: Data de contratação do empregado.

### 2. **FREQUENCIA**
- **Data**: Data do registro de entrada e saída do empregado.
- **Hora de Entrada**: Hora em que o empregado entrou no trabalho.
- **Hora de Saída**: Hora em que o empregado saiu do trabalho.

### 3. **DEPARTAMENTO**
- **ID do Departamento**: Identificador único do departamento (Chave Primária).
- **Nome**: Nome do departamento na organização.

---

## Relacionamentos

### 1. **EMPREGADO pertence_a DEPARTAMENTO**
- Um **EMPREGADO** pertence a um único **DEPARTAMENTO**.
- Cardinalidade: **1:N** (Um empregado pertence a um único departamento, mas um departamento pode ter vários empregados).

### 2. **EMPREGADO registra FREQUENCIA**
- Um **EMPREGADO** registra várias entradas de **FREQUENCIA** (uma para cada dia de trabalho).
- Cardinalidade: **1:N** (Um empregado pode registrar múltiplos registros de frequência, mas cada entrada de frequência pertence a apenas um empregado).

---

## Diagrama ER

```mermaid
erDiagram
    EMPREGADO {
        string CPF "Identificador único"
        string nome
        string cargo
        date data_admissao
    }
    
    FREQUENCIA {
        date data
        string hora_entrada
        string hora_saida
    }
    
    DEPARTAMENTO {
        string id_departamento "Identificador único"
        string nome
    }
    
    EMPREGADO ||--o| DEPARTAMENTO : pertence_a
    EMPREGADO ||--o| FREQUENCIA : registra
