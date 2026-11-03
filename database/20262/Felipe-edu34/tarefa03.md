## Descrição

Implementação da Tarefa 03 da disciplina DCT2201 - Banco de Dados.

Foi adicionada a documentação da atividade, incluindo:
- Configuração do ambiente com Docker Compose.
- Administração do MariaDB.
- Criação e manipulação de tabelas.
- Gerenciamento de usuários e permissões.
- Testes com GRANT e REVOKE.

Repositório pessoal: https://github.com/Felipe-edu34/dct2201-banco-de-dados

Relacionado à Issue #549.


### 1. Qual a diferença entre DDL e DML? O que acontece ao executar DROP TABLE?

DDL (Data Definition Language) é utilizada para definir e modificar a estrutura do banco de dados, por meio de comandos como CREATE, ALTER e DROP.

DML (Data Manipulation Language) é utilizada para manipular os registros armazenados nas tabelas, por meio de comandos como INSERT, UPDATE e DELETE.

O comando DROP TABLE exclui uma tabela, removendo sua estrutura e seus dados. Essa operação pode causar perda de informações e, normalmente, exige um backup para recuperação.

### 2. Por que o usuário app_biblioteca recebeu erro ao executar DROP TABLE?

O usuário `app_biblioteca` recebeu o erro 1142 porque não possui a permissão DROP.

Esse comportamento é esperado, pois o usuário recebeu apenas as permissões SELECT, INSERT, UPDATE e DELETE. Dessa forma, pode manipular os registros, mas não pode excluir a estrutura das tabelas.

Isso demonstra a aplicação do princípio do menor privilégio, no qual cada usuário recebe somente as permissões necessárias para suas atividades.

### 3. Qual a finalidade do símbolo % na criação dos usuários?

O símbolo `%` representa qualquer host, permitindo que o usuário se conecte ao MariaDB a partir de diferentes endereços de origem.

No ambiente Docker, isso facilita a conexão entre os contêineres, pois a aplicação e o banco de dados podem estar em serviços diferentes.

Em ambientes de produção, é recomendável restringir os hosts permitidos sempre que possível.

### 4. Como verificar a quantidade de registros e garantir a integridade referencial?

A quantidade de registros pode ser verificada utilizando COUNT:

```sql
SELECT COUNT(*) AS total_autores FROM autores;
SELECT COUNT(*) AS total_livros FROM livros;
```

A integridade referencial é garantida pelas chaves estrangeiras. Por exemplo, a tabela `livros` possui a chave estrangeira `autor_id`, que referencia a tabela `autores`.

Assim, não é permitido inserir um livro associado a um autor inexistente.

### 5. Qual a importância da normalização do banco de dados?

A normalização organiza as informações para reduzir a repetição de dados e evitar inconsistências.

No banco `biblioteca`, os dados dos autores ficam armazenados na tabela `autores`, enquanto os dados dos livros ficam na tabela `livros`.

A relação entre as tabelas é estabelecida pela chave estrangeira `autor_id`. Dessa maneira, os dados de um autor não precisam ser repetidos em todos os registros de livros.



### a) Por que uma aplicação nunca deve utilizar o usuário root?

O usuário root possui privilégios administrativos amplos, podendo criar e excluir bancos de dados, tabelas e usuários, além de alterar permissões.

Se uma aplicação utilizar essa conta e suas credenciais forem comprometidas, um invasor poderá causar danos graves, como excluir informações, modificar dados e criar outros usuários.

Por isso, é recomendado utilizar uma conta específica para a aplicação, com apenas as permissões necessárias.

### b) Qual a diferença entre DDL e DML? Como separar os privilégios?

DDL define e modifica a estrutura do banco de dados, utilizando comandos como CREATE, ALTER e DROP.

DML manipula os registros das tabelas, utilizando comandos como INSERT, UPDATE e DELETE. O SELECT é utilizado para consultar os dados e também pode ser classificado como DQL.

Separar os privilégios permite que usuários administrativos cuidem da estrutura do banco, enquanto usuários da aplicação realizam somente as operações necessárias sobre os registros.

### c) Qual a importância dos arquivos .env e .env.example?

O arquivo `.env` armazena as configurações locais e informações sensíveis, como senhas e credenciais.

