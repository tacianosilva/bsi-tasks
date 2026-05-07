drop table if exists atividade cascade;
drop table if exists projeto cascade;
drop table if exists departamento cascade;
drop table if exists funcionario cascade;

-- Criação das Tabelas

CREATE TABLE funcionario (
    codigo serial,
    nome varchar(150),
    sexo char(1),
    dt_nasc date,
    salario numeric(12,2),
    supervisor int,
    depto int,
    PRIMARY KEY (codigo),
    FOREIGN KEY (supervisor) REFERENCES funcionario(codigo) on delete set null on update cascade
);

CREATE TABLE departamento (
    codigo serial,
    nome varchar(100),
    sigla varchar(10) unique,
    descricao varchar(250),
    gerente int,
    PRIMARY KEY (codigo),
    FOREIGN KEY (gerente) REFERENCES funcionario(codigo) on delete set null on update cascade
);

-- add foreign key de funcionario
alter table funcionario ADD CONSTRAINT funcDeptoFK FOREIGN KEY (depto) REFERENCES departamento(codigo) on delete set null on update cascade;

CREATE TABLE projeto (
    codigo serial,
    nome varchar(50) unique,
    descricao varchar(250),
    responsavel int,
    depto int,
    data_inicio date,
    data_fim date,
    PRIMARY KEY (codigo),
    FOREIGN KEY (responsavel) REFERENCES funcionario(codigo) on delete set null on update cascade,
    FOREIGN KEY (depto) REFERENCES departamento(codigo) on delete set null on update cascade
);

CREATE TABLE atividade (
    codigo serial,
    descricao varchar(250),
    projeto int,
    data_inicio date,
    data_fim date,
    PRIMARY KEY (codigo),
    FOREIGN KEY (projeto) REFERENCES projeto(codigo) on delete set null on update cascade
);


-- Povoamento Inicial
-- Adicionando Departamentos
insert into departamento
(sigla, descricao, gerente) values
    ('DHC', 'Dep. História', null),
    ('DCT', 'Dep. Computação', null),
    ('DGC', 'Dep. Geografia', null),
    ('DIR', 'Dep. Direito', null);

-- Adicionando Funcionários Gerentes
insert into funcionario
(nome, sexo, dt_nasc, salario, supervisor, depto)
values ('Ana', 'F', '1988-05-07', 2500.00, null, 1);

insert into funcionario
(nome, sexo, dt_nasc, salario, supervisor, depto)
values ('Taciano', 'M', '1980-01-25', 2500.00, null, 2);

-- Adicionando Gerentes
update departamento set gerente = 1 where sigla = 'DHC';
update departamento set gerente = 2 where sigla = 'DCT';

-- Adicionando Funcionários

insert into funcionario
(nome, sexo, dt_nasc, salario, supervisor, depto)
values
    ('Maria', 'F', '1981-07-01', 2500.00, 1, 1),
    ('Josefa', 'F', '1986-09-17', 2500.00, 1, 1),
    ('Carlos', 'M', '1985-11-21', 2500.00, 1, 1),
    ('José', 'M', '1979-07-12', 3500.00, 2, 2),
    ('Gabriel', 'M', '1981-08-11', 1850.00, null, 3),
    ('Margarete', 'F', '1992-03-22', 4500.00, null, 3),
    ('José', 'M', '1979-07-12', 3500.00, 3, null),
    ('Xuxa', 'F', '1970-03-28', 13500.00, null, null),
    ('Sasha', 'F', '1970-03-28', 1500.00, 11, 3),
    ('Victor', 'M', '1970-03-28', 500.00, 2, 1),
    ('Humberto', 'M', '1970-05-07', 1500.00, 2, 2),
    ('Doisberto', 'M', '1980-07-14', 2500.00, 3, 3),
    ('Tresberta', 'F', '1992-09-01', 3000.00, 4, 3);

-- Adicionando Projetos

insert into projeto
(nome, descricao, depto, responsavel, data_inicio, data_fim)
values
    ('APF', 'Analisador de Ponto de Função', 2, 2, '2018-02-26', '2019-06-30'),
    ('Monitoria', 'Projeto de Monitoria 2019.1', 1, 6, '2019-02-26', '2019-12-30'),
    ('BD', 'Projeto de Banco de Dados', 3, 5, '2018-02-26', '2018-06-30'),
    ('ES', 'Projeto de Engenharia de Software', 1, 1, '2018-02-26', '2018-06-30');

-- Adicionando Atividades

insert into atividade
(descricao, projeto, data_inicio, data_fim)
values
    ('APF - Atividade 1', 1, '2018-02-26', '2018-06-30'),
    ('APF - Atividade 2', 1, '2018-06-26', '2018-07-30'),
    ('APF - Atividade 3', 1, '2018-08-26', '2018-09-30'),
    ('APF - Atividade 4', 1, '2018-08-26', '2018-09-30'),
    ('APF - Atividade 5', 1, '2018-09-30', '2018-10-30'),
    ('Monitoria - Atividade 1', 2, '2018-06-26', '2018-07-30'),
    ('BD - Atividade 1', 3, '2018-06-26', '2018-07-30'),
    ('BD - Atividade 2', 3, '2018-08-26', '2018-09-30'),
    ('BD - Atividade 3', 3, '2018-08-26', '2018-09-30'),
    ('ES - Atividade 1', 4, '2018-09-30', '2018-10-30'),
    ('ES - Atividade 2', 4, '2018-06-26', '2018-07-30');
