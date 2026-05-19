# Link de acesso

O link para o projeto encontra-se em: https://github.com/MoisesLuc/bsi-tasks/blob/main/database/20261/tarefas/MoisesLuc/proj_mongodb.py

# Resumo: MongoDB com Python

O MongoDB é um banco NoSQL orientado a documentos. Ele não usa tabelas como os bancos relacionais, mas coleções de documentos em formato parecido com JSON, o que deixa o armazenamento mais flexível.

Suas principais características são a escalabilidade, a flexibilidade de esquema e a facilidade para lidar com dados variados. Ele também oferece suporte a índices, consultas mais elaboradas e agregações, o que ajuda quando a aplicação precisa organizar ou filtrar grandes volumes de informação. Por isso, é bastante usado em sistemas que mudam com frequência.

No Python, o acesso ao MongoDB costuma ser feito com a biblioteca PyMongo, que permite conectar ao banco e executar operações de CRUD, aplicar filtros nas consultas, atualizar documentos de forma parcial e trabalhar com coleções de maneira bem flexível. Em aplicações mais robustas, também é comum usar recursos de agregação e bibliotecas assíncronas, como o Motor, para melhorar o desempenho e o controle das requisições.

## Replica Set no MongoDB

Um Replica Set é um grupo de servidores MongoDB que mantém os mesmos dados sincronizados. Ele serve para dar mais disponibilidade ao banco.

O primário recebe as escritas. Os secundários copiam os dados e podem assumir o papel principal se houver falha. O arbiter não guarda dados, só participa da votação para eleger um novo primário se necessário.

## Como configurar um Replica Set de três membros

No projeto, deve-se subir três instâncias do MongoDB com o mesmo nome de replica set e usar o Python para iniciar e acessar o conjunto.

Com PyMongo, a inicialização pode ser feita assim:

```python
from pymongo import MongoClient

client = MongoClient("mongodb://mongo1:27017")

client.admin.command("replSetInitiate", {
    "_id": "rs0",
    "members": [
        {"_id": 0, "host": "mongo1:27017"},
        {"_id": 1, "host": "mongo2:27017"},
        {"_id": 2, "host": "mongo3:27017"}
    ]
})
```

Na aplicação Python, a conexão ficaria assim:

```python
client = pymongo.MongoClient("mongodb://mongo1:27017,mongo2:27017,mongo3:27017/?replicaSet=rs0")
```
