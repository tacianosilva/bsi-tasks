## 1. Identificação e Repositório
**Nome**
- Eriky Rayan Bezerra de Medeiros

**Usuário no GitHub**
- Eriky-Rayan

**Email Acadêmico**
- eriky.medeiros.706@ufrn.edu.br

**Repositório Público**
- https://github.com/Eriky-Rayan/dct2201-banco-de-dados.git

## 2. Respostas às Perguntas Discursivas dos Passos Práticos

- **Pergunta 1**
    - Enunciado: *Explique com suas palavras a diferença entre criar uma tabela (DDL) e inserir registros nessa tabela (DML). Se apagarmos uma tabela com um comando DDL (`DROP TABLE`), o que acontece com os dados que estavam dentro dela?*

    - Resposta:
- **Pergunta 2**
    - Enunciado: *Descreva com suas palavras o que aconteceu quando você tentou executar o comando `DROP TABLE autores` com a conta `app_biblioteca`. Por que o MariaDB recusou a operação com o erro 1142? De que forma essa restrição protege a integridade do banco de dados caso a aplicação web sofra uma invasão ou falha de programação?*

    - Resposta:
- **Pergunta 3**
    - Enunciado: *Por que os usuários foram criados com o host `'%'` em vez de `'localhost'`? Qual é o papel da rede interna do Docker nessa decisão técnica?*

    - Resposta:
- **Pergunta 4**
    - Enunciado: *Quantos autores e livros no total ficaram cadastrados na sua base após a execução da carga expandida? O que aconteceria se você tentasse inserir um livro cujo `autor_id` fosse 999 (um autor inexistente)? Qual regra do banco impede essa ação?*

    - Resposta:
- **Pergunta 5**
    - Enunciado: *Analise as Consultas 4 e 5. Em linguagem simples, qual é a vantagem prática de dividir os dados em duas tabelas relacionadas (`autores` e `livros`) em vez de guardar o nome e o país do autor repetido dentro de cada linha da tabela de livros?*

    - Resposta:

## 3. Respostas Dissertativas Conceituais

 - **Questão a:** Por que uma aplicação comercial nunca deve se conectar ao banco de dados utilizando o usuário `root`? O que pode ocorrer com o servidor de banco de dados caso as credenciais do usuário da aplicação sejam vazadas?
    - Resposta:
- **Questão b:** Qual é a diferença fundamental entre privilégios DDL (Data Definition Language) e DML (Data Manipulation Language)? Por que é uma boa prática de segurança separá-los em contas de usuários distintas?
    - Resposta:
- **Questão c:** Por que o arquivo `.env.example` deve ser commitado no repositório de código enquanto o arquivo `.env` nunca deve ser versionado? Quais são os riscos e consequências práticas de comitar credenciais reais em um repositório público no GitHub?
    - Resposta:
- **Questão d:** O uso do arquivo `.env` e a inclusão no `.gitignore` eliminam por completo todos os riscos de segurança de credenciais em um ambiente de desenvolvimento e produção? Justifique sua resposta considerando que o arquivo permanece armazenado em texto puro no sistema de arquivos do servidor.
    - Resposta:
- **Questão e:** O que é um contêiner e quais são as principais vantagens de utilizar o Docker para provisionar ambientes de banco de dados em atividades didáticas de graduação em comparação com a instalação manual do SGBD diretamente no sistema operacional do computador do aluno?
    - Resposta:

## 4. Desafios Realizados