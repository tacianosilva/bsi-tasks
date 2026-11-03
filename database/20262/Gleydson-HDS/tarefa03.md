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

---

### **4. DESAFIOS PRÁTICOS**

**DESAFIO 01 - Alteração de porta do SGBD: Altere a variável MARIADB_PORT no .env para a porta 3307. Reinicie o serviço e explique como você reconfigurou a conexão do CloudBeaver para acessar o banco na porta alterada.**

    A variável MARIADB_PORT do arquivo .env foi alterada de 3306 para 3307. Em seguida, a configuração do 
    Docker Compose foi validada e os contêineres foram recriados para aplicar o novo mapeamento de portas.

    Comandos utilizados:

    powershell
    docker compose config --quiet
    docker compose up -d --force-recreate
    docker ps
    docker port lab-mariadb
   
    A conexão do CloudBeaver com o MariaDB permaneceu configurada com o host mariadb e a porta interna 3306. 
    Isso ocorre porque os dois serviços se comunicam pela rede virtual do Docker, utilizando a porta interna do 
    serviço.
    
    Para conexões originadas diretamente no Windows, fora da rede Docker, a configuração passa a utilizar o host 
    localhost e a porta 3307.
    
    A alteração da porta publicada permite acessar o MariaDB pela porta 3307 do computador hospedeiro sem 
    modificar a porta interna do serviço. A configuração separa o acesso externo da comunicação entre os 
    contêineres.    

---

**DESAFIO 02 — Dois ambientes simultâneos: Configure duas pastas distintas no seu computador com arquivos docker-compose.yml e portas/volumes desacoplados. Explique como você garantiu que quatro contêineres rodassem em paralelo sem conflito de portas ou nomes.**

    Foram configurados dois ambientes independentes utilizando Docker Compose, nas pastas tarefa03 e 
    novo_ambiente.

    Cada ambiente possui dois contêineres: um MariaDB e um CloudBeaver. Para evitar conflitos, foram utilizados 
    nomes, portas e volumes distintos.

    O ambiente original utiliza as portas 3307 (MariaDB) e 8978 (CloudBeaver), enquanto o segundo utiliza 3308 
    (MariaDB) e 8979 (CloudBeaver).

    A execução foi validada com o comando docker ps, que confirmou os quatro contêineres em funcionamento 
    simultaneamente, sem conflitos de portas ou nomes.

Evidência:

    PS C:\Users\Cliente\Documents\Faculdade\Banco de Dados\dct2201-banco-de-dados\novo_ambiente> docker ps
    CONTAINER ID   IMAGE                        COMMAND                  CREATED              STATUS              
    PORTS                                         NAMES
    bb9f9d7516af   dbeaver/cloudbeaver:latest   "./launch-product.sh"    About a minute ago   Up About a minute   
    0.0.0.0:8979->8978/tcp, [::]:8979->8978/tcp   novo_ambiente-cloudbeaver
    479f996c6101   mariadb:11                   "docker-entrypoint.s…"   About a minute ago   Up About a minute   
    0.0.0.0:3308->3306/tcp, [::]:3308->3306/tcp   novo_ambiente-mariadb
    e89b3b5593ea   dbeaver/cloudbeaver:latest   "./launch-product.sh"    About an hour ago    Up About an hour    
    0.0.0.0:8978->8978/tcp, [::]:8978->8978/tcp   lab-cloudbeaver
    7f3045547f38   mariadb:11                   "docker-entrypoint.s…"   About an hour ago    Up About an hour    
    0.0.0.0:3307->3306/tcp, [::]:3307->3306/tcp   lab-mariadb

---

**DESAFIO 03  — Persistência do volume e alteração de senha: Altere o valor de MARIADB_ROOT_PASSWORD no arquivo .env para uma nova senha qualquer. Execute docker compose up -d e observe que a autenticação antiga continua válida enquanto a nova falha. Explique detalhadamente por que isso ocorre e quais são os dois caminhos possíveis para aplicar uma nova senha de root.**

    Inicialmente, foi alterado o valor da variável MARIADB_ROOT_PASSWORD no arquivo .env e executado o comando 
    docker compose up -d. Entretanto, a autenticação com a nova senha falhou, enquanto a senha antiga continuou 
    funcionando.

    Isso ocorre porque, na primeira inicialização, o MariaDB utiliza a variável de ambiente para criar o usuário 
    root e definir sua senha. Essas informações ficam armazenadas no volume persistente associado ao diretório /
    var/lib/mysql. Nas inicializações seguintes, o banco identifica que já existe uma estrutura de dados e não 
    executa novamente a configuração inicial.

    Para aplicar a nova senha sem perder os dados, foi utilizado o comando ALTER USER diretamente no MariaDB. 
    Após a alteração, a autenticação com a nova senha foi testada com sucesso.
    
    Por fim, foram realizadas consultas para verificar a quantidade de registros, confirmando que os 14 autores e 
    os 36 livros continuavam armazenados no banco de dados.
    
    Conclui-se que a persistência dos volumes permite preservar os dados mesmo após alterações e recriações de 
    contêineres. Também foi possível observar que as variáveis de ambiente utilizadas na inicialização nã0 
    substituem a administração direta das credenciais de um banco já existente.

