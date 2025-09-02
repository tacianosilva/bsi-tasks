-- Inserindo departamentos ADICIONAIS (Vendas e Compras já existem)
INSERT INTO departamento (nome_dep, gerente, dt_inicio_gerencia) VALUES ('RH', 9491, '2022-01-10');       -- cod_dep = 3
INSERT INTO departamento (nome_dep, gerente, dt_inicio_gerencia) VALUES ('Engenharia',9491, '2021-08-20'); -- cod_dep = 4

-- Inserindo empregados ADICIONAIS (Ana, Taciano, João e Maria já existem) e referenciando departamentos CORRETAMENTE
INSERT INTO empregado (matricula, nome, data_nasc, endereco, sexo, salario, depto) VALUES
(9495, 'Xuxa', '1970-03-27', 'Rua E, 321', 'F', 4500.00, 3), -- RH
(9496, 'Sasha', '1998-07-12', 'Rua F, 654', 'F', 3200.00, 4), -- Engenharia
(9497, 'José', '1988-11-02', 'Rua G, 987', 'M', 3800.00, 4), -- Engenharia
(9498, 'Marcos', '1992-06-18', 'Rua H, 741', 'M', 4200.00, 4), -- Engenharia
(9499, 'Mariana', '1987-09-29', 'Rua I, 852', 'F', 3900.00, 4); -- Engenharia

-- Modificando os gerentes dos departamentos ADICIONAIS (Vendas e Compras já tem gerentes)
UPDATE departamento SET gerente = 9495 WHERE cod_dep = 3; -- Xuxa (9495) é gerente do RH
UPDATE departamento SET gerente = 9493 WHERE cod_dep = 4; -- João (9493) é gerente da Engenharia

-- Inserindo projetos, referenciando departamentos existentes
INSERT INTO projeto (nome, localizacao, depart, lider) VALUES
('Projeto X', 'Caicó', 1, 9491), -- Vendas, liderado por Ana
('Projeto H', 'Natal', 1, 9491), -- Vendas, liderado por Ana
('Projeto U', 'Mossoró', 2, 9492), -- Compras, liderado por Taciano
('Projeto Y', 'Parnamirim', 4, 9493), -- Engenharia, liderado por João
('Projeto Z', 'João Pessoa', 3, 9495); -- RH, liderado por Xuxa

-- Inserindo dependentes
INSERT INTO dependente (matricula, nome, sexo) VALUES
(9495, 'Doisberto', 'M'),
(9496, 'Sashinha', 'F'),
(9497, 'Júnior', 'M'),
(9498, 'Marquinho', 'M'),
(9499, 'Marianinha', 'F');

-- Alocando empregados aos projetos (3 a 4 por projeto, considerando os empregados já existentes)
INSERT INTO alocacao (matric, cod_proj, horas) VALUES
(9491, 1, 20.00), -- Projeto X (Vendas)
(9496, 1, 15.00),
(9497, 1, 10.00),

(9491, 2, 12.00), -- Projeto H (Vendas)
(9495, 2, 18.00),
(9498, 2, 24.00),

(9492, 3, 30.00), -- Projeto U (Compras)
(9494, 3, 25.00),
(9499, 3, 15.00),

(9493, 4, 40.00), -- Projeto Y (Engenharia)
(9496, 4, 35.00),
(9497, 4, 20.00),
(9498, 4, 10.00),

(9495, 5, 30.00),-- Projeto Z (RH)
(9491, 5, 25.00),
(9492, 5, 15.00);
