# Tarefa 03 - Docker Compose, MariaDB e Administração de SGBD

## 1. Identificação e repositório

- **Discente:** Leonardo Breno
- **GitHub:** [leonardobreno](https://github.com/leonardobreno)
- **E-mail acadêmico:** leonardo.breno.141@ufrn.edu.br
- **Repositório pessoal:** [dct2201-banco-de-dados](https://github.com/leonardobreno/dct2201-banco-de-dados)
- **Arquivos da Tarefa 03:** [pasta tarefa03](https://github.com/leonardobreno/dct2201-banco-de-dados/tree/main/tarefa03)

Os arquivos de infraestrutura, scripts SQL e configurações estão no repositório pessoal. O arquivo `.env` contém credenciais locais e não foi versionado; `.env.example` apresenta apenas valores genéricos.

## 2. Respostas às perguntas discursivas dos passos práticos

### Pergunta Discursiva 1 — DDL e DML

DDL é a linguagem usada para definir a estrutura do banco de dados, como criar ou excluir tabelas. DML é usada para manipular os registros armazenados, por exemplo, inserir, consultar, atualizar e excluir linhas. Ao executar `DROP TABLE`, a tabela é removida e, junto com ela, todos os seus registros e sua estrutura. Portanto, não é o mesmo que apagar apenas algumas linhas com `DELETE`.

### Pergunta Discursiva 2 — Erro 1142 e menor privilégio

O usuário `app_biblioteca` recebeu permissões de consulta e manipulação de registros (`SELECT`, `INSERT`, `UPDATE` e `DELETE`), mas não recebeu permissão para executar comandos DDL como `DROP TABLE`. Por isso, ao tentar remover a tabela `autores`, o MariaDB deve recusar a operação com o erro 1142. Essa separação evita que uma aplicação comprometida ou com erro de programação consiga apagar a estrutura do banco. O usuário da aplicação fica limitado às operações necessárias para seu funcionamento.

### Pergunta Discursiva 3 — Host `%`

Os usuários foram criados com host `%` porque os serviços estão em contêineres diferentes e se comunicam pela rede interna criada pelo Docker Compose. Nesse cenário, a conexão não chega ao MariaDB como uma conexão local `localhost`. O `%` permite conexões originadas de diferentes endereços de rede. Em um ambiente de produção, esse acesso deve ser restringido ao menor conjunto de origens necessário.

### Pergunta Discursiva 4 — Povoamento expandido e chave estrangeira

Após a execução do script de povoamento e da configuração final, a consulta de contagem retornou **14 autores, 30 livros e 3 empréstimos**. Se fosse inserido um livro com `autor_id = 999`, sem existir um autor com esse identificador, a operação seria rejeitada. A chave estrangeira `livros.autor_id`, que referencia `autores.id`, impede referências a autores inexistentes e mantém a integridade referencial.

### Pergunta Discursiva 5 — Vantagem de relacionar autores e livros

Manter autores e livros em tabelas separadas evita repetir o nome e o país do autor em cada livro. Cada autor é cadastrado uma única vez e os livros apontam para ele por meio de `autor_id`. Isso reduz duplicação, economiza espaço e evita inconsistências, como registrar o mesmo autor com nomes ou países diferentes. O `JOIN` permite reunir as informações quando necessário, enquanto o agrupamento permite calcular estatísticas por autor.

## 3. Respostas dissertativas conceituais

### Questão a — Por que não usar root na aplicação?

O usuário `root` possui privilégios administrativos muito amplos. Uma aplicação comercial deve utilizar uma conta própria, com somente as permissões necessárias. Se as credenciais da aplicação forem vazadas, um invasor poderá realizar as operações autorizadas para aquela conta. Se a aplicação utilizar `root`, o invasor poderá ter controle muito maior, podendo criar ou remover bancos, tabelas, usuários e dados. O princípio do menor privilégio limita o impacto de um vazamento.

### Questão b — Diferença entre privilégios DDL e DML

Privilégios DDL permitem alterar a estrutura do banco, por exemplo, criar ou remover tabelas. Privilégios DML permitem manipular os dados, por exemplo, consultar, inserir, atualizar e excluir registros. Separar essas permissões em contas distintas reduz o risco de uma aplicação que precisa apenas manipular registros conseguir modificar ou destruir a estrutura do banco.

### Questão c — `.env.example` e `.env`

O `.env.example` deve ser versionado porque documenta quais variáveis precisam ser configuradas, usando valores genéricos e sem segredos. O `.env` contém credenciais reais e valores específicos da máquina, por isso deve permanecer fora do Git. Publicar senhas em um repositório público pode permitir acesso não autorizado ao banco e aos dados. Mesmo que o arquivo seja apagado em um commit posterior, a credencial pode continuar no histórico do Git e já ter sido copiada por terceiros; por isso, uma credencial exposta deve ser trocada.

### Questão d — O `.env` elimina todos os riscos?

Não. O `.env` e o `.gitignore` reduzem o risco de publicar credenciais acidentalmente, mas não protegem o arquivo contra acesso indevido no próprio computador ou servidor. Como ele fica armazenado em texto puro, alguém que obtenha acesso ao sistema de arquivos poderá ler as senhas. Também é necessário restringir permissões do arquivo, proteger o servidor, evitar exposição em logs e utilizar mecanismos de gerenciamento de segredos apropriados em produção.

### Questão e — Contêineres e vantagens do Docker

Um contêiner é um ambiente isolado que executa um processo e suas dependências usando recursos do sistema operacional hospedeiro. O Docker facilita criar ambientes reproduzíveis, iniciar e remover serviços rapidamente e manter versões e configurações consistentes. Em atividades de graduação, isso evita instalações manuais diferentes entre computadores, reduz conflitos com programas já instalados e permite executar mais de um ambiente isolado. Os volumes permitem manter os dados mesmo quando os contêineres são removidos.

## 4. Desafios realizados

### Bloco A — Docker e infraestrutura

#### A1 — Alteração da porta do SGBD

A variável `MARIADB_PORT` foi alterada para `3307`. O mapeamento publicado pelo Docker ficou `3307:3306`: a porta `3307` é utilizada no computador hospedeiro, enquanto o MariaDB continua escutando na porta interna `3306`.

No CloudBeaver, a conexão entre contêineres utiliza o host `mariadb` e a porta interna `3306`. A porta `3307` é utilizada quando a conexão é feita a partir de um programa executado diretamente no computador hospedeiro.

Comando de verificação:

```powershell
docker ps
```

#### A2 — Dois ambientes simultâneos

Foram configurados dois arquivos Compose com nomes de contêineres, portas e volumes diferentes. O primeiro ambiente utiliza `lab-mariadb` e `lab-cloudbeaver`, com as portas publicadas `3307` e `8978`. O segundo utiliza `lab-mariadb-2` e `lab-cloudbeaver-2`, com as portas `3308` e `8979`.

Os volumes também são independentes (`mariadb_data` e `mariadb_data_2`), evitando que os bancos compartilhem os mesmos arquivos de dados.

Comando utilizado para conferir os contêineres:

```powershell
docker ps
```

Foram identificados quatro contêineres em execução.

#### A3 — Persistência do volume e alteração da senha de root

A alteração de `MARIADB_ROOT_PASSWORD` no `.env` não alterou automaticamente a senha já cadastrada. Isso acontece porque a variável é utilizada pelo processo de inicialização do MariaDB quando o diretório de dados do volume é inicializado pela primeira vez. Com o volume já existente, o banco mantém as credenciais armazenadas.

Existem dois caminhos para aplicar uma nova senha:

1. Alterar a senha diretamente no MariaDB com `ALTER USER`, preservando o volume e os dados.
2. Remover e recriar o volume com `docker compose down -v` e depois iniciar novamente com `docker compose up -d`. Esse caminho apaga os dados persistidos e deve ser usado somente quando isso for desejado.

#### A4 — Validação estrita `:?`

Ao retirar a variável obrigatória `MARIADB_ROOT_PASSWORD` do `.env`, o Docker Compose interrompe a configuração e informa que a variável é obrigatória, exibindo a mensagem definida no próprio arquivo Compose: `defina MARIADB_ROOT_PASSWORD no arquivo .env`.

O modificador `${VAR:?mensagem}` impede que o serviço seja iniciado sem uma variável obrigatória. Isso evita subir um banco sem a configuração de senha exigida e torna o erro explícito antes da criação dos contêineres.

#### A5 — Inspeção de variáveis no Compose

O comando utilizado foi:

```powershell
docker compose config
```

Entre as variáveis resolvidas pelo Compose estão:

- `MARIADB_ROOT_PASSWORD`: senha utilizada na configuração inicial do MariaDB.
- `MARIADB_DATABASE`: nome do banco inicial, configurado como `labdb`.
- `MARIADB_PORT`: porta publicada no computador hospedeiro, configurada como `3307`.

O valor real da senha não é reproduzido neste relatório.

### Bloco B — Modelagem e consultas SQL básicas

#### B6 — Criação da tabela de empréstimos

```sql
CREATE TABLE emprestimos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    livro_id INT,
    data_emprestimo DATE,
    devolvido BOOLEAN,
    FOREIGN KEY (livro_id) REFERENCES livros(id)
);
```

A chave estrangeira garante que cada empréstimo esteja associado a um livro existente.

#### B7 — Carga da tabela de empréstimos

```sql
INSERT INTO emprestimos (livro_id, data_emprestimo, devolvido)
VALUES
    (1, '2026-10-20', FALSE),
    (2, '2026-10-21', FALSE),
    (3, '2026-10-22', TRUE);
```

Foram cadastrados três empréstimos: dois pendentes e um devolvido.

#### B8 — Consulta de empréstimos pendentes

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

A consulta retornou os empréstimos pendentes dos livros **Dom Casmurro** e **Memórias Póstumas de Brás Cubas**, ambos de Machado de Assis.

#### B9 — Agrupamento com HAVING

```sql
SELECT
    a.nome AS autor,
    COUNT(*) AS total_livros
FROM autores a
JOIN livros l ON a.id = l.autor_id
GROUP BY a.id, a.nome
HAVING COUNT(*) > 1;
```

A consulta retornou 11 autores com mais de um livro cadastrado.

#### B10 — Atualização proporcional

```sql
UPDATE livros
SET preco = preco * 1.10
WHERE id = 1;
```

O comando aplicou um acréscimo de 10% ao preço do livro de ID 1, `Dom Casmurro`. O preço passou de R$ 39,90 para R$ 43,89. Posteriormente, a execução do `setup.sql` recriou o banco e restaurou os dados iniciais; portanto, o valor final após a automação voltou ao preço definido no script.

#### B11 — Remoção condicional

```sql
INSERT INTO autores (nome, pais, ano_nascimento)
VALUES ('Autor de Teste', 'Brasil', 2000);

DELETE FROM autores
WHERE nome = 'Autor de Teste';
```

O autor foi inserido sem livros associados e depois removido com sucesso. A exclusão foi aceita porque nenhum registro da tabela `livros` referenciava o autor pela chave estrangeira `autor_id`.

### Bloco C — Administração e privilégios avançados

#### C12 — Criação do usuário restrito

```sql
CREATE USER 'relatorios'@'%'
IDENTIFIED BY 'Relatorios2026!';

GRANT SELECT ON biblioteca.livros
TO 'relatorios'@'%';

FLUSH PRIVILEGES;
```

O usuário recebeu permissão de leitura somente na tabela `biblioteca.livros`.

#### C13 — Teste de restrição de visibilidade

Conectado como `relatorios`, o comando abaixo foi executado com sucesso:

```sql
SELECT * FROM livros;
```

A tentativa de consultar autores:

```sql
SELECT * FROM autores;
```

foi recusada com a mensagem:

```text
ERROR 1142 (42000): SELECT command denied to user 'relatorios'@'localhost' for table `biblioteca`.`autores`
```

O bloqueio ocorreu porque o usuário recebeu `SELECT` somente sobre `biblioteca.livros`, não sobre `biblioteca.autores`.

#### C14 — Concessão e revogação dinâmica

Como root, foi concedida a permissão de inserção:

```sql
GRANT INSERT ON biblioteca.livros
TO 'relatorios'@'%';

FLUSH PRIVILEGES;
```

Com o usuário `relatorios`, foi realizado um teste de inserção:

```sql
INSERT INTO livros (titulo, ano_publicacao, preco, autor_id)
VALUES ('Livro de Teste C14', 2026, 25.00, 1);
```

A inserção foi aceita. Em seguida, como root, a permissão foi revogada:

```sql
REVOKE INSERT ON biblioteca.livros
FROM 'relatorios'@'%';

FLUSH PRIVILEGES;
```

Uma nova tentativa de inserção foi recusada com erro 1142, informando que o usuário não possuía o privilégio `INSERT`. A permissão de leitura permaneceu disponível.

#### C15 — Script de automação `setup.sql`

O arquivo `setup.sql` foi criado e versionado no repositório pessoal. Ele recria o banco `biblioteca`, as tabelas `autores`, `livros` e `emprestimos`, as chaves e restrições, os usuários `app_biblioteca` e `consulta`, seus privilégios e a carga de dados.

Execução no ambiente Docker:

```powershell
docker cp .\setup.sql lab-mariadb:/tmp/setup.sql
docker exec -it lab-mariadb mariadb -uroot -p -e "source /tmp/setup.sql"
```

Ao final da execução, as consultas de contagem retornaram:

```text
total_autores: 14
total_livros: 30
total_emprestimos: 3
```

A verificação dos privilégios confirmou que `app_biblioteca` possui `SELECT`, `INSERT`, `UPDATE` e `DELETE` em `biblioteca.*`, enquanto `consulta` possui somente `SELECT` em `biblioteca.*`.

## 5. Arquivos do repositório pessoal

Os arquivos da infraestrutura e dos scripts estão na pasta [`tarefa03/`](https://github.com/leonardobreno/dct2201-banco-de-dados/tree/main/tarefa03) do repositório pessoal:

- `.env.example`: modelo das variáveis de ambiente, sem credenciais reais.
- `.gitignore`: impede o versionamento dos arquivos `.env`.
- `docker-compose.yml`: configuração dos serviços MariaDB e CloudBeaver.
- `povoamento.sql`: inserções para ampliar os dados de autores e livros.
- `setup.sql`: criação e povoamento automatizado do banco.
- `tarefa03-ambiente2/`: configuração do segundo ambiente Docker Compose.

**Observação:** o arquivo `.env` local não foi enviado ao GitHub, pois contém credenciais.

## 6. Entrega

- **Repositório pessoal:** https://github.com/leonardobreno/dct2201-banco-de-dados
- **Pull Request do bsi-tasks:** inserir aqui o link do PR após sua criação.
- **Issue da Tarefa 03:** inserir aqui o número/link da issue criada no repositório original.