O arquivo `.env.example` apresenta um modelo das variáveis necessárias para configurar o projeto, sem disponibilizar as senhas reais.

O `.env` deve ser incluído no `.gitignore`, evitando que suas credenciais sejam publicadas no GitHub.

Caso uma senha seja publicada acidentalmente, ela deve ser alterada imediatamente. Apenas apagar o arquivo do repositório não elimina sua presença no histórico do Git.

### d) O .env e o .gitignore garantem proteção completa das credenciais?

Não. Esses arquivos ajudam a evitar a publicação acidental de informações sensíveis, mas não garantem segurança completa.

O arquivo `.env` continua armazenado em texto simples no computador e pode ser acessado por outros usuários, programas maliciosos ou backups.

Em ambientes de produção, é recomendado utilizar ferramentas próprias para gerenciamento de segredos, restringir permissões de acesso e realizar a troca periódica das credenciais.

### e) O que são contêineres e quais suas vantagens?

Contêineres são ambientes isolados que permitem executar aplicações e serviços utilizando recursos do sistema operacional hospedeiro.

Com Docker, é possível executar o MariaDB e o CloudBeaver sem precisar instalar diretamente esses serviços no sistema principal.

Entre as vantagens estão a portabilidade, a facilidade de configuração, a reprodução do ambiente e o isolamento dos serviços.

Os volumes Docker também permitem persistir os dados mesmo quando os contêineres são encerrados ou recriados.

Entretanto, contêineres não são máquinas virtuais completas e não garantem segurança absoluta.

## 10. Desafios

### Desafio A1 - Alteração da porta do MariaDB

Para alterar a porta externa do MariaDB para 3307, basta modificar a variável no arquivo `.env`:

```env
MARIADB_PORT=3307
```

A configuração do Docker Compose continua utilizando a variável:

```yaml
ports:
  - "${MARIADB_PORT:-3306}:3306"
```

Assim, o acesso pelo computador hospedeiro será realizado pela porta 3307. Entre contêineres, a comunicação continua utilizando a porta interna 3306.

### Desafio A2 - Executar duas instâncias do ambiente

Para executar duas instâncias simultaneamente, é necessário evitar conflitos de nomes de contêineres, portas e volumes.

Uma solução é utilizar diretórios e arquivos Compose separados, removendo os nomes fixos definidos em `container_name`.

Também devem ser utilizadas portas externas diferentes, por exemplo:

- Primeira instância: MariaDB 3306 e CloudBeaver 8978.
- Segunda instância: MariaDB 3307 e CloudBeaver 8979.

Cada projeto deve possuir seu próprio volume para evitar compartilhamento acidental dos dados.

### Desafio A3 - Alterar a senha do root

Alterar somente a variável `MARIADB_ROOT_PASSWORD` no `.env` não altera automaticamente a senha de um banco que já foi inicializado.

Isso acontece porque a imagem do MariaDB utiliza essa variável durante a inicialização do banco de dados no volume.

Para alterar a senha de uma instalação existente, conecte-se como root e execute:

```sql
ALTER USER 'root'@'localhost'
IDENTIFIED BY 'NovaSenhaForte2026!';
```

O host do usuário deve ser conferido no ambiente, pois pode ser diferente de `localhost`.

Outra possibilidade é remover o volume e recriar o ambiente, mas isso apaga os dados persistidos e só deve ser feito quando eles puderem ser descartados.

### Desafio A4 - Executar sem o arquivo .env

Quando o arquivo `.env` não existe e uma variável obrigatória é declarada com a sintaxe `${VAR:?mensagem}`, o Docker Compose interrompe a interpolação e apresenta uma mensagem de erro.

Isso evita que o serviço seja iniciado sem uma configuração obrigatória, como a senha do root.

### Desafio A5 - Verificar as variáveis do Docker Compose

O comando abaixo permite visualizar a configuração final após a substituição das variáveis:

```bash
docker compose config
```

Ele permite conferir as portas, os serviços e outras configurações utilizadas pelo Compose.

Entretanto, a saída pode exibir senhas e outras informações sensíveis. Portanto, não deve ser compartilhada publicamente.

### Desafio B6 - Criar a tabela emprestimos

Foi criada a tabela `emprestimos`, contendo uma chave primária e uma chave estrangeira que referencia a tabela `livros`.

