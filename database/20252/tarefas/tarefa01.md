# Tarefa 01 - Conceitos BD e MER

**Nome:** Arthur De Medeiros Dantas  

**Usuário do GitHub:** THUR165  

**E-mail:** arthur.dantas.017@ufrn.edu.br  

---

## Seção A: Banco de Dados e SGBD

Um **Banco de Dados (BD)** é um conjunto estruturado de informações organizadas de forma a permitir fácil acesso, manipulação e atualização. Ele é utilizado para centralizar dados e garantir consistência nas operações.  

Um **Sistema Gerenciador de Banco de Dados (SGBD)** é o software responsável por criar, manipular, controlar acesso e manter a integridade do banco de dados.  

**Exemplos:**  
- Banco de Dados: Microsoft SQL Server Database, Firebase Database, Neo4j Database, Cassandra Database.  
- SGBDs correspondentes: SQL Server, Firebase, Neo4j, Apache Cassandra.  

---

## Seção B: Problemas ao utilizar Sistemas de Arquivos para armazenar dados  

1. **Falta de padronização** – cada arquivo pode ter formato diferente.  
2. **Manutenção difícil** – qualquer alteração exige modificações manuais em vários arquivos.  
3. **Acesso ineficiente** – consultas complexas são complicadas de implementar.  
4. **Ausência de integridade** – não há restrições para evitar erros como duplicação de dados.  
5. **Confiabilidade baixa** – perda ou corrupção de arquivos compromete os dados.  
6. **Controle de concorrência inexistente** – múltiplos usuários acessando ao mesmo tempo podem causar conflitos.  

---

## Seção C: Modelo Entidade-Relacionamento (MER)  

O **MER** é usado no projeto de banco de dados para representar, de forma conceitual, os elementos de um sistema. Seus três elementos básicos são:  

1. **Entidades** – objetos ou conceitos que podem ser identificados no mundo real. Exemplo: *Aluno*, *Curso*.  
2. **Atributos** – informações que descrevem as entidades ou relacionamentos. Exemplo: *nome*, *data de nascimento*, *carga horária*.  
3. **Relacionamentos** – ligações entre entidades, representando interações. Exemplo: *Aluno matricula-se em Curso*.  

---