# Tarefa - MongoDB

## Programa

**Programa:** [Main.java](implementacaoJava/src/main/java/Main.java)

Para executar o programa Java, acesse a pasta `implementacaoJava`:

```bash
cd implementacaoJava
```

Compile e execute o projeto utilizando Maven:

```bash
mvn exec:java -Dexec.mainClass="Main"
```

O programa irá conectar ao MongoDB e executar as operações de inserção, consulta, atualização e remoção de dados.

---

## Script de Inicialização do Banco

**Script de inicialização:** [init.js](init.js)

O script `init.js` é executado automaticamente ao iniciar os containers com o comando:

```bash
docker compose up -d
```

Após a inicialização, é possível acessar o MongoDB utilizando:

```bash
docker exec -it mongodb_atividades mongosh -u admin -p admin123 --authenticationDatabase admin
```

Selecionar o banco de dados:

```javascript
use AtividadesProj
```

Listar as coleções existentes:

```javascript
show collections
```

Consultar os dados armazenados na coleção de projetos:

```javascript
db.projetos.find().pretty()
```
```javascript
db.empregados.find().pretty()
```
```javascript
db.atividades.find().pretty()
```

---

# Resumo Sobre MongoDB

O MongoDB é um Sistema Gerenciador de Banco de Dados (SGBD) NoSQL orientado a documentos. Diferente dos bancos relacionais tradicionais, como MySQL e PostgreSQL, o MongoDB armazena os dados em documentos no formato BSON (Binary JSON), permitindo uma estrutura mais flexível e dinâmica.

Esse modelo orientado a documentos possibilita armazenar informações complexas sem a necessidade de tabelas rígidas e relacionamentos tradicionais. Cada documento pode possuir diferentes atributos, o que facilita alterações na estrutura dos dados ao longo do desenvolvimento da aplicação.

O MongoDB possui como principais características:

- Modelo NoSQL orientado a documentos;
- Armazenamento em formato BSON;
- Alta flexibilidade de esquema;
- Facilidade de escalabilidade horizontal;
- Alto desempenho para grandes volumes de dados;
- Suporte a replicação e alta disponibilidade;
- Compatibilidade com diversas linguagens de programação;
- Suporte a consultas avançadas e indexação.

No contexto desta atividade, o MongoDB será utilizado para desenvolver um sistema de gerenciamento de atividades em projetos com empregados, permitindo armazenar projetos, atividades e informações dos funcionários de forma flexível e eficiente.

---

# Alta Disponibilidade e Replica Sets

O MongoDB possui suporte a alta disponibilidade através do mecanismo chamado **Replica Set**. Um Replica Set é um conjunto de servidores MongoDB que mantêm cópias sincronizadas dos mesmos dados, garantindo tolerância a falhas e maior disponibilidade da aplicação.

Em um Replica Set, os membros possuem diferentes papéis:

- **Primário (Primary):** responsável por receber operações de escrita e atualização dos dados;
- **Secundário (Secondary):** mantém uma cópia sincronizada dos dados do servidor primário e pode assumir automaticamente o papel principal em caso de falha;
- **Arbiter:** não armazena dados, mas participa do processo de votação para eleição de um novo servidor primário.

Para transformar o MongoDB em um Replica Set com três membros utilizando Docker, seria necessário:

1. Criar múltiplos containers MongoDB no `docker-compose.yml`;
2. Configurar todos os containers com o parâmetro `--replSet`;
3. Inicializar o Replica Set utilizando o comando `rs.initiate()` no Mongo Shell;
4. Adicionar os membros ao conjunto utilizando `rs.add()`.

Exemplo de configuração no `docker-compose.yml`:

```yaml
command: ["mongod", "--replSet", "rs0", "--bind_ip_all"]
```

Exemplo de inicialização no Mongo Shell:

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

Após a configuração, o MongoDB passa a possuir maior tolerância a falhas e disponibilidade dos dados.