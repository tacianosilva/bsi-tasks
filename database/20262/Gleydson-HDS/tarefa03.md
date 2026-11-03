# **TAREFA 03: DOCKER, MARIADB e ADMINISTRAÇÃO DE SGBD**

### **1. IDENTIFICAÇÃO**

Disciplina: DCT2201 — Banco de Dados

Aluno: Gleydson Henrique Dantas da Silva

Usuário do GitHub: Gleydson-HDS

Repositório pessoal: https://github.com/Gleydson-HDS/dct2201-banco-de-dados

---

### **2. RESPOSTAS ÀS PERGUNTAS DISCURSIVAS DOS PASSOS PRÁTICOS**

***PERGUNTA DISCURSIVA 01 - Explique com suas palavras a diferença entre criar uma tabela (DDL) e inserir 
registros nessa tabela (DML). Se apagarmos uma tabela com um comando DDL (DROP TABLE), o que acontece com os 
dados que estavam dentro dela?***
  
    A DDL (Data Definition Language) é utilizada para definir e modificar a estrutura do banco de dados, 
    como criar   tabelas com o comando CREATE TABLE. Já a DML (Data Manipulation Language) é utilizada para 
    manipular os dados armazenados nessas tabelas, como inserir registros com o comando INSERT INTO. 
  
    Se apagarmos uma tabela utilizando o comando DROP TABLE, sua estrutura e todos os dados armazenados nela 
    serão    excluídos. Por isso, esse comando deve ser utilizado com cuidado, pois a perda dos dados pode ser 
    permanente caso não exista um backup.

***PERGUNTA DISCURSIVA 02 - Descreva com suas palavras o que aconteceu quando você tentou executar o comando
DROP TABLE autores com a conta app_biblioteca. Por que o MariaDB recusou a operação com o erro 1142? De que 
forma essa restrição protege a integridade do banco de dados caso a aplicação web sofra uma invasão ou falha 
de programação?***
  
    Ao utilizar a conta app_biblioteca, foi testada a execução do comando:

    DROP TABLE autores;

    O MariaDB recusou o comando porque o usuário app_biblioteca recebeu apenas permissões para consultar, 
    inserir, atualizar e excluir registros. Ele não recebeu o privilégio DROP, necessário para excluir uma tabela.

    Essa restrição ajuda a proteger a estrutura do banco de dados. Caso uma aplicação web seja invadida ou
    apresente uma falha de programação, as permissões limitadas reduzem o risco de que ela exclua tabelas e
    comprometa a estrutura do banco.

***PERGUNTA DISCURSIVA 03 - Por que os usuários foram criados com o host '%' em vez de 'localhost'? Qual é o papel 
da rede interna do Docker nessa decisão técnica?***

    Os usuários foram criados com o host % porque esse caractere permite conexões originadas de diferentes 
    endereços de rede, conforme as regras de autenticação do MariaDB.

    No ambiente Docker, o CloudBeaver e o MariaDB podem funcionar em contêineres separados e comunicar-se pela 
    rede   interna do Docker. Nesse cenário, a conexão entre os serviços não é necessariamente identificada como 
    uma conexão proveniente de localhost.

    Por isso, o uso de % permite que os usuários sejam autenticados a partir dos endereços de rede utilizados 
    pelos   serviços. Em ambientes reais, essa permissão deve ser restringida sempre que possível, seguindo o 
    princípio do
    menor privilégio.    

***PERGUNTA DISCURSIVA 04 - Quantos autores e livros no total ficaram cadastrados na sua base após a execução da 
carga expandida? O que aconteceria se você tentasse inserir um livro cujo autor_id fosse 999 (um autor inexistente)?
Qual regra do banco impede essa ação?***

    Após a execução da carga expandida, a base de dados biblioteca ficou com 14 autores e 36 livros cadastrados.      
    Apesar do enunciando pedir pelo menos 25, optei por aumentar o leque de livros.

    Se eu tentasse inserir um livro utilizando o valor 999 na coluna autor_id, sendo que não existe um autor com 
    esse identificador na tabela autores, o MariaDB recusaria a operação. Isso acontece porque a coluna autor_id      da tabela livros possui uma chave estrangeira (FOREIGN KEY) que referencia a coluna id da tabela autores.

    Essa restrição aplica a regra da integridade referencial, que impede que um livro seja associado a um autor 
    inexistente, mantendo a consistência dos relacionamentos entre as tabelas.

***PERGUNTA DISCURSIVA 05 - Analise as Consultas 4 e 5. Em linguagem simples, qual é a vantagem prática de dividir os dados em duas tabelas
relacionadas (autores e livros) em vez de guardar o nome e o país do autor repetido dentro de cada linha da tabela de livros?***

    A principal vantagem de dividir os dados em duas tabelas relacionadas, autores e livros, é evitar a
    repetição desnecessária de informações e facilitar a manutenção do banco de dados.
    
    Se o nome e o país de cada autor fossem armazenados repetidamente em cada registro de livro,
    seria necessário atualizar várias linhas caso alguma dessas informações mudasse.
    Isso aumentaria o risco de inconsistências, como o mesmo autor aparecer com nomes ou países diferentes.

    Com a separação das tabelas, as informações de cada autor ficam armazenadas uma única
    vez na tabela autores, enquanto a tabela livros utiliza a coluna autor_id para estabelecer
    o relacionamento entre as obras e seus autores. A consulta INNER JOIN permite recuperar essas
    informações em conjunto, sem precisar duplicar os dados dos autores em cada livro.

    Dessa forma, essa organização reduz a redundância, facilita as atualizações e contribui para
    manter a consistência e a integridade dos dados.

---

