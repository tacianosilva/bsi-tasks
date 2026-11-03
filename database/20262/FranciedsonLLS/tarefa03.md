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
## 3. Respostas Dissertativas Conceituais

### Questão a - Por que a aplicação nunca deve usar `root`

O `root` tem **todos os privilégios** sobre o servidor inteiro: pode apagar qualquer banco, alterar estruturas, criar e remover usuários, mudar senhas e ler os dados de todos os sistemas hospedados ali. Uma aplicação comercial precisa, em geral, apenas ler e gravar dados no seu próprio banco. Conectar com `root` dá a ela um poder que ela não usa e que vira risco.

Se as credenciais da aplicação vazarem, por exemplo por um arquivo de configuração exposto, um log ou SQL Injection, quem as obtiver passa a agir com os privilégios dessa conta:

- **com `root`:** o invasor controla o servidor inteiro. Pode apagar todos os bancos (`DROP DATABASE`), copiar todos os dados, criar uma conta própria para manter o acesso e até trancar os administradores, trocando a senha do `root`;
- **com uma conta de menor privilégio** (como a `app_biblioteca`): o dano fica restrito ao banco `biblioteca` e às operações de DML. Ainda é sério, porque ele pode ler e alterar dados, mas não destrói estruturas nem toma o servidor.

Por isso a conta da aplicação deve ter só o necessário, e o `root` fica reservado para administração.

### Questão b - Privilégios DDL x DML e por que separá-los

- **DDL** (Data Definition Language): privilégios sobre a **estrutura**, como `CREATE`, `ALTER`, `DROP`, `INDEX` e `REFERENCES`. Eles mudam o "formato" do banco.
- **DML** (Data Manipulation Language): privilégios sobre o **conteúdo**, como `SELECT`, `INSERT`, `UPDATE` e `DELETE`. Eles mexem nas linhas, sem mudar a estrutura.

No dia a dia, a aplicação só precisa de DML. Mudanças de estrutura acontecem raramente, em migrações planejadas feitas por um administrador. Separar em contas distintas (como `app_biblioteca` só com DML, `consulta` só com `SELECT` e o `root` para DDL) traz duas vantagens:
1. **Limita o estrago** de invasões e bugs, como mostrou o erro 1142: mesmo comprometida, a conta da aplicação não derruba tabelas.
2. **Separa responsabilidades e facilita a auditoria:** fica claro quem pode mudar a estrutura, e qualquer alteração de esquema passa obrigatoriamente pela conta administrativa.

### Questão c - Por que versionar o `.env.example` e nunca o `.env`

O `.env.example` é a **documentação do contrato de configuração**: mostra quais variáveis o projeto precisa (`MARIADB_ROOT_PASSWORD`, `MARIADB_DATABASE`, `MARIADB_PORT`, `CLOUDBEAVER_PORT`), com valores genéricos. Quem clona o repositório copia o arquivo para `.env` e preenche com os próprios valores. Ele não contém segredo nenhum, então pode e deve ser versionado.

O `.env` contém os **valores reais**, inclusive senhas. Se for commitado em um repositório público:
- qualquer pessoa pode ler as credenciais, e existem robôs que varrem o GitHub o tempo todo procurando senhas e chaves expostas;
- **apagar o arquivo depois não resolve**: ele continua no histórico do Git, em forks e em clones já feitos. A única solução segura é **trocar a senha** (considerar a credencial comprometida) e limpar o histórico;
- as consequências vão de acesso indevido ao banco, vazamento de dados pessoais (com implicações legais, como a LGPD) e perda de dados, até custos financeiros quando se trata de chaves de serviços de nuvem.

O `.gitignore` com a linha `.env` evita esse erro. Neste trabalho isso foi confirmado com `git check-ignore -v .env` e com o `git status`, que nunca listou o `.env`.

### Questão d - `.env` + `.gitignore` eliminam todos os riscos?

**Não.** Eles resolvem um problema específico: impedem que a senha vá parar no **repositório Git**. Mas o arquivo continua salvo **em texto puro** no disco, e outros riscos permanecem:

