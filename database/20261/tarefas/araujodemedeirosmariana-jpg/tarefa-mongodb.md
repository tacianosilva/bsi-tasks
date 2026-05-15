# Tarefa - MongoDB

## 🔗 Links
- **Programa CRUD:** [./crud_mongodb.py](./crud_mongodb.py)
- **Script de inicialização:** [./init.js](./init.js)
- **Docker Compose (Replica Set):** [./docker-compose-replicaset.yml](./docker-compose-replicaset.yml)

---

## 📌 Resumo sobre MongoDB

O **MongoDB** é um SGBD **NoSQL orientado a documentos** (document database), que armazena dados em formato BSON (JSON binário). Diferente dos bancos relacionais, ele não utiliza tabelas com esquemas fixos, mas sim **coleções** de documentos flexíveis.

### Principais características:
- **Schema-less**: documentos na mesma coleção podem ter estruturas diferentes.
- **Escalabilidade horizontal**: via sharding.
- **Alta disponibilidade**: via Replica Sets.
- **Consultas poderosas**: suporte a índices, agregações e queries geoespaciais.
- **Linguagem de consulta rica**: operadores como `$match`, `$group`, `$lookup`.
- **Transações ACID** (a partir da versão 4.0) para cenários que exigem consistência multdocumento.

No contexto de gerenciamento de atividades em projetos, o MongoDB permite modelar cada projeto como um documento contendo suas atividades (subdocumentos) ou relacionar coleções via referências, conforme a necessidade de performance ou atomicidade.

---

## 🐳 3. Servidor MongoDB com Docker (Replica Set)

### Comando básico (para teste único):
```bash
docker run -d --name mongodb -p 27017:27017 mongo:latest
```

### Acessar o MongoDB Shell:
```bash
docker exec -it mongodb mongosh
```

### Criar banco e usuário:
```javascript
use AtividadesProj
db.createUser({
  user: "adminUser",
  pwd: "senhaSegura123",
  roles: [{ role: "readWrite", db: "AtividadesProj" }]
})
```
## 🧩 4. Esquema das coleções

### Coleção projetos
```json
{
  "_id": "ObjectId",
  "nome": "Sistema de E-commerce",
  "lider": "Mariana Araújo",
  "dataInicio": "ISODate(2025-01-15)",
  "status": "ativo"
}
```

### Coleção atividades
```json
{
  "_id": "ObjectId",
  "projetoId": "ObjectId",
  "titulo": "Configurar ambiente",
  "responsavel": "Mariana",
  "prazo": "ISODate(2025-02-15)",
  "concluida": false
}
```

### Coleção empregados
```json
{
  "_id": "ObjectId",
  "nome": "Mariana Araújo",
  "email": "mariana@empresa.com",
  "cargo": "Gerente"
}
```

---

## 📜 5. Script de inicialização (init.js)

```javascript
use AtividadesProj

// ==================== PROJETOS ====================
db.projetos.insertMany([
  { nome: "Sistema de E-commerce", lider: "Mariana Araújo", dataInicio: new Date(), status: "ativo" },
  { nome: "App Mobile de Entregas", lider: "João Pedro", dataInicio: new Date(), status: "planejado" },
  { nome: "Dashboard de BI", lider: "Ana Clara", dataInicio: new Date(), status: "concluido" }
])

// ==================== ATIVIDADES ====================
const projetoEcommerce = db.projetos.findOne({ nome: "Sistema de E-commerce" })._id
const projetoApp = db.projetos.findOne({ nome: "App Mobile de Entregas" })._id
const projetoDashboard = db.projetos.findOne({ nome: "Dashboard de BI" })._id

db.atividades.insertMany([
  { titulo: "Configurar ambiente", responsavel: "Mariana", prazo: new Date(), concluida: false, projetoId: projetoEcommerce },
  { titulo: "Desenvolver API", responsavel: "Carlos", prazo: new Date(), concluida: false, projetoId: projetoEcommerce },
  { titulo: "Implementar frontend", responsavel: "Fernanda", prazo: new Date(), concluida: true, projetoId: projetoApp },
  { titulo: "Criar gráficos", responsavel: "Ana Clara", prazo: new Date(), concluida: true, projetoId: projetoDashboard }
])

// ==================== EMPREGADOS ====================
db.empregados.insertMany([
  { nome: "Mariana Araújo", email: "mariana@empresa.com", cargo: "Gerente" },
  { nome: "Carlos Silva", email: "carlos@empresa.com", cargo: "Dev Backend" },
  { nome: "Fernanda Lima", email: "fernanda@empresa.com", cargo: "Dev Frontend" }
])

print("✅ Banco de dados inicializado com sucesso!")
```

