# Respostas

## Scripts SQL

#### 1. Inserir uma atividade em algum projeto

```sql

insert into atividade 
(descricao, projeto, data_inicio, data_fim) 
values ('TAS - Atividade 13', 4, '2017-11-10', '2019-08-19');

```

#### 2. Atualizar o líder de algum projeto

```sql
update projeto set responsavel = 8 where codigo = 3;
```

#### 3. Listar todos os projetos e suas atividades
```sql
select  pr.nome as Projeto, 
coalesce(a.descricao, 'Sem Atividades' ) as Atividade, 
a.data_inicio as Inicio, a.data_fim as Fim
from projeto pr
	left join atividade a on pr.codigo = a.projeto
	order by pr.nome;
```
## ODBC (Open Database Connectivity)
É uma interface padrão para conectar aplicações a diferentes bancos de dados
independente da linguagem ou do sistema gerenciador. Usa chamadas de API procedurais
Embora tenha origem no Windows, hoje pode ser usada em outros sistemas também.

## JDBC (Java Database Connectivity)
É o equivalente do ODBC para Java. Fornece uma interface orientada a objetos que
permite conectar, enviar consultas e manipular resultados em bancos de dados. Além
disso, possibilita controlar como o usuário acessa o banco, integrando-se naturalmente
com o ecossistema Java.

## ORM

Em Java, o ORM (Object-Relational Mapping) é uma técnica que permite trabalhar com dados do
banco usando objetos, sem precisar escrever comandos SQL diretamente. O framework mais usado
é o Hibernate, que implementa a especificação JPA (Java Persistence API) e faz o mapeamento
entre classes e tabelas, facilitando operações como inserir, atualizar e consultar dados de
forma automatizada.
