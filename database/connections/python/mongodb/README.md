# MongoDB

Exemplo de uso de MongoDB com Python e Docker.

## Servidor MongoDB com Docker

Crie uma rede para o `mongodb-server` e para o `mongo-express`:
```docker
docker network create -d bridge mongodb-network
```
Execute o servidor do MongoDB:
```docker
docker run --name mongodb-server -p 27017:27017 \
       -e MONGO_INITDB_ROOT_USERNAME=user \
       -e MONGO_INITDB_ROOT_PASSWORD=pass \
       --network mongodb-network \
       -d mongo:latest
```

No computadores do laboratório IMD, a versão mais nova do MongoDB não executou. Foi necessário usar a versão `mongo:4.2.21`.

### Cliente MongoDB Express

**MongoDB Express** é uma Interface de Administração Web do MongoDB escrita em Node.js, Express e Bootstrap3. O **MongoDB Express** está disponível no repositório: https://github.com/mongo-express/mongo-express.

```docker
docker run -it --rm \
    --network mongodb-network \
    --name mongo-express \
    -p 8081:8081 \
    -e ME_CONFIG_MONGODB_SERVER="mongodb-server" \
    -e ME_CONFIG_MONGODB_ADMINUSERNAME="user" \
    -e ME_CONFIG_MONGODB_ADMINPASSWORD="pass" \
    mongo-express
```
