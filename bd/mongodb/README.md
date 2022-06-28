# MongoDB

Exemplo de uso de MongoDB com Python e Docker.

## Servidor MongoDB com Docker

```docker
docker run --name mongodb-server -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=user -e MONGO_INITDB_ROOT_PASSWORD=pass mongo:latest
```
