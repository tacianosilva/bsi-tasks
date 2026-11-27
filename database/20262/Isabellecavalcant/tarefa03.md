# Tarefa 03 — Docker Compose, MariaDB e Administração de SGBD

## 1. Identificação e Repositório

- **Discente:** Isabelle Cavalcanti da Silva
- **Curso:** Sistemas de Informação — CERES/UFRN
- **Disciplina:** DCT2201 — Banco de Dados
- **Usuário no GitHub:** Isabellecavalcant
- **E-mail acadêmico:** isabelle.silva.712@ufrn.edu.br
- **Issue:** [#548 — Tarefa 03 - Docker e SGBD - Isabellecavalcant](https://github.com/tacianosilva/bsi-tasks/issues/548)
- **Repositório pessoal:** [dct2201-banco-de-dados](https://github.com/Isabellecavalcant/dct2201-banco-de-dados)

Os arquivos de infraestrutura e configuração foram organizados na raiz do repositório pessoal. Entre eles estão `.env.example`, `.gitignore`, `docker-compose.yml`, `povoamento.sql`, `setup.sql` e `README.md`.

O arquivo `.env` foi mantido localmente e incluído no `.gitignore`, evitando o compartilhamento de credenciais reais.

## 2. Respostas às Perguntas Discursivas

### Pergunta Discursiva 1 — Diferença entre DDL e DML

A DDL (Data Definition Language) é utilizada para definir e modificar a estrutura de um banco de dados, permitindo criar, alterar e excluir bancos, tabelas e outros objetos. São exemplos os comandos `CREATE TABLE`, `ALTER TABLE` e `DROP TABLE`.

Já a DML (Data Manipulation Language) é utilizada para manipular os registros armazenados nas tabelas. Entre seus principais comandos estão `INSERT`, `SELECT`, `UPDATE` e `DELETE`.

A principal diferença é que a DDL trabalha com a estrutura do banco, enquanto a DML trabalha com os dados armazenados nessa estrutura.

Quando uma tabela é excluída utilizando `DROP TABLE`, sua estrutura e todos os registros armazenados nela são removidos. Portanto, trata-se de uma operação que pode causar perda de dados.

### Pergunta Discursiva 2 — Princípio do menor privilégio e erro 1142

O usuário `app_biblioteca` foi criado com permissões de consulta, inserção, atualização e exclusão de registros, mas sem privilégios para modificar a estrutura das tabelas.

Assim, uma tentativa de executar `DROP TABLE autores` utilizando essa conta deve ser recusada pelo MariaDB, pois o usuário não possui a permissão DDL necessária para excluir tabelas. O erro 1142 indica justamente que o comando solicitado foi negado por falta de privilégio.

Essa restrição aplica o princípio do menor privilégio, segundo o qual cada usuário deve possuir somente as permissões necessárias para realizar suas atividades.

Em uma aplicação web, essa separação é importante porque, caso a aplicação seja invadida ou apresente uma falha de programação, o invasor ficará limitado às permissões da conta comprometida. Dessa forma, uma conta destinada à manipulação de registros não poderá excluir tabelas ou alterar livremente a estrutura do banco.

### Pergunta Discursiva 3 — Utilização do host '%'

Os usuários foram criados utilizando o host `%` porque os serviços do projeto estão distribuídos em contêineres diferentes.

O CloudBeaver e o MariaDB se comunicam por meio da rede virtual interna criada pelo Docker Compose. Dessa maneira, a conexão do CloudBeaver com o banco não se origina necessariamente de `localhost`, mas de outro endereço dentro da rede Docker.

O caractere `%` funciona como um curinga, permitindo conexões originadas de diferentes endereços de rede. Isso possibilita que os serviços conteinerizados utilizem as contas criadas sem depender de um endereço local específico.

### Pergunta Discursiva 4 — Povoamento expandido e integridade referencial

Após a carga inicial e o povoamento expandido, o banco de dados `biblioteca` ficou com 14 autores e 30 livros cadastrados.

A tabela `livros` possui a coluna `autor_id`, que estabelece uma relação com a chave primária `id` da tabela `autores`.

Caso fosse realizada uma tentativa de inserir um livro com `autor_id = 999`, sem que existisse um autor com esse identificador, o MariaDB recusaria a operação.

Isso acontece devido à restrição de chave estrangeira (`FOREIGN KEY`), responsável por garantir a integridade referencial entre as tabelas. Essa regra impede que um livro seja associado a um autor inexistente.

### Pergunta Discursiva 5 — Vantagens da separação entre autores e livros

Separar as informações de autores e livros em tabelas relacionadas evita a repetição desnecessária de dados.

Se o nome e o país do autor fossem armazenados em cada registro da tabela de livros, essas informações precisariam ser repetidas sempre que um autor tivesse mais de uma obra cadastrada.

Com a separação, os dados do autor são armazenados uma única vez na tabela `autores`, enquanto a tabela `livros` mantém apenas a referência ao autor por meio da chave estrangeira `autor_id`.

Essa organização reduz a redundância, facilita atualizações, evita inconsistências e melhora a manutenção do banco de dados. Além disso, permite recuperar informações relacionadas por meio de consultas com `JOIN`.

## 3. Respostas às Questões Conceituais

### Questão A — Por que uma aplicação comercial não deve utilizar root?

Uma aplicação comercial não deve utilizar o usuário `root` porque essa conta possui privilégios administrativos muito amplos, permitindo executar operações que modificam ou removem estruturas e dados do banco de dados.

Caso as credenciais de `root` sejam vazadas, um invasor poderá obter controle administrativo sobre o SGBD, podendo excluir tabelas, modificar registros, criar usuários, alterar permissões e até comprometer completamente a base de dados.

Por isso, é recomendável criar uma conta específica para a aplicação, concedendo somente os privilégios necessários ao seu funcionamento. Dessa forma, mesmo que as credenciais sejam comprometidas, os possíveis danos ficam limitados às permissões concedidas.

### Questão B — Diferença entre privilégios DDL e DML

Os privilégios DDL estão relacionados às operações que modificam a estrutura do banco de dados, como criar, alterar ou excluir tabelas.

Os privilégios DML estão relacionados às operações realizadas sobre os registros, como inserir, consultar, atualizar e excluir dados.

Separar essas permissões em contas distintas é uma boa prática de segurança porque evita que usuários ou aplicações que precisam apenas manipular registros também tenham autorização para modificar estruturas importantes do banco.

Essa separação reduz riscos de alterações indevidas e facilita o controle de acesso.

### Questão C — Diferença entre .env.example e .env

O arquivo `.env.example` deve ser versionado porque funciona como um modelo de configuração, apresentando as variáveis necessárias para executar o projeto sem expor credenciais reais.

Já o arquivo `.env` contém os valores efetivamente utilizados no ambiente local, incluindo senhas e outras informações sensíveis. Por isso, ele deve ser incluído no `.gitignore` e permanecer fora do controle de versão.

Caso credenciais reais sejam publicadas em um repositório público no GitHub, outras pessoas poderão acessá-las e utilizá-las indevidamente. Isso pode resultar em acessos não autorizados, vazamento de informações, alteração ou exclusão de dados e comprometimento dos serviços associados.

### Questão D — O uso de .env e .gitignore elimina todos os riscos?

Não. O uso do `.env` e sua inclusão no `.gitignore` ajudam a evitar que credenciais sejam enviadas acidentalmente ao repositório, mas não eliminam todos os riscos de segurança.

O arquivo `.env` permanece armazenado em texto puro no sistema de arquivos da máquina ou do servidor. Portanto, uma pessoa que consiga acesso ao ambiente poderá visualizar as credenciais.

Além disso, uma configuração incorreta do Git ou o compartilhamento indevido do arquivo pode expor informações sensíveis.

Em ambientes profissionais, é recomendável utilizar mecanismos específicos de gerenciamento de segredos, limitar as permissões de acesso aos arquivos, utilizar credenciais diferentes para cada ambiente e realizar a rotação periódica das senhas.

### Questão E — O que é um contêiner e quais são suas vantagens?

Um contêiner é uma unidade isolada de execução que reúne uma aplicação e os componentes necessários para seu funcionamento, utilizando os recursos do sistema operacional hospedeiro.

O Docker permite criar, executar e administrar esses contêineres de maneira padronizada.

Em atividades didáticas, sua utilização apresenta diversas vantagens em comparação com a instalação manual de um SGBD diretamente no sistema operacional.

Entre elas estão a facilidade de instalação e configuração, o isolamento dos ambientes, a possibilidade de executar diferentes versões de um SGBD, a reprodução de configurações entre computadores e a facilidade de remover ou recriar serviços sem interferir diretamente nas instalações locais.

Além disso, o Docker Compose permite administrar vários serviços simultaneamente, como o MariaDB e o CloudBeaver, por meio de um único arquivo de configuração.

## 4. Desafios Realizados

### Bloco A — Docker e Infraestrutura de Ambiente

#### A1 — Alteração de porta do SGBD

Inicialmente, a porta 3306 já estava ocupada por uma instalação local do MySQL. Para evitar conflito, a variável `MARIADB_PORT` foi alterada para `3307` no arquivo `.env`.

A configuração do Docker Compose manteve a porta interna do MariaDB em 3306, modificando apenas a porta publicada no computador hospedeiro.

Trecho utilizado:

```yaml
ports:
  - "${MARIADB_PORT:-3306}:3306"
```

O acesso ao MariaDB pelo terminal passou a utilizar o mapeamento da porta 3307 do host para a porta 3306 do contêiner.

Na conexão do CloudBeaver, foi utilizado o nome do serviço `mariadb` como host e a porta interna `3306`, pois os serviços compartilham a rede Docker.

#### A2 — Dois ambientes simultâneos

Foi criado um segundo ambiente em diretório separado, utilizando outra configuração do Docker Compose.

Foram definidos nomes e portas diferentes para evitar conflitos:

| Serviço | Primeiro ambiente | Segundo ambiente |
|---|---|---|
| MariaDB | lab-mariadb | lab-mariadb-2 |
| CloudBeaver | lab-cloudbeaver | lab-cloudbeaver-2 |
| Porta MariaDB no host | 3307 | 3308 |
| Porta CloudBeaver no host | 8978 | 8979 |
| Volume | mariadb_data | mariadb_data_2 |

Dessa forma, os quatro contêineres puderam funcionar simultaneamente, utilizando portas, nomes e volumes independentes.

#### A3 — Persistência do volume e alteração da senha root

Foi alterado o valor da variável `MARIADB_ROOT_PASSWORD` no arquivo `.env` e o ambiente foi reiniciado.

Foi observado que a alteração do arquivo não modificou automaticamente a senha da conta `root` já existente.

Isso acontece porque a variável `MARIADB_ROOT_PASSWORD` é utilizada durante a inicialização inicial do banco, quando o volume ainda não possui dados. Depois que o volume é inicializado, as credenciais ficam armazenadas no próprio MariaDB.

Existem duas maneiras principais de alterar a senha:

1. Executar um comando administrativo, como `ALTER USER`, para modificar a senha diretamente no SGBD.
2. Remover o volume persistente e inicializar o banco novamente, fazendo com que as variáveis do `.env` sejam aplicadas durante a criação da nova base.

Também foi observada a diferença entre as contas `root@localhost` e `root@%`, que podem possuir senhas diferentes.

#### A4 — Comportamento da validação estrita (:?)

O arquivo `.env` foi temporariamente renomeado para `.env.teste`, e em seguida foi executado:

```bash
docker compose config
```

Como a variável obrigatória `MARIADB_ROOT_PASSWORD` não estava disponível, o Docker Compose interrompeu a validação e apresentou uma mensagem informando que a variável precisava ser definida.

Após o teste, o arquivo `.env` foi restaurado.

O modificador `${VAR:?mensagem}` é importante porque impede que os serviços sejam iniciados quando uma variável obrigatória não está configurada. Em ambientes profissionais, isso evita inicializações incompletas ou inseguras.

#### A5 — Inspeção de variáveis no compose

Foi executado:

```bash
docker compose config --format json
```

O comando permitiu verificar os valores resolvidos a partir do arquivo `.env`.

As três variáveis verificadas foram:

| Variável | Valor resolvido |
|---|---|
| MARIADB_DATABASE | labdb |
| MARIADB_PORT | 3307 |
| CLOUDBEAVER_PORT | 8978 |

A verificação confirmou que o Docker Compose estava interpretando corretamente as configurações do ambiente.

### Bloco B — Modelagem e Consultas SQL Básicas

#### B6 — Criação da tabela de empréstimos

Foi criada a tabela `emprestimos` no banco `biblioteca`, utilizando uma chave primária e uma chave estrangeira que referencia a tabela `livros`.

```sql
CREATE TABLE biblioteca.emprestimos (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    livro_id INT(11) NOT NULL,
    data_emprestimo DATE NOT NULL,
    devolvido BOOLEAN DEFAULT FALSE,
    CONSTRAINT fk_emprestimos_livros
        FOREIGN KEY (livro_id)
        REFERENCES biblioteca.livros(id)
) ENGINE=InnoDB;
```

A chave estrangeira garante que cada empréstimo esteja associado a um livro existente.

#### B7 — Carga da tabela empréstimos

Foram inseridos três registros, sendo dois empréstimos pendentes e um já devolvido.

```sql
INSERT INTO biblioteca.emprestimos
    (livro_id, data_emprestimo, devolvido)
VALUES
    (6, '2026-11-03', FALSE),
    (7, '2026-11-01', FALSE),
    (8, '2026-10-28', TRUE);
```

Os valores `FALSE` representam empréstimos ainda não devolvidos, enquanto `TRUE` indica que o livro foi devolvido.

#### B8 — Consulta de pendências

Foi elaborada uma consulta utilizando `JOIN` para relacionar as tabelas `emprestimos`, `livros` e `autores`.

```sql
SELECT
    e.id AS emprestimo,
    l.titulo,
    e.data_emprestimo,
    a.nome AS autor
FROM biblioteca.emprestimos e
JOIN biblioteca.livros l
    ON e.livro_id = l.id
JOIN biblioteca.autores a
    ON l.autor_id = a.id
WHERE e.devolvido = FALSE;
```

A consulta retornou os dois empréstimos pendentes, apresentando o título do livro, a data do empréstimo e o nome do autor.

#### B9 — Filtragem de grupos com HAVING

Foi utilizada uma consulta com `GROUP BY`, `COUNT` e `HAVING` para identificar autores com mais de um livro cadastrado.

```sql
SELECT
    a.nome AS autor,
    COUNT(*) AS total_livros
FROM biblioteca.autores a
JOIN biblioteca.livros l
    ON a.id = l.autor_id
GROUP BY a.id, a.nome
HAVING COUNT(*) > 1;
```

A cláusula `GROUP BY` agrupou os livros por autor, enquanto `HAVING` filtrou os grupos que possuíam mais de uma obra.

#### B10 — Atualização proporcional

Foi aplicado um reajuste de 10% nos preços dos livros.

```sql
UPDATE biblioteca.livros
SET preco = ROUND(preco * 1.10, 2);
```

A operação multiplicou os preços por 1,10, acrescentando 10% ao valor anterior. O comando `ROUND` manteve os valores com duas casas decimais.

Foram realizadas consultas antes e depois da atualização para comparar os preços.

#### B11 — Remoção condicional

Foi cadastrado um autor de teste sem livros associados.

```sql
INSERT INTO biblioteca.autores
    (nome, pais, ano_nascimento)
VALUES
    ('Autor de Teste B11', 'Brasil', 1990);
```

Em seguida, o registro foi removido:

```sql
DELETE FROM biblioteca.autores
WHERE nome = 'Autor de Teste B11';
```

A remoção foi aceita porque o autor não possuía livros associados na tabela `livros`.

A restrição de chave estrangeira impede a exclusão de um autor que ainda esteja sendo referenciado por registros de livros, mas não impede a exclusão de um autor sem dependências.

### Bloco C — Administração e Privilégios Avançados

#### C12 — Criação de usuário restrito para relatórios

Foi criado o usuário `relatorios` com permissão exclusiva de leitura sobre a tabela `livros`.

```sql
CREATE USER 'relatorios'@'%'
IDENTIFIED BY 'RelatoriosLab2026!';

GRANT SELECT
ON biblioteca.livros
TO 'relatorios'@'%';
```

A conta recebeu somente o privilégio `SELECT` sobre a tabela especificada.

#### C13 — Teste de restrição de visibilidade

Foi testado o acesso do usuário `relatorios` à tabela `livros`, que foi permitido.

Em seguida, foi tentada uma consulta à tabela `autores`:

```sql
SELECT * FROM biblioteca.autores;
```

O MariaDB recusou a operação por falta de privilégio de leitura sobre essa tabela, apresentando erro de acesso negado (erro 1142).

Isso confirmou que as permissões concedidas estavam limitadas à tabela `biblioteca.livros`.

#### C14 — Concessão e revogação dinâmica de privilégios

Inicialmente, foi concedido temporariamente o privilégio `INSERT` ao usuário `relatorios` para permitir uma inserção de teste.

Como o MariaDB diferencia contas pelo par usuário/host, foi necessário criar e utilizar também a conta `relatorios@localhost` para o teste realizado pela conexão local do terminal.

```sql
CREATE USER 'relatorios'@'localhost'
IDENTIFIED BY 'RelatoriosLab2026!';

GRANT INSERT
ON biblioteca.livros
TO 'relatorios'@'localhost';
```

Após a concessão, a inserção de teste foi executada com sucesso.

Em seguida, o privilégio foi revogado:

```sql
REVOKE INSERT
ON biblioteca.livros
FROM 'relatorios'@'localhost';
```

Depois da revogação, uma nova tentativa de inserção foi recusada pelo MariaDB, que informou que o usuário não possuía autorização para executar a operação.

Esse procedimento demonstrou que os privilégios podem ser concedidos e removidos dinamicamente, permitindo controlar o acesso conforme a necessidade.

#### C15 — Script idempotente de automação (setup.sql)

Foi desenvolvido o arquivo `setup.sql` para automatizar a preparação do banco de dados `biblioteca`.

O script realiza:

- Exclusão e recriação do banco `biblioteca`;
- Criação das tabelas `autores` e `livros`;
- Definição da chave primária e da chave estrangeira;
- Criação dos usuários `app_biblioteca` e `consulta`;
- Concessão dos respectivos privilégios;
- Inclusão dos registros de povoamento.

O arquivo foi complementado com os comandos de inserção presentes em `povoamento.sql`.

Para executá-lo no contêiner, foi utilizado:

```bash
docker exec -e MYSQL_PWD='RootLab2026!aB' -i lab-mariadb mariadb -uroot < setup.sql
```

A variável `MYSQL_PWD` permitiu fornecer a senha ao cliente MariaDB sem solicitar entrada interativa, uma vez que a entrada padrão estava sendo utilizada pelo redirecionamento do arquivo SQL.

Após a primeira execução, foram verificadas as tabelas e a quantidade de registros:

```bash
docker exec -e MYSQL_PWD='RootLab2026!aB' lab-mariadb mariadb -uroot -e "SHOW TABLES FROM biblioteca; SELECT COUNT(*) AS total_autores FROM biblioteca.autores; SELECT COUNT(*) AS total_livros FROM biblioteca.livros;"
```

O resultado confirmou:

| Verificação | Resultado |
|---|---:|
| Tabelas | autores e livros |
| Total de autores | 14 |
| Total de livros | 30 |

O script foi executado novamente, sem apresentar erros. Após a segunda execução, uma nova consulta confirmou que os registros continuavam consistentes, com 14 autores e 30 livros.

Assim, foi demonstrado que o script pode ser executado repetidamente para reconstruir o estado inicial do banco.

**Observação:** o script utiliza `DROP DATABASE IF EXISTS`, portanto, sua execução apaga e recria o banco `biblioteca`. Consequentemente, os dados e as alterações anteriores nessa base são perdidos. A repetibilidade do script não significa preservação dos dados anteriores, mas a capacidade de reconstruir o ambiente inicial de maneira consistente.

## 5. Consultas Obrigatórias

As seis consultas solicitadas foram executadas no banco `biblioteca`.

### Consulta 1 — Seleção completa de livros

```sql
SELECT * FROM livros;
```

Retorna todos os registros e colunas da tabela `livros`.

### Consulta 2 — Projeção e ordenação descendente

```sql
SELECT titulo, ano_publicacao
FROM livros
ORDER BY ano_publicacao DESC;
```

Retorna os títulos e anos de publicação, ordenados do mais recente para o mais antigo.

### Consulta 3 — Filtragem de livros anteriores a 1900

```sql
SELECT *
FROM livros
WHERE ano_publicacao < 1900;
```

Retorna somente os livros publicados antes de 1900.

### Consulta 4 — Junção entre livros e autores

```sql
SELECT
    l.titulo,
    a.nome AS autor,
    l.preco
FROM livros l
JOIN autores a
    ON l.autor_id = a.id;
```

Relaciona os livros aos seus respectivos autores, utilizando a chave estrangeira.

### Consulta 5 — Média de preço por autor

```sql
SELECT
    a.nome AS autor,
    AVG(l.preco) AS preco_medio
FROM autores a
JOIN livros l
    ON a.id = l.autor_id
GROUP BY a.id, a.nome;
```

Agrupa os livros por autor e calcula o preço médio das obras de cada um.

### Consulta 6 — Livros acima da média geral

```sql
SELECT *
FROM livros
WHERE preco > (
    SELECT AVG(preco)
    FROM livros
);
```

Utiliza uma subconsulta para calcular a média geral dos preços e retornar somente os livros com preço superior a esse valor.

## 6. Repositório e Arquivos Entregues

Os arquivos de infraestrutura e configuração foram disponibilizados no repositório pessoal público:

[Repositório dct2201-banco-de-dados](https://github.com/Isabellecavalcant/dct2201-banco-de-dados)

O repositório contém os seguintes arquivos:

| Arquivo | Finalidade |
|---|---|
| `.env.example` | Modelo das variáveis de ambiente necessárias para executar o projeto |
| `.gitignore` | Impede o versionamento do arquivo `.env` |
| `docker-compose.yml` | Define os serviços MariaDB e CloudBeaver |
| `povoamento.sql` | Contém os comandos de povoamento do banco de dados |
| `setup.sql` | Automatiza a criação do banco, das tabelas, dos usuários, das permissões e dos dados |
| `README.md` | Documenta a configuração e a execução do ambiente |

O arquivo `.env` foi mantido localmente e não foi enviado ao repositório, preservando as credenciais utilizadas no ambiente de desenvolvimento.

## 7. Considerações Finais

A realização da Tarefa 03 permitiu aplicar conceitos de conteinerização, administração de bancos de dados relacionais, linguagem SQL, controle de acesso e versionamento de código.

A utilização do Docker Compose facilitou a criação e administração dos serviços MariaDB e CloudBeaver, enquanto os volumes nomeados permitiram compreender a persistência dos dados independentemente do ciclo de vida dos contêineres.

As atividades com SQL possibilitaram praticar a criação de estruturas, manipulação de registros, consultas relacionais, agregações e subconsultas. Os desafios de administração também demonstraram a importância do controle de privilégios e do princípio do menor privilégio.

Por fim, a organização dos arquivos em um repositório pessoal e a preparação do relatório no `bsi-tasks` permitiram aplicar o fluxo de versionamento e colaboração utilizado no desenvolvimento de software.
