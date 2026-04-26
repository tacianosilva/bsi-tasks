-- Criação das Tabelas

DROP TABLE IF EXISTS atividade CASCADE;
DROP TABLE IF EXISTS projeto CASCADE;
DROP TABLE IF EXISTS departamento CASCADE;
DROP TABLE IF EXISTS funcionario CASCADE;

CREATE TABLE funcionario (
	codigo SERIAL PRIMARY KEY,
	nome VARCHAR(50),
	sexo CHAR(1),
	dtNasc DATE,
	salario NUMERIC(10,2),
	codSupervisor INT,
	codDepto INT,
	FOREIGN KEY (codSupervisor) REFERENCES funcionario(codigo) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE departamento (
	codigo SERIAL PRIMARY KEY,
	sigla VARCHAR(10) UNIQUE,
	descricao VARCHAR(50),
	codGerente INT,
	FOREIGN KEY (codGerente) REFERENCES funcionario(codigo) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE projeto (
	codigo SERIAL PRIMARY KEY,
	nome VARCHAR(50) UNIQUE,
	descricao VARCHAR(250),
	codResponsavel INT,
	codDepto INT,
	dataInicio DATE,
	dataFim DATE,
	FOREIGN KEY (codResponsavel) REFERENCES funcionario(codigo) ON DELETE SET NULL ON UPDATE CASCADE,
	FOREIGN KEY (codDepto) REFERENCES departamento(codigo) ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE atividade (
	codigo SERIAL PRIMARY KEY,
	descricao VARCHAR(250),
	codProjeto INT,
	dataInicio DATE,
	dataFim DATE,
	FOREIGN KEY (codProjeto) REFERENCES projeto(codigo) ON DELETE SET NULL ON UPDATE CASCADE
);

ALTER TABLE funcionario ADD CONSTRAINT funcDeptoFK FOREIGN KEY (codDepto) REFERENCES departamento(codigo) ON DELETE SET NULL ON UPDATE CASCADE;