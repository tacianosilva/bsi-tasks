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

### Pergunta Discursiva 4: povoamento com IA e integridade referencial
 
Depois da carga expandida, a base ficou com **14 autores e 30 livros** (4 autores e 5 livros da carga mínima, mais 10 autores e 25 livros do povoamento). A contagem foi conferida com `SELECT COUNT(*)` em cada tabela.
 
Gerei os dados com uma ferramenta de IA generativa, usando o prompt do enunciado, e **revisei o resultado antes de executar**. A primeira versão gerada tinha inconsistências:
 
- repetia autores que já existiam nos IDs 1 a 4 (Machado de Assis, Clarice Lispector, Gabriel García Márquez e Jane Austen);
- associava livros ao autor errado, por exemplo "O Pequeno Príncipe" e "A Arte da Guerra" ligados ao ID 1 (Machado de Assis) e "Dom Quixote" ligado ao ID 2 (Clarice Lispector);
- repetia livros da carga mínima.
Esse script **não foi executado**. A versão corrigida (autores distintos e cada livro ligado ao autor correto), também feita com auxílio de IA e revisada por mim, é a que está em `povoamento.sql`. Esse tipo de erro é de significado e não de estrutura, então o banco não o detectaria: a chave estrangeira aceitaria um livro ligado ao autor errado, desde que o ID existisse.
 
Ao tentar inserir um livro com `autor_id = 999` (autor inexistente), o MariaDB recusou:
 
```
SQL Error [1452] [23000]: (conn=11) Cannot add or update a child row: a foreign key constraint fails (`biblioteca`.`livros`, CONSTRAINT `livros_ibfk_1` FOREIGN KEY (`autor_id`) REFERENCES `autores` (`id`))
```
 
A regra que impede a ação é a **restrição de chave estrangeira** `livros_ibfk_1` (`FOREIGN KEY (autor_id) REFERENCES autores(id)`), que garante a integridade referencial: um livro só pode apontar para um autor que exista na tabela `autores`.
 
### Pergunta Discursiva 5: vantagem de separar `autores` e `livros`
 
Na Consulta 4 (`JOIN`), o título do livro vem da tabela `livros` e o nome do autor vem de `autores`, e o resultado retornou 30 linhas, uma por livro. Na Consulta 5 (`GROUP BY` e `AVG`), os livros foram agrupados por autor e o resultado retornou 14 linhas, uma por autor (por exemplo, Machado de Assis com preço médio de 40.425).
 
Se o nome e o país do autor ficassem repetidos em cada linha de `livros`, "Machado de Assis" apareceria quatro vezes só com os dados que tenho. Isso traria três problemas: desperdício de espaço, risco de inconsistência (o mesmo autor escrito de formas diferentes, o que quebraria o agrupamento da Consulta 5) e dificuldade de manutenção, já que corrigir um dado do autor exigiria alterar várias linhas. Com duas tabelas, o dado do autor existe **uma única vez**, qualquer correção é feita em um só lugar, e o `JOIN` reconstrói a visão completa quando necessário.
 
---
 
 ## 3. Respostas Dissertativas Conceituais
 
### Questão a: por que a aplicação nunca deve usar o usuário `root`
 
O `root` tem poder total sobre o servidor: pode ler e alterar qualquer banco, apagar tabelas e bancos inteiros, criar e remover usuários e alterar privilégios. Uma aplicação comercial só precisa operar sobre os dados do próprio banco, então dar a ela `root` concede muito mais poder do que o necessário.
 
Se as credenciais da aplicação vazarem, o impacto depende dessa conta. Com `root`, o invasor controla o servidor de banco inteiro: pode copiar todos os dados, apagá-los, criar contas para manter acesso e atingir outros bancos do mesmo servidor. Com uma conta restrita como `app_biblioteca`, o dano fica limitado aos dados daquele banco, e, como mostrei no erro 1142, ela não consegue apagar tabelas.
 
