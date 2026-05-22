# Tarefa 03 - MongoDB

**Nome:** Vitória Geovanna de Assis Pereira

**Matrícula:** 20230039237

**Email:** vitoria.assis.067@ufrn.edu.br

# O que é MongoDB
O mongodb é um banco NoSQL que armazena dados no formato orientado a documentos, lançado em fevereiro de 2009 e desenvolvido em C++. Ele foi projetado para ter uma escalabilidade e suportar grandes volumes de dados não estruturados. Sendo o banco de dados que permite aos usuários acessar dados facilmente a partir de uma infinidade de linguagens de programação e outras ferramentas de dados. 

# Recursos utilizados
- MongoDB Compass
- Docker Compose
- JavaScript
- Node.js
- VScod

# Estrutura das pastas e arquivos
```text
database/
└── 20261/
    └── tarefas/
        └── vitoria31032003/
            ├── crud/
            │   ├── app.js
            │   ├── package.json
            │   └── package-lock.json
            ├── mongodb/
            │   └── init.js
            ├── tarefa-mongodb.md
            └── docker-compose.yml
```

# Foi utilizado um processo para acessar o servidor do MongoDB
1. O mongodb foi inicializado usando Docker com o comando: **docker compose up --d**.
2. Após isso, o servidor permaneceu executando na porta 2707.
3. Foi utilizada uma aplicação de CRUD em JavaScript com Node.js e biblioteca **mongodb** para se conectar ao banco.
4. Depois disso, de se conectar ao banco, a aplicação de CRUD foi realizada com operação de inserir, consultar, atualizar e deletar dados no banco.

# Links dos arquivos
Script de inicialização: (https://github.com/vitoria31032003/bsi-tasks/blob/master/database/20261/tarefas/vitoria31032003/mongodb/init.js)
Aplicação do CRUD: (https://github.com/vitoria31032003/bsi-tasks/blob/master/database/20261/tarefas/vitoria31032003/crud/app.js)