Evidência: 

    PS C:\Users\Cliente\Documents\Faculdade\Banco de Dados\dct2201-banco-de-dados\tarefa03> docker exec -it lab-
    mariadb mariadb -u root -p
    Enter password:
    Welcome to the MariaDB monitor.  Commands end with ; or \g.
    Your MariaDB connection id is 16
    Server version: 11.8.9-MariaDB-ubu2404 mariadb.org binary distribution
    
    Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.
    
    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
    
    MariaDB [(none)]>

---

**DESAFIO 04 - Comportamento da validação estrita (:?): Apague temporariamente o arquivo .env (ou comente a linha da senha de root) e execute docker compose up -d. Documente a mensagem de erro emitida pelo Compose e explique discursivamente a importância do modificador :? em ambientes profissionais.**

    Foi realizado um teste removendo temporariamente o arquivo .env e executando o comando docker compose up -d.
 
    Como a variável MARIADB_ROOT_PASSWORD não estava definida, o Docker Compose interrompeu a validação da 
    configuração e apresentou uma mensagem informando que a variável era obrigatória, conforme a regra 
    ${MARIADB_ROOT_PASSWORD:?mensagem} definida no arquivo docker-compose.yml.
    
    O modificador :? é importante em ambientes profissionais porque impede que serviços sejam iniciados sem 
    configurações essenciais. Isso reduz erros de implantação, facilita o diagnóstico de problemas e aumenta a 
    confiabilidade do ambiente.
    
    Após o teste, o arquivo .env foi restaurado, preservando as configurações originais.

Evidência:

    PS C:\Users\Cliente> cd "C:\Users\Cliente\Documents\Faculdade\Banco de Dados\dct2201-banco-de-dados\tarefa03"
    PS C:\Users\Cliente\Documents\Faculdade\Banco de Dados\dct2201-banco-de-dados\tarefa03> Copy-Item .env 
    .env.backup
    PS C:\Users\Cliente\Documents\Faculdade\Banco de Dados\dct2201-banco-de-dados\tarefa03> Rename-Item .env 
    .env.temp
    PS C:\Users\Cliente\Documents\Faculdade\Banco de Dados\dct2201-banco-de-dados\tarefa03> docker compose up -d
    error while interpolating services.mariadb.environment.MARIADB_ROOT_PASSWORD: required variable 
    MARIADB_ROOT_PASSWORD is missing a value: defina MARIADB_ROOT_PASSWORD no arquivo .env

    What's next:
        Debug this Compose error with Gordon → docker ai "help me fix this compose error"

---

**DESAFIO 05 - Inspeção de variáveis no compose: Execute docker compose config no terminal e liste três variáveis de ambiente que foram resolvidas e interpoladas a partir do .env.**

    Foi executado o comando docker compose config para visualizar a configuração final do ambiente Docker após a 
    interpolação das variáveis definidas no arquivo .env.
    
    Foram identificadas três variáveis:

    MARIADB_ROOT_PASSWORD: define a senha do usuário root do MariaDB.

    MARIADB_DATABASE: define o banco de dados inicial.

    MARIADB_PORT: define a porta externa utilizada para acessar o serviço MariaDB.

    O comando permite verificar se as variáveis foram corretamente interpretadas pelo Docker Compose antes da 
    inicialização dos serviços, facilitando a identificação de erros de configuração.

