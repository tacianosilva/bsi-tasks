# Tarefa Mongo

## 1. Link do projeto

- Repositório da atividade: https://github.com/Paulo-Douglas/DB2/tree/main/task/mongotask

## 2. Como subir a aplicação

- No diretório do projeto, execute:

```bash
docker compose up --build
```

- Esse comando faz o build das imagens (se necessario) e sobe os containers definidos no `docker-compose.yml`.

## 3. Como testar a aplicação

- API (Swagger):
	- Acesse no navegador: `http://localhost:8080/swagger`

- Cliente Mongo:
	- Acesse na porta `8081` (exemplo comum de interface web): `http://localhost:8081`

## 4. Resumo sobre MongoDB (linguagem escolhida: Java + Spring Boot)

MongoDB e um SGBD NoSQL orientado a documentos (document database). Em vez de armazenar dados em tabelas relacionais com esquema rigido, ele organiza as informacoes em colecoes de documentos no formato BSON (similar a JSON).

Principais caracteristicas:

- Modelo flexivel de dados: documentos podem variar de estrutura.
- Alta produtividade: integra muito bem com Java + Spring Boot por meio do Spring Data MongoDB, facilitando repositorios, consultas e mapeamento de documentos.
- Escalabilidade horizontal: suporte nativo a sharding.
- Alta disponibilidade: suporte a Replica Set.
- Boa performance para leitura/escrita em cenarios com grande volume de dados semiestruturados.

## 5. O que e Replica Set no MongoDB

Replica Set e um conjunto de instancias MongoDB que mantem o mesmo conjunto de dados replicado entre si para garantir alta disponibilidade e tolerancia a falhas.

Papeis dos membros:

- Primario (primary):
	- Recebe operacoes de escrita.
	- Repassa as alteracoes para os secundarios via replication log (oplog).

- Secundario (secondary):
	- Replica os dados do primario.
	- Pode atender leituras (quando configurado para isso).
	- Pode ser eleito primario se o atual falhar.

- Arbiter:
	- Nao armazena dados.
	- Participa apenas da votacao de eleicao para desempate (quorum).

## 6. Etapas e comandos para transformar em Replica Set de 3 membros (AtividadesProj)

Considerando uma configuracao inicial com Docker, o caminho essencial e:

1. Executar tres containers MongoDB com `--replSet` e nomes de host fixos.
2. Expor portas para acesso local (ex.: 27017, 27018, 27019).
3. Iniciar o Replica Set com `rs.initiate(...)` no mongo shell.
4. Validar status com `rs.status()`.
5. Criar/usar o banco `AtividadesProj` apos a inicializacao.

### 6.1 Exemplo de servicos no docker-compose

```yaml
services:
	mongo1:
		image: mongo:7
		container_name: mongo1
		command: ["mongod", "--replSet", "rs0", "--bind_ip_all"]
		ports:
			- "27017:27017"
		volumes:
			- mongo1_data:/data/db

	mongo2:
		image: mongo:7
		container_name: mongo2
		command: ["mongod", "--replSet", "rs0", "--bind_ip_all"]
		ports:
			- "27018:27017"
		volumes:
			- mongo2_data:/data/db

	mongo3:
		image: mongo:7
		container_name: mongo3
		command: ["mongod", "--replSet", "rs0", "--bind_ip_all"]
		ports:
			- "27019:27017"
		volumes:
			- mongo3_data:/data/db

volumes:
	mongo1_data:
	mongo2_data:
	mongo3_data:
```

Subindo os servicos:

```bash
docker compose up -d --build
```

### 6.2 Inicializacao do Replica Set no mongo shell

Conectar no primeiro no:

```bash
docker exec -it mongo1 mongosh
```

Iniciar o Replica Set com tres membros:

```javascript
rs.initiate({
	_id: "rs0",
	members: [
		{ _id: 0, host: "mongo1:27017", priority: 2 },
		{ _id: 1, host: "mongo2:27017", priority: 1 },
		{ _id: 2, host: "mongo3:27017", arbiterOnly: true }
	]
})
```

Validar estado:

```javascript
rs.status()
```

### 6.3 Criacao e uso do banco AtividadesProj

Ainda no `mongosh` (no primario):

```javascript
use AtividadesProj
db.createCollection("atividades")
db.atividades.insertOne({ titulo: "Exemplo", status: "aberta" })
db.atividades.find()
```

Com isso, o banco `AtividadesProj` passa a operar sobre uma topologia de Replica Set com tres membros, oferecendo maior disponibilidade e resiliencia.
