# Tarefa 01 - Conceitos BD e MER

| Nome                     | Usuário                                                  | E-mail                                                                                               |
| ------------------------ | -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Anderson G. Pereira Cruz | [andersonstack](mailto:https://github.com/andersonstack) | [Pessoal](mailto:andersong.pereiracruz@gmail.com) / [Acadêmico](mailto:gabriel.cruz.133@ufrn.edu.br) |

## Banco de Dados

Banco de dados é um sistema computarizado de manutenção de registros de forma eficiente e segura. Permite:

- Inserir | Buscar | Excluir | Alterar Dados existentes;
- Controle de acesso e segurança;
- Escalabilidade.

### Exemplos

| Tipo      | Características                                   | Exemplos                               |
| --------- | ------------------------------------------------- | -------------------------------------- | ------------------ |
| SQL       | Dados estruturados em tabelas com relacionamentos | MySQL, PostgreSQL, Oracle, SQL, Server |
| No-SQL    | Flexível: Semelhante a documentos Json            | MongoDB, Cassandra, Redis, Neo4j       |
| OO        | Armazena objetos                                  | Db40, ObjectDB                         | Aplicações em Java |
| In-Memory | Dados Armazenados na RAM                          | Redis, Memcached                       |

## Sistema Gerenciador de Banco de Dados

Permite criar, administrar e processar os B.D. Sua principal função, em geral, é a de isolar os usuários do banco de dados dos **detalhes do nível de hardware**;
Garante o **ACID** _(Atomicidade, Consistência, Isolação, Durabilidade)_.

### Exemplos

| Tipo      | Destaque                                   |
| --------- | ------------------------------------------ |
| SQL       | Suporta a transações ACID e SQL padrão     |
| NoSQL     | Estabilidade horizontal e esquema flexível |
| OO        | Armazenamento direto de objetos            |
| In-Memory | Baixa latência                             |

# Principais Problemas no Uso de Sistemas de Arquivos para Armazenamento de Dados

## 1. Redundância e Inconsistência de Dados

- **Problema**: Dados duplicados em múltiplos arquivos
- **Exemplo**: Informações de um cliente podem aparecer em arquivos de vendas, entregas e cadastros
- **Consequência**: Atualizações não sincronizadas levam a dados conflitantes

## 2. Isolamento dos Dados

- **Problema**: Dados espalhados em diversos arquivos sem relacionamento explícito
- **Exemplo**: Relacionar informações de pedidos com dados de clientes requer programação complexa
- **Consequência**: Dificuldade em obter visões integradas dos dados

## 3. Problemas de Atomicidade

- **Problema**: Falta de mecanismos para garantir transações completas
- **Exemplo**: Se um sistema falhar durante transferência bancária, pode debitar sem creditar
- **Consequência**: Inconsistências nos dados após falhas

## 4. Dificuldade no Acesso Concorrente

- **Problema**: Controle limitado de acesso simultâneo
- **Exemplo**: Dois usuários editando o mesmo arquivo podem sobrescrever alterações
- **Consequência**: Perda de dados e corrupção de informações

## 5. Problemas de Segurança

- **Problema**: Controle de acesso granular difícil de implementar
- **Exemplo**: Não é fácil restringir acesso a campos específicos dentro de arquivos
- **Consequência**: Vulnerabilidades de segurança e acesso não autorizado

## 6. Dependência de Programas Aplicativos

- **Problema**: Estrutura dos dados embutida no código dos programas
- **Exemplo**: Mudar a estrutura de um arquivo exige alterar todos programas que o usam
- **Consequência**: Alto custo de manutenção e pouca flexibilidade

## 7. Falta de Padronização

- **Problema**: Cada aplicação implementa seu próprio formato de armazenamento
- **Exemplo**: Dados de clientes podem ter formatos diferentes em sistemas distintos
- **Consequência**: Dificuldade de integração entre sistemas

## 8. Problemas de Integridade

- **Problema**: Dificuldade em implementar regras de validação centralizadas
- **Exemplo**: Não há mecanismo fácil para garantir que CPFs sejam únicos e válidos
- **Consequência**: Dados incorretos ou inválidos no sistema

## Comparação com SGBDs

| Problema               | Sistema de Arquivos | SGBD             |
| ---------------------- | ------------------- | ---------------- |
| Redundância            | Alta                | Controlada       |
| Consistência           | Frágil              | Garantida (ACID) |
| Acesso concorrente     | Problemático        | Gerenciado       |
| Segurança              | Básica              | Granular         |
| Independência de dados | Baixa               | Alta             |

# Elementos Básicos do Modelo Entidade-Relacionamento (MER)

## 1. Entidades

- **Definição**: Objetos do mundo real representados no banco de dados
- **Características**:
  - Correspondem a "coisas" que precisamos armazenar dados (ex: cliente, produto)
  - São representadas por **retângulos** no diagrama
- **Exemplos**:
  - `MÉDICO`, `PACIENTE`, em um sistema médico.

## 2. Atributos

- **Definição**: Propriedades ou características das entidades
- **Tipos**:
  - **Simples**: Não divisíveis (ex: CPF, data_nascimento)
  - **Compostos**: Podem ser divididos (ex: endereço → rua, cidade, CEP)
  - **Multivalorados**: Podem ter vários valores (ex: telefones de um paciente)
  - **Derivados**: Calculados a partir de outros (ex: idade a partir da data de nascimento)
- **Representação**:
  - Mostrados como **elipses** conectadas à entidade
  - Atributos-chave sublinhados

## 3. Relacionamentos

- **Definição**: Associações significativas entre entidades
- **Características**:
  - Representados por **losangos** no diagrama
  - Podem ter **cardinalidade** (1:1, 1:N, N:N)
- **Exemplos**:
  - `MÉDICO` **realiza** `CONSULTA` (1:N)
  - `PACIENTE` **participa** `CONSULT` (1:N)

## Diagrama MER Básico em Mermaid

Figura 01 - Diagrama MER
![alt text](image.png)

# Notações para Diagramas Entidade-Relacionamento (ER)

## 1. Notação de Peter Chen (Original)

- **Entidades**: Retângulos
- **Atributos**: Elipses
- **Relacionamentos**: Losangos
- **Cardinalidade**: Números (1, N, M)

## 2. Notação Crow's Foot

- **||** = Um (One)
- **|{** = Muitos (Many)
- **}o** = Zero ou um

Utilizado na codificação dos diagramas em `Mermaid` *Figura 01*.

## 3. Notação UML (Classe)

* **Entidade:** Classes
* **Atributos:** Listados na classe
* **Cardinalidades:** 1, 1.., 0..

## 4. Entidade Fraca / Subordinada

Tem caído em desuso na prática moderna de modelagem de dados. Normalmente essa aplicação é feita nas regras de negócio da aplicação.

| Notação | Representação |
| - | - |
| Chen | Retângulo duplo |
| Crow's Foot | Retângulo com borda dupla |
| UML | Classe com estereótipo *weak*|

***
`Apesar das diferenças visuais, todas representam os mesmos conceitos fundamentais de modelagem ER. A escolha depende geralmente da ferramenta utilizada ou do padrão da organização.`
