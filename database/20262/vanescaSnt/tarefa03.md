# Tarefa 03 - Docker Compose, MariaDB e Administração de SGBD

## 1. Identificação e Repositório

- **Nome completo:** Vanesca Héllen dos Santos Silva
- **Usuário no GitHub:** [vanescaSnt]
- **E-mail acadêmico:** [vanesca.santos.115@ufrn.edu.br]
- **Repositório pessoal:** [https://github.com/vanescaSnt/dct2201-banco-de-dados.git](https://github.com/vanescaSnt/dct2201-banco-de-dados.git)

O repositório pessoal contém os arquivos de configuração e os scripts da atividade (`docker-compose.yml`, `.env.example`, `.gitignore`, `povoamento.sql` e `setup.sql`), organizados na pasta `tarefa03/` e descritos no `README.md`.

## 2. Respostas às Perguntas Discursivas dos Passos Práticos

### Pergunta Discursiva 1

Os comandos DDL (Data Definition Language) definem a estrutura onde os dados ficam guardados, como o `CREATE DATABASE` e o `CREATE TABLE`, que criam o banco e as tabelas com suas colunas e regras. Já os comandos DML (Data Manipulation Language) trabalham com o conteúdo dessas estruturas, como o `INSERT`, que cadastra novos registros, o `SELECT`, que consulta, o `UPDATE`, que altera, e o `DELETE`, que remove.

Se uma tabela for apagada com o comando DDL `DROP TABLE`, todos os dados que estavam dentro dela são apagados junto com a própria estrutura. A tabela deixa de existir no banco, e os registros só podem ser recuperados se houver um backup. Por isso esse comando é considerado destrutivo e deve ficar restrito a contas de administração.

### Pergunta Discursiva 2

Ao executar o comando `DROP TABLE autores;` conectado com a conta `app_biblioteca`, o MariaDB recusou a instrução e retornou o erro `SQL Error [1142] [42000]: DROP command denied to user 'app_biblioteca'@'[...]' for table 'autores'`. A tabela não foi apagada e todos os dados permaneceram intactos.

O erro 1142 indica que o usuário não tem permissão para executar aquele tipo de comando sobre aquela tabela. Na criação da conta, foram concedidos à `app_biblioteca` apenas os privilégios `SELECT`, `INSERT`, `UPDATE` e `DELETE`, que servem para ler e manipular os dados, e não o privilégio `DROP`, que permite destruir a estrutura da tabela. Como o MariaDB só permite o que foi explicitamente concedido, o comando foi negado. Isso é o princípio do menor privilégio onde cada conta recebe somente o que precisa para cumprir sua função.

Essa restrição protege o banco caso a aplicação web sofra uma invasão ou tenha uma falha de programação. Se um alguém conseguir executar comandos por meio da aplicação ou se um erro de código disparar um comando indevido, ele só conseguirá fazer o que a conta permite, ou seja, mexer nos registros. Não conseguirá apagar tabelas, alterar a estrutura do banco nem criar ou remover usuários, fazendo o dano ficar limitado e a estrutura do banco é preservada.

### Pergunta Discursiva 3

Os usuários foram criados com o host '%' porque, no MariaDB, uma conta é identificada pelo par 'usuario'@'host', e o host define de onde a conexão é aceita. Uma conta criada com `'localhost'` só aceita conexões originadas na própria máquina onde o banco está rodando. Já o curinga '%' aceita conexões vindas de qualquer endereço de rede.

Na arquitetura com Docker, o MariaDB e o CloudBeaver rodam em contêineres distintos, ligados por uma rede virtual interna criada pelo Docker Compose. Quando o CloudBeaver se conecta ao banco, a conexão não vem de localhost, e sim de outro contêiner, com um endereço IP da sub-rede do Docker. Se as contas tivessem sido criadas com 'localhost', o MariaDB trataria essa conexão como vinda de um host não autorizado e recusaria o acesso. Por isso o '%' é necessário para que serviços em contêineres diferentes consigam se autenticar. Como o banco não fica exposto fora da rede do Docker, a não ser pela porta publicada no `docker-compose.yml`, essa abertura continua controlada.

### Pergunta Discursiva 4

Após a execução da carga inicial e do povoamento expandido gerado com IA generativa, a base ficou com **14 autores** e **42 livros** cadastrados, conferidos com os comandos `SELECT COUNT(*) FROM autores;` e `SELECT COUNT(*) FROM livros;`.

Ao tentar inserir um livro com `autor_id` igual a 999, que não corresponde a nenhum autor existente, o MariaDB recusou a operação e retornou o erro `SQL Error [1452] [23000]: Cannot add or update a child row: a foreign key constraint fails`, apontando para a restrição `livros_ibfk_1`. O livro não foi cadastrado e a tabela `livros` permaneceu inalterada.

Quem impede essa ação é a chave estrangeira `FOREIGN KEY (autor_id) REFERENCES autores(id)`, definida na criação da tabela `livros`. Ela garante a integridade referencial: um livro só pode ser cadastrado se o seu `autor_id` pertencer a um autor que já exista na tabela `autores`. Dessa forma, o banco evita registros órfãos, ou seja, livros ligados a autores que não existem.

### Pergunta Discursiva 5

A Consulta 4 usa um `JOIN` para combinar as tabelas `livros` e `autores`, ligando a chave estrangeira `livros.autor_id` à chave primária `autores.id`. Com isso, é possível exibir o título do livro junto com o nome do seu autor e o preço. A Consulta 5 também faz essa ligação e acrescenta o agrupamento por autor (`GROUP BY`), calculando a média de preço das obras de cada escritor com a função `AVG`. As duas consultas só funcionam bem porque os dados estão separados em duas tabelas relacionadas.

A vantagem prática de dividir os dados em `autores` e `livros` é que o nome e o país de cada autor são guardados uma única vez, e os livros apenas apontam para ele pelo identificador. Se esses dados fossem repetidos em cada linha da tabela de livros, um autor com vários livros teria o mesmo texto copiado várias vezes, o que ocuparia mais espaço e abriria espaço para inconsistências, como o mesmo autor aparecer com grafias diferentes ou países diferentes em linhas distintas. Com as tabelas separadas, uma correção no cadastro do autor é feita em um só lugar e vale para todos os seus livros, e as consultas conseguem agrupar e comparar os dados de forma confiável.

## 3. Respostas Dissertativas Conceituais
 
### Questão a
 
Uma aplicação comercial nunca deve se conectar ao banco de dados com o usuário `root` porque essa conta tem poder total sobre o servidor, podendo criar e apagar bancos e tabelas, alterar a estrutura dos dados, criar e remover usuários e conceder privilégios. A aplicação, no entanto, precisa apenas ler e gravar registros em um banco específico. Dar a ela mais poder do que o necessário contraria o princípio do menor privilégio e aumenta o estrago possível em caso de erro ou ataque.
 
Se as credenciais da aplicação forem vazadas, o impacto depende dos privilégios da conta. Com uma conta restrita, como a `app_biblioteca`, quem decidir atacar vai ficar limitado ao banco liberado e às operações de leitura e alteração de registros, o que já é grave, pois ele pode consultar, modificar ou apagar dados, mas o servidor como um todo continua protegido. Se a aplicação usasse o `root`, o atacante teria controle completo do servidor de banco de dados, podendo apagar todos os bancos, acessar dados de outras aplicações, criar contas próprias para manter o acesso e até comprometer outros sistemas hospedados no mesmo servidor.
 
### Questão b
 
A diferença está no que cada grupo de comandos afeta. Os privilégios DDL (Data Definition Language) permitem definir e alterar a estrutura do banco, como criar, modificar e apagar bancos e tabelas (`CREATE`, `ALTER`, `DROP`). Os privilégios DML (Data Manipulation Language) permitem trabalhar com os dados dentro dessas estruturas, ou seja, consultar, inserir, atualizar e remover registros (`SELECT`, `INSERT`, `UPDATE`, `DELETE`).
 
É uma boa prática de segurança separá-los em contas distintas porque o dia a dia de uma aplicação só exige DML, enquanto mudanças de estrutura são raras e feitas por quem administra o banco. Ao dar à aplicação apenas privilégios DML, uma invasão ou falha de programação não consegue destruir tabelas nem alterar o esquema, e o dano fica restrito aos registros. Além disso, a separação facilita o controle e a auditoria, pois fica claro quem pode alterar a estrutura do banco e quem apenas usa os dados.
 
### Questão c
 
O arquivo `.env.example` deve ser commitado porque funciona como um modelo que lista quais variáveis o projeto precisa (senha do root, nome do banco, portas), mas com valores fictícios, sem nenhuma credencial real. Assim, qualquer pessoa que clonar o repositório sabe como montar o seu próprio `.env`, bastando copiar o modelo e preencher os valores. Já o `.env` contém as senhas reais do ambiente e, por isso, nunca deve ser versionado, o que é garantido por sua inclusão no `.gitignore`.
 
Comitar credenciais reais em um repositório público traz riscos sérios, pois qualquer pessoa vai poder ler a senha, e existem robôs que varrem o GitHub em busca de chaves e senhas expostas, muitas vezes em poucos minutos. As consequências incluem acesso indevido ao banco, vazamento ou destruição de dados e uso do servidor por terceiros. Além disso, mesmo que o arquivo seja apagado depois, a senha continua no histórico de commits do Git, e a única solução segura é trocar a credencial imediatamente.
 
### Questão d
 
Não. O uso do `.env` com o `.gitignore` evita que as credenciais sejam enviadas ao repositório, mas não elimina por completo os riscos. O arquivo continua armazenado em texto puro no sistema de arquivos, de modo que qualquer pessoa ou programa com acesso à máquina ou à pasta do projeto consegue lê-lo. Isso inclui outros usuários do mesmo computador ou servidor, um invasor que obtenha acesso ao sistema, uma falha que exponha o arquivo e cópias de segurança que acabem incluindo o `.env`. Também tem o risco de erro humano, como enviar o arquivo por e-mail ou mensagem, ou esquecer de incluí-lo no `.gitignore` antes do primeiro commit.
 
### Questão e
 
Um contêiner é uma unidade isolada que empacota uma aplicação junto com tudo o que ela precisa para funcionar, como bibliotecas, dependências e configurações. Ele roda como um processo isolado, compartilhando o núcleo do sistema operacional da máquina, o que o torna mais leve e rápido de iniciar do que uma máquina virtual completa. No caso desta atividade, o MariaDB e o CloudBeaver rodam cada um em seu contêiner, criados a partir de imagens prontas.
 
O Docker oferece várias vantagens em relação à instalação manual do SGBD no computador. A instalação é rápida e reproduzível, pois basta o arquivo `docker-compose.yml` e um comando para subir o ambiente. O SGBD não "suja" o sistema e pode ser removido por completo, junto com os dados, sem deixar resíduos. Também é possível errar e recomeçar do zero em poucos segundos, manter vários ambientes isolados em paralelo e compartilhar toda a configuração como código versionado, o que facilita a correção e a repetição do experimento.
