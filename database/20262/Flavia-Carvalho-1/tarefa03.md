# Tarefa 03 - Docker e SGBD
 
**Disciplina:** DCT2201 - Banco de Dados | **Curso:** Sistemas de Informação - CERES/UFRN
 
---
 
## 1. Identificação e Repositório
 
- **Nome completo:** Flávia Juliana Araújo de Carvalho
- **Usuário no GitHub:** Flavia-Carvalho-1
- **E-mail acadêmico:** flavia.carvalho.124@ufrn.edu.br
- **Repositório pessoal público:** [dct2201-banco-de-dados (README.md)](https://github.com/Flavia-Carvalho-1/dct2201-banco-de-dados/blob/0678540454252b2874592d62be01a9fb74aab3f0/README.md)
Arquivos de infraestrutura (no repositório pessoal, pasta `tarefa03/`): `docker-compose.yml`, `.env.example`, `povoamento.sql`, `setup.sql`. O `.gitignore` fica na raiz do repositório e impede o versionamento do `.env`.
 
**Ambiente utilizado** (saídas reais):
 
```
git version 2.53.0.windows.3
Docker version 29.9.2, build a82e528
Docker Compose version v5.6.1
```
 
Imagens: `mariadb:11` (o log mostrou MariaDB 11.8.9) e `dbeaver/cloudbeaver:latest`. Terminal utilizado: PowerShell no Windows, com Docker Desktop.
 
Verificação de que o `.env` é ignorado pelo Git:
 
```
PS> git check-ignore -v .env
.gitignore:1:.env       .env
```
 
O log do MariaDB na primeira inicialização terminou com `mariadbd: ready for connections.`, e a conexão do CloudBeaver foi feita com host `mariadb` (nome do serviço no Compose) e porta `3306`.
 
---

## 2. Perguntas Discursivas dos Passos Práticos
 
### Pergunta Discursiva 1: DDL x DML e o impacto de um `DROP TABLE`
 
DDL (Data Definition Language) é a parte da linguagem que define a estrutura onde os dados ficam guardados: `CREATE DATABASE`, `CREATE TABLE`, `ALTER`, `DROP`. Foi com DDL que criei o banco `biblioteca` e as tabelas `autores` e `livros`, definindo colunas, tipos, chave primária e chave estrangeira. DML (Data Manipulation Language) trabalha com o conteúdo dessas estruturas: `INSERT`, `SELECT`, `UPDATE` e `DELETE`. Usando a analogia da gaveta, o DDL é construir a gaveta e decidir como ela é dividida, e o DML é guardar, consultar, trocar e retirar os papéis dentro dela.
 
Se uma tabela é apagada com `DROP TABLE`, a estrutura e todos os registros que estavam nela desaparecem juntos. Não existe uma "lixeira" no SGBD: sem backup, esses dados não podem ser recuperados. Por isso `DROP` é considerado um comando destrutivo.
 
 ### Pergunta Discursiva 2: erro 1142 ao tentar `DROP TABLE` com a conta restrita
 
Criei uma conexão no CloudBeaver com o usuário `app_biblioteca` e executei `DROP TABLE autores;`. O MariaDB recusou o comando e a tabela continuou intacta. A mensagem recebida foi:
 
```
SQL Error [1142] [42000]: (conn=11) DROP command denied to user 'app_biblioteca'@'172.18.0.3' for table `biblioteca`.`autores`
```
 
A recusa aconteceu porque essa conta só recebeu privilégios de manipulação de dados. O `SHOW GRANTS` mostra isso:
 
```
-- app_biblioteca
GRANT USAGE ON *.* TO `app_biblioteca`@`%`
GRANT SELECT, INSERT, UPDATE, DELETE ON `biblioteca`.* TO `app_biblioteca`@`%`
 
-- consulta
GRANT USAGE ON *.* TO `consulta`@`%`
GRANT SELECT ON `biblioteca`.* TO `consulta`@`%`
```
 
Apagar uma tabela exige o privilégio `DROP`, que nunca foi concedido. No MariaDB tudo o que não foi concedido explicitamente é negado, e o erro 1142 é essa negação.
 
Essa restrição protege o banco se a aplicação sofrer uma invasão (por exemplo, SQL injection ou vazamento da senha) ou tiver uma falha de programação. Quem controlar a conta da aplicação conseguirá, no máximo, ler e alterar dados, mas não conseguirá apagar tabelas nem mudar a estrutura do banco. O estrago fica limitado, e isso é o princípio do menor privilégio.

### Pergunta Discursiva 3: por que o host `'%'` em vez de `'localhost'`
 
No MariaDB, uma conta é identificada pelo par `'usuario'@'host'`, e o host indica de onde a conexão pode vir. Com `'localhost'`, o servidor só aceitaria conexões originadas na própria máquina do servidor (socket UNIX ou loopback).
 
Neste laboratório quem se conecta é o CloudBeaver, que roda em **outro contêiner**. Ele chega ao MariaDB pela rede virtual criada pelo Docker Compose (`tarefa03_default`), com um endereço IP interno daquela rede. A prova está nas mensagens de erro coletadas: o MariaDB enxergou as conexões como vindas de `172.18.0.3`, e não de `localhost`. Uma conta `'app_biblioteca'@'localhost'` seria recusada nessa situação. O curinga `'%'` aceita qualquer origem, o que permite que contêineres distintos na rede interna do Docker se autentiquem.
 
Como o contêiner do CloudBeaver tem o próprio `localhost`, a conexão também precisa usar como host o nome do serviço (`mariadb`), que o Docker resolve para o IP do contêiner do banco. Em produção, convém restringir o host (por exemplo, à sub-rede da aplicação) em vez de usar `'%'`.