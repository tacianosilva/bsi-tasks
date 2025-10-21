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

