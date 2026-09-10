## Q1. O modelo de dados entidade-relacionamento foi desenvolvido para facilitar o projeto de banco de dados, permitindo especificação de um esquema que representa a estrutura lógica geral de um banco de dados. Descreva os três elementos básicos de um Modelo Entidade Relacionamento (MER).
 
O MER é composto por três elementos fundamentais:
 
1. **Entidades**
   Representam objetos ou conceitos do mundo real sobre os quais se deseja armazenar informações (ex.: Cliente, Funcionário, Projeto). Cada entidade dá origem a um conjunto de ocorrências (instâncias) com as mesmas características. No diagrama, geralmente são representadas por retângulos.
2. **Atributos**
   Descrevem as propriedades ou características de uma entidade (ou de um relacionamento). Podem ser simples, compostos, multivalorados, derivados ou identificadores (chave). Exemplo: a entidade *Cliente* pode ter os atributos `código`, `nome` e `email`.
3. **Relacionamentos**
   Representam as associações (interações) entre duas ou mais entidades. Todo relacionamento possui uma **cardinalidade**, que indica quantas ocorrências de uma entidade podem se associar a quantas ocorrências de outra (1:1, 1:N, N:M), e uma **participação** (total ou parcial), que indica se toda ocorrência da entidade participa obrigatoriamente do relacionamento.
---
