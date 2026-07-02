-- Povoamento Inicial

INSERT INTO departamento (sigla, descricao, codGerente) VALUES ('DHC', 'Dep História', NULL);
INSERT INTO departamento (sigla, descricao, codGerente) VALUES ('DCT', 'Dep Computação', NULL);
INSERT INTO departamento (sigla, descricao, codGerente) VALUES ('DGC', 'Dep Geografia', NULL);
INSERT INTO departamento (sigla, descricao, codGerente) VALUES ('DXT', NULL, NULL);

-- Adicionando Gerentes

INSERT INTO funcionario (nome, sexo, dtNasc, salario, codSupervisor, codDepto) VALUES ('Ana', 'F', '1988-05-07', 2500.00, NULL, 1);
INSERT INTO funcionario (nome, sexo, dtNasc, salario, codSupervisor, codDepto) VALUES ('Taciano', 'M', '1980-01-25', 2500.00, NULL, 2);

UPDATE departamento SET codGerente = 1 WHERE sigla = 'DHC';
UPDATE departamento SET codGerente = 2 WHERE sigla = 'DCT';

-- Adicionando Funcionários

INSERT INTO funcionario (nome, sexo, dtNasc, salario, codSupervisor, codDepto) VALUES ('Maria', 'F', '1981-07-01', 2500.00, 1, 1);
INSERT INTO funcionario (nome, sexo, dtNasc, salario, codSupervisor, codDepto) VALUES ('Josefa', 'F', '1986-09-17', 2500.00, 1, 1);