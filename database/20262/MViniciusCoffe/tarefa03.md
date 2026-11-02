# Tarefa 03 - Docker Compose, MariaDB e Administração de SGBD

## 1. Identificação e Repositório

- **Nome:** Marcus Vinícius de Souza Azevedo
- **Usuário GitHub:** [@MViniciusCoffe](https://github.com/MViniciusCoffe)
- **E-mail acadêmico:** vinicius.azevedo.123@ufrn.edu.br
- **Repositório pessoal:** [https://github.com/ufrn-marcus-sa/tarefas-bd](https://github.com/ufrn-marcus-sa/tarefas-bd#tarefa-03---docker-compose-mariadb-e-administração-de-sgbd), pasta `tarefa03/` (`docker-compose.yml`, `.env.example`, `povoamento.sql`, `setup.sql`) e `.gitignore` na raiz do repositório (ignora o `.env`)

### Ambiente utilizado

```text
$ docker --version            -> Docker 29.9.2
$ docker compose version      -> Docker Compose version 5.6.1
$ git check-ignore -v tarefa03/.env   # executado na raiz do repositório
.gitignore:1:.env	tarefa03/.env
```

```text
$ docker compose up -d
 Container lab-mariadb Started
 Container lab-cloudbeaver Started
```

Executei os scripts SQL pelo cliente `mariadb` (com `docker exec` no contêiner `lab-mariadb`), o que me permitiu copiar as saídas exatas. Os mesmos comandos podem ser executados no editor SQL do CloudBeaver (http://localhost:8978, host `mariadb`, porta `3306`). Rodei os testes com usuários restritos a partir de um contêiner na mesma rede do Compose (`--network tarefa03_default -h mariadb`), assim como o CloudBeaver se conecta. Por isso o host que aparece nos erros é um IP da rede Docker (`172.19.0.4`).

---

## 2. Respostas às Perguntas Discursivas

### Pergunta Discursiva 1 - DDL x DML

Criar uma tabela (DDL) é definir a **estrutura**: o nome da tabela, as colunas, os tipos e as regras (PK, FK, NOT NULL). Nenhum dado é guardado nesse momento, é como montar uma estante vazia. Inserir registros (DML, com `INSERT`) é colocar **conteúdo** dentro dessa estrutura já existente, e o `SELECT`, `UPDATE` e `DELETE` lidam com esse conteúdo sem mudar a estrutura.

Ao executar `DROP TABLE`, a estrutura e **todos os dados dentro dela são apagados de forma definitiva**. Não existe "lixeira": só é possível recuperar com um backup. No MariaDB o `DROP` também faz um commit implícito, então não dá para desfazer com `ROLLBACK`. Além disso, se outra tabela tiver uma FK apontando para ela (como `livros` -> `autores`), o SGBD recusa o `DROP` enquanto essa dependência existir.

### Pergunta Discursiva 2 - Erro 1142 e menor privilégio

Ao executar `DROP TABLE autores` com a conta `app_biblioteca`, o MariaDB recusou o comando:

```text
ERROR 1142 (42000): DROP command denied to user 'app_biblioteca'@'172.19.0.4' for table `biblioteca`.`autores`
```

O erro 1142 significa que o usuário não tem o privilégio necessário para aquele comando naquele objeto. O `SHOW GRANTS` mostra que `app_biblioteca` só recebeu `SELECT, INSERT, UPDATE, DELETE ON biblioteca.*`, ou seja, só operações DML. O privilégio `DROP` (DDL) nunca foi concedido, então o servidor bloqueia o comando antes de executá-lo.

Esse é o princípio do menor privilégio: a aplicação tem apenas o que precisa para funcionar. Se a aplicação sofrer uma invasão (por exemplo, SQL Injection) ou tiver um bug que monte um comando errado, o estrago fica limitado ao que a conta pode fazer. O atacante não consegue apagar tabelas, mudar a estrutura, criar usuários nem acessar outros bancos. O esquema do banco continua íntegro e o dano fica restrito aos dados, que podem ser restaurados de backup.

### Pergunta Discursiva 3 - Host `'%'` x `'localhost'`

No MariaDB uma conta é o par `'usuario'@'host'`, e o host é a **origem da conexão**. `'localhost'` só aceita conexões feitas de dentro do próprio servidor (socket UNIX/loopback do contêiner `lab-mariadb`).

O Docker Compose cria uma rede virtual (`tarefa03_default`) e cada contêiner recebe um IP próprio nela. Quando o CloudBeaver (outro contêiner) conecta no host `mariadb`, o MariaDB vê a conexão vindo de um IP da rede Docker, como `172.19.0.4`, e não de `localhost`. Uma conta `'app_biblioteca'@'localhost'` seria recusada. O curinga `'%'` aceita qualquer origem e é por isso que funciona entre contêineres. Esses IPs são dinâmicos e podem mudar a cada `up`, por isso fixar um IP específico não seria prático.

Vi essa diferença na prática: rodando o `DROP` por `docker exec` (socket local) o erro mostrou `'app_biblioteca'@'localhost'`, e rodando pela rede Docker mostrou `'app_biblioteca'@'172.19.0.4'`. Em produção o ideal seria restringir mais, por exemplo `'app'@'172.19.0.%'`, e não publicar a porta 3306 para fora.

### Pergunta Discursiva 4 - Povoamento com IA e integridade referencial

Gerei a carga expandida com IA generativa (Claude), salva em `povoamento.sql`: **10 autores e 27 livros novos**, incluindo livros para os autores 1 a 4. Depois da execução a base ficou com:

```text
+---------+      +--------+
| autores |      | livros |
+---------+      +--------+
|      14 |      |     32 |
+---------+      +--------+
```

Ao tentar inserir um livro com `autor_id = 999`:

```sql
INSERT INTO livros (titulo, ano_publicacao, preco, autor_id) VALUES ('Fantasma', 2000, 10.00, 999);
```

```text
ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails
(`biblioteca`.`livros`, CONSTRAINT `livros_ibfk_1` FOREIGN KEY (`autor_id`) REFERENCES `autores` (`id`))
```

Quem impede é a **restrição de chave estrangeira** (`FOREIGN KEY (autor_id) REFERENCES autores(id)`), que garante a **integridade referencial**: todo `autor_id` em `livros` precisa existir em `autores.id`. Isso evita "livros órfãos" apontando para autores inexistentes.

### Pergunta Discursiva 5 - Vantagem de separar `autores` e `livros`

Na Consulta 4 o `JOIN` junta as duas tabelas pela chave e mostra o nome do autor ao lado de cada livro. Na Consulta 5 o `GROUP BY a.id` agrupa os livros de cada autor para calcular a média de preço. As duas funcionam porque cada autor está cadastrado **uma única vez** e os livros só guardam o `autor_id`.

Vantagens práticas dessa separação (normalização):

- **Sem repetição:** "Machado de Assis, Brasil, 1839" fica escrito uma vez, e não em cada um dos 3 livros dele.
- **Atualização em um lugar só:** para corrigir o país de um autor basta um `UPDATE` em uma linha. Com dados duplicados seria fácil esquecer alguma linha e deixar a base inconsistente.
- **Agrupamentos confiáveis:** o agrupamento é feito pelo `id`. Se o nome fosse texto repetido, um erro de digitação ("Machado de Assiz") criaria um "autor" a mais na Consulta 5.
- **Menos espaço** ocupado e possibilidade de cadastrar um autor mesmo antes de ele ter livros.

---

## 3. Respostas Dissertativas Conceituais

### Questão a - Por que a aplicação nunca deve usar `root`?

O `root` tem **todos os privilégios em todo o servidor**: criar e apagar qualquer banco, criar usuários, ler tabelas de sistema, alterar senhas e, dependendo da configuração, ler e escrever arquivos no servidor (`FILE`). Uma aplicação não precisa de nada disso.

Se as credenciais da aplicação vazarem (código público, log, SQL Injection) e ela usar `root`, o atacante passa a controlar o SGBD inteiro. Ele pode apagar todos os bancos (`DROP DATABASE`), roubar dados de outras aplicações no mesmo servidor, criar uma conta de backdoor para manter acesso, trocar a senha do root e deixar os administradores sem acesso, ou cifrar e apagar dados para pedir resgate. Com uma conta restrita como `app_biblioteca`, o vazamento ainda é grave, mas fica limitado ao DML do banco `biblioteca`.

### Questão b - Privilégios DDL x DML

- **DDL** (`CREATE`, `ALTER`, `DROP`, `INDEX`...) altera a **estrutura** do banco: tabelas, colunas, índices, restrições.
- **DML** (`SELECT`, `INSERT`, `UPDATE`, `DELETE`) manipula os **dados** dentro dessa estrutura.

A aplicação no dia a dia só precisa de DML. A estrutura só muda em migrações planejadas, feitas por um administrador ou um processo de deploy. Separar em contas diferentes (uma "dona do esquema" usada só nas migrações e uma de aplicação só com DML) reduz a superfície de ataque, impede que um bug ou invasão destrua o esquema, deixa claro quem pode mudar o quê e facilita a auditoria. Também dá para ter contas ainda mais restritas, como `consulta` (só `SELECT`) e `relatorios` (só `SELECT` em uma tabela).

### Questão c - `.env.example` versionado x `.env` ignorado

O `.env.example` é a **documentação do contrato de configuração**. Ele mostra quais variáveis o projeto precisa (`MARIADB_ROOT_PASSWORD`, `MARIADB_PORT`...) com valores fictícios, para que qualquer pessoa que clonar o repositório saiba o que preencher. Como não contém segredos, pode ficar público.

O `.env` tem os **valores reais**, que são da máquina de cada um e nunca devem ir para o Git. Os riscos de commitar credenciais em um repositório público:

- Robôs varrem o GitHub o tempo todo atrás de senhas e chaves, e uma credencial vazada pode ser explorada em minutos.
- Apagar o arquivo em um commit seguinte **não resolve**: a senha continua no histórico do Git e em forks e clones já feitos. A única correção real é **trocar (rotacionar) a credencial** e, se possível, reescrever o histórico.
- As consequências vão de vazamento e perda de dados até custos financeiros (chaves de nuvem usadas para mineração ou perda de dados importantes) e problemas legais (LGPD).

### Questão d - `.env` + `.gitignore` eliminam todos os riscos?

**Não.** O `.gitignore` só protege contra **um** risco: enviar o arquivo para o repositório. O `.env` continua em **texto puro** no disco, então:

- Qualquer pessoa ou processo com acesso de leitura ao servidor (outro usuário, um backup, uma falha de path traversal na aplicação) consegue ler a senha.
- A senha também aparece em outros lugares. Vi isso nesta tarefa: `docker compose config` imprime `MARIADB_ROOT_PASSWORD: RootLab2026!aB` e `docker exec lab-mariadb printenv MARIADB_ROOT_PASSWORD` mostra a senha dentro do contêiner. `docker inspect` também mostra as variáveis de ambiente.
- O arquivo pode ir parar em backups, imagens Docker (se copiado no `Dockerfile`), prints ou mensagens.

Em produção usam-se medidas adicionais: permissões restritas no arquivo (`chmod 600`), gerenciadores de segredos (Docker Secrets, HashiCorp Vault, AWS Secrets Manager), rotação periódica de senhas, menor privilégio para cada conta e não expor a porta do banco para fora da rede interna. O `.env` é uma boa prática de desenvolvimento, não uma solução completa de segurança.

### Questão e - O que é um contêiner e vantagens do Docker no ensino

Um **contêiner** é um processo isolado que roda com seu próprio sistema de arquivos, rede e processos, empacotado a partir de uma **imagem** com tudo o que o software precisa (binários, bibliotecas, configuração). Diferente de uma máquina virtual, ele compartilha o kernel do sistema host, por isso é leve e sobe em segundos.

#### Como o isolamento funciona por dentro

Um contêiner não é uma "mini máquina". Ele é um **processo comum do Linux** que o kernel isola usando três recursos principais: **namespaces**, **cgroups** e um **sistema de arquivos em camadas**. O Docker (via `containerd` e `runc`) só configura esses recursos e inicia o processo.

**1. Namespaces: o que o processo consegue ver**

Cada namespace dá ao processo uma visão própria de um recurso do sistema:

| Namespace | Isola                          | Efeito no `lab-mariadb`                                                                                                      |
| --------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| `pid`     | árvore de processos            | o `mariadbd` é o PID 1 lá dentro e não enxerga os processos do host                                                          |
| `net`     | interfaces, IPs, portas, rotas | tem a própria interface `eth0` na rede `tarefa03_default` (IP `172.19.0.2`) e a própria porta 3306                           |
| `mnt`     | pontos de montagem             | vê o sistema de arquivos da imagem (Ubuntu), não o do host                                                                   |
| `uts`     | hostname                       | tem o hostname próprio (o ID do contêiner)                                                                                   |
| `ipc`     | memória compartilhada e filas  | não compartilha IPC com processos do host                                                                                    |
| `user`    | IDs de usuário e grupo         | permite mapear o root do contêiner para um usuário sem privilégios no host (*rootless*/`userns-remap`, não ativo por padrão) |
| `cgroup`  | visão da hierarquia de cgroups | o contêiner vê o próprio cgroup como raiz (`/`)                                                                              |

**2. cgroups: quanto o processo pode usar**

Os *control groups* limitam e contabilizam CPU, memória, I/O e número de processos. O Docker cria um cgroup para cada contêiner, e opções como `--memory` e `--cpus` (ou `deploy.resources` no Compose) viram limites nesse cgroup. Assim um contêiner não consegue consumir toda a máquina e derrubar os outros.

**3. Sistema de arquivos em camadas (OverlayFS) e volumes**

A imagem `mariadb:11` é formada por **camadas somente leitura** empilhadas. Ao criar o contêiner, o Docker adiciona por cima uma **camada gravável** usando OverlayFS. Essa camada é descartada quando o contêiner é removido, e é por isso que o banco precisa do volume `mariadb_data` montado em `/var/lib/mysql`: o volume fica fora dessa camada e sobrevive ao `docker compose down`.

Somam-se a isso a rede virtual (uma *bridge* com DNS interno, que faz o nome `mariadb` resolver para o IP do contêiner) e mecanismos de segurança como *capabilities* reduzidas e perfis seccomp, que restringem as chamadas de sistema permitidas.

**Evidências no meu ambiente**

```text
# Mesmo kernel no host e no contêiner (compartilhado)
$ uname -r                                  -> 7.2.11-arch1-1
$ docker exec lab-mariadb uname -r          -> 7.2.11-arch1-1

# Distribuições diferentes (namespace mnt + imagem)
host:       NAME="Arch Linux"
contêiner:  PRETTY_NAME="Ubuntu 24.04.5 LTS"

# Namespace pid: o mesmo processo tem PIDs diferentes
$ docker inspect -f '{{.State.Pid}}' lab-mariadb      -> 215992   (visto pelo host)
$ docker exec lab-mariadb cat /proc/1/comm            -> mariadbd (é o PID 1 lá dentro)
$ docker exec lab-mariadb ls /proc  (só PIDs)          -> 1 124 130 131 132

# Namespace uts: hostname próprio
$ docker exec lab-mariadb hostname                    -> 9785b4ca05af

# Namespace net: IP próprio na rede do Compose
$ docker inspect ... lab-mariadb                      -> 172.19.0.2

# cgroup: o host vê o contêiner num scope próprio do systemd,
# enquanto o contêiner enxerga a si mesmo como raiz
host:       0::/system.slice/docker-9785b4ca05af....scope
contêiner:  0::/

# Driver do sistema de arquivos
$ docker inspect -f '{{.Driver}}' lab-mariadb         -> overlayfs

# No host é só mais um processo, rodando com o UID 999 (usuário mysql da imagem)
$ ps -o pid,user,comm -p 215992
    PID USER     COMMAND
 215992 999      mariadbd
```

Essas saídas mostram a diferença em relação a uma VM: não existe um segundo kernel. O `mariadbd` roda direto no kernel do meu Arch Linux, mas acredita estar sozinho em um Ubuntu, com PID 1, hostname e IP próprios.

Vantagens em relação a instalar o SGBD direto no computador do aluno:

- **Ambiente idêntico para todos:** `mariadb:11` é a mesma versão no Linux, Windows ou macOS, sem o problema do "na minha máquina funciona".
- **Instalação e remoção rápidas e limpas:** `docker compose up -d` sobe tudo e `docker compose down -v` remove sem deixar resíduos no sistema.
- **Infraestrutura como código:** o `docker-compose.yml` documenta e versiona o ambiente.
- **Isolamento:** não conflita com outro MySQL instalado. Basta trocar a porta (fiz isso no Desafio 1 e no 2, com dois ambientes em paralelo).
- **Recomeçar do zero é fácil**, o que ajuda a experimentar e errar sem medo.
- **Proximidade com o mercado**, onde contêineres são padrão em desenvolvimento e deploy.

---

## 4. Desafios Realizados

### Bloco A - Docker e Infraestrutura

#### Desafio 1 - Porta 3307

```bash
sed -i 's/^MARIADB_PORT=.*/MARIADB_PORT=3307/' .env
docker compose up -d        # recria apenas o lab-mariadb
docker ps --format '{{.Names}}\t{{.Ports}}'
```

```text
lab-mariadb	0.0.0.0:3307->3306/tcp, [::]:3307->3306/tcp
lab-cloudbeaver	0.0.0.0:8978->8978/tcp, [::]:8978->8978/tcp
```

**Reconfiguração do CloudBeaver:** na conexão do CloudBeaver **nada precisou mudar**. Host continuou `mariadb` e porta continuou `3306`. O mapeamento `"${MARIADB_PORT}:3306"` só altera a porta **publicada no host** (lado esquerdo). Dentro da rede Docker o MariaDB continua escutando em `3306`, e é por essa rede que o CloudBeaver se conecta. Só clientes rodando **fora** do Docker, na minha máquina (DBeaver desktop, `mariadb -h 127.0.0.1`), passariam a usar `localhost:3307`. Como os dados estão no volume, nada foi perdido na recriação do contêiner.

#### Desafio 2 - Dois ambientes simultâneos

Criei uma segunda pasta `tarefa03-amb2/` com cópia do compose alterando `container_name` e o nome do volume, e um `.env` com outras portas:

```yaml
# tarefa03-amb2/docker-compose.yml (trechos alterados)
    container_name: lab2-mariadb
      - mariadb_data2:/var/lib/mysql
    container_name: lab2-cloudbeaver
volumes:
  mariadb_data2:
```

```text
# tarefa03-amb2/.env
MARIADB_ROOT_PASSWORD=Amb2Lab2026!xY
MARIADB_DATABASE=labdb
MARIADB_PORT=3308
CLOUDBEAVER_PORT=8979
```

```text
$ docker ps --format '{{.Names}}\t{{.Ports}}'
lab2-cloudbeaver	0.0.0.0:8979->8978/tcp, [::]:8979->8978/tcp
lab2-mariadb	0.0.0.0:3308->3306/tcp, [::]:3308->3306/tcp
lab-mariadb	0.0.0.0:3307->3306/tcp, [::]:3307->3306/tcp
lab-cloudbeaver	0.0.0.0:8978->8978/tcp, [::]:8978->8978/tcp
```

Quatro contêineres rodaram em paralelo sem conflito porque:

- **Portas do host diferentes** (3307/8978 e 3308/8979). As portas internas (3306/8978) podem se repetir, já que cada contêiner tem sua própria interface de rede.
- **`container_name` diferentes**, porque o nome de contêiner é único no Docker host e repeti-lo daria erro de conflito.
- **Nome do projeto diferente:** o Compose usa o nome da pasta como projeto (`tarefa03` e `tarefa03-amb2`), então redes (`tarefa03_default` e `tarefa03-amb2_default`) e volumes ficam separados. Renomeei também o volume para `mariadb_data2` para deixar isso explícito.

Ao final removi o segundo ambiente com `docker compose down -v` dentro de `tarefa03-amb2/`.

#### Desafio 3 - Persistência do volume e senha de root

```bash
sed -i 's/^MARIADB_ROOT_PASSWORD=.*/MARIADB_ROOT_PASSWORD=NovaSenha2026!zZ/' .env
docker compose up -d
docker exec lab-mariadb printenv MARIADB_ROOT_PASSWORD
docker exec lab-mariadb mariadb -uroot -p'RootLab2026!aB' -e 'select "senha antiga OK"'
docker exec lab-mariadb mariadb -uroot -p'NovaSenha2026!zZ' -e 'select 1'
```

```text
NovaSenha2026!zZ
senha antiga OK
ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)
```

O contêiner recebeu a variável nova, mas a **senha antiga continua válida e a nova falha**. A variável `MARIADB_ROOT_PASSWORD` só é usada pelo script de entrypoint da imagem na **primeira inicialização**, quando `/var/lib/mysql` está vazio. Nessa hora ele cria as tabelas de sistema e grava o hash da senha em `mysql.global_priv`, **dentro do volume**. Nas subidas seguintes o entrypoint vê que o diretório de dados já existe, pula a inicialização e o servidor usa o hash que já está gravado. A variável passa a ser ignorada.

Dois caminhos para aplicar uma nova senha:

1. **Alterar a senha pelo SQL, mantendo os dados:** conectado com a senha atual, executar
   `ALTER USER 'root'@'%' IDENTIFIED BY 'NovaSenha2026!zZ'; ALTER USER 'root'@'localhost' IDENTIFIED BY 'NovaSenha2026!zZ';`
   e depois atualizar o `.env` para ficar coerente.
2. **Destruir e recriar o volume:** `docker compose down -v` seguido de `docker compose up -d`. O entrypoint inicializa tudo de novo com a senha do `.env`, mas **todos os dados são perdidos** (aqui eles podem ser recriados com o `setup.sql`).

Depois do teste voltei o `.env` para a senha original.

#### Desafio 4 - Validação estrita `:?`

```bash
mv .env .env.bak
docker compose up -d
```

```text
error while interpolating services.mariadb.environment.MARIADB_ROOT_PASSWORD: required variable MARIADB_ROOT_PASSWORD is missing a value: defina MARIADB_ROOT_PASSWORD no arquivo .env
```

O Compose **abortou antes de criar qualquer contêiner** e mostrou a mensagem definida no `${MARIADB_ROOT_PASSWORD:?...}`. Em ambientes profissionais isso é importante porque a falha acontece **cedo e de forma clara** (fail fast). Sem o `:?` a variável viraria uma string vazia e o problema só apareceria depois: o contêiner do MariaDB entraria em `Exited (1)`, ou, pior, alguém poderia "resolver" usando `MARIADB_ALLOW_EMPTY_ROOT_PASSWORD` e subir um banco sem senha. O `:?` deixa explícito que a variável é obrigatória e serve também como documentação do que precisa estar no `.env`. Restaurei com `mv .env.bak .env`.

#### Desafio 5 - `docker compose config`

```text
$ docker compose config | grep -E 'MARIADB_|published'
        published: "8978"
      MARIADB_DATABASE: labdb
      MARIADB_ROOT_PASSWORD: RootLab2026!aB
        published: "3307"
```

Três variáveis resolvidas a partir do `.env`:

1. `MARIADB_ROOT_PASSWORD` -> `RootLab2026!aB` (interpolada em `environment`)
2. `MARIADB_DATABASE` -> `labdb` (interpolada em `environment`)
3. `MARIADB_PORT` -> `3307` (interpolada no `published` da porta do MariaDB). Também foi resolvida `CLOUDBEAVER_PORT` -> `8978`.

Isso também mostra o ponto da Questão d: o `config` imprime a senha em texto puro.

### Bloco B - Modelagem e Consultas SQL

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

No MariaDB `BOOLEAN` é sinônimo de `TINYINT(1)` (`FALSE` = 0, `TRUE` = 1).

#### Desafio 7 - Carga de empréstimos

```sql
INSERT INTO emprestimos (livro_id, data_emprestimo, devolvido) VALUES
(1,  '2026-10-05', FALSE),   -- Dom Casmurro (pendente)
(8,  '2026-10-12', FALSE),   -- O Amor nos Tempos do Cólera (pendente)
(13, '2026-09-20', TRUE);    -- Os Irmãos Karamázov (devolvido)
```

#### Desafio 8 - Empréstimos pendentes

```sql
SELECT l.titulo, e.data_emprestimo, a.nome AS autor
FROM emprestimos e
JOIN livros l  ON e.livro_id = l.id
JOIN autores a ON l.autor_id = a.id
WHERE e.devolvido = FALSE;
```

```text
+------------------------------+-----------------+--------------------------+
| titulo                       | data_emprestimo | autor                    |
+------------------------------+-----------------+--------------------------+
| Dom Casmurro                 | 2026-10-05      | Machado de Assis         |
| O Amor nos Tempos do Cólera  | 2026-10-12      | Gabriel García Márquez   |
+------------------------------+-----------------+--------------------------+
```

#### Desafio 9 - `HAVING`

```sql
SELECT a.nome AS autor, COUNT(*) AS total_livros
FROM autores a
JOIN livros l ON a.id = l.autor_id
GROUP BY a.id, a.nome
HAVING COUNT(*) > 1;
```

```text
+--------------------------+--------------+
| autor                    | total_livros |
+--------------------------+--------------+
| Machado de Assis         |            3 |
| Clarice Lispector        |            2 |
| Gabriel García Márquez   |            2 |
| Jane Austen              |            2 |
| Fiódor Dostoiévski       |            3 |
| George Orwell            |            2 |
| José Saramago            |            3 |
| Jorge Amado              |            3 |
| Franz Kafka              |            2 |
| Chimamanda Ngozi Adichie |            2 |
| Haruki Murakami          |            2 |
| Victor Hugo              |            2 |
| Toni Morrison            |            2 |
| Graciliano Ramos         |            2 |
+--------------------------+--------------+
```

Os 14 autores aparecem porque o povoamento deu pelo menos 2 livros a cada um. O `WHERE` filtra linhas antes de agrupar, e o `HAVING` filtra os grupos depois do `COUNT(*)`.

#### Desafio 10 - `UPDATE` de +10%

```sql
SELECT id, titulo, preco FROM livros WHERE id = 1;   -- 39.90
UPDATE livros SET preco = ROUND(preco * 1.10, 2) WHERE id = 1;
SELECT id, titulo, preco FROM livros WHERE id = 1;   -- 43.89
```

```text
| 1 | Dom Casmurro | 39.90 |   ->   | 1 | Dom Casmurro | 43.89 |
```

O preço de *Dom Casmurro* passou de R$ 39,90 para R$ 43,89 (39,90 x 1,10). Usei o `WHERE id = 1` para atingir um único livro, porque um `UPDATE` sem `WHERE` reajustaria a tabela inteira. O `ROUND(..., 2)` mantém as duas casas do `DECIMAL(10,2)`.

#### Desafio 11 - `DELETE` de autor sem livros

```sql
INSERT INTO autores (nome, pais, ano_nascimento) VALUES ('Autor Temporário', 'Brasil', 1990);
SELECT id, nome FROM autores WHERE nome = 'Autor Temporário';   -- id 15
DELETE FROM autores WHERE nome = 'Autor Temporário';
SELECT ROW_COUNT() AS linhas_removidas;                         -- 1
```

A remoção foi aceita porque **nenhuma linha de `livros` referenciava o `id` 15**. A FK `livros.autor_id -> autores.id` só impede apagar um autor (linha "pai") que ainda tem livros (linhas "filhas") apontando para ele. Esse caso daria `ERROR 1451 ... a foreign key constraint fails`, pois sem `ON DELETE CASCADE` o padrão é `RESTRICT`. Como o autor não tinha livros, a exclusão não deixou nenhuma referência órfã.

### Bloco C - Administração e Privilégios

#### Desafio 12 - Usuário `relatorios`

```sql
CREATE USER 'relatorios'@'%' IDENTIFIED BY 'Relatorios2026!';
GRANT SELECT ON biblioteca.livros TO 'relatorios'@'%';
SHOW GRANTS FOR 'relatorios'@'%';
```

```text
GRANT USAGE ON *.* TO `relatorios`@`%` IDENTIFIED BY PASSWORD '*83EE...'
GRANT SELECT ON `biblioteca`.`livros` TO `relatorios`@`%`
```

O privilégio é **no nível da tabela** (`biblioteca.livros`), e não do banco todo (`biblioteca.*`).

#### Desafio 13 - Restrição de visibilidade

```text
relatorios> SELECT COUNT(*) FROM livros;
32

relatorios> SELECT * FROM autores;
ERROR 1142 (42000): SELECT command denied to user 'relatorios'@'172.19.0.4' for table `biblioteca`.`autores`
```

A consulta em `livros` funciona, mas em `autores` o SGBD retorna o erro 1142 porque `relatorios` só tem `SELECT` em `biblioteca.livros`. O MariaDB confere os privilégios em ordem (global, banco, tabela, coluna) e não encontrou nenhum que cubra `autores`. O usuário também não vê a tabela `autores` em `SHOW TABLES`. Na prática ele também não conseguiria fazer o `JOIN` da Consulta 4.

#### Desafio 14 - `GRANT` e `REVOKE` dinâmicos

```sql
-- como root
GRANT INSERT ON biblioteca.livros TO 'relatorios'@'%';
```

```text
relatorios> INSERT INTO livros (titulo, ano_publicacao, preco, autor_id) VALUES ('Angústia', 1936, 41.90, 14);
relatorios> SELECT ROW_COUNT();
1
```

```sql
-- como root
REVOKE INSERT ON biblioteca.livros FROM 'relatorios'@'%';
SHOW GRANTS FOR 'relatorios'@'%';   -- voltou a ter apenas SELECT ON biblioteca.livros
```

```text
relatorios> INSERT INTO livros (titulo, ano_publicacao, preco, autor_id) VALUES ('Infância', 1945, 33.90, 14);
ERROR 1142 (42000): INSERT command denied to user 'relatorios'@'172.19.0.4' for table `biblioteca`.`livros`
```

Com o `GRANT` a inserção funcionou. Depois do `REVOKE`, a mesma operação passou a ser recusada com o erro 1142, enquanto o `SELECT` continuou funcionando. A mudança valeu na hora, sem `FLUSH PRIVILEGES` e sem reiniciar nada, porque `GRANT` e `REVOKE` atualizam diretamente as tabelas de privilégio em memória. Com isso dá para dar uma permissão temporária para uma tarefa e retirá-la logo depois.

#### Desafio 15 - `setup.sql` idempotente

O arquivo [`setup.sql`](https://github.com/ufrn-marcus-sa/tarefas-bd/blob/main/tarefa03/setup.sql) está versionado no repositório pessoal. O que garante a idempotência:

- `DROP DATABASE IF EXISTS biblioteca;` seguido de `CREATE DATABASE`: o banco sempre começa vazio, então as inserções não duplicam e os `AUTO_INCREMENT` voltam a 1 (os `autor_id` dos livros continuam corretos).
- `DROP USER IF EXISTS ...` antes de cada `CREATE USER`: recria `app_biblioteca`, `consulta` e `relatorios` com os privilégios corretos, sem erro de "usuário já existe".
- Recria `autores`, `livros` e `emprestimos` com PKs e FKs, e carrega a carga mínima, o `povoamento.sql` e os empréstimos.

Teste: executei o script **duas vezes seguidas** e as contagens foram as mesmas:

```bash
docker exec -i lab-mariadb mariadb -uroot -p'RootLab2026!aB' < setup.sql
docker exec -i lab-mariadb mariadb -uroot -p'RootLab2026!aB' < setup.sql
```

```text
+---------+--------+-------------+
| autores | livros | emprestimos |
+---------+--------+-------------+
|      14 |     32 |           3 |
+---------+--------+-------------+
+----------------+------+
| User           | Host |
+----------------+------+
| app_biblioteca | %    |
| consulta       | %    |
| relatorios     | %    |
+----------------+------+
```
