Aluno: Henderson Emanuel Bernardo de Medeiros

Usuário: HendsMede1r0s

Email: henderson.medeiros.131@ufrn.edu.br 

Link do repositório: [https://github.com/HendsMede1r0s/dct2201-banco-de-dados](https://github.com/HendsMede1r0s/dct2201-banco-de-dados)


# Perguntas Discursivas

## Pergunta Discursiva 1
### Descreva com suas palavras o que aconteceu quando você tentou executar o comando DROP TABLE autores com a conta app_biblioteca. Por que o MariaDB recusou a operação com o erro 1142? De que forma essa restrição protege a integridade do banco de dados caso a aplicação web sofra uma invasão ou falha de programação?

DDL é a definição do banco de dados, nela você implementa as regras que aquele banco terá e que todos os dados terão que seguir essas regras. É a DDL que dá as permissões, as regras, os limites e as barreiras que todo dado que ali está deve seguir.

DML é basicamente o CRUD do banco de dados, nela podemos manipular os dados conforme quisermos, se esses dados estiverem dentro das regras do DDL. Portanto, podemos cadastrar, vizualizar, editar ou excluir os dados daquele banco com a DML.

* Caso apagemos uma tabela inteira com um _DROP TABLE_, os dados e informações daquela tabela irão desaparacer, pois eles estariam ligados a diretamenta aquela tabela que foi apagada, portanto se se apagarmos uma tabela, os dados que ali estão também serão apagados. Contudo os bancos de dados atuais costumam possuir ua regra que impede a exclusão de tabelas que já tenham dados nelas, para que esses dados não sejam perdidos.

## Pergunta Discursiva 2
### Descreva com suas palavras o que aconteceu quando você tentou executar o comando DROP TABLE autores com a conta app_biblioteca. Por que o MariaDB recusou a operação com o erro 1142? De que forma essa restrição protege a integridade do banco de dados caso a aplicação web sofra uma invasão ou falha de programação?

Quando se utiliza _DROP TABLE autores_ com uma conta que tenha a permissão necessária, como app_biblioteca, o MariaDB alerta que fazer essa operação causará a perda de todos os dados daquela tabela. ele dá esse erro para impedir a perda dos dados. 

* Caso ocorra uma invasão ou falha no banco de dados, esse erro impede que qualquer coisa que aconteça, os dados e as tabelas serão mantidos sem serem perdidos. pois independente da permissão da pessoa sobre o banco, ela não poderá ocasionar uma perda de dados intencionalmente ou Inconscientemente.

## Pergunta Discursiva 3
### Por que os usuários foram criados com o host '%' em vez de 'localhost'? Qual é o papel da rede interna do Docker nessa decisão técnica?

no localhost só autoriza se o cliente estiver rodando dentro do próprio contêiner do MariaDB. já no '%', Autoriza conexões vindas de outros contêineres através da rede do Docker. O docker é como se fosse um servidor que rodasse pro fora para podermos rodar da maquina que quisermos.

## Pergunta Discursiva 4
### Quantos autores e livros no total ficaram cadastrados na sua base após a execução da carga expandida? O que aconteceria se você tentasse inserir um livro cujo autor_id fosse 999 (um autor inexistente)? Qual regra do banco impede essa ação?

foram adicionados 10 autores e 26 livros. e caso fossem inserido um livro com autor_id de 999 iria dar erro, pois não há um autor com esse id, portanto não daria para colocar um livro em um autor que não existe. e isso é a é a Restrição de Integridade Referencial.

## Pergunta Discursiva 5
### Analise as Consultas 4 e 5. Em linguagem simples, qual é a vantagem prática de dividir os dados em duas tabelas relacionadas (autores e livros) em vez de guardar o nome e o país do autor repetido dentro de cada linha da tabela de livros?

é necessário pra não deixarmos dados redundantes e para separmos apenas o que é viavel para a quelasituação. por exemplo, em nenhum dos casos precisavamos do país, protanto é bom, para não deixarmos tudo junto e misturado, causando futuras confusões, que separemos o que queremos em tabelas para que juntemos logo após.

# Desafios Práticos

## Bloco A: Docker e Infraestrutura de Ambiente

1. Após mudança da porta e reinicialização do docker, tivemos que refazer a conexão a partir do mariadb com a porta correta
2. Para que tenhamos ambientes simultaneos preciamos criar novos arquivos onde mudamos as portas, os nomes dos contêineres e mudaros volumes de um novo arquivo yml
3. Conseguimos logar com a senha antiga pois já existe um banco de dados criado lá, então ele acaba ignorando as senhas. para que mjdemos a senha podemos mudar nos volumes do arquivo yml e reiniando; ou fazendo mudando pelo SQL editor com comandos.
4. Na mensagem de erro diz que é preciso de uma senha para que rodemos o docker. mas podemos usar o ":?" como um "se não", caso tenha senha utilize isso, caso não utilizaria uma pré definida para que nunca dê esse erro caso a pessoa esquecesse de por uma root password.
5. A MARIADB_DATABASE, a MARIA_ROOT_PASSWORD e o target de mariadb

## Bloco B: Modelagem e Consultas SQL Básicas
6. CREATE TABLE emprestimos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    livro_id INT,
    data_emprestimo DATE,
    devolvido BOOLEAN,
    FOREIGN KEY (livro_id) REFERENCES livros(id)
);

7. INSERT INTO emprestimos (livro_id, data_emprestimo, devolvido) VALUES 
(1, '2026-10-15', FALSE),
(2, '2026-10-20', FALSE),
(3, '2026-10-25', TRUE);

8. SELECT 
    l.titulo, 
    e.data_emprestimo, 
    a.nome AS autor
    FROM emprestimos e
    JOIN livros l ON e.livro_id = l.id
    JOIN autores a ON l.autor_id = a.id
    WHERE e.devolvido = FALSE;

9. SELECT 
    a.nome AS autor, 
    COUNT(l.id) AS total_livros
    FROM autores a
    JOIN livros l ON a.id = l.autor_id
    GROUP BY a.id, a.nome
    HAVING COUNT(l.id) > 1;

10. SELECT id, titulo, preco FROM livros WHERE id = 1;
    UPDATE livros 
    SET preco = preco * 1.10 
    WHERE id = 1;
    SELECT id, titulo, preco FROM livros WHERE id = 1;

11. INSERT INTO autores (nome, pais, ano_nascimento) 
    VALUES ('Autor Temporario Teste', 'Brasil', 2000);
    SELECT id, nome FROM autores WHERE nome = 'Autor Temporario Teste';
    DELETE FROM autores 
    WHERE nome = 'Autor Temporario Teste';

## Bloco C: Administração e Privilégios Avançados

12. CREATE USER 'relatorios'@'%' IDENTIFIED BY 'Relatorios2026!';
    GRANT SELECT ON biblioteca.livros TO 'relatorios'@'%';
    FLUSH PRIVILEGES;
13. Error executing query:
SQL Error [1142] [42000]: (conn=19) SELECT command denied to user 'relatorios'@'172.18.0.3' for table `biblioteca`.`autores`

Esse erro ocorre pois o usuário que foi criado não possui permisão para ver autores, mas sim exclusivamente a tabela livros.

14. Antes de revogarmos o Insert, o usuário tinha o poder de inserir qualquer coisa dentro do banco, mas depois que tiramos a permissão com o revoke e tentamos novamente adicionar outro livro, dá um erro, pois o usuário não possui mais o a permissão de fazer tal coisa.