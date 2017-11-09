insert into empregado
(matricula, nome)
values (9491, 'Ana');

insert into empregado
(matricula, nome)
values (9491, 'Taciano');

insert into departamento 
(codDep, nomeDep, gerente)
values (1, 'Vendas', 9491);

insert into departamento 
(codDep, nomeDep, gerente)
values (2, 'Compras', 9492);

update empregado set depto = 1 where matricula = '9491';
update empregado set depto = 1 where matricula = '9492';

update empregado set dataNasc = '2000-12-11' where matricula = '9491';