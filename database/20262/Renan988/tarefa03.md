# 1 - Indentificação
 - **Nome Completo:** Renan Medeiros Nogueira;
 - **Usuário no GitHub:** Renan988;
 - **Email Acadêmico:** renan.medeiros.150@ufrn.edu.br

### Pergunta Discursiva 1

**Diferença entre DDL e DML:**
* **Criar uma tabela (DDL — Data Definition Language):** Trata-se da etapa de definição da estrutura. O comando DDL (`CREATE TABLE`) funciona como o projeto ou esqueleto do banco de dados: ele define o nome da tabela, quais colunas existirão, os tipos de dados aceitos (como texto, inteiros ou números decimais), quais campos são obrigatórios e as regras de relacionamento (chaves primárias e estrangeiras).
* **Inserir registros (DML — Data Manipulation Language):** Trata-se da etapa de manipulação do conteúdo. Com o comando DML (`INSERT INTO`), preenchemos a estrutura que já foi criada previamente com os dados reais. Em termos simples: o DDL constrói as "gavetas" e o DML coloca os "objetos" dentro delas.

**Impacto de apagar uma tabela com `DROP TABLE` (DDL):**
Quando executamos o comando DDL `DROP TABLE`, a estrutura completa da tabela é destruída no banco de dados. Como consequência, todos os registros e dados que estavam armazenados dentro dela são permanentemente apagados e perdidos, juntamente com suas definições de colunas e restrições.

### Pergunta Discursiva 2

**Análise do Erro 1142 e Princípio do Menor Privilégio:**
Quando tentei executar o comando `DROP TABLE autores` utilizando a conta `app_biblioteca`, o MariaDB recusou a operação e retornou o erro `1142 (42000): DROP command denied to user 'app_biblioteca'@'...' for table 'autores'`. Isso ocorreu porque a essa conta só foram concedidos privilégios de manipulação de dados (DML: `SELECT`, `INSERT`, `UPDATE`, `DELETE`), não possuindo permissões de definição de dados (DDL), como o comando `DROP`.

Essa restrição aplica na prática o **princípio do menor privilégio**. Caso a aplicação web seja alvo de uma invasão (por exemplo, por meio de uma vulnerabilidade de SQL Injection) ou execute um código com falhas de programação, o atacante/sistema não conseguirá apagar tabelas ou destruir o esquema estrutural do banco de dados, protegendo a integridade física da infraestrutura e limitando severamente a extensão dos danos.

---

### Pergunta Discursiva 3

**Uso do Host '%' vs 'localhost' e a Rede Interna do Docker:**
No MariaDB e MySQL, as contas de usuário são compostas pelo par `'usuario'@'host'`, onde o host restringe de onde a conexão pode se originar. Se o usuário fosse criado como `'app_biblioteca'@'localhost'`, o MariaDB aceitaria apenas conexões locais vindas do próprio contêiner onde o SGBD reside (via socket UNIX ou loopback).

Como a arquitetura utilizada utiliza o **Docker Compose**, o serviço do MariaDB e a interface do CloudBeaver rodam em contêineres completamente isolados, comunicando-se através de uma rede virtual interna criada pelo Docker (que atribui endereços de IP distintos a cada contêiner em uma sub-rede própria). O caractere curinga `'%'` funciona como um wildcard, permitindo que a aplicação se autentique com sucesso a partir de qualquer contêiner membro da rede virtual do Docker.

### Pergunta Discursiva 4

**Total de Registros Cadastrados:**
Após a execução da carga expandida de dados, a base de dados ficou cadastrada com o total de **14 autores** (4 da carga inicial + 10 gerados pela IA) e **30 livros** (5 da carga inicial + 25 gerados pela IA).

**Inserção com `autor_id = 999` e Regra de Restrição:**
Se eu tentasse executar uma instrução DML `INSERT` na tabela `livros` informando um `autor_id` igual a `999` (um autor que não existe na tabela `autores`), o MariaDB recusaria a inserção e retornaria um erro de violação de restrição (por exemplo, `SQL Error [1452] [23000]: Cannot add or update a child row: a foreign key constraint fails`).

A regra do banco que impede essa ação é a **Integridade Referencial**, garantida pela restrição de **Chave Estrangeira (`FOREIGN KEY`)**. Essa restrição exige que todo valor inserido na coluna `autor_id` da tabela filha (`livros`) corresponda obrigatoriamente a um valor de `id` já existente e válido na tabela pai (`autores`).

