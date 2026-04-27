SELECT p.nome AS projeto, a.descricao AS atividade
FROM projeto p
JOIN atividade a ON a.projeto = p.codigo;