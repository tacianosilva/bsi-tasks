# Tarefa Individual - MongoDB

Este documento contém a resolução da tarefa sobre o MongoDB.

## Resumo sobre o MongoDB
O MongoDB é um Sistema de Gerenciamento de Banco de Dados (SGBD) NoSQL **orientado a documentos**. Diferente de bancos de dados relacionais que utilizam tabelas e linhas, o MongoDB armazena dados no formato de documentos BSON (Binary JSON). 

Principais características:
- **Esquema flexível**: Os documentos na mesma coleção não precisam ter a mesma estrutura de campos, permitindo evoluções rápidas e iterativas no design de dados.
- **Alta disponibilidade**: Suporta nativamente **Replica Sets**, que são grupos de instâncias do MongoDB mantendo o mesmo conjunto de dados, garantindo tolerância a falhas.
- **Escalabilidade horizontal**: Através de **Sharding**, o MongoDB pode distribuir os dados em várias máquinas, lidando com grandes volumes e alta carga de acessos.
- **Consultas ricas**: Suporta um poderoso framework de agregação, índices secundários e geoespaciais, e consultas complexas nos documentos.

## Código e Scripts
- [Script de Inicialização do MongoDB](./python_mongo/init_mongo.js)
- [Programa CRUD em Python](./python_mongo/crud_mongo.py)
- [Arquivo Docker Compose](./docker-compose.yml) (modificado para incluir o MongoDB)

Para instalar as dependências do programa Python, utilize o comando:
```bash
pip install pymongo
```

## Alta Disponibilidade e Replica Sets

### O que é um Replica Set?
Um Replica Set no MongoDB é um grupo de processos `mongod` que mantêm o mesmo conjunto de dados. Eles fornecem redundância e alta disponibilidade, sendo a base para todas as implantações em produção. A replicação protege o banco de dados contra a perda de um único servidor ou problemas de hardware.

### Papéis dos Membros
Em um Replica Set típico de 3 membros, temos os seguintes papéis:
1. **Primário (Primary)**: É o único membro que recebe operações de escrita (Create, Update, Delete). Ele registra todas as alterações em seu *oplog* (operations log).
2. **Secundário (Secondary)**: Os secundários replicam o *oplog* do primário e aplicam as operações em seus próprios conjuntos de dados, mantendo-os sincronizados com o primário. Eles podem atender a operações de leitura caso configurados pelo cliente, ajudando no balanceamento de carga. Em caso de falha do primário, os secundários realizam uma eleição para escolher um novo primário.
3. **Árbitro (Arbiter)**: Opcional (quando se tem um número par de nós com dados). Um árbitro não possui cópia dos dados, ele apenas participa das eleições para garantir uma maioria (quorum). Útil quando não se quer gastar recursos de hardware para armazenar dados redundantes, mas precisa-se de um terceiro voto.

---

## Configuração Avançada de Replica Set (Exemplo)

Considerando a configuração inicial do Docker, para transformar o servidor MongoDB num Replica Set de 3 membros (primário e dois secundários) para o banco `AtividadesProj`, as etapas essenciais seriam:

### 1. Modificar o docker-compose.yml
Precisaríamos definir 3 serviços MongoDB e configurar o parâmetro `--replSet`.

```yaml
version: "3.9"

services:
  mongo1:
    image: mongo:6.0
    command: ["--replSet", "rs0", "--bind_ip_all"]
    ports:
      - "27017:27017"

  mongo2:
    image: mongo:6.0
    command: ["--replSet", "rs0", "--bind_ip_all"]
    ports:
      - "27018:27017"

  mongo3:
    image: mongo:6.0
    command: ["--replSet", "rs0", "--bind_ip_all"]
    ports:
      - "27019:27017"
```

### 2. Inicializar o Replica Set no Mongo Shell
Após subir os containers (`docker-compose up -d`), precisamos conectar em um dos nós (ex: `mongo1`) e iniciar o replica set:

```bash
docker exec -it mongo1 mongosh
```

Dentro do Mongo Shell, rodaríamos a configuração de inicialização do Replica Set:

```javascript
rs.initiate(
  {
    _id: "rs0",
    members: [
      { _id: 0, host: "mongo1:27017" },
      { _id: 1, host: "mongo2:27017" },
      { _id: 2, host: "mongo3:27017" }
    ]
  }
)
```

Com isso, os três nós formariam um Replica Set, e as eleições definiriam automaticamente o nó primário. Qualquer dado inserido no primário seria instantaneamente copiado para os secundários através da leitura contínua do *oplog*.
