# Tarefa - MongoDB

## 👤 Dados do aluno
- **Nome:** Laety Maniery de Araújo Batista
- **Matrícula:** 20220002663
- **E-mail:** laety.maniery.119@ufrn.edu.br

## 📌 1. O que é MongoDB

MongoDB é um SGBD NoSQL orientado a documentos (document database), onde os dados são armazenados em formato BSON (similar ao JSON).

### Características principais:
- Estrutura flexível (schema dinâmico)
- Alta escalabilidade
- Alto desempenho
- Suporte a replicação e sharding
- Modelo baseado em documentos

---

## 📌 2. Modelo de dados (coleções)

### Empregados
```json
{ "_id": 1, "nome": "Ana", "cargo": "Dev" }

## 🚀 Execução do Projeto

### Subir o MongoDB
docker compose up -d

### Verificar containers
docker ps

### Acessar o MongoDB
mongosh -u admin -p admin123

### Selecionar banco
use AtividadesProj

### Executar seed
load("scripts/seed.js")

### Rodar aplicação
pip install pymongo
python src/app.py

### Parar ambiente
docker compose down