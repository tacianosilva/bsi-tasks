SET FOREIGN_KEY_CHECKS=0; -- Desabilitar Foreign Keys

drop table if exists atividade cascade;
drop table if exists projeto cascade;
drop table if exists departamento cascade;
drop table if exists funcionario cascade;

SET FOREIGN_KEY_CHECKS=1; -- Habilitando Foreign Keys

# Criação das Tabelas

CREATE TABLE funcionario (
	codigo int AUTO_INCREMENT,
	nome varchar(50),
	sexo char(1),
	dtNasc date,
	salario decimal(10,2),
	codSupervisor int,
	codDepto int,
	PRIMARY KEY (codigo),
	FOREIGN KEY (codSupervisor) REFERENCES funcionario(codigo) on delete set null on update cascade
);

CREATE TABLE departamento (
	codigo int AUTO_INCREMENT,
	sigla varchar(10),
	descricao varchar(50),
	codGerente int,
	PRIMARY KEY (codigo),
	UNIQUE KEY depSigla (sigla),
	FOREIGN KEY (codGerente) REFERENCES funcionario(codigo) on delete set null on update cascade
);

CREATE TABLE projeto (
	codigo int AUTO_INCREMENT,
	nome varchar(50),
	descricao varchar(250),
	codResponsavel int,
	codDepto int,
	dataInicio date, 
	dataFim date,
	PRIMARY KEY (codigo),
	UNIQUE KEY projNome (nome),
	FOREIGN KEY (codResponsavel) REFERENCES funcionario(codigo) on delete set null on update cascade,
	FOREIGN KEY (codDepto) REFERENCES departamento(codigo) on delete set null on update cascade
);
 
CREATE TABLE atividade (
	codigo int AUTO_INCREMENT,
	descricao varchar(250),
	codProjeto int,
	dataInicio date, 
	dataFim date,
	PRIMARY KEY (codigo),
	FOREIGN KEY (codProjeto) REFERENCES projeto(codigo) on delete set null on update cascade

);

alter table funcionario ADD CONSTRAINT funcDeptoFK FOREIGN KEY (codDepto) REFERENCES departamento(codigo) on delete set null on update cascade;

# Povoamento Inicial

insert into departamento
(sigla, descricao, codGerente)
values ('DHC', 'Dep História', null);

insert into departamento
(sigla, descricao, codGerente)
values ('DCT', 'Dep Computação', null);

insert into departamento
(sigla, descricao, codGerente)
values ('DGC', 'Dep Geografia', null);

insert into departamento
(sigla, descricao, codGerente)
values ('DXT', null, null);

# Adicionando Gerentes

insert into funcionario
(nome, sexo, dtNasc, salario, codSupervisor, codDepto)
values ('Ana', 'F', '1988-05-07', 2500.00, null, 1);

insert into funcionario
(nome, sexo, dtNasc, salario, codSupervisor, codDepto)
values ('Taciano', 'M', '1980-01-25', 2500.00, null, 2);

update departamento set codGerente = 1 where sigla = 'DHC';
update departamento set codGerente = 2 where sigla = 'DCT';

# Adicionando Funcionários

insert into funcionario
(nome, sexo, dtNasc, salario, codSupervisor, codDepto)
values ('Maria', 'F', '1981-07-01', 2500.00, 1, 1);

insert into funcionario
(nome, sexo, dtNasc, salario, codSupervisor, codDepto)
values ('Josefa', 'F', '1986-09-17', 2500.00, 1, 1);

insert into funcionario
(nome, sexo, dtNasc, salario, codSupervisor, codDepto)
values ('Carlos', 'M', '1985-11-21', 2500.00, 1, 1);

insert into funcionario
(nome, sexo, dtNasc, salario, codSupervisor, codDepto)
values ('Humberto', 'M', '1970-05-07', 1500.00, 2, 2);

insert into funcionario
(nome, sexo, dtNasc, salario, codSupervisor, codDepto)
values ('José', 'M', '1979-07-12', 3500.00, 2, 2);

insert into funcionario
(nome, sexo, dtNasc, salario, codSupervisor, codDepto)
values ('Xuxa', 'F', '1970-03-28', 13500.00, null, null);

insert into funcionario
(nome, sexo, dtNasc, salario, codSupervisor, codDepto)
values ('Sasha', 'F', '1970-03-28', 1500.00, 3, 1);

insert into funcionario
(nome, sexo, dtNasc, salario, codSupervisor, codDepto)
values ('Victor', 'M', '1970-03-28', 500.00, 4, 1);

insert into funcionario
(nome, sexo, dtNasc, salario, codSupervisor, codDepto)
values ('Doisberto', 'M', '1980-07-14', 2500.00, 3, 3);

insert into funcionario
(nome, sexo, dtNasc, salario, codSupervisor, codDepto)
values ('Tresberta', 'F', '1992-09-01', 3000.00, 4, 3);

# Adicionando Projetos

insert into projeto(nome, descricao, codDepto, codResponsavel, dataInicio, dataFim)
values ('APF', 'Analisador de Ponto de Função', 2, 2, '2018-02-26', '2019-06-30');

insert into projeto(nome, descricao, codDepto, codResponsavel, dataInicio, dataFim)
values ('Monitoria', 'Projeto de Monitoria 2019.1', 1, 6, '2019-02-26', '2019-12-30');

insert into projeto(nome, descricao, codDepto, codResponsavel, dataInicio, dataFim)
values ('BD', 'Projeto de Banco de Dados', 3, 5, '2018-02-26', '2018-06-30');

insert into projeto(nome, descricao, codDepto, codResponsavel, dataInicio, dataFim)
values ('ES', 'Projeto de Engenharia de Software', 1, 1, '2018-02-26', '2018-06-30');

# Adicionando Atividades

insert into atividade(descricao, codProjeto, dataInicio, dataFim)
values ('APF - Atividade 1', 1, '2018-02-26', '2018-06-30');
insert into atividade(descricao, codProjeto, dataInicio, dataFim)
values ('APF - Atividade 2', 1, '2018-06-26', '2018-07-30');
insert into atividade(descricao, codProjeto, dataInicio, dataFim)
values ('APF - Atividade 3', 1, '2018-08-26', '2018-09-30');
insert into atividade(descricao, codProjeto, dataInicio, dataFim)
values ('APF - Atividade 4', 1, '2018-08-26', '2018-09-30');
insert into atividade(descricao, codProjeto, dataInicio, dataFim)
values ('APF - Atividade 5', 1, '2018-09-30', '2018-10-30');

insert into atividade(descricao, codProjeto, dataInicio, dataFim)
values ('Monitoria - Atividade 1', 2, '2018-06-26', '2018-07-30');

insert into atividade(descricao, codProjeto, dataInicio, dataFim)
values ('BD - Atividade 1', 3, '2018-06-26', '2018-07-30');
insert into atividade(descricao, codProjeto, dataInicio, dataFim)
values ('BD - Atividade 2', 3, '2018-08-26', '2018-09-30');
insert into atividade(descricao, codProjeto, dataInicio, dataFim)
values ('BD - Atividade 3', 3, '2018-08-26', '2018-09-30');

insert into atividade(descricao, codProjeto, dataInicio, dataFim)
values ('ES - Atividade 1', 4, '2018-09-30', '2018-10-30');
insert into atividade(descricao, codProjeto, dataInicio, dataFim)
values ('ES - Atividade 2', 4, '2018-06-26', '2018-07-30');
