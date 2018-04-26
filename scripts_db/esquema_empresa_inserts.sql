insert into departamento 
(codDep, nomeDep, gerente)
values (3, 'RH', 9491);

insert into departamento 
(codDep, nomeDep, gerente)
values (4, 'Administrativo', 9492);

insert into empregado
(matricula, nome, depto)
values (9493, 'Xuxa', 2);

insert into empregado
(matricula, nome, depto)
values (9494, 'Sasha', 3);

insert into empregado
(matricula, nome, depto)
values (9495, 'José', 3);

insert into empregado
(matricula, nome, depto)
values (9496, 'Marcos', 3);

insert into empregado
(matricula, nome, depto)
values (9497, 'Maria', 3);

INSERT INTO `projeto`
(`codproj`,
`nome`,
`local`,
`depart`)
VALUES
(1,
'Projeto X',
'Caicó',
1
);

INSERT INTO `projeto`
(`codproj`,
`nome`,
`local`,
`depart`)
VALUES
(2,
'Projeto H',
'Caicó',
1
);

INSERT INTO `projeto`
(`codproj`,
`nome`,
`local`,
`depart`)
VALUES
(3,
'Projeto U',
'Caicó',
2
);

INSERT INTO `dependente`
(`coddepend`,
`matricula`,
`nome`,
`sexo`)
VALUES
(1,
9492,
'José Filho',
'M');

INSERT INTO `dependente`
(`coddepend`,
`matricula`,
`nome`,
`sexo`)
VALUES
(2,
9493,
'Umberto',
'M');

INSERT INTO `dependente`
(`coddepend`,
`matricula`,
`nome`,
`sexo`)
VALUES
(1,
9495,
'Doisberto',
'M');

INSERT INTO `alocacao`
(`matric`,
`codigop`,
`horas`)
VALUES
(9495,
 1,
 4.00
);
