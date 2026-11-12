# Tarefas-bd

Atividades de Banco de Dados

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

