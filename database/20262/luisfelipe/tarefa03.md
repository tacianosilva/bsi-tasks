# Tarefa 03 — Docker e SGBD Relacional

## 1. Identificação e Repositório

**Discente:** Luis Felipe Linhares Pereira  
**Usuário no GitHub:** luisfelipelinhares
**E-mail acadêmico:** luis.felipe.linhares.701@ufrn.edu.br  
**Disciplina:** Banco de Dados  
**SGBD utilizado:** MariaDB 11  
**Ferramentas:** Docker, Docker Compose e CloudBeaver.

**Repositório pessoal no GitHub:**

https://github.com/Luisfelipelinhares/-Tarefa-03---Docker-e-SGBD---luisfelipelinhares-

O repositório contém os arquivos necessários para a configuração e execução do ambiente:

- `docker-compose.yml`: define os serviços e configurações dos contêineres.
- `.env.example`: apresenta um modelo das variáveis de ambiente necessárias.
- `.gitignore`: impede que arquivos sensíveis sejam enviados ao GitHub.
- `povoamento.sql`: contém os comandos de inserção dos dados.
- `setup.sql`: contém os comandos iniciais de configuração do banco de dados.
- `README.md`: apresenta as orientações para instalação e execução do ambiente.

---

## 2. Respostas às Perguntas Discursivas dos Passos Práticos

### Pergunta Discursiva 1 — Diferença entre DDL e DML

DDL (Data Definition Language) é a linguagem utilizada para definir e modificar a estrutura do banco de dados. Seus principais comandos são `CREATE`, `ALTER` e `DROP`.

Já DML (Data Manipulation Language) é utilizada para manipular os registros armazenados nas tabelas, por meio de comandos como `INSERT`, `UPDATE` e `DELETE`.

A execução de um comando `DROP TABLE` provoca a exclusão completa da tabela, incluindo sua estrutura e todos os registros armazenados. Diferentemente de um `DELETE`, que remove registros sem necessariamente eliminar a tabela, o `DROP TABLE` remove o próprio objeto do banco de dados.

### Pergunta Discursiva 2 — Erro 1142 e princípio do menor privilégio

O erro 1142 ocorre quando um usuário tenta executar uma operação para a qual não possui autorização. No caso de um `DROP TABLE`, significa que a conta utilizada não possui o privilégio necessário para excluir tabelas.

Essa situação está relacionada ao princípio do menor privilégio, que determina que cada usuário deve possuir somente as permissões necessárias para realizar suas atividades.

Essa prática aumenta a segurança do banco de dados, pois impede que usuários com permissões limitadas executem operações administrativas ou destrutivas. Assim, mesmo que uma conta seja comprometida, os danos ficam limitados às permissões que ela possui.

### Pergunta Discursiva 3 — Utilização do host '%'

Na arquitetura conteinerizada do Docker, os serviços executam em contêineres diferentes, cada um possuindo seu próprio ambiente de rede.

Por esse motivo, utilizar `'localhost'` na criação de um usuário do MariaDB pode impedir a conexão de aplicações que estejam em outros contêineres, pois esse endereço representa a própria máquina ou contêiner em que a conexão está sendo realizada.

A utilização de `'%'` permite que o usuário se conecte a partir de diferentes endereços de origem, incluindo outros contêineres da rede Docker.

Entretanto, essa configuração deve ser acompanhada de medidas de segurança, como senhas fortes, permissões restritas e controle da exposição das portas do banco de dados.

### Pergunta Discursiva 4 — Povoamento expandido e integridade referencial

Para expandir o banco de dados, foram elaborados comandos SQL com auxílio de inteligência artificial, incluindo autores de diferentes nacionalidades e períodos históricos, além de livros associados a esses autores.

O povoamento elaborado acrescenta 10 autores aos 4 registros que já existiam, totalizando 14 autores. Também foram elaborados 30 registros de livros, com títulos variados, preços decimais e anos de publicação compatíveis com a época dos respectivos autores.

A tabela `livros` possui a coluna `autor_id`, que funciona como chave estrangeira para a coluna `id` da tabela `autores`.

Caso seja realizada uma tentativa de inserir um livro associado a um autor inexistente, o MariaDB retorna um erro de chave estrangeira, impedindo a operação.

Isso acontece porque a integridade referencial garante que os relacionamentos entre as tabelas sejam válidos, evitando registros que apontem para autores que não existem.

### Pergunta Discursiva 5 — Consultas relacionais e normalização

A utilização de duas tabelas relacionadas, `autores` e `livros`, permite organizar os dados de maneira estruturada e evitar a duplicação de informações.

A tabela `autores` armazena os dados de cada escritor, enquanto a tabela `livros` armazena os dados das obras e utiliza a chave estrangeira `autor_id` para identificar seus respectivos autores.

Com essa estrutura, é possível realizar consultas utilizando `INNER JOIN`, relacionando informações das duas tabelas.

A normalização oferece vantagens como:

- Redução da duplicidade de informações.
- Maior consistência dos dados.
- Facilidade de manutenção e atualização.
- Melhor organização do banco de dados.
- Preservação da integridade referencial.

