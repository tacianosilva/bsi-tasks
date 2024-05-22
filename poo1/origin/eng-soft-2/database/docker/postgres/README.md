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
