# MongoDB

Exemplo de uso de MongoDB com Python e Docker.

## Servidor MongoDB com Docker

Execute o servidor do MongoDB e o cliente Mongo-Express conforme apresentado no tutorial [Servidor MongoDB com Docker](https://github.com/tacianosilva/bsi-tasks/blob/master/database/docker/mongodb)

## Instalação das dependências

Crie um ambiente virtual python usando o módulo `venv`:
```console
python3 -m venv .venv 
```

Ative o ambiente virtual python:
```console
source .venv/bin/activate 
```

Instale as dependências:
```console
pip install -r requirements.txt
```

## Execute o script python de demostração:
```console
 python demo_mongodb_test.py
```
