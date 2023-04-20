# Dicas sobre Banco de Dados

Dicas e exemplos para as disciplinas relacionadas com Banco de Dados.

## Exemplos de uso de JDBC

No diretório [JDBC](jdbc/) temos um projeto java com exemplos de conexões JDBC, usando drivers para o MariaDB e para o MySql.

## Scripts SQL

No diretório [SCRIPTS](scripts/) temos vários scripts de criação e povoamento para Base de Dados usadas nas aulas da disciplina Banco de Dados.

## Links Interessantes

* [Limitando acessos no PostgreSQL](https://ubiq.co/database-blog/how-to-limit-access-to-database-in-postgresql/)
* [Start a Remote MySQL Server with Docker quickly](https://medium.com/@backslash112/start-a-remote-mysql-server-with-docker-quickly-9fdff22d23fd)

## Instalação do Docker

O tutorial [how-to-install-and-use-docker-on-ubuntu-22-04-pt](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-22-04)) da digitalocean traz detalhes para a instalação do docker na sua máquina. Você também pode acessar o [Site Oficial do Docker](https://docs.docker.com/engine/install/ubuntu/).

Siga os passos 1 e 2 do tutorial e verifique se o daemon foi iniciado e o processo habilitado a iniciar no boot. Verifique se ele está funcionando:

```console
sudo systemctl status docker
```

## Executando container do Servidor MariaDB

Antes de executar o container, baixe a imagem do `mariadb`:
```console
docker pull mariadb
```

Para que os dados fiquem persistidos, crie um diretório para ser o volume de dados compartilhado com o container:
```console
mkdir -p $HOME/docker/volumes/mariadb
```

Agora inicie o container:
```console
docker run -d --name mariadb-server -p 3306:3306 -e "MYSQL_ROOT_PASSWORD=password" -v $HOME/docker/volumes/mariadb:/var/lib/mysql mariadb
```

### Acessando via MariaDB Cli (MySql Cli)

Se não tiver, instale o cliente de acesso ao SGBD:

```console
sudo apt install mysql-client
```

Acesse usando o `host 127.0.0.1` e o usuário `root`:

```console
mysql -h 127.0.0.1 -u root -p
```

### Acessando MariaDB via CloudBeaver (dbeaver)

Para que os dados fiquem persistidos, crie um diretório para ser o volume de dados compartilhado com o container:
```console
mkdir -p $HOME/docker/volumes/cloudbeaver
```

Antes de executar o container, baixe a imagem do `dbeaver/cloudbeaver`:
```console
docker pull dbeaver/cloudbeaver:23.0.2
```

Agora inicie o container:
```console
docker run --name cloudbeaver -d -p 8978:8978 -v $HOME/docker/volumes/cloudbeaver:/opt/cloudbeaver/workspace dbeaver/cloudbeaver:23.0.2
```

Informações aqui: [CloudBeaver - Run Docker Container](https://cloudbeaver.io/docs/Run-Docker-Container/)!

## Executando container do Servidor MySql

Antes de executar o container, baixe a imagem do `mysql`:

```console
docker pull mysql
```

Para que os dados fiquem persistidos, crie um diretório para ser o volume de dados compartilhado com o container:
```console
mkdir -p $HOME/docker/volumes/mysqldb
```

Agora inicie o container:
```console
docker run --name mysqlserver-server -d -p 3306:3306 -e "MYSQL_ROOT_PASSWORD=password" -v $HOME/docker/volumes/mysqldb:/var/lib/mysql mysql
```

### Acessando via MySql Client

Para utilizar o **MySql Client** podemos instalar diretamente no sistema ou utilizar o docker para executá-lo.

Instalando o **MySQL Client** no sistema para acesso ao SGBD:

```console
sudo apt install mysql-client
```

Acesse usando o `host 127.0.0.1` e o usuário `root`:

```console
mysql -h 127.0.0.1 -u root -p
```

:warning: Ao executar o comando acima de acesso pode surgir a mensagem de erro: <span style="color:red">ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock'`</span>. Como o servidor mysql está sendo executado em um container ele não está habilitado para o acesso via localhost (127.0.0.1).

:pushpin: Se você estiver utilizando o **MySql Server**, precisará descobrir o IP do container para poder acessar usando o cliente de linha de comando. Fonte: https://www.baeldung.com/docker-cant-connect-local-mysql

```console
docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mysql-server
```
Retornará um ou mais IPs de acesso como, por exemplo, o IP: 172.17.0.3. Desta forma, a chamada para o cliente será:

```console
mysql -h 172.17.0.3 -u root -p
```

:pushpin: Outra solução é executar o cliente via o container docker e configurar o servidor MySQL para permitir acesso via localhost. Fonte: https://sidroniolima.com.br/blog/2020/08/12/instalacao-mysql-via-docker-com-acesso-pelo-workbench/

```console
docker exec -it mysql-server mysql -u root -p
```

Execute o seguinte comando `SQL`:
```sql
grant all privileges on *.* to 'root'@'%' with grant option;
flush privileges;
```

## Usando servidor PostgreSQL + pgAdmin com Docker

Para usar o SGBD do PostgreSQL usando Docker, vamos fazer de duas maneiras:
* A primeira usando dois containers independentes e criando uma rede (network) do docker;
* A segunda usando o docker compose para criar os dois servições numa mesma rede.

## Maneira 1

Criar a rede postgres-network
```console
docker network create -d bridge postgres-network
```

Criar container postgres-server

```console
docker run --name postgres-server -e "POSTGRES_PASSWORD=postgres" -p 5432:5432 -v $HOME/dev/docker/volumes/postgres/conf:/var/lib/postgresql -v $HOME/dev/docker/volumes/postgres/data:/var/lib/postgresql/data --network=postgres-network -d postgres
```

Criar container pgadmin-server

```console
docker run --name pgadmin-server  -p 15432:80 -e "PGADMIN_DEFAULT_EMAIL=admin@pgamin.com" -e "PGADMIN_DEFAULT_PASSWORD=pgadmin" --network=postgres-network -d dpage/pgadmin4
```

### Manaira 2

A maneira 2 consiste em criarmos um arquivo `docker-compose.yml`.

```yaml
version: "3.8"

services:
  postgres:
    container_name: postgres-compose
    image: postgres
    volumes:
      - ./data/db:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=empresa_db
      - POSTGRES_USER=taciano
      - POSTGRES_PASSWORD=password
    restart: always
    ports:
      - "5400:5432"
    networks:
      - postgres-compose-network
  
  pgadmin:
    container_name: pgadmin4-compose
    image: dpage/pgadmin4
    restart: always
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@admin.com
      PGADMIN_DEFAULT_PASSWORD: pgadmin
    ports:
      - "16543:80"
    depends_on:
      - postgres
    networks:
      - postgres-compose-network

networks: 
  postgres-compose-network:
    driver: bridge
```

## Links

* https://techexpert.tips/pt-br/mariadb-pt-br/mariadb-instalacao-docker/
* https://renatogroffe.medium.com/postgresql-pgadmin-4-docker-compose-montando-rapidamente-um-ambiente-para-uso-55a2ab230b89
* https://hashinteractive.com/blog/docker-compose-up-with-postgres-quick-tips/
* https://mariadb.com/kb/en/installing-and-using-mariadb-via-docker/
* https://mariadb.com/resources/blog/try-mariadb-server-10-3-in-docker/
* https://www.pgadmin.org/
* https://www.postgresql.org
