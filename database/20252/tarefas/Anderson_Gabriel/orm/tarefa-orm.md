# ORM
[Acessar documentação](https://sequelize.org/)

Sequelize é um ORM (Object-Relational Mapping) para Node.js, que permite interagir com bancos de dados SQL usando JavaScript/TypeScript em vez de escrever queries SQL diretamente.

Suporta diversos bancos de dados: PostgreSQL, MySQL, MariaDB, SQLite, MSSQL, entre outros.

Facilita CRUD, relações entre tabelas, validações e migrações de forma programática.

| Conceito           | Descrição                                                                                 |
|-------------------|-------------------------------------------------------------------------------------------|
| **Model**          | Representa uma tabela do banco. Cada instância do model representa uma linha da tabela.  |
| **Instance**       | Um objeto de um model específico, equivalente a um registro do banco.                   |
| **DataTypes**      | Tipos de dados que você define nos campos do model (STRING, INTEGER, BOOLEAN, DATE, etc.). |
| **Associations**   | Relacionamentos entre modelos: `hasOne`, `hasMany`, `belongsTo`, `belongsToMany`.        |
| **Sequelize Methods** | Métodos para manipular dados: `findAll`, `findByPk`, `create`, `update`, `destroy`.   |


# Node
[Acessar documentação](https://nodejs.org/pt)

O Node.js é um ambiente de execução de código JavaScript fora do navegador, baseado no motor V8 do Google Chrome.
Ele permite criar aplicações do lado do servidor usando JavaScript, o que antes era restrito apenas ao front-end.
O Node é conhecido por seu modelo assíncrono e orientado a eventos, que oferece alta performance e escalabilidade — ideal para aplicações web, APIs e serviços em tempo real.
Com seu gerenciador de pacotes npm, é possível instalar facilmente bibliotecas e frameworks, como o Sequelize para ORM e o Express para criação de servidores HTTP.

# ODBC
> ODBC (Open Database Connectivity) é uma interface padrão para conectar aplicações a bancos de dados, independente da linguagem ou SGBD.


**Drive Postgresql:**

psqlODBC é o driver oficial do PostgreSQL para ODBC, permitindo que aplicações usem a API ODBC para se comunicar com PostgreSQL.

O ODBC traduz comandos da aplicação em SQL compreensível pelo PostgreSQL.

**Drives:**

Driver → software que conhece o protocolo do PostgreSQL (psqlodbcw.so para Unicode, psqlodbca.so para ANSI).

Driver Manager → gerencia a conexão entre a aplicação e o driver (no Linux: unixODBC).

DSN (Data Source Name) → configuração de conexão (nome, host, porta, usuário, senha, banco).


# Rodando a aplicação

```bash
# instalar drive odbc para postgresql
sudo apt install odbc-postgresql
# dar pull na imagem do postgresql
docker pull postgresql:17
# criar container
docker run -d   --name bd_postgres   -e POSTGRES_USER=admin   -e POSTGRES_PASSWORD=senha   -e POSTGRES_DB=atividade_db   -p 5432:5432   postgres:17
# instalar dependências do projeto
npm install
```

## Arquivo odbc.ini
No diretório **/etc/** criar **odbc.ini**:
> [MeuPostgres] <br>
>Driver = PostgreSQL Unicode <br>
>Database = atividade_db <br>
>Servername = 127.0.0.1 <br>
>UserName = admin <br>
>Password = senha <br>
>Port = 5432 <br>

---
## Rodando para ORM
```bash
npm run orm
```

## Rodando para ODBC
```bash
npm run odbc
```

# Querys - SQL

**Pegar todas as atividades e projetos**
```sql
SELECT 
    a.codigo,
    a.descricao AS atividade_descricao,
    a.projeto AS projeto_codigo,
    a.data_inicio,
    a.data_fim,
    p.nome AS projeto_nome,
    p.descricao AS projeto_descricao
    FROM atividade a
    LEFT JOIN projeto p ON p.codigo = a.projeto;
```

**Criar atividade**
```sql
INSERT INTO atividade (descricao, projeto, data_fim, data_inicio)
VALUES (
    defina_sua_descricao,
    defina_codigo__projeto,
    defina_sua_data_fim,
    defina_sua_data_inicio
)
```

**Mudar responsável do projeto**
```sql
UPDATE projeto SET responsavel = defina_codigo_responsavel
WHERE codigo = defina_codigo_projeto
```