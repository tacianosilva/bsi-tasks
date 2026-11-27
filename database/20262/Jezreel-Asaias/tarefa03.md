# Tarefa 03 - Docker Compose, MariaDB e Administração de SGBD

## 1. Identificação e Repositório

- **Nome:** Jezreel Asaias da Silva Souza
- **GitHub:** [Jezreel-Asaias](https://github.com/Jezreel-Asaias)
- **E-mail acadêmico:** jezreel.asaias.silva.129@ufrn.edu.br
- **Repositório pessoal (arquivos da tarefa):** [dct2201-banco-de-dados](https://github.com/Jezreel-Asaias/dct2201-banco-de-dados/blob/main/README.md)
    - Pasta `tarefa03/`: `docker-compose.yml`, `.env.example`, `povoamento.sql` e `setup.sql`. O `.gitignore` (que bloqueia o `.env`) fica na raiz do repositório, e o `README.md` descreve cada arquivo.

Verificação de que o `.env` é ignorado pelo Git:

```
$ git check-ignore -v .env
.gitignore:1:.env       .env
```

---

## 2. Respostas às Perguntas Discursivas dos Passos Práticos

### Pergunta Discursiva 1 – DDL x DML e o `DROP TABLE`

DDL define a **estrutura** (`CREATE`, `ALTER`, `DROP`): é o projeto das gavetas. DML manipula o **conteúdo** (`INSERT`, `SELECT`, `UPDATE`, `DELETE`): é o que se guarda nas gavetas. Criar a tabela só cria o esqueleto vazio, e inserir registros é o que a preenche. Ao executar `DROP TABLE`, a tabela **e todos os dados dela são removidos** de forma definitiva (o DDL não é desfeito com `ROLLBACK` no MariaDB), a menos que exista backup.

### Pergunta Discursiva 2 – Erro 1142 com `app_biblioteca`

Ao rodar `DROP TABLE autores` com `app_biblioteca`, o MariaDB recusou a operação:

```
$ docker exec -it lab-mariadb mariadb -uapp_biblioteca -p'AppBib2026!' biblioteca -e "DROP TABLE autores;"
ERROR 1142 (42000) at line 1: DROP command denied to user 'app_biblioteca'@'localhost' for table `biblioteca`.`autores`
```

Conforme o `SHOW GRANTS`, essa conta só recebeu `SELECT, INSERT, UPDATE, DELETE` em `biblioteca.*` (DML) e não tem o privilégio `DROP`. Isso é o **princípio do menor privilégio**: cada conta tem só o que precisa. Se a aplicação web for invadida ou tiver um bug (por exemplo, SQL Injection), o atacante fica limitado a ler/alterar dados e não consegue apagar tabelas, alterar o esquema nem criar usuários, o que limita o dano.

```
Grants for app_biblioteca@%: GRANT SELECT, INSERT, UPDATE, DELETE ON `biblioteca`.* TO `app_biblioteca`@`%`
Grants for consulta@%:       GRANT SELECT ON `biblioteca`.* TO `consulta`@`%`
```

### Pergunta Discursiva 3 – Por que o host `'%'` e não `'localhost'`

No MariaDB a conta é o par `'usuario'@'host'`, e o host indica de onde a conexão pode vir. O CloudBeaver roda em **outro contêiner**, e a conexão chega ao MariaDB pela rede virtual criada pelo Docker Compose, com IP de origem na sub-rede do Docker (não `localhost`). Uma conta `'...'@'localhost'` só aceitaria conexões feitas de dentro do próprio contêiner do MariaDB. Por isso usamos `'%'`, que aceita qualquer origem. Em produção é recomendável restringir ao IP ou à sub-rede da aplicação. Pelo mesmo motivo, na conexão do CloudBeaver o host é o nome do serviço (`mariadb`), e nunca `localhost`, que apontaria para o próprio contêiner do CloudBeaver.

### Pergunta Discursiva 4 – Povoamento com IA e integridade referencial

O povoamento expandido (`povoamento.sql`) foi gerado com IA generativa a partir do prompt do roteiro e executado no banco. Resultado final:

```
+---------+       +--------+
| autores |       | livros |
+---------+       +--------+
|      14 |       |     38 |
+---------+       +--------+
```

(4 autores e 5 livros da carga inicial, mais 10 autores e 33 livros da carga expandida.)

Ao tentar inserir um livro com `autor_id = 999`, o banco recusou:

```
ERROR 1452 (23000) at line 1: Cannot add or update a child row: a foreign key constraint fails (`biblioteca`.`livros`, CONSTRAINT `livros_ibfk_1` FOREIGN KEY (`autor_id`) REFERENCES `autores` (`id`))
```

A regra que impede isso é a **chave estrangeira** (integridade referencial): `livros.autor_id` só aceita valores que existam em `autores.id`.

### Pergunta Discursiva 5 – Vantagem de separar `autores` e `livros`

Com duas tabelas, os dados do autor (nome, país) ficam em **um único lugar**, e cada livro só guarda o `autor_id`. Vantagens: (1) sem redundância, pois o nome não se repete em cada livro; (2) corrigir um dado, como o país, exige alterar uma só linha, evitando inconsistências (como o mesmo autor escrito de formas diferentes); (3) economia de espaço; (4) o `JOIN` (Consulta 4) e o agrupamento (Consulta 5) reconstroem e resumem a informação quando necessário, e a FK garante que nenhum livro aponte para um autor inexistente. Na Consulta 5, por exemplo, a média de preço por autor só funciona de forma confiável porque cada autor é identificado por um `id` único.

---

## 3. Respostas Dissertativas Conceituais

**a) Por que nunca usar `root` na aplicação?**
`root` tem poder total: pode ler, alterar e apagar qualquer banco, criar usuários e mudar privilégios. Se a aplicação usar `root` e as credenciais vazarem (ou houver SQL Injection), o atacante controla todo o servidor de banco: pode roubar, corromper ou apagar todos os dados e criar contas para manter acesso. Com uma conta restrita, o estrago fica limitado ao que ela pode fazer.

**b) DDL x DML e separação em contas distintas**
DDL (`CREATE`, `ALTER`, `DROP`) altera a estrutura do banco, e DML (`SELECT`, `INSERT`, `UPDATE`, `DELETE`) lida com os dados. Separá-los em contas diferentes é boa prática porque a aplicação no dia a dia só precisa de DML. Mudanças estruturais ficam com uma conta administrativa, usada apenas em migrações. Assim, bugs ou invasões na aplicação não conseguem destruir ou alterar o esquema, e fica mais fácil auditar quem fez o quê.

