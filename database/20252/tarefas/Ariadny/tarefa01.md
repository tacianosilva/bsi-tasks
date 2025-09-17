# Tarefa 01 - Conceitos BD e MER

**Nome:** [Seu Nome Aqui]
**Usuário Github:** [Seu Usuário Github Aqui]
**E-mail:** [Seu E-mail Aqui]

---

### a. Descreva o que é um Banco de Dados e o que é um Sistema Gerenciador de Banco de Dados. Cite exemplos de Bancos de Dados e seus SGBDs.

**Banco de Dados (BD)**
Um Banco de Dados é uma coleção organizada de dados estruturados, armazenados de forma eletrônica em um sistema de computador. Ele é projetado para ser facilmente acessado, gerenciado e atualizado. O principal objetivo de um banco de dados é armazenar e recuperar informações de forma eficiente e segura.

**Sistema Gerenciador de Banco de Dados (SGBD)**
Um Sistema Gerenciador de Banco de Dados (SGBD), ou *DBMS (Database Management System)* em inglês, é o software que interage com os usuários, aplicações e o próprio banco de dados para capturar, analisar e gerenciar os dados. Ele atua como uma interface entre o banco de dados e o usuário final ou programas, permitindo a definição, criação, consulta, atualização e administração de bancos de dados.

**Exemplos de Bancos de Dados e seus SGBDs:**

| Tipo de Banco de Dados | Exemplo de SGBD | Descrição |
| :--- | :--- | :--- |
| **Relacional** | MySQL, PostgreSQL, Oracle, SQL Server | Organiza os dados em tabelas com linhas e colunas, com relações predefinidas entre elas. |
| **Não Relacional (NoSQL) - Documento** | MongoDB, CouchDB | Armazena dados em documentos flexíveis, como JSON ou BSON, sem um esquema rígido. |
| **Não Relacional (NoSQL) - Chave-Valor** | Redis, Amazon DynamoDB | Armazena dados em pares de chave-valor, sendo um dos modelos mais simples. |
| **Não Relacional (NoSQL) - Colunar** | Apache Cassandra, HBase | Armazena dados em colunas em vez de linhas, otimizado para consultas em grandes volumes de dados. |

---

### b. Quais os principais problemas de utilizar Sistemas de Arquivos para armazenagem de dados.

Utilizar sistemas de arquivos tradicionais (como planilhas ou arquivos de texto) para gerenciar dados apresenta várias desvantagens em comparação com um SGBD:

* **Redundância e Inconsistência de Dados:** A mesma informação pode ser duplicada em vários arquivos. Alterar um dado em um local e não nos outros gera inconsistência.
* **Dificuldade no Acesso aos Dados:** É necessário criar um novo programa para cada nova tarefa ou consulta de dados. Não há uma linguagem de consulta padrão.
* **Isolamento de Dados:** Os dados estão espalhados em vários arquivos e formatos diferentes, tornando difícil a criação de aplicações que acessem dados de mais de um arquivo.
* **Problemas de Integridade:** As restrições de integridade (por exemplo, garantir que o valor de um campo seja positivo) são difíceis de implementar e precisam ser codificadas em cada aplicação que acessa os dados.
* **Problemas de Atomicidade:** Se ocorrer uma falha durante uma operação (por exemplo, uma transferência bancária que debita de uma conta, mas falha antes de creditar na outra), o sistema de arquivos não garante que os dados permaneçam em um estado consistente.
* **Anomalias de Acesso Concorrente:** O acesso simultâneo por vários usuários pode levar a inconsistências se não for gerenciado adequadamente, algo que sistemas de arquivos não fazem nativamente.
* **Problemas de Segurança:** É difícil aplicar políticas de segurança complexas, como permitir que certos usuários vejam apenas parte dos dados em um arquivo.

---

### c. Descreva os três elementos básicos de um Modelo Entidade Relacionamento (MER).

O Modelo Entidade-Relacionamento (MER) é uma abordagem de modelagem de dados que representa a estrutura lógica de um banco de dados. Seus três elementos básicos são:

1.  **Entidade:** É um objeto do mundo real que é distinguível de outros objetos. Uma entidade pode ser uma pessoa, um lugar, um objeto, um evento ou um conceito sobre o qual armazenamos informações. Por exemplo: `ALUNO`, `CURSO`, `CARRO`. No diagrama, é geralmente representada por um retângulo.

2.  **Atributo:** É uma propriedade ou característica que descreve uma entidade. Cada entidade possui atributos que a definem. Por exemplo, a entidade `ALUNO` pode ter os atributos `Matricula`, `Nome` e `DataNascimento`. Atributos podem ser de vários tipos: simples, compostos, monovalorados, multivalorados e derivados.

3.  **Relacionamento:** Representa uma associação entre duas ou mais entidades. Ele descreve como as entidades interagem umas com as outras. Por exemplo, um `ALUNO` pode estar **matriculado em** um `CURSO`. O relacionamento "matriculado em" conecta as entidades `ALUNO` e `CURSO`. Relacionamentos são caracterizados pela sua **cardinalidade**, que define o número de instâncias de uma entidade que podem se associar a instâncias de outra entidade.

---

