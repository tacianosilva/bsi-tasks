# 1 - Indentificação
 - **Nome Completo:** Pedro Lucas da Silva Araújo;
 - **Usuário no GitHub:** Pedro1349;
 - **Email Acadêmico:** pedro.araujo.716@ufrn.edu.br;
 - **Repositório pessoal:** [BD_UFRN_Tarefa03](https://github.com/Pedro1349/BD_UFRN_Tarefa03);

# 2 - Perguntas Discursivas:
## Pergunta Discursiva 1: Diferença entre DDL e DML, e impacto de um DROP TABLE
  ### Resposta:
  Criar uma tabela é uma instrução DDL de "CREATE", ou seja, é um comando que cria uma estrutura no banco de dados (tabela). Inserir registros é uma instrução DML de "INSERT", ou seja, é um comando usado para inserir dados em uma tabela no banco de dados.
  Se apagar uma tabela com um comando DDL, os dados que estavam nela são deletados também

## Pergunta Discursiva 2: Análise do erro 1142 ao tentar DROP TABLE com usuário restrito e relação com o princípio do menor privilégio.
  ### Resposta:
  O MariaDB recusou a operação e deu o seguinte erro: "SQL Error [1142] [42000]: DROP command denied to user 'app_biblioteca'@'...' for table 'autores'".
  A operação foi recusada, pois o usuário "app_biblioteca" não tem permissão para executar comandos DDL
  Em caso de invasão na conta do "app_biblioteca", o impacto ao sistema é limitado, pois se o hacker tentar executar comandos DDL, o MariaDB rejeitará a ação automaticamente. Da mesma forma, essa restrição funciona como uma camada de proteção contra falhas de programação e erros humanos, impedindo que scripts de testes mal escritos executem exclusões irreversíveis e causem a perda de tabelas inteiras de produção.

## Pergunta Discursiva 3: Justificativa técnica para o uso do host '%' em vez de 'localhost' na arquitetura conteinerizada do Docker.
  ### Resposta:
  porque ao usar "localhost", o MariaDB só aceitaria conexões que nascessem dentro do próprio container dele. Como o CloudBeaver está rodando em outro container separado, o banco de dados enxerga a requisição vindo de um IP externo, e não do localhost.
  Por isso o "%" é usado, já que ele permite conexões vindas de qualquer endereço IP.

## Pergunta Discursiva 4: Relato sobre o povoamento expandido gerado com IA (quantidade final de registros) e o que ocorre ao tentar associar livro a autor inexistente (integridade referencial).
  ### Resposta:
  total de autores é 14, já o total de livros é 32 (5 antigos + 28 criados).
  Se eu tentasse inserir um livro cujo autor_id é 999, O MariaDB rejeitaria a inserção e apresentaria um erro de violação de chave estrangeira (autor não existe). A regra do banco que garante esse comportamento é a integridade referencial, implementada por meio de uma restrição de chave estrangeira

## Pergunta Discursiva 5: Análise das consultas relacionais e vantagens de normalizar dados em tabelas separadas (autores e livros) em vez de duplicar textos.
  ### Resposta:
  A principal vantagem de dividir os dados em duas tabelas relacionadas é evitar a repetição desnecessária de informações. Em vez de armazenar o nome e o país do autor em cada registro de livro, essas informações ficam cadastradas apenas uma vez na tabela autores, enquanto a tabela livros utiliza o campo "autor_id" para identificar a qual autor cada obra pertence. Dessa forma, essa divisão reduz a duplicação de dados, economiza espaço de armazenamento, facilita atualizações e evita inconsistências. Por exemplo, se o nome de um autor precisar ser alterado, basta modificar seu cadastro na tabela autores, sem precisar atualizar todos os seus livros. Além disso, o relacionamento por chave estrangeira garante a integridade dos dados, impedindo que sejam cadastrados livros associados a autores inexistentes.

# 3 - Perguntas Conceituais:

## Questão a: Por que uma aplicação comercial nunca deve se conectar ao banco de dados utilizando o usuário root? O que pode ocorrer com o servidor de banco de dados caso as credenciais do usuário da aplicação sejam vazadas?
  ### Resposta:
  Pois o "root" possui privilégios administrativos amplos, permitindo acessar, modificar ou excluir praticamente todos os dados. O ideal é utilizar um usuário específico, com permissões limitadas às operações necessárias para a aplicação. Caso suas credenciais sejam vazadas, uma pessoa mal-intencionada poderá acessar informações confidenciais, alterar ou excluir registros, dependendo dos privilégios concedidos. Por isso, utilizar o princípio do menor privilégio é fundamental para garantir a segurança e a integridade das informações.

## Questão b: Qual é a diferença fundamental entre privilégios DDL (Data Definition Language) e DML (Data Manipulation Language)? Por que é uma boa prática de segurança separá-los em contas de usuários distintas?
  ### Resposta:
  Os privilégios DDL permitem criar (CREATE), alterar (ALTER) e excluir (DROP) estruturas do banco de dados, como tabelas e o próprio banco de dados. Já os privilégios DML permitem manipular os dados existentes, realizando operações como inserir (INSERT), consultar (SELECT), atualizar (UPDATE) e excluir (DELETE) registros. Separar esses privilégios em contas de usuários distintas é uma boa prática de segurança porque limita o acesso de cada usuário às suas necessidades. Assim, um usuário responsável por inserir e consultar dados não poderá modificar a estrutura do banco, reduzindo o risco de alterações indevidas, perda de informações e problemas de segurança.

## Questão c: Por que o arquivo .env.example deve ser commitado no repositório de código enquanto o arquivo .env nunca deve ser versionado? Quais são os riscos e consequências práticas de comitar credenciais reais em um repositório público no GitHub?
  ### Resposta:
  O arquivo ".env.example" deve ser enviado ao repositório porque serve como modelo, mostrando quais variáveis de ambiente são necessárias para configurar o projeto, sem expor informações confidenciais. Já o arquivo ".env" não deve ser enviado, pois contém dados sensíveis, como senhas e usuários. Caso essas informações sejam publicadas em um repositório público no GitHub, pessoas aleátorias poderão utilizá-las para acessar o banco de dados, roubar informações, modificar ou excluir registros e comprometer a segurança do sistema. Mesmo que o arquivo seja removido posteriormente, as informações confidenciais podem continuar disponíveis no histórico do Git.

## Questão d: O uso do arquivo .env e a inclusão no .gitignore eliminam por completo todos os riscos de segurança de credenciais em um ambiente de desenvolvimento e produção? Justifique sua resposta considerando que o arquivo permanece armazenado em texto puro no sistema de arquivos do servidor.
  ### Resposta:
  Não. Pois, o uso do arquivo ".env" e sua inclusão no ".gitignore" não eliminam completamente os riscos de segurança, apenas ajudam a evitar que as credenciais sejam enviadas acidentalmente para o repositório Git. Como o arquivo ".env" permanece armazenado em texto puro no sistema de arquivos do servidor, pessoas que conseguirem acesso indevido à máquina poderão visualizar as senhas e utilizar essas informações para acessar o banco de dados. Por isso, é importante restringir as permissões de acesso ao arquivo e utilizar senhas fortes para proteger o servidor.

## Questão e: O que é um contêiner e quais são as principais vantagens de utilizar o Docker para provisionar ambientes de banco de dados em atividades didáticas de graduação em comparação com a instalação manual do SGBD diretamente no sistema operacional do computador do aluno?
  ### Resposta:
  Um contêiner é um ambiente isolado que reúne uma aplicação e suas dependências, permitindo que ela seja executada de maneira padronizada em diferentes computadores. O Docker facilita a criação e o gerenciamento desses ambientes, oferecendo vantagens como facilidade de instalação, isolamento dos serviços, rapidez na configuração e possibilidade de utilizar diferentes versões de um SGBD sem interferir diretamente no sistema operacional. Em atividades didáticas de graduação, isso permite que todos os alunos utilizem ambientes semelhantes, reduzindo problemas de compatibilidade e diferenças de configuração. Além disso, os contêineres podem ser facilmente removidos, recriados e compartilhados, tornando os testes e experimentos mais práticos e evitando a necessidade de instalar e configurar manualmente o banco de dados no computador de cada aluno.

# Desafios Práticos:
## (A) 1 - Alteração de porta do SGBD: Altere a variável MARIADB_PORT no .env para a porta 3307. Reinicie o serviço e explique como você reconfigurou a conexão do CloudBeaver para acessar o banco na porta alterada.
  ### Resposta:
  Fui no arquivo .env e mudei o valor da variável "MARIADB_PORT" de "4444" para "3307". Para reiniciar os serviços, usei o comando "docker compose down" e o comando "docker compose up -d".
  Depois acessei o "localhost:8978" para acessar o CloudBeaver, passei pelo setup inicial e me conectei ao banco do mariadb pela porta 3306 usando o usuário "root" e host "mariadb". Quando fiz a conexão, os dados criados previamente continuaram salvos

  ## (A) 2 - Dois ambientes simultâneos: Configure duas pastas distintas no seu computador com arquivos docker-compose.yml e portas/volumes desacoplados. Explique como você garantiu que quatro contêineres rodassem em paralelo sem conflito de portas ou nomes.
  ### Resposta:
  Dupliquei a pasta "Pedro1349" contendo os arquivo: "docker-compose.yml" e ".env". Depois troquei os nomes dos containers e dos volumes para "lab-mariadb2" e "lab-cloudbeaver2", fui no arquivo ".env" da pasta nova e troquei as ports para "MARIADB_PORT=4444" e "CLOUDBEAVER_PORT=8979".
  Por fim, rodei o "docker compose up" e "docker ps" para verificar se as 4 instâncias estão rodando ao mesmo tempo

  ## (A) 3 - Persistência do volume e alteração de senha de root: Altere o valor de MARIADB_ROOT_PASSWORD no arquivo .env para uma nova senha qualquer. Execute docker compose up -d e observe que a autenticação antiga continua válida enquanto a nova falha. Explique detalhadamente por que isso ocorre e quais são os dois caminhos possíveis para aplicar uma nova senha de root.
  ### Resposta:
  A senha configurada no arquivo ".env" foi alterada para "teste0123". Reinicei os serviços usando o comando "docker compose down" e o comando "docker compose up -d". Então, observei que de fato a senha antiga continuava funcionando e a nova senha ainda não permitia a autenticação.

  Isso acontece porque o MariaDB utiliza um volume persistente (mariadb_data) para armazenar seus dados, incluindo as informações de autenticação do usuário root. Quando a variável "MARIADB_ROOT_PASSWORD" é alterada no arquivo ".env", a nova senha não é aplicada, pois o banco já foi inicializado anteriormente e mantém os dados antigos no volume.

  Existem dois caminhos para resolver isso:
  1 - Alterar a senha diretamente no MariaDB e preservar os dados existentes: utiliza-se o comando "ALTER USER 'root'@'%' IDENTIFIED BY 'NovaSenha'".
  2 - Remover o volume persistente, recriar o container, mas não preservar os dados existentes: isso faz com que o MariaDB seja inicializado novamente com a nova senha definida no ".env"

  ## (A) 4 - Comportamento da validação estrita (:?): Apague temporariamente o arquivo .env (ou comente a linha da senha de root) e execute docker compose up -d. Documente a mensagem de erro emitida pelo Compose e explique discursivamente a importância do modificador :? em ambientes profissionais.
  ### Resposta:
  Apareceu o seguinte erro: "error while interpolating services.mariadb.environment.MARIADB_ROOT_PASSWORD: required variable MARIADB_ROOT_PASSWORD is missing a value: defina MARIADB_ROOT_PASSWORD no arquivo .env"
  Esse erro aconteceu pois o ":?" utilizado no arquivo "docker-compose.yml" exige que a variável esteja definida e não esteja vazia. Sua importância em ambientes profissionais é garantir que configurações essenciais, como senhas, sejam fornecidas antes da inicialização dos serviços, evitando falhas de configuração, acessos indevidos e problemas de segurança.

  ## (A) 5 - Inspeção de variáveis no compose: Execute docker compose config no terminal e liste três variáveis de ambiente que foram resolvidas e interpoladas a partir do .env.
  ### Resposta:
  utilizei o comando "docker compose config" e essas são as 3 variáveis que escolhi:
  1 - "MARIADB_DATABASE: labdb"
  2 - "mariadb: ports: published: 3307"
  3 - "cloudbeaver: ports: published: "8978"


  ## (B) 6 - Criação da tabela de empréstimos: Escreva o comando DDL para criar a tabela emprestimos contendo os campos id (INT AUTO_INCREMENT PRIMARY KEY), livro_id (INT), data_emprestimo (DATE) e devolvido (BOOLEAN), com restrição de chave estrangeira referenciando livros(id).
  ### Resposta:
  ```sql
    CREATE TABLE IF NOT EXISTS emprestimos (
      id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
      livro_id int UNSIGNED,
      data_emprestimo DATE NOT NULL,
      devolvido boolean,
      FOREIGN KEY (livro_id) REFERENCES livros(id)
    );
  ```

  ## (B) 7 - Carga da tabela empréstimos: Escreva as instruções INSERT para cadastrar três registros de empréstimos, sendo dois com status não devolvido (FALSE ou 0) e um devolvido (TRUE ou 1).
  ### Resposta:
  ```sql
  USE biblioteca;

  INSERT INTO emprestimos (livro_id, data_emprestimo, devolvido) VALUES
  (1, '2026-11-01', TRUE),
  (2, '2026-11-02', FALSE),
  (5, '2026-11-03', FALSE);

  ```


  ## (B) 8 - Consulta de pendências: Escreva uma consulta que liste todos os empréstimos pendentes (não devolvidos), trazendo o título do livro, a data de empréstimo e o nome do autor do livro.
  ### Resposta:
  ```sql
  SELECT l.titulo, e.data_emprestimo, a.nome AS autor FROM emprestimos e
  INNER JOIN livros l ON e.livro_id = l.id
  INNER JOIN autores a ON l.autor_id = a.id
  WHERE e.devolvido = FALSE;
  ```


  ## (B) 9 - Filtragem de grupos com HAVING: Escreva uma consulta que agrupe os livros por autor e retorne a contagem total de obras de cada um, filtrando exclusivamente autores que possuem mais de 1 livro cadastrado (HAVING COUNT(*) > 1).
  ### Resposta:
  ```sql
  SELECT a.nome AS autor, COUNT(l.id) AS total_livros FROM autores a
  INNER JOIN livros l ON a.id = l.autor_id
  GROUP BY a.id, a.nome
  HAVING COUNT(*) > 1
  ORDER BY total_livros DESC;
  ```

  ## (B) 10 - Atualização proporcional (UPDATE): Execute uma instrução DML para reajustar o preço de um livro específico em 10% de acréscimo. Transcreva a consulta UPDATE utilizada e comente o resultado.
  ### Resposta:
  ```sql
  UPDATE livros
  SET preco = preco + preco/2
  WHERE id = 2;
  ```
  Comentários: o preco do livro "A Hora da Estrela" (id = 3) saiu de 32.5 para 35.75
  Código usado para conferir o resultado:
  ```sql
  SELECT id, titulo, preco
  FROM livros
  WHERE id = 3;
  ```


  ## (B) 11 - Remoção condicional (DELETE): Cadastre um novo autor sem nenhum livro associado e, em seguida, execute a instrução DELETE para removê-lo da tabela autores. Explique por que essa remoção foi aceita sem violar a restrição de chave estrangeira.
  ### Resposta:
  Código usado para criar o autor:
  ```sql
  INSERT INTO autores (nome, pais, ano_nascimento)
  VALUES ('Autor Temporário', 'Brasil', 1990);
  ```
  Código usado para excluir o autor
  ```sql
  DELETE FROM autores
  WHERE nome = 'Autor Temporário';
  ```
  Comentários: A restrição de chave estrangeira impede que um autor seja excluído quando existem livros associados a ele. Como não havia nenhum relacionamento dependente desse autor, o banco de dados permitiu a exclusão sem violar a regra de integridade referencial.


  ## (C) 12 - Criação de usuário restrito para relatórios: Crie um usuário chamado relatorios com senha Relatorios2026!, concedendo privilégio de SELECT exclusivamente sobre a tabela livros do banco biblioteca.
  ### Resposta:
  Para criar o usuário, eu usei o seguinte comando sql como usuário root:
  ```sql
  CREATE USER 'relatorios'@'%' IDENTIFIED BY 'Relatorios2026!';
  ```
  Para garantir os privilégios, eu usei o seguinte comando sql como usuário root:

  ```sql
  GRANT SELECT ON biblioteca.livros TO 'relatorios'@'%';
  ```

  ## (C) 13 - Teste de restrição de visibilidade: Conecte-se com o usuário relatorios, tente consultar a tabela autores e transcreva a mensagem de erro emitida pelo SGBD, explicando o motivo do bloqueio.
  ### Resposta:
  Tentei executar o seguinte comando sql:
  ```sql
  SELECT * from autores;
  ```
  Apareceu o seguinte erro:
  "Error executing query: SQL Error [1142] [42000]: (conn=7) SELECT command denied to user 'relatorios'@'172.18.0.3' for table `biblioteca`.`autores`"
  Explicação do erro: esse erro ocorreu porque o usuário "relatorios" não tem o privilégio de consultar a tabela "autores" do banco de dados, por isso que o erro diz que o comando "SELECT" foi negado para o usuário. Esse usuário só tem permissão de fazer a consulta da tabela "livros" do banco de dados

  ## (C) 14 - Concessão e revogação dinâmica de privilégios: Conectado como root, conceda privilégio de INSERT na tabela livros para o usuário relatorios. Realize uma inserção de teste com sucesso e, em seguida, revogue o privilégio via REVOKE. Descreva discursivamente o resultado de tentar inserir novamente após a revogação.
  ### Resposta:
  Usei o seguinte comando sql como usuário root para garantir o privilégio de INSERT para o usuário "relatorios":
  ```sql
  GRANT INSERT ON biblioteca.livros TO 'relatorios'@'%';
  ```

  Usei o seguinte comando sql como usuário "relatorios" para inserir um novo livro:
  ```sql
  INSERT INTO livros (titulo, ano_publicacao, preco, autor_id) VALUES
  ('O futuro chegou :o', 2058, 100, 1);
  ```

  Usei o seguinte comando sql como usuário root para tirar o privilégio de INSERT para o usuário "relatorios":
  ```sql
  REVOKE INSERT ON biblioteca.livros FROM 'relatorios'@'%';
  ```

  Usei o seguinte comando sql como usuário "relatorios" para tentar inserir um novo livro:
  ```sql
  INSERT INTO livros (titulo, ano_publicacao, preco, autor_id) VALUES
  ('O futuro chegou :o 2', 2059, 150, 1);
  ```

  Apareceu o seguinte erro quando tentei executar o comando: "Error executing query: SQL Error [1142] [42000]: (conn=7) INSERT command denied to user 'relatorios'@'172.18.0.3' for table `biblioteca`.`livros`".
  Explicação do erro: esse erro ocorreu porque o usuário "relatorios" não tem mais o privilégio de inserir registros na tabela "livros" do banco de dados, por isso que o erro diz que o comando "INSERT" foi negado para o usuário. Esse usuário só tem permissão de fazer a consulta da tabela "livros" do banco de dados

  ## (C) 15 - Script idempotente de automação (setup.sql): Desenvolva um script SQL completo chamado setup.sql que recrie do zero todo o banco de dados biblioteca, suas tabelas, restrições, usuários (app_biblioteca, consulta) com privilégios e a carga de dados. Versiona esse arquivo no seu repositório pessoal no GitHub.
  ### Resposta:
  Crei o arquivo setup.sql, está dentro da pasta "Arquivos". Essa pasta está no repositório: [BD_UFRN_Tarefa03](https://github.com/Pedro1349/BD_UFRN_Tarefa03)
