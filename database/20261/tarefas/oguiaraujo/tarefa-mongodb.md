# Tarefa - MongoDB

[Implementação do MongoDB](https://github.com/oguiaraujo/BD2.git)


## Resumo sobre MongoDB

O **MongoDB** é um SGBD NoSQL orientado a documentos (*document database*), lançado em 2009 pela MongoDB, Inc. Em vez de armazenar dados em tabelas e linhas como os bancos relacionais, o MongoDB armazena dados em **documentos BSON** (*Binary JSON*) — estruturas flexíveis e auto-descritivas que suportam tipos aninhados, arrays e subdocumentos.

### Principais características

**Schema flexível.** Documentos de uma mesma coleção podem ter campos diferentes, sem necessidade de migrações de esquema a cada mudança no modelo de dados.

**Escalabilidade horizontal (Sharding).** O MongoDB distribui dados automaticamente entre múltiplos servidores (*shards*), permitindo escalar a capacidade de armazenamento e throughput horizontalmente.

**Alta disponibilidade (Replica Sets).** Grupos de instâncias sincronizadas que garantem redundância de dados e failover automático em caso de falha de nó.

**Linguagem de consulta rica (MQL).** Suporte a filtros, projeções, ordenação, índices compostos, geoespaciais e textuais, além de um poderoso *Aggregation Pipeline* para transformação e análise de dados.

**Transações ACID multi-documento.** A partir da versão 4.0, o MongoDB suporta transações com garantias de atomicidade, consistência, isolamento e durabilidade em múltiplos documentos e coleções.

### Conceitos fundamentais

| Conceito | Descrição | Equivalente relacional |
|---|---|---|
| **Documento** | Unidade básica de dado em formato BSON | Linha (*row*) |
| **Coleção** | Agrupamento de documentos sem esquema fixo | Tabela |
| **Campo** | Par chave-valor dentro de um documento | Coluna |
| **`_id`** | Campo obrigatório e único por documento | Chave primária |
| **Embedding** | Subdocumentos aninhados dentro de um documento | JOIN desnormalizado |
| **Referencing** | Referência por `_id` entre coleções | Chave estrangeira |

O MongoDB é especialmente adequado para dados semi-estruturados, sistemas com esquema evolutivo, alta carga de leitura/escrita e aplicações que exigem escalabilidade horizontal com alta disponibilidade.

---

## Esquema das Coleções

O banco de dados `AtividadesProj` possui três coleções. As atividades são armazenadas **embutidas** (*embedded*) dentro de cada projeto, seguindo o padrão de modelagem orientada a documentos.

**`empregados`**
```json
{
  "_id": "ObjectId",
  "nome": "string",
  "email": "string",
  "cargo": "string",
  "departamento": "string",
  "data_admissao": "Date"
}
```

**`projetos`** (com atividades embutidas)
```json
{
  "_id": "ObjectId",
  "nome": "string",
  "descricao": "string",
  "status": "ativo | concluido | suspenso",
  "lider_id": "ObjectId (ref: empregados)",
  "data_inicio": "Date",
  "data_fim_prevista": "Date",
  "atividades": [
    {
      "titulo": "string",
      "descricao": "string",
      "responsavel_id": "ObjectId (ref: empregados)",
      "status": "pendente | em_andamento | concluida",
      "prioridade": "baixa | media | alta",
      "data_inicio": "Date",
      "data_fim_prevista": "Date"
    }
  ]
}
```

**`departamentos`**
```json
{
  "_id": "ObjectId",
  "nome": "string",
  "sigla": "string",
  "responsavel_id": "ObjectId (ref: empregados)"
}
```

---

## Operações CRUD

O programa [`crud/crud.py`](crud/crud.py) conecta-se ao MongoDB e implementa as quatro operações abaixo usando a biblioteca `pymongo`.

**a) Create — Inserir nova atividade em um projeto existente**

Usa o operador `$push` para adicionar um subdocumento ao array `atividades` do projeto sem substituir os existentes.

```python
db.projetos.update_one(
    {"nome": nome_projeto},
    {"$push": {"atividades": atividade}},
)
```

**b) Read — Listar todos os projetos e suas atividades**

Busca todos os documentos da coleção `projetos` com projeção nos campos relevantes e itera sobre o array `atividades` de cada um.

```python
projetos = db.projetos.find({}, {"nome": 1, "status": 1, "atividades": 1})
```

**c) Update — Atualizar o líder de um projeto específico**

Busca o `_id` do novo líder na coleção `empregados` e usa `$set` para substituir o campo `lider_id` do projeto.

```python
db.projetos.update_one(
    {"nome": nome_projeto},
    {"$set": {"lider_id": lider["_id"]}},
)
```

