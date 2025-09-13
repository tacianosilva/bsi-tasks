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