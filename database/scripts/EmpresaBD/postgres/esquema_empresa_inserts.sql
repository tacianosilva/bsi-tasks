insert into departamento (nomeDep, gerente)
values
('RH', 9491),
('Administrativo', 9492);

insert into empregado (matricula, nome, depto, sexo, supervisor, salario)
values
(9493, 'Xuxa', 2, 'F', NULL, 1985),
(9494, 'Sasha', 3, 'F', 9491, 1550),
(9495, 'José', 3, 'M', 9492, 3000),
(9496, 'Marcos', 3, 'M', 9491, 1789),
(9497, 'Maria', 3, 'F', 9492, 3468);

INSERT INTO projeto (nome, localizacao, depart)
VALUES
('Projeto X', 'Caicó', 1),
('Projeto H', 'Caicó', 1),
('Projeto U', 'Caicó', 2);

INSERT INTO dependente (matricula, nome, sexo)
VALUES
(9492, 'José Filho', 'M'),
(9493, 'Sasha', 'F'),
(9495, 'Umberto', 'M'),
(9495, 'Doisberto', 'M'),
(9497, 'Maria Filha', 'F');

INSERT INTO alocacao (matric, codProj, horas)
VALUES
(9495, 1, 4.00);
