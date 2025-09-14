# Tarefa 01 - Conceitos BD e MER
José Guilherme Silva de Araújo | oguiaraujo | guilherme.araujo.702@ufrn.edu.br

## Banco de dados e SGBDs
Um Banco de Dados (BD) é uma coleção organizada e estruturada de dados, armazenados eletronicamente em um sistema de
computador. O seu propósito fundamental é armazenar e permitir a recuperação de informações de maneira eficiente,
confiável e segura.

Um Sistema Gerenciador de Banco de Dados (SGBD) é o software que atua como uma interface entre o usuário/aplicação e o
banco de dados. Ele é responsável por gerenciar e controlar o acesso aos dados, permitindo a criação, consulta,
atualização e exclusão de informações.

### Exemplos:
**Relacional:** 	Oracle Database, MySQL, PostgreSQL  
**Não Relacional (NoSQL):** MongoDB, Couchbase, Redis, Amazon DynamoDB

## Principais problemas ao utilizar sistemas de arquivo para armazenar dados
* **Redundância e Inconsistência:** Dados duplicados em vários arquivos causam inconsistências.

* **Dificuldade de Acesso:** Exige a criação de programas específicos para cada nova consulta, tornando o acesso
ineficiente.

* **Isolamento de Dados:** Informações espalhadas em diferentes formatos dificultam a criação de uma visão integrada.

* **Falta de Integridade:** É difícil impor regras para garantir a validade e a consistência dos dados.

* **Falhas de Atomicidade:** Operações com múltiplos passos podem falhar no meio, corrompendo os dados.

* **Erros de Concorrência:** Acesso simultâneo por vários usuários pode levar a resultados incorretos.

* **Falta de segurança:** É complexo controlar as permissões de acesso e alteração dos dados.

## Três elementos básicos de um Modelo Entidade Relacionamento (MER)

**1. Entidade:** Representa um objeto do mundo real sobre o qual se deseja armazenar informações. Uma entidade pode ser
algo concreto (como Aluno, Carro, Produto) ou abstrato (como Venda, Matrícula, Conta). Em um diagrama, é geralmente
representada por um retângulo.

**2. Atributo:** Descreve uma propriedade ou característica de uma entidade. Por exemplo, a entidade Aluno pode ter os
atributos Matricula, Nome e CPF. Em um diagrama, são geralmente representados por elipses ligadas à sua entidade.

**3. Relacionamento:** Representa uma associação ou interação entre duas ou mais entidades. Por exemplo, um Aluno se
matricula em um Curso. O nome do relacionamento (no caso, "se matricula em") descreve a associação entre as entidades
Aluno e Curso. Em um diagrama, é geralmente representado por um losango.