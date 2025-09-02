DROP TABLE IF EXISTS dependente CASCADE;
DROP TABLE IF EXISTS alocacao CASCADE;
DROP TABLE IF EXISTS projeto CASCADE;
ALTER TABLE IF EXISTS departamento DROP CONSTRAINT IF EXISTS dep_gerente_fk;
DROP TABLE IF EXISTS empregado CASCADE;
DROP TABLE IF EXISTS departamento CASCADE;

CREATE TABLE empregado (
  matricula INT(11) NOT NULL,  
  nome VARCHAR(150) NOT NULL,
  data_nasc DATE DEFAULT NULL,
  endereco VARCHAR(250) DEFAULT NULL,
  sexo CHAR(1) DEFAULT NULL,
  salario DECIMAL(10,2) DEFAULT NULL,
  supervisor INT(11) DEFAULT NULL,
  depto INT(11) DEFAULT NULL,
  PRIMARY KEY (matricula),
  CONSTRAINT emp_super_fk FOREIGN KEY (supervisor) REFERENCES empregado(matricula) ON DELETE SET NULL
);

CREATE TABLE departamento (
  cod_dep INT(11) NOT NULL AUTO_INCREMENT,
  nome_dep VARCHAR(100) NOT NULL,
  gerente INT(11) NOT NULL,
  dt_inicio_gerencia DATE DEFAULT NULL,
  PRIMARY KEY (cod_dep),
  UNIQUE KEY nome_dep_uk (nome_dep)
);

ALTER TABLE empregado ADD CONSTRAINT emp_dep_fk
  FOREIGN KEY (depto) REFERENCES departamento(cod_dep) ON DELETE SET NULL;

ALTER TABLE departamento ADD CONSTRAINT dep_gerente_fk 
  FOREIGN KEY (gerente) REFERENCES empregado(matricula);

CREATE TABLE projeto (
  cod_proj INT(11) NOT NULL AUTO_INCREMENT,
  nome VARCHAR(250) DEFAULT NULL,
  localizacao VARCHAR(150) DEFAULT NULL,
  depart INT(11) DEFAULT NULL,
  lider INT(11) DEFAULT NULL,
  PRIMARY KEY (cod_proj),
  FOREIGN KEY (depart) REFERENCES departamento(cod_dep) ON DELETE SET NULL,
  FOREIGN KEY (lider) REFERENCES empregado(matricula) ON DELETE SET NULL
);

CREATE TABLE alocacao (
  cod_aloc INT(11) NOT NULL AUTO_INCREMENT,
  matric INT(11) NOT NULL,
  cod_proj INT(11) NOT NULL,
  horas DECIMAL(4,2) DEFAULT NULL,
  PRIMARY KEY (cod_aloc)
);

CREATE TABLE dependente (
  cod_depend INT(11) NOT NULL AUTO_INCREMENT,
  matricula INT(11) NOT NULL,
  nome VARCHAR(150) DEFAULT NULL,
  sexo CHAR(1) DEFAULT NULL,
  PRIMARY KEY (cod_depend)
);

ALTER TABLE alocacao ADD FOREIGN KEY (matric) REFERENCES empregado(matricula) ON DELETE RESTRICT;
ALTER TABLE alocacao ADD FOREIGN KEY (cod_proj) REFERENCES projeto(cod_proj) ON DELETE RESTRICT;

ALTER TABLE dependente ADD FOREIGN KEY (matricula) REFERENCES empregado(matricula) ON DELETE RESTRICT;

# Carga inicial

-- Inserindo empregados com dados completos
INSERT INTO empregado (matricula, nome, data_nasc, endereco, sexo, salario)
VALUES
(9491, 'Ana', '1980-05-10', 'Rua A, 123', 'F', 5000.00),
(9492, 'Taciano', '1975-12-20', 'Rua B, 456', 'M', 6000.00);

-- Inserindo departamentos, agora com dt_inicio_gerencia
INSERT INTO departamento (nome_dep, gerente, dt_inicio_gerencia)
VALUES
('Vendas', 9491, '2020-01-15'),
('Compras', 9492, '2021-03-10');

-- Atualizando o departamento dos empregados CORRETAMENTE
UPDATE empregado SET depto = 1 WHERE matricula = 9491; -- Ana para Vendas (cod_dep = 1)
UPDATE empregado SET depto = 2 WHERE matricula = 9492; -- Taciano para Compras (cod_dep = 2)


-- Exemplo de inserção com supervisor
INSERT INTO empregado (matricula, nome, data_nasc, endereco, sexo, salario, supervisor, depto)
VALUES (9493, 'João', '1990-03-15', 'Rua C, 789', 'M', 3000.00, 9491, 1); -- João supervisionado por Ana (9491) e no departamento de Vendas (1)

-- Exemplo de inserção sem supervisor
INSERT INTO empregado (matricula, nome, data_nasc, endereco, sexo, salario, depto)
VALUES (9494, 'Maria', '1985-07-22', 'Rua D, 012', 'F', 3500.00, 2); -- Maria sem supervisor e no departamento de Compras (2)