Dessa forma, caso um autor possua vários livros, suas informações pessoais são armazenadas apenas uma vez, sendo referenciadas pelos registros correspondentes na tabela de livros.

---

## 3. Respostas Dissertativas Conceituais

### Questão A — Por que uma aplicação comercial nunca deve utilizar o usuário root?

Uma aplicação comercial nunca deve utilizar o usuário `root` para acessar o banco de dados, pois essa conta possui privilégios administrativos elevados, permitindo realizar praticamente qualquer operação, incluindo criar, alterar e excluir tabelas, bancos de dados e usuários.

O correto é criar uma conta específica para a aplicação, concedendo somente as permissões necessárias para seu funcionamento.

Caso as credenciais dessa conta sejam vazadas, um invasor poderá acessar os dados e executar operações de acordo com os privilégios concedidos. Se a aplicação utilizar uma conta administrativa, o comprometimento poderá resultar na exclusão de todo o banco de dados, alteração de informações, criação de usuários indevidos e até comprometimento de outros serviços do servidor.

Por isso, limitar os privilégios é uma medida fundamental para reduzir os riscos de segurança.

### Questão B — Diferença entre privilégios DDL e DML

Os privilégios DDL estão relacionados à definição e alteração da estrutura do banco de dados. Permitem operações como criação, modificação e exclusão de tabelas.

Já os privilégios DML permitem manipular os dados armazenados, realizando operações de inserção, consulta, atualização e exclusão de registros.

Separar essas permissões em contas diferentes é uma boa prática de segurança, pois evita que usuários responsáveis pela manipulação dos dados tenham autorização para modificar a estrutura do banco.

Por exemplo, uma aplicação pode utilizar uma conta com permissões DML para cadastrar e consultar informações, enquanto uma conta administrativa fica responsável pelas alterações estruturais.

Essa separação reduz os riscos de alterações acidentais e de ataques que possam comprometer a estrutura do banco.

### Questão C — Importância dos arquivos .env.example e .env

O arquivo `.env.example` deve ser versionado no GitHub porque apresenta um modelo das variáveis de ambiente necessárias para configurar o projeto, sem expor informações confidenciais.

Já o arquivo `.env` contém os valores reais dessas variáveis, como senhas, usuários e outras credenciais de acesso. Por isso, ele deve ser incluído no `.gitignore`, impedindo seu envio acidental ao repositório.

Caso credenciais reais sejam publicadas em um repositório público, qualquer pessoa poderá ter acesso a elas e tentar utilizá-las para acessar o banco de dados ou outros serviços.

As consequências podem incluir roubo de informações, exclusão de registros, alteração de dados e comprometimento da infraestrutura.

Mesmo que o arquivo seja removido posteriormente, as credenciais podem permanecer disponíveis no histórico de commits. Portanto, quando ocorre um vazamento, é necessário revogar ou substituir imediatamente as credenciais comprometidas.

### Questão D — O uso do .env e do .gitignore elimina todos os riscos?

Não. A utilização do arquivo `.env` e sua inclusão no `.gitignore` são medidas importantes, mas não eliminam completamente os riscos de segurança.

O arquivo `.env` permanece armazenado em texto puro no sistema de arquivos do computador ou servidor. Isso significa que pessoas ou processos que consigam acessar esse arquivo poderão visualizar as credenciais armazenadas nele.

Além disso, podem ocorrer vazamentos por meio de backups desprotegidos, permissões inadequadas, compartilhamento indevido de arquivos ou comprometimento do próprio servidor.

Para aumentar a segurança, é importante restringir as permissões de acesso aos arquivos, utilizar senhas fortes, evitar compartilhar credenciais e adotar mecanismos de gerenciamento de segredos em ambientes de produção.

Portanto, o `.env` e o `.gitignore` reduzem determinados riscos, mas precisam fazer parte de uma estratégia de segurança mais ampla.

### Questão E — O que é um contêiner e quais são as vantagens do Docker?

Um contêiner é uma unidade isolada de execução que reúne uma aplicação e suas dependências necessárias para funcionar. Ele utiliza recursos do sistema operacional hospedeiro, mas mantém seu próprio ambiente isolado.

O Docker permite criar, executar e gerenciar esses contêineres de maneira prática e padronizada.

Em atividades didáticas de graduação, utilizar o Docker para provisionar um banco de dados apresenta diversas vantagens em comparação com a instalação manual do SGBD diretamente no sistema operacional.

Entre as principais vantagens estão:

- **Facilidade de instalação:** não é necessário realizar toda a configuração manual do MariaDB no computador.
- **Padronização:** todos os alunos podem utilizar o mesmo ambiente e a mesma versão do SGBD.
- **Isolamento:** o banco de dados funciona em um ambiente separado do sistema operacional.
- **Portabilidade:** o ambiente pode ser reproduzido em diferentes computadores.
- **Facilidade de manutenção:** os contêineres podem ser interrompidos, removidos e recriados.
- **Organização:** o Docker Compose permite definir vários serviços em um único arquivo de configuração.

Assim, o Docker facilita o desenvolvimento e o aprendizado, reduzindo problemas relacionados a diferenças de configuração entre os computadores dos alunos.

