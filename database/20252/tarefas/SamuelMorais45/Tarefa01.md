# Tarefa 01 - Conceitos BD e MER  

**Nome:** Samuel Morais de Araujo 
**Usuário GitHub:** SamuelMorais45  
**E-mail:** morais123samuel@gmail.com 


## 1. Descreva o que é um Banco de Dados e o que é um Sistema Gerenciador de Banco de Dados. Cite exemplos de Bancos de Dados e seus SGBDs.  

Um Banco de Dados (BD) é uma coleção organizada de informações que podem ser facilmente acessadas, gerenciadas e atualizadas. Ele armazena dados de forma estruturada, permitindo consultas e manipulação eficiente.  

Um Sistema Gerenciador de Banco de Dados (SGBD) é um software que possibilita a criação, manipulação e gerenciamento de bancos de dados. Ele fornece ferramentas para segurança, integridade e controle de acesso aos dados.  

**Exemplos:**  
- Banco de Dados: MySQL Database, Oracle Database, PostgreSQL Database, MongoDB.  
- SGBD: MySQL, Oracle, PostgreSQL, MongoDB Server.  

## 2. Quais os principais problemas de utilizar Sistemas de Arquivos para armazenagem de dados.

- Redundância e inconsistência de dados: informações duplicadas podem gerar conflitos.  
- Dificuldade de acesso aos dados: não há uma linguagem padronizada como o SQL.  
- Falta de integridade e segurança: não existem mecanismos robustos de restrição e autenticação.  
- Problemas de concorrência: múltiplos acessos simultâneos podem corromper os dados.  
- Manutenção complexa: difícil escalabilidade e adaptação para novos requisitos.  

## 3. O modelo de dados entidade-relacionamento foi desenvolvido para facilitar o projeto de banco de dados, permitindo especificação de um esquema que representa a estrutura lógica geral de um banco de dados. Descreva os três elementos básicos de um Modelo Entidade Relacionamento (MER).

1. Entidades: representações de objetos do mundo real que possuem relevância no sistema (ex.: Empregado, Turno, Dia da Semana).  
2. Relacionamentos: associações entre entidades (ex.: Empregado trabalha em Turno).  
3. Atributos: características que descrevem entidades e relacionamentos (ex.: nome, e-mail, horário início).  

## 4. Pesquise sobre as várias notações possíveis para Diagramas ER, cite alguns exemplos de notações diferentes para o mesmo conceito (ex: Cardinalidade, Entidade Subordinada,etc.).

Os Diagramas Entidade-Relacionamento (ER) podem ser representados de diferentes formas, de acordo com a notação escolhida. Cada notação define um conjunto de símbolos gráficos para entidades, relacionamentos, atributos e cardinalidades.  

 Principais Notações  

1. Notação de Chen 
   - Entidades → retângulos.  
   - Relacionamentos → losangos.  
   - Atributos → elipses conectadas às entidades ou relacionamentos.  
   - Cardinalidade → indicada com números ou símbolos próximos às entidades.  
   - Exemplo: Empregado (retângulo) — Trabalha_em (losango) — Projeto (retângulo).  

2. Notação Crow’s Foot (pé de galinha) 
   - Entidades → retângulos.  
   - Relacionamentos → linhas conectando entidades.  
   - Cardinalidade → representada por símbolos nas extremidades da linha:  
     - Pé de galinha (três tracinhos) = muitos (N).  
     - Traço simples = um (1).  
     - Bolinha = zero (0).  
   - Exemplo: Um Departamento (1) possui (pé de galinha) vários Empregados (N).  

3. Notação UML (Unified Modeling Language)  
   - Muito usada em projetos de software orientado a objetos.  
   - Entidades → classes (retângulos divididos em seções).  
   - Relacionamentos → associações (linhas).  
   - Cardinalidade → escrita como *multiplicidade* próxima à associação (ex.: 0..1, 1..*, 1..1).  
   - Exemplo: Um Empregado (1..1) pode estar associado a vários Projetos (0..*).  

---

 Comparação de um mesmo conceito em diferentes notações  

- Cardinalidade (1 para N):  
  - Chen: (1, N).  
  - Crow’s Foot: │───< (pé de galinha).  
  - UML: 1..1 ↔ 0..*.  

- Entidade Subordinada (Especialização):  
  - Chen: entidade geral ligada a entidades específicas com um triângulo.  
  - Crow’s Foot: relacionamento com linha hierárquica.  
  - UML: herança (seta com triângulo aberto apontando para a superclasse).  

## 5. Construa um Diagrama ER para projetar uma base de dados de um Sistema de Controle de Freqüência de Empregados de uma organização. A base de dados não deve conter redundância de dados. O modelo ER deve ser representado com um diagrama usando Mermaid.js. O modelo deve apresentar, ao menos, entidades, relacionamentos, atributos, identificadores e restrições de cardinalidade. O modelo deve ser feito no nível conceitual, sem incluir chaves estrangeiras.

```mermaid
erDiagram
    EMPREGADO {
        int codigo PK
        string nome
        string email
        string tipo
    }

    EMPREGADO_LIVRE {
        int horas_mes
        int horas_min_dia
    }

    EMPREGADO_FIXO {
        string descricao
    }

    TURNO {
        int id_turno PK
        string hora_inicio
        string hora_fim
    }

    DIA_SEMANA {
        string codigo PK
        string nome
    }

    PONTO {
        int id_ponto PK
        string hora_entrada
        string hora_saida
    }

    EMPREGADO ||--o{ EMPREGADO_LIVRE : "especialização"
    EMPREGADO ||--o{ EMPREGADO_FIXO : "especialização"
    EMPREGADO_FIXO }o--o{ TURNO : "atua_em"
    TURNO }o--|| DIA_SEMANA : "ocorre_em"
    EMPREGADO ||--o{ PONTO : "registra"
    TURNO ||--o{ PONTO : "referencia"
    DIA_SEMANA ||--o{ PONTO : "referencia"
