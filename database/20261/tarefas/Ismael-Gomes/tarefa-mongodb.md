# Tarefa Individual - MongoDB

## Resumo

Esta parte da atividade implementa um banco de dados MongoDB para gerenciar projetos, empregados e atividades de um departamento.

O banco foi configurado com Docker e possui um programa CRUD desenvolvido em Java, utilizando o MongoDB Driver. A aplicação permite listar projetos e atividades, criar atividades, atualizar o líder de um projeto e remover atividades.

---

## Estrutura da implementação

A estrutura criada para a parte MongoDB foi:

parte3-mongodb/
- docker-compose.yml
- pom.xml
- .gitignore
- scripts/init-mongo.js
- replica-set/
- src/main/java/br/bsi/ismael/mongodb/App.java

---

## Banco de dados

O banco de dados utilizado foi:

AtividadesProj

O usuário criado para a aplicação foi:

atividades_user

---

## Coleções criadas

Foram criadas três coleções principais:

- empregados
- projetos
- atividades

---

## Coleção empregados

A coleção empregados armazena os funcionários do departamento.

Exemplo de documento:

{
  nome: "Ana Souza",
  email: "ana.souza@empresa.com",
  cargo: "Gerente de Projetos",
  departamento: "Tecnologia"
}

Campos principais:

- nome: nome do empregado;
- email: e-mail do empregado;
- cargo: cargo do empregado;
- departamento: departamento ao qual pertence.

---

## Coleção projetos

A coleção projetos armazena os projetos do departamento.

Exemplo de documento:

{
  nome: "Sistema de Controle de Atividades",
  descricao: "Sistema para organizar atividades internas do departamento.",
  liderId: ObjectId("..."),
  membrosIds: [ObjectId("..."), ObjectId("...")],
  status: "Em andamento",
  dataInicio: ISODate("2026-03-01")
}

Campos principais:

- nome: nome do projeto;
- descricao: descrição do projeto;
- liderId: referência ao empregado líder do projeto;
- membrosIds: lista de empregados participantes;
- status: situação atual do projeto;
- dataInicio: data de início do projeto.

---

## Coleção atividades

A coleção atividades armazena as tarefas vinculadas aos projetos.

Exemplo de documento:

{
  titulo: "Criar modelo de dados",
  descricao: "Definir as coleções principais do sistema.",
  projetoId: ObjectId("..."),
  responsavelId: ObjectId("..."),
  status: "Concluída",
  prioridade: "Alta",
  estimativaHoras: 6,
  criadoEm: ISODate("...")
}

Campos principais:

- titulo: título da atividade;
- descricao: descrição da atividade;
- projetoId: referência ao projeto da atividade;
- responsavelId: referência ao empregado responsável;
- status: situação atual da atividade;
- prioridade: prioridade da atividade;
- estimativaHoras: tempo estimado para conclusão;
- criadoEm: data de criação da atividade.

---

## Script de inicialização

O script de inicialização está localizado em:

parte3-mongodb/scripts/init-mongo.js

Esse script é executado automaticamente quando o container MongoDB é iniciado pela primeira vez.

Ele realiza as seguintes ações:

- cria o banco AtividadesProj;
- cria o usuário atividades_user;
- cria as coleções empregados, projetos e atividades;
- define validações básicas para os documentos;
- insere dados iniciais;
- cria índices nas coleções.

---

## Como subir o MongoDB

Entre na pasta da parte MongoDB:

cd parte3-mongodb

Suba o container:

docker compose up -d

Verifique se o container está rodando:

docker ps

O container esperado é:

atividadesproj-mongo

---

## Como acessar o MongoDB pelo terminal

Execute:

docker exec -it atividadesproj-mongo mongosh -u root -p root123 --authenticationDatabase admin

Dentro do mongosh, selecione o banco:

use AtividadesProj

Liste as coleções:

show collections

---

## Programa CRUD em Java

O programa CRUD foi desenvolvido em Java e está localizado em:

parte3-mongodb/src/main/java/br/bsi/ismael/mongodb/App.java

A aplicação usa o driver oficial do MongoDB para Java, configurado no arquivo:

parte3-mongodb/pom.xml

---

## Como executar o CRUD

Com o MongoDB rodando, execute:

mvn compile exec:java

O sistema exibe um menu com as seguintes opções:

1 - Listar projetos e atividades
2 - Criar nova atividade
3 - Atualizar líder de um projeto
4 - Remover atividade
0 - Sair

---

## Operações implementadas

### Create

A opção 2 - Criar nova atividade permite inserir uma nova atividade em um projeto já existente.

### Read

A opção 1 - Listar projetos e atividades lista os projetos cadastrados e suas atividades.

### Update

A opção 3 - Atualizar líder de um projeto permite alterar o líder de um projeto existente.

### Delete

A opção 4 - Remover atividade remove uma atividade pelo título informado.

---

## Replica Set no MongoDB

Um Replica Set no MongoDB é um conjunto de servidores MongoDB que mantém cópias dos mesmos dados. Ele é usado para garantir maior disponibilidade e tolerância a falhas.

Em uma configuração básica de Replica Set existem três tipos de membros:

- Primário: recebe as operações de escrita;
- Secundário: mantém uma cópia dos dados do primário;
- Árbitro: participa das eleições, mas não armazena dados.

Quando o nó primário falha, os secundários realizam uma eleição e um novo primário pode assumir automaticamente.

---

## Exemplo de configuração de Replica Set

Um exemplo simples de configuração com três membros pode ser feito com três containers MongoDB:

services:
  mongo1:
    image: mongo:7.0
    container_name: mongo-rs1
    command: ["mongod", "--replSet", "rsAtividades", "--bind_ip_all"]
    ports:
      - "27018:27017"

  mongo2:
    image: mongo:7.0
    container_name: mongo-rs2
    command: ["mongod", "--replSet", "rsAtividades", "--bind_ip_all"]
    ports:
      - "27019:27017"

  mongo3:
    image: mongo:7.0
    container_name: mongo-rs3
    command: ["mongod", "--replSet", "rsAtividades", "--bind_ip_all"]
    ports:
      - "27020:27017"

Depois de subir os containers, o Replica Set pode ser iniciado com:

rs.initiate({
  _id: "rsAtividades",
  members: [
    { _id: 0, host: "mongo-rs1:27017" },
    { _id: 1, host: "mongo-rs2:27017" },
    { _id: 2, host: "mongo-rs3:27017" }
  ]
})

Para verificar o status:

rs.status()

---

## Resultado do teste

Durante o teste da aplicação, o container MongoDB foi iniciado corretamente e o programa Java conseguiu listar os projetos e atividades cadastrados inicialmente.

Foram exibidos os seguintes projetos:

- Sistema de Controle de Atividades;
- Portal de Relatórios;
- Automação de Processos.

Isso confirma que o Docker, o script de inicialização, o banco MongoDB e o CRUD Java estão funcionando corretamente.

---

## Conclusão

A atividade implementa um ambiente MongoDB com Docker, cria um banco chamado AtividadesProj, define coleções com documentos relacionados entre empregados, projetos e atividades, insere dados iniciais e disponibiliza um CRUD em Java para manipular os dados.
