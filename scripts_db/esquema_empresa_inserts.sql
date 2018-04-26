insert into departamento 
(nomeDep, gerente)
values ('RH', 9491);

insert into departamento 
(nomeDep, gerente)
values ('Administrativo', 9492);

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
(`nome`,
`localizacao`,
`depart`)
VALUES
('Projeto X',
'Caicó',
1
);

INSERT INTO `projeto`
(`nome`,
`localizacao`,
`depart`)
VALUES
('Projeto H',
'Caicó',
1
);

INSERT INTO `projeto`
(`nome`,
`localizacao`,
`depart`)
VALUES
('Projeto U',
'Caicó',
2
);

INSERT INTO `dependente`
(`matricula`,
`nome`,
`sexo`)
VALUES
(9492,
'José Filho',
'M');

INSERT INTO `dependente`
(`matricula`,
`nome`,
`sexo`)
VALUES
(9493,
'Umberto',
'M');

INSERT INTO `dependente`
(`matricula`,
`nome`,
`sexo`)
VALUES
(9495,
'Doisberto',
'M');

INSERT INTO `alocacao`
(`matric`,
`codProj`,
`horas`)
VALUES
(9495,
 1,
 4.00
);
