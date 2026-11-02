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

    - Resposta: DDL serve para criar a estrutura da tabela que receberá dados posteriormente, mas está vazia em sua concepção. DML serve para popular a tabela com dados que estejam organizados conforme a estrutura da tabela e as regras do banco impostas. Ao apagar uma tabela utilizando o comando DROP TABLE, a estrutura da tabela e todos os dados armazenados nela são eliminados definitivamente do banco de dados. Caso existam restrições de chave estrangeira apontando para essa tabela, o SGBD interromperá a execução do comando e exibirá um erro, impedindo o apagamento até que as dependências sejam resolvidas.
- **Pergunta 2**
    - Enunciado: *Descreva com suas palavras o que aconteceu quando você tentou executar o comando `DROP TABLE autores` com a conta `app_biblioteca`. Por que o MariaDB recusou a operação com o erro 1142? De que forma essa restrição protege a integridade do banco de dados caso a aplicação web sofra uma invasão ou falha de programação?*

    - Resposta: Ao tentar executar o comando `DROP TABLE autores` logado como `app_biblioteca`, o MariaDB interrompeu a operação e retornou o erro 1142 (42000): `DROP command denied to user 'app_biblioteca'@'...' for table 'autores'`. Isso aconteceu porque a conta da aplicação não possui o privilégio DDL DROP concedido no banco de dados.
    Ao tentar executar o comando DROP TABLE autores logado como app_biblioteca, o MariaDB interrompeu a operação e retornou o erro 1142 (42000): DROP command denied to user 'app_biblioteca'@'localhost' for table 'autores'. Isso aconteceu porque a conta da aplicação não possui o privilégio DDL DROP concedido no banco de dados.
    Essa restrição segue o Princípio do Menor Privilégio, garantindo que a conta da aplicação tenha apenas os acessos estritamente necessários para o seu funcionamento em tempo de execução (como SELECT, INSERT, UPDATE e DELETE). Se algum invasor tentasse injetar um script malicioso, o sgbd bloquearia a operação. O mesmo aconteceria se alguem cometesse algum erro durante o processo de programação, desde que a operação tentada exija um privilégio que a conta da aplicação não possui
- **Pergunta 3**
    - Enunciado: *Por que os usuários foram criados com o host `'%'` em vez de `'localhost'`? Qual é o papel da rede interna do Docker nessa decisão técnica?*

    - Resposta: A especificação `'usuario'@'localhost'` limita o acesso estritamente a conexões locais que partem de dentro do próprio contêiner do banco de dados (via soquete Unix ou interface de loopback). Por estarem em contêineres distintos, o CloudBeaver faz a conexão utilizando o IP atribuído à sua própria interface na rede do Docker. Como o IP exato dos contêineres pode mudar a cada reinicialização ou recriação do ambiente, utiliza-se o caractere coringa '%' ('usuario'@'%'), que instrui o SGBD a aceitar conexões vindas de qualquer endereço IP, viabilizando a comunicação entre os contêineres da rede Docker.
- **Pergunta 4**
    - Enunciado: *Quantos autores e livros no total ficaram cadastrados na sua base após a execução da carga expandida? O que aconteceria se você tentasse inserir um livro cujo `autor_id` fosse 999 (um autor inexistente)? Qual regra do banco impede essa ação?*

    - Resposta: Após a execução do script de carga expandida, o banco de dados ficou com 14 autores e 30 livros cadastrados.
    Caso houvesse a tentativa de inserir um livro com `autor_id = 999`, o MariaDB recusaria a operação e retornaria um erro de violação de restrição.
    A regra responsável por esse bloqueio é o princípio da integridade referencial, implementada na tabela livros por meio de uma restrição de chave estrangeira (FOREIGN KEY):
    `FOREIGN KEY (autor_id) REFERENCES autores(id)`
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