```sql
CREATE TABLE emprestimos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    livro_id INT,
    data_emprestimo DATE,
    devolvido BOOLEAN,
    FOREIGN KEY (livro_id) REFERENCES livros(id)
);
```

### Desafio B7 - Inserir empréstimos

Foram inseridos três registros para representar empréstimos realizados em datas diferentes:

```sql
INSERT INTO emprestimos
(livro_id, data_emprestimo, devolvido)
VALUES
(1, '2026-10-20', FALSE),
(2, '2026-10-22', FALSE),
(3, '2026-10-25', TRUE);
```

### Desafio B8 - Consultar empréstimos em andamento

A consulta abaixo apresenta os livros que ainda não foram devolvidos, juntamente com seus autores:

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

### Desafio B9 - Identificar autores com mais de um livro

A consulta utiliza GROUP BY para agrupar os livros por autor e HAVING para apresentar somente os autores com mais de um livro:

```sql
SELECT
    a.nome AS autor,
    COUNT(l.id) AS quantidade_livros
FROM autores a
JOIN livros l ON l.autor_id = a.id
GROUP BY a.id, a.nome
HAVING COUNT(l.id) > 1;
```

### Desafio B10 - Atualizar o preço de um livro

O comando abaixo aumenta em 10% o preço do livro de ID 1:

```sql
UPDATE livros
SET preco = ROUND(preco * 1.10, 2)
WHERE id = 1;
```

O preço pode ser conferido antes e depois da atualização com SELECT.

### Desafio B11 - Inserir e excluir um autor temporário

Foi utilizado um registro temporário para testar as operações de inserção e exclusão:

```sql
INSERT INTO autores (nome, pais, ano_nascimento)
VALUES ('Autor Temporário', 'Brasil', 2000);
```

Depois, o registro pode ser removido:

```sql
DELETE FROM autores
WHERE nome = 'Autor Temporário';
```

Como nenhum livro foi associado a esse autor temporário, sua exclusão não viola a chave estrangeira.

### Desafio C12 - Criar usuário para relatórios

Foi criado um usuário com permissão somente de consulta na tabela `livros`:

```sql
CREATE USER 'relatorios'@'%'
IDENTIFIED BY 'Relatorios2026!';

GRANT SELECT ON biblioteca.livros
TO 'relatorios'@'%';
```

### Desafio C13 - Testar as permissões do usuário

Conectado como `relatorios`, foi possível consultar a tabela `livros`:

```sql
SELECT * FROM livros;
```

Ao tentar consultar a tabela `autores`:

```sql
SELECT * FROM autores;
```

O MariaDB retornou um erro de acesso negado, pois o usuário não possui permissão para consultar essa tabela.

### Desafio C14 - Conceder e revogar permissão de INSERT

Inicialmente, foi concedida a permissão de inserção:

```sql
GRANT INSERT ON biblioteca.livros
TO 'relatorios'@'%';
```

Após o teste de inserção, a permissão foi revogada:

```sql
REVOKE INSERT ON biblioteca.livros
FROM 'relatorios'@'%';
```

Uma nova tentativa de inserção deve retornar erro de acesso negado, demonstrando que a permissão foi retirada.

### Desafio C15 - Reconstruir o banco de dados

Para reconstruir o banco de dados desde o início, o arquivo `setup.sql` foi organizado para criar o banco `biblioteca`, suas tabelas, relacionamentos, usuários, permissões e dados iniciais.

O script utiliza:

```sql
DROP DATABASE IF EXISTS biblioteca;
CREATE DATABASE biblioteca
CHARACTER SET utf8mb4
COLLATE utf8mb4_general_ci;
```

Também utiliza `DROP USER IF EXISTS` antes da criação dos usuários, evitando conflitos caso eles já existam.

Essa abordagem permite executar novamente o script e reconstruir o ambiente inicial. Entretanto, a operação é destrutiva, pois remove os dados anteriores do banco.

**Atenção:** o arquivo `povoamento.sql` é utilizado separadamente para inserir os autores e livros adicionais.

## 11. Conclusão

A atividade permitiu aplicar conceitos de administração de banco de dados, configuração de serviços com Docker Compose, modelagem relacional, manipulação de dados e gerenciamento de privilégios.

Os testes demonstraram a importância da integridade referencial, da separação de usuários e da aplicação do princípio do menor privilégio.
