# Usando servidor PostgreSQL + pgAdmin com Docker

Para usar o SGBD do PostgreSQL usando Docker, vamos fazer de duas maneiras:
* A primeira usando dois containers independentes e criando uma rede (network) do docker;
* A segunda usando o docker compose para criar os dois servições numa mesma rede.

## Maneira 1

Para que os dados fiquem persistidos, crie um diretório para ser o volume de dados compartilhado com o container:
```
mkdir -p $HOME/docker/volumes/postgres/conf
mkdir -p $HOME/docker/volumes/postgres/data
```

Criar a rede **postgres-network** para colocar dos dois container na rede, e assim eles se comunicarem pelo nome.
```console
docker network create -d bridge postgres-network
```

Antes de executar o container, você pode baixar a imagem do postgres:
```
docker pull postgres:16.2
```

Criar e inicie o container **postgres-server**:
```console
docker run --name postgres-server -e "POSTGRES_PASSWORD=postgres" -p 5432:5432 \
           -v $HOME/docker/volumes/postgres/conf:/var/lib/postgresql \
           -v $HOME/docker/volumes/postgres/data:/var/lib/postgresql/data \
           --network=postgres-network -d postgres:16.2
```

Criar e iniciar o container **pgadmin-server**:

```console
docker run --name pgadmin-server  -p 15432:80 \
           -e "PGADMIN_DEFAULT_EMAIL=admin@pgadmin.com" \
           -e "PGADMIN_DEFAULT_PASSWORD=pgadmin" \
           --network=postgres-network -d dpage/pgadmin4:8.4
```

### Acessando via cliente psql

:pushpin: É possível executar **psql** via o container docker, usando o comando `docker exec`.

```console
docker exec -it postgres-server psql -U postgres
```

Abrirá o prompt de comando do postgres.
```output
psql (15.2 (Debian 15.2-1.pgdg110+1))
Type "help" for help.

postgres=#
```
Comandos para listar bancos de dados e tabelas.

| Comando | Descrição | Exemplo |
|---|---|---|
| `\l` ou `\list` | Lista todos os bancos de dados disponíveis. | `\l` |
| `\c` ou `\connect` | Conecta a um banco de dados específico. | `\c nome_do_banco_de_dados` |
| `\dt` ou `\d` | Lista todas as tabelas no banco de dados atual. | `\dt` |
| `\q` ou `exit` ou `quit` | Sai do psql. | `\q` |
| `\h` ou `\help` | Obter mais informações. | `\h` |

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
