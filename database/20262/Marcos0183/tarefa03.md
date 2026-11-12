# Tarefas-bd

Atividades de Banco de Dados


## Identificação

- Nome : Marcos Vinícius Dantas da Silva 

- Usuário Github : Marcos0183

- E-mail Acadêmico: marcos.silva.714@ufrn.edu.br

## Repositório

- Link: https://github.com/Marcos0183/tarefas-bd

### Pergunta-Discursiva 1:

Ao criar uma tabela com comandos DDL, estamos definindo a estrutura da tabela, ou seja, criamos os tipos, tamanho, condições e lógica dos espaços de dados que ainda serão inseridos na tabela. Esses dados são inseridos usando comandos DML, que irão manipular ou inserir os dados nos espaços definidos pelos comando DDL. 

Como estamos usando um comando DDL, que manipula a estrutura da tabela, então ao apagarmos a tabela com DROP, a tabela e seus dados são excluídos. A tabela que é a estrutura onde os dados são armazenados deixa de existir, seus dados não tem mais o espaço para serem guardados, portanto, os dados também são apagados.

### Pergunta-Discursiva 2:

Ao executar o comando DROP Table autores pelo usuário app_biblioteca a interface interrompe a execução do comando, com o seguinte aviso: "Você está prestes a executar um comando DROP. Pode haver perda de dados. Tem certeza?", ao escolhermos que desejemos processeguir, o seguinte erro aparece: 

- "SQL Error [1142] [42000]: DROP command denied to user 'app_biblioteca'@'...' for table 'autores'".

O erro mostrado após a tentativa de execução do comando DROP aconteceu pois o usuário app_biblioteca não possui o privilégio(não é permitido) utilizar desse comando no banco de dados biblioteca, é por esse motivo que na mensagem de erro possui o [1142], que é um indicador do Mariadb de que há falta de privilégio para determinada execução.

A integridade do banco de dados é mantida, uma vez que comandos de usuários não autorizados são proibidos de serem executados, portanto, possíveis tentativas de mudanças não autorizadas no banco de dados não afetaram informações que possuem dependências entre si, não havendo a perca de dados.

### Pergunta-Discursiva 3:

O MariaDB e o CloudBeaver estão executando em dois contêiners distindos, a partir do momento que o CloudBeaver tenta acessar o MariaDB, a conexão parte do endereço de rede do contêiner ClouderBeaver, portanto, para o MariaDB, a origem da conexão não é um 'localhost', mais sim sub-redes virtuais Docker das aplicaçãos ClouderBeaver e dos serviços do Docker. Por esse motivo, é necessário o uso do '%', que permite que a conta responda a conexões de diferentes endereços de rede.

### Pergunta-Discursiva 4:

Após a expansão ficou registrado 14 autores e 33 livros. Ao tentar inserir um livro com o autor_id(FK) = 999 é retornado o seguinte erro : 

- "Error executing query:
SQL Error [1452] [23000]: (conn=5) Cannot add or update a child row: a foreign key constraint fails (`biblioteca`.`livros`, CONSTRAINT `livros_ibfk_1` FOREIGN KEY (`autor_id`) REFERENCES `autores` (`id`))".

Esse erro está indicando que a chave estrangeira(FK), que é um valor do atributo autor_id na tabela autores não existe, e como esse valor não existe, então é impossível que ocorra a referência da tabela livro para a tabela autores. A regra que o banco de dados segue para impedir que ocorra a atribuição de uma chave estrageira não existente é a integridade referencial.

### Pergunta-Discursiva 5: 

Ao evitar redundâncias de dados nas tabelas, evitamos de guardar dados que ja existem em outras relações, dessa forma, as tabelas ficam menores e quanto mais pequenas são, mais simples de realizarem processos de modificação com os dados nelas, pois a etapa de busca ficará mais rápida. Também há um lado positivo para a memória de armazenamento, que tera menos dados repetidos, logo, menos espaço ocupado.


### Questão a)

