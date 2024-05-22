# Evento DoWhile da Rocketseat

Workshop Criando um crud com spring webflux - programação reativa com Java.
Ministado por [Kamila Santos](https://github.com/Kamilahsantos)

Projeto [dowhile-reactive-api](https://github.com/Kamilahsantos/dowhile-reactive-api)

## Spring WebFlux

## MongoDB

* [Query Documents](https://www.tutorialkart.com/mongodb/mongodb-query-documents/)

### Iniciando MongoDB com Docker

baixar a imagem do mongodb:

```bash
    docker pull mongo
```

rodar o container do mongodb

```bash
    docker run --name mongodb -p 27017:27017 -d mongo
```

verificar os processos em execução

```bash
    docker ps
```

Outras fontes de informação sobre MongoDB com Docker:

* [How to Deploy and Manage MongoDB with Docker](https://phoenixnap.com/kb/docker-mongodb)
* [Getting Started With MongoDB As A Docker Container Deployment](https://www.thepolyglotdeveloper.com/2019/01/getting-started-mongodb-docker-container-deployment/)

### Acessanado via Terminal

```bash
    sudo docker exec -it mongodb bash
```

Depois digite mongo para entrar no cliente:

```bash
    mongo
```