- **Acesso ao servidor ou à máquina:** qualquer pessoa ou processo com permissão de leitura na pasta (outro usuário do sistema, um malware, um invasor que entrou por outra falha) lê a senha diretamente.
- **Backups, cópias e imagens:** o `.env` pode ir parar em backups, arquivos `.zip`, imagens Docker ou serviços de sincronização sem proteção.
- **Exposição em tempo de execução:** neste próprio laboratório, `docker compose config` e `docker exec lab-mariadb printenv MARIADB_ROOT_PASSWORD` exibiram a senha em texto claro. Quem tem acesso ao Docker vê as variáveis de ambiente dos contêineres, e elas também podem aparecer em logs e mensagens de erro.
- **Erro humano:** basta um `git add -f .env`, um `.gitignore` apagado ou uma cópia com outro nome (como `.env.bak`) para o arquivo ser versionado.

Por isso, em produção, o recomendado é usar um **gerenciador de segredos** (Docker Secrets, HashiCorp Vault, AWS Secrets Manager, Azure Key Vault etc.), permissões de arquivo restritas, rotação periódica de senhas e o menor privilégio em todas as contas. O `.env` é uma boa prática para **desenvolvimento**, não uma solução completa de segurança.

### Questão e - O que é um contêiner e as vantagens do Docker no ensino

Um **contêiner** é um processo isolado que roda com tudo o que precisa (binários, bibliotecas e configuração) empacotado em uma **imagem**. Ele compartilha o kernel do sistema hospedeiro, por isso é muito mais leve e rápido que uma máquina virtual, mas tem o próprio sistema de arquivos, a própria rede e os próprios processos.

Vantagens em relação a instalar o SGBD direto no sistema do aluno:

- **Mesmo ambiente para todos:** a imagem `mariadb:11` é a mesma em Windows, Linux ou macOS, o que acaba com o "na minha máquina funciona".
- **Instalação e remoção limpas:** um `docker compose up -d` sobe tudo, e um `docker compose down -v` apaga tudo, sem deixar serviços, arquivos ou configurações espalhados pelo sistema.
- **Sem conflito com o que já existe:** neste trabalho, mudei a porta para 3307 e rodei **dois ambientes completos ao mesmo tempo** (Desafios 1 e 2), algo trabalhoso com instalação manual.
- **Infraestrutura como código:** o `docker-compose.yml` versionado documenta exatamente como o ambiente é montado, e qualquer pessoa reproduz o mesmo resultado.
- **Liberdade para errar:** dá para quebrar, apagar o volume e recomeçar do zero em segundos (o `setup.sql` recria o banco inteiro), o que é ideal para aprender.
- **Proximidade com o mercado:** é a mesma forma como bancos e serviços são executados em empresas e na nuvem.

---
## 4. Desafios Realizados

### Bloco A - Docker e Infraestrutura de Ambiente

#### Desafio 1 - Alteração da porta para 3307

Alterei `MARIADB_PORT=3306` para `MARIADB_PORT=3307` no `.env` e reapliquei a configuração:

```powershell
(Get-Content .env) -replace 'MARIADB_PORT=3306','MARIADB_PORT=3307' | Set-Content .env -Encoding ascii
docker compose up -d
docker ps --format "table {{.Names}}\t{{.Ports}}\t{{.Status}}"
```

```text
 ✔ Container lab-cloudbeaver Running
 ✔ Container lab-mariadb     Started
NAMES             PORTS                       STATUS
lab-mariadb       0.0.0.0:3307->3306/tcp      Up Less than a second
lab-cloudbeaver   0.0.0.0:8978->8978/tcp      Up 3 hours
```

**Reconfiguração do CloudBeaver: nenhuma foi necessária.** A conexão continuou com host `mariadb` e porta `3306`, e funcionou normalmente. Executei no CloudBeaver:

```sql
SELECT @@port;   -- resultado: 3306
```

O mapeamento `3307:3306` só muda a porta **do lado do host** (meu Windows). Dentro do contêiner, o MariaDB continua escutando na 3306. O CloudBeaver acessa o banco **pela rede interna do Docker**, contêiner para contêiner, onde a porta continua 3306. A porta 3307 só precisaria ser usada por um cliente rodando **fora** do Docker, direto no Windows (por exemplo, um DBeaver desktop em `localhost:3307`).

#### Desafio 2 - Dois ambientes simultâneos

Criei uma segunda pasta, `tarefa03/ambiente2/`, com outro `docker-compose.yml` e outro `.env`:

```text
# ambiente2/.env (valores do .env.example correspondente)
MARIADB_DATABASE=labdb2
MARIADB_PORT=3308
CLOUDBEAVER_PORT=8979
```

