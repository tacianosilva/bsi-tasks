Nome do Aluno: Nikcael Gidalte Lopes da Silva  
Email Acadêmico: nikcael.lopes.124@ufrn.edu.br  
[Link do Perfil do Github](https://github.com/nikcaellp)  
[link do repositorio Local](https://github.com/nikcaellp/tarefas-bd.git)   

## 1-Explique com suas palavras a diferença entre criar uma tabela (DDL) e inserir registros nessa tabela (DML). Se apagarmos uma tabela com um comando DDL (DROP TABLE), o que acontece com os dados que estavam dentro dela?
A diferença entre DDL e DML está na finalidade de cada tipo de comando SQL
O DDL é utilizado para definir e modificar a estrutura do banco de dados, como criar, alterar ou excluir tabelas, por meio de comandos como CREATE, ALTER e DROP. Já o DML é utilizado para manipular os registros armazenados nessas tabelas, permitindo inserir, consultar, atualizar e excluir dados, por meio de comandos como INSERT, SELECT, UPDATE e DELETE.

Se executarmos o comando DROP TABLE, a tabela será removida do banco de dados, incluindo sua estrutura e todos os registros armazenados nela. Ou seja, os dados serão excluídos junto com a tabela, e não poderão mais ser acessados por meio dela.

## 2-Descreva com suas palavras o que aconteceu quando você tentou executar o comando DROP TABLE autores com a conta app_biblioteca. Por que o MariaDB recusou a operação com o erro 1142? De que forma essa restrição protege a integridade do banco de dados caso a aplicação web sofra uma invasão ou falha de programação?
Ao tentar executar o comando `DROP TABLE autores` utilizando a conta `app_biblioteca`, o MariaDB recusou a operação e apresentou o erro 1142, informando que o usuário não possuía permissão para excluir a tabela. isso aconteceu porque foram concedidas a essa conta apenas permissões de consulta e manipulação dos registros, sem autorização para modificar ou excluir a estrutura das tabelas.

Essa restrição segue o princípio do menor privilégio e aumenta a segurança do banco de dados. Caso a aplicação web sofra uma invasão ou apresente uma falha de programação, o invasor ou a própria aplicação não conseguirá excluir tabelas utilizando essa conta, reduzindo os possíveis danos e protegendo a estrutura e a integridade do banco de dados.

## 3-Por que os usuários foram criados com o host '%' em vez de 'localhost'? Qual é o papel da rede interna do Docker nessa decisão técnica?
Os usuários foram criados com o host `'%'` porque precisam permitir conexões originadas de outros endereços, e não apenas da própria máquina onde o MariaDB está instalado. O símbolo `%` funciona como um curinga, permitindo conexões de diferentes hosts.

Nesse cenário, o MariaDB está em um contêiner Docker e o CloudBeaver em outro. A comunicação entre eles acontece por meio da rede interna do docker, utilizando o nome do serviço `mariadb` como endereço de conexão. Por isso, utilizar `'%'` permite que os usuários se conectem ao banco a partir do contêiner do CloudBeaver, enquanto `'localhost'` restringiria o acesso ao próprio ambiente do MariaDB.

## 4-Quantos autores e livros no total ficaram cadastrados na sua base após a execução da carga expandida? O que aconteceria se você tentasse inserir um livro cujo autor_id fosse 999 (um autor inexistente)? Qual regra do banco impede essa ação?
ficou com 14 autores e 33 livros cadastrados.

Se tentássemos inserir um livro utilizando o valor `999` no campo `autor_id`, considerando que não existe um autor com esse identificador, o MariaDB recusaria a operação. Isso acontece porque existe uma restrição de chave estrangeira que estabelece o relacionamento entre `livros.autor_id` e `autores.id`.

Essa regra garante a integridade referencial do banco de dados, impedindo que sejam cadastrados livros associados a autores inexistentes.

## 5-Analise as Consultas 4 e 5. Em linguagem simples, qual é a vantagem prática de dividir os dados em duas tabelas relacionadas (autores e livros) em vez de guardar o nome e o país do autor repetido dentro de cada linha da tabela de livros?
A principal vantagem de dividir os dados em duas tabelas relacionadas é evitar a repetição desnecessária de informações. Em vez de armazenar o nome e o país do autor em cada livro, essas informações ficam cadastradas uma única vez na tabela `autores`, enquanto a tabela `livros` utiliza o campo `autor_id` para identificar a qual autor cada livro pertence.

Essa organização facilita a manutenção dos dados, economiza espaço de armazenamento e evita inconsistências. Por exemplo, se o país de um autor precisar ser atualizado, basta alterar essa informação em um único registro, sem precisar modificar todos os livros associados a ele. Essa estrutura também facilita a organização e a realização de consultas utilizando relacionamentos entre tabelas.

### 1-DESAFIO
A realização desta etapa apresentou dificuldades que foram além da simples alteração da porta no arquivo `.env`. Durante a tentativa de reiniciar o serviço MariaDB para aplicar a nova configuração, ocorreu um problema relacionado ao Docker instalado via Snap e às permissões do AppArmor no Ubuntu.

A resolução exigiu bastante tempo de investigação. Foi necessário consultar documentações, pesquisar na internet e analisar mensagens de erro e registros do sistema para identificar a origem do problema. Em determinado momento, a dificuldade foi tão grande que cheguei a pensar em desistir da atividade kkkkkkk.

Apesar disso, continuei investigando e buscando compreender o que estava acontecendo, em vez de executar comandos aleatórios que poderiam comprometer os dados já armazenados no banco. Essa experiência mostrou que administrar um ambiente de banco de dados envolve não apenas conhecer SQL e Docker, mas também saber diagnosticar problemas relacionados ao sistema operacional, permissões, redes e containers.

Mesmo sendo uma etapa bastante trabalhosa, considero que a dificuldade também proporcionou um aprendizado importante sobre investigação e resolução de problemas técnicos.

### 2-DESAFIO

Para demonstrar a execução de dois ambientes independentes, foram criadas duas pastas distintas, cada uma contendo seu próprio arquivo `docker-compose.yml` e arquivo `.env`.

No primeiro ambiente, foram utilizados os contêineres `lab-mariadb-01` e `lab-cloudbeaver`, com as portas 3307 e 8978, respectivamente. No segundo ambiente, foram utilizados `lab-mariadb-02` e `lab-cloudbeaver-02`, com as portas 3308 e 8979.

A separação foi garantida por meio de nomes exclusivos para os contêineres, portas diferentes no computador e volumes independentes para armazenamento dos dados. Além disso, cada ambiente foi iniciado com um nome de projeto diferente no Docker Compose, criando redes isoladas para a comunicação entre seus serviços.

Dessa forma, foi possível manter os quatro contêineres em execução simultaneamente, sem conflitos de portas, nomes ou armazenamento. Também foi possível acessar cada instância do CloudBeaver separadamente pelo navegador, utilizando `localhost:8978` para o primeiro ambiente e `localhost:8979` para o segundo.

### 3-DESAFIO

Ao alterar o valor da variável `MARIADB_ROOT_PASSWORD` no arquivo `.env` e executar novamente o comando `docker compose up -d`, foi possível observar que a senha antiga continuou funcionando, enquanto a nova senha não foi aceita.

Isso acontece porque a imagem oficial do MariaDB utiliza a variável `MARIADB_ROOT_PASSWORD` durante a inicialização do banco de dados, quando o diretório de armazenamento ainda está vazio. Nesse momento, o MariaDB cria as estruturas internas, configura os usuários e define as credenciais iniciais.

Entretanto, como os dados são armazenados em um volume persistente, as informações de autenticação permanecem salvas mesmo quando o contêiner é recriado ou reiniciado. Assim, modificar o arquivo `.env` altera apenas a configuração fornecida ao contêiner, mas não modifica automaticamente os usuários e as senhas que já estão registrados no banco de dados.

Existem dois caminhos possíveis para aplicar uma nova senha de root:

**1. Alterar a senha diretamente no MariaDB (preservando os dados):**

A primeira alternativa é acessar o banco de dados utilizando a senha atual e executar o comando SQL `ALTER USER`, informando a nova senha. Por exemplo:

```sql
ALTER USER 'root'@'%' IDENTIFIED BY 'NOVA_SENHA';
```

Caso também seja necessário alterar a conta `root` local, pode-se executar:

```sql
ALTER USER 'root'@'localhost' IDENTIFIED BY 'NOVA_SENHA';
```

Essa alternativa modifica as credenciais diretamente no banco de dados, preservando as tabelas e os registros existentes.

**2. Remover o volume persistente e recriar o banco de dados:**

A segunda alternativa consiste em remover o volume que armazena os dados do MariaDB e iniciar novamente os contêineres. Com o volume vazio, o banco será inicializado do zero e utilizará o novo valor de `MARIADB_ROOT_PASSWORD` definido no arquivo `.env`.

Essa alternativa faz com que o banco seja recriado, mas provoca a perda dos dados armazenados no volume, caso não exista um backup.

Portanto, a persistência dos volumes é importante para preservar os dados entre reinicializações e recriações de contêineres. Ao mesmo tempo, demonstra que as variáveis de ambiente utilizadas na inicialização não substituem alterações realizadas diretamente no banco de dados.

### 4-DESAFIO

Inicialmente, ao remover o arquivo `.env` e executar `docker compose up -d`, o Compose apresentou o aviso:

```text
WARN[0000] The "MARIADB_ROOT_PASSWORD" variable is not set. Defaulting to a blank string.
```

Mesmo sem a variável definida, a execução continuou, pois ela estava sendo utilizada sem uma validação obrigatória.

Para corrigir esse comportamento, foi utilizado o modificador `:?` na declaração da variável:

```yaml
MARIADB_ROOT_PASSWORD: ${MARIADB_ROOT_PASSWORD:?A senha root precisa ser definida}
```

Esse modificador determina que a variável deve existir e possuir um valor. Caso contrário, o Docker Compose interrompe a execução e apresenta uma mensagem de erro personalizada.

Em ambientes profissionais, essa validação é importante porque impede que serviços sejam iniciados com configurações obrigatórias ausentes, especialmente credenciais e senhas. Isso aumenta a segurança, reduz erros de configuração e torna a infraestrutura mais previsível.

### 5-DESAFIO
Ao executar o comando `docker compose config`, foi possível visualizar a configuração final do ambiente Docker, com as variáveis de ambiente interpoladas a partir do arquivo `.env`.

Três variáveis identificadas foram:

- `MARIADB_ROOT_PASSWORD`: utilizada para definir a senha do usuário root do MariaDB.
- `MARIADB_DATABASE`: define o banco de dados inicial, cujo valor resolvido foi `labdb`.
- `MARIADB_PORT`: define a porta de acesso ao MariaDB pelo computador, cujo valor resolvido foi `3307`.

Também foi identificada a variável `CLOUDBEAVER_PORT`, resolvida para `8978`.

Esse comando permite verificar se as variáveis foram corretamente carregadas e se a configuração do Docker Compose está sendo interpretada como esperado.

### 6-DESAFIO
**Comando SQL utilizado:**

```sql
CREATE TABLE emprestimos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    livro_id INT,
    data_emprestimo DATE,
    devolvido BOOLEAN,
    FOREIGN KEY (livro_id) REFERENCES livros(id)
);
```

**Verificação da criação:**

```sql
SHOW TABLES;
```

**Descrição:** A tabela `emprestimos` foi criada para registrar os empréstimos de livros. O campo `id` é a chave primária, enquanto `livro_id` estabelece uma chave estrangeira que relaciona cada empréstimo a um registro da tabela `livros`. Os demais campos armazenam a data do empréstimo e o estado de devolução.
### 7-DESAFIO 
Para realizar a carga da tabela `emprestimos`, foram inseridos três registros utilizando o comando `INSERT INTO`. Dois registros foram cadastrados com o status `FALSE`, indicando que os livros ainda não foram devolvidos, enquanto o terceiro foi cadastrado com o status `TRUE`, indicando que o empréstimo já foi finalizado.

**Comando SQL utilizado:**

```sql
INSERT INTO emprestimos (livro_id, data_emprestimo, devolvido)
VALUES
    (1, '2026-10-20', FALSE),
    (2, '2026-10-22', FALSE),
    (3, '2026-10-25', TRUE);
```

O comando permitiu inserir os
### 8-DESAFIO
Para consultar os empréstimos pendentes, foi utilizada uma instrução `SELECT` com dois relacionamentos (`INNER JOIN`) entre as tabelas `emprestimos`, `livros` e `autores`. O filtro `WHERE e.devolvido = FALSE` permite exibir somente os empréstimos cujos livros ainda não foram devolvidos.

**Comando SQL utilizado:**

```sql
SELECT
    l.titulo AS livro,
    e.data_emprestimo,
    a.nome AS autor
FROM emprestimos e
INNER JOIN livros l ON e.livro_id = l.id
INNER JOIN autores a ON l.autor_id = a.id
WHERE e.devolvido = FALSE;
```

A consulta retorna o título do livro, a data em que foi emprestado e o nome do respectivo autor.
### 9-DESAFIO
Para identificar os autores que possuem mais de um livro cadastrado, foi utilizada uma consulta com `INNER JOIN`, `GROUP BY` e `HAVING`. A função `COUNT()` realiza a contagem de obras por autor, enquanto o `HAVING COUNT(*) > 1` filtra os resultados, exibindo somente aqueles que possuem mais de um livro.

**Comando SQL utilizado:**

```sql
SELECT
    a.nome AS autor,
    COUNT(l.id) AS total_livros
FROM autores a
INNER JOIN livros l ON a.id = l.autor_id
GROUP BY a.id, a.nome
HAVING COUNT(*) > 1;
```

A consulta retorna o nome de cada autor e a quantidade de livros cadastrados em seu nome.

### 10-DESAFIO
Para realizar o reajuste de 10% no preço de um livro específico, foi utilizado o comando `UPDATE`, multiplicando o valor atual por `1.10`. A condição `WHERE` foi utilizada para garantir que somente o livro selecionado fosse alterado.

**Comando SQL utilizado:**

```sql
UPDATE livros
SET preco = preco * 1.10
WHERE id = 1;
```

**Resultado:** O preço do livro de ID 1 foi reajustado em 10%, mantendo os demais registros da tabela sem alterações.
### 11-DESAFIO
Inicialmente, foi cadastrado um novo autor na tabela `autores`, sem associá-lo a nenhum livro. Em seguida, foi executado o comando `DELETE` para remover o registro recém-criado.

**Comandos SQL utilizados:**

```sql
INSERT INTO autores (nome, pais, ano_nascimento)
VALUES ('Autor Teste', 'Brasil', 1990);

DELETE FROM autores
WHERE id = LAST_INSERT_ID();
```

**Resultado:** A exclusão foi realizada com sucesso, pois o autor não possuía livros associados na tabela `livros`. Dessa forma, não havia registros dependentes que impedissem a remoção, respeitando a restrição de chave estrangeira.
### 12-DESAFIO
Foi criado o usuário `relatorios` no MariaDB e concedida a permissão `SELECT` exclusivamente sobre a tabela `livros`, pertencente ao banco de dados `biblioteca`.

**Comandos SQL utilizados:**

```sql
CREATE USER 'relatorios'@'localhost'
IDENTIFIED BY 'Relatorios2026!';

GRANT SELECT ON biblioteca.livros
TO 'relatorios'@'localhost';

SHOW GRANTS FOR 'relatorios'@'localhost';
```

**Resultado:** O usuário foi criado com permissão para consultar os registros da tabela `livros`, sem receber autorização para consultar outras tabelas ou modificar os dados do banco.
### 13-DESAFIO
Para verificar as restrições de acesso, foi realizada uma conexão utilizando o usuário `relatorios`. Em seguida, foi executada uma consulta na tabela `autores`.

**Comando SQL utilizado:**

```sql
SELECT * FROM biblioteca.autores;
```

**Mensagem de erro:**

```text
ERROR 1142 (42000): SELECT command denied to user
'relatorios' for table 'autores'
```

**Resultado:** O acesso foi negado porque o usuário `relatorios` possui permissão de consulta (`SELECT`) exclusivamente sobre a tabela `livros`. Como não foi concedida permissão para consultar a tabela `autores`, o MariaDB bloqueou a operação, respeitando as restrições de privilégios configuradas.
### 14-DESAFIO
Inicialmente, foi concedida ao usuário `relatorios` a permissão de `INSERT` na tabela `livros`, por meio do comando `GRANT`. Após essa concessão, foi realizada uma inserção de teste, executada com sucesso.

Em seguida, o privilégio foi removido utilizando o comando `REVOKE`. Ao tentar realizar uma nova inserção, o MariaDB bloqueou a operação devido à ausência de autorização.

**Comandos SQL utilizados:**

```sql
-- Concessão do privilégio
GRANT INSERT ON biblioteca.livros
TO 'relatorios'@'%';

-- Inserção de teste
INSERT INTO biblioteca.livros
    (titulo, ano_publicacao, preco, autor_id)
VALUES
    ('Livro de teste - INSERT', 2026, 19.90, NULL);

-- Revogação do privilégio
REVOKE INSERT ON biblioteca.livros
FROM 'relatorios'@'%';
```

**Resultado:** O teste demonstrou que os privilégios de acesso podem ser concedidos e revogados dinamicamente. Após a revogação, o usuário continuou podendo consultar os registros da tabela `livros`, devido à permissão `SELECT` mantida anteriormente, mas perdeu a autorização para inserir novos registros.

## Questão A – Uso do usuário root em aplicações comerciais

Uma aplicação comercial nunca deve utilizar o usuário `root` para se conectar ao banco de dados, pois essa conta possui privilégios administrativos e acesso praticamente irrestrito às estruturas e aos dados. O correto é utilizar uma conta específica para a aplicação, com permissões limitadas às operações necessárias. Caso suas credenciais sejam vazadas, um invasor poderá acessar, modificar ou excluir dados, remover tabelas e até comprometer toda a estrutura do banco de dados, causando perda de informações e prejuízos à organização.

## Questão B – Diferença entre privilégios DDL e DML

Os privilégios DDL estão relacionados à definição e alteração das estruturas do banco de dados, incluindo a criação, modificação e exclusão de tabelas. Já os privilégios DML permitem manipular os dados armazenados nessas estruturas, por meio de operações como inserção, atualização e exclusão de registros. Separar esses privilégios em contas distintas é uma boa prática de segurança, pois impede que usuários responsáveis pela manipulação dos dados realizem alterações estruturais indevidas, reduzindo os riscos de danos ao banco.

## Questão C – Diferença entre .env e .env.example

O arquivo `.env.example` deve ser versionado porque funciona como um modelo de configuração, apresentando as variáveis necessárias para executar o projeto, mas sem conter credenciais reais. Já o arquivo `.env` armazena informações sensíveis, como senhas e dados de acesso, por isso deve ser incluído no `.gitignore` e mantido fora do repositório. Caso credenciais reais sejam publicadas em um repositório público no GitHub, pessoas não autorizadas poderão utilizá-las para acessar serviços, bancos de dados e outros recursos, causando vazamento de informações, alterações indevidas e prejuízos financeiros.

## Questão D – Limitações de segurança do arquivo .env

A utilização do arquivo `.env` e sua inclusão no `.gitignore` ajudam a reduzir os riscos de exposição de credenciais, mas não eliminam completamente as ameaças de segurança. Isso ocorre porque o arquivo permanece armazenado em texto puro no sistema de arquivos do servidor, podendo ser acessado por pessoas ou processos que tenham permissões suficientes. Portanto, é necessário adotar outras medidas, como restringir as permissões de acesso ao arquivo, proteger o servidor, utilizar mecanismos de gerenciamento de segredos e realizar a troca periódica das credenciais quando necessário.

## Questão E – Contêineres e vantagens do Docker

Um contêiner é uma unidade isolada de execução que reúne uma aplicação e suas dependências, utilizando os recursos do sistema operacional hospedeiro. O Docker permite criar e administrar esses ambientes de maneira prática e padronizada. Em atividades didáticas de graduação, sua utilização facilita a instalação e configuração de bancos de dados, evita conflitos com outros programas instalados no computador e permite que todos os alunos trabalhem com ambientes semelhantes. Além disso, os contêineres podem ser iniciados, interrompidos e recriados facilmente, tornando o processo de aprendizagem, testes e desenvolvimento mais organizado e reproduzível.