-- Script idempotente de provisionamento do banco biblioteca
DROP DATABASE IF EXISTS biblioteca;

CREATE DATABASE biblioteca
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_general_ci;

USE biblioteca;

CREATE TABLE autores (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  pais VARCHAR(50),
  ano_nascimento INT
);

CREATE TABLE livros (
  id INT AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR(150) NOT NULL,
  ano_publicacao INT,
  preco DECIMAL(10,2),
  autor_id INT,
  FOREIGN KEY (autor_id) REFERENCES autores(id)
);

CREATE TABLE emprestimos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  livro_id INT,
  data_emprestimo DATE,
  devolvido BOOLEAN,
  FOREIGN KEY (livro_id) REFERENCES livros(id)
);

-- Recriação idempotente dos usuários e privilégios
DROP USER IF EXISTS 'app_biblioteca'@'%';
CREATE USER 'app_biblioteca'@'%' IDENTIFIED BY 'AppBib2026!';
GRANT SELECT, INSERT, UPDATE, DELETE ON biblioteca.* TO 'app_biblioteca'@'%';

DROP USER IF EXISTS 'consulta'@'%';
CREATE USER 'consulta'@'%' IDENTIFIED BY 'Consulta2026!';
GRANT SELECT ON biblioteca.* TO 'consulta'@'%';

FLUSH PRIVILEGES;

-- Carga inicial e expandida de autores
INSERT INTO autores (nome, pais, ano_nascimento) VALUES
('Machado de Assis', 'Brasil', 1839),
('Clarice Lispector', 'Brasil', 1920),
('Gabriel García Márquez', 'Colômbia', 1927),
('Jane Austen', 'Inglaterra', 1775),
('George Orwell', 'Inglaterra', 1903),
('Jorge Amado', 'Brasil', 1912),
('Fiódor Dostoiévski', 'Rússia', 1821),
('Franz Kafka', 'Áustria-Hungria', 1883),
('Virginia Woolf', 'Inglaterra', 1882),
('José Saramago', 'Portugal', 1922),
('Chimamanda Ngozi Adichie', 'Nigéria', 1977),
('Haruki Murakami', 'Japão', 1949),
('Isabel Allende', 'Chile', 1942),
('Graciliano Ramos', 'Brasil', 1892);

-- Carga inicial e expandida de livros
INSERT INTO livros (titulo, ano_publicacao, preco, autor_id) VALUES
('Dom Casmurro', 1899, 39.90, 1),
('Memórias Póstumas de Brás Cubas', 1881, 45.00, 1),
('A Hora da Estrela', 1977, 32.50, 2),
('Cem Anos de Solidão', 1967, 59.90, 3),
('Orgulho e Preconceito', 1813, 29.90, 4),
('Quincas Borba', 1891, 38.90, 1),
('O Alienista', 1882, 24.50, 1),
('Perto do Coração Selvagem', 1943, 36.00, 2),
('A Paixão Segundo G.H.', 1964, 41.90, 2),
('O Amor nos Tempos do Cólera', 1985, 54.90, 3),
('Razão e Sensibilidade', 1811, 34.90, 4),
('1984', 1949, 44.90, 5),
('A Revolução dos Bichos', 1945, 29.90, 5),
('Capitães da Areia', 1937, 42.00, 6),
('Gabriela, Cravo e Canela', 1958, 49.90, 6),
('Crime e Castigo', 1866, 69.90, 7),
('Os Irmãos Karamázov', 1880, 84.90, 7),
('A Metamorfose', 1915, 27.50, 8),
('O Processo', 1925, 39.90, 8),
('Mrs. Dalloway', 1925, 37.90, 9),
('Ao Farol', 1927, 43.50, 9),
('Ensaio sobre a Cegueira', 1995, 52.90, 10),
('Memorial do Convento', 1982, 48.00, 10),
('Hibisco Roxo', 2003, 46.90, 11),
('Americanah', 2013, 55.90, 11),
('Norwegian Wood', 1987, 51.00, 12),
('Kafka à Beira-Mar', 2002, 64.90, 12),
('A Casa dos Espíritos', 1982, 53.90, 13),
('Paula', 1994, 44.00, 13),
('Vidas Secas', 1938, 35.90, 14),
('São Bernardo', 1934, 33.90, 14);

-- Carga de empréstimos de exemplo
INSERT INTO emprestimos (livro_id, data_emprestimo, devolvido) VALUES
(1, '2026-11-01', FALSE),
(4, '2026-11-05', FALSE),
(3, '2026-10-20', TRUE);