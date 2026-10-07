```mermaid


erDiagram
    CLIENTE {
        string codigo PK
        string nome
        string email_contato
    }
    
    PROJETO {
        string codigo PK
        string nome
        string descricao
    }
    
    FUNCIONARIO {
        string codigo PK
        string nome
        string email
        string papel
    }
    
    SQUAD {
        string codigo PK
        string nome
    }
    
    SPRINT {
        string codigo PK
        string objetivo
        date data_inicio
        date data_fim
    }

    TAREFA {
        string codigo PK
        string descricao
        string prioridade
        string situacao
        int estimativa_horas
    }
    
    RELEASE {
        string codigo PK
        string versao
        date data_lancamento
    }
    
    TESTE_VALIDACAO {
        string codigo PK
        string tipo
        string resultado
    }

    CLIENTE ||--o{ PROJETO : "possui"
    PROJETO ||--o{ TAREFA : "contém"
    SQUAD ||--o{ FUNCIONARIO : "integra"
    SQUAD ||--o{ SPRINT : "executa"
    SPRINT ||--o{ TAREFA : "organiza"
    SQUAD ||--o{ TAREFA : "resolve"
    CLIENTE ||--o{ RELEASE : "recebe"
    SQUAD ||--o{ RELEASE : "planeja"
    RELEASE }|--|{ TAREFA : "agrupa"
    RELEASE ||--o{ TESTE_VALIDACAO : "passa_por" 

    