**c) `.env.example` sim, `.env` não**
O `.env.example` documenta quais variáveis o projeto exige, com valores genéricos, e ajuda quem clona o repositório. O `.env` guarda valores reais (senhas) e é específico de cada máquina. Se credenciais reais forem commitadas em repositório público, robôs que varrem o GitHub as encontram em minutos, e o resultado pode ser acesso indevido ao banco, vazamento de dados, uso abusivo de recursos e custos. Além disso, o histórico do Git preserva o segredo mesmo que o arquivo seja apagado depois, então a senha precisa ser **trocada/revogada**. (Neste próprio repositório, um `.env.bak` chegou a ser versionado por engano e foi removido; é um exemplo de como esse tipo de descuido acontece.)

**d) `.env` + `.gitignore` eliminam todos os riscos?**
Não. Eles apenas evitam que o segredo vá para o repositório. O arquivo continua em **texto puro** no disco: quem tiver acesso ao sistema de arquivos (outro usuário, malware, backup sem proteção, imagem Docker que copie o arquivo, logs, `docker inspect` mostrando variáveis de ambiente) consegue lê-lo. Em produção convém usar gestores de segredos (Docker/Kubernetes Secrets, Vault, serviços de nuvem), permissões restritas no arquivo, rotação periódica de senhas e privilégios mínimos.

