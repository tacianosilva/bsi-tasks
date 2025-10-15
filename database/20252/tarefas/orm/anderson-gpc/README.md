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


### Rodando a aplicação

```bash
cd /database/20252/tarefas/orm/anderson-gpc
npm install
npm run dev
```