### Pergunta Discursiva 5

**Vantagens da Normalização e Divisão em Tabelas Relacionadas:**
Ao analisar as Consultas 4 e 5, fica evidente que separar as informações em duas tabelas distintas (`autores` e `livros`) traz vantagens práticas fundamentais em relação ao armazenamento de dados duplicados:

1. **Eliminação de Redundância e Economia de Espaço:** Se o nome, país e ano de nascimento do autor fossem gravados dentro de cada linha da tabela `livros`, esses dados seriam repetidos dezenas de vezes para autores com muitas obras. A divisão economiza espaço de armazenamento ao guardar cada autor uma única vez.
2. **Integridade e Facilidade de Atualização (Manutenção Única):** Se um autor mudar de nome ou se o seu país de origem precisar ser corrigido, a alteração é feita em apenas um registro na tabela `autores`. Caso estivesse tudo em uma única tabela, seria necessário atualizar centenas de linhas de livros individualmente, correndo o risco de gerar inconsistências se alguma linha fosse esquecida.
3. **Facilidade em Agregações e Análises:** A separação simplifica o cálculo de estatísticas (como a média de preço calculada na Consulta 5). O banco identifica o autor pelo seu `id` único, permitindo agrupar e cruzar dados com precisão e sem ambiguidades.

## Desafios:

### 1. Alteração de porta do SGBD:** Altere a variável `MARIADB_PORT` no `.env` para a porta `3307`. Reinicie o serviço e explique como você reconfigurou a conexão do CloudBeaver para acessar o banco na porta alterada.

Fiz a alteração no `.env` trocando a porta para `3307` e reiniciei os serviços com `docker compose down` e `docker compose up -d`. Conectei no CloudBeaver, fiz a conexão com o MariaDB e funcionou normalmente sem precisar mexer na porta `3306` configurada lá dentro, e os dados continuavam todos acessíveis.

### 2. Dois ambientes simultâneos: Configure duas pastas distintas no seu computador com arquivos docker-compose.yml e portas/volumes desacoplados. Explique como você garantiu que quatro contêineres rodassem em paralelo sem conflito de portas ou nomes.

Para rodar os quatro contêineres juntos (dois do MariaDB e dois do CloudBeaver) sem dar conflito, precisei ajustar três coisas:

1. **Portas do host:** No `.env` do `projeto2`, mudei as portas de saída para não dar erro de porta em uso (`bind: address already in use`). Deixei o `projeto1` nas portas padrão (`3306` do MariaDB e `8978` do CloudBeaver) e o `projeto2` usando `3307` e `8979`.
2. **Nome dos projetos e contêineres:** Como subi o Compose em pastas separadas e passei a flag `-p` (`proj1` e `proj2`), o Docker criou os contêineres com nomes diferentes (`proj1-mariadb-1` e `proj2-mariadb-1`), sem um atropelar o outro.
3. **Volumes de dados:** Os volumes onde o banco salva os arquivos também receberam o prefixo do projeto (`proj1_mariadb_data` e `proj2_mariadb_data`). Com isso, os dois bancos rodaram de forma isolada sem misturar ou sobrescrever as informações.

### 3. Persistência do volume e alteração de senha de root: Altere o valor de MARIADB_ROOT_PASSWORD no arquivo .env para uma nova senha qualquer. Execute docker compose up -d e observe que a autenticação antiga continua válida enquanto a nova falha. Explique detalhadamente por que isso ocorre e quais são os dois caminhos possíveis para aplicar uma nova senha de root.

Ao alterar a senha no `.env` e rodar o `docker compose up -d`, a senha antiga continuou funcionando e a nova falhou. Isso acontece porque a variável `MARIADB_ROOT_PASSWORD` só é lida pelo script de inicialização do contêiner (`docker-entrypoint`) na primeira vez que o ambiente é criado, quando o diretório do banco ainda está vazio. Como o volume nomeado (`mariadb_data`) já existia e continha os dados salvos, o MariaDB simplesmente ignorou a nova variável do `.env` e manteve a senha gravada no disco.

Para aplicar uma nova senha de root, existem dois caminhos:

