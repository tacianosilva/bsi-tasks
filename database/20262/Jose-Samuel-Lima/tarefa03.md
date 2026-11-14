# Tarefa 03 — Docker Compose, MariaDB e Administração de SGBD

## 1. Identificação e repositório

- **Discente:** José-Samuel-Lima
- **Usuário GitHub:** [@Jose-Samuel-Lima](https://github.com/Jose-Samuel-Lima)
- **E-mail acadêmico:** jose.lima.146@ufrn.edu.br
- **Disciplina:** DCT2201 — Banco de Dados (Sistemas de Informação — CERES/UFRN)
- **Issue da tarefa:** [#558 — Tarefa 03 - Docker e SGBD - Jose-Samuel-Lima](https://github.com/tacianosilva/bsi-tasks/issues/558)
- **Repositório pessoal:** [https://github.com/Jose-Samuel-Lima/Banco-de-Dados](https://github.com/Jose-Samuel-Lima/Banco-de-Dados)
- **README do repositório pessoal:** [https://github.com/Jose-Samuel-Lima/Banco-de-Dados/blob/main/README.md](https://github.com/Jose-Samuel-Lima/Banco-de-Dados/blob/main/README.md)

Os arquivos de infraestrutura da Tarefa 03 estão na pasta [`tarefa03/`](https://github.com/Jose-Samuel-Lima/Banco-de-Dados/tree/main/tarefa03):

| Arquivo | Finalidade |
|---|---|
| [`docker-compose.yml`](https://github.com/Jose-Samuel-Lima/Banco-de-Dados/blob/main/tarefa03/docker-compose.yml) | Orquestra os serviços `mariadb` e `cloudbeaver`. |
| [`.env.example`](https://github.com/Jose-Samuel-Lima/Banco-de-Dados/blob/main/tarefa03/.env.example) | Modelo versionado das variáveis de ambiente, sem credenciais reais. |
| [`.gitignore`](https://github.com/Jose-Samuel-Lima/Banco-de-Dados/blob/main/.gitignore) | Bloqueia o arquivo local `.env`. |
| [`povoamento.sql`](https://github.com/Jose-Samuel-Lima/Banco-de-Dados/blob/main/tarefa03/povoamento.sql) | Carga expandida com 10 autores e 25 livros adicionais. |
| [`setup.sql`](https://github.com/Jose-Samuel-Lima/Banco-de-Dados/blob/main/tarefa03/setup.sql) | Script completo e reexecutável que recria banco, tabelas, usuários, privilégios e carga de dados. |

> **Observação sobre o CloudBeaver:** durante a execução, a imagem mais recente do CloudBeaver passou a ativar `forceHttps` no runtime e redirecionava `http://localhost:8978` para HTTPS, fazendo a página não carregar. A correção aplicada foi adicionar `CLOUDBEAVER_FORCE_HTTPS: "false"` ao serviço `cloudbeaver` no `docker-compose.yml`. Depois disso, `http://localhost:8978` passou a responder HTTP 200. As consultas SQL foram executadas no contêiner `lab-mariadb` com o cliente `mariadb` para gerar evidências reproduzíveis; a mesma conexão pode ser usada no editor SQL do CloudBeaver com host `mariadb` e porta interna `3306`.

## 2. Ambiente executado

- Docker Engine: `29.9.2`
- Docker Compose: `v5.6.1`
- MariaDB: `11.8.9-MariaDB-ubu2404`
- CloudBeaver: `26.2.4.202611021139`
- Sistema operacional: Windows (Docker Desktop com backend WSL2)

Contêineres em execução ao final da atividade:

```text
NAMES             STATUS              PORTS
lab-cloudbeaver   Up                  0.0.0.0:8978->8978/tcp, [::]:8978->8978/tcp
lab-mariadb       Up                  0.0.0.0:3306->3306/tcp, [::]:3306->3306/tcp
```

Verificação do `.env` ignorado:

```bash
$ cd tarefa03
$ git check-ignore -v .env
.gitignore:2:.env	.env
```

A linha `.gitignore:2:.env` confirma que o arquivo local de credenciais está bloqueado pelo Git.

### 2.1 Correção do acesso ao CloudBeaver

O primeiro acesso a `http://localhost:8978` falhava porque o CloudBeaver redirecionava a requisição para HTTPS, embora o contêiner estivesse escutando HTTP na porta 8978. O log apresentava:

```text
WARN i.c.server.jetty.RequestHostFilter - Request schema is 'http' but 'forceHttps' is enabled. Redirecting to 'https'.
```

A configuração de runtime da imagem tinha `"forceHttps": "${CLOUDBEAVER_FORCE_HTTPS:true}"`. A solução foi definir a variável no compose:

```yaml
  cloudbeaver:
    image: dbeaver/cloudbeaver:latest
    container_name: lab-cloudbeaver
    environment:
      CLOUDBEAVER_FORCE_HTTPS: "false"
```

Após recriar o serviço com `docker compose up -d`, a verificação passou a retornar:

```text
STATUS=200
```

## 3. Respostas às perguntas discursivas dos passos práticos

### Pergunta Discursiva 1 — DDL x DML e o efeito de `DROP TABLE`

**DDL (Data Definition Language)** é a parte do SQL usada para definir a **estrutura** do banco: criar, alterar ou remover bancos, tabelas, colunas, chaves e restrições. Exemplos: `CREATE DATABASE`, `CREATE TABLE`, `ALTER TABLE` e `DROP TABLE`. Já **DML (Data Manipulation Language)** trabalha com o **conteúdo** armazenado nessas estruturas: inserir, consultar, atualizar e remover linhas. Exemplos: `INSERT`, `SELECT`, `UPDATE` e `DELETE`.

Quando executamos `DROP TABLE autores`, removemos a definição da tabela e, junto com ela, **todos os registros que estavam dentro dela**. Não é uma operação de “limpar linhas”: a estrutura e os dados são destruídos. Por isso o comando é irreversível sem backup e deve ser usado com muita cautela. No exercício, o usuário `app_biblioteca` não possuía privilégio DDL e recebeu o erro 1142, justamente para impedir que uma aplicação de manipulação de dados apagasse a estrutura.

### Pergunta Discursiva 2 — Erro 1142 e o princípio do menor privilégio

Ao conectar como `app_biblioteca` e executar `DROP TABLE autores`, o MariaDB recusou a operação:

```text
ERROR 1142 (42000): DROP command denied to user 'app_biblioteca'@'127.0.0.1' for table `biblioteca`.`autores`
```

O erro 1142 significa **comando negado por falta de privilégio**. A conta `app_biblioteca` recebeu apenas `SELECT`, `INSERT`, `UPDATE` e `DELETE` sobre `biblioteca.*`; ela não recebeu `DROP`, `CREATE` ou `ALTER`. Portanto, o SGBD bloqueou a operação antes de alterar qualquer estrutura.

Essa restrição aplica o **princípio do menor privilégio**: cada conta recebe somente o mínimo necessário para sua função. Se a aplicação web for invadida ou tiver um defeito que execute um comando destrutivo, o dano fica limitado às operações DML permitidas. A estrutura do banco e os dados de outras tabelas continuam protegidos, e o ataque não consegue simplesmente derrubar o esquema com um `DROP TABLE`.

### Pergunta Discursiva 3 — Por que usar o host `'%'` em vez de `'localhost'`?

No MariaDB/MySQL, a conta é identificada por `'usuario'@'host'`. O host define de **onde** aquela conta pode se autenticar. `'localhost'` restringe a conexão à própria máquina, normalmente via socket UNIX ou loopback. Já `'%'` é o curinga que aceita conexões de qualquer endereço de rede.

No Docker Compose, o CloudBeaver e o MariaDB são contêineres separados. Quando o CloudBeaver conecta ao banco, a origem não é o `localhost` do contêiner do MariaDB: é o endereço IP do contêiner do CloudBeaver dentro da rede virtual criada pelo Compose. Se os usuários fossem criados apenas como `'app_biblioteca'@'localhost'`, a conexão vinda do CloudBeaver seria recusada. Por isso usamos `'%'`, que permite a autenticação a partir da rede interna do Docker. O nome `mariadb` resolve para o contêiner do SGBD dentro dessa rede, e a porta interna continua sendo `3306`.

### Pergunta Discursiva 4 — Povoamento expandido e integridade referencial

Após a carga inicial (4 autores e 5 livros) e a execução do `povoamento.sql` (10 autores e 25 livros adicionais), a base ficou com:

```text
total_autores
14
total_livros
30
```

Ou seja, **14 autores** e **30 livros** no total.

Se tentarmos inserir um livro com `autor_id = 999`, o MariaDB recusa a operação:

```text
ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails
(`biblioteca`.`livros`, CONSTRAINT `livros_ibfk_1` FOREIGN KEY (`autor_id`) REFERENCES `autores` (`id`))
```

A regra que impede essa ação é a **chave estrangeira** `livros.autor_id → autores.id`. Ela garante a **integridade referencial**: todo livro precisa apontar para um autor que realmente exista. Sem essa restrição, teríamos livros “órfãos”, com um `autor_id` que não corresponde a nenhum registro da tabela `autores`, quebrando as junções e a consistência dos dados.

### Pergunta Discursiva 5 — Vantagem de separar `autores` e `livros`

As Consultas 4 e 5 mostram a vantagem prática da modelagem relacional. A Consulta 4 faz `JOIN` entre `livros` e `autores` para exibir o título ao lado do nome real do autor. A Consulta 5 usa `GROUP BY` e `AVG` para calcular o preço médio por autor. Essas operações só são simples porque os dados estão organizados em tabelas relacionadas.

Se o nome e o país do autor fossem repetidos em cada linha de `livros`, teríamos **redundância** e vários problemas: o mesmo nome seria gravado muitas vezes, qualquer correção precisaria ser feita em várias linhas, aumentaria a chance de inconsistência (por exemplo, “Machado de Assis” escrito de formas diferentes) e o banco ocuparia mais espaço. Com a normalização, o autor é cadastrado uma única vez em `autores`, e `livros` guarda apenas a chave `autor_id`. Isso facilita atualizações, evita anomalias e permite que as consultas combinem as informações com `JOIN` quando necessário.

## 4. Respostas dissertativas conceituais

### Questão a — Por que uma aplicação comercial nunca deve usar o usuário `root`?

O `root` é uma conta administrativa com poder praticamente total: pode criar e apagar bancos, alterar estruturas, conceder privilégios, ler e modificar qualquer dado e, em muitos casos, comprometer a configuração do servidor. Uma aplicação web não precisa desse poder para funcionar; ela normalmente só precisa executar operações DML sobre o seu próprio banco.

Se as credenciais da aplicação forem vazadas e ela estiver usando `root`, o atacante herda todos esses poderes. Ele pode apagar tabelas, exfiltrar dados de outros bancos, criar usuários, alterar privilégios e até dificultar a recuperação do ambiente. Com uma conta restrita, o impacto fica limitado ao escopo concedido. Por isso o `root` deve ser usado apenas para administração pontual e por pessoas autorizadas, nunca como conta de execução da aplicação.

### Questão b — Privilégios DDL x DML e separação de contas

Privilégios **DDL** controlam a definição da estrutura: `CREATE`, `ALTER`, `DROP`, `INDEX`, `REFERENCES`, entre outros. Privilégios **DML** controlam os dados: `SELECT`, `INSERT`, `UPDATE` e `DELETE`.

Separar esses privilégios em contas distintas é uma boa prática de segurança porque reduz o “raio de dano”. A conta da aplicação pode receber apenas DML, enquanto a conta de administração/migração recebe DDL. Assim, um erro de programação ou uma invasão na aplicação não consegue alterar ou destruir o esquema. Além disso, a separação facilita auditoria: fica claro quem pode mudar a estrutura e quem apenas manipula dados.

### Questão c — `.env.example` versionado x `.env` não versionado

O `.env.example` é um **modelo/documentação** do contrato de configuração. Ele mostra quais variáveis existem, com valores genéricos ou descritivos, sem segredos reais. Por isso pode e deve ser versionado: outra pessoa consegue preparar o ambiente sabendo o que precisa definir.

O `.env` contém os **valores reais** da máquina local, incluindo senhas. Ele não deve ser versionado porque o repositório pode ser público, pode ser clonado por terceiros, pode vazar em um fork, em um backup ou no histórico do Git. Se uma credencial real for commitada, removê-la do arquivo atual não basta: ela continua no histórico e deve ser considerada comprometida. A consequência prática é acesso não autorizado ao banco, alteração ou exclusão de dados, uso indevido de recursos e necessidade de trocar a senha e revisar acessos.

### Questão d — `.env` + `.gitignore` eliminam todos os riscos?

Não. O `.env` e o `.gitignore` reduzem o risco de vazamento **acidental pelo Git**, mas não eliminam todos os riscos. O arquivo `.env` continua armazenado em texto puro no disco do computador ou do servidor. Quem tiver acesso ao sistema de arquivos, a um backup, a um snapshot de máquina, a um processo malicioso ou a um usuário com privilégios indevidos pode ler as credenciais.

Além disso, o `.gitignore` não protege contra:
- commit forçado com `git add -f`;
- arquivos copiados manualmente para outro local;
- variáveis impressas em logs;
- vazamento por e-mail, chat ou captura de tela;
- acesso físico ou remoto ao servidor.

Em produção, o ideal é usar um gerenciador de segredos (Vault, AWS Secrets Manager, Docker Secrets, Kubernetes Secrets etc.), criptografia, controle de acesso, rotação de credenciais e princípio do menor privilégio. O `.env` é aceitável para desenvolvimento local, mas não é uma solução completa de segurança.

### Questão e — O que é um contêiner e quais vantagens ele traz?

Um contêiner é uma unidade isolada de execução que empacota uma aplicação e suas dependências (bibliotecas, configurações, binários) e compartilha o kernel do sistema operacional hospedeiro. Ele é mais leve que uma máquina virtual completa e pode ser criado, iniciado, parado e removido rapidamente.

Para atividades didáticas de banco de dados, as vantagens incluem:
- **Reprodutibilidade:** todos os alunos usam a mesma imagem e a mesma versão do SGBD.
- **Isolamento:** o MariaDB do laboratório não interfere em instalações locais nem em outros projetos.
- **Facilidade de limpeza:** `docker compose down -v` remove o ambiente e os dados de teste.
- **Portabilidade:** o mesmo `docker-compose.yml` funciona em Windows, Linux e macOS com Docker.
- **Rapidez:** não é necessário instalar e configurar manualmente o SGBD no sistema operacional.
- **Persistência controlada:** volumes nomeados mantêm os dados entre reinícios e podem ser removidos de forma explícita.
- **Padronização de rede:** os serviços se comunicam pelo nome dentro da rede virtual do Compose, o que ensina conceitos reais de arquitetura de aplicações.

A desvantagem é que o aluno precisa entender o ciclo de vida dos contêineres, volumes, redes e variáveis de ambiente; ainda assim, o ganho de reprodutibilidade e isolamento compensa em laboratórios.

## 5. Desafios realizados

### Bloco A — Docker e infraestrutura de ambiente

#### Desafio 1 — Alteração da porta do SGBD para 3307

Alterei o `.env` local para:

```text
MARIADB_PORT=3307
```

Depois recriei o serviço:

```bash
docker compose up -d
docker compose ps
docker port lab-mariadb
```

Saída relevante:

```text
NAME              ...   PORTS
lab-cloudbeaver   ...   0.0.0.0:8978->8978/tcp, [::]:8978->8978/tcp
lab-mariadb       ...   0.0.0.0:3307->3306/tcp, [::]:3307->3306/tcp

3306/tcp -> 0.0.0.0:3307
3306/tcp -> [::]:3307
```

Testes de conectividade no host:

```text
Test-NetConnection localhost:3307 -> True
Test-NetConnection localhost:3306 -> False
```

O CloudBeaver continuou respondendo em `http://localhost:8978` (HTTP 200). Também validei a conexão interna a partir de outro contêiner na rede `tarefa03_default`:

```bash
docker run --rm --network tarefa03_default -e MYSQL_PWD mariadb:11 \
  mariadb -hmariadb -P3306 -uroot -e "SELECT 1 AS conexao_interna_ok;"
```

Resultado:

```text
conexao_interna_ok
1
```

**Como a conexão do CloudBeaver foi reconfigurada?** Na verdade, ela **não precisa ser alterada** quando apenas a porta do host muda. O mapeamento `3307:3306` significa “porta 3307 no host → porta 3306 dentro do contêiner”. O CloudBeaver está na mesma rede Docker do MariaDB e continua usando:

- **Host:** `mariadb`
- **Porta:** `3306`

A porta `3307` serve para clientes executados **no host** (por exemplo, um cliente MariaDB instalado no Windows). Se o CloudBeaver fosse configurado para acessar o host, ele usaria `host.docker.internal:3307`, mas esse não é o caso: dentro da rede do Compose, o nome do serviço e a porta interna permanecem `mariadb:3306`. Depois do teste, reverti o `.env` para `MARIADB_PORT=3306` e recriei o serviço.

#### Desafio 2 — Dois ambientes simultâneos

Criei uma segunda pasta, `t3-ambiente-b`, com um compose próprio. Para evitar conflitos, usei:

- projeto Compose diferente: `-p t3-ambiente-b`;
- nomes de contêiner diferentes: `lab-mariadb-b` e `lab-cloudbeaver-b`;
- portas de host diferentes: `3307` para o MariaDB e `8979` para o CloudBeaver;
- volume próprio: `mariadb_data_b`;
- rede própria, criada automaticamente pelo projeto `t3-ambiente-b_default`.

Compose do segundo ambiente:

```yaml
services:
  mariadb-b:
    image: mariadb:11
    container_name: lab-mariadb-b
    environment:
      MARIADB_ROOT_PASSWORD: ${MARIADB_ROOT_PASSWORD:?defina MARIADB_ROOT_PASSWORD no arquivo .env}
      MARIADB_DATABASE: ${MARIADB_DATABASE:-labdb_b}
    ports:
      - "${MARIADB_PORT:-3307}:3306"
    volumes:
      - mariadb_data_b:/var/lib/mysql

  cloudbeaver-b:
    image: dbeaver/cloudbeaver:latest
    container_name: lab-cloudbeaver-b
    environment:
      CLOUDBEAVER_FORCE_HTTPS: "false"
    ports:
      - "${CLOUDBEAVER_PORT:-8979}:8978"
    depends_on:
      - mariadb-b

volumes:
  mariadb_data_b:
```

`.env` do segundo ambiente:

```text
MARIADB_ROOT_PASSWORD=********
MARIADB_DATABASE=labdb_b
MARIADB_PORT=3307
CLOUDBEAVER_PORT=8979
```

Subida:

```bash
cd t3-ambiente-b
docker compose -p t3-ambiente-b up -d
docker ps --filter name=lab-
```

Saída com os quatro contêineres em paralelo:

```text
NAMES               STATUS          PORTS
lab-cloudbeaver-b   Up              0.0.0.0:8979->8978/tcp, [::]:8979->8978/tcp
lab-mariadb-b       Up              0.0.0.0:3307->3306/tcp, [::]:3307->3306/tcp
lab-cloudbeaver     Up              0.0.0.0:8978->8978/tcp, [::]:8978->8978/tcp
lab-mariadb         Up              0.0.0.0:3306->3306/tcp, [::]:3306->3306/tcp
```

Validações:

```text
CloudBeaver B em http://localhost:8979 -> HTTP 200
MariaDB B em localhost:3307 -> porta aberta (True)
```

Depois da evidência, removi o segundo ambiente sem afetar o primeiro:

```bash
docker compose -p t3-ambiente-b down -v
```

**Por que não houve conflito?** Porque cada ambiente tem seu próprio nome de projeto, seus próprios nomes de contêiner, suas próprias portas de host e seu próprio volume. O Docker Compose também cria redes separadas por projeto, então os serviços de um ambiente não enxergam os do outro pelo nome. O único recurso compartilhado é o daemon Docker, que orquestra tudo.

#### Desafio 3 — Persistência do volume e alteração da senha de root

Alterei temporariamente o `.env` para:

```text
MARIADB_ROOT_PASSWORD=NovaSenha2026!aB
```

Executei `docker compose up -d`. O contêiner do MariaDB foi recriado, mas o volume `mariadb_data` já existia. Testei as duas senhas:

```text
# senha antiga
resultado
senha antiga ainda funciona

# senha nova
ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)
```

**Por que isso ocorre?** O entrypoint da imagem MariaDB só usa `MARIADB_ROOT_PASSWORD` para configurar a senha do root quando o diretório `/var/lib/mysql` está vazio, ou seja, na **primeira inicialização** do volume. Depois que o banco já foi inicializado, a senha fica gravada nas tabelas internas do MariaDB (`mysql.user`). Alterar a variável no `.env` e recriar o contêiner não reaplica essa configuração, porque o volume persistente é reaproveitado. A senha antiga continua válida e a nova não existe.

**Dois caminhos possíveis para aplicar uma nova senha:**

1. **Caminho destrutivo (perde os dados):** remover o volume e reinicializar do zero.
   ```bash
   docker compose down -v
   # editar .env com a nova senha
   docker compose up -d
   ```
   O entrypoint criará um diretório de dados novo e aplicará a nova senha. É simples, mas apaga todos os bancos e tabelas.

2. **Caminho não destrutivo (preserva os dados):** entrar com a senha antiga e alterar a senha via SQL.
   ```sql
   ALTER USER 'root'@'%' IDENTIFIED BY 'NovaSenha2026!aB';
   ALTER USER 'root'@'localhost' IDENTIFIED BY 'NovaSenha2026!aB';
   FLUSH PRIVILEGES;
   ```
   Depois disso, atualizar o `.env` para a nova senha e recriar o serviço com `docker compose up -d`. O volume e os dados são preservados. É importante alterar as duas contas (`root@%` e `root@localhost`), pois o MariaDB pode ter entradas distintas para cada host.

Depois do teste, reverti o `.env` para a senha original e recriei o serviço. A base permaneceu com 14 autores, 30 livros e 3 empréstimos.

#### Desafio 4 — Comportamento da validação estrita `:?`

Em uma cópia do compose sem o arquivo `.env`, executei:

```bash
docker compose config
```

O Compose abortou com:

```text
error while interpolating services.mariadb.environment.MARIADB_ROOT_PASSWORD:
required variable MARIADB_ROOT_PASSWORD is missing a value:
defina MARIADB_ROOT_PASSWORD no arquivo .env
```

**Importância do `:?`:** o modificador transforma uma variável obrigatória em uma **falha rápida e explícita**. Sem ele, o Compose poderia subir o MariaDB com senha vazia ou com um valor padrão inseguro, criando um banco exposto. Em ambientes profissionais, isso é essencial em pipelines de CI/CD, implantação automatizada e ambientes de produção: é melhor o processo falhar imediatamente, com uma mensagem clara, do que iniciar um serviço em estado inseguro. O `:?` também documenta a dependência de configuração e evita erros silenciosos.

#### Desafio 5 — Inspeção de variáveis no Compose

Executei:

```bash
docker compose config
```

O Compose resolveu e interpolou, entre outras, as seguintes variáveis:

| Variável | Valor resolvido |
|---|---|
| `MARIADB_ROOT_PASSWORD` | valor definido no `.env` (omitido aqui por segurança) |
| `MARIADB_DATABASE` | `labdb` |
| `MARIADB_PORT` | `3306` (porta publicada no host) |
| `CLOUDBEAVER_PORT` | `8978` |
| `CLOUDBEAVER_FORCE_HTTPS` | `"false"` |

Trecho da saída (com a senha mascarada):

```text
CLOUDBEAVER_FORCE_HTTPS: "false"
target: 8978
published: "8978"
MARIADB_DATABASE: labdb
MARIADB_ROOT_PASSWORD: ********
target: /var/lib/mysql
target: 3306
published: "3306"
```

A interpolação mostra que o Compose leu o `.env`, aplicou os valores e montou a configuração final antes de criar os contêineres. Os fallbacks `:-` foram usados em `MARIADB_DATABASE` e nas portas; a validação `:?` foi usada na senha do root.

### Bloco B — Modelagem e consultas SQL básicas

#### Desafio 6 — Criação da tabela `emprestimos`

```sql
USE biblioteca;

CREATE TABLE emprestimos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  livro_id INT NOT NULL,
  data_emprestimo DATE NOT NULL,
  devolvido BOOLEAN NOT NULL DEFAULT FALSE,
  FOREIGN KEY (livro_id) REFERENCES livros(id)
);
```

Estrutura criada:

```text
Field            Type        Null  Key  Default  Extra
id               int(11)     NO    PRI  NULL     auto_increment
livro_id         int(11)     NO    MUL  NULL
data_emprestimo  date        NO         NULL
devolvido        tinyint(1)  NO         0
```

Definição completa:

```sql
CREATE TABLE `emprestimos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `livro_id` int(11) NOT NULL,
  `data_emprestimo` date NOT NULL,
  `devolvido` tinyint(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`),
  KEY `livro_id` (`livro_id`),
  CONSTRAINT `emprestimos_ibfk_1` FOREIGN KEY (`livro_id`) REFERENCES `livros` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
```

A chave estrangeira `livro_id` garante que um empréstimo só possa ser registrado para um livro existente. `BOOLEAN` no MariaDB é armazenado como `TINYINT(1)`, com `0` para falso e `1` para verdadeiro.

#### Desafio 7 — Carga da tabela `emprestimos`

```sql
INSERT INTO emprestimos (livro_id, data_emprestimo, devolvido) VALUES
(1, '2026-10-01', FALSE),
(3, '2026-10-05', FALSE),
(5, '2026-09-20', TRUE);
```

Resultado:

```text
id  livro_id  data_emprestimo  devolvido
1   1         2026-10-01       0
2   3         2026-10-05       0
3   5         2026-09-20       1
```

Dois empréstimos estão pendentes (`0`) e um já foi devolvido (`1`).

#### Desafio 8 — Consulta de empréstimos pendentes

```sql
SELECT l.titulo, e.data_emprestimo, a.nome AS autor
FROM emprestimos e
JOIN livros l ON e.livro_id = l.id
JOIN autores a ON l.autor_id = a.id
WHERE e.devolvido = FALSE;
```

Resultado:

```text
titulo             data_emprestimo  autor
Dom Casmurro       2026-10-01       Machado de Assis
A Hora da Estrela  2026-10-05       Clarice Lispector
```

A consulta usa dois `JOIN`: um para recuperar o título do livro e outro para recuperar o autor desse livro. O filtro `devolvido = FALSE` mantém apenas os empréstimos em aberto.

#### Desafio 9 — Agrupamento com `HAVING`

```sql
SELECT a.nome AS autor, COUNT(*) AS total_livros
FROM autores a
JOIN livros l ON a.id = l.autor_id
GROUP BY a.id, a.nome
HAVING COUNT(*) > 1
ORDER BY total_livros DESC, autor;
```

Resultado:

```text
autor                      total_livros
Machado de Assis           4
Clarice Lispector          3
Gabriel García Márquez     3
Chimamanda Ngozi Adichie   2
Fiódor Dostoiévski         2
Franz Kafka                2
Haruki Murakami            2
Isabel Allende             2
Jane Austen                2
Jorge Amado                2
José Saramago              2
Toni Morrison              2
Virginia Woolf             2
```

O `GROUP BY` agrupa as linhas por autor e `COUNT(*)` conta quantos livros cada um tem. O `HAVING` filtra os **grupos** depois da agregação; por isso ele é usado aqui em vez de `WHERE`, que filtraria linhas antes de agrupar. O resultado mostra apenas autores com mais de um livro.

#### Desafio 10 — Atualização proporcional de preço

Antes:

```text
id  titulo         preco
1   Dom Casmurro   39.90
```

Comando:

```sql
UPDATE livros
SET preco = preco * 1.10
WHERE id = 1;
```

Depois:

```text
id  titulo         preco
1   Dom Casmurro   43.89
```

O `UPDATE` alterou somente a linha com `id = 1`, aplicando um acréscimo de 10% sobre o preço atual (`39.90 × 1.10 = 43.89`). O `WHERE` é essencial: sem ele, todos os livros seriam reajustados. O valor foi posteriormente restaurado pelo `setup.sql` para manter o estado padronizado da entrega.

#### Desafio 11 — Remoção condicional de autor sem livros

```sql
INSERT INTO autores (nome, pais, ano_nascimento)
VALUES ('Autor Temporário', 'Brasil', 1990);

SELECT id, nome FROM autores WHERE nome = 'Autor Temporário';
```

Resultado:

```text
id  nome
15  Autor Temporário
```

Remoção:

```sql
DELETE FROM autores
WHERE nome = 'Autor Temporário';

SELECT COUNT(*) AS ocorrencias
FROM autores
WHERE nome = 'Autor Temporário';
```

Resultado:

```text
ocorrencias
0
```

A remoção foi aceita porque o autor recém-criado **não possuía nenhum livro associado** em `livros`. A chave estrangeira `livros.autor_id → autores.id` só seria violada se existisse pelo menos um livro apontando para o `id` 15. Como não havia filhos, o `DELETE` não quebrou a integridade referencial. Se o autor tivesse livros, o MariaDB recusaria a remoção com erro 1451, a menos que os livros fossem removidos/reatribuídos antes ou que a FK tivesse uma regra `ON DELETE CASCADE`/`SET NULL`.

### Bloco C — Administração e privilégios avançados

#### Desafio 12 — Usuário restrito para relatórios

```sql
CREATE USER 'relatorios'@'%' IDENTIFIED BY 'Relatorios2026!';
GRANT SELECT ON biblioteca.livros TO 'relatorios'@'%';
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'relatorios'@'%';
```

Saída:

```text
Grants for relatorios@%
GRANT USAGE ON *.* TO `relatorios`@`%` IDENTIFIED BY PASSWORD '*83EEE5D32FC681716C2F6D6E7A4637027FE007EF'
GRANT SELECT ON `biblioteca`.`livros` TO `relatorios`@`%`
```

O usuário recebeu `SELECT` **apenas na tabela `livros`**, não no banco inteiro. Isso é um exemplo de privilégio no nível de tabela: ele pode ler os livros, mas não os autores nem outras tabelas.

#### Desafio 13 — Teste de restrição de visibilidade

Conectado como `relatorios`, executei:

```sql
USE biblioteca;
SELECT * FROM autores;
```

O SGBD recusou:

```text
ERROR 1142 (42000): SELECT command denied to user 'relatorios'@'127.0.0.1' for table `biblioteca`.`autores`
```

Para confirmar que o privilégio sobre `livros` funciona, executei:

```sql
SELECT COUNT(*) AS total_livros_visiveis FROM biblioteca.livros;
```

Resultado:

```text
total_livros_visiveis
30
```

O bloqueio ocorre porque o `GRANT SELECT` foi concedido somente em `biblioteca.livros`. A conta não tem `SELECT` em `biblioteca.autores`, então o MariaDB aplica o princípio do menor privilégio e nega a consulta. Isso é útil para relatórios que só precisam de uma tabela específica, sem expor dados de autores ou de outras tabelas.

#### Desafio 14 — Concessão e revogação dinâmica de privilégios

Conectado como `root`, concedi `INSERT`:

```sql
GRANT INSERT ON biblioteca.livros TO 'relatorios'@'%';
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'relatorios'@'%';
```

Saída:

```text
Grants for relatorios@%
GRANT USAGE ON *.* TO `relatorios`@`%` IDENTIFIED BY PASSWORD '*83EEE5D32FC681716C2F6D6E7A4637027FE007EF'
GRANT SELECT, INSERT ON `biblioteca`.`livros` TO `relatorios`@`%`
```

Com o novo privilégio, a inserção de teste funcionou:

```sql
INSERT INTO livros (titulo, ano_publicacao, preco, autor_id)
VALUES ('Livro de Teste', 2026, 19.90, 1);

SELECT * FROM livros WHERE titulo = 'Livro de Teste';
```

Resultado:

```text
id  titulo          ano_publicacao  preco  autor_id
31  Livro de Teste  2026            19.90  1
```

Em seguida, revoguei o privilégio:

```sql
REVOKE INSERT ON biblioteca.livros FROM 'relatorios'@'%';
FLUSH PRIVILEGES;
SHOW GRANTS FOR 'relatorios'@'%';
```

Saída:

```text
Grants for relatorios@%
GRANT USAGE ON *.* TO `relatorios`@`%` IDENTIFIED BY PASSWORD '*83EEE5D32FC681716C2F6D6E7A4637027FE007EF'
GRANT SELECT ON `biblioteca`.`livros` TO `relatorios`@`%`
```

Tentando inserir novamente após a revogação:

```sql
INSERT INTO livros (titulo, ano_publicacao, preco, autor_id)
VALUES ('Livro Bloqueado', 2026, 29.90, 1);
```

Resultado:

```text
ERROR 1142 (42000): INSERT command denied to user 'relatorios'@'127.0.0.1' for table `biblioteca`.`livros`
```

O `GRANT` e o `REVOKE` têm efeito imediato sobre as verificações de privilégio do MariaDB. O `FLUSH PRIVILEGES` foi usado por hábito e para garantir a recarga das tabelas de privilégios, embora `GRANT`/`REVOKE` já atualizem essas tabelas automaticamente. A conta voltou a ter somente leitura em `livros`, e a tentativa de escrita foi negada com 1142.

#### Desafio 15 — Script idempotente `setup.sql`

O arquivo [`setup.sql`](https://github.com/Jose-Samuel-Lima/Banco-de-Dados/blob/main/tarefa03/setup.sql) recria do zero:

- o banco `biblioteca` com `utf8mb4`;
- as tabelas `autores`, `livros` e `emprestimos`, com chaves primárias e estrangeiras;
- 14 autores e 30 livros (carga inicial + povoamento expandido);
- 3 empréstimos (2 pendentes e 1 devolvido);
- os usuários `app_biblioteca`, `consulta` e `relatorios`, com privilégios distintos;
- uma conferência final com `COUNT(*)` das três tabelas.

O script usa `DROP USER IF EXISTS` e `DROP DATABASE IF EXISTS` antes de recriar tudo. Isso permite executá-lo várias vezes e sempre chegar ao mesmo estado final. Ele é um script de **reset padronizado**: a reexecução é idempotente em relação ao estado final, mas **não preserva** dados existentes, porque o banco é recriado do zero.

Executei o script duas vezes. A segunda execução produziu:

```text
tabela       total
autores      14
livros       30
emprestimos  3
```

Trecho principal do script:

```sql
DROP USER IF EXISTS 'app_biblioteca'@'%';
DROP USER IF EXISTS 'consulta'@'%';
DROP USER IF EXISTS 'relatorios'@'%';

DROP DATABASE IF EXISTS biblioteca;

CREATE DATABASE biblioteca
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_general_ci;

USE biblioteca;

CREATE TABLE autores (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  pais VARCHAR(50),
  ano_nascimento INT
);

CREATE TABLE livros (
  id INT AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR(150) NOT NULL,
  ano_publicacao INT,
  preco DECIMAL(10,2),
  autor_id INT,
  FOREIGN KEY (autor_id) REFERENCES autores(id)
);

CREATE TABLE emprestimos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  livro_id INT NOT NULL,
  data_emprestimo DATE NOT NULL,
  devolvido BOOLEAN NOT NULL DEFAULT FALSE,
  FOREIGN KEY (livro_id) REFERENCES livros(id)
);

-- Carga de 14 autores e 30 livros (trecho omitido; arquivo completo no repositório)

CREATE USER 'app_biblioteca'@'%' IDENTIFIED BY 'AppBib2026!';
GRANT SELECT, INSERT, UPDATE, DELETE ON biblioteca.* TO 'app_biblioteca'@'%';

CREATE USER 'consulta'@'%' IDENTIFIED BY 'Consulta2026!';
GRANT SELECT ON biblioteca.* TO 'consulta'@'%';

CREATE USER 'relatorios'@'%' IDENTIFIED BY 'Relatorios2026!';
GRANT SELECT ON biblioteca.livros TO 'relatorios'@'%';

FLUSH PRIVILEGES;

SELECT 'autores' AS tabela, COUNT(*) AS total FROM autores
UNION ALL
SELECT 'livros', COUNT(*) FROM livros
UNION ALL
SELECT 'emprestimos', COUNT(*) FROM emprestimos;
```

## 6. Consultas obrigatórias — resultados

As seis consultas foram executadas após a carga expandida. Abaixo estão os resultados completos.

### Consulta 1 — `SELECT * FROM livros`

```sql
SELECT * FROM livros;
```

```text
id  titulo                              ano_publicacao  preco   autor_id
1   Dom Casmurro                        1899            39.90   1
2   Memórias Póstumas de Brás Cubas     1881            45.00   1
3   A Hora da Estrela                   1977            32.50   2
4   Cem Anos de Solidão                 1967            59.90   3
5   Orgulho e Preconceito               1813            29.90   4
6   Crime e Castigo                     1866            54.90   5
7   Os Irmãos Karamázov                 1880            69.90   5
8   Mrs. Dalloway                       1925            42.50   6
9   Ao Farol                            1927            47.00   6
10  Capitães da Areia                   1937            38.90   7
11  Gabriela, Cravo e Canela            1958            44.90   7
12  Amada                               1987            49.90   8
13  O Olho Mais Azul                    1970            39.90   8
14  Norwegian Wood                      1987            52.00   9
15  Kafka à Beira-Mar                   2002            64.90   9
16  Americanah                          2013            56.90   10
17  Meio Sol Amarelo                    2006            48.50   10
18  Dom Quixote                         1605            79.90   11
19  A Metamorfose                       1915            29.90   12
20  O Processo                          1925            45.90   12
21  A Casa dos Espíritos                1982            51.90   13
22  Paula                               1994            46.50   13
23  Ensaio sobre a Cegueira             1995            58.90   14
24  O Evangelho Segundo Jesus Cristo    1991            55.00   14
25  Quincas Borba                       1891            41.90   1
26  A Paixão Segundo G.H.               1964            36.90   2
27  Água Viva                           1973            34.50   2
28  O Amor nos Tempos do Cólera         1985            57.90   3
29  Crônica de uma Morte Anunciada      1981            43.90   3
30  Emma                                1815            35.50   4
```

### Consulta 2 — projeção e ordenação descendente

```sql
SELECT titulo, ano_publicacao
FROM livros
ORDER BY ano_publicacao DESC;
```

```text
titulo                              ano_publicacao
Americanah                          2013
Meio Sol Amarelo                    2006
Kafka à Beira-Mar                   2002
Ensaio sobre a Cegueira             1995
Paula                               1994
O Evangelho Segundo Jesus Cristo    1991
Amada                               1987
Norwegian Wood                      1987
O Amor nos Tempos do Cólera         1985
A Casa dos Espíritos                1982
Crônica de uma Morte Anunciada      1981
A Hora da Estrela                   1977
Água Viva                           1973
O Olho Mais Azul                    1970
Cem Anos de Solidão                 1967
A Paixão Segundo G.H.               1964
Gabriela, Cravo e Canela            1958
Capitães da Areia                   1937
Ao Farol                            1927
Mrs. Dalloway                       1925
O Processo                          1925
A Metamorfose                       1915
Dom Casmurro                        1899
Quincas Borba                       1891
Memórias Póstumas de Brás Cubas     1881
Os Irmãos Karamázov                 1880
Crime e Castigo                     1866
Emma                                1815
Orgulho e Preconceito               1813
Dom Quixote                         1605
```

### Consulta 3 — filtro `WHERE ano_publicacao < 1900`

```sql
SELECT *
FROM livros
WHERE ano_publicacao < 1900;
```

```text
id  titulo                              ano_publicacao  preco   autor_id
1   Dom Casmurro                        1899            39.90   1
2   Memórias Póstumas de Brás Cubas     1881            45.00   1
5   Orgulho e Preconceito               1813            29.90   4
6   Crime e Castigo                     1866            54.90   5
7   Os Irmãos Karamázov                 1880            69.90   5
18  Dom Quixote                         1605            79.90   11
25  Quincas Borba                       1891            41.90   1
30  Emma                                1815            35.50   4
```

### Consulta 4 — `INNER JOIN` entre livros e autores

```sql
SELECT l.titulo, a.nome AS autor, l.preco
FROM livros l
JOIN autores a ON l.autor_id = a.id;
```

```text
titulo                              autor                     preco
Dom Casmurro                        Machado de Assis          39.90
Memórias Póstumas de Brás Cubas     Machado de Assis          45.00
Quincas Borba                       Machado de Assis          41.90
A Hora da Estrela                   Clarice Lispector         32.50
A Paixão Segundo G.H.               Clarice Lispector         36.90
Água Viva                           Clarice Lispector         34.50
Cem Anos de Solidão                 Gabriel García Márquez    59.90
O Amor nos Tempos do Cólera         Gabriel García Márquez    57.90
Crônica de uma Morte Anunciada      Gabriel García Márquez    43.90
Orgulho e Preconceito               Jane Austen               29.90
Emma                                Jane Austen               35.50
Crime e Castigo                     Fiódor Dostoiévski        54.90
Os Irmãos Karamázov                 Fiódor Dostoiévski        69.90
Mrs. Dalloway                       Virginia Woolf            42.50
Ao Farol                            Virginia Woolf            47.00
Capitães da Areia                   Jorge Amado               38.90
Gabriela, Cravo e Canela            Jorge Amado               44.90
Amada                               Toni Morrison             49.90
O Olho Mais Azul                    Toni Morrison             39.90
Norwegian Wood                      Haruki Murakami           52.00
Kafka à Beira-Mar                   Haruki Murakami           64.90
Americanah                          Chimamanda Ngozi Adichie  56.90
Meio Sol Amarelo                    Chimamanda Ngozi Adichie  48.50
Dom Quixote                         Miguel de Cervantes       79.90
A Metamorfose                       Franz Kafka               29.90
O Processo                          Franz Kafka               45.90
A Casa dos Espíritos                Isabel Allende            51.90
Paula                               Isabel Allende            46.50
Ensaio sobre a Cegueira             José Saramago             58.90
O Evangelho Segundo Jesus Cristo    José Saramago             55.00
```

### Consulta 5 — `GROUP BY` e `AVG`

```sql
SELECT a.nome AS autor, AVG(l.preco) AS preco_medio
FROM autores a
JOIN livros l ON a.id = l.autor_id
GROUP BY a.id, a.nome;
```

```text
autor                     preco_medio
Machado de Assis          42.266667
Clarice Lispector         34.633333
Gabriel García Márquez    53.900000
Jane Austen               32.700000
Fiódor Dostoiévski        62.400000
Virginia Woolf            44.750000
Jorge Amado               41.900000
Toni Morrison             44.900000
Haruki Murakami           58.450000
Chimamanda Ngozi Adichie  52.700000
Miguel de Cervantes       79.900000
Franz Kafka               37.900000
Isabel Allende            49.200000
José Saramago             56.950000
```

### Consulta 6 — subconsulta com média geral

```sql
SELECT *
FROM livros
WHERE preco > (SELECT AVG(preco) FROM livros);
```

```text
id  titulo                              ano_publicacao  preco   autor_id
4   Cem Anos de Solidão                 1967            59.90   3
6   Crime e Castigo                     1866            54.90   5
7   Os Irmãos Karamázov                 1880            69.90   5
12  Amada                               1987            49.90   8
14  Norwegian Wood                      1987            52.00   9
15  Kafka à Beira-Mar                   2002            64.90   9
16  Americanah                          2013            56.90   10
17  Meio Sol Amarelo                    2006            48.50   10
18  Dom Quixote                         1605            79.90   11
21  A Casa dos Espíritos                1982            51.90   13
23  Ensaio sobre a Cegueira             1995            58.90   14
24  O Evangelho Segundo Jesus Cristo    1991            55.00   14
28  O Amor nos Tempos do Cólera         1985            57.90   3
```

## 7. Estado final e reproducibilidade

Ao final, o ambiente principal permaneceu em execução com:

```text
NAMES             STATUS              PORTS
lab-cloudbeaver   Up                  0.0.0.0:8978->8978/tcp
lab-mariadb       Up                  0.0.0.0:3306->3306/tcp
```

Contagens finais após a segunda execução do `setup.sql`:

```text
tabela       total
autores      14
livros       30
emprestimos  3
```

Para reproduzir o ambiente:

```bash
cd tarefa03
cp .env.example .env       # no Windows: copy .env.example .env
# editar .env e definir MARIADB_ROOT_PASSWORD
docker compose config
docker compose up -d
docker ps
```

Para executar o `setup.sql` via cliente dentro do contêiner:

```bash
docker cp setup.sql lab-mariadb:/tmp/setup.sql
docker exec -e MYSQL_PWD="$MARIADB_ROOT_PASSWORD" lab-mariadb \
  mariadb -uroot --default-character-set=utf8mb4 -e "source /tmp/setup.sql"
```

No CloudBeaver, a conexão com o MariaDB deve usar:

- **Host:** `mariadb`
- **Porta:** `3306`
- **Banco:** `labdb` ou `biblioteca`
- **Usuário:** `root`
- **Senha:** a definida em `MARIADB_ROOT_PASSWORD` no `.env`

O host **não** deve ser `localhost`, pois `localhost` dentro do contêiner do CloudBeaver aponta para o próprio CloudBeaver, onde não há SGBD escutando. O nome `mariadb` é resolvido pela rede interna criada pelo Docker Compose.

## 8. Referências

- Tarefa oficial: [tarefa-docker-sgbd.md](https://github.com/tacianosilva/bsi-tasks/blob/main/database/tarefas/tarefa-docker-sgbd.md)
- Issue da entrega: [tacianosilva/bsi-tasks#558](https://github.com/tacianosilva/bsi-tasks/issues/558)
- Repositório pessoal: [Jose-Samuel-Lima/Banco-de-Dados](https://github.com/Jose-Samuel-Lima/Banco-de-Dados)
- Docker Docs — Compose file reference: [https://docs.docker.com/compose/compose-file/](https://docs.docker.com/compose/compose-file/)
- MariaDB Docs — GRANT: [https://mariadb.com/kb/en/grant/](https://mariadb.com/kb/en/grant/)
- MariaDB Docs — Foreign Keys: [https://mariadb.com/kb/en/foreign-keys/](https://mariadb.com/kb/en/foreign-keys/)
- CloudBeaver Docs — Run Docker Container: [https://cloudbeaver.io/docs/Run-Docker-Container/](https://cloudbeaver.io/docs/Run-Docker-Container/)
