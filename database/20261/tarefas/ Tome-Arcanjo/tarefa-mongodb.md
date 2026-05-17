# Tarefa mongodb

**Link para programa: https://github.com/Tome-arcanjo/bdwork2**

**Link para scripts: https://github.com/Tome-arcanjo/bdwork2/blob/main/init.js**


# Tarefa - MongoDB

## MongoDB com JavaScript

O MongoDB é um Sistema Gerenciador de Banco de Dados (SGBD) NoSQL orientado a documentos. Diferente dos bancos de dados relacionais tradicionais, ele não utiliza tabelas e linhas para armazenar informações. Em vez disso, os dados são organizados em documentos no formato BSON, que é semelhante ao JSON utilizado em JavaScript.

O MongoDB é bastante utilizado no desenvolvimento de aplicações modernas devido à sua flexibilidade, escalabilidade e facilidade de integração com JavaScript e Node.js.

## Principais características do MongoDB

- **Orientado a documentos:**  
  Os dados são armazenados em documentos, permitindo representar informações de maneira mais natural e flexível.

- **Modelo NoSQL:**  
  Não depende de tabelas relacionais e pode lidar melhor com grandes volumes de dados e aplicações distribuídas.

- **Esquema flexível:**  
  Cada documento pode possuir estruturas diferentes, facilitando alterações durante o desenvolvimento do sistema.

- **Escalabilidade:**  
  O MongoDB oferece suporte à distribuição de dados em múltiplos servidores, permitindo crescimento horizontal da aplicação.

- **Alta performance:**  
  Possui bom desempenho em operações de leitura e escrita, principalmente em aplicações web modernas.

- **Integração com JavaScript:**  
  Como utiliza um formato semelhante ao JSON, o MongoDB se integra facilmente com aplicações desenvolvidas em JavaScript.

## Conclusão

O MongoDB é um dos bancos de dados NoSQL mais populares da atualidade. Sua estrutura orientada a documentos oferece maior flexibilidade no armazenamento de dados, tornando-o uma excelente escolha para aplicações modernas, escaláveis e integradas ao ecossistema JavaScript.

# Foi utilizado o Railway para provisionamento do servidor MongoDB em nuvem, como alternativa ao uso local via Docker.

## Banco utilizado:
**- AtividadesProj**

**Usuário criado automaticamente pelo Railway.**

**A conexão foi realizada utilizando a string fornecida pela plataforma.**

# Script de inicialização em js

## Link: https://github.com/Tome-arcanjo/bdwork2/blob/main/init.js

# Crud integrado ao bd

## Link: https://github.com/Tome-arcanjo/bdwork2/blob/main/app.js

# Replica Set no MongoDB

Um Replica Set no MongoDB é um conjunto de servidores MongoDB que mantêm cópias sincronizadas do mesmo banco de dados. Esse mecanismo é utilizado para garantir alta disponibilidade, redundância e tolerância a falhas no sistema.

Os membros de um Replica Set trabalham juntos para garantir que os dados permaneçam acessíveis mesmo em caso de falha de algum servidor.

## Papéis dos membros do Replica Set

### Primário (Primary)

O membro primário é o servidor principal do Replica Set. Todas as operações de escrita, como inserções, atualizações e remoções de dados, são realizadas nele.

Os demais membros replicam automaticamente os dados armazenados no primário.

Caso o servidor primário falhe, um novo primário é eleito automaticamente entre os secundários.

### Secundário (Secondary)

Os membros secundários mantêm cópias atualizadas dos dados do servidor primário através do processo de replicação.

Eles podem assumir o papel de primário em caso de falha do atual primário. Além disso, podem ser utilizados para operações de leitura, ajudando na distribuição de carga do sistema.

### Arbiter

O arbiter é um membro especial do Replica Set que não armazena dados.

Sua principal função é participar das votações para eleição de um novo primário quando ocorre alguma falha no Replica Set.

Ele é utilizado principalmente para desempatar votações em conjuntos com número par de membros.

# Configuração de um Replica Set no Mongo Shell

Para transformar o servidor MongoDB em um Replica Set de três membros utilizando Mongo Shell, seria necessário iniciar as instâncias MongoDB com suporte a replicação habilitado e, em seguida, configurar o conjunto através do shell.

## Etapas Essenciais

1. Iniciar as três instâncias MongoDB com o parâmetro `--replSet`;
2. Acessar uma das instâncias utilizando o Mongo Shell;
3. Inicializar o Replica Set;
4. Adicionar os três membros ao conjunto;
5. Verificar o status da replicação.

---

# Inicialização do Replica Set

Após iniciar as instâncias MongoDB, acessar o shell:

```bash
mongosh
```

Em seguida, executar:

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

---

# Verificação do Status

Para verificar se o Replica Set foi configurado corretamente:

```javascript
rs.status()
```

O comando exibirá:
- o membro primário (PRIMARY);
- os membros secundários (SECONDARY);
- informações sobre sincronização e replicação.

---

# Banco de Dados

Após a configuração do Replica Set, o banco de dados `AtividadesProj` poderá ser utilizado normalmente, com replicação automática dos dados entre os três membros do conjunto.

---

# Benefícios da Configuração

A utilização de Replica Set fornece:
- alta disponibilidade;
- redundância de dados;
- tolerância a falhas;
- eleição automática de um novo primário em caso de falha.