### Como executar o script:
```bash
docker exec -i mongodb mongosh < init.js
```
---

## 💻 6. Programa CRUD (Python)

### Operações implementadas:
Operação | Função |	Descrição
---------  | ----------- | ----------- |
CREATE | criar_atividade() | Insere nova atividade em projeto existente
READ | listar_projetos_com_atividades() | Lista todos os projetos e suas atividades
UPDATE | atualizar_lider_projeto() | Altera o líder de um projeto específico
DELETE | remover_atividade() | Remove uma atividade (com confirmação)

### Como executar:
```bash
# Instalar dependência
pip install pymongo

# Executar o programa
python3 crud_mongodb.py
```

### Exemplo de uso:

```text
==================================================
📌 SISTEMA DE GERENCIAMENTO DE ATIVIDADES - CRUD MongoDB
==================================================
1️⃣  Criar nova atividade (CREATE)
2️⃣  Listar projetos e atividades (READ)
3️⃣  Atualizar líder de projeto (UPDATE)
4️⃣  Remover atividade (DELETE)
5️⃣  Mostrar estatísticas
0️⃣  Sair
==================================================

👉 Escolha uma opção: 2

📊 RELATÓRIO DE PROJETOS E ATIVIDADES
============================================================

📁 PROJETO: Sistema de E-commerce
   Líder: Mariana Araújo
   Status: ativo
   Total de atividades: 2
   📋 Atividades:
      1. Configurar ambiente
         - Responsável: Mariana
         - Status: ⏳ EM ANDAMENTO
      2. Desenvolver API
         - Responsável: Carlos
         - Status: ⏳ EM ANDAMENTO
```

---         

## 🔁 7. Replica Set - Alta Disponibilidade

### O que é um Replica Set?
Um Replica Set é um conjunto de servidores MongoDB que mantêm cópias idênticas dos dados, garantindo alta disponibilidade e tolerância a falhas. Se o membro primário falha, um secundário é automaticamente eleito primário.

### Papéis dos membros:

Papel |	Função 
---------  | ----------- |
Primário | Recebe todas as operações de escrita. Suas alterações são registradas no oplog (operation log).
Secundário | Replica os dados do primário (via oplog) e pode atender leituras (se configurado). Torna-se primário em caso de falha.
Arbiter | Não armazena dados. Participa apenas da eleição do novo primário, servindo como "voto de desempate".

### Benefícios:
Failover automático: se o primário cair, um secundário assume

Redundância de dados: múltiplas cópias dos dados

Leituras distribuídas: pode-se configurar leituras nos secundários

---

## ⚙️ 8. Configuração do Replica Set com Docker Compose

### Arquivo docker-compose-replicaset.yml:
```yaml
version: '3.8'
services:
  mongo1:
    image: mongo:latest
    container_name: mongo1
    command: mongod --replSet rs0 --bind_ip_all
    ports:
      - "27017:27017"
    volumes:
      - mongo1_data:/data/db
    networks:
      - mongodb_net

  mongo2:
    image: mongo:latest
    container_name: mongo2
    command: mongod --replSet rs0 --bind_ip_all
    ports:
      - "27018:27017"
    volumes:
      - mongo2_data:/data/db
    networks:
      - mongodb_net

  mongo3:
    image: mongo:latest
    container_name: mongo3
    command: mongod --replSet rs0 --bind_ip_all
    ports:
      - "27019:27017"
    volumes:
      - mongo3_data:/data/db
    networks:
      - mongodb_net

volumes:
  mongo1_data:
  mongo2_data:
  mongo3_data:

networks:
  mongodb_net:
    driver: bridge
```

### Etapas para configurar o Replica Set:

Subir os containers:

```bash
docker-compose -f docker-compose-replicaset.yml up -d

Acessar um dos membros:

```bash
docker exec -it mongo1 mongosh
```

Inicializar o Replica Set:

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

Verificar o status:

```javascript
rs.status()
```

Verificar quem é o primário:

```javascript
rs.isMaster()
```

### Conexão com Replica Set no Python:

```python
from pymongo import MongoClient
```

# String de conexão para Replica Set
```
client = MongoClient(
    "mongodb://localhost:27017,localhost:27018,localhost:27019/?replicaSet=rs0"
)

db = client.AtividadesProj
```
