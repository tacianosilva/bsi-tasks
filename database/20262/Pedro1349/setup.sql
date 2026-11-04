DROP DATABASE IF EXISTS biblioteca;

CREATE DATABASE biblioteca
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_general_ci;

USE biblioteca;

-- Criação das tabelas
CREATE TABLE IF NOT EXISTS autores (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  pais VARCHAR(50),
  ano_nascimento INT
);

CREATE TABLE IF NOT EXISTS livros (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR(150) NOT NULL,
  ano_publicacao INT,
  preco DECIMAL(10,2),
  autor_id INT UNSIGNED,
  FOREIGN KEY (autor_id) REFERENCES autores(id)
);

CREATE TABLE IF NOT EXISTS emprestimos (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    livro_id int UNSIGNED,
    data_emprestimo DATE NOT NULL,
    devolvido boolean,
    FOREIGN KEY (livro_id) REFERENCES livros(id)
);

-- Povoamento
INSERT INTO autores (nome, pais, ano_nascimento) VALUES
('Machado de Assis', 'Brasil', 1839),
('Clarice Lispector', 'Brasil', 1920),
('Gabriel García Márquez', 'Colômbia', 1927),
('Jane Austen', 'Inglaterra', 1775);
('Machado de Assis2', 'Brasil', 1839),
('William Shakespeare2', 'Inglaterra', 1564),
('Victor Hugo2', 'França', 1802),
('Jane Austen2', 'Inglaterra', 1775),
('Franz Kafka', 'República Tcheca', 1883),
('Gabriel García Márquez', 'Colômbia', 1927),
('Leo Tolstói', 'Rússia', 1828),
('Clarice Lispector', 'Ucrânia/Brasil', 1920),
('Homero', 'Grécia Antiga', -800),
('Mary Shelley', 'Inglaterra', 1797);

INSERT INTO livros (titulo, ano_publicacao, preco, autor_id) VALUES
('Dom Casmurro2', 1899, 39.90, 1),
('Memórias Póstumas de Brás Cubas2', 1881, 45.00, 1),
('A Hora da Estrela2', 1977, 32.50, 2),
('Cem Anos de Solidão2', 1967, 59.90, 3),
('Orgulho e Preconceito2', 1813, 29.90, 4);
('A Jornada do Conhecimento2', 2018, 45.90, 1),
('Mistérios da Antiguidade2', 2020, 59.90, 2),
('O Segredo das Estrelas2', 2019, 39.90, 3),
('Caminhos da Literatura2', 2021, 49.90, 4),
('A Arte de Pensar2', 2022, 54.90, 1),
('Contos do Amanhã2', 2023, 42.90, 2),
('Histórias de Outros Mundos2', 2017, 64.90, 3),
('Reflexões sobre a Vida2', 2024, 35.90, 4),
('Memórias Póstumas de Brás Cubas2', 1881, 39.90, 5),
('Dom Casmurro', 1899, 44.90, 5),
('Romeu e Julieta', 1597, 49.90, 6),
('Hamlet', 1603, 54.90, 6),
('Os Miseráveis', 1862, 89.90, 7),
('O Corcunda de Notre-Dame', 1831, 69.90, 7),
('Orgulho e Preconceito', 1813, 49.90, 8),
('Razão e Sensibilidade', 1811, 45.90, 8),
('A Metamorfose', 1915, 34.90, 9),
('O Processo', 1925, 42.90, 9),
('Cem Anos de Solidão', 1967, 59.90, 10),
('O Amor nos Tempos do Cólera', 1985, 64.90, 10),
('Guerra e Paz', 1869, 99.90, 11),
('Anna Kariênina', 1878, 79.90, 11),
('A Hora da Estrela', 1977, 39.90, 12),
('Perto do Coração Selvagem', 1943, 44.90, 12),
('Ilíada', -750, 59.90, 13),
('Odisseia', -700, 59.90, 13),
('Frankenstein', 1818, 49.90, 14),
('O Último Homem', 1826, 54.90, 14);

INSERT INTO emprestimos (livro_id, data_emprestimo, devolvido) VALUES
(1, '2026-11-01', TRUE),
(2, '2026-11-02', FALSE),
(5, '2026-11-03', FALSE);

-- UPDATES:
UPDATE livros
SET preco = preco + preco/2
WHERE id = 2;

-- CRIAÇÃO DE USUÁRIOS E ADIÇÃO DE PRIVILÉGIOS
CREATE USER 'app_biblioteca'@'%' IDENTIFIED BY 'AppBib2026!';
CREATE USER 'consulta'@'%' IDENTIFIED BY 'Consulta2026!';
CREATE USER 'relatorios'@'%' IDENTIFIED BY 'Relatorios2026!';

GRANT SELECT, INSERT, UPDATE, DELETE ON biblioteca.* TO 'app_biblioteca'@'%';
GRANT SELECT ON biblioteca.* TO 'consulta'@'%';
GRANT SELECT ON biblioteca.livros TO 'relatorios'@'%';

FLUSH PRIVILEGES;
