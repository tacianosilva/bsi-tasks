# Tarefa 01 - Conceitos BD e MER

**Nome:** Felipe Iago Dantas  
**Usuário GitHub:** Felipe-Dantas31  
**E-mail:** liodan31@gmail.com  

---

## a. Banco de Dados e SGBD

Um **Banco de Dados (BD)** é um conjunto estruturado de dados inter-relacionados que representa informações sobre um domínio específico, armazenados de forma organizada para facilitar o acesso e gerenciamento. Um **Sistema Gerenciador de Banco de Dados (SGBD)** é um software que fornece ferramentas para criar, manipular e administrar bancos de dados, garantindo integridade, segurança e eficiência.

**Exemplos:**
- Bancos de Dados: MySQL, PostgreSQL, MongoDB, Oracle
- SGBDs: MySQL Workbench, pgAdmin, Oracle SQL Developer, MongoDB Compass

---

## b. Problemas de Sistemas de Arquivos

Os principais problemas incluem:
1. **Redundância de dados** - mesma informação armazenada em múltiplos arquivos
2. **Inconsistência** - dados desatualizados em diferentes arquivos
3. **Dificuldade de acesso** - consultas complexas são difíceis de implementar
4. **Problemas de integridade** - falta de mecanismos para validação de dados
5. **Isolamento de dados** - informações dispersas em vários arquivos
6. **Segurança limitada** - controle de acesso menos sofisticado
7. **Concorrência inadequada** - dificuldade em gerenciar acesso simultâneo

---

## c. Elementos do Modelo Entidade-Relacionamento (MER)

Os três elementos fundamentais são:
1. **Entidades** - objetos do mundo real que possuem existência independente (ex: Empregado, Departamento)
2. **Atributos** - características que descrevem as entidades (ex: nome, código, data)
3. **Relacionamentos** - associações significativas entre entidades (ex: trabalha_em, pertence_a)

---

## d. Notações para Diagramas ER

Principais notações e suas diferenças:

1. **Notação de Peter Chen (Original)**
   - Entidades: retângulos
   - Relacionamentos: losangos
   - Atributos: elipses
   - Cardinalidade: 1:N, M:N, etc.

2. **Notação Crow's Foot (Pé de Galinha)**
   - Entidades: retângulos
   - Relacionamentos: linhas com símbolos
   - Cardinalidade: | (um), >| (muitos), O (opcional)

3. **Notação UML (Unified Modeling Language)**
   - Entidades: classes
   - Relacionamentos: associações
   - Cardinalidade: 1, 1..*, 0..1, etc.

**Diferenças na representação:**
- Entidade fraca: Chen (retângulo duplo) vs UML (<<weak>>)
- Cardinalidade: Chen (1:N) vs Crow's Foot (símbolos gráficos) vs UML (1..*)
- Atributos: Chen (elipses) vs UML (dentro da classe)

---

## e. Diagrama ER para Controle de Frequência

```mermaid
erDiagram
    EMPREGADO ||--o{ REGISTRO_PONTO : "possui"
    EMPREGADO {
        int codigo PK
        string nome
        string email
        string tipo
    }
    
    EMPREGADO ||--|{ EMP_LIVRE : "pode ser"
    EMP_LIVRE {
        int horas_mensais
        int minimo_horas_dia
    }
    
    EMPREGADO ||--|{ EMP_TURNO : "pode ser"
    EMP_TURNO ||--o{ TURNO : "trabalha"
    
    TURNO {
        int id PK
        time hora_inicio
        time hora_fim
    }
    
    DIA_SEMANA ||--o{ TURNO : "possui"
    DIA_SEMANA {
        string codigo PK "dom, seg, ter..."
        string nome "Domingo, Segunda..."
    }
    
    REGISTRO_PONTO {
        int id PK
        date data
        time entrada
        time saida
    }
