# Executando container do Servidor MySql

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

## Acessando via MySql Client

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
