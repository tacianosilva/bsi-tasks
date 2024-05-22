# Executando SGBDs utilizando Containers Docker

Nessa página apresentamos várias maneiras de executar os SGBDs usando containers docker.

## Instalação do Docker

O tutorial [How To Install and Use Docker on Ubuntu 22.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-22-04) da digitalocean traz detalhes para a instalação do docker na sua máquina. Você também pode acessar o [Site Oficial do Docker](https://docs.docker.com/engine/install/ubuntu/).

Siga os passos 1 e 2 do tutorial e verifique se o daemon foi iniciado e o processo habilitado a iniciar no boot. Verifique se ele está funcionando:

```console
sudo systemctl status docker
```

## SGBDs com containers Docker

* [MariaDB](mariadb/)
* [MySql](mysql)
* [Postgres](postgres/)
* [MongoDB](mongodb/)

## Links

* https://techexpert.tips/pt-br/mariadb-pt-br/mariadb-instalacao-docker/
* https://renatogroffe.medium.com/postgresql-pgadmin-4-docker-compose-montando-rapidamente-um-ambiente-para-uso-55a2ab230b89
* https://hashinteractive.com/blog/docker-compose-up-with-postgres-quick-tips/
* https://mariadb.com/kb/en/installing-and-using-mariadb-via-docker/
* https://mariadb.com/resources/blog/try-mariadb-server-10-3-in-docker/
* https://www.pgadmin.org/
* https://www.postgresql.org