### Questão b: privilégios DDL x DML e por que separá-los
 
Privilégios DDL permitem alterar a **estrutura** do banco (`CREATE`, `ALTER`, `DROP`). Privilégios DML permitem trabalhar com o **conteúdo** das tabelas (`SELECT`, `INSERT`, `UPDATE`, `DELETE`). A aplicação no dia a dia só precisa de DML.
 
Separar em contas distintas é boa prática porque limita o dano de erros e ataques: uma falha na aplicação ou uma credencial vazada não consegue destruir ou modificar a estrutura do banco. Mudanças estruturais ficam com uma conta administrativa, usada em momentos controlados e por pessoas responsáveis. Neste laboratório isso ficou demonstrado com `app_biblioteca` (DML), `consulta` (somente `SELECT`) e `root` (administração).
 
### Questão c: `.env.example` x `.env` e os riscos de commitar credenciais
 
O `.env.example` é o modelo de configuração: lista as variáveis de que o projeto precisa, com valores genéricos (como `troque_por_uma_senha_forte`), e por isso deve ser versionado, pois documenta o contrato de configuração e permite que qualquer pessoa monte o próprio `.env`. O `.env` contém os valores reais (senhas) e nunca deve ser versionado.
 
Commitar credenciais reais em um repositório público é grave. Robôs varrem o GitHub em busca de segredos e os encontram muito rápido. Além disso, o histórico do Git guarda o conteúdo antigo: apagar o arquivo depois não remove a senha dos commits anteriores. As consequências práticas incluem acesso indevido ao banco, vazamento ou destruição de dados e a obrigação de trocar todas as credenciais expostas.
 
### Questão d: `.env` + `.gitignore` eliminam todos os riscos?
 
Não. Essa prática evita apenas o vazamento das credenciais **por meio do repositório**. O arquivo continua gravado em texto puro no sistema de arquivos, e qualquer pessoa ou processo com acesso ao disco, a um backup ou ao contêiner comprometido pode ler as senhas. Há ainda outros caminhos de exposição: as variáveis aparecem em `docker compose config`, como se vê nas saídas deste relatório, e podem ser vistas em inspeções do contêiner (`docker inspect`).
 
Em ambientes reais usam-se complementos: gerenciadores de segredos (Docker secrets, HashiCorp Vault, cofres de provedores de nuvem), permissões restritas no arquivo, rotação periódica de senhas e privilégio mínimo para cada conta.
 
### Questão e: o que é um contêiner e vantagens do Docker no ensino
 
Um contêiner é um processo isolado que empacota uma aplicação com as bibliotecas e dependências de que precisa, compartilhando o kernel do sistema operacional hospedeiro. Por isso é mais leve e rápido de iniciar que uma máquina virtual completa.
 
Para atividades didáticas de banco de dados, as vantagens sobre instalar o SGBD diretamente no computador são:
 
- **Ambiente igual para todos:** o mesmo `docker-compose.yml` gera o mesmo ambiente em qualquer máquina.
- **Instalação rápida e sem poluir o sistema:** não há instalador nem serviço residente.
- **Fácil de destruir e recriar do zero** (`docker compose down -v`).
- **Várias versões ou ambientes lado a lado:** no Desafio 2 rodei dois ambientes completos ao mesmo tempo.
- **Reprodutibilidade:** toda a infraestrutura está descrita em arquivos versionáveis.
- **Isolamento de conflitos:** se há um MySQL local na porta 3306, basta mudar a porta publicada.

---
 
 ## 4. Desafios Realizados
 
### Bloco A: Docker e Infraestrutura
 
#### Desafio 1: alteração de porta do SGBD
 
No `.env` alterei `MARIADB_PORT=3307` e reiniciei o serviço:
 