```powershell
cd ambiente2
docker compose up -d
docker ps --format "table {{.Names}}\t{{.Ports}}\t{{.Status}}"
docker volume ls
```

```text
 ✔ Network ambiente2_default     Created
 ✔ Volume ambiente2_mariadb_data Created
 ✔ Container lab2-mariadb        Started
 ✔ Container lab2-cloudbeaver    Started

NAMES              PORTS                       STATUS
lab2-cloudbeaver   0.0.0.0:8979->8978/tcp      Up Less than a second
lab2-mariadb       0.0.0.0:3308->3306/tcp      Up Less than a second
lab-mariadb        0.0.0.0:3307->3306/tcp      Up 2 seconds
lab-cloudbeaver    0.0.0.0:8978->8978/tcp      Up 3 hours

DRIVER    VOLUME NAME
local     ambiente2_mariadb_data
local     tarefa03_mariadb_data
```

Os quatro contêineres rodaram em paralelo sem conflito por causa de quatro cuidados:
1. **Nomes de contêiner diferentes:** `container_name` precisa ser único no Docker. Se o segundo compose também usasse `lab-mariadb`, a subida falharia com conflito de nome. Por isso o segundo ambiente usa `lab2-mariadb` e `lab2-cloudbeaver`.
2. **Portas do host diferentes:** duas aplicações não podem ocupar a mesma porta do host. O primeiro ambiente usa 3307/8978 e o segundo 3308/8979. As portas **internas** (3306 e 8978) podem se repetir, porque cada contêiner tem a sua própria rede.
3. **Volumes separados:** o Compose usa o nome da pasta como **nome do projeto** e prefixa os recursos com ele. Assim o volume `mariadb_data` virou `tarefa03_mariadb_data` em um ambiente e `ambiente2_mariadb_data` no outro, e cada banco tem seus próprios dados.
4. **Redes separadas:** pelo mesmo motivo, cada projeto ganhou sua rede (`tarefa03_default` e `ambiente2_default`). Por isso, nos dois ambientes, o CloudBeaver encontra o "seu" banco pelo mesmo nome `mariadb`, sem confusão.

Ao final, desliguei o segundo ambiente com `docker compose down` dentro de `ambiente2/`.

#### Desafio 3 - Persistência do volume e troca da senha root

Troquei a senha no `.env` para uma senha nova e subi de novo:

```powershell
(Get-Content .env) -replace 'MARIADB_ROOT_PASSWORD=<senha antiga>','MARIADB_ROOT_PASSWORD=<senha nova>' | Set-Content .env -Encoding ascii
docker compose up -d
docker exec lab-mariadb printenv MARIADB_ROOT_PASSWORD
docker exec lab-mariadb mariadb -uroot -p<senha antiga> -e "SELECT 'senha antiga funciona' AS resultado;"
docker exec lab-mariadb mariadb -uroot -p<senha nova>   -e "SELECT 'senha nova funciona' AS resultado;"
```

```text
 ✔ Container lab-mariadb     Started          <- contêiner recriado com a variável nova
<senha nova>                                  <- printenv: a variável dentro do contêiner já mudou

resultado
senha antiga funciona                         <- senha ANTIGA continua entrando

ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)   <- senha NOVA falha
```

**Por que isso acontece:** a variável `MARIADB_ROOT_PASSWORD` só é usada pelo script de inicialização da imagem (`docker-entrypoint.sh`) quando ele encontra o diretório de dados **vazio**, ou seja, na **primeira inicialização do volume**. Nessa hora ele cria o banco do sistema e grava a senha do `root` (já como hash) nas tabelas internas do MariaDB, dentro do volume `tarefa03_mariadb_data`. Nas subidas seguintes, o volume já tem dados, o script pula essa etapa e a variável é ignorada. O contêiner foi recriado com a variável nova (como o `printenv` mostrou), mas o banco continua usando a senha gravada no volume.

**Dois caminhos para aplicar uma nova senha de root:**
1. **Alterar a senha dentro do SGBD, preservando os dados.** Conectado como `root` com a senha atual:
   ```sql
   ALTER USER 'root'@'%'         IDENTIFIED BY 'nova_senha';
   ALTER USER 'root'@'localhost' IDENTIFIED BY 'nova_senha';
   FLUSH PRIVILEGES;
   ```
   Em seguida, atualizar o `.env` com a mesma senha, para manter a documentação coerente, e atualizar a senha salva na conexão do CloudBeaver.