**e) O que é um contêiner e vantagens do Docker no ensino**
Contêiner é um processo isolado que empacota a aplicação e suas dependências, compartilhando o kernel do sistema hospedeiro (mais leve que uma máquina virtual). Vantagens para aulas: ambiente **idêntico** para todos os alunos; instalação em poucos comandos (`docker compose up -d`); não "suja" o sistema operacional nem conflita com outras versões instaladas; fácil de destruir e recriar do zero (`down -v`); configuração versionada como código (reprodutível); e permite rodar vários ambientes isolados ao mesmo tempo.

---

## 4. Desafios Realizados

### Bloco A – Docker e Infraestrutura

**Desafio 1 – Alterar a porta para 3307**

```bash
sed -i 's/^MARIADB_PORT=.*/MARIADB_PORT=3307/' .env
docker compose up -d
docker ps --format "table {{.Names}}\t{{.Ports}}"
```

```
NAMES             PORTS
lab-mariadb       0.0.0.0:3307->3306/tcp, [::]:3307->3306/tcp
lab-cloudbeaver   0.0.0.0:8978->8978/tcp, [::]:8978->8978/tcp
```

O mapeamento passou a ser `3307:3306`, e o banco continuou respondendo (`SELECT COUNT(*) FROM biblioteca.livros` → 38). **O CloudBeaver não precisou ser reconfigurado**: ele acessa o MariaDB pela rede interna do Docker, usando `mariadb:3306`, e a porta interna do contêiner continua 3306. A porta 3307 vale apenas para clientes **fora** do Docker (por exemplo, um cliente SQL instalado na máquina, conectando em `localhost:3307`). Depois do teste, a porta foi restaurada para 3306.

**Desafio 2 – Dois ambientes simultâneos**
Copiei a pasta para `~/ambiente2` e alterei, no `docker-compose.yml`, os nomes dos contêineres (`lab2-mariadb`, `lab2-cloudbeaver`) e, no `.env`, as portas (`MARIADB_PORT=3308`, `CLOUDBEAVER_PORT=8979`):

```bash
sed -i 's/lab-mariadb/lab2-mariadb/; s/lab-cloudbeaver/lab2-cloudbeaver/' docker-compose.yml
sed -i 's/^MARIADB_PORT=.*/MARIADB_PORT=3308/; s/^CLOUDBEAVER_PORT=.*/CLOUDBEAVER_PORT=8979/' .env
docker compose up -d
```

```
NAMES              PORTS
lab2-cloudbeaver   0.0.0.0:8979->8978/tcp, [::]:8979->8978/tcp
lab2-mariadb       0.0.0.0:3308->3306/tcp, [::]:3308->3306/tcp
lab-mariadb        0.0.0.0:3306->3306/tcp, [::]:3306->3306/tcp
lab-cloudbeaver    0.0.0.0:8978->8978/tcp, [::]:8978->8978/tcp

DRIVER    VOLUME NAME
local     ambiente2_mariadb_data
local     tarefa03_mariadb_data
```

Quatro contêineres rodaram em paralelo porque eliminei os três pontos de conflito: (1) `container_name` precisa ser único no Docker; (2) as portas do **host** precisam ser únicas (3306/8978 no primeiro ambiente e 3308/8979 no segundo; as portas internas 3306/8978 podem se repetir, pois cada contêiner tem sua própria rede); (3) volumes e redes são prefixados pelo nome do projeto Compose, que é o nome da pasta (`tarefa03_...` e `ambiente2_...`), então os dados ficaram separados sem configuração extra.

**Desafio 3 – Persistência do volume e troca da senha de root**
Alterei `MARIADB_ROOT_PASSWORD` para `NovaSenha2026` no `.env` e executei `docker compose up -d`:

```
$ docker exec -it lab-mariadb mariadb -uroot -p'RootLab2026!aB' -e "SELECT 'senha antiga funciona' AS teste;"
+-----------------------+
| teste                 |
+-----------------------+
| senha antiga funciona |
+-----------------------+
$ docker exec -it lab-mariadb mariadb -uroot -p'NovaSenha2026' -e "SELECT 1;"
ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)
```

