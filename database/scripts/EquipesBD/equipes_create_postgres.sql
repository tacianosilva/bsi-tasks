DROP TABLE IF EXISTS atividade_membro;
DROP TABLE IF EXISTS atividade_projeto;
DROP TABLE IF EXISTS atividade;
DROP TABLE IF EXISTS projeto;
DROP TABLE IF EXISTS membro;
DROP TABLE IF EXISTS equipe;
DROP TABLE IF EXISTS departamento CASCADE;
DROP TABLE IF EXISTS funcionario;

CREATE TABLE funcionario (
  codigo serial,
  nome varchar(100) NOT NULL,
  sexo char(1) DEFAULT NULL,
  data_nasc date DEFAULT NULL,
  salario decimal(10,2) DEFAULT NULL,
  supervisor int,
  depto int,
  PRIMARY KEY (codigo),
  CONSTRAINT funcSuperFK FOREIGN KEY (supervisor) REFERENCES funcionario(codigo) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE departamento (
  codigo serial,
  nome varchar(50) NOT NULL,
  sigla varchar(15) NOT NULL UNIQUE,
  descricao varchar(200) NOT NULL,
  gerente int,
  PRIMARY KEY (codigo),
  CONSTRAINT depGerenteFK FOREIGN KEY (gerente) REFERENCES funcionario(codigo) ON DELETE SET NULL ON UPDATE CASCADE
);

ALTER TABLE funcionario ADD CONSTRAINT funcDeptoFK FOREIGN KEY (depto) REFERENCES departamento(codigo) ON DELETE SET NULL ON UPDATE CASCADE;

CREATE TABLE equipe (
  codigo serial,
  nome_equipe varchar(50) DEFAULT NULL,
  PRIMARY KEY (codigo)
);

CREATE TABLE membro (
  codigo serial,
  cod_equipe int,
  cod_funcionario int,
  PRIMARY KEY (codigo),
  FOREIGN KEY (cod_equipe) references equipe(codigo) on delete set null,
  FOREIGN KEY (cod_funcionario) references funcionario(codigo) on delete set null
);

CREATE TABLE projeto (
  codigo serial,
  nome varchar(50) NOT NULL,
  descricao varchar(200) DEFAULT NULL,
  depto int,
  responsavel int,
  data_inicio date DEFAULT NULL,
  data_fim date DEFAULT NULL,
  situacao varchar(45) DEFAULT NULL,
  data_conclusao date DEFAULT NULL,
  cod_equipe int,
  PRIMARY KEY (codigo),
  FOREIGN KEY (depto) references departamento(codigo) on delete set null,
  FOREIGN KEY (responsavel) references funcionario(codigo) on delete set null,
  FOREIGN KEY (cod_equipe) references equipe(codigo) on delete set null
);

CREATE TABLE atividade (
  codigo serial,
  titulo varchar(50) NOT NULL,
  descricao varchar(150) DEFAULT NULL,
  data_inicio date DEFAULT NULL,
  data_fim date DEFAULT NULL,
  situacao varchar(45) DEFAULT NULL,
  data_conclusao date DEFAULT NULL,
  PRIMARY KEY (codigo)
);

CREATE TABLE atividade_projeto (
  cod_atividade int,
  cod_projeto int,
  PRIMARY KEY (cod_atividade, cod_projeto),
  FOREIGN KEY (cod_atividade) references atividade(codigo),
  FOREIGN KEY (cod_projeto) references projeto(codigo)
);

CREATE TABLE atividade_membro (
  cod_atividade int,
  cod_membro int,
  PRIMARY KEY (cod_atividade, cod_membro),
  FOREIGN KEY (cod_atividade) references atividade(codigo),
  FOREIGN KEY (cod_membro) references membro(codigo)
);

INSERT INTO departamento(sigla, nome, descricao, gerente)
VALUES ('DHC', 'Departamento de História', 'Departamento de História do CERES', null),
       ('DCT', 'Depepartamento de Computação e Tecnologia', 'Depepartamento de Computação e Tecnologia do CERES', null);

INSERT INTO funcionario(nome, sexo, data_nasc, salario, supervisor, depto)
VALUES ('Ana', 'F', '1988-05-07', 2500.00, null, 1),
       ('Taciano', 'M', '1980-01-25', 2500.00, null, 2);

UPDATE departamento SET gerente = 1 WHERE sigla = 'DHC';
UPDATE departamento SET gerente = 2 WHERE sigla = 'DCT';

INSERT INTO funcionario(nome, sexo, data_nasc, salario, supervisor, depto)
VALUES ('Maria', 'F', '1981-07-01', 2500.00, 1, 1),
       ('Josefa', 'F', '1986-09-17', 2500.00, 1, 1),
       ('Carlos', 'M', '1985-11-21', 2500.00, 1, 1),
       ('Humberto', 'M', '1970-05-07', 1500.00, 2, 2),
       ('José', 'M', '1979-07-12', 3500.00, 2, 2),
       ('Xuxa', 'F', '1970-03-28', 13500.00, null, null),
       ('Sasha', 'F', '1970-03-28', 1500.00, 2, 1),
       ('Victor', 'M', '1970-03-28', 500.00, 4, 1);

INSERT INTO equipe(nome_equipe)
VALUES ('BSI');

INSERT INTO membro(cod_equipe, cod_funcionario)
VALUES (1, 1), (1, 2), (1, 3), (1, 4);

INSERT INTO equipe(nome_equipe)
VALUES ('Amazon');

INSERT INTO membro(cod_equipe, cod_funcionario)
VALUES (2, 7), (2, 8), (2, 9), (2, 10);

INSERT INTO projeto(nome, depto, responsavel, data_inicio, data_fim, situacao, cod_equipe)
VALUES ('APF', 2, 2, '2018-02-26', '2018-06-30', 'Em andamento', 2);

INSERT INTO projeto(nome, depto, responsavel, data_inicio, data_fim, situacao, cod_equipe)
VALUES ('Monitoria', 1, 2, '2018-02-26', '2018-06-30', 'Planejado', 1);

INSERT INTO projeto(nome, depto, responsavel, data_inicio, data_fim, situacao, cod_equipe)
VALUES ('BD', 2, 1, '2018-02-26', '2018-06-30', 'Em andamento', 1);

INSERT INTO projeto(nome, depto, responsavel, data_inicio, data_fim, data_conclusao, situacao, cod_equipe)
VALUES ('ES', 1, 1, '2018-02-26', '2018-06-30', '2018-05-29', 'Concluído', 1);

INSERT INTO atividade(titulo, data_inicio, data_fim, situacao, data_conclusao)
VALUES 
    ('Planejamento de Release', '2018-02-26', '2020-11-01', 'Concluído', '2020-10-01'),
	('Planejamento de Iteração', '2018-02-26', '2020-11-10', 'Concluído', '2020-10-02'),
	('Especificar User Story Base', '2018-02-26', '2020-11-02', 'Planejado', CURRENT_DATE),
	('Especificar User Story Cadastro de Usuários', '2018-02-26', '2020-11-03', 'Em andamento', CURRENT_DATE),
	('Implementar User Story Cadastro de Usuários', '2018-02-26', '2020-11-04', 'Planejado', null),
	('Implementar User Story Base', '2018-02-26', '2020-11-10', 'Em andamento', null),
	('Atualizar Lista de Requisitos Funcionais', '2018-02-26', '2020-11-10', 'Em andamento', null);

INSERT INTO atividade_membro(cod_atividade, cod_membro)
VALUES (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (1, 6), (1, 7), (2, 8);

INSERT INTO atividade_projeto(cod_atividade, cod_projeto)
VALUES (1, 1), (2, 2), (3, 2), (4, 3), (5, 4), (6, 2);
