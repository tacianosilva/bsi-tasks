# Dicas sobre Banco de Dados

Dicas e exemplos para as disciplinas relacionadas com Banco de Dados.

## Exemplos de uso de JDBC

No diretório [JDBC](jdbc/) temos um projeto java com exemplos de conexões JDBC, usando drivers para o MariaDB e para o MySql.

## Scripts SQL

No diretório [SCRIPTS](scripts/) temos vários scripts de criação e povoamento para Base de Dados usadas nas aulas da disciplina Banco de Dados.

## Usando servidor MariaDB com Docker

### Instalação do Docker

O tutorial [how-to-install-and-use-docker-on-ubuntu-20-04-pt](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-pt) da digitalocean traz detalhes para a instalação do docker na sua máquina. Você também pode acessar o [Site Oficial do Docker](https://docs.docker.com/engine/install/ubuntu/).

Siga os passos 1 e 2 do tutorial e verifique se o daemon foi iniciado e o processo habilitado a iniciar no boot. Verifique se ele está funcionando:

```bash
   $ sudo systemctl status docker
```

### Executando container do Servidor MariaDB

Antes de executar o container, baixe a imagem do `mariadb`:

```bash
    $ docker pull mariadb
```

Para que os dados fiquem persistidos, crie um diretório para ser o volume de dados compartilhado com o container:

```bash
    $ mkdir $HOME/docker/volumes/mariadb
```

Agora inicie o container:

```bash
   $ docker run -d --name mariadb-server -p 3306:3306 -e "MYSQL_ROOT_PASSWORD=docker" -v $HOME/docker/volumes/mariadb:/var/lib/mysql mariadb
```

### Acessando via MariaDB Cli (MySql Cli)

Se não tiver, instale o cliente de acesso ao SGBD:

```bash
    $ sudo apt install mysql-client
```

Acesse usando o `host 127.0.0.1` e o usuário `root`:

```bash
    $ mysql -h 127.0.0.1 -u root -p
```

## Usando servidor PostgreSQL + pgAdmin com Docker

Para usar o SGBD do PostgreSQL usando Docker, vamos fazer de duas maneiras:
* A primeira usando dois containers independentes e criando uma rede (network) do docker;
* A segunda usando o docker compose para criar os dois servições numa mesma rede.

## Maneira 1

Criar a rede postgres-network
```bash
    $ docker network create -d bridge postgres-network
```

Criar container postgres-server

```bash
docker run --name postgres-server -e "POSTGRES_PASSWORD=postgres" -p 5432:5432 -v $HOME/dev/docker/volumes/postgres:/var/lib/postgresql/data --network=postgres-network -d postgres
```

Criar container pgadmin-server

```bash
docker run --name pgadmin-server  -p 15432:80 -e "PGADMIN_DEFAULT_EMAIL=tacianosilva@gmail.com" -e "PGADMIN_DEFAULT_PASSWORD=pgadmin" --network=postgres-network -d dpage/pgadmin4
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