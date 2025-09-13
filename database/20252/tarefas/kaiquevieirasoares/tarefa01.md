# Tarefa 01 - Conceitos BD e MER

**Nome:** Kaique Vieira Soares  

**Usuário do GitHub:** kaiquevieirasoares  

**E-mail:** kaique.vieira.168@ufrn.edu.br  

---

## Seção A: Banco de Dados e SGBD

Um **Banco de Dados (BD)** é uma coleção organizada de dados que podem ser acessados, gerenciados e atualizados de forma eficiente. Ele tem como objetivo centralizar e estruturar informações para que possam ser utilizadas de maneira consistente.  

Um **Sistema Gerenciador de Banco de Dados (SGBD)** é um software responsável por administrar, controlar o acesso, armazenar, recuperar e manter a integridade e a segurança dos dados em um banco de dados.  

**Exemplos:**  
- Banco de Dados: MySQL Database, PostgreSQL Database, Oracle Database, MongoDB Database.  
- SGBDs correspondentes: MySQL, PostgreSQL, Oracle DBMS, MongoDB.  

---

## Seção B: Problemas ao utilizar Sistemas de Arquivos para armazenar dados

1. **Redundância e Inconsistência de Dados** – o mesmo dado pode estar duplicado em vários arquivos, dificultando a manutenção.  
2. **Dificuldade de Acesso** – para realizar consultas complexas é necessário programar manualmente, sem padronização.  
3. **Isolamento de Dados** – dados ficam espalhados em múltiplos arquivos sem integração.  
4. **Problemas de Integridade** – ausência de mecanismos para garantir regras de negócio (ex: restrições).  
5. **Dificuldade de Compartilhamento e Confiabilidade** – acesso simultâneo não é controlado adequadamente.  
6. **Falta de Segurança** – não existem controles de autenticação, autorização e auditoria robustos.  

---

## Seção C: Modelo Entidade-Relacionamento (MER)

O **MER** é um modelo conceitual criado para facilitar o projeto de banco de dados, permitindo representar a **estrutura lógica geral** de forma independente de implementação. Seus três elementos básicos são:  

1. **Entidades** – representam objetos ou conceitos do mundo real que possuem existência independente. Exemplo: *Cliente*, *Produto*.  
2. **Atributos** – características ou propriedades que descrevem uma entidade ou relacionamento. Exemplo: *nome*, *CPF*, *preço*.  
3. **Relacionamentos** – associações entre entidades. Exemplo: *Cliente compra Produto*.  

---

## Seção D: Notações em Diagramas ER

Existem várias **notações** gráficas para modelar Diagramas ER, e cada uma pode representar os mesmos conceitos de forma diferente.  

**Exemplos:**  

- **Cardinalidade:**  
  - Notação de Pé de Galinha (Crow’s Foot): usa “pés” para indicar 1:1, 1:N, N:M.  
  - Notação de Chen: indica cardinalidade por meio de números (1, N, M) próximos às entidades.  
  - Notação UML: usa intervalos como (0..1), (1..*).  

- **Entidade Subordinada (Herança / Especialização):**  
  - Notação de Chen: triângulo representando a especialização.  
  - Notação UML: generalização com seta vazada apontando para a superclasse.  

- **Atributos:**  
  - Notação de Chen: elipses conectadas à entidade.  
  - Notação UML: listados diretamente dentro da caixa da entidade.  

Essas variações de notação permitem representar os mesmos conceitos de maneiras diferentes, dependendo da ferramenta ou da preferência metodológica.  
