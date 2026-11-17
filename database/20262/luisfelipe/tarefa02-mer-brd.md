Q1
O Modelo Entidade-Relacionamento (MER) fundamenta-se em três elementos básicos para abstrair o mundo real e representar a estrutura lógica de um banco de dados:

* **Entidades:** Representam objetos, pessoas, lugares ou conceitos do mundo real que possuem existência própria e sobre os quais o sistema precisa armazenar informações (ex.: *Cliente*, *Funcionário*, *Projeto*). Podem ser concretas (como um objeto físico) ou abstratas (como uma venda ou um contrato).
* **Atributos:** São as propriedades, características ou qualificadores que descrevem as entidades ou os relacionamentos (ex.: *Nome*, *E-mail*, *Data de Nascimento*). Dentre os atributos, destaca-se o identificador (ou chave), que possui a função de distinguir de forma única cada ocorrência de uma entidade.
* **Relacionamentos:** Definem as conexões, vínculos ou associações lógicas existentes entre duas ou mais entidades, refletindo a dinâmica e as regras de negócio da aplicação (ex.: um *Funcionário* **pertence a** uma *Squad*).

Q2
Existem diversas notações para Diagramas Entidade-Relacionamento (DER), desenvolvidas para atender a diferentes níveis de abstração (conceitual e lógico) e padrões da indústria.

