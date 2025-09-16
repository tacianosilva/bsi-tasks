# Tarefa 01 - Conceitos BD e MER

Nome: Isaque Guimarães
Usuário GitHub: @Isaqueguicar
E-mail:

---

5. Diagrama ER - Sistema de Controle de Frequência (nível conceitual)
Requisitos resumidos (implementados no ER):
- Empregados: identificados por código, nome, e-mail. Existem 2 tipos: *livre* e *fixo*.  
- Empregados do tipo *livre*: horas por mês e mínimo de horas por dia.  
- Empregados do tipo *fixo*: têm turnos (início, fim) e a semana é organizada por dias (código/nome). Podem ter até 2 turnos por dia.  
- Todos os empregados registram ponto (entrada/saída) em cada turno/dia.

Diagrama em Mermaid.js:

```mermaid
erDiagram
    EMPREGADO {
        int codigo PK
        string nome
        string email
        string tipo
    }

    EMPREGADO ||--o{ BATE_PONTO : "registra"
    BATE_PONTO {
        int id_ponto PK
        datetime hora_entrada
        datetime hora_saida
    }

    EMPREGADO ||--|{ EMPREGADO_LIVRE : "é"
    EMPREGADO_LIVRE {
        int horas_mes
        int minimo_horas_dia
    }

    EMPREGADO ||--|{ EMPREGADO_FIXO : "é"
    EMPREGADO_FIXO ||--o{ TURNO : "tem"
    TURNO {
        int id_turno PK
        time hora_inicio
        time hora_fim
    }

    TURNO }o--|| DIA_SEMANA : "ocorre_em"
    DIA_SEMANA {
        string codigo PK
        string nome
    }