2. **Recriar o volume do zero, perdendo os dados:**
   ```bash
   docker compose down -v   # remove contêineres, rede e o volume mariadb_data
   docker compose up -d     # volume novo e vazio -> o entrypoint aplica a senha do .env
   ```
   Depois, rodar o `setup.sql` para recriar banco, usuários e dados.

Ao final do teste, voltei o `.env` para a senha original e executei `docker compose up -d`.

#### Desafio 4 - Validação estrita com `:?`

Renomeei temporariamente o `.env` e tentei subir o ambiente:

```powershell
Rename-Item .env .env.tmp
docker compose up -d
Rename-Item .env.tmp .env
```

```text
error while interpolating services.mariadb.environment.MARIADB_ROOT_PASSWORD: required variable MARIADB_ROOT_PASSWORD is missing a value: defina MARIADB_ROOT_PASSWORD no arquivo .env
```

O Compose **abortou antes de criar ou alterar qualquer contêiner**. Isso aconteceu por causa do `${MARIADB_ROOT_PASSWORD:?defina MARIADB_ROOT_PASSWORD no arquivo .env}`. As outras variáveis usam `:-` e têm valor padrão (`labdb`, `3306`, `8978`), por isso não geraram erro. A senha, de propósito, não tem padrão.

**Importância em ambientes profissionais:** o `:?` faz a configuração **falhar cedo e de forma clara** ("fail fast"). Sem ele, o banco poderia subir com senha vazia ou com um valor padrão conhecido, ou o contêiner falharia depois, com um erro confuso nos logs. Em um pipeline de deploy, isso impede que um ambiente inseguro chegue a produção por esquecimento de uma variável. A mensagem personalizada ainda diz exatamente o que corrigir.

#### Desafio 5 - Variáveis resolvidas no `docker compose config`

```powershell
docker compose config
```

Trechos da saída (senha omitida):

```yaml
name: tarefa03
services:
  cloudbeaver:
    container_name: lab-cloudbeaver
    ports:
      - mode: ingress
        target: 8978
        published: "8978"        # <- CLOUDBEAVER_PORT
  mariadb:
    container_name: lab-mariadb
    environment:
      MARIADB_DATABASE: labdb               # <- MARIADB_DATABASE
      MARIADB_ROOT_PASSWORD: ********       # <- MARIADB_ROOT_PASSWORD (valor real do .env)
    ports:
      - mode: ingress
        target: 3306
        published: "3306"        # <- MARIADB_PORT
volumes:
  mariadb_data:
    name: tarefa03_mariadb_data
```

Variáveis resolvidas e interpoladas a partir do `.env`:
1. **`MARIADB_ROOT_PASSWORD`**: virou o valor real em `services.mariadb.environment`.
2. **`MARIADB_DATABASE`**: virou `labdb`.
3. **`MARIADB_PORT`**: virou `published: "3306"` (antes do Desafio 1).
4. **`CLOUDBEAVER_PORT`**: virou `published: "8978"`.

O comando também mostra o que o Compose deriva sozinho: o nome do projeto (`tarefa03`), a rede `tarefa03_default` e o volume `tarefa03_mariadb_data`. O fato de a senha aparecer em texto claro reforça o que foi discutido na Questão d.

### Bloco B - Modelagem e Consultas SQL Básicas

