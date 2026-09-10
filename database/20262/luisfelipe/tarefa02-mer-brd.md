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