---

## 4. Desafios Realizados

### Bloco A — Configuração do ambiente Docker

O primeiro desafio consistiu em configurar o ambiente de banco de dados utilizando Docker Compose.

Foi utilizado o arquivo `docker-compose.yml` para definir dois serviços principais:

- MariaDB 11, responsável pelo gerenciamento do banco de dados.
- CloudBeaver, utilizado como interface gráfica para acessar e administrar o banco.

Também foram utilizados volumes para persistência dos dados e variáveis de ambiente para configurar as credenciais.

**Comando utilizado no terminal:**

```powershell
docker compose up -d
```

Inicialmente, ocorreu um erro:

```text
no configuration file provided: not found
```

O problema aconteceu porque o comando foi executado em um diretório acima da pasta que continha o arquivo `docker-compose.yml`.

Após acessar a pasta correta, identificada como `Tarefa-03`, o comando foi executado novamente e os serviços foram iniciados.

**Resultado obtido:**

- Imagem `mariadb:11` baixada.
- Imagem `dbeaver/cloudbeaver:latest` baixada.
- Volume `tarefa-03_mariadb_data` criado.
- Contêiner `lab-mariadb` iniciado.
- Contêiner `lab-cloudbeaver` iniciado.
- Porta `3306` disponibilizada para o MariaDB.
- Porta `8978` disponibilizada para o CloudBeaver.

O ambiente foi iniciado com sucesso, permitindo a utilização do banco de dados por meio dos contêineres.

### Bloco B — Configuração e segurança do banco de dados

O segundo desafio envolveu a configuração inicial do banco de dados e o gerenciamento de usuários e permissões.

O arquivo `setup.sql` foi utilizado para organizar os comandos de configuração inicial.

Também foram trabalhados conceitos de segurança, principalmente a separação entre usuários administrativos e usuários com permissões limitadas.

A utilização de contas distintas permite controlar quais operações cada usuário pode executar, evitando que uma conta destinada à manipulação de dados tenha privilégios administrativos desnecessários.

**Exemplos de comandos SQL relacionados ao gerenciamento de permissões:**

```sql
-- Criar um usuário para a aplicação
CREATE USER 'app_user'@'%'
IDENTIFIED BY 'SENHA_FORTE';

-- Conceder permissões de manipulação de dados
GRANT SELECT, INSERT, UPDATE, DELETE
ON biblioteca.*
TO 'app_user'@'%';

-- Atualizar os privilégios
FLUSH PRIVILEGES;
```

Os comandos acima ilustram a separação de privilégios e devem corresponder às configurações efetivamente utilizadas no arquivo `setup.sql`.

### Bloco C — Povoamento e consultas relacionais

O terceiro desafio envolveu a criação e manipulação dos dados do banco de dados.

Foram utilizadas as tabelas `autores` e `livros`, relacionadas por meio de uma chave primária e uma chave estrangeira.

A estrutura permite cadastrar diversos autores e associar diferentes livros a cada um deles.

**Exemplo de inserção de autores:**

```sql
INSERT INTO autores (nome, pais, ano_nascimento) VALUES
('William Shakespeare', 'Inglaterra', 1564),
('Machado de Assis', 'Brasil', 1839),
('Jane Austen', 'Inglaterra', 1775),
('Franz Kafka', 'República Tcheca', 1883),
('Gabriel García Márquez', 'Colômbia', 1927);
```

**Exemplo de inserção de livros:**

```sql
INSERT INTO livros
(titulo, ano_publicacao, preco, autor_id)
VALUES
('Romeu e Julieta', 1597, 29.90, 5),
('Hamlet', 1603, 34.90, 5),
('Quincas Borba', 1891, 39.90, 6),
('Orgulho e Preconceito', 1813, 44.90, 7),
('A Metamorfose', 1915, 34.90, 8);
```

O povoamento expandido elaborado com auxílio de inteligência artificial acrescentou 10 autores aos 4 previamente cadastrados e gerou 30 livros associados aos autores de IDs 1 a 14.

**Consulta para visualizar os autores cadastrados:**

```sql
SELECT * FROM autores;
```

**Consulta para visualizar os livros cadastrados:**

```sql
SELECT * FROM livros;
```

**Consulta relacional utilizando INNER JOIN:**

```sql
SELECT
    livros.id,
    livros.titulo,
    livros.ano_publicacao,
    livros.preco,
    autores.nome AS autor,
    autores.pais
FROM livros
INNER JOIN autores
    ON livros.autor_id = autores.id;
```

Essa consulta permite visualizar os livros juntamente com os nomes e países de seus respectivos autores, demonstrando o funcionamento do relacionamento entre as tabelas.

**Consulta para identificar a quantidade de livros por autor:**

```sql
SELECT
    autores.nome,
    COUNT(livros.id) AS quantidade_livros
FROM autores
LEFT JOIN livros
    ON autores.id = livros.autor_id
GROUP BY autores.id, autores.nome;
```

A utilização de `LEFT JOIN` permite apresentar todos os autores, inclusive aqueles que ainda não possuem livros cadastrados.
S