Todos executados como `root` no CloudBeaver (`Executed queries: 10 / 10`, `Updated Rows: 6`). Script completo em [`tarefa03/sql/06-desafios-bloco-b.sql`](https://github.com/FranciedsonLLS/dct2201-banco-de-dados/blob/main/tarefa03/sql/06-desafios-bloco-b.sql).

#### Desafio 6 - Tabela `emprestimos`

```sql
CREATE TABLE IF NOT EXISTS emprestimos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  livro_id INT,
  data_emprestimo DATE,
  devolvido BOOLEAN,
  FOREIGN KEY (livro_id) REFERENCES livros(id)
);
```

Conferência com `SHOW CREATE TABLE emprestimos`:

```text
CREATE TABLE `emprestimos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `livro_id` int(11) DEFAULT NULL,
  `data_emprestimo` date DEFAULT NULL,
  `devolvido` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `livro_id` (`livro_id`),
  CONSTRAINT `emprestimos_ibfk_1` FOREIGN KEY (`livro_id`) REFERENCES `livros` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

O MariaDB não tem um tipo booleano próprio: `BOOLEAN` é sinônimo de `TINYINT(1)`. Por isso `FALSE` é gravado como `0` e `TRUE` como `1`. O índice `livro_id` foi criado automaticamente para a chave estrangeira.

#### Desafio 7 - Três empréstimos

```sql
INSERT INTO emprestimos (livro_id, data_emprestimo, devolvido) VALUES
(1, '2026-10-20', FALSE),  -- Dom Casmurro (pendente)
(4, '2026-10-27', FALSE),  -- Cem Anos de Solidão (pendente)
(2, '2026-10-05', TRUE);   -- Memórias Póstumas de Brás Cubas (devolvido)
```

```text
+----+----------+-----------------+-----------+
| id | livro_id | data_emprestimo | devolvido |
+----+----------+-----------------+-----------+
|  1 |        1 | 2026-10-20      |         0 |
|  2 |        4 | 2026-10-27      |         0 |
|  3 |        2 | 2026-10-05      |         1 |
+----+----------+-----------------+-----------+
```

#### Desafio 8 - Empréstimos pendentes

```sql
SELECT l.titulo, e.data_emprestimo, a.nome AS autor
FROM emprestimos e
JOIN livros  l ON e.livro_id = l.id
JOIN autores a ON l.autor_id = a.id
WHERE e.devolvido = FALSE;
```

```text
+----------------------+-----------------+--------------------------+
| titulo               | data_emprestimo | autor                    |
+----------------------+-----------------+--------------------------+
| Dom Casmurro         | 2026-10-20      | Machado de Assis         |
| Cem Anos de Solidão  | 2026-10-27      | Gabriel García Márquez   |
+----------------------+-----------------+--------------------------+
```

São dois `JOIN` encadeados: `emprestimos → livros`, pela FK `livro_id`, e `livros → autores`, pela FK `autor_id`. O empréstimo devolvido (id 3) foi filtrado pelo `WHERE`.

#### Desafio 9 - Autores com mais de 1 livro (`HAVING`)

```sql
SELECT a.nome AS autor, COUNT(*) AS total_livros
FROM autores a
JOIN livros l ON l.autor_id = a.id
GROUP BY a.id, a.nome
HAVING COUNT(*) > 1;
```

```text
+--------------------------+--------------+
| autor                    | total_livros |
+--------------------------+--------------+
| Machado de Assis         |            4 |
| Clarice Lispector        |            3 |
| Gabriel García Márquez   |            3 |
| Jane Austen              |            3 |
| George Orwell            |            2 |
| Fiódor Dostoiévski       |            2 |
| Franz Kafka              |            2 |
| Victor Hugo              |            2 |
| Chimamanda Ngozi Adichie |            2 |
| Haruki Murakami          |            2 |
| Jorge Amado              |            2 |
| José Saramago            |            2 |
+--------------------------+--------------+
```

Dos 14 autores, 12 aparecem. Miguel de Cervantes e Mary Shelley ficaram de fora porque têm só um livro cada. O `WHERE` filtra **linhas** antes do agrupamento, enquanto o `HAVING` filtra **grupos** depois do `GROUP BY`. Por isso a condição sobre `COUNT(*)` só pode ficar no `HAVING`.

#### Desafio 10 - Reajuste de 10% (`UPDATE`)

```sql
SELECT id, titulo, preco FROM livros WHERE id = 1;   -- antes
UPDATE livros SET preco = ROUND(preco * 1.10, 2) WHERE id = 1;
SELECT id, titulo, preco FROM livros WHERE id = 1;   -- depois
```

```text
antes:  |  1 | Dom Casmurro | 39.90 |
depois: |  1 | Dom Casmurro | 43.89 |
```

O preço passou de R$ 39,90 para **R$ 43,89** (39,90 × 1,10 = 43,89), e apenas 1 linha foi afetada. O `WHERE id = 1` é essencial: sem ele, o `UPDATE` reajustaria **todos** os livros. Usei a chave primária no filtro para garantir que só aquele livro fosse alterado, e o `ROUND(..., 2)` mantém as duas casas decimais da coluna `DECIMAL(10,2)`.

#### Desafio 11 - Remoção de autor sem livros (`DELETE`)

```sql
INSERT INTO autores (nome, pais, ano_nascimento)
VALUES ('Autor Teste Sem Livros', 'Brasil', 2000);
SELECT * FROM autores WHERE nome = 'Autor Teste Sem Livros';   -- 1 linha

DELETE FROM autores WHERE nome = 'Autor Teste Sem Livros';
SELECT COUNT(*) FROM autores WHERE nome = 'Autor Teste Sem Livros';   -- 0
```

```text
+----------------------+
| autor_teste_restante |
+----------------------+
|                    0 |
+----------------------+
```

A remoção foi aceita porque a chave estrangeira fica na tabela **filha** (`livros.autor_id → autores.id`) e só bloqueia apagar um autor **que esteja sendo referenciado**. Como nenhum livro apontava para o autor de teste, não havia nenhuma linha "filha" que ficaria órfã, e a integridade referencial continuou garantida. Se eu tentasse apagar, por exemplo, o Machado de Assis (id 1), que tem livros, o MariaDB recusaria com o erro 1451 (*Cannot delete or update a parent row: a foreign key constraint fails*), já que a FK foi criada com o comportamento padrão (`RESTRICT`).

### Bloco C - Administração e Privilégios Avançados

Executado pelo terminal, conectando explicitamente como cada usuário com `docker exec ... mariadb -u<usuario>`. Como o cliente roda **dentro** do contêiner do MariaDB, as mensagens mostram `'relatorios'@'localhost'`. A conta `'relatorios'@'%'` também aceita conexões locais, porque `%` corresponde a qualquer host.

#### Desafio 12 - Usuário `relatorios`

```sql
-- como root
CREATE USER 'relatorios'@'%' IDENTIFIED BY 'Relatorios2026!';
GRANT SELECT ON biblioteca.livros TO 'relatorios'@'%';
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'relatorios'@'%';
```

```text
GRANT USAGE ON *.* TO `relatorios`@`%` IDENTIFIED BY PASSWORD '*...'
GRANT SELECT ON `biblioteca`.`livros` TO `relatorios`@`%`
```

Diferente das contas anteriores (`biblioteca.*`, o banco inteiro), aqui o privilégio foi dado **no nível de tabela** (`biblioteca.livros`).

#### Desafio 13 - Tentativa de ler `autores`

```powershell
docker exec lab-mariadb mariadb -urelatorios -p<senha> -t biblioteca -e "SELECT COUNT(*) AS livros_visiveis FROM livros; SELECT * FROM autores;"
```

```text
+-----------------+
| livros_visiveis |
+-----------------+
|              31 |
+-----------------+
ERROR 1142 (42000) at line 1: SELECT command denied to user 'relatorios'@'localhost' for table `biblioteca`.`autores`
```

A leitura de `livros` funcionou, mas a de `autores` foi bloqueada com o **erro 1142**. O motivo é que o `relatorios` só tem `SELECT` na tabela `livros`, e não no banco todo. Para qualquer outra tabela ele não tem privilégio nenhum. É o menor privilégio aplicado com granularidade de tabela: uma conta de relatórios enxerga apenas os dados de que precisa.

#### Desafio 14 - `GRANT` e `REVOKE` dinâmicos

```sql
-- 1) como root
GRANT INSERT ON biblioteca.livros TO 'relatorios'@'%';
SHOW GRANTS FOR 'relatorios'@'%';
--   GRANT SELECT, INSERT ON `biblioteca`.`livros` TO `relatorios`@`%`

-- 2) como relatorios: inserção de teste -> SUCESSO
INSERT INTO livros (titulo, ano_publicacao, preco, autor_id)
VALUES ('Livro Teste Relatorios 1', 2026, 10.00, 1);
--   | 36 | Livro Teste Relatorios 1 |

-- 3) como root
REVOKE INSERT ON biblioteca.livros FROM 'relatorios'@'%';
SHOW GRANTS FOR 'relatorios'@'%';
--   GRANT SELECT ON `biblioteca`.`livros` TO `relatorios`@`%`

-- 4) como relatorios: nova inserção -> FALHA
INSERT INTO livros (titulo, ano_publicacao, preco, autor_id)
VALUES ('Livro Teste Relatorios 2', 2026, 10.00, 1);
```

```text
ERROR 1142 (42000) at line 1: INSERT command denied to user 'relatorios'@'localhost' for table `biblioteca`.`livros`
```

Depois do `GRANT INSERT`, a inserção de teste funcionou na hora. Depois do `REVOKE INSERT`, a nova tentativa foi recusada com o **erro 1142**, e o `SHOW GRANTS` voltou a mostrar só o `SELECT`. As alterações feitas com `GRANT` e `REVOKE` passam a valer imediatamente, sem reiniciar o servidor, e o `REVOKE` retira só o privilégio indicado, mantendo os demais. Isso permite conceder um acesso temporário (como uma carga de dados pontual) e retirá-lo logo depois.

Observação: o livro de teste recebeu o `id` 36, e não 32, porque inserções que falham (como os testes com `autor_id = 999`) também consomem valores do `AUTO_INCREMENT`, e o InnoDB não reaproveita esses números. Ao final, removi o livro de teste como `root` (`DELETE FROM livros WHERE titulo = 'Livro Teste Relatorios 1';`), e a base voltou a ter 31 livros.

#### Desafio 15 - Script idempotente `setup.sql`

Arquivo: [`tarefa03/setup.sql`](https://github.com/FranciedsonLLS/dct2201-banco-de-dados/blob/main/tarefa03/setup.sql)

O script recria do zero, nesta ordem:
1. **Banco:** `DROP DATABASE IF EXISTS biblioteca;` e `CREATE DATABASE biblioteca` com `utf8mb4`.
2. **Tabelas e restrições:** `autores`, `livros` (FK para `autores`) e `emprestimos` (FK para `livros`), na ordem pai → filho.
3. **Usuários:** `DROP USER IF EXISTS` seguido de `CREATE USER` e `GRANT` para `app_biblioteca` (DML), `consulta` (SELECT) e `relatorios` (SELECT em `livros`).
4. **Carga de dados:** carga inicial (IDs 1 a 4), povoamento expandido (IDs 5 a 14) e os três empréstimos.
5. **Conferência:** um `SELECT` com os totais.

O que o torna **idempotente**, ou seja, com o mesmo resultado final não importa quantas vezes seja executado:
- O `DROP DATABASE IF EXISTS` apaga o banco antigo junto com todas as tabelas e dados. Assim os `CREATE TABLE` e `INSERT` sempre começam do zero, sem erro de "tabela já existe" e sem dados duplicados.
- Os `DROP USER IF EXISTS` são necessários porque **usuários não pertencem ao banco**: eles ficam nas tabelas de sistema e sobrevivem ao `DROP DATABASE`. Remover e recriar garante que senha e privilégios sejam sempre exatamente os do script. Os `GRANT` vêm **depois** da criação das tabelas porque o privilégio de nível de tabela (`biblioteca.livros`) exige que a tabela exista.
- Os IDs dos autores são explícitos, então os livros sempre apontam para o autor correto.

Teste de idempotência, com duas execuções seguidas:

```powershell
docker cp setup.sql lab-mariadb:/tmp/setup.sql
docker exec lab-mariadb sh -c 'mariadb -uroot -p$MARIADB_ROOT_PASSWORD -t < /tmp/setup.sql'   # 1ª execução
docker exec lab-mariadb sh -c 'mariadb -uroot -p$MARIADB_ROOT_PASSWORD -t < /tmp/setup.sql'   # 2ª execução
```

```text
=== 1ª execução ===
+---------------+--------------+-------------------+
| total_autores | total_livros | total_emprestimos |
+---------------+--------------+-------------------+
|            14 |           31 |                 3 |
+---------------+--------------+-------------------+
=== 2ª execução ===
+---------------+--------------+-------------------+
| total_autores | total_livros | total_emprestimos |
+---------------+--------------+-------------------+
|            14 |           31 |                 3 |
+---------------+--------------+-------------------+
```

As duas execuções terminaram sem erro e com os mesmos totais. Os privilégios conferidos depois disso também ficaram idênticos ao esperado:

```text
GRANT SELECT, INSERT, UPDATE, DELETE ON `biblioteca`.* TO `app_biblioteca`@`%`
GRANT SELECT ON `biblioteca`.* TO `consulta`@`%`
GRANT SELECT ON `biblioteca`.`livros` TO `relatorios`@`%`
```

> O `docker cp` foi usado em vez de redirecionar o arquivo pelo PowerShell (`Get-Content ... |`) porque o PowerShell do Windows pode alterar a codificação no pipe e corromper os acentos. Copiando o arquivo para dentro do contêiner, o cliente `mariadb` lê o UTF-8 original.
