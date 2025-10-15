### ORM
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


### Node
[Acessar documentação](https://nodejs.org/pt)

O Node.js é um ambiente de execução de código JavaScript fora do navegador, baseado no motor V8 do Google Chrome.
Ele permite criar aplicações do lado do servidor usando JavaScript, o que antes era restrito apenas ao front-end.
O Node é conhecido por seu modelo assíncrono e orientado a eventos, que oferece alta performance e escalabilidade — ideal para aplicações web, APIs e serviços em tempo real.
Com seu gerenciador de pacotes npm, é possível instalar facilmente bibliotecas e frameworks, como o Sequelize para ORM e o Express para criação de servidores HTTP.

### Rodando a aplicação

```bash
npm install
npm run dev
```