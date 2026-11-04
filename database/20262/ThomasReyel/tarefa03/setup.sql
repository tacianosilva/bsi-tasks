E agora?
DROP DATABASE IF EXISTS biblioteca;

CREATE DATABASE biblioteca
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_general_ci;

USE biblioteca;


CREATE TABLE autores (
  id             INT AUTO_INCREMENT PRIMARY KEY,
  nome           VARCHAR(100) NOT NULL,
  pais           VARCHAR(50),
  ano_nascimento INT
);

CREATE TABLE livros (
  id             INT AUTO_INCREMENT PRIMARY KEY,
  titulo         VARCHAR(150) NOT NULL,
  ano_publicacao INT,
  preco          DECIMAL(10,2),
  autor_id       INT,
  FOREIGN KEY (autor_id) REFERENCES autores(id)
);

CREATE TABLE emprestimos (
  id              INT AUTO_INCREMENT PRIMARY KEY,
  livro_id        INT NOT NULL,
  data_emprestimo DATE NOT NULL,
  devolvido       BOOLEAN NOT NULL DEFAULT FALSE,
  FOREIGN KEY (livro_id) REFERENCES livros(id)
);



-- Autores 1 a 4: genericos (os livros 1 a 8 referenciam esses ids)
INSERT INTO autores (nome, pais, ano_nascimento) VALUES
('Autor 1', NULL, NULL),
('Autor 2', NULL, NULL),
('Autor 3', NULL, NULL),
('Autor 4', NULL, NULL);

-- Autores 5 a 14
INSERT INTO autores (nome, pais, ano_nascimento) VALUES
('Machado de Assis',         'Brasil',      1839),
('Clarice Lispector',        'Brasil',      1920),
('Gabriel García Márquez',   'Colômbia',    1927),
('Jane Austen',              'Reino Unido', 1775),
('Fiódor Dostoiévski',       'Rússia',      1821),
('Franz Kafka',              'Áustria',     1883),
('Chimamanda Ngozi Adichie', 'Nigéria',     1977),
('Haruki Murakami',          'Japão',       1949),
('Virginia Woolf',           'Reino Unido', 1882),
('Jorge Amado',              'Brasil',      1912);

INSERT INTO livros (titulo, ano_publicacao, preco, autor_id) VALUES
-- Autores 1 a 4
('Obra Completa do Autor 1',          1998, 59.90, 1),
('Ensaio do Autor 1',                 2005, 45.00, 1),
('Romance do Autor 2',                2010, 39.90, 2),
('Contos do Autor 2',                 2015, 34.50, 2),
('Poesias do Autor 3',                2001, 29.90, 3),
('Crônicas do Autor 3',               2018, 42.00, 3),
('Estudo do Autor 4',                 1995, 55.00, 4),
('Novela do Autor 4',                 2020, 48.75, 4),
-- Machado de Assis (5)
('Dom Casmurro',                      1899, 34.90, 5),
('Memórias Póstumas de Brás Cubas',   1881, 39.90, 5),
('Quincas Borba',                     1891, 32.50, 5),
-- Clarice Lispector (6)
('A Hora da Estrela',                 1977, 36.90, 6),
('Perto do Coração Selvagem',         1943, 44.00, 6),
-- Gabriel García Márquez (7)
('Cem Anos de Solidão',               1967, 54.90, 7),
('O Amor nos Tempos do Cólera',       1985, 49.90, 7),
-- Jane Austen (8)
('Orgulho e Preconceito',             1813, 29.90, 8),
('Emma',                              1815, 31.50, 8),
-- Fiódor Dostoiévski (9)
('Crime e Castigo',                   1866, 47.90, 9),
('Os Irmãos Karamazov',               1880, 58.00, 9),
-- Franz Kafka (10)
('A Metamorfose',                     1915, 27.90, 10),
('O Processo',                        1925, 41.90, 10),
-- Chimamanda Ngozi Adichie (11)
('Americanah',                        2013, 52.90, 11),
('Meio Sol Amarelo',                  2006, 46.50, 11),
-- Haruki Murakami (12)
('Kafka à Beira-Mar',                 2002, 56.90, 12),
('Norwegian Wood',                    1987, 43.90, 12),
-- Virginia Woolf (13)
('Mrs. Dalloway',                     1925, 38.90, 13),
('Ao Farol',                          1927, 40.00, 13),
-- Jorge Amado (14)
('Gabriela, Cravo e Canela',          1958, 37.90, 14),
('Capitães da Areia',                 1937, 35.50, 14),
('Dona Flor e Seus Dois Maridos',     1966, 45.90, 14);

INSERT INTO emprestimos (livro_id, data_emprestimo, devolvido) VALUES
(1, '2026-01-11', TRUE),
(1, '2026-03-11', FALSE),
(4, '2026-02-11', FALSE);

-- ---------------------------------------------------------------------

DROP USER IF EXISTS 'app_biblioteca'@'%';
DROP USER IF EXISTS 'consulta'@'%';
DROP USER IF EXISTS 'relatorios'@'%';


CREATE USER 'app_biblioteca'@'%' IDENTIFIED BY 'AppBib2026!';
GRANT SELECT, INSERT, UPDATE, DELETE ON biblioteca.* TO 'app_biblioteca'@'%';


CREATE USER 'consulta'@'%' IDENTIFIED BY 'Consulta2026!';
GRANT SELECT ON biblioteca.* TO 'consulta'@'%';


CREATE USER 'relatorios'@'%' IDENTIFIED BY 'Relatorios2026!';
GRANT SELECT ON biblioteca.livros TO 'relatorios'@'%';

FLUSH PRIVILEGES;