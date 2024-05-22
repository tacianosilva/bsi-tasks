drop table if exists dependente cascade;
drop table if exists alocacao cascade;
drop table if exists projeto cascade;
drop table if exists empregado cascade;
drop table if exists departamento cascade;

CREATE TABLE `empregado` (
  `matricula` int(11) NOT NULL,  
  `nome` varchar(15) NOT NULL,
  `dataNasc` date DEFAULT NULL,
  `endereco` varchar(30) DEFAULT NULL,
  `sexo` char(1) DEFAULT NULL,
  `salario` decimal(10,2) DEFAULT NULL,
  `supervisor` int(11) DEFAULT NULL,
  `depto` int(11) DEFAULT NULL,
  PRIMARY KEY (`matricula`),
  CONSTRAINT `empSuperFK` FOREIGN KEY (`supervisor`) REFERENCES `empregado` (`matricula`) on delete set null
);

CREATE TABLE `departamento` (
  `codDep` int(11) NOT NULL AUTO_INCREMENT,
  `nomeDep` varchar(15) NOT NULL,
  `gerente` int(11) NOT NULL,
  `dataInicioGerencia` date DEFAULT NULL,
  PRIMARY KEY (`codDep`),
  UNIQUE KEY `nomeDep` (`nomeDep`)
);

CREATE TABLE `projeto` (
  `codproj` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) DEFAULT NULL,
  `localizacao` varchar(45) DEFAULT NULL,
  `depart` int(11) DEFAULT NULL,
  `lider` int(11) DEFAULT NULL,
  PRIMARY KEY (`codproj`),
  foreign key (depart) references departamento(codDep) on delete set null,
  foreign key (lider) references empregado(matricula) on delete set null
);

CREATE TABLE `alocacao` (
  `codAloc` int(11) NOT NULL AUTO_INCREMENT,
  `matric` int(11) NOT NULL,
  `codProj` int(11) NOT NULL,
  `horas` decimal(4,2) DEFAULT NULL,
  PRIMARY KEY (`codAloc`)
);

CREATE TABLE `dependente` (
  `codDepend` int(11) NOT NULL AUTO_INCREMENT,
  `matricula` int(11) NOT NULL,
  `nome` varchar(45) DEFAULT NULL,
  `sexo` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`codDepend`)
);

alter table alocacao add foreign key (`matric`) references empregado(matricula) on delete restrict;
alter table alocacao add foreign key (`codProj`) references projeto(codproj) on delete restrict;

alter table dependente add foreign key (matricula) references empregado(matricula) on delete restrict;

# Carga inicial

insert into empregado
(matricula, nome)
values (9491, 'Ana');

insert into empregado
(matricula, nome)
values (9492, 'Taciano');

insert into departamento 
(nomeDep, gerente)
values ('Vendas', 9491);

insert into departamento 
(nomeDep, gerente)
values ('Compras', 9492);

update empregado set depto = 1 where matricula = '9491';
update empregado set depto = 1 where matricula = '9492';

alter table empregado add constraint empDepFK
foreign key (depto) references departamento(codDep) on delete set null;