1. **Recriar o volume (destrutivo):** Apagar o volume antigo com `docker compose down -v` e subir o ambiente novamente com `docker compose up -d`. Isso força o contêiner a rodar a inicialização do zero e aplicar a senha nova do `.env`, mas todos os dados anteriores são perdidos.
2. **Alterar via comando SQL (preservando os dados):** Manter os dados intactos, acessar o MariaDB com a senha antiga (via CloudBeaver ou `docker exec`) e rodar a instrução `ALTER USER 'root'@'%' IDENTIFIED BY 'NovaSenha'; FLUSH PRIVILEGES;`.

### 4. Comportamento da validação estrita (:?): Apague temporariamente o arquivo .env (ou comente a linha da senha de root) e execute docker compose up -d. Documente a mensagem de erro emitida pelo Compose e explique discursivamente a importância do modificador :? em ambientes profissionais.

A sintaxe `${VAR:?mensagem}` funciona como uma trava de segurança. Se a variável não estiver definida no .env (ou se o arquivo for apagado), o Docker Compose nem tenta subir o ambiente: ele aborta o processo na hora e solta a mensagem de erro que configuramos.

Em ambientes profissionais, usar essa validação é essencial por dois motivos:

- Evitar brechas de segurança: Garante que o banco nunca vai subir para produção sem senha de root ou com acesso liberado por esquecimento da equipe de infra.

- Conceito de Fail-Fast: Em esteiras automáticas de deploy (CI/CD), é melhor o processo quebrar imediatamente antes de criar os contêineres do que deixar o sistema subir pela metade e dar problema depois de já estar rodando.

### 5. Inspeção de variáveis no compose: Execute docker compose config no terminal e liste três variáveis de ambiente que foram resolvidas e interpoladas a partir do .env.

Ao rodar o comando `docker compose config`, o Docker Compose lê os arquivos de configuração, resolve as variáveis declaradas no `.env` e exibe o YAML final já interpolado. Três variáveis de ambiente resolvidas a partir do `.env` foram:

1. **`MARIADB_ROOT_PASSWORD`**: Substituída dentro das variáveis de ambiente do serviço `mariadb`, definindo a senha secreta do usuário root.
2. **`MARIADB_DATABASE`**: Interpolada no serviço `mariadb` para definir o nome do banco de dados inicial criado automaticamente na sobida do contêiner (`labdb`).
3. **`CLOUDBEAVER_PORT`**: Resolvida na seção `ports` do serviço `cloudbeaver`, mapeando a porta de acesso da interface web no host (`8978:8978`).

### 6. Criação da tabela de empréstimos: Escreva o comando DDL para criar a tabela emprestimos contendo os campos id (INT AUTO_INCREMENT PRIMARY KEY), livro_id (INT), data_emprestimo (DATE) e devolvido (BOOLEAN), com restrição de chave estrangeira referenciando livros(id)

**Comando SQL (DDL):**
```sql
USE biblioteca;

CREATE TABLE IF NOT EXISTS emprestimos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  livro_id INT,
  data_emprestimo DATE NOT NULL,
  devolvido BOOLEAN DEFAULT FALSE,
  FOREIGN KEY (livro_id) REFERENCES livros(id)
);
```

O comando DDL cria a tabela `emprestimos` estruturando os campos necessários para o controle do acervo. O campo `livro_id` foi configurado como chave estrangeira (`FOREIGN KEY`) apontando para a coluna `id` da tabela `livros`, o que garante a integridade referencial: nenhum empréstimo pode ser registrado para um livro que não existe no banco. O campo `devolvido` usa o tipo `BOOLEAN` (que no MariaDB é tratado internamente como `TINYINT(1)`), com valor padrão `FALSE` para indicar que o livro começa pendente de devolução.

### 7. Carga da tabela empréstimos: Escreva as instruções INSERT para cadastrar três registros de empréstimos, sendo dois com status não devolvido (FALSE ou 0) e um devolvido (TRUE ou 1).

**Comandos SQL (DML):**
```sql
USE biblioteca;

INSERT INTO emprestimos (livro_id, data_emprestimo, devolvido) VALUES
(1, '2026-03-01', FALSE),
(5, '2026-03-05', FALSE),
(10, '2026-02-15', TRUE);
```
Inseri três registros de empréstimos associados a livros já existentes no acervo (IDs 1, 5 e 10). Para os dois primeiros registros, o campo `devolvido` foi definido como `FALSE` (ou 0), indicando que as obras continuam pendentes. Já o terceiro registro recebeu o valor `TRUE` (ou 1), registrando a devolução concluída do livro. As datas foram inseridas no formato padrão do SQL (AAAA-MM-DD).

