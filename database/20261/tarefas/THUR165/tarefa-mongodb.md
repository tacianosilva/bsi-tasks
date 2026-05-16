# Tarefa - MongoDB

## Links

- Código Python: crud_mongodb.py

- Docker: docker-compose.yml

- Script de inicialização: init_db.py

---

## O que é MongoDB?

MongoDB é um banco de dados NoSQL orientado a documentos.

Ele armazena dados em documentos BSON (Binary JSON), um formato semelhante ao JSON tradicional, porém otimizado para armazenamento e desempenho.

Diferente dos bancos relacionais tradicionais, o MongoDB não utiliza tabelas e linhas. Em vez disso, ele organiza os dados em coleções e documentos, permitindo maior flexibilidade na estrutura das informações.

O MongoDB é amplamente utilizado em aplicações modernas devido à sua alta escalabilidade, facilidade de integração com aplicações web e capacidade de lidar com grandes volumes de dados.

Entre suas principais características estão:

- Modelo orientado a documentos;
- Flexibilidade de esquema;
- Alta performance em operações de leitura e escrita;
- Escalabilidade horizontal;
- Suporte a Replica Sets para alta disponibilidade;
- Facilidade de integração com diversas linguagens de programação.

Na linguagem Python, a conexão com o MongoDB pode ser realizada utilizando a biblioteca PyMongo.

# Alta Disponibilidade e Configuração Avançada (Replica Sets)

##  O que é um Replica Set no MongoDB?

Replica Set é um conjunto de múltiplas instâncias do MongoDB que mantêm uma cópia idêntica dos mesmos dados. Seu principal objetivo é garantir alta disponibilidade, redundância e tolerância a falhas no sistema.

Esse mecanismo permite que, caso um servidor falhe, outro assuma automaticamente suas funções, evitando a indisponibilidade da aplicação.

O Replica Set é uma das principais funcionalidades do MongoDB para ambientes de produção, pois aumenta a confiabilidade do banco de dados e reduz riscos de perda de dados.

O funcionamento ocorre através da replicação automática dos dados entre os membros do conjunto.

---

## Papéis dos membros do Replica Set

### 🔹 Primário (Primary)

O membro primário é o servidor principal do Replica Set.

Ele é responsável por:
- receber operações de escrita;
- atualizar os dados;
- coordenar a replicação para os outros membros.

Todas as operações de escrita realizadas pela aplicação são enviadas inicialmente ao nó primário.

---

### 🔹 Secundário (Secondary)

Os membros secundários mantêm cópias dos dados do primário.

Suas funções são:
- replicar os dados automaticamente;
- atuar como backup;
- assumir o papel de primário em caso de falha.

Caso o servidor primário fique indisponível, ocorre uma eleição automática entre os secundários para definir um novo primário.

---

### 🔹 Arbiter

O Arbiter é um membro especial que:
- não armazena dados;
- não realiza replicação;
- participa apenas do processo de eleição.

Seu objetivo é auxiliar na tomada de decisão quando há necessidade de eleger um novo primário.

O uso do Arbiter ajuda a manter um número ímpar de votos no Replica Set, evitando empates durante as eleições.

---

## Benefícios do Replica Set

Entre os principais benefícios do Replica Set estão:

- Alta disponibilidade;
- Recuperação automática de falhas;
- Redundância de dados;
- Maior confiabilidade;
- Tolerância a falhas;
- Continuidade da aplicação;
- Possibilidade de distribuição de leitura entre secundários.

---

## Processo de Failover

Quando o servidor primário falha:

1. Os membros secundários detectam a falha;
2. Uma eleição é iniciada automaticamente;
3. Um dos secundários é promovido a novo primário;
4. A aplicação continua funcionando com mínima interrupção.

Esse processo é conhecido como failover automático.

---

## Configuração de Replica Set utilizando Docker

Para transformar o MongoDB em um Replica Set de três membros utilizando Docker, é necessário executar múltiplos containers do MongoDB com a configuração de replicação habilitada.

---

## Etapas principais

### 1. Criar múltiplos containers MongoDB

É necessário criar:
- 1 servidor primário;
- 2 servidores secundários.

Cada container deve possuir:
- porta própria;
- volume próprio;
- nome único.

---

### 2. Habilitar o Replica Set

Cada instância MongoDB deve iniciar com o parâmetro:

```yaml
--replSet rs0
```

Esse parâmetro ativa o suporte a Replica Sets.

---

## Exemplo de configuração Docker Compose

```yaml
version: '3.8'

services:

  mongo1:
    image: mongo:7
    container_name: mongo1
    command: mongod --replSet rs0
    ports:
      - "27017:27017"

  mongo2:
    image: mongo:7
    container_name: mongo2
    command: mongod --replSet rs0
    ports:
      - "27018:27017"

  mongo3:
    image: mongo:7
    container_name: mongo3
    command: mongod --replSet rs0
    ports:
      - "27019:27017"
```

---

## 3. Inicializar o Replica Set

Após iniciar os containers:

```bash
docker-compose up -d
```

Entrar no Mongo Shell:

```bash
docker exec -it mongo1 mongosh
```

---

## 4. Executar o comando rs.initiate()

```javascript
rs.initiate({
   _id: "rs0",
   members: [
      { _id: 0, host: "mongo1:27017" },
      { _id: 1, host: "mongo2:27017" },
      { _id: 2, host: "mongo3:27017" }
   ]
})
```

Esse comando:
- cria o Replica Set;
- define os membros participantes;
- inicia o processo de replicação.

---

## 5. Verificar status

Para verificar se o Replica Set foi criado corretamente:

```javascript
rs.status()
```

O comando exibe:
- membros;
- estado dos servidores;
- quem é o primário;
- quem são os secundários.

---

## Funcionamento da replicação

Após a configuração:
- todas as escritas são feitas no primário;
- os secundários replicam automaticamente os dados;
- em caso de falha, outro servidor assume automaticamente.

Isso vai garantir maior disponibilidade e segurança para o banco de dados da aplicação AtividadesProj.