**d) Delete — Remover uma atividade de um projeto**

Usa o operador `$pull` para remover do array `atividades` o subdocumento cujo `titulo` corresponde ao informado.

```python
db.projetos.update_one(
    {"nome": nome_projeto},
    {"$pull": {"atividades": {"titulo": titulo_atividade}}},
)
```

---

## Alta Disponibilidade — Replica Sets

### O que é um Replica Set?

Um **Replica Set** no MongoDB é um grupo de instâncias `mongod` que mantêm o **mesmo conjunto de dados** de forma sincronizada e contínua. Ele é o mecanismo principal de alta disponibilidade do MongoDB, oferecendo:

- **Redundância de dados** — cópias em múltiplos nós;
- **Failover automático** — se o primário falha, os secundários elegem um novo primário sem intervenção manual;
- **Recuperação de falhas** — nós que ficam offline reintegram-se ao conjunto ao voltar, replicando as operações perdidas via *oplog*;
- **Leituras escaláveis** — leituras podem ser direcionadas a secundários com *read preference* configurável.

### Papéis dos membros

**Primário (*Primary*)** — única instância que aceita operações de escrita (insert, update, delete). Registra todas as suas operações no ***oplog*** (*operations log*), que os secundários consomem para replicar as mudanças. Só pode haver um primário por vez, eleito por votação entre os membros.

**Secundário (*Secondary*)** — mantém uma cópia dos dados replicando o oplog do primário de forma contínua e assíncrona. Pode atender leituras (se habilitado) e participa das eleições. Um Replica Set pode ter até 50 membros, com até 7 votantes.

**Árbitro (*Arbiter*)** — membro especial que **não armazena dados** e **nunca se torna primário**. Sua única função é participar das eleições para garantir que haja um número ímpar de votos e evitar empates. É usado quando o custo de uma terceira instância completa é inviável.

```
┌─────────────┐   oplog   ┌─────────────┐
│   PRIMÁRIO  │──────────►│  SECUNDÁRIO │
│  (escrita)  │           │  (leitura)  │
└─────────────┘           └─────────────┘
       │                        │
       └──────── eleição ────────┘
                    │
             ┌─────────────┐
             │   ÁRBITRO   │
             │   (voto)    │
             └─────────────┘
```

> **Atenção:** o árbitro não contribui para a redundância de dados. Em produção crítica, prefira três membros completos (um primário e dois secundários).

---

## Configuração do Replica Set com Docker

O arquivo [`docker-compose-replicaset.yml`](docker-compose-replicaset.yml) define três containers (`mongo1`, `mongo2`, `mongo3`) na mesma rede Docker, cada um iniciado com a flag `--replSet rs0`.

| Container | Papel inicial | Porta externa |
|---|---|---|
| `mongo1` | Primário | 27017 |
| `mongo2` | Secundário | 27018 |
| `mongo3` | Secundário | 27019 |

**Passo 1 — Subir os containers**

```bash
docker compose -f docker-compose-replicaset.yml up -d
```

**Passo 2 — Acessar o shell do primeiro nó**

```bash
docker exec -it mongo1 mongosh
```

**Passo 3 — Inicializar o Replica Set**

```javascript
rs.initiate({
  _id: "rs0",
  members: [
    { _id: 0, host: "mongo1:27017", priority: 2 },
    { _id: 1, host: "mongo2:27017", priority: 1 },
    { _id: 2, host: "mongo3:27017", priority: 1 },
  ],
})
```

**Passo 4 — Verificar o status**

```javascript
rs.status()   // exibe o papel de cada membro (PRIMARY / SECONDARY)
rs.conf()     // exibe a configuração atual do Replica Set
```

**Passo 5 — Criar banco e usuário**

```javascript
use admin
db.createUser({
  user: "admin", pwd: "admin123",
  roles: [{ role: "root", db: "admin" }],
})

use AtividadesProj
db.createUser({
  user: "app_user", pwd: "app_senha123",
  roles: [{ role: "readWrite", db: "AtividadesProj" }],
})
```

**Passo 6 — Conectar a aplicação**

A string de conexão para Replica Set inclui todos os hosts e o nome do conjunto:

```
mongodb://app_user:app_senha123@localhost:27017,localhost:27018,localhost:27019/AtividadesProj?replicaSet=rs0
```

**Testando o failover**

```bash
# Derrubar o primário
docker stop mongo1

# Verificar a nova eleição em outro nó
docker exec -it mongo2 mongosh --eval "rs.status()"

# Restaurar o nó (volta como secundário e sincroniza automaticamente)
docker start mongo1
```

---