Evidência:

    PS C:\Users\Cliente\Documents\Faculdade\Banco de Dados\dct2201-banco-de-dados\tarefa03> docker compose config
    name: tarefa03
    services:
      cloudbeaver:
        container_name: lab-cloudbeaver
        image: dbeaver/cloudbeaver:latest
        networks:
          default: null
        depends_on:
          mariadb:
            condition: service_started
            required: true
        ports:
          - mode: ingress
            target: 8978
            published: "8978"
            protocol: tcp
      mariadb:
        container_name: lab-mariadb
        environment:
          MARIADB_DATABASE: labdb
          MARIADB_ROOT_PASSWORD: NewRootLab2026!aB
        image: mariadb:11
        networks:
          default: null
        volumes:
          - type: volume
            source: mariadb_data
            target: /var/lib/mysql
            volume: {}
        ports:
          - mode: ingress
            target: 3306
            published: "3307"
            protocol: tcp
    networks:
      default:
        name: tarefa03_default
    volumes:
      mariadb_data:
        name: tarefa03_mariadb_data

--- 

**DESAFIO 06 - Criação da tabela de empréstimos: Escreva o comando DDL para criar a tabela emprestimos contendo os campos id (INT AUTO_INCREMENT PRIMARY KEY), livro_id (INT), data_emprestimo (DATE) e devolvido (BOOLEAN), com restrição de chave estrangeira referenciando livros(id).**

    Foi criada a tabela emprestimos no banco de dados biblioteca, utilizando o comando DDL CREATE TABLE.

    A tabela possui os campos id, livro_id, data_emprestimo e devolvido. O campo id foi definido como chave 
    primária com incremento automático (AUTO_INCREMENT), enquanto livro_id foi definido como chave estrangeira, 
    referenciando o campo id da tabela livros.

    Essa estrutura permite registrar os empréstimos de livros, armazenar suas respectivas datas e identificar se 
    cada empréstimo já foi devolvido.

Evidências:

    CREATE TABLE emprestimos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        livro_id INT,
        data_emprestimo DATE,
        devolvido BOOLEAN,
        FOREIGN KEY (livro_id) REFERENCES livros(id)
    );

    Verificação da estrutura:
    
    DESCRIBE emprestimos;
    
    Verificação das restrições e chaves:
    
    SHOW CREATE TABLE emprestimos;

---

**DESAFIO 07 - Carga da tabela empréstimos: Escreva as instruções INSERT para cadastrar três registros de empréstimos, sendo dois com status não devolvido (FALSE ou 0) e um devolvido (TRUE ou 1).**

    Foram inseridos três registros na tabela emprestimos, utilizando o comando SQL INSERT INTO.

    Os registros foram configurados com diferentes situações: dois empréstimos com status FALSE (não devolvidos) 
    e um com status TRUE (devolvido).

    Após a inserção, foi executada uma consulta com SELECT * FROM emprestimos para verificar os registros 
    cadastrados.

Evidências — Sequência de comandos SQL

    Inserção dos registros:

    INSERT INTO emprestimos (livro_id, data_emprestimo, devolvido)
    VALUES
        (1, '2026-10-20', FALSE),
        (2, '2026-10-22', FALSE),
        (3, '2026-10-25', TRUE);

    Verificação dos registros:

    SELECT * FROM emprestimos;

---

**DESAFIO 08 - Consulta de pendências: Escreva uma consulta que liste todos os empréstimos pendentes (não devolvidos), trazendo o título do livro, a data de empréstimo e o nome do autor do livro.**
    
    Foi desenvolvida uma consulta SQL utilizando INNER JOIN para relacionar as tabelas emprestimos, livros e 
    autores.
    
    A consulta retorna o título do livro, a data do empréstimo e o nome do respectivo autor, utilizando a 
    condição WHERE e.devolvido = FALSE para exibir somente os empréstimos que ainda não foram devolvidos.  

Evidências — Sequência de comandos SQL

    Consulta dos empréstimos pendentes:
    
    SELECT
        l.titulo AS livro,
        e.data_emprestimo,
        a.nome AS autor
    FROM emprestimos e
    INNER JOIN livros l ON e.livro_id = l.id
    INNER JOIN autores a ON l.autor_id = a.id
    WHERE e.devolvido = FALSE;
    
    A consulta permite identificar os empréstimos que ainda estão pendentes e seus respectivos livros e autores.

---

