## Q1. O modelo de dados entidade-relacionamento foi desenvolvido para facilitar o projeto de banco de dados, permitindo especificação de um esquema que representa a estrutura lógica geral de um banco de dados. Descreva os três elementos básicos de um Modelo Entidade Relacionamento (MER).
 
O MER é composto por três elementos fundamentais:
 
1. **Entidades**
   Representam objetos ou conceitos do mundo real sobre os quais se deseja armazenar informações (ex.: Cliente, Funcionário, Projeto). Cada entidade dá origem a um conjunto de ocorrências (instâncias) com as mesmas características. No diagrama, geralmente são representadas por retângulos.
2. **Atributos**
   Descrevem as propriedades ou características de uma entidade (ou de um relacionamento). Podem ser simples, compostos, multivalorados, derivados ou identificadores (chave). Exemplo: a entidade *Cliente* pode ter os atributos `código`, `nome` e `email`.
3. **Relacionamentos**
   Representam as associações (interações) entre duas ou mais entidades. Todo relacionamento possui uma **cardinalidade**, que indica quantas ocorrências de uma entidade podem se associar a quantas ocorrências de outra (1:1, 1:N, N:M), e uma **participação** (total ou parcial), que indica se toda ocorrência da entidade participa obrigatoriamente do relacionamento.
   
---

## Q2. Pesquise sobre as várias notações possíveis para Diagramas ER e cite alguns exemplos de notações diferentes para o mesmo conceito (ex.: cardinalidade, entidade subordinada, etc.).
 
Existem diversas notações para representar o Modelo ER, sendo as mais conhecidas: **Notação de Chen**, **Notação de Crow's Foot (Pé de Galinha)**, **Notação de Bachman**, **Notação Min-Max (ISO)** e **UML (para diagramas de classe usados como ER)**. Elas divergem principalmente na forma de representar cardinalidade, entidades fracas/subordinadas e atributos.
 
### Exemplo 1 — Cardinalidade "um para muitos" (1:N)
 
| Notação | Representação |
|---|---|
| Chen | Losango com o relacionamento rotulado e os números "1" e "N" escritos nas linhas que ligam às entidades |
| Crow's Foot (Pé de Galinha) | Uma linha reta (lado "1") e uma linha terminando em "pé de galinha" ‑ um garfo de três pontas (lado "N") |
| Min-Max (ISO) | Pares `(0,1)` ou `(1,1)` e `(0,N)` ou `(1,N)` escritos próximos a cada entidade |
| UML | Multiplicidades escritas como `1` e `0..*` ou `1..*` nas extremidades da associação |
 
### Exemplo 2 — Entidade fraca / subordinada
 
| Notação | Representação |
|---|---|
| Chen | Retângulo de borda dupla para a entidade fraca e losango de borda dupla para o relacionamento identificador |
| Crow's Foot | Entidade desenhada com cantos arredondados ou com um símbolo diferenciado; a linha de conexão costuma ter um traço adicional indicando dependência de existência |
| UML | Um losango vazado (agregação) ou preenchido (composição) na extremidade da entidade "forte", indicando que a entidade dependente não existe sem ela |
 
### Exemplo 3 — Atributos
 
| Notação | Representação |
|---|---|
| Chen | Elipses ligadas por linhas à entidade; elipse tracejada para atributo derivado; elipse com contorno duplo para atributo multivalorado |
| Crow's Foot | Atributos listados dentro do próprio retângulo da entidade (como colunas de uma tabela), sem elipses separadas |
| UML | Atributos listados em um compartimento específico da caixa de classe, com tipo de dado explícito (ex.: `nome : String`) |

---