### 8 Consulta de pendências: Escreva uma consulta que liste todos os empréstimos pendentes (não devolvidos), trazendo o título do livro, a data de empréstimo e o nome do autor do livro.

**Comando SQL (DQL):**
```sql
USE biblioteca;

SELECT 
    l.titulo, 
    e.data_emprestimo, 
    a.nome AS autor
FROM emprestimos e
JOIN livros l ON e.livro_id = l.id
JOIN autores a ON l.autor_id = a.id
WHERE e.devolvido = FALSE;

```
A consulta utiliza dois `JOINs` para relacionar as três tabelas do banco: conecta emprestimos a livros através do `livro_id` e livros a autores usando o `autor_id`. O filtro `WHERE e.devolvido = FALSE` garante que apenas os empréstimos em aberto sejam retornados, exibindo o título da obra, a data em que foi emprestada e o nome do autor correspondente.

### 9. Filtragem de grupos com HAVING: Escreva uma consulta que agrupe os livros por autor e retorne a contagem total de obras de cada um, filtrando exclusivamente autores que possuem mais de 1 livro cadastrado (HAVING COUNT(*) > 1).

**Comando SQL (DQL):**
```sql
USE biblioteca;

SELECT 
    a.nome AS autor, 
    COUNT(l.id) AS total_livros
FROM autores a
JOIN livros l ON a.id = l.autor_id
GROUP BY a.id, a.nome
HAVING COUNT(l.id) > 1;
```

A consulta une as tabelas autores e livros e agrupa os resultados por autor utilizando o `GROUP BY`. Enquanto o `WHERE` filtra linhas individuais antes do agrupamento, a cláusula `HAVING COUNT(l.id) > 1` entra em ação depois que os grupos já foram formados, descartando autores com apenas uma obra e retornando só quem tem dois ou mais livros cadastrados no banco.

### 10. Atualização proporcional (UPDATE): Execute uma instrução DML para reajustar o preço de um livro específico em 10% de acréscimo. Transcreva a consulta UPDATE utilizada e comente o resultado.

**Comando SQL (DML):**
```sql
USE biblioteca;

UPDATE livros 
SET preco = preco * 1.10 
WHERE id = 1;
```
A instrução `UPDATE` aplica um acréscimo proporcional de 10% multiplicando o valor da coluna `preco` por 1.10. O uso do `WHERE id = 1` é fundamental para garantir que o reajuste afete apenas a linha do livro desejado, evitando que a alteração seja aplicada acidentalmente a toda a tabela. Ao rodar o comando, o MariaDB retorna que 1 linha foi afetada, e a checagem no banco confirma o novo valor recalculado corretamente.

### 11. Remoção condicional (DELETE): Cadastre um novo autor sem nenhum livro associado e, em seguida, execute a instrução DELETE para removê-lo da tabela autores. Explique por que essa remoção foi aceita sem violar a restrição de chave estrangeira.

**Comandos SQL (DML):**
```sql
USE biblioteca;

-- 1. Cadastrar um autor sem nenhum livro associado
INSERT INTO autores (nome, pais, ano_nascimento) VALUES
('Autor Teste', 'Brasil', 1990);

-- 2. Remover o autor recém-criado
DELETE FROM autores 
WHERE nome = 'Autor Teste';
```
A remoção do autor foi executada com sucesso e sem violar a restrição de chave estrangeira (`FOREIGN KEY`) porque a chave estrangeira protege apenas a integridade referencial entre registros relacionados. Como o novo autor foi cadastrado e nenhum livro da tabela `livros` foi associado ao id dele (não existiam linhas filhas apontando para esse registro pai), o MariaDB permitiu o `DELETE` sem gerar conflito.

Se houvesse pelo menos um livro cadastrado utilizando o `id` desse autor, o banco teria bloqueado a exclusão e retornado o erro `1451` (falha na restrição de chave estrangeira).

### 12. Criação de usuário restrito para relatórios: Crie um usuário chamado relatorios com senha Relatorios2026!, concedendo privilégio de SELECT exclusivamente sobre a tabela livros do banco biblioteca.

