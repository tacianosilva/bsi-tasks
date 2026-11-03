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

### **3. RESPOSTAS DISSERTATIVAS CONCEITUAIS**

**Questão a: Por que uma aplicação comercial nunca deve se conectar ao banco de dados utilizando o usuário root? O que pode ocorrer com o servidor de banco de dados caso as credenciais do usuário da aplicação sejam vazadas?**

    Uma aplicação comercial nunca deve utilizar o usuário root para se conectar ao banco de dados, pois ele possui privilégios administrativos elevados, podendo criar, alterar e excluir bancos de dados, tabelas e usuários. Caso a aplicação apresente uma falha de segurança ou suas credenciais sejam vazadas, um invasor poderá utilizar esses privilégios para comprometer todo o servidor de banco de dados.
    
    Entre as possíveis consequências estão a exclusão ou alteração de dados, o roubo de informações confidenciais, a criação de usuários não autorizados e a interrupção dos serviços.
    
    Por isso, recomenda-se utilizar um usuário específico para a aplicação, com permissões limitadas às operações necessárias. Esse princípio é conhecido como Princípio do Menor Privilégio, reduzindo os danos que podem ocorrer em caso de comprometimento das credenciais.
    
**Questão b: Qual é a diferença fundamental entre privilégios DDL (Data Definition Language) e DML (Data Manipulation Language)? Por que é uma boa prática de segurança separá-los em contas de usuários distintas?**

    A diferença fundamental entre DDL e DML está no tipo de operação realizada no banco de dados.

    DDL (Data Definition Language): permite definir e modificar a estrutura do banco de dados, por meio de comandos como CREATE, ALTER e DROP, utilizados para criar, alterar e excluir tabelas e outros objetos.

    DML (Data Manipulation Language): permite manipular os dados armazenados nas tabelas, por meio de comandos como INSERT, UPDATE e DELETE, utilizados para inserir, atualizar e excluir registros.

    Separar esses privilégios em contas distintas é uma boa prática de segurança porque limita as ações que cada usuário pode realizar. Por exemplo, uma aplicação que precisa apenas cadastrar e consultar informações não necessita de permissão para alterar a estrutura do banco de dados.
    
    Dessa forma, caso as credenciais de uma aplicação sejam comprometidas, o invasor terá menos possibilidades de causar danos, como excluir tabelas ou modificar a estrutura do banco. Essa separação também facilita o controle de acesso e a administração do banco de dados.

**Questão c: Por que o arquivo .env.example deve ser commitado no repositório de código enquanto o arquivo .env nunca deve ser versionado? Quais são os riscos e consequências práticas de comitar credenciais reais em um repositório público no GitHub?**

    O arquivo .env.example deve ser versionado porque funciona como um modelo de configuração, indicando quais variáveis de ambiente são necessárias para executar o projeto, sem armazenar credenciais reais. Dessa forma, outros desenvolvedores conseguem configurar seu próprio ambiente utilizando esse arquivo como referência.
    
    Já o arquivo .env contém configurações locais e informações sensíveis, como senhas e credenciais de acesso ao banco de dados. Por isso, ele não deve ser versionado e precisa estar listado no .gitignore.
    
    Comitar credenciais reais em um repositório público no GitHub pode permitir que pessoas não autorizadas obtenham acesso ao banco de dados e a outros serviços. Entre as possíveis consequências estão o roubo, a alteração ou a exclusão de informações, além do comprometimento de todo o ambiente.
    
    É importante destacar que excluir o arquivo de um commit posterior não elimina necessariamente o risco, pois as credenciais podem continuar disponíveis no histórico do Git ou em cópias do repositório. Caso isso aconteça, as senhas expostas devem ser alteradas imediatamente.
    
**Questão d: O uso do arquivo .env e a inclusão no .gitignore eliminam por completo todos os riscos de segurança de credenciais em um ambiente de desenvolvimento e produção? Justifique sua resposta considerando que o arquivo permanece armazenado em texto puro no sistema de arquivos do servidor.**

    Não. O uso do arquivo .env e sua inclusão no .gitignore não eliminam completamente os riscos de segurança das credenciais. Essas medidas evitam que o arquivo seja enviado acidentalmente ao repositório Git, mas não protegem seu conteúdo contra acessos indevidos no próprio sistema.
    
    Como o arquivo permanece armazenado em texto puro no sistema de arquivos do servidor, qualquer pessoa ou processo que consiga acessá-lo poderá visualizar as credenciais, caso não existam outras medidas de proteção.
    
    Entre os riscos estão o acesso não autorizado ao arquivo, o vazamento por meio de backups desprotegidos, a exposição em logs e o comprometimento do servidor.
    
    Para reduzir esses riscos, é importante restringir as permissões de leitura do arquivo, proteger os backups, evitar registrar senhas em logs e utilizar ferramentas de gerenciamento de segredos (Secrets Management) em ambientes de produção.
    
    Portanto, o .env e o .gitignore são medidas importantes, mas devem fazer parte de uma estratégia de segurança mais ampla, que proteja as credenciais durante todo o seu armazenamento e utilização.

**Questão e: O que é um contêiner e quais são as principais vantagens de utilizar o Docker para provisionar ambientes de banco de dados em atividades didáticas de graduação em comparação com a instalação manual do SGBD diretamente no sistema operacional do computador do aluno?**

    Um contêiner é uma unidade isolada que reúne uma aplicação e suas dependências necessárias para funcionar, utilizando recursos do sistema operacional hospedeiro. Ele permite executar aplicações em ambientes separados, sem a necessidade de instalar e configurar todos os componentes diretamente no computador.
    
    A utilização do Docker para provisionar ambientes de banco de dados em atividades didáticas apresenta diversas vantagens em comparação com a instalação manual de um SGBD:
    
    Facilidade de instalação: permite configurar o MariaDB e outras ferramentas por meio de arquivos de configuração, como o docker-compose.yml.
    
    Padronização: todos os alunos podem utilizar o mesmo ambiente, reduzindo problemas causados por diferenças entre sistemas operacionais e configurações.
    
    Isolamento: os serviços executados nos contêineres ficam separados do sistema operacional e de outras aplicações.
    
    Reprodutibilidade: permite recriar o ambiente com as mesmas configurações sempre que necessário.
    
    Facilidade de manutenção: possibilita iniciar, parar e substituir contêineres sem precisar reinstalar o SGBD no computador.
    
    Organização: permite executar diferentes versões ou instâncias de bancos de dados simultaneamente, utilizando portas distintas.
    
    Portanto, o Docker facilita o aprendizado e a realização de atividades práticas, pois oferece ambientes padronizados, isolados e reproduzíveis, reduzindo o tempo gasto com instalações e configurações manuais.
