# Executando container do Servidor MariaDB

Antes de executar o container, você pode baixar do **Docker Hub** a imagem oficial do `mariadb` e indicar sua versão mais atual `mariadb:latest` ou outra versão, por exemplo a versão `mariadb:10`:
```console
docker pull mariadb:10
```

Para que os dados fiquem persistidos, crie um diretório para ser o volume de dados compartilhado com o container:
```console
mkdir -p $HOME/docker/volumes/mariadb
```
Você também pode usar a criação de volumes do próprio *docker* (https://docs.docker.com/storage/volumes/).

Agora inicie o container:
```console
docker run --name mariadb-server -p 3306:3306 -d \
           -e "MYSQL_ROOT_PASSWORD=password" \
           -v $HOME/docker/volumes/mariadb:/var/lib/mysql \
           mariadb:10
```

## Acessando via MariaDB Cli (MySql Cli)

:pushpin: É possível executar **MariaDB Cli** via o container docker, usando o comando `docker exec`.

```console
docker exec -it mysql-server mysql -u root -p
```

Caso deseje pode instalar o cliente de acesso ao SGBD diretamente no SO:

```console
sudo apt install mysql-client
```

Acesse usando o host `127.0.0.1` ou `localhost`, com o usuário `root` e a senha passada em `MYSQL_ROOT_PASSWORD`:

```console
mysql -h 127.0.0.1 -u root -p
```

## Acessando MariaDB via CloudBeaver (dbeaver)

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
docker run --name cloudbeaver-client -d -p 8978:8978 \
           -v $HOME/docker/volumes/cloudbeaver:/opt/cloudbeaver/workspace \
           dbeaver/cloudbeaver:23.0.2
```

Abra o link http://localhost:8978 no navegador e configure a conexão com o servidor do mariadb.

Para acessar seu servidor mariadb, você precisa descobrir o IP do container que está executando o mariadb. Use o comando informando ao final o nome do conainer, neste exemplo é: `mariadb-server`.
```console
docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mariadb-server
```
Retornará um ou mais IPs de acesso como, por exemplo, o IP: 172.17.0.3. Desta forma, ao configurar a conexão no `cloudbeaver`, o `host` será o IP encontrado.

### Executando os container em uma mesma rede docker

Se você criar uma rede docker, você poderá conectar o `cloudbeaver` ao servidor do `mariadb` pelo nome do container.
```console
docker network create -d bridge database-network
```

Adicionando o servidor do mariadb na rede usando o nome do container.
```console
docker network connect database-network mariadb-server
```

Adicionando o client do cloudbeaver na rede usando o nome do container.
```console
docker network connect database-network cloudbeaver-client
```

Agora, para acessar seu servidor mariadb, você deve configurar a conexão no `cloudbeaver` usando o `host` sendo o nome do container do mariadb, no caso deste exemplo será `mariadb-server`.

## Mais informações:

* [CloudBeaver - Run Docker Container](https://cloudbeaver.io/docs/Run-Docker-Container/)