**DESAFIO 09 - Filtragem de grupos com HAVING: Escreva uma consulta que agrupe os livros por autor e retorne a contagem total de obras de cada um, filtrando exclusivamente autores que possuem mais de 1 livro cadastrado (HAVING COUNT(*) > 1).**
    
    Foi desenvolvida uma consulta SQL utilizando INNER JOIN para relacionar as tabelas autores e livros, 
    agrupando os registros por autor com GROUP BY.
    
    A função COUNT(*) foi utilizada para contabilizar a quantidade de livros cadastrados para cada autor. Em 
    seguida, foi aplicada a cláusula HAVING COUNT(*) > 1 para retornar exclusivamente os autores que possuem mais 
    de uma obra cadastrada.

Evidências — Sequência de comandos SQL

    Consulta de livros por autor:
    
    SELECT
        a.nome AS autor,
        COUNT(*) AS total_livros
    FROM autores a
    INNER JOIN livros l ON a.id = l.autor_id
    GROUP BY a.id, a.nome
    HAVING COUNT(*) > 1;
    
    A consulta permite identificar os autores com maior quantidade de livros cadastrados, demonstrando a 
    utilização de agrupamento e filtragem com HAVING.

---

**DESAFIO 10 - Atualização proporcional (UPDATE): Execute uma instrução DML para reajustar o preço de um livro específico em 10% de acréscimo. Transcreva a consulta UPDATE utilizada e comente o resultado.**
Foi realizada uma atualização na tabela livros utilizando o comando SQL UPDATE, com o objetivo de reajustar o preço de um livro específico em 10%.

    A operação foi feita por meio da multiplicação do preço atual por 1.10, aplicando o acréscimo de 10%. A cláusula WHERE foi utilizada para garantir que somente o livro selecionado fosse atualizado.

Evidências — Sequência de comandos SQL

    Atualização do preço:
    
    UPDATE livros
    SET preco = preco * 1.10
    WHERE id = 1;
    
    Verificação do resultado:
    
    SELECT id, titulo, preco
    FROM livros
    WHERE id = 1;
    
    O resultado permite verificar o novo preço do livro após o reajuste. A utilização da cláusula WHERE evita que os preços dos demais livros sejam alterados.

---

**DESAFIO 11 - Remoção condicional (DELETE): Cadastre um novo autor sem nenhum livro associado e, em seguida, execute a instrução DELETE para removê-lo da tabela autores. Explique por que essa remoção foi aceita sem violar a restrição de chave estrangeira.**

    Foi cadastrado um novo autor na tabela autores, sem associação com nenhum livro da tabela livros. Em seguida, foi executado o comando DELETE para remover esse registro.
    
    A remoção foi aceita porque nenhum livro possuía uma chave estrangeira (autor_id) referenciando o identificador do autor excluído. Dessa forma, a operação não violou a restrição de integridade referencial.
    
Evidências — Sequência de comandos SQL
    
    Cadastro do autor:
    
    INSERT INTO autores (nome, pais, ano_nascimento)
    VALUES ('Autor Temporario', 'Brasil', 1990);
    
    Verificação do cadastro:
    
    SELECT *
    FROM autores
    WHERE nome = 'Autor Temporario';
    
    Remoção do autor:
    
    DELETE FROM autores
    WHERE nome = 'Autor Temporario';
    
    Confirmação da remoção:
    
    SELECT *
    FROM autores
    WHERE nome = 'Autor Temporario';
    
    A última consulta permite confirmar que o autor não permanece cadastrado na tabela.

---

**DESAFIO 12 - Criação de usuário restrito para relatórios: Crie um usuário chamado relatorios com senha Relatorios2026!, concedendo privilégio de SELECT exclusivamente sobre a tabela livros do banco biblioteca.**

    Foi criado o usuário relatorios no MariaDB, com uma senha específica e acesso restrito à tabela livros do banco de dados biblioteca.
    
    Foi concedido exclusivamente o privilégio SELECT, permitindo consultar os registros da tabela autorizada, sem permissão de leitura nas demais tabelas. Essa configuração segue o princípio do menor privilégio, limitando o acesso do usuário às operações necessárias.

Evidências — Sequência de comandos SQL

    Criação do usuário:
    
    CREATE USER 'relatorios'@'%' IDENTIFIED BY 'Relatorios2026!';
    
    Concessão do privilégio de leitura:
    
    GRANT SELECT ON biblioteca.livros TO 'relatorios'@'%';
    
    Verificação das permissões:
    
    SHOW GRANTS FOR 'relatorios'@'%';
    
    Teste de consulta na tabela autorizada:
    
    SELECT * FROM biblioteca.livros;
    
    Teste de acesso à tabela não autorizada:
    
    SELECT * FROM biblioteca.autores;