```
PS> docker compose up -d
[+] up 2/2
 ✔ Container lab-cloudbeaver Running
 ✔ Container lab-mariadb     Started
 
PS> docker ps
CONTAINER ID   IMAGE                        COMMAND                 CREATED          STATUS          PORTS                                         NAMES
7bb64069a40b   mariadb:11                   "docker-entrypoint.s…"  13 seconds ago   Up 11 seconds   0.0.0.0:3307->3306/tcp, [::]:3307->3306/tcp   lab-mariadb
2711348678ab   dbeaver/cloudbeaver:latest   "./launch-product.sh"   5 hours ago      Up 5 hours      0.0.0.0:8978->8978/tcp, [::]:8978->8978/tcp   lab-cloudbeaver
```
 
A porta publicada do MariaDB passou a ser `3307->3306`.
 
**Reconfiguração do CloudBeaver:** a conexão do CloudBeaver **não precisou ser alterada**. Ele acessa o MariaDB pela rede interna do Docker, usando o nome do serviço e a porta interna (`mariadb:3306`), que não mudou. A variável `MARIADB_PORT` altera apenas o lado do **host** no mapeamento `"${MARIADB_PORT:-3306}:3306"`. A porta 3307 só é usada por clientes que estão fora do Docker, como um DBeaver instalado no Windows, que usaria `localhost:3307`. Após a mudança, testei a conexão no CloudBeaver (host `mariadb`, porta `3306`) e ela continuou funcionando normalmente, o que confirma essa explicação.
 
#### Desafio 2: dois ambientes simultâneos
 
Copiei a pasta `tarefa03` para `tarefa03-b` e, no ambiente B, usei portas e nomes diferentes (`MARIADB_PORT=3307`, `CLOUDBEAVER_PORT=8979` e nomes de contêiner `lab2-mariadb` e `lab2-cloudbeaver`). Em cada pasta executei `docker compose up -d`:
 
```
PS> docker compose up -d        (dentro de tarefa03-b)
[+] up 4/4
 ✔ Network tarefa03-b_default     Created
 ✔ Volume tarefa03-b_mariadb_data Created
 ✔ Container lab2-mariadb         Started
 ✔ Container lab2-cloudbeaver     Started
 
PS> docker ps
CONTAINER ID   IMAGE                        COMMAND                 CREATED          STATUS          PORTS                                         NAMES
9de45c2a5e17   dbeaver/cloudbeaver:latest   "./launch-product.sh"   17 seconds ago   Up 16 seconds   0.0.0.0:8979->8978/tcp, [::]:8979->8978/tcp   lab2-cloudbeaver
844bd02acd55   mariadb:11                   "docker-entrypoint.s…"  17 seconds ago   Up 16 seconds   0.0.0.0:3307->3306/tcp, [::]:3307->3306/tcp   lab2-mariadb
5e570cad87a8   mariadb:11                   "docker-entrypoint.s…"  5 minutes ago    Up 5 minutes    0.0.0.0:3306->3306/tcp, [::]:3306->3306/tcp   lab-mariadb
2711348678ab   dbeaver/cloudbeaver:latest   "./launch-product.sh"   5 hours ago      Up 5 hours      0.0.0.0:8978->8978/tcp, [::]:8978->8978/tcp   lab-cloudbeaver
```
 
**Como evitei conflitos entre os quatro contêineres:**
 
1. **Portas do host:** o ambiente A usa 3306 e 8978, e o B usa 3307 e 8979. Duas aplicações não podem ocupar a mesma porta do host.
2. **Nomes dos contêineres:** `container_name` precisa ser único no Docker, então o ambiente B usa `lab2-mariadb` e `lab2-cloudbeaver`.
3. **Redes e volumes:** o Compose prefixa esses recursos com o nome do projeto (a pasta), gerando `tarefa03-b_default` e `tarefa03-b_mariadb_data`. Assim os dados e a rede do ambiente B ficam separados dos do A.
As portas internas (3306 e 8978) são iguais nos dois ambientes sem problema, pois cada contêiner tem a sua própria rede isolada.
 
#### Desafio 3: persistência do volume e alteração da senha de root
 
