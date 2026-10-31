# 1. Identificação e Repositório

**Discente:** Helena Dantas Mariano

**Usuário no GitHub:** [HelenaMariano2025](https://github.com/HelenaMariano2025)

**E-mail acadêmico:** helena.mariano.123@ufrn.edu.br

**Repositório pessoal público:** [dct2201-banco-de-dados](https://github.com/HelenaMariano2025/dct2201-banco-de-dados)

# 2. Respostas às Perguntas Discursivas dos Passos Práticos

### Pergunta Discursiva 1

**Explique com suas palavras a diferença entre criar uma tabela (DDL) e inserir registros nessa tabela (DML). Se apagarmos uma tabela com um comando DDL (`DROP TABLE`), o que acontece com os dados que estavam dentro dela?**

**Resposta:**

DDL (Data Definition Language) é a linguagem utilizada para definir e modificar a estrutura do banco de dados, como criar, alterar e excluir tabelas. Um exemplo é o comando `CREATE TABLE`, utilizado para criar uma tabela.

Já DML (Data Manipulation Language) é utilizada para manipular os dados armazenados nas tabelas, permitindo inserir, consultar, atualizar e excluir registros, por meio de comandos como `INSERT`, `SELECT`, `UPDATE` e `DELETE`.

Quando executamos o comando `DROP TABLE`, a tabela é removida do banco de dados, incluindo sua estrutura e todos os registros armazenados nela. Portanto, essa operação causa a perda dos dados daquela tabela.

### Pergunta Discursiva 2

**Descreva com suas palavras o que aconteceu quando você tentou executar o comando `DROP TABLE autores` com a conta `app_biblioteca`. Por que o MariaDB recusou a operação com o erro 1142? De que forma essa restrição protege a integridade do banco de dados caso a aplicação web sofra uma invasão ou falha de programação?**

**Resposta:**

Ao executar o comando `DROP TABLE autores` utilizando a conta `app_biblioteca`, o MariaDB recusou a operação e apresentou o erro 1142, informando que o usuário não possuía autorização para executar esse comando.

Isso aconteceu porque essa conta recebeu apenas permissões de consulta e manipulação de dados, como `SELECT`, `INSERT`, `UPDATE` e `DELETE`, não possuindo privilégios para excluir tabelas.

Essa restrição segue o princípio do menor privilégio, que consiste em conceder a cada usuário somente as permissões necessárias para realizar suas funções. Dessa forma, caso a aplicação web sofra uma invasão ou apresente uma falha de programação, o invasor ou o próprio sistema não terá autorização para excluir a estrutura das tabelas, reduzindo os riscos de danos ao banco de dados.

### Pergunta Discursiva 3

**Por que os usuários foram criados com o host `'%'` em vez de `'localhost'`? Qual é o papel da rede interna do Docker nessa decisão técnica?**

**Resposta:**

Os usuários foram criados com o host `'%'` porque essa configuração permite conexões a partir de diferentes endereços de origem, não restringindo o acesso somente à própria máquina onde o MariaDB está instalado.

Em um ambiente Docker, o MariaDB e o CloudBeaver são executados em contêineres separados, que se comunicam por meio de uma rede interna. Assim, a conexão realizada pelo CloudBeaver chega ao MariaDB através do endereço de rede do contêiner, e não necessariamente como uma conexão local (`localhost`).

Por isso, utilizar `'%'` permite que os usuários do banco de dados sejam autenticados nas conexões realizadas pela rede interna do Docker. Entretanto, as permissões concedidas a cada usuário continuam limitando as operações que ele pode executar.

### Pergunta Discursiva 4

**Quantos autores e livros no total ficaram cadastrados na sua base após a execução da carga expandida? O que aconteceria se você tentasse inserir um livro cujo `autor_id` fosse 999 (um autor inexistente)? Qual regra do banco impede essa ação?**

**Resposta:**

Após a execução do povoamento inicial e da carga expandida, o banco de dados ficou com 14 autores e 30 livros cadastrados. Inicialmente, foram inseridos 4 autores e 5 livros. Posteriormente, foram adicionados mais 10 autores e 25 livros, utilizando dados gerados com auxílio de inteligência artificial.

Caso fosse realizada uma tentativa de inserir um livro com `autor_id = 999`, sendo esse identificador inexistente na tabela `autores`, o MariaDB recusaria a operação e apresentaria um erro de violação de chave estrangeira.

Isso acontece devido à regra de integridade referencial, implementada por meio da chave estrangeira (`FOREIGN KEY`). Essa regra garante que todo livro cadastrado esteja associado a um autor existente, evitando relacionamentos inválidos entre as tabelas.

### Pergunta Discursiva 5

**Analise as Consultas 4 e 5. Em linguagem simples, qual é a vantagem prática de dividir os dados em duas tabelas relacionadas (`autores` e `livros`) em vez de guardar o nome e o país do autor repetido dentro de cada linha da tabela de livros?**

**Resposta:**

Dividir os dados em duas tabelas relacionadas permite organizar melhor as informações e evitar repetições desnecessárias. Na tabela `autores`, ficam armazenadas as informações de cada autor, como nome, país e ano de nascimento. Já na tabela `livros`, ficam os dados das obras, incluindo o identificador do autor responsável.

Essa organização evita que o nome e o país de um mesmo autor precisem ser repetidos em todos os seus livros. Além disso, caso seja necessário atualizar alguma informação do autor, basta modificá-la em um único registro na tabela `autores`.

As consultas 4 e 5 demonstram essa relação por meio do comando `JOIN`, que permite combinar informações das duas tabelas. Dessa forma, é possível consultar os livros e seus respectivos autores, além de calcular informações como o preço médio dos livros de cada autor.

Portanto, essa divisão facilita a manutenção dos dados, reduz a duplicação de informações e contribui para a consistência e a organização do banco de dados.

# 3. Respostas Dissertativas Conceituais

### Questão a: 

**Por que uma aplicação comercial nunca deve se conectar ao banco de dados utilizando o usuário root? O que pode ocorrer com o servidor de banco de dados caso as credenciais do usuário da aplicação sejam vazadas?**

**Resposta:**

Uma aplicação comercial não deve utilizar o usuário root, pois ele possui privilégios administrativos, permitindo criar e excluir bancos, modificar tabelas e gerenciar usuários. Caso suas credenciais sejam vazadas, um invasor poderá comprometer todo o servidor, causando exposição, alteração ou perda de dados.

Durante o Bloco A, observamos a importância da proteção das credenciais ao alterar a senha root no arquivo .env. Mesmo após a reinicialização dos containers, a senha antiga continuou funcionando devido à persistência do volume. Também verificamos que o Docker Compose impede a inicialização quando uma variável obrigatória, como MARIADB_ROOT_PASSWORD, está ausente. Além disso, a criação de dois ambientes independentes demonstrou a importância de separar configurações, portas e volumes.

Por isso, deve-se aplicar o princípio do menor privilégio, utilizando um usuário exclusivo para a aplicação e concedendo apenas as permissões necessárias. No nosso ambiente, o usuário app_biblioteca recebeu permissões de consulta e manipulação de registros, mas não pôde excluir tabelas, como comprovado no teste com DROP TABLE autores. Dessa forma, mesmo que suas credenciais sejam vazadas, os possíveis danos ficam limitados às permissões concedidas.


### Questão b: 

**Qual é a diferença fundamental entre privilégios DDL (Data Definition Language) e DML (Data Manipulation Language)? Por que é uma boa prática de segurança separá-los em contas de usuários distintas?**

**Resposta:**

Os privilégios DDL estão relacionados à definição e à estrutura do banco de dados, permitindo operações como criar, alterar e excluir tabelas (CREATE, ALTER e DROP). Já os privilégios DML permitem manipular os dados existentes, por meio de operações como consultar, inserir, atualizar e excluir registros (SELECT, INSERT, UPDATE e DELETE).

Durante o Bloco B, essa diferença ficou evidente quando tentamos criar a tabela emprestimos utilizando o usuário app_biblioteca. A operação foi negada porque esse usuário não possuía o privilégio CREATE, sendo necessário utilizar o usuário root para realizar a criação. Depois disso, utilizamos o usuário da aplicação para as operações de manipulação de dados, respeitando suas permissões.

Separar esses privilégios em contas distintas é uma boa prática de segurança porque evita que usuários responsáveis pelas operações do sistema possam modificar ou excluir a estrutura do banco de dados. Assim, mesmo que as credenciais de uma aplicação sejam comprometidas, o invasor terá limitações para realizar alterações estruturais, reduzindo os riscos de perda de dados e comprometimento do banco.


### Questão c: 

**Por que o arquivo .env.example deve ser commitado no repositório de código enquanto o arquivo .env nunca deve ser versionado? Quais são os riscos e consequências práticas de comitar credenciais reais em um repositório público no GitHub?**

**Resposta:**

O arquivo .env.example deve ser versionado porque apresenta as variáveis necessárias para configurar o projeto, utilizando valores fictícios. Já o .env contém credenciais reais, como senhas, e deve permanecer privado.

Comitar credenciais em um repositório público pode permitir acessos não autorizados ao banco de dados, causando vazamento, alteração ou exclusão de informações. Por isso, é importante utilizar o .gitignore para proteger esses arquivos.

No Bloco C, criamos o usuário relatorios com acesso restrito à consulta da tabela livros. Testamos suas permissões e verificamos o funcionamento dos comandos GRANT e REVOKE, concedendo e revogando temporariamente o privilégio de inserção.

Também elaboramos o arquivo setup.sql, com o objetivo de automatizar a criação do banco biblioteca, suas tabelas, restrições, dados e usuários. Por fim, trabalhamos com a proteção das credenciais, diferenciando arquivos de configuração públicos e privados.

As atividades permitiram compreender a importância do controle de privilégios, da segurança das credenciais e da automação na administração de bancos de dados.

### Questão d: 

**O uso do arquivo .env e a inclusão no .gitignore eliminam por completo todos os riscos de segurança de credenciais em um ambiente de desenvolvimento e produção? Justifique sua resposta considerando que o arquivo permanece armazenado em texto puro no sistema de arquivos do servidor.**

**Resposta:**

Não. O uso do .env e sua inclusão no .gitignore ajudam a proteger as credenciais contra a publicação acidental no repositório, mas não eliminam todos os riscos. Como o arquivo permanece armazenado em texto puro no servidor, pessoas que obtiverem acesso ao sistema poderão visualizar as senhas. Por isso, é importante restringir as permissões de acesso, proteger o servidor e utilizar ferramentas de gerenciamento de segredos em ambientes de produção.

### Questão e: 

**O que é um contêiner e quais são as principais vantagens de utilizar o Docker para provisionar ambientes de banco de dados em atividades didáticas de graduação em comparação com a instalação manual do SGBD diretamente no sistema operacional do computador do aluno?**

**Resposta:**

Um contêiner é uma unidade isolada que reúne uma aplicação e suas dependências para que ela funcione em diferentes ambientes. O Docker permite criar e executar esses contêineres de maneira prática e padronizada.

Em atividades didáticas, sua principal vantagem é facilitar a instalação e configuração dos SGBDs, evitar conflitos com programas já instalados no computador e permitir que todos os alunos utilizem ambientes semelhantes. Além disso, facilita a criação, remoção e reprodução dos ambientes, tornando as atividades mais simples e organizadas do que a instalação manual diretamente no sistema operacional.


# 10. Consultas Obrigatórias (Leitura de Dados com SELECT)

### Consulta 1: Seleção completa de livros

**Comando SQL utilizado:**

```sql
SELECT * FROM livros;
```

**Resultado obtido:**

|id|titulo|ano_publicacao|preco|autor_id|
|--|------|--------------|-----|--------|
|1|Dom Casmurro|1899|39.90|1|
|2|Memórias Póstumas de Brás Cubas|1881|45.00|1|
|3|A Hora da Estrela|1977|32.50|2|
|4|Cem Anos de Solidão|1967|59.90|3|
|5|Orgulho e Preconceito|1813|29.90|4|
|6|O Guarani|1857|34.90|5|
|7|Iracema|1865|29.90|5|
|8|Senhora|1875|39.90|5|
|9|Capitães da Areia|1937|42.90|6|
|10|Gabriela, Cravo e Canela|1958|49.90|6|
|11|Dona Flor e Seus Dois Maridos|1966|45.90|6|
|12|O Sítio do Picapau Amarelo|1920|35.90|7|
|13|Urupês|1918|32.90|7|
|14|Mensagem|1934|39.90|8|
|15|Livro do Desassossego|1982|55.90|8|
|16|Os Miseráveis|1862|59.90|9|
|17|O Corcunda de Notre-Dame|1831|49.90|9|
|18|Oliver Twist|1838|44.90|10|
|19|Um Conto de Duas Cidades|1859|49.90|10|
|20|David Copperfield|1850|54.90|10|
|21|A Revolução dos Bichos|1945|35.90|11|
|22|1984|1949|42.90|11|
|23|Assassinato no Expresso do Oriente|1934|45.90|12|
|24|E Não Sobrou Nenhum|1939|39.90|12|
|25|Morte no Nilo|1937|42.90|12|
|26|O Velho e o Mar|1952|37.90|13|
|27|Adeus às Armas|1929|43.90|13|
|28|Romancero Gitano|1928|39.90|14|
|29|Bodas de Sangue|1933|34.90|14|
|30|A Casa de Bernarda Alba|1936|36.90|14|

### Consulta 2: Projeção de atributos e ordenação descendente

**Comando SQL utilizado:**

```sql
SELECT titulo, ano_publicacao
FROM livros
ORDER BY ano_publicacao DESC;
```

**Resultado obtido:**

|titulo|ano_publicacao|
|------|--------------|
|Livro do Desassossego|1982|
|A Hora da Estrela|1977|
|Cem Anos de Solidão|1967|
|Dona Flor e Seus Dois Maridos|1966|
|Gabriela, Cravo e Canela|1958|
|O Velho e o Mar|1952|
|1984|1949|
|A Revolução dos Bichos|1945|
|E Não Sobrou Nenhum|1939|
|Capitães da Areia|1937|
|Morte no Nilo|1937|
|A Casa de Bernarda Alba|1936|
|Assassinato no Expresso do Oriente|1934|
|Mensagem|1934|
|Bodas de Sangue|1933|
|Adeus às Armas|1929|
|Romancero Gitano|1928|
|O Sítio do Picapau Amarelo|1920|
|Urupês|1918|
|Dom Casmurro|1899|
|Memórias Póstumas de Brás Cubas|1881|
|Senhora|1875|
|Iracema|1865|
|Os Miseráveis|1862|
|Um Conto de Duas Cidades|1859|
|O Guarani|1857|
|David Copperfield|1850|
|Oliver Twist|1838|
|O Corcunda de Notre-Dame|1831|
|Orgulho e Preconceito|1813|

### Consulta 3: Filtragem condicional (WHERE)

**Comando SQL utilizado:**

```sql
SELECT *
FROM livros
WHERE ano_publicacao < 1900;
```

**Resultado obtido:**

|id|titulo|ano_publicacao|preco|autor_id|
|--|------|--------------|-----|--------|
|1|Dom Casmurro|1899|39.90|1|
|2|Memórias Póstumas de Brás Cubas|1881|45.00|1|
|5|Orgulho e Preconceito|1813|29.90|4|
|6|O Guarani|1857|34.90|5|
|7|Iracema|1865|29.90|5|
|8|Senhora|1875|39.90|5|
|16|Os Miseráveis|1862|59.90|9|
|17|O Corcunda de Notre-Dame|1831|49.90|9|
|18|Oliver Twist|1838|44.90|10|
|19|Um Conto de Duas Cidades|1859|49.90|10|
|20|David Copperfield|1850|54.90|10|

### Consulta 4: Junção relacional (INNER JOIN) entre livros e autores

**Comando SQL utilizado:**

```sql
SELECT l.titulo, a.nome AS autor, l.preco
FROM livros l
JOIN autores a ON l.autor_id = a.id;
```

**Resultado obtido:**

|titulo|autor|preco|
|------|-----|-----|
|Dom Casmurro|Machado de Assis|39.90|
|Memórias Póstumas de Brás Cubas|Machado de Assis|45.00|
|A Hora da Estrela|Clarice Lispector|32.50|
|Cem Anos de Solidão|Gabriel García Márquez|59.90|
|Orgulho e Preconceito|Jane Austen|29.90|
|O Guarani|José de Alencar|34.90|
|Iracema|José de Alencar|29.90|
|Senhora|José de Alencar|39.90|
|Capitães da Areia|Jorge Amado|42.90|
|Gabriela, Cravo e Canela|Jorge Amado|49.90|
|Dona Flor e Seus Dois Maridos|Jorge Amado|45.90|
|O Sítio do Picapau Amarelo|Monteiro Lobato|35.90|
|Urupês|Monteiro Lobato|32.90|
|Mensagem|Fernando Pessoa|39.90|
|Livro do Desassossego|Fernando Pessoa|55.90|
|Os Miseráveis|Victor Hugo|59.90|
|O Corcunda de Notre-Dame|Victor Hugo|49.90|
|Oliver Twist|Charles Dickens|44.90|
|Um Conto de Duas Cidades|Charles Dickens|49.90|
|David Copperfield|Charles Dickens|54.90|
|A Revolução dos Bichos|George Orwell|35.90|
|1984|George Orwell|42.90|
|Assassinato no Expresso do Oriente|Agatha Christie|45.90|
|E Não Sobrou Nenhum|Agatha Christie|39.90|
|Morte no Nilo|Agatha Christie|42.90|
|O Velho e o Mar|Ernest Hemingway|37.90|
|Adeus às Armas|Ernest Hemingway|43.90|
|Romancero Gitano|Federico García Lorca|39.90|
|Bodas de Sangue|Federico García Lorca|34.90|
|A Casa de Bernarda Alba|Federico García Lorca|36.90|

### Consulta 5: Agrupamento e cálculo de média (GROUP BY e AVG)

**Comando SQL utilizado:**

```sql
SELECT a.nome AS autor, AVG(l.preco) AS preco_medio
FROM autores a
JOIN livros l ON a.id = l.autor_id
GROUP BY a.id, a.nome;
```

**Resultado obtido:**

|autor|preco_medio|
|-----|-----------|
|Machado de Assis|42.450000|
|Clarice Lispector|32.500000|
|Gabriel García Márquez|59.900000|
|Jane Austen|29.900000|
|José de Alencar|34.900000|
|Jorge Amado|46.233333|
|Monteiro Lobato|34.400000|
|Fernando Pessoa|47.900000|
|Victor Hugo|54.900000|
|Charles Dickens|49.900000|
|George Orwell|39.400000|
|Agatha Christie|42.900000|
|Ernest Hemingway|40.900000|
|Federico García Lorca|37.233333|

### Consulta 6: Subconsulta comparativa

**Comando SQL utilizado:**

```sql
SELECT *
FROM livros
WHERE preco > (SELECT AVG(preco) FROM livros);
```

**Resultado obtido:**

|id|titulo|ano_publicacao|preco|autor_id|
|--|------|--------------|-----|--------|
|2|Memórias Póstumas de Brás Cubas|1881|45.00|1|
|4|Cem Anos de Solidão|1967|59.90|3|
|9|Capitães da Areia|1937|42.90|6|
|10|Gabriela, Cravo e Canela|1958|49.90|6|
|11|Dona Flor e Seus Dois Maridos|1966|45.90|6|
|15|Livro do Desassossego|1982|55.90|8|
|16|Os Miseráveis|1862|59.90|9|
|17|O Corcunda de Notre-Dame|1831|49.90|9|
|18|Oliver Twist|1838|44.90|10|
|19|Um Conto de Duas Cidades|1859|49.90|10|
|20|David Copperfield|1850|54.90|10|
|22|1984|1949|42.90|11|
|23|Assassinato no Expresso do Oriente|1934|45.90|12|
|25|Morte no Nilo|1937|42.90|12|
|27|Adeus às Armas|1929|43.90|13|