Isso ocorre porque o entrypoint da imagem só lê `MARIADB_ROOT_PASSWORD` na **primeira inicialização**, quando o diretório de dados está vazio. A senha fica gravada nas tabelas de usuários dentro do volume `mariadb_data`, que persiste entre recriações do contêiner. Como o volume já existia, a variável foi ignorada. Dois caminhos para aplicar uma nova senha:

1. **Destruir o volume** (perde os dados): `docker compose down -v` e depois `docker compose up -d`, o que reinicializa o banco com a senha do `.env`.
2. **Alterar a senha dentro do banco** (preserva os dados): `ALTER USER 'root'@'localhost' IDENTIFIED BY 'NovaSenha';` (e também para `'root'@'%'`), atualizando o `.env` para refletir a nova senha.

Depois do teste, o `.env` foi restaurado e os 38 livros continuavam no banco, o que confirma que os dados persistiram.

**Desafio 4 – Validação estrita `:?`**
Renomeei o `.env` temporariamente e executei `docker compose up -d`:

```
error while interpolating services.mariadb.environment.MARIADB_ROOT_PASSWORD: required variable MARIADB_ROOT_PASSWORD is missing a value: defina MARIADB_ROOT_PASSWORD no arquivo .env
```

O modificador `:?` faz o Compose **falhar cedo e com mensagem clara**, em vez de subir um banco com senha vazia/insegura ou com configuração incompleta. Em ambientes profissionais isso evita deploys inseguros e erros silenciosos, e a mensagem personalizada diz exatamente o que corrigir.

**Desafio 5 – `docker compose config`**

```
$ docker compose config | grep -E "MARIADB_ROOT_PASSWORD|MARIADB_DATABASE|published"
        published: "8978"      (CLOUDBEAVER_PORT)
      MARIADB_DATABASE: labdb
      MARIADB_ROOT_PASSWORD: RootLab2026!aB
        published: "3306"      (MARIADB_PORT)
```

Três variáveis resolvidas a partir do `.env`: `MARIADB_ROOT_PASSWORD`, `MARIADB_DATABASE` e as portas publicadas (`MARIADB_PORT` e `CLOUDBEAVER_PORT`).

### Bloco B – Modelagem e Consultas

**Desafio 6 – Tabela `emprestimos`**

```sql
CREATE TABLE emprestimos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  livro_id INT,
  data_emprestimo DATE,
  devolvido BOOLEAN,
  FOREIGN KEY (livro_id) REFERENCES livros(id)
);
```

**Desafio 7 – Carga da tabela empréstimos**

```sql
INSERT INTO emprestimos (livro_id, data_emprestimo, devolvido) VALUES
(1, '2026-10-01', FALSE),
(3, '2026-10-05', FALSE),
(4, '2026-09-20', TRUE);
```

**Desafio 8 – Pendências**

```sql
SELECT l.titulo, e.data_emprestimo, a.nome AS autor
FROM emprestimos e
JOIN livros l  ON e.livro_id = l.id
JOIN autores a ON l.autor_id = a.id
WHERE e.devolvido = FALSE;
```

```
+-------------------+-----------------+-------------------+
| titulo            | data_emprestimo | autor             |
+-------------------+-----------------+-------------------+
| Dom Casmurro      | 2026-10-01      | Machado de Assis  |
| A Hora da Estrela | 2026-10-05      | Clarice Lispector |
+-------------------+-----------------+-------------------+
```

**Desafio 9 – `HAVING`**

```sql
SELECT a.nome AS autor, COUNT(*) AS total_obras
FROM autores a
JOIN livros l ON l.autor_id = a.id
GROUP BY a.id, a.nome
HAVING COUNT(*) > 1;
```

