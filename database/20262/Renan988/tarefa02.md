# Tarefa 02 - MER e Projeto de Banco de Dados Relacional

##  Q1. O modelo de dados entidade-relacionamento foi desenvolvido para facilitar o projeto de banco de dados, permitindo especificação de um esquema que representa a estrutura lógica geral de um banco de dados. Descreva os três elementos básicos de um Modelo Entidade Relacionamento (MER). 

O Modelo Entidade-Relacionamento fundamenta-se em três conceitos fundamentais para representar a estrutura lógica de um banco de dados:

1. **Entidades:** São objetos, coisas ou conceitos do mundo real que possuem existência independente e sobre os quais desejamos armazenar dados. No diagrama, são representadas por retângulos (ex: `Cliente`, `Produto`, `Funcionario`).
2. **Atributos:** São as propriedades, características ou descrições que qualificam uma entidade ou um relacionamento (ex: para a entidade `Cliente`, os atributos podem ser `CPF`, `Nome`, `Data_Nascimento`).
3. **Relacionamentos:** São as associações ou conexões lógicas que ocorrem.

## Q2. Notações para Diagramas ER

Ao longo dos anos, diferentes metodologias e padrões surgiram para representar visualmente os conceitos de um Modelo Entidade-Relacionamento (MER). Embora o objetivo principal seja sempre o mesmo — mapear entidades, atributos e relacionamentos —, a forma gráfica de expressar esses elementos muda consideravelmente dependendo da notação escolhida. 

Abaixo estão as principais notações utilizadas na modelagem de dados e como elas diferem na representação de conceitos específicos:

### 1. Principais Notações Existentes

*   **Notação de Chen (Original):** Criada por Peter Chen em 1976, é a abordagem clássica e amplamente utilizada em contextos acadêmicos. Nela, as entidades são retângulos, os atributos são elipses (bolinhas) ligadas às entidades, e os relacionamentos são representados por losangos.
*   **Notação Pé de Galinha (Crow's Foot / Information Engineering):** Muito comum no desenvolvimento de software comercial e ferramentas modernas de modelagem (como Lucidchart, dbdiagram.io, etc.). Ela elimina os losangos e elipses, transformando as entidades em tabelas compactas onde os atributos aparecem listados internamente, e utiliza símbolos bifurcados nas pontas das linhas para indicar a cardinalidade.
*   **Notação UML (Unified Modeling Language):** Originalmente voltada para a Orientação a Objetos, a UML possui um diagrama específico chamado *Diagrama de Classes* que frequentemente substitui o ERD tradicional. Nele, as entidades viram classes (retângulos divididos em compartimentos para nome, atributos e operações) e os relacionamentos são linhas com pontas numéricas indicando multiplicidade.
*   **Notação de Bachman:** Um dos modelos predecessores, focado em estruturas de redes e dados hierárquicos, onde setas e blocos indicam o fluxo e as dependências estruturais.

---

### 2. Exemplos Comparativos de Representação para o Mesmo Conceito

Para entender a divergência prática entre as abordagens, veja como diferentes notações tratam os mesmos conceitos estruturais:

*   **Cardinalidade (Ex: Relação 1 para N):**
    *   *Notação de Chen:* Utiliza letras ou números posicionados em cima das linhas que ligam a entidade ao losango de relacionamento (ex: `1` de um lado e `N` ou `M` do outro).
    *   *Notação Pé de Galinha:* Utiliza traços verticais para "um" e um símbolo ramificado (semelhante a um pé de galinha) para "muitos" na própria extremidade da linha de ligação entre as tabelas.
    *   *Notação UML:* Utiliza restrições textuais diretas nas pontas da associação (ex: `1..1` para um e somente um, e `0..*` para de zero a muitos).

*   **Entidade Fraca (Entidade que depende de uma forte para existir):**
    *   *Notação de Chen:* É representada por um **retângulo duplo** (duas bordas) e seu relacionamento com a entidade forte é desenhado com um **losango duplo**.
    *   *Notação Pé de Galinha:* Geralmente é representada visualmente como uma entidade comum, mas diferenciada pelo tipo de chave estrangeira que compõe sua chave primária composta (identificação dependente) ou por traços pontilhados na linha de relacionamento (relacionamento identificador).

*   **Atributos Multivalorados (Atributos que podem ter vários valores, como vários telefones para uma pessoa):**
    *   *Notação de Chen:* Utiliza uma **elipse dupla** ligada à entidade.
    *   *Notação Pé de Galinha / Relacional:* Como o modelo relacional puro não suporta atributos multivalorados em uma única coluna, essa notação exige a criação de uma **nova entidade filha** (uma tabela auxiliar) ligada por uma relação 1 para N.

    