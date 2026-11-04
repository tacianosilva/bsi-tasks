
INSERT INTO autores (nome, pais, ano_nascimento) VALUES
('Machado de Assis',        'Brasil',        1839),
('Clarice Lispector',       'Brasil',        1920),
('Gabriel García Márquez',  'Colômbia',      1927),
('Jane Austen',             'Reino Unido',   1775),
('Fiódor Dostoiévski',      'Rússia',        1821),
('Franz Kafka',             'Áustria',       1883),
('Chimamanda Ngozi Adichie','Nigéria',       1977),
('Haruki Murakami',         'Japão',         1949),
('Virginia Woolf',          'Reino Unido',   1882),
('Jorge Amado',             'Brasil',        1912);


-- --- Autores pré-existentes (IDs 1 a 4) ---
INSERT INTO livros (titulo, ano_publicacao, preco, autor_id) VALUES
('Obra Completa do Autor 1',     1998, 59.90,  1),
('Ensaio do Autor 1',            2005, 45.00,  1),
('Romance do Autor 2',           2010, 39.90,  2),
('Contos do Autor 2',            2015, 34.50,  2),
('Poesias do Autor 3',           2001, 29.90,  3),
('Crônicas do Autor 3',          2018, 42.00,  3),
('Estudo do Autor 4',            1995, 55.00,  4),
('Novela do Autor 4',            2020, 48.75,  4),

-- --- Machado de Assis (id 5) ---
('Dom Casmurro',                 1899, 34.90,  5),
('Memórias Póstumas de Brás Cubas', 1881, 39.90, 5),
('Quincas Borba',                1891, 32.50,  5),

-- --- Clarice Lispector (id 6) ---
('A Hora da Estrela',            1977, 36.90,  6),
('Perto do Coração Selvagem',    1943, 44.00,  6),

-- --- Gabriel García Márquez (id 7) ---
('Cem Anos de Solidão',          1967, 54.90,  7),
('O Amor nos Tempos do Cólera',  1985, 49.90,  7),

-- --- Jane Austen (id 8) ---
('Orgulho e Preconceito',        1813, 29.90,  8),
('Emma',                         1815, 31.50,  8),

-- --- Fiódor Dostoiévski (id 9) ---
('Crime e Castigo',              1866, 47.90,  9),
('Os Irmãos Karamazov',          1880, 58.00,  9),

-- --- Franz Kafka (id 10) ---
('A Metamorfose',                1915, 27.90,  10),
('O Processo',                   1925, 41.90,  10),

-- --- Chimamanda Ngozi Adichie (id 11) ---
('Americanah',                   2013, 52.90,  11),
('Meio Sol Amarelo',             2006, 46.50,  11),

-- --- Haruki Murakami (id 12) ---
('Kafka à Beira-Mar',            2002, 56.90,  12),
('Norwegian Wood',               1987, 43.90,  12),

-- --- Virginia Woolf (id 13) ---
('Mrs. Dalloway',                1925, 38.90,  13),
('Ao Farol',                     1927, 40.00,  13),

-- --- Jorge Amado (id 14) ---
('Gabriela, Cravo e Canela',     1958, 37.90,  14),
('Capitães da Areia',            1937, 35.50,  14),
('Dona Flor e Seus Dois Maridos', 1966, 45.90, 14);