
Nome: Mariana Araujo de Medeiros</br>
Matricula: 	20200139394</br>
Usuário github: araujodemedeirosmariana-jpg</br>
E-mail: araujodemedeirosmariana@gmail.com

## 📚 Tarefa MongoDB

A tarefa consiste na implementação de um sistema de gerenciamento de atividades em projetos utilizando MongoDB.

### 📁 Arquivos da tarefa:
- [Documentação completa](./tarefa-mongodb.md)
- [Programa CRUD](./crud_mongodb.py)
- [Script de inicialização](./init.js)
- [Docker Compose](./docker-compose-replicaset.yml)

### ✅ Funcionalidades:
- CRUD completo (Create, Read, Update, Delete)
- MongoDB rodando em container Docker
- Banco de dados `AtividadesProj` com projetos, atividades e empregados
- Script de inicialização com dados de exemplo

### 🚀 Como executar:
```bash
# Iniciar MongoDB
docker start mongodb

# Executar programa CRUD
python3 database/20261/tarefas/araujodemedeirosmariana-jpg/crud_mongodb.py
