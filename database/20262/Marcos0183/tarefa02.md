#

# Q1

### Entidade
Representa um objeto do mundo real(físico ou abstrato) sobre o qual o sistema precisa armazenar informações. Graficamente, é representado por um rentângulo.
### Atributo 
São as características, propriedades ou campos que descrevem uma entidade. Graficamente, é representado por uma elipse ou círculo ligado à entidade.
### Relacionamento
Define a associação ou ligação lógica entre duas ou mais entidades, decrevendo como elas interagem. Graficamente, é representado por um losango

#

# Q2

### Pé de Galinha
Linha com terminações em ramificações(três pontas para "muitos", traço perpendicular para "um", círculo para "zero"). Entidades representadas em retângulos divididos em duas seções. Os atributos são listados diretamente na entidade(dentro do retângulo).

### Peter Chen
Retângulos(Entidades), Losangolos(Relacionementos) e Elipses(Atributos).

### IDEF1X
Caixas com cantos arrendodados ou retos, círculos cheios/vazios no final das linhas para relacionamentos. Atrobutos ficam na caixa da entidade, divididos por uma linha horizontal.

### UML 
Classes(Retângulos divididos em 3 partes) com atributos e métodos, multiplicidade nas pontas(1..*,0..1).

### Barker
Caixas com cantos arredondados, linhas contínuas, tracejados, com "pé de galinha" em uma extremidade.

#

# Q3

### Relações


- EMPRESA (1,1) -- ◇ Empresa_Cliente ◇ -- (0,N) CLIENTE;
- EMPRESA (1,1) -- ◇ Empresa_Equipe ◇ -- (0,N) EQUIPE;
- EMPRESA (1,1) -- ◇ Empresa_Funcionario ◇ -- (1,N) FUNCIONARIO;
- EQUIPE (1,N) -- ◇ Equipe_Funcionario ◇ -- (1,N) FUNCIONARIO;
- EQUIPE (1,1) -- ◇ Equipe_Release ◇ -- (0,N) RELEASE;
- EQUIPE (1,1) -- ◇ Equipe_Interacao ◇ -- (0,N) INTERACAO;
- CLIENTE (1,1) -- ◇ Tarefa_de_Clientes ◇ -- (0,N) TAREFA;
- CLIENTE (1,1) -- ◇ Cliente_Release ◇ -- (0,N) RELEASE;
- TAREFA (1,1) -- ◇ Tarefa_Validacao ◇ -- (1,N).




```mermaid

---
config:
  theme: dark
  layout: elk
---
erDiagram
    EMPRESA{}

    CLIENTE{
        string codigo
        string e-mail
        string nome
    }

    EQUIPE{

    }

    FUNCIONARIO{
        string codigo
        string e-mail
        string nome
        string funcao
    }

    TAREFA {
        string codigo
        string descricao
        string prioridade
        string situcao
        string est_horas
    }

    INTERACAO{

    }

    RELEASE{

    }

    VALIDACAO{

    }


    EMPRESA ||--o{ CLIENTE : Empresa_Cliente
    EMPRESA ||--o{ EQUIPE : Empresa_Equipe
    EMPRESA ||--o{ FUNCIONARIO : Empresa_Funcionario
    EQUIPE  }|--|{ FUNCIONARIO: Equipe_Funcionario
    EQUIPE  ||--o{ TAREFA: Equipe_Tarefa
    EQUIPE  ||--o{ RELEASE: Equipe_Release
    EQUIPE  ||--o{ INTERACAO: Equipe_Iteracao
    CLIENTE ||--o{ TAREFA: Tarefa_de_Clientes
    CLIENTE ||--o{ RELEASE: Cliente_Release
    TAREFA  ||--o{ VALIDACAO: Tarefa_Validacao






```