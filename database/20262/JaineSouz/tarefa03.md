# Tarefa 03 — Docker Compose, MariaDB e Administração de SGBD

## 1. Identificação e Repositório

- **Discente:** Jaine Souza da Luz
- **Usuário no GitHub:** JaineSouz
- **E-mail acadêmico:** jaine.luz.138@ufrn.edu.br
- **Curso:** Sistemas de Informação — CERES/UFRN
- **Disciplina:** DCT2201 — Banco de Dados
- **Issue:** [#523 — Tarefa 03 - Docker e SGBD - JaineSouz](https://github.com/tacianosilva/bsi-tasks/issues/523)
- **Repositório pessoal:** [DCT2201 — Banco de Dados](https://github.com/JaineSouz/dct2201-banco-de-dados)
- **Pull Request:** (https://github.com/tacianosilva/bsi-tasks/pull/528)

Os arquivos de infraestrutura e configuração da atividade estão organizados no repositório pessoal, principalmente nas pastas `tarefa03/` e `tarefa03-instancia2/`. O repositório contém os arquivos `docker-compose.yml`, `.env.example`, `.gitignore`, `povoamento.sql` e `setup.sql`, além do README com orientações sobre a organização do projeto.

O arquivo `.env` contém credenciais locais e está incluído no `.gitignore`, portanto não é versionado no GitHub.

---

## 2. Respostas às Perguntas Discursivas dos Passos Práticos

### Pergunta Discursiva 1 — Diferença entre DDL e DML

DDL (Data Definition Language) é a linguagem utilizada para definir e modificar a estrutura do banco de dados, como criar, alterar ou excluir tabelas. Alguns comandos são `CREATE`, `ALTER` e `DROP`.

DML (Data Manipulation Language) é utilizada para manipular os dados armazenados nas tabelas, permitindo inserir, consultar, atualizar e excluir registros. Alguns comandos são `INSERT`, `SELECT`, `UPDATE` e `DELETE`.

O comando `DROP TABLE` pertence à DDL e remove a tabela inteira, incluindo sua estrutura e seus dados. Já o comando `DELETE` remove registros, mas mantém a estrutura da tabela.

### Pergunta Discursiva 2 — Erro 1142 e princípio do menor privilégio

O erro 1142 ocorreu porque o usuário `app_biblioteca` não possuía permissão para executar o comando `DROP TABLE` sobre a tabela `autores`.

Esse comportamento está relacionado ao princípio do menor privilégio, segundo o qual cada usuário deve possuir apenas as permissões necessárias para realizar suas atividades. Assim, uma conta utilizada pela aplicação pode inserir, consultar, atualizar ou excluir registros sem ter autorização para apagar a estrutura das tabelas.

### Pergunta Discursiva 3 — Uso do host `%` em ambientes Docker

O host `%` permite que o usuário do banco de dados realize conexões a partir de diferentes endereços IP, conforme as permissões concedidas. Em uma arquitetura com Docker, a aplicação ou interface administrativa pode acessar o MariaDB por meio da rede interna do Docker, utilizando um endereço diferente de `localhost`.

Se o usuário fosse criado somente com o host `localhost`, o acesso poderia ficar restrito às conexões originadas no próprio contêiner do banco. Por isso, o uso de `%` pode ser necessário nesse ambiente, desde que acompanhado de uma senha forte e de privilégios limitados.

### Pergunta Discursiva 4 — Povoamento e integridade referencial

O povoamento expandido resultou em **14 autores e 30 livros** cadastrados na biblioteca.

A chave estrangeira `autor_id`, presente na tabela `livros`, referencia a chave primária `id` da tabela `autores`. Essa relação garante que um livro seja associado a um autor existente.

Caso seja realizada uma tentativa de inserir um livro com `autor_id = 999`, sem existir um autor com esse identificador, o banco rejeitará a operação. Isso acontece por causa da restrição de chave estrangeira, que protege a integridade referencial dos dados.

### Pergunta Discursiva 5 — Vantagem da divisão entre autores e livros

A vantagem de dividir os dados em duas tabelas relacionadas é evitar a repetição das informações dos autores em cada livro. Dessa forma, os dados do autor ficam armazenados em um único lugar e os livros fazem referência a ele por meio de uma chave estrangeira.

Isso reduz a duplicidade de informações, facilita atualizações e ajuda a manter a consistência dos dados.

---

## 3. Respostas Dissertativas Conceituais

### Questão a — Por que uma aplicação comercial não deve utilizar o usuário root?

Uma aplicação comercial não deve se conectar ao banco de dados utilizando o usuário `root`, pois essa conta possui privilégios administrativos muito amplos. Caso as credenciais sejam vazadas, uma pessoa mal-intencionada poderá acessar, modificar ou excluir tabelas e dados, além de alterar usuários e permissões.

O ideal é criar uma conta específica para a aplicação, concedendo somente os privilégios necessários para seu funcionamento. Dessa forma, mesmo que as credenciais sejam comprometidas, os possíveis danos ficam limitados.

### Questão b — Diferença entre privilégios DDL e DML

Os privilégios DDL permitem realizar alterações na estrutura do banco de dados, como criar ou excluir tabelas. Já os privilégios DML permitem manipular os registros, como consultar, inserir, atualizar e excluir dados.

Separar esses privilégios em contas diferentes é uma boa prática de segurança, pois evita que um usuário que precisa apenas manipular informações consiga alterar ou remover toda a estrutura do banco.

### Questão c — Diferença entre `.env.example` e `.env`

O arquivo `.env.example` deve ser versionado porque apresenta os nomes das variáveis necessárias para configurar o projeto, utilizando valores genéricos ou exemplos. Ele ajuda outras pessoas a entenderem quais configurações precisam ser preenchidas.

Já o arquivo `.env` contém valores reais, como senhas e outras informações privadas, por isso não deve ser enviado ao repositório. Caso credenciais reais sejam publicadas em um repositório público, outras pessoas poderão utilizá-las para acessar serviços e dados sem autorização.

### Questão d — O uso de `.env` e `.gitignore` elimina todos os riscos?

Não. O uso do `.env` e do `.gitignore` ajuda a evitar que credenciais sejam enviadas acidentalmente ao repositório, mas não elimina todos os riscos de segurança.

Isso acontece porque o arquivo `.env` continua armazenado em texto puro no sistema de arquivos. Uma pessoa que consiga acessar o servidor ou o computador poderá visualizar as credenciais. Por isso, também é importante controlar o acesso aos arquivos, utilizar permissões adequadas, proteger os servidores e trocar as senhas quando houver suspeita de exposição.

### Questão e — O que é um contêiner e quais são as vantagens do Docker?

Um contêiner é uma unidade isolada que reúne uma aplicação e os recursos necessários para sua execução. O Docker permite criar e executar esses contêineres de maneira organizada.

Nas atividades acadêmicas, o Docker facilita a instalação e a configuração de ambientes, evita a necessidade de instalar diretamente o SGBD no sistema operacional e permite que diferentes estudantes utilizem configurações semelhantes. Também facilita a criação, remoção e reprodução dos ambientes, sem interferir diretamente em outros programas instalados no computador.

---

## 4. Desafios Práticos

### Bloco A — Docker e Infraestrutura de Ambiente

#### A1 — Alteração de porta do SGBD

A variável `MARIADB_PORT` foi alterada no arquivo `.env` para `3307`. Em seguida, os serviços foram reiniciados com:

```bash
docker compose up -d
```

A verificação dos contêineres com `docker ps` confirmou o mapeamento da porta `3307` do computador para a porta `3306` interna do contêiner MariaDB.

A conexão do CloudBeaver utiliza o nome do serviço `mariadb` e a porta interna `3306`, pois os serviços estão conectados pela rede do Docker. Já o acesso ao MariaDB diretamente pelo computador utiliza a porta externa `3307`.

#### A2 — Dois ambientes simultâneos

Foi criada uma segunda pasta chamada `tarefa03-instancia2`, contendo arquivos próprios de configuração do Docker Compose e variáveis de ambiente.

A primeira instância utiliza os contêineres `lab-mariadb` e `lab-cloudbeaver`, com as portas externas `3307` e `8978`.

A segunda instância utiliza `lab-mariadb-2` e `lab-cloudbeaver-2`, com as portas externas `3308` e `8979`.

Também foram utilizados bancos de dados e volumes diferentes, evitando conflitos entre os ambientes. A execução de `docker ps` confirmou que os quatro contêineres estavam ativos simultaneamente.

#### A3 — Persistência do volume e alteração de senha de root

A senha configurada no arquivo `.env` foi alterada para uma nova senha. Após executar:

```bash
docker compose up -d
```

foi observado que a senha antiga continuava funcionando e a nova senha ainda não permitia a autenticação.

Isso ocorre porque a variável `MARIADB_ROOT_PASSWORD` é utilizada na inicialização inicial do banco. Depois que o volume é criado e os dados são armazenados, a senha fica registrada no próprio MariaDB. Alterar o arquivo `.env` não modifica automaticamente a senha já existente no banco.

Foram identificadas duas formas de aplicar a nova senha:

**Primeira forma — Alterar a senha diretamente no MariaDB, preservando os dados:**

```sql
ALTER USER 'root'@'%' IDENTIFIED BY 'NOVA_SENHA';
ALTER USER 'root'@'localhost' IDENTIFIED BY 'NOVA_SENHA';
```

Nesse caso, a senha é modificada diretamente no banco, sem excluir o volume.

**Segunda forma — Recriar o ambiente:**

```bash
docker compose down -v
docker compose up -d
```

Esse procedimento remove os contêineres e o volume de dados. Na inicialização seguinte, a senha definida no `.env` será utilizada novamente. Entretanto, os dados armazenados no volume serão perdidos.

No teste realizado, foram identificadas as contas `root@%` e `root@localhost`, e a alteração foi aplicada às duas. Depois disso, a nova senha foi testada com sucesso.

#### A4 — Comportamento da validação estrita `:?`

O arquivo `.env` foi temporariamente renomeado para simular sua ausência. Em seguida, foi executado:

```bash
docker compose up -d
```

O Docker Compose apresentou a seguinte mensagem:

```text
error while interpolating services.mariadb.environment.MARIADB_ROOT_PASSWORD: required variable MARIADB_ROOT_PASSWORD is missing a value: defina MARIADB_ROOT_PASSWORD no arquivo .env
```

Depois do teste, o arquivo foi restaurado.

O modificador `:?` realiza uma validação obrigatória da variável. Caso ela não esteja definida ou esteja vazia, o Docker Compose interrompe a execução e apresenta a mensagem configurada.

Essa validação é importante em ambientes profissionais porque impede que os serviços sejam iniciados sem uma configuração obrigatória, como a senha do usuário administrador do banco de dados.

#### A5 — Inspeção de variáveis no Compose

Foi executado o comando:

```bash
docker compose config
```

O comando apresentou a configuração final do ambiente após a interpolação das variáveis do arquivo `.env`.

Entre as variáveis verificadas estão:

| Variável | Valor resolvido |
|---|---|
| `MARIADB_DATABASE` | `labdb` |
| `MARIADB_PORT` | `3307` |
| `CLOUDBEAVER_PORT` | `8978` |

A variável `MARIADB_ROOT_PASSWORD` também foi definida no arquivo `.env`, mas seu valor não foi apresentado no relatório por se tratar de uma credencial privada.

---

### Bloco B — Modelagem e Consultas SQL Básicas

#### B6 — Criação da tabela de empréstimos

Foi criada a tabela `emprestimos`, contendo os campos solicitados e uma chave estrangeira que referencia a tabela `livros`.

```sql
CREATE TABLE emprestimos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    livro_id INT NOT NULL,
    data_emprestimo DATE NOT NULL,
    devolvido BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (livro_id) REFERENCES livros(id)
) ENGINE=InnoDB;
```

A chave estrangeira garante que cada empréstimo esteja associado a um livro existente.

#### B7 — Carga da tabela de empréstimos

Foram cadastrados três empréstimos, sendo dois não devolvidos e um devolvido.

```sql
INSERT INTO emprestimos (livro_id, data_emprestimo, devolvido)
VALUES
(1, '2026-10-20', FALSE),
(2, '2026-10-22', FALSE),
(3, '2026-10-25', TRUE);
```

Assim, a tabela passou a conter dois empréstimos pendentes e um empréstimo já devolvido.

#### B8 — Consulta de pendências

A consulta utiliza junções entre as tabelas `emprestimos`, `livros` e `autores` para apresentar o título do livro, a data do empréstimo e o nome do autor. O filtro `devolvido = FALSE` retorna somente os empréstimos pendentes.

```sql
SELECT
    l.titulo,
    e.data_emprestimo,
    a.nome AS autor
FROM emprestimos e
JOIN livros l ON e.livro_id = l.id
JOIN autores a ON l.autor_id = a.id
WHERE e.devolvido = FALSE;
```

Com os três registros cadastrados, a consulta deve retornar os dois empréstimos que ainda não foram devolvidos.

#### B9 — Filtragem de grupos com HAVING

A consulta agrupa os livros por autor e apresenta a quantidade de obras cadastradas para cada um. O `HAVING COUNT(*) > 1` filtra os grupos que possuem mais de um livro.

```sql
SELECT
    a.nome AS autor,
    COUNT(*) AS quantidade_livros
FROM autores a
JOIN livros l ON a.id = l.autor_id
GROUP BY a.id, a.nome
HAVING COUNT(*) > 1;
```

O `GROUP BY` agrupa os registros por autor, enquanto o `HAVING` filtra os resultados após o agrupamento.

#### B10 — Atualização proporcional

Foi realizado um reajuste de 10% no preço do livro de identificador `1`.

```sql
UPDATE livros
SET preco = preco * 1.10
WHERE id = 1;
```

O preço anterior era R$ 39,90 e, após o reajuste, passou para R$ 43,89.

A operação foi realizada utilizando `UPDATE`, que permite modificar os valores de registros já existentes.

#### B11 — Remoção condicional

O teste consistiu em cadastrar um autor sem livros associados e, em seguida, removê-lo da tabela `autores`.

Um exemplo de sequência SQL para realizar esse procedimento é:

```sql
INSERT INTO autores (nome, pais, ano_nascimento)
VALUES ('Autor Temporario', 'Brasil', 1990);

SET @id_autor = LAST_INSERT_ID();

DELETE FROM autores
WHERE id = @id_autor;
```

A remoção é permitida porque o autor cadastrado não possui livros relacionados na tabela `livros`. Dessa forma, nenhum registro existente fica apontando para um autor que foi excluído.

No teste realizado, o autor temporário foi removido com sucesso, e a quantidade final de autores permaneceu em 14.

---

### Bloco C — Administração e Privilégios Avançados

#### C12 — Criação de usuário restrito para relatórios

Foi criado o usuário `relatorios` com a senha definida na atividade e concedida permissão de consulta exclusivamente sobre a tabela `livros` do banco `biblioteca`.

```sql
CREATE USER 'relatorios'@'%'
IDENTIFIED BY 'Relatorios2026!';

GRANT SELECT ON biblioteca.livros
TO 'relatorios'@'%';
```

Dessa forma, o usuário consegue consultar os livros, mas não recebe automaticamente permissão para acessar as demais tabelas.

#### C13 — Teste de restrição de visibilidade

A conexão foi realizada utilizando o usuário `relatorios`. A consulta à tabela `livros` foi permitida, enquanto a tentativa de consultar a tabela `autores` foi bloqueada.

Comando utilizado:

```sql
SELECT * FROM biblioteca.autores;
```

Mensagem apresentada pelo MariaDB:

```text
SQL Error [1142] [42000]:
SELECT command denied to user 'relatorios'@'172.19.0.3'
for table 'biblioteca.autores'
```

O erro ocorreu porque o usuário possui permissão de `SELECT` somente sobre a tabela `biblioteca.livros`. A tabela `autores` está fora do escopo de permissões concedido.

Esse teste demonstra a aplicação do princípio do menor privilégio.

#### C14 — Concessão e revogação dinâmica de privilégios

Inicialmente, foi concedida ao usuário `relatorios` a permissão de inserir registros na tabela `livros`.

```sql
GRANT INSERT ON biblioteca.livros
TO 'relatorios'@'%';
```

Com a permissão concedida, foi realizada uma inserção de teste com sucesso.

Em seguida, o privilégio foi revogado:

```sql
REVOKE INSERT ON biblioteca.livros
FROM 'relatorios'@'%';
```

Após a revogação, uma nova tentativa de inserção foi bloqueada pelo MariaDB, que apresentou erro 1142 informando que o usuário não possuía permissão para executar `INSERT` na tabela.

Esse teste demonstra que os privilégios podem ser concedidos e removidos conforme a necessidade, mantendo o controle sobre as operações que cada usuário pode realizar.

#### C15 — Script de automação `setup.sql`

Foi desenvolvido o arquivo `setup.sql` no repositório pessoal, com a finalidade de recriar o banco de dados `biblioteca`, suas tabelas, restrições, dados e configurações de usuários e privilégios.

O script contém a criação das tabelas `autores`, `livros` e `emprestimos`, além da carga de dados utilizada na atividade e das configurações dos usuários.

O arquivo foi versionado no repositório pessoal:

[Consultar o repositório e os arquivos da Tarefa 03](https://github.com/JaineSouz/dct2201-banco-de-dados)

**Observação:** o script contém instruções para remover e recriar o banco de dados. Portanto, sua execução apaga os dados existentes e deve ser realizada somente quando houver intenção de reconstruir o ambiente. O arquivo foi revisado e versionado no repositório pessoal, mas sua execução não foi realizada nesta etapa.

---

## 5. Consultas Obrigatórias — SELECT

As seis consultas foram executadas individualmente no CloudBeaver para consultar e analisar os dados cadastrados no banco de dados `biblioteca`.

### Consulta 1 — Seleção completa dos livros

Recupera todos os registros e todas as colunas da tabela `livros`.

```sql
SELECT * FROM livros;
```

### Consulta 2 — Seleção de atributos e ordenação decrescente

Exibe somente o título e o ano de publicação dos livros, ordenados do mais recente para o mais antigo.

```sql
SELECT titulo, ano_publicacao
FROM livros
ORDER BY ano_publicacao DESC;
```

### Consulta 3 — Filtragem com WHERE

Retorna os livros publicados antes do ano de 1900.

```sql
SELECT *
FROM livros
WHERE ano_publicacao < 1900;
```

### Consulta 4 — Junção entre livros e autores

Utiliza `INNER JOIN` para relacionar as tabelas `livros` e `autores`, apresentando o título da obra, o nome do autor e o preço.

```sql
SELECT l.titulo, a.nome AS autor, l.preco
FROM livros l
JOIN autores a ON l.autor_id = a.id;
```

### Consulta 5 — Agrupamento e cálculo de média

Agrupa os livros por autor e calcula o preço médio das obras de cada um, utilizando `GROUP BY` e `AVG`.

```sql
SELECT a.nome AS autor, AVG(l.preco) AS preco_medio
FROM autores a
JOIN livros l ON a.id = l.autor_id
GROUP BY a.id, a.nome;
```

### Consulta 6 — Subconsulta comparativa

Utiliza uma subconsulta para calcular a média geral dos preços e apresentar somente os livros que possuem preço superior a essa média.

```sql
SELECT *
FROM livros
WHERE preco > (SELECT AVG(preco) FROM livros);
```

---

## 6. Considerações Finais

A atividade permitiu praticar a criação e configuração de ambientes com Docker Compose, a utilização de volumes para persistência de dados e a conexão entre serviços por meio da rede interna do Docker.

Também foram trabalhados comandos SQL para criação de tabelas, inserção, consulta, atualização e exclusão de dados, além da utilização de chaves estrangeiras para garantir a integridade referencial.

Por fim, os testes de usuários e privilégios demonstraram a importância de limitar o acesso de cada conta às operações necessárias, aplicando o princípio do menor privilégio.

Os arquivos de infraestrutura e scripts desenvolvidos foram organizados e versionados no repositório pessoal, enquanto o relatório foi preparado em Markdown para envio no repositório de tarefas da disciplina.
