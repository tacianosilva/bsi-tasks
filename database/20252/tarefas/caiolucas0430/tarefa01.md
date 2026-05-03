 Tarefa 01 - Conceitos de BD e MER

**Nome:** <Caio Lucas>  
**Usuário GitHub:** <caiolucas0430>  
**E-mail:** <caiolucas0430@gmail.com>  

---

## 1. Banco de Dados e SGBD
Um banco de dados é como uma biblioteca digital. Ele organiza e armazena informações de forma estruturada, permitindo que você as acesse, gerencie e atualize facilmente. Por exemplo, o registro de clientes de uma loja, as vendas de uma empresa ou os dados de alunos em uma escola são todos exemplos de bancos de dados. 

Um **Sistema Gerenciador de Banco de Dados (SGBD)** é o software que permite criar, gerenciar e manipular bancos de dados.  
Exemplos de SGBDs:  
- MySQL  
- PostgreSQL  
- Oracle  
- SQL Server  
- MongoDB  

---

## 2. Problemas dos Sistemas de Arquivos
Usar apenas sistemas de arquivos para armazenar dados apresenta problemas, como:
- **Redundância e inconsistência** (informações duplicadas e desatualizadas).  
- **Dificuldade de acesso** (não há linguagem de consulta estruturada).  
- **Falta de segurança** (sem controle de acesso adequado).  
- **Falta de integridade** (não há mecanismos para garantir regras dos dados).  
- **Dificuldade em manter e atualizar** os arquivos.  

---

## 3. Modelo Entidade-Relacionamento (MER)
Os três elementos básicos de um MER são:
- **Entidades:** objetos ou conceitos do mundo real que queremos representar (ex: Empregado, Turno).  
- **Relacionamentos:** associações entre entidades (ex: Empregado → TrabalhaEm → Turno).  
- **Atributos:** propriedades que descrevem entidades ou relacionamentos (ex: nome, e-mail, horário de início).  

---

## 4. Notações para Diagramas ER
Existem várias notações para representar Diagramas ER. Algumas delas:  
- **Notação de Chen:** entidades como retângulos, relacionamentos como losangos, atributos como elipses.  
- **Notação de Crow’s Foot (pés de galinha):** muito usada em engenharia de software, mostra claramente a cardinalidade (1:1, 1:N, N:M).  
- **Notação UML:** utiliza diagramas de classes para representar entidades e relacionamentos.  

Exemplo de variação para **cardinalidade**:  
- Chen: `1:N` escrito próximo às entidades.  
- Crow’s Foot: símbolos de pé de galinha para "muitos" e uma linha simples para "um".  

---

## 5. Diagrama ER
erDiagram
    EMPREGADO {
        int codigo PK
        string nome
        string email
    }

    TIPO_EMPREGADO {
        string tipo PK
    }
    
    HORARIO_LIVRE {
        int horas_mensais
        int periodo_minimo_diario
    }
    
    TURNO_FIXO {
        string hora_inicio
        string hora_fim
    }

    DIA_DA_SEMANA {
        string codigo PK
        string nome
    }
    
    PONTO {
        datetime hora_entrada PK
        datetime hora_saida
    }

    EMPREGADO }o--|| TIPO_EMPREGADO : tem
    EMPREGADO ||--|{ HORARIO_LIVRE : tem
    EMPREGADO ||--|{ TURNO_FIXO : tem

    EMPREGADO ||--|{ PONTO : registra
    TURNO_FIXO }o--|| PONTO : pertence_a
    DIA_DA_SEMANA }o--|| PONTO : registrado_em
    
    TURNO_FIXO }o--|| DIA_DA_SEMANA : ocorre_em

    ---