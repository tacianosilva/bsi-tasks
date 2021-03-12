# Dicas sobre Banco de Dados

Dicas e exemplos para as disciplinas relacionadas com Banco de Dados.

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

## Exemplos de uso de JDBC

No diretório [JDBC](jdbc/) temos um projeto java com exemplos de conexões JDBC, usando drivers para o MariaDB e para o MySql.

## Scripts SQL

No diretório [SCRIPTS](scripts/) temos vários scripts de criação e povoamento para Base de Dados usadas nas aulas da disciplina Banco de Dados.