Retornou os 14 autores, pois todos têm ao menos 2 livros (Machado de Assis com 4; Clarice, García Márquez, Jane Austen, Tolstói, Dostoiévski, Kafka, Woolf e Murakami com 3; os demais com 2). O `HAVING` filtra **grupos** depois do `GROUP BY`, enquanto o `WHERE` filtra linhas antes do agrupamento.

**Desafio 10 – `UPDATE` (+10%)**

```sql
UPDATE livros SET preco = ROUND(preco * 1.10, 2) WHERE titulo = 'Dom Casmurro';
```

O preço de "Dom Casmurro" passou de **39.90 para 43.89** (39,90 × 1,10). O `WHERE` garante que só esse livro foi alterado; sem ele, todos os preços seriam reajustados.

**Desafio 11 – `DELETE`**

```sql
INSERT INTO autores (nome, pais, ano_nascimento) VALUES ('Autor Teste', 'Brasil', 1990);
DELETE FROM autores WHERE nome = 'Autor Teste';
```

O autor foi inserido com `id = 15` e removido; depois disso a tabela voltou a ter 14 autores. A remoção foi aceita porque nenhum registro de `livros` referencia esse autor. A FK só impede apagar um registro "pai" quando existem "filhos" apontando para ele (apagar, por exemplo, Machado de Assis falharia com erro 1451).

### Bloco C – Administração e Privilégios

**Desafio 12 – Usuário `relatorios`**

```sql
CREATE USER 'relatorios'@'%' IDENTIFIED BY 'Relatorios2026!';
GRANT SELECT ON biblioteca.livros TO 'relatorios'@'%';
FLUSH PRIVILEGES;
```

O usuário foi criado pelo `setup.sql`. Conferência:

```
GRANT USAGE ON *.* TO `relatorios`@`%` IDENTIFIED BY PASSWORD '...'
GRANT SELECT ON `biblioteca`.`livros` TO `relatorios`@`%`
```

**Desafio 13 – Teste de visibilidade**
Conectado como `relatorios`, a leitura de `livros` funcionou e a de `autores` foi bloqueada:

```
ERROR 1142 (42000) at line 1: SELECT command denied to user 'relatorios'@'localhost' for table `biblioteca`.`autores`
```

O privilégio foi concedido apenas sobre `biblioteca.livros`. Sobre `autores` o usuário não tem nenhum, e por padrão o MariaDB nega o que não foi explicitamente concedido.

**Desafio 14 – `GRANT` e `REVOKE` dinâmicos**

```sql
-- como root
GRANT INSERT ON biblioteca.livros TO 'relatorios'@'%';
-- como relatorios: INSERT de teste (sucesso)
INSERT INTO livros (titulo, ano_publicacao, preco, autor_id) VALUES ('Livro de Teste', 2026, 10.00, 1);
-- como root
REVOKE INSERT ON biblioteca.livros FROM 'relatorios'@'%';
```

Com o `INSERT` concedido, a inserção funcionou. Depois do `REVOKE`, uma nova tentativa falhou:

```
ERROR 1142 (42000) at line 1: INSERT command denied to user 'relatorios'@'localhost' for table `biblioteca`.`livros`
```

Isso mostra que os privilégios podem ser concedidos e retirados dinamicamente, sem recriar o usuário. O registro de teste foi removido depois (`DELETE FROM livros WHERE titulo='Livro de Teste'`), e a tabela voltou a ter 38 livros.

**Desafio 15 – `setup.sql`**
Script idempotente versionado no repositório pessoal (`tarefa03/setup.sql`). Ele faz `DROP DATABASE IF EXISTS biblioteca`, recria o banco e as tabelas (`autores`, `livros`, `emprestimos`) com FKs, recria os usuários (`app_biblioteca`, `consulta` e `relatorios`) com `DROP USER IF EXISTS` + `CREATE USER` + `GRANT`, e carrega todos os dados. Executado com:

```bash
docker exec -i lab-mariadb mariadb -uroot -p'<senha>' < setup.sql
```

Pode ser rodado várias vezes com o mesmo resultado (14 autores, 38 livros e 3 empréstimos).
