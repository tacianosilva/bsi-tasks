# Tarefa 03 --- Docker Compose, MariaDB e Administração de SGBD

> **Relatório de respostas --- DCT2201 / Banco de Dados**

## 1. Identificação e repositório

-   **Discente:** Thiago Alexandre Braga de Medeiros
-   **GitHub:** [@thiagobraga77](https://github.com/thiagobraga77)
-   **E-mail :** \thiagobraga2a@gmail.com\
-   **Repositório pessoal:**
    https://github.com/thiagobraga77/dct2201-banco-de-dados
-   **Arquivos da atividade:** `tarefa03/`



## 2. Respostas às perguntas discursivas

### Pergunta 1 --- Diferença entre DDL e DML

DDL é a linguagem utilizada para definir e modificar a estrutura do
banco de dados. Comandos como `CREATE TABLE`, `ALTER TABLE` e
`DROP TABLE` são exemplos. Já DML é utilizada para manipular os
registros armazenados, por meio de comandos como `INSERT`, `SELECT`,
`UPDATE` e `DELETE`.

Quando uma tabela é removida com `DROP TABLE`, sua estrutura e os
registros armazenados nela são excluídos. Por isso, esse comando deve
ser utilizado com cuidado, pois não remove apenas uma linha, mas a
tabela inteira.

### Pergunta 2 --- Erro 1142 e princípio do menor privilégio

Ao tentar executar `DROP TABLE autores` utilizando o usuário
`app_biblioteca`, o MariaDB recusou a operação e apresentou o erro 1142.
Isso aconteceu porque esse usuário recebeu permissões de manipulação de
dados --- `SELECT`, `INSERT`, `UPDATE` e `DELETE` ---, mas não recebeu
permissão para executar operações estruturais como `DROP`.

Essa restrição aplica o princípio do menor privilégio: cada conta recebe
somente as permissões necessárias para sua função. Assim, caso a
aplicação seja invadida ou apresente uma falha de programação, o invasor
não terá automaticamente permissão para remover tabelas e comprometer
toda a estrutura do banco.

### Pergunta 3 --- Uso do host `%`

Os usuários foram criados com o host `%` porque os serviços estão em
containers diferentes e se comunicam pela rede interna criada pelo
Docker Compose. Nesse cenário, a conexão do CloudBeaver com o MariaDB
não se origina do `localhost` do container do banco, mas de outro
endereço da rede Docker.

O `%` funciona como curinga para permitir conexões provenientes de
diferentes endereços. Em um ambiente real, essa permissão deve ser
restringida à rede ou aos hosts necessários sempre que possível.

### Pergunta 4 --- Povoamento expandido e integridade referencial

Após executar a carga inicial de quatro autores e cinco livros e
acrescentar os registros gerados com IA, a quantidade esperada é de **14
autores e pelo menos 30 livros**. A quantidade efetiva deve ser
confirmada no banco com:

``` sql
SELECT COUNT(*) AS total_autores FROM autores;
SELECT COUNT(*) AS total_livros FROM livros;
```

Se fosse inserido um livro com `autor_id = 999`, sem existir um autor
com esse identificador, o MariaDB recusaria a operação. A chave
estrangeira `FOREIGN KEY (autor_id) REFERENCES autores(id)` impede que
um livro seja associado a um autor inexistente. Essa regra mantém a
integridade referencial entre as tabelas.

### Pergunta 5 --- Vantagem de separar autores e livros

Manter autores e livros em tabelas relacionadas evita repetir o nome e o
país do autor em cada registro de livro. O livro armazena apenas o
identificador do autor, que é relacionado à chave primária da tabela
`autores`.

Essa organização reduz a duplicação de informações e facilita
atualizações. Por exemplo, se o país de um autor precisar ser corrigido,
a alteração será feita em um único registro, em vez de modificar várias
linhas da tabela de livros. Essa separação também ajuda a manter a
consistência dos dados.

## 3. Respostas dissertativas conceituais

### Questão A --- Por que uma aplicação não deve usar root?

Uma aplicação comercial não deve acessar o banco de dados usando `root`,
pois essa conta possui privilégios administrativos muito amplos. Se as
credenciais forem vazadas, uma pessoa mal-intencionada poderá alterar ou
apagar bancos, tabelas e usuários, além de comprometer a disponibilidade
e a integridade dos dados. O mais seguro é criar uma conta específica
para a aplicação, concedendo somente as permissões necessárias para suas
operações.

### Questão B --- Diferença entre privilégios DDL e DML

Privilégios DDL permitem criar, alterar ou remover estruturas do banco,
como bancos de dados e tabelas. Privilégios DML permitem consultar e
manipular os registros, por exemplo, inserir, atualizar ou excluir
dados.

Separar essas permissões em contas diferentes reduz os riscos. Uma
aplicação que precisa cadastrar e consultar informações normalmente não
precisa ter autorização para apagar tabelas ou modificar a estrutura do
banco.

### Questão C --- Por que versionar `.env.example`, mas não `.env`?

O arquivo `.env.example` documenta quais variáveis precisam ser
configuradas, utilizando valores genéricos ou instruções, sem expor
senhas reais. Por isso, ele pode ser enviado ao repositório para ajudar
outras pessoas a configurar o projeto.

O arquivo `.env` contém os valores efetivamente utilizados no ambiente
local, incluindo credenciais. Se for enviado a um repositório público,
outras pessoas poderão obter essas informações e tentar acessar o banco
ou outros serviços. Por esse motivo, `.env` deve estar no `.gitignore` e
não deve ser versionado.

### Questão D --- `.env` e `.gitignore` eliminam todos os riscos?

Não. O `.gitignore` evita que o Git inclua o arquivo em novos commits,
mas não criptografa seu conteúdo nem protege o arquivo contra pessoas
que tenham acesso ao sistema. O `.env` continua armazenado em texto puro
e pode ser exposto por permissões inadequadas, cópias de segurança
inseguras, malware ou acesso indevido ao servidor.

Em ambientes profissionais, também é importante restringir as permissões
do arquivo, proteger o servidor, evitar registrar segredos em logs e
utilizar mecanismos próprios de gerenciamento de segredos quando
disponíveis. Se uma credencial for exposta, ela deve ser substituída.

### Questão E --- O que é um container e quais as vantagens do Docker?

Um container é uma unidade isolada que executa uma aplicação e suas
dependências, utilizando recursos do sistema operacional hospedeiro. O
Docker facilita a criação e execução desses ambientes de maneira
padronizada.

Em uma atividade de banco de dados, o Docker permite instalar e iniciar
o MariaDB sem realizar uma instalação manual diretamente no sistema
operacional. Também facilita reproduzir o ambiente em outros
computadores, separar serviços, configurar portas e volumes e remover os
containers sem necessariamente perder os dados persistidos em volumes.
Isso torna os testes mais organizados e reduz conflitos com programas já
instalados.

## 4. Desafios práticos realizados



### Bloco A --- Docker e infraestrutura

#### Desafio 1 --- Alteração da porta do SGBD

No arquivo `.env`, a variável foi alterada para:

``` env
MARIADB_PORT=3307
```

Em seguida, os serviços foram atualizados:

``` bash
docker compose up -d
docker ps
```

O mapeamento esperado é `3307` no computador para `3306` dentro do
container (`3307:3306`). Como o CloudBeaver e o MariaDB estão na rede
interna do Compose, a conexão entre eles continua utilizando o host
`mariadb` e a porta interna `3306`. Clientes executados diretamente no
computador podem utilizar a porta externa `3307`.

#### Desafio 2 --- Dois ambientes simultâneos

Foram utilizadas duas pastas independentes, cada uma com seu próprio
`docker-compose.yml`, arquivo `.env` e volume. Para evitar conflitos, os
ambientes precisam utilizar nomes de containers, portas externas e
volumes diferentes.

Exemplo de distribuição:

  Serviço                                  Ambiente 1            Ambiente 2
  ------------------------------- ------------------- ---------------------
  MariaDB --- porta externa                      3307                  3308
  CloudBeaver --- porta externa                  8978                  8979
  Container MariaDB                     `lab-mariadb`       `lab-mariadb-2`
  Container CloudBeaver             `lab-cloudbeaver`   `lab-cloudbeaver-2`
  Volume                               `mariadb_data`      `mariadb_data_2`

Os quatro containers podem ser conferidos com:

``` bash
docker ps
```

#### Desafio 3 --- Persistência do volume e alteração da senha root

Alterar `MARIADB_ROOT_PASSWORD` no `.env` e executar
`docker compose up -d` não altera a senha de um banco que já foi
inicializado. A imagem do MariaDB utiliza essa variável durante a
inicialização inicial do diretório de dados. Depois disso, a senha fica
armazenada nos dados persistidos pelo volume.

Há dois caminhos para alterar a senha: executar `ALTER USER` conectado
ao MariaDB com uma conta administrativa; ou remover e recriar o volume
com `docker compose down -v` e depois `docker compose up -d`. O segundo
caminho apaga os dados armazenados no volume e só deve ser utilizado
quando essa perda for desejada.

#### Desafio 4 --- Validação estrita `:?`

A variável da senha no `docker-compose.yml` utiliza uma expressão
semelhante a:

``` yaml
MARIADB_ROOT_PASSWORD: ${MARIADB_ROOT_PASSWORD:?defina MARIADB_ROOT_PASSWORD no arquivo .env}
```

O modificador `:?` faz o Docker Compose interromper a interpretação da
configuração quando a variável não está definida ou está vazia,
apresentando a mensagem indicada. Isso evita iniciar o serviço sem uma
senha root configurada. Em ambientes profissionais, validações desse
tipo ajudam a detectar configurações incompletas antes da execução.

#### Desafio 5 --- Inspeção das variáveis no Compose

O comando utilizado foi:

``` bash
docker compose config
```

Ele valida e apresenta a configuração final do Compose após resolver as
variáveis. Entre as variáveis interpoladas estão
`MARIADB_ROOT_PASSWORD`, `MARIADB_DATABASE` e `MARIADB_PORT`. A saída
pode conter credenciais; por isso, não deve ser publicada sem remover os
segredos.

### Bloco B --- Modelagem e consultas SQL básicas

#### Desafio 6 --- Criação da tabela de empréstimos

``` sql
USE biblioteca;

CREATE TABLE emprestimos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    livro_id INT,
    data_emprestimo DATE,
    devolvido BOOLEAN,
    FOREIGN KEY (livro_id) REFERENCES livros(id)
);
```

A tabela registra os empréstimos e utiliza `livro_id` como chave
estrangeira para relacionar cada empréstimo a um livro existente.

#### Desafio 7 --- Carga da tabela de empréstimos

``` sql
INSERT INTO emprestimos
    (livro_id, data_emprestimo, devolvido)
VALUES
    (1, '2026-10-10', FALSE),
    (2, '2026-10-15', FALSE),
    (3, '2026-10-20', TRUE);
```

Foram inseridos três registros: dois empréstimos pendentes e um
devolvido. Os identificadores `1`, `2` e `3` precisam existir na tabela
`livros`; caso os IDs sejam diferentes no banco, os valores devem ser
ajustados.

#### Desafio 8 --- Consulta de pendências

``` sql
SELECT
    l.titulo,
    e.data_emprestimo,
    a.nome AS autor
FROM emprestimos e
JOIN livros l ON e.livro_id = l.id
JOIN autores a ON l.autor_id = a.id
WHERE e.devolvido = FALSE;
```

A consulta relaciona empréstimos, livros e autores. A condição
`WHERE e.devolvido = FALSE` retorna somente os empréstimos que ainda não
foram devolvidos.

#### Desafio 9 --- Filtragem com HAVING

``` sql
SELECT
    a.nome AS autor,
    COUNT(l.id) AS quantidade_livros
FROM autores a
JOIN livros l ON a.id = l.autor_id
GROUP BY a.id, a.nome
HAVING COUNT(*) > 1;
```

A consulta agrupa os livros por autor, conta as obras de cada grupo e
utiliza `HAVING` para apresentar somente autores com mais de um livro
cadastrado.

#### Desafio 10 --- Atualização proporcional

``` sql
UPDATE livros
SET preco = preco * 1.10
WHERE id = 1;
```

O comando aumenta em 10% o preço do livro de identificador `1`. O filtro
`WHERE` limita a alteração a esse registro. O novo valor pode ser
conferido com:

``` sql
SELECT id, titulo, preco
FROM livros
WHERE id = 1;
```

#### Desafio 11 --- Remoção condicional

``` sql
INSERT INTO autores (nome, pais, ano_nascimento)
VALUES ('Autor de Teste', 'Brasil', 1990);

DELETE FROM autores
WHERE nome = 'Autor de Teste';
```

O autor foi cadastrado sem livros associados e, em seguida, removido. A
exclusão é permitida porque nenhuma linha da tabela `livros` referencia
o identificador desse autor. A chave estrangeira impede a remoção de um
autor que ainda esteja relacionado a livros, conforme a restrição
configurada.

### Bloco C --- Administração e privilégios avançados

#### Desafio 12 --- Usuário restrito para relatórios

Executado com uma conta administrativa:

``` sql
CREATE USER 'relatorios'@'%'
IDENTIFIED BY 'Relatorios2026!';

GRANT SELECT ON biblioteca.livros
TO 'relatorios'@'%';

FLUSH PRIVILEGES;
```

O usuário `relatorios` recebeu permissão de leitura exclusivamente na
tabela `biblioteca.livros`.

#### Desafio 13 --- Teste de restrição de visibilidade

Na conexão feita com o usuário `relatorios`, a consulta abaixo deve
funcionar:

``` sql
SELECT * FROM livros;
```

Já esta consulta deve ser recusada:

``` sql
SELECT * FROM autores;
```

O MariaDB apresenta erro de acesso negado, normalmente erro 1142, porque
o usuário não recebeu o privilégio `SELECT` sobre `biblioteca.autores`.



#### Desafio 14 --- Concessão e revogação dinâmica

Conectado como `root`, foi concedida a permissão de inserção:

``` sql
GRANT INSERT ON biblioteca.livros
TO 'relatorios'@'%';
```

Com o usuário `relatorios`, foi realizado um teste de inserção:

``` sql
INSERT INTO livros
    (titulo, ano_publicacao, preco, autor_id)
VALUES
    ('Livro de Teste', 2026, 49.90, 1);
```

Depois, conectado novamente como `root`, a permissão foi revogada:

``` sql
REVOKE INSERT ON biblioteca.livros
FROM 'relatorios'@'%';
```

Após a revogação, uma nova tentativa de `INSERT` pelo usuário
`relatorios` deve ser recusada, pois ele voltou a ter somente a
permissão de consulta na tabela `livros`.

#### Desafio 15 --- Script `setup.sql`

O arquivo `setup.sql` foi criado para automatizar a preparação do banco
`biblioteca`, suas tabelas, relacionamentos, usuários, permissões e
carga inicial. Ele foi salvo no repositório pessoal.



## 5. Consultas obrigatórias

As seis consultas abaixo foram utilizadas para verificar os dados do
banco.

**Consulta 1 --- Todos os livros**

``` sql
SELECT * FROM livros;
```

**Consulta 2 --- Títulos e anos em ordem decrescente**

``` sql
SELECT titulo, ano_publicacao
FROM livros
ORDER BY ano_publicacao DESC;
```

**Consulta 3 --- Livros publicados antes de 1900**

``` sql
SELECT *
FROM livros
WHERE ano_publicacao < 1900;
```

**Consulta 4 --- Livros com seus autores e preços**

``` sql
SELECT l.titulo, a.nome AS autor, l.preco
FROM livros l
JOIN autores a ON l.autor_id = a.id;
```

**Consulta 5 --- Média de preço dos livros por autor**

``` sql
SELECT a.nome AS autor, AVG(l.preco) AS preco_medio
FROM autores a
JOIN livros l ON a.id = l.autor_id
GROUP BY a.id, a.nome;
```

**Consulta 6 --- Livros acima da média geral de preços**

``` sql
SELECT *
FROM livros
WHERE preco > (SELECT AVG(preco) FROM livros);
```


