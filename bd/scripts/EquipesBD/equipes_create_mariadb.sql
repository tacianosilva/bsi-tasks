SET FOREIGN_KEY_CHECKS=0; -- to disable them

drop table if exists atividade_membro cascade;
drop table if exists atividade_projeto cascade;
drop table if exists atividade cascade;
drop table if exists membro cascade;
drop table if exists projeto cascade;
drop table if exists equipe cascade;
drop table if exists departamento cascade;
drop table if exists funcionario cascade;

SET FOREIGN_KEY_CHECKS=1; -- to re-enable them


CREATE TABLE funcionario (
  codigo int(11) NOT NULL AUTO_INCREMENT,
  nome varchar(15) NOT NULL,
  sexo char(1) DEFAULT NULL,
  dataNasc date DEFAULT NULL,
  salario decimal(10,2) DEFAULT NULL,
  supervisor int(11) DEFAULT NULL,
  depto int(11) DEFAULT NULL,
  PRIMARY KEY (codigo),
  CONSTRAINT funcSuperFK FOREIGN KEY (supervisor) REFERENCES funcionario(codigo) on delete set null on update cascade
);

CREATE TABLE departamento (
  codigo int(11) NOT NULL AUTO_INCREMENT,
  sigla varchar(15) NOT NULL,
  descricao varchar(25) NOT NULL,
  gerente int(11) DEFAULT NULL,
  PRIMARY KEY (codigo),
  UNIQUE KEY sigla (sigla),
  CONSTRAINT depGerenteFK FOREIGN KEY (gerente) REFERENCES funcionario(codigo) on delete set null on update cascade
);

alter table funcionario ADD CONSTRAINT funcDeptoFK FOREIGN KEY (depto) REFERENCES departamento (codigo) on delete set null on update cascade;

CREATE TABLE equipe (
  codigo int(11) NOT NULL AUTO_INCREMENT,
  nomeEquipe varchar(45) DEFAULT NULL,
  PRIMARY KEY (codigo)
);

CREATE TABLE membro (
  codigo int(11) NOT NULL AUTO_INCREMENT,
  codEquipe int(11) DEFAULT NULL,
  codFuncionario int(11) DEFAULT NULL,
  PRIMARY KEY (codigo),
  foreign key (codEquipe) references equipe(codigo) on delete set null,
  foreign key (codFuncionario) references funcionario(codigo) on delete set null
);


CREATE TABLE projeto (
  codigo int(11) NOT NULL AUTO_INCREMENT,
  descricao varchar(45) DEFAULT NULL,
  depto int(11) DEFAULT NULL,
  responsavel int(11) DEFAULT NULL,
  dataInicio date DEFAULT NULL,
  dataFim date DEFAULT NULL,
  situacao varchar(45) DEFAULT NULL,
  dataConclusao date DEFAULT NULL,
  equipe int(11) DEFAULT NULL,
  PRIMARY KEY (codigo),
  foreign key (depto) references departamento(codigo) on delete set null,
  foreign key (responsavel) references funcionario(codigo) on delete set null,
  foreign key (equipe) references equipe(codigo) on delete set null
);

CREATE TABLE atividade (
  codigo int(11) NOT NULL AUTO_INCREMENT,
  descricao varchar(45) DEFAULT NULL,
  dataInicio date DEFAULT NULL,
  dataFim date DEFAULT NULL,
  situacao varchar(45) DEFAULT NULL,
  dataConclusao date DEFAULT NULL,
  PRIMARY KEY (codigo)
);

CREATE TABLE atividade_projeto (
  codAtividade int(11) NOT NULL,
  codProjeto int(11) NOT NULL,
  PRIMARY KEY (codProjeto, codAtividade),
  foreign key (codAtividade) references atividade(codigo),
  foreign key (codProjeto) references projeto(codigo)
);

CREATE TABLE atividade_membro (
  codAtividade int(11) NOT NULL,
  codMembro int(11) NOT NULL,
  PRIMARY KEY (codAtividade, codMembro),
  foreign key (codAtividade) references atividade(codigo),
  foreign key (codMembro) references membro(codigo)
);

insert into departamento
(sigla, descricao, gerente)
values ('DHC', 'Dep História', null);

insert into departamento
(sigla, descricao, gerente)
values ('DCT', 'Dep Computação', null);

insert into funcionario
(nome, sexo, dataNasc, salario, supervisor, depto)
values ('Ana', 'F', '1988-05-07', 2500.00, null, 1);

insert into funcionario
(nome, sexo, dataNasc, salario, supervisor, depto)
values ('Taciano', 'M', '1980-01-25', 2500.00, null, 2);

update departamento set gerente = 1 where sigla = 'DHC';
update departamento set gerente = 2 where sigla = 'DCT';

insert into funcionario
(nome, sexo, dataNasc, salario, supervisor, depto)
values ('Maria', 'F', '1981-07-01', 2500.00, 1, 1);

insert into funcionario
(nome, sexo, dataNasc, salario, supervisor, depto)
values ('Josefa', 'F', '1986-09-17', 2500.00, 1, 1);