| Conceito | Notação de Chen | Notação Pé de Galinha (*Crow's Foot*) | Notação UML |
| --- | --- | --- | --- |
| **Entidade** | Retângulo | Retângulo | Classe (Retângulo estruturado) |
| **Relacionamento** | Losango contendo o nome da ação | Linha conectando as entidades | Linha (Associação) conectando as classes |
| **Atributos** | Elipses (óvalos) conectadas à entidade | Texto listado dentro da caixa da entidade | Atributos listados na seção interna da classe |
| **Cardinalidade (1:N)** | Rótulos $1$ e $N$ (ou min/máx entre parênteses) | Símbolo de "pé de galinha" no lado $N$ e traço no lado $1$ | Notação de intervalo nas pontas (ex.: `1` e `0..*`) |
| **Entidade Fraca** | Retângulo duplo com losango duplo | Cantos arredondados ou linha de conexão contínua | Classe vinculada por composição (losango preenchido) |

**Exemplos Práticos de Notações Diferentes**

* **Cardinalidade / Multiplicidade (Muitos para Vários):**
* *Chen:* Adiciona rótulos explícitos nas linhas de conexão com os caracteres **1**, **N** ou limites explícitos como `(0,N)`.
* *Crow's Foot:* Utiliza marcadores gráficos nas extremidades da linha. Um círculo representa opcionalidade (`0`), um traço representa obrigatoriedade (`1`) e três ramificações representam "muitos" (`>`).
* *UML:* Utiliza a notação de intervalos explícitos nas pontas das linhas, como `1..1` (exatamente um) ou `0..*` (zero a muitos).


* **Entidade Subordinada / Fraca (depende de outra para existir/identificar-se):**
* *Chen:* Desenhada com **retângulo duplo**, unida por um **losango duplo** à entidade forte.
* *Crow's Foot:* Utiliza uma linha **sólida/contínua** no relacionamento para demonstrar identificação compulsória (em relacionamentos não-identificadores, a linha é tracejada).
* *IDEF1X:* Representa entidades dependentes com **cantos arredondados** na caixa da entidade, diferente das independentes que possuem cantos retos.


* **Atributo Identificador (Chave Primária):**
* *Chen:* Elipse com o texto do atributo **sublinhado**.
* *Crow's Foot:* O atributo é posicionado na **seção superior** do retângulo da entidade, com a indicação `PK` ao lado.
* *UML:* O atributo recebe um estereótipo `<<PK>>` ou símbolo de visibilidade especial.

Q3
erDiagram
    CLIENTE {
        int codigo_cliente PK
        string nome
        string email
    }

    PROJETO {
        int codigo_projeto PK
        string nome
    }

    FUNCIONARIO {
        int codigo_funcionario PK
        string nome
        string email
        string papel
    }

    SQUAD {
        int codigo_squad PK
        string nome
    }

    TAREFA {
        int codigo_tarefa PK
        string descricao
        string prioridade
        string situacao
        int estimativa_horas
    }

    SPRINT {
        int codigo_sprint PK
        date data_inicio
        date data_fim
    }

    RELEASE {
        int codigo_release PK
        date data_liberacao
        string resultado_validacao
    }

    CLIENTE ||--|{ PROJETO : "contrata"
    PROJETO ||--|{ TAREFA : "contem"
    SQUAD ||--|{ FUNCIONARIO : "aloca"
    SQUAD ||--o{ TAREFA : "resolve"
    SQUAD ||--o{ SPRINT : "executa"
    SQUAD ||--o{ RELEASE : "planeja"
    CLIENTE ||--o{ RELEASE : "recebe"
    SPRINT ||--o{ TAREFA : "organiza"
    RELEASE }|--|{ TAREFA : "agrupa"

Q4
A seguir, apresenta-se o **mapeamento do Diagrama ER para o Modelo Relacional**. As Chaves Primárias (**PK**) e Chaves Estrangeiras (**FK**) estão explicitadas para cada relação:

---

### **1. CLIENTE**

Armazena as empresas clientes contratantes.

* **CLIENTE** (**`codigo_cliente`** [PK], `nome`, `email`)
* **PK:** `codigo_cliente`



---

### **2. PROJETO**

Projetos contratados por cada cliente.

* **PROJETO** (**`codigo_projeto`** [PK], `nome`, `codigo_cliente` [FK])
* **PK:** `codigo_projeto`
* **FK:** `codigo_cliente` referencia `CLIENTE(codigo_cliente)`



---

### **3. SQUAD**

Equipes de desenvolvimento de software.

* **SQUAD** (**`codigo_squad`** [PK], `nome`)
* **PK:** `codigo_squad`



---

### **4. FUNCIONARIO**

Membros das equipes com seus respectivos papéis.

* **FUNCIONARIO** (**`codigo_funcionario`** [PK], `nome`, `email`, `papel`, `codigo_squad` [FK])
* **PK:** `codigo_funcionario`
* **FK:** `codigo_squad` referencia `SQUAD(codigo_squad)`



---

### **5. SPRINT**

Iterações de trabalho conduzidas pelas squads.

* **SPRINT** (**`codigo_sprint`** [PK], `data_inicio`, `data_fim`, `codigo_squad` [FK])
* **PK:** `codigo_sprint`
* **FK:** `codigo_squad` referencia `SQUAD(codigo_squad)`



---

### **6. TAREFA**

Atividades/issues a serem resolvidas.

* **TAREFA** (**`codigo_tarefa`** [PK], `descricao`, `prioridade`, `situacao`, `estimativa_horas`, `codigo_projeto` [FK], `codigo_squad` [FK], `codigo_sprint` [FK, opcional])
* **PK:** `codigo_tarefa`
* **FK:** `codigo_projeto` referencia `PROJETO(codigo_projeto)`
* **FK:** `codigo_squad` referencia `SQUAD(codigo_squad)`
* **FK:** `codigo_sprint` referencia `SPRINT(codigo_sprint)` *(pode ser nula até a tarefa ser alocada em uma sprint)*



---

### **7. RELEASE**

Entregas/versões planejadas por uma squad para um cliente.

* **RELEASE** (**`codigo_release`** [PK], `data_liberacao`, `resultado_validacao`, `codigo_squad` [FK], `codigo_cliente` [FK])
* **PK:** `codigo_release`
* **FK:** `codigo_squad` referencia `SQUAD(codigo_squad)`
* **FK:** `codigo_cliente` referencia `CLIENTE(codigo_cliente)`



---

### **8. RELEASE_TAREFA** (Tabela Intermediária do Relacionamento N:M)

Associa as tarefas incluídas em cada release.

* **RELEASE_TAREFA** (**`codigo_release`** [PK][FK], **`codigo_tarefa`** [PK][FK])
* **PK Composta:** (`codigo_release`, `codigo_tarefa`)
* **FK1:** `codigo_release` referencia `RELEASE(codigo_release)`
* **FK2:** `codigo_tarefa` referencia `TAREFA(codigo_tarefa)`

Q5
* **Vinculação de Projetos a Clientes:** Um **PROJETO** só pode ser criado se estiver associado a um **CLIENTE** previamente cadastrado. Não é permitido excluir um cliente da base enquanto existirem projetos associados a ele (*ON DELETE RESTRICT*).
* **Alocação de Funcionários em Squads:** Todo **FUNCIONARIO** deve estar vinculado a uma **SQUAD** existente. A exclusão de uma squad não deve ser permitida enquanto houver funcionários alocados nela.
* **Composição Obrigatória de Squad (Liderança):** Toda **SQUAD** deve possuir pelo menos um **FUNCIONARIO** associado cujo atributo `papel` seja classificado como "Líder Técnico".
* **Atribuição e Origem de Tarefas:** Uma **TAREFA** só pode ser cadastrada se estiver vinculada a um **PROJETO** existente e a uma **SQUAD** responsável. A remoção do projeto ou da squad impede a permanência do registro da tarefa sem dono.
* **Vínculo de Tarefas com Sprints:** Uma **TAREFA** só pode referenciar uma **SPRINT** que exista no banco de dados. Caso uma sprint seja removida, a referência na tarefa correspondente deve ser definida como nula (*ON DELETE SET NULL*), mantendo a tarefa na base para replanejamento.
* **Execução de Sprints:** Uma **SPRINT** só pode ser planejada e iniciada se estiver diretamente associada a uma **SQUAD** existente.
* **Planejamento de Releases:** Uma **RELEASE** só pode ser criada se estiver associada a uma **SQUAD** responsável e a um **CLIENTE** destinatário devidamente cadastrados.
* **Associação entre Releases e Tarefas:** Um registro na tabela intermediária **RELEASE_TAREFA** só pode existir se referenciar uma **RELEASE** e uma **TAREFA** válidas. Se uma release ou uma tarefa for excluída, os vínculos correspondentes nesta tabela associativa devem ser removidos automaticamente (*ON DELETE CASCADE*).