Uma aplicação comercial nunca deve se conectar ao banco de dados utilizando o usuário root, pois esse usuário possui privilégios administrativos, podendo realizar alterações tanto nos dados quanto na estrutura do banco de dados. O correto é criar um usuário específico para a aplicação, concedendo apenas os privilégios necessários para seu funcionamento. Caso as credenciais desse usuário sejam vazadas, os danos causados ao banco de dados dependerão dos privilégios que ele possui. Se tiver permissões excessivas, um invasor poderá excluir tabelas, modificar registros, acessar informações confidenciais ou até mesmo comprometer todo o banco de dados.

### Questão b)

A diferença entre os privilégios DDL e DML está no tipo de operação que cada um permite realizar no banco de dados. Os privilégios DDL permitem manipular a estrutura do banco de dados, como criar, alterar e excluir tabelas, utilizando comandos como CREATE, ALTER e DROP. Já os privilégios DML permitem manipular os dados armazenados nas estruturas criadas pelos comandos DDL, utilizando comandos como INSERT, UPDATE, DELETE e SELECT. É uma boa prática separar esses privilégios em contas distintas, pois cada usuário terá apenas as permissões necessárias para realizar suas funções, evitando que uma conta responsável por inserir ou consultar dados também possa alterar ou excluir a estrutura das tabelas.

### Questão c)

O arquivo .env.example deve ser versionado no repositório, pois ele serve como um modelo das variáveis de ambiente necessárias para configurar e executar a aplicação, sem armazenar credenciais reais. Já o arquivo .env não deve ser versionado, pois contém informações sensíveis, como senhas e credenciais de acesso ao banco de dados. Caso essas informações sejam publicadas em um repositório público no GitHub, qualquer pessoa poderá ter acesso a elas e utilizá-las para tentar estabelecer conexões com o banco de dados. Dependendo das permissões da conta exposta, isso pode permitir o acesso a informações confidenciais, alterações nos registros ou até mesmo a exclusão de tabelas e dados.

### Questão d)

Não, a utilização do arquivo .env e sua inclusão no .gitignore não eliminam completamente os riscos de segurança das credenciais. Essas medidas evitam que informações sensíveis sejam enviadas acidentalmente para o repositório, mas não impedem que outras pessoas tenham acesso ao arquivo diretamente no sistema onde ele está armazenado. Como as credenciais permanecem em texto puro, caso um invasor consiga acessar o sistema de arquivos do servidor, poderá visualizar as informações presentes no arquivo e utilizá-las para tentar acessar o banco de dados. Portanto, além de utilizar essas medidas, é necessário controlar o acesso aos arquivos, restringir as permissões dos usuários e utilizar mecanismos adicionais de proteção para armazenar e gerenciar credenciais.

### Questão e)

Um contêiner é uma unidade que permite executar uma aplicação ou serviço em um ambiente isolado, contendo suas próprias dependências e configurações necessárias para seu funcionamento. O Docker utiliza essa tecnologia para criar, executar e gerenciar contêineres. Uma das principais vantagens de utilizar o Docker para provisionar ambientes de banco de dados em atividades didáticas é a facilidade de instalação e configuração dos SGBDs, uma vez que não é necessário realizar manualmente todas as etapas de instalação diretamente no sistema operacional do computador. Além disso, podemos utilizar arquivos de configuração, como o docker-compose.yml, para definir os serviços e suas configurações, permitindo que outros alunos reproduzam o mesmo ambiente com maior facilidade. Outra vantagem é o isolamento dos serviços em contêineres, evitando conflitos entre dependências e versões de programas instalados no computador. Dessa forma, o Docker facilita a preparação dos ambientes de estudo, tornando o processo mais organizado, padronizado e simples de reproduzir.


## Desafios Práticos:

### 1. 
Não precisei reconfigurar. Pois, como o CloudBeaver também estar dentro do Docker Compose, ele consegue acessar o MariaDB diretamente pelo rede interna do Docker, ou seja, o que está acontecendo é que os dois estão se comunicando pela porta interna 3306 que não foi mudada e não pela externa que é agora a 3307.

### 2.