insert into funcionario
(nome, sexo, dataNasc, salario, supervisor, depto)
values ('Carlos', 'M', '1985-11-21', 2500.00, 1, 1);

insert into funcionario
(nome, sexo, dataNasc, salario, supervisor, depto)
values ('Humberto', 'M', '1970-05-07', 1500.00, 2, 2);

insert into funcionario
(nome, sexo, dataNasc, salario, supervisor, depto)
values ('José', 'M', '1979-07-12', 3500.00, 2, 2);

insert into funcionario
(nome, sexo, dataNasc, salario, supervisor, depto)
values ('Xuxa', 'F', '1970-03-28', 13500.00, null, null);

insert into funcionario
(nome, sexo, dataNasc, salario, supervisor, depto)
values ('Sasha', 'F', '1970-03-28', 1500.00, 2, 1);

insert into funcionario
(nome, sexo, dataNasc, salario, supervisor, depto)
values ('Victor', 'M', '1970-03-28', 500.00, 4, 1);

insert into equipe
(nomeEquipe)
values ('BSI');

insert into membro
(codEquipe, codFuncionario)
values (1, 1);

insert into membro
(codEquipe, codFuncionario)
values (1, 2);

insert into membro
(codEquipe, codFuncionario)
values (1, 3);

insert into membro
(codEquipe, codFuncionario)
values (1, 4);

insert into equipe
(nomeEquipe)
values ('Amazon');

insert into membro
(codEquipe, codFuncionario)
values (1, 7);

insert into membro
(codEquipe, codFuncionario)
values (1, 8);

insert into membro
(codEquipe, codFuncionario)
values (1, 9);

insert into membro
(codEquipe, codFuncionario)
values (1, 10);

insert into projeto(descricao, depto, responsavel, DataInicio, DataFim, situacao, equipe)
values ('APF', 2, 2, '2018-02-26', '2018-06-30', 'Em andamento', 2);

insert into projeto(descricao, depto, responsavel, DataInicio, DataFim, situacao, equipe)
values ('Monitoria', 1, 2, '2018-02-26', '2018-06-30', 'Planejado', 1);

insert into projeto(descricao, depto, responsavel, DataInicio, DataFim, situacao, equipe)
values ('BD', 2, 1, '2018-02-26', '2018-06-30', 'Em andamento', 1);

insert into projeto(descricao, depto, responsavel, DataInicio, DataFim, dataConclusao, situacao, equipe)
values ('ES', 1, 1, '2018-02-26', '2018-06-30', '2018-05-29', 'Concluído', 1);


INSERT INTO atividade(descricao, dataInicio, dataFim, situacao, dataConclusao)
	VALUES ('Preparar calendário', '2018-02-26', '2020-11-01', 'Concluído', '2020-10-01');
INSERT INTO atividade(descricao, dataInicio, dataFim, situacao, dataConclusao)
	VALUES ('Preparar calendário', '2018-02-26', '2020-11-10', 'Concluído', '2020-10-02');
INSERT INTO atividade(descricao, dataInicio, dataFim, situacao, dataConclusao)
	VALUES ('Consultar direção', '2018-02-26', '2020-11-02', 'Planejado', CURDATE());
INSERT INTO atividade(descricao, dataInicio, dataFim, situacao, dataConclusao)
	VALUES ('Consultar direção', '2018-02-26', '2020-11-03', 'Em andamento', CURDATE());
INSERT INTO atividade(descricao, dataInicio, dataFim, situacao, dataConclusao)
	VALUES ('Consultar direção', '2018-02-26', '2020-11-04', 'Planejado', CURDATE());
INSERT INTO atividade(descricao, dataInicio, dataFim, situacao, dataConclusao)
	VALUES ('Emitir prestação de contas', '2018-02-26', '2020-11-10', 'Em andamento', CURDATE());

INSERT INTO atividade_membro(codAtividade, codMembro)
	VALUES (1, 1);
INSERT INTO atividade_membro(codAtividade, codMembro)
	VALUES (2, 2);
INSERT INTO atividade_membro(codAtividade, codMembro)
	VALUES (3, 3);
INSERT INTO atividade_membro(codAtividade, codMembro)
	VALUES (4, 4);
INSERT INTO atividade_membro(codAtividade, codMembro)
	VALUES (5, 5);
INSERT INTO atividade_membro(codAtividade, codMembro)
	VALUES (1, 6);
INSERT INTO atividade_membro(codAtividade, codMembro)
	VALUES (1, 7);
INSERT INTO atividade_membro(codAtividade, codMembro)
	VALUES (2, 8);

INSERT INTO atividade_projeto(codAtividade, codProjeto)
	VALUES (1, 1);
INSERT INTO atividade_projeto(codAtividade, codProjeto)
	VALUES (2, 2);
INSERT INTO atividade_projeto(codAtividade, codProjeto)
	VALUES (3, 2);
INSERT INTO atividade_projeto(codAtividade, codProjeto)
	VALUES (4, 3);
INSERT INTO atividade_projeto(codAtividade, codProjeto)
	VALUES (5, 4);
INSERT INTO atividade_projeto(codAtividade, codProjeto)
	VALUES (6, 2);
