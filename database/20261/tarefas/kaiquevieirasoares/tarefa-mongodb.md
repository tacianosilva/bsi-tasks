# Tarefa Individual - MongoDB

### Links do Repositório
* **Programa (CRUD em Java e repositório principal):** [atividades-bd-2](https://github.com/kaiquevieirasoares/atividades-bd-2)
* **Script de Inicialização:** [init-mongo.js](https://github.com/kaiquevieirasoares/atividades-bd-2/blob/main/tarefa-mongodb/init-mongo.js)
* **Configuração Docker:** [docker-compose.yml](https://github.com/kaiquevieirasoares/atividades-bd-2/blob/main/tarefa-mongodb/docker-compose.yml)

---

### 2.b. Resumo sobre o MongoDB
[cite_start]O MongoDB é um Sistema de Gerenciamento de Banco de Dados (SGBD) NoSQL classificado como orientado a documentos (document database)[cite: 16]. Ao contrário dos bancos de dados relacionais tradicionais que organizam os dados em tabelas e linhas, o MongoDB armazena as informações em documentos no formato BSON (uma representação binária e otimizada do JSON).

**Principais Características:**
* **Esquema Flexível (Schema-less):** Documentos armazenados em uma mesma coleção não precisam ter a mesma estrutura de campos, permitindo evoluções rápidas no modelo de dados sem a necessidade de migrações complexas.
* **Alta Performance:** Otimizado para operações de leitura e escrita intensas, armazenando dados relacionados juntos para acesso rápido.
* **Escalabilidade Horizontal:** Suporte nativo a *sharding*, distribuindo grandes volumes de dados através de múltiplos servidores.
* [cite_start]**Alta Disponibilidade:** Utiliza o conceito de Replica Sets para garantir replicação contínua dos dados e tolerância a falhas[cite: 29].

---

### 3. Configuração do Servidor MongoDB via Docker
[cite_start]Para subir o servidor com o banco `Atividades_Proj` e um usuário com senha, utilizamos o Docker[cite: 17, 18]. O arquivo `docker-compose.yml` foi configurado da seguinte forma:

```yaml
version: '3.8'

services:
  mongodb:
    image: mongo:latest
    container_name: mongodb_server
    ports:
      - "27017:27017"
    environment:
      MONGO_INITDB_ROOT_USERNAME: admin
      MONGO_INITDB_ROOT_PASSWORD: adminpassword
      MONGO_INITDB_DATABASE: Atividades_Proj
    volumes:
      - mongo_data:/data/db
      - ./init-mongo.js:/docker-entrypoint-initdb.d/init-mongo.js:ro

volumes:
  mongo_data:
```

---

### 4. Esquema das Coleções e Script de Inicialização
[cite_start]Para o gerenciamento de atividades em projetos com empregados, utilizamos três coleções principais[cite: 19]. Diferente do relacional, usamos referências e sub-documentos onde faz sentido:
1.  `empregados`: Guarda os dados dos funcionários.
2.  `projetos`: Guarda as informações do projeto e faz referência ao líder (empregado).
3.  `atividades`: Guarda as tarefas, fazendo referência ao projeto e ao empregado responsável.

[cite_start]O arquivo `init-mongo.js` foi criado para inserir os 3 documentos iniciais exigidos em cada coleção[cite: 20]:

```javascript
// Seleciona o banco de dados
db = db.getSiblingDB('Atividades_Proj');

// Criação e Inserção em Empregados
db.empregados.insertMany([
  { _id: 1, nome: "Alice Silva", cargo: "Desenvolvedora Backend", email: "alice@gmail.com" },
  { _id: 2, nome: "Bruno Costa", cargo: "Tech Lead", email: "bruno@gmail.com" },
  { _id: 3, nome: "Carla Souza", cargo: "Gerente de Projetos", email: "carla@gmail.com" }
]);

// Criação e Inserção em Projetos
db.projetos.insertMany([
  { _id: 101, nome: "Sistema iService", descricao: "Modernização da arquitetura SaaS", lider_id: 2, status: "Em Andamento" },
  { _id: 102, nome: "Portal B2B", descricao: "Tendências de publicidade", lider_id: 3, status: "Em Andamento" },
  { _id: 103, nome: "Migração Cloud", descricao: "Migração de infraestrutura on-premise para nuvem", lider_id: 2, status: "Planejamento" }
]);

// Criação e Inserção em Atividades
db.atividades.insertMany([
  { _id: 1001, titulo: "Configurar OAuth2 e JWT", projeto_id: 101, responsavel_id: 1, status: "Concluída", prioridade: "Alta" },
  { _id: 1002, titulo: "Criar colunas discriminator no PostgreSQL", projeto_id: 102, responsavel_id: 1, status: "Em Andamento", prioridade: "Média" },
  { _id: 1003, titulo: "Aprovar pull request #7 de CI/CD", projeto_id: 101, responsavel_id: 2, status: "Pendente", prioridade: "Alta" }
]);
```

---

### 6. Alta Disponibilidade e Configuração Avançada (Replica Sets)

**a. O que é um Replica Set e os papéis dos membros:**
[cite_start]Para garantir alta disponibilidade e tolerância a falhas, o MongoDB utiliza o conceito de Replica Sets[cite: 28, 29]. Um Replica Set é um cluster de processos MongoDB que mantêm cópias idênticas dos mesmos dados. [cite_start]Os papéis (roles) dos membros são divididos em primário, secundário e arbiter[cite: 30]:
* **Primário (Primary):** É o nó principal, sendo o único membro que pode receber operações de escrita (Create, Update, Delete). Ele registra todas as mudanças em um log de operações (`oplog`).
* **Secundário (Secondary):** Mantém uma cópia exata do banco de dados aplicando as operações do `oplog` do Primário. Pode ser configurado para receber operações de leitura, aliviando a carga do primário. Se o primário cair, um secundário pode ser eleito como novo primário.
* **Arbiter (Árbitro):** Não armazena nenhuma cópia dos dados. Sua única função é participar das eleições (votar) caso o nó primário fique indisponível, garantindo que o cluster tenha o quórum necessário para eleger um novo primário de forma rápida.

**b. Etapas e Comandos para transformar em um Replica Set de três membros:**
[cite_start]Considerando a configuração inicial via Docker, os passos essenciais para transformar o servidor MongoDB em um Replica Set de três membros para o banco de dados `Atividades_Proj` seriam[cite: 37]:

1.  **Alterar o `docker-compose.yml`:** Criar três serviços MongoDB distintos (ex: `mongo-primary`, `mongo-sec1`, `mongo-sec2`) na mesma rede Docker.
2.  **Adicionar o parâmetro de inicialização:** Em cada serviço no `docker-compose`, adicionar o comando de inicialização `--replSet rs_atividades` para indicar que pertencem ao mesmo cluster.
3.  **Iniciar o cluster e conectar no shell:** Rodar `docker-compose up -d` e acessar o *Mongo Shell* (`mongosh`) do nó que desejamos que seja o primário.
4.  **Comando de Configuração Avançada (no Mongo Shell):** Executar a inicialização do Replica Set:
    ```javascript
    rs.initiate({
      _id: "rs_atividades",
      members: [
        { _id: 0, host: "mongo-primary:27017" },
        { _id: 1, host: "mongo-sec1:27017" },
        { _id: 2, host: "mongo-sec2:27017" }
      ]
    })
    ```
5.  **Verificar status:** Rodar `rs.status()` no shell para confirmar se a configuração foi propagada e os papéis (PRIMARY e SECONDARY) foram atribuídos corretamente.