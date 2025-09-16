<h2> Tarefa 01 - Conceitos BD e MER <h2>
Nome: Juliany Tairis de Oliveira Borges </br>
Usuário Github: jtairis</br>
Email: juliany.borges.142@ufrn.edu.br
<hr>
<h3>Banco de Dados e SGBD</h3>

Um Banco de Dados (BD) é um conjunto de informações organizadas de forma estruturada, com o objetivo de facilitar o armazenamento, a recuperação e a manipulação de dados. Em outras palavras, é como uma “coleção organizada” que guarda dados de forma lógica. Já o Sistema Gerenciador de Banco de Dados (SGBD) é o software que faz a ponte entre o usuário/aplicação e o banco de dados em si. Ele controla a forma como os dados são gravados, consultados, alterados e removidos, garantindo integridade, segurança e desempenho.

Exemplos:
- Banco de dados: MySQL Database, Oracle Database, PostgreSQL, MongoDB.
- SGBDs correspondentes: MySQL Server, Oracle DBMS, PostgreSQL DBMS, MongoDB Server.

<h3> Problemas ao usar Sistemas de Arquivos para armazenar dados</h3>

Antes dos SGBDs, muitas empresas utilizavam arquivos convencionais (como planilhas ou textos) para guardar informações. Esse modelo trazia diversos problemas, como:
- Redundância de dados: a mesma informação ficava repetida em vários arquivos.
- Dificuldade de acesso: era complicado buscar e cruzar dados entre diferentes arquivos.
- Baixa segurança: qualquer um com acesso poderia alterar informações sem controle.
- Inconsistência: quando um dado era alterado em um arquivo, muitas vezes não era atualizado em outros.
- Manutenção complexa: mudar a estrutura ou corrigir erros exigia retrabalho enorme.

<h3>Modelo Entidade-Relacionamento (MER)</h3>

O MER é uma forma de representar visualmente como os dados de um sistema se organizam e se relacionam. Ele ajuda a planejar a estrutura lógica de um banco de dados antes da implementação. Os três elementos básicos do MER são:

1- Entidades – representam objetos do mundo real ou conceitos importantes, que possuem atributos (ex.: Cliente, Produto).
2- Relacionamentos – mostram como as entidades se conectam entre si (ex.: um Cliente “realiza” um Pedido).
3- Atributos – características ou propriedades de uma entidade ou relacionamento (ex.: nome do cliente, preço do produto).

<h3>Notações em Diagramas ER</h3>

Existem diferentes formas gráficas de representar MER, chamadas de notações. Cada uma usa símbolos ou estilos próprios, mas todas têm a mesma função: mostrar entidades, atributos e relacionamentos.
Alguns exemplos:

<h4>Cardinalidade:</h4>

 - Notação de pé de galinha (Crow’s Foot) → usa símbolos como “pé de galinha” para representar 1:1, 1:N, N:M.

 - Notação de Chen → utiliza números ou descrições ao lado das linhas (1, N).

<h4>Entidade subordinada (ou entidade fraca):</h4>

- Em Chen → desenhada com um retângulo duplo.

- Em Crow’s Foot → diferenciada por estilos de linhas ou identificadores próprios.
Essas variações existem porque diferentes autores e ferramentas adotam convenções distintas, mas no fim todas transmitem as mesmas ideias.
