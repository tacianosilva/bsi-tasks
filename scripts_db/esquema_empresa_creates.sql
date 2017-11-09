drop table if exists empregado cascade;
drop table if exists departamento cascade;
drop table if exists projeto cascade;
drop table if exists alocacao cascade;
drop table if exists dependente cascade;

CREATE TABLE `empregado` (
  `nome` varchar(15) NOT NULL,
  `matricula` char(9) NOT NULL,
  `dataNasc` date DEFAULT NULL,
  `endereco` varchar(30) DEFAULT NULL,
  `sexo` char(1) DEFAULT NULL,
  `salario` decimal(10,2) DEFAULT NULL,
  `supervisor` char(9) DEFAULT NULL,
  `depto` int(11) DEFAULT NULL,
  PRIMARY KEY (`matricula`),
  CONSTRAINT `empSuperFK` FOREIGN KEY (`supervisor`) REFERENCES `empregado` (`matricula`)
);

CREATE TABLE `departamento` (
  `nomeDep` varchar(15) NOT NULL,
  `codDep` int(11) NOT NULL,
  `gerente` char(9) NOT NULL,
  `dataInicioGer` date DEFAULT NULL,
  PRIMARY KEY (`codDep`),
  UNIQUE KEY `nomeDep` (`nomeDep`)
);

CREATE TABLE `projeto` (
  `codproj` int(11) NOT NULL,
  `nome` varchar(45) DEFAULT NULL,
  `local` varchar(45) DEFAULT NULL,
  `depart` varchar(45) DEFAULT NULL,
  `projetocol` int(11) DEFAULT NULL,
  PRIMARY KEY (`codproj`)
);

CREATE TABLE `alocacao` (
  `matric` int(11) NOT NULL,
  `codigop` int(11) NOT NULL,
  `horas` decimal(4,2) DEFAULT NULL,
  PRIMARY KEY (`matric`,`codigop`)
);

CREATE TABLE `dependente` (
  `coddepend` int(11) NOT NULL,
  `matricula` int(11) NOT NULL,
  `nome` varchar(45) DEFAULT NULL,
  `sexo` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`coddepend`,`matricula`)
);

alter table empregado add constraint empDepFK
foreign key (depto) references departamento(codDep);