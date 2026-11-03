# Tarefa 03 - Docker Compose, MariaDB e Administração de SGBD

## 1. Identificação e Repositório

- **Discente:** Franciedson Lucas Linhares da Silva
- **Usuário no GitHub:** [@FranciedsonLLS](https://github.com/FranciedsonLLS)
- **E-mail acadêmico:** franciedsonlucas@gmail.com
- **Issue:** #545
- **Repositório pessoal público:** <https://github.com/FranciedsonLLS/dct2201-banco-de-dados>
  - Arquivos da Tarefa 03: [`tarefa03/`](https://github.com/FranciedsonLLS/dct2201-banco-de-dados/tree/main/tarefa03) (`docker-compose.yml`, `.env.example`, `.gitignore`, `povoamento.sql`, `setup.sql`, scripts de cada etapa em `sql/` e o segundo ambiente do Desafio 2 em `ambiente2/`). O `README.md` do repositório descreve a finalidade de cada arquivo.

**Ambiente utilizado:** Windows (x64) com Docker Desktop (backend WSL 2), Git 2.56.0, Docker 29.9.2 e Docker Compose v5.6.1.

> Nas evidências abaixo, a senha real do usuário `root` aparece substituída por `********` ou pela variável `$MARIADB_ROOT_PASSWORD`, pois ela fica apenas no arquivo `.env` local, que não é versionado. Os hashes de senha retornados pelo `SHOW GRANTS` também foram abreviados como `'*...'`.

### Verificações iniciais (passos 3.5 e 5)

```text
PS> git check-ignore -v .env
tarefa03/.gitignore:1:.env      .env

PS> docker compose up -d
PS> docker ps
CONTAINER ID   IMAGE                        STATUS         PORTS                       NAMES
6e105e27bb07   dbeaver/cloudbeaver:latest   Up 3 minutes   0.0.0.0:8978->8978/tcp      lab-cloudbeaver
828e35849b64   mariadb:11                   Up 3 minutes   0.0.0.0:3306->3306/tcp      lab-mariadb
```

O `git check-ignore` confirma que a linha 1 do `.gitignore` impede o versionamento do `.env`. A conexão no CloudBeaver foi criada com host `mariadb`, porta `3306` e usuário `root` (driver MariaDB Connector/J).

---

## 2. Respostas às Perguntas Discursivas

### Pergunta Discursiva 1 - DDL x DML e o efeito do `DROP TABLE`

Criar uma tabela (DDL) é definir a **estrutura**: o nome da tabela, as colunas, os tipos de dado e as regras (chave primária, `NOT NULL`, chave estrangeira). Nesse momento a tabela existe, mas está vazia. Inserir registros (DML) é trabalhar com o **conteúdo**: o `INSERT` coloca linhas dentro de uma estrutura que já existe, e o `SELECT`, `UPDATE` e `DELETE` consultam e alteram essas linhas sem mudar a estrutura. Em resumo, o DDL monta a "gaveta" e o DML guarda e mexe nos "papéis" dentro dela.

Ao executar `DROP TABLE`, a tabela inteira é removida do banco: a estrutura **e todos os dados** que estavam nela são apagados juntos. Não existe "lixeira". Os dados só voltam se houver backup ou um script de recriação e carga, como o `setup.sql` deste trabalho.

### Pergunta Discursiva 2 - Erro 1142 no `DROP TABLE` com `app_biblioteca`

Conectado no CloudBeaver como `app_biblioteca` (host `mariadb`, banco `biblioteca`), executei `DROP TABLE autores;` e o MariaDB recusou o comando:

```text
SQL Error [1142] [42000]: (conn=6) DROP command denied to user 'app_biblioteca'@'172.18.0.3' for table `biblioteca`.`autores`
```

O erro aconteceu porque o `app_biblioteca` só recebeu privilégios de **DML** (`SELECT, INSERT, UPDATE, DELETE`), como mostra o `SHOW GRANTS`:

```text
GRANT USAGE ON *.* TO `app_biblioteca`@`%` IDENTIFIED BY PASSWORD '*...'
GRANT SELECT, INSERT, UPDATE, DELETE ON `biblioteca`.* TO `app_biblioteca`@`%`

GRANT USAGE ON *.* TO `consulta`@`%` IDENTIFIED BY PASSWORD '*...'
GRANT SELECT ON `biblioteca`.* TO `consulta`@`%`
```

O `DROP` é um comando **DDL**, e esse privilégio nunca foi concedido. O SGBD confere as permissões antes de executar e bloqueia a operação, sem apagar nada. (O `USAGE` só significa que a conta pode fazer login, sem nenhum privilégio extra.)

Isso é o **princípio do menor privilégio**: a conta da aplicação tem apenas o que precisa para funcionar. Se a aplicação web for invadida (por exemplo, por SQL Injection) ou tiver um bug que gere um comando destrutivo, o atacante ou o erro ficam limitados ao que a conta permite. Ele não consegue apagar tabelas, alterar a estrutura nem criar usuários. O estrago possível fica muito menor e a estrutura do banco continua íntegra.

### Pergunta Discursiva 3 - Por que `'%'` e não `'localhost'`

No MariaDB, uma conta é identificada pelo par `'usuario'@'host'`, e o host é **de onde a conexão vem**. Com `'localhost'`, a conta só aceitaria conexões feitas de dentro do próprio contêiner do MariaDB.

No nosso ambiente, o CloudBeaver roda em **outro contêiner**. O Docker Compose cria uma rede virtual interna (`tarefa03_default`), e cada contêiner recebe um IP nela. O próprio erro 1142 acima mostra isso: a conexão chegou como `'app_biblioteca'@'172.18.0.3'`, que é o IP do contêiner do CloudBeaver, e não `localhost`. Por isso as contas foram criadas com `'%'`, o curinga que aceita qualquer origem. Sem ele, o CloudBeaver levaria "Access denied".

A rede interna também explica por que a conexão usa o host `mariadb`: o Docker tem um DNS interno que resolve o **nome do serviço** do compose para o IP do contêiner. Por isso nunca se usa `localhost` no CloudBeaver, porque `localhost` lá dentro é o próprio CloudBeaver.

> Observação: em ambiente de produção, o ideal seria restringir o host à faixa da rede (por exemplo, `'172.18.%'`) em vez de liberar qualquer endereço. No laboratório o `'%'` é aceitável porque a porta só está exposta na máquina local.

### Pergunta Discursiva 4 - Povoamento com IA e integridade referencial

O povoamento expandido (`povoamento.sql`) foi gerado com uma ferramenta de IA generativa a partir do prompt do roteiro. Ele adicionou 10 autores de várias nacionalidades e épocas (IDs 5 a 14) e 26 livros. Antes de executar, revisei os anos de publicação em relação ao ano de nascimento de cada autor. Também deixei os IDs dos autores explícitos no `INSERT`, para que os livros apontassem sempre para o autor certo.

Total final cadastrado: **14 autores e 31 livros** (4 + 10 autores; 5 + 26 livros).

```text
total_autores: 14
total_livros: 31
```

Ao tentar inserir um livro com `autor_id = 999` (autor inexistente), o MariaDB recusou:

```text
SQL Error [1452] [23000]: Cannot add or update a child row: a foreign key constraint fails
(`biblioteca`.`livros`, CONSTRAINT `livros_ibfk_1` FOREIGN KEY (`autor_id`) REFERENCES `autores` (`id`))
```

Quem impede é a **chave estrangeira** (`FOREIGN KEY (autor_id) REFERENCES autores(id)`), que garante a **integridade referencial**: um livro só pode apontar para um autor que exista na tabela `autores`. Assim o banco nunca fica com um livro "órfão".

### Pergunta Discursiva 5 - Vantagem de separar `autores` e `livros`

Separar em duas tabelas evita **repetir** os dados do autor em cada livro. O Machado de Assis tem 4 livros cadastrados. Se o nome e o país dele estivessem em cada linha de `livros`, seriam 4 cópias da mesma informação. Com a separação:

- **Uma fonte única da verdade:** para corrigir o nome ou o país de um autor, altero **uma linha** em `autores` e todos os livros passam a refletir a correção. Não existe o risco de uma cópia ficar "Machado de Assis" e outra "Machado de Assiz".
- **Menos espaço e menos erro de digitação:** cada livro guarda só um número (`autor_id`).
- **Consultas continuam fáceis:** a Consulta 4 (`JOIN`) junta o título com o nome do autor quando preciso, e a Consulta 5 (`GROUP BY a.id, a.nome` + `AVG`) calcula o preço médio por autor de forma confiável, porque cada autor é um registro único identificado pelo `id`. Com nomes repetidos e escritos de jeitos diferentes, o agrupamento separaria o mesmo autor em grupos distintos e a média sairia errada.
- **Regras de integridade:** a chave estrangeira impede livros de autores inexistentes (como visto na Pergunta 4).

Trecho do resultado da Consulta 5:

```text
| autor                  | preco_medio |
| Machado de Assis       |   36.675000 |
| Gabriel García Márquez |   54.566667 |
| Fiódor Dostoiévski     |   79.900000 |
```

---