Alterei `MARIADB_ROOT_PASSWORD` no `.env` para `NovaSenha2026!` e executei `docker compose up -d`. Em seguida testei as duas senhas:
 
```
PS> docker compose up -d
 ✔ Container lab-mariadb     Running
 ✔ Container lab-cloudbeaver Running
 
PS> docker exec -it lab-mariadb mariadb -uroot -p'RootLab2026!aB' -e "SELECT 1;"
+---+
| 1 |
+---+
| 1 |
+---+
 
PS> docker exec -it lab-mariadb mariadb -uroot -p'NovaSenha2026!' -e "SELECT 1;"
ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)
```
 
A senha antiga continuou válida e a nova foi recusada.
 
**Por que isso ocorre:** a variável `MARIADB_ROOT_PASSWORD` só é lida pelo script de entrypoint da imagem na **primeira inicialização** do diretório de dados. Nesse momento a senha é gravada nos dados do MariaDB, dentro do volume `mariadb_data`. Nas execuções seguintes, o volume já está inicializado, então o MariaDB reaproveita os dados (e a senha antiga) e ignora o valor novo do `.env`. O `.env` apenas alimenta o contêiner, e a senha real vive dentro do banco.
 
**Dois caminhos para aplicar uma nova senha de root:**
 
1. **Recriar o volume** com `docker compose down -v` seguido de `docker compose up -d`. A nova senha do `.env` é aplicada na criação, mas **todos os dados são perdidos**.
2. **Alterar a senha dentro do banco**, sem perder dados, conectado com a senha antiga:
```sql
ALTER USER 'root'@'%' IDENTIFIED BY 'NovaSenha2026!';
ALTER USER 'root'@'localhost' IDENTIFIED BY 'NovaSenha2026!';
FLUSH PRIVILEGES;
```
 
Executei o caminho 2 como root: o `ALTER USER` foi aceito, a nova senha passou a ser válida e a antiga deixou de funcionar. Depois disso é preciso manter o `.env` e a conexão do CloudBeaver coerentes com a senha real, e foi o que fiz. Ao final, voltei root para a senha original do laboratório, e as demais etapas seguiram com ela.
 
#### Desafio 4: validação estrita `:?`
 
Renomeei o `.env` para `.env.bak` e executei o Compose:
 
```
PS> mv .env .env.bak
PS> docker compose up -d
error while interpolating services.mariadb.environment.MARIADB_ROOT_PASSWORD: required variable MARIADB_ROOT_PASSWORD is missing a value: defina MARIADB_ROOT_PASSWORD no arquivo .env
```
 
O Compose abortou antes de criar qualquer contêiner. O modificador `:?` faz a execução **falhar cedo e com uma mensagem clara** quando a variável está ausente ou vazia. Em ambientes profissionais isso é importante porque impede a subida de um banco sem senha (inseguro) ou com configuração incompleta, evita falhas obscuras mais tarde e acelera o diagnóstico, já que a mensagem diz exatamente o que corrigir. O `.env` foi restaurado depois do teste.
 
#### Desafio 5: inspeção com `docker compose config`
 
Saída resumida do comando (valores já resolvidos a partir do `.env`):
 
```
services:
  mariadb:
    container_name: lab-mariadb
    environment:
      MARIADB_DATABASE: labdb
      MARIADB_ROOT_PASSWORD: RootLab2026!aB
    image: mariadb:11
    ports:
      - mode: ingress
        target: 3306
        published: "3306"
        protocol: tcp
```
 
Três variáveis interpoladas a partir do `.env`:
 
1. `MARIADB_ROOT_PASSWORD: RootLab2026!aB`
2. `MARIADB_DATABASE: labdb`
3. A porta publicada do MariaDB, `published: "3306"` (de `MARIADB_PORT`). No CloudBeaver, a porta publicada `"8978"` vem de `CLOUDBEAVER_PORT`.
A senha acima é a senha de laboratório fornecida no próprio enunciado da tarefa.
 
---
 