**Comandos SQL (DCL):**
```sql
USE biblioteca;

-- 1. Criar o usuário relatorios com acesso liberado a partir de qualquer host da rede
CREATE USER IF NOT EXISTS 'relatorios'@'%' IDENTIFIED BY 'Relatorios2026!';

-- 2. Conceder permissão de leitura (SELECT) exclusivamente na tabela livros
GRANT SELECT ON biblioteca.livros TO 'relatorios'@'%';

-- 3. Atualizar a tabela de privilégios do MariaDB
FLUSH PRIVILEGES;
```
O comando `CREATE USER IF NOT EXISTS` cria a conta `relatorios` de forma segura. Em seguida, a instrução `GRANT SELECT ON biblioteca.livros` aplica o princípio do menor privilégio, limitando a permissão de leitura apenas à tabela `livros`.

Se esse usuário tentar realizar qualquer alteração (`INSERT`, `UPDATE`, `DELETE`) ou consultar outras tabelas do mesmo banco (como `autores` ou `emprestimos`), o MariaDB bloqueará a operação imediatamente e retornará um erro de permissão negada (`Erro 1142`).

### 13. Teste de restrição de visibilidade: Conecte-se com o usuário relatorios, tente consultar a tabela autores e transcreva a mensagem de erro emitida pelo SGBD, explicando o motivo do bloqueio.

**Comando SQL executado (autenticado como `relatorios`):**
```sql
SELECT * FROM autores;
```

```
SQL Error [1142] [42000]: SELECT command denied to user 'relatorios'@'%' for table 'autores'
```
O MariaDB bloqueou a operação e retornou o Erro 1142 porque o usuário `relatorios` foi configurado estritamente sob o princípio do menor privilégio. Como concedemos permissão de `SELECT` apenas para a tabela `biblioteca.livros`, qualquer tentativa desse usuário de consultar a tabela `autores` (ou qualquer outra tabela do banco) é impedida pelo SGBD, garantindo o controle de acesso e o isolamento dos dados.

### 14. Concessão e revogação dinâmica de privilégios: Conectado como root, conceda privilégio de INSERT na tabela livros para o usuário relatorios. Realize uma inserção de teste com sucesso e, em seguida, revogue o privilégio via REVOKE. Descreva discursivamente o resultado de tentar inserir novamente após a revogação.

**Comandos SQL (DCL e DML):**
```sql
USE biblioteca;

GRANT INSERT ON biblioteca.livros TO 'relatorios'@'%';
FLUSH PRIVILEGES;

INSERT INTO livros (titulo, ano_publicacao, preco, autor_id) 
VALUES ('Livro Teste Privilégio', 2026, 49.90, 1);

REVOKE INSERT ON biblioteca.livros FROM 'relatorios'@'%';
FLUSH PRIVILEGES;

INSERT INTO livros (titulo, ano_publicacao, preco, autor_id) 
VALUES ('Livro Teste Bloqueado', 2026, 39.90, 1);
```
Após conceder a permissão de `INSERT` com a conta `root`, o usuário `relatorios` conseguiu cadastrar o primeiro livro de teste perfeitamente. Em seguida, ao executar o `REVOKE` como `root`, o privilégio de escrita foi removido da conta.

Ao tentar realizar a segunda inserção com o usuário `relatorios`, o MariaDB bloqueou a operação imediatamente e retornou o erro `1142 (42000): INSERT command denied to user 'relatorios'@'%' for table 'livros'`. Isso demonstra a dinâmica dos privilégios no MariaDB: o SGBD valida as permissões a cada comando executado, aplicando as restrições no exato momento em que o direito é revogado.

### 15. Script idempotente de automação (setup.sql): Desenvolva um script SQL completo chamado setup.sql que recrie do zero todo o banco de dados biblioteca, suas tabelas, restrições, usuários (app_biblioteca, consulta) com privilégios e a carga de dados. Versiona esse arquivo no seu repositório pessoal no GitHub.

Para garantir essa idempotência no setup.sql, o script começa executando DROP DATABASE IF EXISTS biblioteca seguido da criação limpa do esquema (CREATE DATABASE). Da mesma forma, os usuários app_biblioteca e consulta passam por DROP USER IF EXISTS antes de serem criados novamente com suas respectivas regras de GRANT. Por fim, toda a estrutura DDL (tabelas autores, livros e emprestimos) e a carga DML são aplicadas na ordem exata de dependência das chaves estrangeiras, permitindo reconstruir todo o ambiente do zero com um único comando.