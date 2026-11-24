# Tarefa 03 — Docker Compose, MariaDB e Administração de SGBD

## 1. Identificação e Repositório

- **Discente:** Jefferson Willame Sena de Medeiros
- **GitHub:** [JefWill](https://github.com/JefWill)
- **E-mail acadêmico:** Jefferson.willame.712@ufrn.edu.br
- **Disciplina:** DCT2201 — Banco de Dados, Sistemas de Informação — CERES/UFRN.
- **Repositório pessoal público e README:** [dct2201-banco-de-dados](https://github.com/JefWill/dct2201-banco-de-dados/blob/main/README.md).
- **Arquivos:** [docker-compose.yml](https://github.com/JefWill/dct2201-banco-de-dados/blob/main/tarefa03/docker-compose.yml), [.env.example](https://github.com/JefWill/dct2201-banco-de-dados/blob/main/tarefa03/.env.example), [.gitignore](https://github.com/JefWill/dct2201-banco-de-dados/blob/main/.gitignore), [povoamento.sql](https://github.com/JefWill/dct2201-banco-de-dados/blob/main/tarefa03/povoamento.sql) e [setup.sql](https://github.com/JefWill/dct2201-banco-de-dados/blob/main/tarefa03/setup.sql).

As cinco respostas dos passos práticos foram elaboradas pelo discente. O povoamento expandido foi gerado com auxílio do ChatGPT. A organização do relatório, as respostas conceituais adicionais e os scripts dos desafios também contaram com assistência de IA e foram conferidos por execução no laboratório.

**Contexto das evidências:** em 02/11/2026, o banco original foi conferido com 14 autores e 35 livros. Para preservar esse trabalho, os desafios foram executados por terminal em dois projetos Compose separados, `tarefa03/ambiente1/` e `tarefa03/ambiente2/`. O primeiro recebeu uma cópia do banco original; o segundo foi usado para a demonstração da senha persistida e os testes de recriação. Os resultados abaixo correspondem a essas execuções, sem alegar que foram feitos pela interface do CloudBeaver. Os comandos SQL podem ser repetidos no editor SQL da interface com a conta indicada. Ao final, os contêineres de teste foram removidos com `down`, mantendo seus volumes; o laboratório original permaneceu em execução e sem alterações.

## 2. Respostas às Perguntas Discursivas dos Passos Práticos

### Pergunta Discursiva 1 — DDL, DML e exclusão de tabela

A diferença é que a DDL (linguagem de definição de dados) é usada para criar, alterar ou excluir tabelas, enquanto a DML (linguagem de manipulação de dados) é usada para inserir, atualizar ou excluir registros nessas tabelas. Se apagarmos uma tabela com `DROP TABLE`, sua estrutura e os dados que estavam dentro dela também serão apagados, desde que o comando seja aceito pelo banco.

### Pergunta Discursiva 2 — Erro 1142 e menor privilégio

O MariaDB recusou o comando porque o usuário `app_biblioteca` não possuía a permissão necessária. Essa restrição protege a estrutura do banco: se alguém conseguir acesso à aplicação, não terá permissão para excluir tabelas usando essa conta. O usuário possui `SELECT`, `INSERT`, `UPDATE` e `DELETE`, mas não `DROP`. Isso aplica o princípio do menor privilégio. Ainda existe risco de alteração ou exclusão de registros pelas permissões DML concedidas.

### Pergunta Discursiva 3 — Host de autenticação e rede Docker

Os usuários foram criados com o host `'%'` para aceitar conexões de outros hosts, incluindo os contêineres da rede interna do Docker. Esse curinga não se limita à rede Docker: ele corresponde a qualquer host que consiga alcançar o servidor. Já `'localhost'` restringe a origem à própria máquina ou contêiner do servidor. Como o CloudBeaver está em outro contêiner, ele se conecta pelo nome do serviço `mariadb` e chega com um endereço da rede Docker.

### Pergunta Discursiva 4 — Povoamento e integridade referencial

Ficaram cadastrados 14 autores e 35 livros: aos 4 autores e 5 livros iniciais foram acrescentados 10 autores e 30 livros de `povoamento.sql`. Ao inserir um livro com `autor_id = 999`, o MariaDB recusa a operação com erro 1452, pois a chave estrangeira `livros.autor_id` referencia `autores.id`, e o autor 999 não existe. Essa restrição garante a integridade referencial.

### Pergunta Discursiva 5 — Vantagens de separar autores e livros

A vantagem é evitar a repetição de dados, economizar espaço e manter as informações consistentes. O nome e o país do autor são armazenados uma única vez; uma correção é feita em um só registro. Cada livro guarda o identificador do autor, e o `JOIN` reúne as informações quando necessário. A relação também permite agrupar os livros por autor para calcular médias, como na Consulta 5.

## 3. Respostas Dissertativas Conceituais

### Questão a — Por que a aplicação não deve usar root

O usuário `root` tem poderes administrativos que uma aplicação comercial normalmente não precisa. Se suas credenciais vazarem, um invasor pode apagar bancos, modificar estruturas, acessar informações e administrar usuários e privilégios, conforme os poderes dessa conta. A aplicação deve usar uma conta própria, limitada às operações e tabelas de que necessita. Isso reduz os danos de um vazamento ou falha, embora não elimine os riscos sobre os dados acessíveis a ela.

### Questão b — Separação entre DDL e DML

DDL modifica a estrutura, por exemplo com `CREATE`, `ALTER` e `DROP`. DML manipula os registros, por exemplo com `INSERT`, `UPDATE` e `DELETE`; neste laboratório, as permissões de leitura com `SELECT` também integram a conta de uso dos dados. Separar as contas permite que a aplicação trabalhe com os registros sem receber poder para excluir ou alterar tabelas. Mudanças de estrutura ficam sob uma conta administrativa ou de migração, usada de forma controlada.

### Questão c — Versionamento de .env.example e .env

O `.env.example` documenta os nomes das variáveis e valores genéricos, permitindo que outra pessoa prepare o ambiente. O `.env` contém a configuração local e senhas reais, por isso deve ficar fora do Git. Publicar essas credenciais pode permitir acesso indevido e alterações ou exposição de dados. Apagar a linha em um commit posterior não remove o segredo do histórico nem das cópias já feitas; em caso de vazamento, a credencial deve ser revogada ou trocada e o histórico tratado quando necessário.

### Questão d — Limites de segurança do .env e .gitignore

Esses arquivos não eliminam todos os riscos. O `.gitignore` evita a inclusão automática de um arquivo ainda não rastreado, mas não protege um `.env` que já tenha sido commitado. Além disso, o arquivo continua em texto puro: alguém com acesso ao sistema de arquivos, a um backup ou a permissões administrativas pode lê-lo. É necessário restringir o acesso ao arquivo e ao servidor, controlar backups e logs, usar contas com menor privilégio e, em produção, considerar mecanismos próprios de gestão de segredos.

### Questão e — Contêineres e vantagens didáticas

Um contêiner executa processos com um sistema de arquivos e recursos isolados, normalmente compartilhando o kernel do ambiente Linux que o hospeda. No Docker Desktop com WSL 2, esse ambiente Linux é fornecido pelo WSL. Para as aulas, o Docker facilita usar a mesma versão do SGBD, reproduzir a configuração com Compose e evitar conflitos com instalações locais. Também permite experimentar redes, portas e persistência, além de criar e remover ambientes sem reinstalar o banco diretamente no Windows. Os dados só persistem após a remoção dos contêineres quando são armazenados adequadamente, como no volume nomeado do laboratório.

## 4. Desafios Realizados

### Bloco A — Docker e Infraestrutura de Ambiente

#### Desafio 1 — Porta do SGBD

No `.env` de `tarefa03/ambiente1/`, foi definido `MARIADB_PORT=3307`, substituindo o valor padrão 3306 do roteiro. O ambiente foi aplicado com:

```cmd
cd tarefa03\ambiente1
docker compose up -d
docker compose ps
```

O mapeamento observado foi `3307:3306`. No CloudBeaver desse ambiente, a configuração correta continua sendo **host `mariadb`, porta `3306`**: a comunicação ocorre diretamente pela rede interna. Portanto, não se deve mudar a porta dessa conexão para 3307. A porta 3307 seria usada por um cliente executado no Windows, com host `localhost`. O mapeamento e a separação das redes foram conferidos com a configuração resolvida e a inspeção dos contêineres; não foi necessário alterar a porta interna do MariaDB. O laboratório original permaneceu em `3306:3306`.

#### Desafio 2 — Dois ambientes simultâneos

Foram criadas duas pastas com os arquivos versionados no repositório pessoal:

| Pasta | Nome do projeto Compose | MariaDB no Windows | CloudBeaver no Windows | Volume |
|---|---|---|---|---|
| `tarefa03/ambiente1/` | `tarefa03-ambiente1` | 3307 | 8979 | `tarefa03-ambiente1_mariadb_data` |
| `tarefa03/ambiente2/` | `tarefa03-ambiente2` | 3308 | 8980 | `tarefa03-ambiente2_mariadb_data` |

```cmd
cd tarefa03\ambiente1
docker compose up -d
cd ..\ambiente2
docker compose up -d
docker ps
```

Os arquivos usam `name:` distinto e não fixam `container_name`. O Compose gera nomes próprios para cada projeto. Assim, quatro contêineres de teste rodaram em paralelo, com redes, volumes e portas separados. Os dois contêineres do laboratório original também permaneceram ativos, fora desses projetos. Dentro de cada rede o serviço continua se chamando `mariadb`, sem conflito entre os ambientes.

#### Desafio 3 — Senha de root e volume persistente

No ambiente 2, a senha do `.env` foi alterada temporariamente e o serviço reaplicado:

```cmd
cd tarefa03\ambiente2
notepad .env
docker compose up -d mariadb
docker compose exec mariadb mariadb --protocol=tcp -h127.0.0.1 -uroot -p
```

Foram feitas duas tentativas, com a senha anterior e com a nova, sem registrá-las no relatório. A anterior autenticou; a nova retornou:

```text
ERROR 1045 (28000): Access denied for user 'root'@'127.0.0.1' (using password: YES)
```

O volume já continha as tabelas internas de autenticação. A variável `MARIADB_ROOT_PASSWORD` é usada para inicializar um diretório de dados vazio, e não redefine a senha toda vez que o contêiner é recriado.

Há dois caminhos: entrar com uma conta administrativa e executar `ALTER USER` para a conta root apropriada, preservando os dados, ou remover o volume e inicializar novamente com o novo `.env`, perdendo os dados daquele volume. Para o primeiro caminho, a forma SQL é `ALTER USER 'root'@'%' IDENTIFIED BY '<nova_senha>';`, ajustando o host conforme a conta existente. Para um laboratório descartável, o segundo caminho seria `docker compose down -v` e depois `docker compose up -d`. Esses dois comandos de destruição/recriação são explicativos e não foram executados neste teste. Após a demonstração, o `.env` do ambiente 2 foi restaurado para a senha que continuava válida.

#### Desafio 4 — Validação estrita da variável obrigatória

A linha `MARIADB_ROOT_PASSWORD` foi retirada temporariamente apenas do `.env` do ambiente 2. Ao executar `docker compose up -d`, o Compose interrompeu a resolução da configuração antes de iniciar novos serviços:

```text
error while interpolating services.mariadb.environment.MARIADB_ROOT_PASSWORD: required variable MARIADB_ROOT_PASSWORD is missing a value: defina MARIADB_ROOT_PASSWORD no arquivo .env
```

O modificador `${MARIADB_ROOT_PASSWORD:?mensagem}` exige que a variável exista e não esteja vazia. Ele torna uma configuração obrigatória explícita e evita iniciar um serviço com uma configuração incompleta. Isso não verifica a força da senha; apenas sua presença. O arquivo foi restaurado depois do teste.

#### Desafio 5 — Variáveis interpoladas

```cmd
cd tarefa03\ambiente1
docker compose config
```

Na configuração resolvida, foram conferidos `MARIADB_DATABASE=labdb`, `MARIADB_PORT=3307` e `CLOUDBEAVER_PORT=8979`. As duas portas são interpoladas nos mapeamentos do Compose; não são variáveis repassadas automaticamente ao processo do banco. A variável `MARIADB_ROOT_PASSWORD` também foi resolvida, mas seu valor foi omitido das evidências. Foi usada a saída JSON de `docker compose config --format json` para conferir esses campos sem publicar a senha.

### Bloco B — Modelagem e Consultas SQL Básicas

Os comandos deste bloco foram executados no banco `biblioteca` do ambiente 1.

#### Desafio 6 — Tabela emprestimos

```sql
USE biblioteca;
CREATE TABLE IF NOT EXISTS emprestimos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  livro_id INT,
  data_emprestimo DATE,
  devolvido BOOLEAN,
  FOREIGN KEY (livro_id) REFERENCES livros(id)
);
```

A chave estrangeira impede associar um empréstimo a um livro inexistente. No MariaDB, `BOOLEAN` é um sinônimo de `TINYINT(1)`; neste laboratório foram usados os valores 0 e 1.

#### Desafio 7 — Três empréstimos

```sql
INSERT INTO emprestimos (livro_id, data_emprestimo, devolvido) VALUES
(1, '2026-11-01', FALSE),
(2, '2026-11-02', FALSE),
(3, '2026-10-30', TRUE);
SELECT * FROM emprestimos;
```

```text
id	livro_id	data_emprestimo	devolvido
1	1	2026-11-01	0
2	2	2026-11-02	0
3	3	2026-10-30	1
```

#### Desafio 8 — Empréstimos pendentes com livro e autor

```sql
SELECT l.titulo, e.data_emprestimo, a.nome AS autor
FROM emprestimos e
JOIN livros l ON l.id = e.livro_id
JOIN autores a ON a.id = l.autor_id
WHERE e.devolvido = FALSE;
```

```text
titulo	data_emprestimo	autor
Dom Casmurro	2026-11-01	Machado de Assis
Memórias Póstumas de Brás Cubas	2026-11-02	Machado de Assis
```

#### Desafio 9 — Autores com mais de um livro

```sql
SELECT a.nome AS autor, COUNT(*) AS total_obras
FROM autores a
JOIN livros l ON l.autor_id = a.id
GROUP BY a.id, a.nome
HAVING COUNT(*) > 1
ORDER BY a.id;
```

```text
autor	total_obras
Machado de Assis	4
Clarice Lispector	3
Gabriel García Márquez	3
Jane Austen	3
José de Alencar	3
Mary Shelley	2
Fiódor Dostoiévski	2
Eça de Queirós	2
Franz Kafka	2
Virginia Woolf	2
George Orwell	2
Jorge Luis Borges	2
Chinua Achebe	2
Chimamanda Ngozi Adichie	3
```

O `HAVING` filtra o resultado depois do agrupamento. Neste povoamento, todos os 14 autores possuem mais de um livro.

#### Desafio 10 — Reajuste de 10%

```sql
SELECT preco AS antes FROM livros WHERE id = 1;
UPDATE livros SET preco = ROUND(preco * 1.10, 2) WHERE id = 1;
SELECT titulo, preco AS depois FROM livros WHERE id = 1;
```

```text
antes
39.90
titulo	depois
Dom Casmurro	43.89
```

O preço de `Dom Casmurro` passou de 39,90 para 43,89. O filtro por chave primária limitou a alteração a um livro. Repetir o `UPDATE` acumularia novos reajustes; ele foi aplicado uma vez nessa base.

#### Desafio 11 — Remoção de autor sem livros

```sql
INSERT INTO autores (nome, pais, ano_nascimento)
VALUES ('Autor temporário do desafio', 'Brasil', 2000);
SET @autor_temporario = LAST_INSERT_ID();
DELETE FROM autores WHERE id = @autor_temporario;
SELECT ROW_COUNT() AS removidos;
SELECT COUNT(*) AS autores FROM autores;
```

```text
removidos
1
autores
14
```

A exclusão foi aceita porque nenhum livro referenciava esse autor. O identificador gerado foi guardado na mesma sessão para remover somente o registro recém-criado. A base voltou a ter 14 autores.

### Bloco C — Administração e Privilégios Avançados

#### Desafio 12 — Usuário de relatórios

Como root no ambiente 1:

```sql
CREATE USER 'relatorios'@'%' IDENTIFIED BY 'Relatorios2026!';
GRANT SELECT ON biblioteca.livros TO 'relatorios'@'%';
```

Como `relatorios`, `SELECT COUNT(*) FROM biblioteca.livros;` retornou 35. A permissão foi concedida no nível da tabela `livros`, sem acesso geral ao banco.

#### Desafio 13 — Consulta bloqueada

Conectado como `relatorios`:

```sql
SELECT * FROM biblioteca.autores;
```

```text
ERROR 1142 (42000) at line 1: SELECT command denied to user 'relatorios'@'127.0.0.1' for table `biblioteca`.`autores`
```

O erro 1142 ocorreu porque a conta recebeu `SELECT` sobre `livros`, mas não sobre `autores`. O teste usou TCP por `127.0.0.1` dentro do contêiner de teste, por isso esse é o host mostrado na mensagem. Uma conexão originada no CloudBeaver apresentaria o endereço de origem correspondente à rede Docker.

#### Desafio 14 — Concessão e revogação de INSERT

Como root:

```sql
GRANT INSERT ON biblioteca.livros TO 'relatorios'@'%';
```

Como `relatorios`:

```sql
INSERT INTO biblioteca.livros (titulo, ano_publicacao, preco, autor_id)
VALUES ('Livro de teste de privilégio', 2026, 10.00, 1);
SELECT ROW_COUNT() AS inseridos;
```

```text
inseridos
1
```

Como root:

```sql
REVOKE INSERT ON biblioteca.livros FROM 'relatorios'@'%';
```

Em uma nova conexão como `relatorios`:

```sql
INSERT INTO biblioteca.livros (titulo, ano_publicacao, preco, autor_id)
VALUES ('Inserção após revogação', 2026, 10.00, 1);
```

```text
ERROR 1142 (42000) at line 1: INSERT command denied to user 'relatorios'@'127.0.0.1' for table `biblioteca`.`livros`
```

Antes da revogação, um registro foi inserido. Depois dela, a conta manteve apenas `SELECT` e a segunda inserção foi recusada. Não foi necessário executar `FLUSH PRIVILEGES`, pois `GRANT` e `REVOKE` atualizam os privilégios diretamente. A primeira linha de teste foi removida como root, usando seu título e ano, e a contagem voltou a 35 livros.

#### Desafio 15 — Script setup.sql e idempotência

O arquivo completo está em [tarefa03/setup.sql](https://github.com/JefWill/dct2201-banco-de-dados/blob/main/tarefa03/setup.sql). Ele remove e recria `biblioteca`, cria as tabelas e chaves estrangeiras, recria as contas didáticas e suas permissões e executa as cargas inicial e expandida. Também reproduz os três empréstimos, o reajuste do livro 1 e a conta `relatorios` somente com `SELECT`, representando o estado final dos desafios.

O script é **destrutivo por definição**, pois contém `DROP DATABASE IF EXISTS biblioteca`. Foi executado duas vezes exclusivamente no ambiente 2. Para executá-lo manualmente a partir de `tarefa03`, a sequência equivalente é:

```cmd
docker compose -f ambiente2/docker-compose.yml --env-file ambiente2/.env cp setup.sql mariadb:/tmp/setup.sql
docker compose -f ambiente2/docker-compose.yml --env-file ambiente2/.env exec mariadb mariadb -uroot -p
```

Dentro do cliente MariaDB:

```sql
SOURCE /tmp/setup.sql;
SELECT COUNT(*) FROM biblioteca.autores;
SELECT COUNT(*) FROM biblioteca.livros;
SELECT COUNT(*) FROM biblioteca.emprestimos;
```

Na validação automatizada, o conteúdo foi fornecido ao cliente MariaDB pela entrada padrão, sem exibir a senha. Ambas as execuções concluíram sem erro e produziram:

```text
autores
14
livros
35
emprestimos
3
preco
43.89
```

A repetição parte de uma base vazia, portanto não duplica registros nem acumula o reajuste. Idempotente aqui significa reconstruir o mesmo estado lógico; não significa preservar dados inseridos depois da carga. O arquivo não contém a senha local de root. As senhas das contas de exercício são os exemplos didáticos indicados no roteiro.

### Conferências complementares e encerramento

As seis consultas obrigatórias da seção 10 estão em [consultas.sql](https://github.com/JefWill/dct2201-banco-de-dados/blob/main/tarefa03/consultas.sql) e foram executadas na cópia do ambiente 1. A tentativa de `DROP TABLE autores` com `app_biblioteca` retornou erro 1142; a inserção de um livro com autor 999 retornou erro 1452. Os dados finais dos desafios ficaram em 14 autores, 35 livros e 3 empréstimos.

Após os testes:

```cmd
cd tarefa03\ambiente2
docker compose down
cd ..\ambiente1
docker compose down
```

Os volumes foram preservados. O banco principal continuou com seus 14 autores, 35 livros e preço original de 39,90 para o livro 1. O `.env` de cada ambiente está ignorado pelo Git e não integra a entrega. Apenas este Markdown será enviado no PR ao repositório da disciplina; todos os arquivos de infraestrutura e SQL ficam no repositório pessoal.
