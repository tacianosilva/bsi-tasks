CREATE TABLE empregado (
  matricula INTEGER NOT NULL,
  nome varchar(15) NOT NULL,
  dataNasc date DEFAULT NULL,
  endereco varchar(30) DEFAULT NULL,
  sexo char(1) DEFAULT NULL,
  salario decimal(10,2) DEFAULT NULL,
  supervisor INTEGER DEFAULT NULL,
  depto INTEGER DEFAULT NULL,
  PRIMARY KEY (matricula),
  CONSTRAINT empSuperFK FOREIGN KEY (supervisor) REFERENCES empregado (matricula) on delete set null
);

CREATE TABLE departamento (
  codDep SERIAL NOT NULL,
  nomeDep varchar(15) NOT NULL,
  gerente INTEGER NOT NULL,
  dataInicioGerencia date DEFAULT NULL,
  PRIMARY KEY (codDep),
  UNIQUE (nomeDep)
);

CREATE TABLE projeto (
  codproj SERIAL NOT NULL,
  nome varchar(45) DEFAULT NULL,
  localizacao varchar(45) DEFAULT NULL,
  depart INTEGER DEFAULT NULL,
  lider INTEGER DEFAULT NULL,
  PRIMARY KEY (codproj),
  foreign key (depart) references departamento(codDep) on delete set null,
  foreign key (lider) references empregado(matricula) on delete set null
);

CREATE TABLE alocacao (
  codAloc SERIAL NOT NULL,
  matric INTEGER NOT NULL,
  codProj INTEGER NOT NULL,
  horas decimal(4,2) DEFAULT NULL,
  PRIMARY KEY (codAloc)
);

CREATE TABLE dependente (
  codDepend SERIAL NOT NULL,
  matricula INTEGER NOT NULL,
  nome varchar(45) DEFAULT NULL,
  sexo varchar(1) DEFAULT NULL,
  PRIMARY KEY (codDepend)
);

alter table alocacao add foreign key (matric) references empregado(matricula) on delete restrict;
alter table alocacao add foreign key (codProj) references projeto(codproj) on delete restrict;

alter table dependente add foreign key (matricula) references empregado(matricula) on delete restrict;

-- Carga inicial

insert into empregado (matricula, nome, sexo, salario)
values
(9491, 'Ana', 'F', 2500),
(9492, 'Taciano', 'M', 2250);

insert into departamento (nomeDep, gerente)
values
('Vendas', 9491),
('Compras', 9492);

update empregado set depto = 1 where matricula = '9491';
update empregado set depto = 1 where matricula = '9492';

alter table empregado add constraint empDepFK
foreign key (depto) references departamento(codDep) on delete set null;