**DESAFIO 13 - Teste de restrição de visibilidade: Conecte-se com o usuário relatorios, tente consultar a tabela autores e transcreva a mensagem de erro emitida pelo SGBD, explicando o motivo do bloqueio.**

    Foi realizado um teste de acesso utilizando o usuário relatorios, com o objetivo de verificar se as permissões concedidas anteriormente estavam funcionando corretamente.
    
    Após conectar-se com o usuário, foi executada uma consulta à tabela autores. Como esse usuário possui exclusivamente o privilégio SELECT sobre a tabela livros, o MariaDB bloqueou a operação.

Evidências — Sequência de comandos

    Conexão com o usuário restrito:

    docker exec -it lab-mariadb mariadb -u relatorios -p

    Tentativa de consulta à tabela não autorizada:

    USE biblioteca;

    SELECT * FROM autores;

    Mensagem de erro do SGBD:

    ERROR 1142 (42000): SELECT command denied to user 'relatorios'@'localhost' for table 'autores'

Comentário do resultado

    O erro 1142 indica que o comando SELECT foi negado por falta de permissão. Isso ocorre porque o usuário relatorios não recebeu autorização para consultar a tabela autores, tendo acesso de leitura somente à tabela livros.
    
    Esse comportamento demonstra o funcionamento do controle de privilégios do MariaDB e a aplicação do princípio do menor privilégio.

---

**DESAFIO 14 - Concessão e revogação dinâmica de privilégios: Conectado como root, conceda privilégio de INSERT na tabela livros para o usuário relatorios. Realize uma inserção de teste com sucesso e, em seguida, revogue o privilégio via REVOKE. Descreva discursivamente o resultado de tentar inserir novamente após a revogação.**

    Foi concedido temporariamente ao usuário relatorios o privilégio INSERT sobre a tabela livros do banco de dados biblioteca.
    
    Inicialmente, o usuário conseguiu inserir um novo registro na tabela, demonstrando que a permissão havia sido concedida corretamente. Em seguida, o privilégio foi revogado utilizando o comando REVOKE.
    
    Após a revogação, uma nova tentativa de inserção foi bloqueada pelo MariaDB, pois o usuário não possuía mais autorização para executar operações INSERT. O privilégio SELECT permaneceu ativo, permitindo apenas a consulta dos registros.
    
 Eidências — Sequência de comandos SQL
    
        Concessão do privilégio:
    
    GRANT INSERT ON biblioteca.livros TO 'relatorios'@'%';
    
        Inserção de teste:
    
    INSERT INTO biblioteca.livros
    (titulo, ano_publicacao, preco, autor_id)
    VALUES
    ('Livro de Teste', 2026, 35.90, 1);
    
        Revogação do privilégio:
    
    REVOKE INSERT ON biblioteca.livros FROM 'relatorios'@'%';
    
        Verificação das permissões restantes:
    
    SHOW GRANTS FOR 'relatorios'@'%';
    
        Nova tentativa de inserção após a revogação:
    
    INSERT INTO biblioteca.livros
    (titulo, ano_publicacao, preco, autor_id)
    VALUES
    ('Segundo Livro de Teste', 2026, 29.90, 1);
    
    Após a revogação, a tentativa de inserção retorna o erro ERROR 1142, indicando que o comando INSERT foi negado por falta de permissão. Isso demonstra que os privilégios de usuários podem ser concedidos e revogados dinamicamente, sem a necessidade de excluir ou recriar a conta.

---

**DESAFIO 15 - Script idempotente de automação (setup.sql): Desenvolva um script SQL completo chamado setup.sql que recrie do zero todo o banco de dados biblioteca, suas tabelas, restrições, usuários (app_biblioteca, consulta) com privilégios e a carga de dados. Versiona esse arquivo no seu repositório pessoal no GitHub.**

    Foi desenvolvido o arquivo setup.sql para automatizar a criação do banco de dados biblioteca. O script realiza a exclusão e recriação do banco, cria as tabelas autores, livros e emprestimos, define as chaves primárias e estrangeiras e insere os dados iniciais.
    
    Também foram criados os usuários app_biblioteca e consulta, com permissões específicas: o primeiro possui privilégios de consulta, inserção, atualização e exclusão de registros, enquanto o segundo possui apenas permissão de leitura.
    
    Ao final, foram incluídas consultas para verificar a quantidade de registros nas tabelas e os privilégios dos usuários.
