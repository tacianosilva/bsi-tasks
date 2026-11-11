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