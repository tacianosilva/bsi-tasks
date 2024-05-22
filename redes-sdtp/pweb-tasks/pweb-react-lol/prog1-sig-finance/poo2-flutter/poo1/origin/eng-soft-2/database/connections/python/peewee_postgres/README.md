
# Exemplo de uso do ORM PeeWee para Python

Peewee is a simple and small ORM.

## Requisitos

Criar ambiente virtual chamando `.venv`:
```console
python3 -m venv .venv
```

Execute um servidor PostgreSQL e o PgAdmin para criar o banco e executar o código.
```docker
docker run --name postgres-server -e "POSTGRES_PASSWORD=postgres" -p 5432:5432 -v $HOME/dev/docker/volumes/postgres/conf:/var/lib/postgresql -v $HOME/dev/docker/volumes/postgres/data:/var/lib/postgresql/data --network=postgres-network -d postgres

docker run --name pgadmin-server -p 15432:80 -e "PGADMIN_DEFAULT_EMAIL=admin@admin.com" -e "PGADMIN_DEFAULT_PASSWORD=pgadmin" --network=postgres-network -d --restart always dpage/pgadmin4:latest
```

É necessário criar um banco de dados (vazio) via `psql` ou `pgadmin`, pois o **peewee** pode criar tabelas mas não cria **databases**. Adicione as informações do servidor PostgreSQL no arquivo de ambiente `.env`:

```environment
DATABASE_HOST=localhost
DATABASE_NAME=dbname
DATABASE_USER=postgres
DATABASE_PASS=postgres
DATABASE_PORT=5432
```

Ativar ambiente virtual, carregar variáveis de ambiente do arquivo `.env` e instalar dependências definidas no arquivo `requirements.txt`.
```console
source .venv/bin/activate
source .env
pip install -r requirements.txt
```

## Execução

```console
python main.py
```

## Documentação

* http://docs.peewee-orm.com/en/latest/peewee/models.html
* https://docs.peewee-orm.com/en/latest/peewee/example.html
* http://docs.peewee-orm.com/en/latest/peewee/api.html
* https://zetcode.com/python/peewee/
