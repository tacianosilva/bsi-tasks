# Tarefa 03 — Docker Compose, MariaDB e Administração de SGBD

## 1. Identificação e Repositório

- **Discente:** Juan Vyctor Silva Garcia de Oliveira
- **GitHub:** [Juan-Vyctor](https://github.com/Juan-Vyctor)
- **E-mail acadêmico:** juan.oliveira.704@ufrn.edu.br
- **Disciplina:** DCT2201 — Banco de Dados, Sistemas de Informação — CERES/UFRN.
- **Repositório pessoal público e README:** [dct2201-banco-de-dados](https://github.com/Juan-Vyctor/dct2201-banco-de-dados/blob/main/README.md).
- **Arquivos:** [docker-compose.yml](https://github.com/Juan-Vyctor/dct2201-banco-de-dados/blob/main/tarefa3/docker-compose.yaml), [.env.example](https://github.com/Juan-Vyctor/dct2201-banco-de-dados/blob/main/tarefa3/.env.example), [.gitignore](https://github.com/Juan-Vyctor/dct2201-banco-de-dados/blob/main/.gitignore), [povoamento.sql](https://github.com/Juan-Vyctor/dct2201-banco-de-dados/blob/main/tarefa3/povoamento.sql) e setup.sql.

Vale ressaltar que o arquivo de povoamento da base ([povoamento.sql](https://github.com/Juan-Vyctor/dct2201-banco-de-dados/blob/main/tarefa3/povoamento.sql)) foi gerado com auxílio de uma IA generativa, o [Claude](claude.ai), devido à instruções explicitas vindas da tarefa.


## 2. Repostas das perguntas discursivas

### *Explique com suas palavras a diferença entre criar uma tabela (DDL) e inserir registros nessa tabela (DML). Se apagarmos uma tabela com um comando DDL (`DROP TABLE`), o que acontece com os dados que estavam dentro dela?*

Criar uma tabela seria como uma nova entidade no banco, com campos distintos e características diferentes, podendo se relacionar com outras ou não. Um exemplo seria:

```SQL
CREATE TABLE pessoa(
  id INT PRIMARY KEY,
  nome VARCHAR(50),
  cpf INT
);
```

Estamos criando uma nova tabela sem nenhum valor, apenas fazendo o "molde". O DML seria lidar com o povoamento dessa tabela, inserindo, removendo e alterando dados, inserindo uma nova tupla na tabela.

Se for feito o `DROP TABLE`, os dados se perdem, simples e fácil. Se não há mais onde serem guardados os dados, não há mais dados guardados.

### *Descreva com suas palavras o que aconteceu quando você tentou executar o comando `DROP TABLE autores` com a conta `app_biblioteca`. Por que o MariaDB recusou a operação com o erro 1142? De que forma essa restrição protege a integridade do banco de dados caso a aplicação web sofra uma invasão ou falha de programação?*

Foi uma questão de segurança. Como `app_biblioteca` não tem permissão alguma além de fazer consultas no banco, é impossível que o mesmo tome alguma ação maliciosa sob os dados salvos, como fazer a exclusão da tabela. O erro 1142 é exatamente isso, `Command denied to user for table`, negando o usuário de fazer o que queria. Com essa camada de segurança, caso um usuário externo consiga acesso às queries e tente forçar um comando ao banco (criação de uma nova tupla ou exclusão de algum dado), ele será barrado por não ter as permissões necessárias.

### *Por que os usuários foram criados com o host `'%'` em vez de `'localhost'`? Qual é o papel da rede interna do Docker nessa decisão técnica?*

Como `localhost` funciona apenas com a própria máquina, podem ocorrer problemas com os contêineres internos da rede do Docker, que vem de fora. Por isso usar o `%`, ele é um coringa que aceita qualquer host que chegue sem mais problemas. O CloudBeaver fica em outro contêiner, e isso poderia dar conflito se não usássemos a entrada genérica, nesse caso com o nome `mariadb` que definimos.

### *Quantos autores e livros no total ficaram cadastrados na sua base após a execução da carga expandida? O que aconteceria se você tentasse inserir um livro cujo `autor_id` fosse 999 (um autor inexistente)? Qual regra do banco impede essa ação?*

No total ficaram 14 autores e 31 livros. Fazendo o teste manual com um `autor_id`como 999, foi retornado o seguinte erro:

```SQL
Error executing query:
SQL Error [1452] [23000]: (conn=10) Cannot add or update a child row: a foreign key constraint fails (`biblioteca`.`livros`, CONSTRAINT `livros_ibfk_1` FOREIGN KEY (`autor_id`) REFERENCES `autores` (`id`))
```

Esse erro trata exatamente da falha da `foreign key`, impedindo o resto da operação de acontecer.

### *Analise as Consultas 4 e 5. Em linguagem simples, qual é a vantagem prática de dividir os dados em duas tabelas relacionadas (`autores` e `livros`) em vez de guardar o nome e o país do autor repetido dentro de cada linha da tabela de livros?*

O motivo principal é evitar dados repetidos e dessa forma diminuir a chance de ter inconsistências no sistema. Nessa base, Machado de Assis tem quatro livros salvos, se todas as suas informações ficassem salvas na tabela `livros`, qualquer alteração no perfil do autor teria de ser repetida em todas as entradas, algo que em bancos maiores é completamente inviável. Deixar em tabelas separadas facilita tanto a busca (procurar dentro de `autores`) quanto manter a consistência de dados.


## 3. Desafios

### Bloco A: Docker e Infraestrutura de Ambiente

#### 1. Alteração de porta do SGBD: Altere a variável MARIADB_PORT no .env para a porta 3307. Reinicie o serviço e explique como você reconfigurou a conexão do CloudBeaver para acessar o banco na porta alterada.

Mudando o arquivo a variável no arquivo `.env`, o próximo passo foi também corrigir as configurações do `docker-composer.yaml`, mais especificamente em ports, trocando para a nova 3307. Tentei fazer o comando para subir ao ar, mas recebi um erro:

```
Error response from daemon: Conflict. The container name "/lab-mariadb" is already in use by container "<ID do contêiner>".
You have to remove (or rename) that container to be able to reuse that name.
```

Então fiz isso, removi o antigo com `docker rm lab-mariadb`, e imaginando que o mesmo aconteceria com o contêiner `lab-cloudbeaver`, fiz o mesmo procedimento, apenas alterando o nome do arquivo a ser removido. Depois disso, subi com `docker compose up -d && docker compose ps` e tudo parecia estar certinho.

Indo para o Cloudbeaver, tive que fazer a configuração inicial novamente, já que o anterior foi removido. Criei com as mesmas senhas e dados, e recriei todas as entradas que estavam no banco anteriormente.


#### 2.  Dois ambientes simultâneos: Configure duas pastas distintas no seu computador com arquivos docker-compose.yml e portas/volumes desacoplados. Explique como você garantiu que quatro contêineres rodassem em paralelo sem conflito de portas ou nomes.

A organização de diretórios ficou a seguite:

```
dct2201-banco-de-dados/
├── .gitignore
├── README.txt
└── tarefa3/
    ├── .env
    ├── .env.example
    ├── docker-compose.yaml
    ├── povoamento.sql
    ├── ambiente1/
    │   ├── .env
    │   ├── .env.example
    │   └── docker-compose.yaml
    └── ambiente2/
        ├── .env
        ├── .env.example
        └── docker-compose.yaml
```

As mudanças principais foram dentro de cada arquivo. Nos dois ambientes novos, os arquivos ` .env` tiveram seus dados alterados para impedir conflitos, tanto o Mariadb quanto o CloudBeaver ganharam novas portas, e um novo nome foi dado para cada database. Nos arquivos ` .yaml`, a ideia foi similar mas um pouco mais aprofundada: os dois contêiners ganharam o sufixo   `ambiente<numero>`para serem diferenciados, assim como seus`volumes`. Também foi necessário mudar as portas utilizadas para estarem de acordo com os novos valores do `.env`, alteração feita da mesma forma que a anterior. Como não existiam valores prévios para esses ambientes, não foi necessário faazer nenhuma exclusão.


#### 3. Persistência do volume e alteração de senha de root: Altere o valor de MARIADB_ROOT_PASSWORD no arquivo .env para uma nova senha qualquer. Execute docker compose up -d e observe que a autenticação antiga continua válida enquanto a nova falha. Explique detalhadamente por que isso ocorre e quais são os dois caminhos possíveis para aplicar uma nova senha de root.

A que se mantém válida é a antiga, mesmo após a atualização do `.env`. O que acontece é que o MariaDB só faz a verificação das variáveis de ambiente se não houver um banco já criado. Como na primeira inicialização não tinha, foi feito todo o processo de criação e definição de valores, algo que até é citado nas instruções da tarefa. Como à esse ponto já existe um banco, o MariaDB simplesmente pula essa etapa, e nem chega a olhar o `.env` novamente.

Duas das formas de resolver são as seguinte:

1. Apagar tudo e criar de novo. Como não vão haver dados salvos, o processo inicial será feito novamente e os novos dados serão aplicados, ao custo de perder tudo que o banco possuia.
2. Alterar a senha manualmente. É possível acessar via Docker nosso banco, e lá dentro fazer a alteração dos dados. O comando `ALTER USER 'usuario' IDENTIFIED BY 'nova senha'` funciona perfeitamente para o que é requisitado aqui.

#### 4. Comportamento da validação estrita (:?): Apague temporariamente o arquivo .env (ou comente a linha da senha de root) e execute docker compose up -d. Documente a mensagem de erro emitida pelo Compose e explique discursivamente a importância do modificador :? em ambientes profissionais.

```
error while interpolating services.mariadb.environment.MARIADB_ROOT_PASSWORD:
required variable MARIADB_ROOT_PASSWORD is missing a value: defina MARIADB_ROOT_PASSWORD no arquivo .env
```

O símbolo `:?` é um sinal de obrigatoriedade no Docker, e ele pode ser entendido como "se essa variável está faltando, é um erro." O valor antes do sinal é o que não queremos que falte, nesse caso a senha, e o após é o erro que queremos exibir para quem tentou fazer a operação. Esse tipo de tratamento é extremamente importante não somente em ambientes profissionais mas em qualquer projeto trabalhado por múltiplas pessoas. Não pensando somente no fator "rodar o código com algo faltando", isso também previne que a ausência de algo vital para o funcionamento não irá causar nenhum problema na aplicação enquanto no ar, como o corrompimento de um arquivo ou a quebra de alguma parte do sistema.


#### 5. Inspeção de variáveis no compose: Execute docker compose config no terminal e liste três variáveis de ambiente que foram resolvidas e interpoladas a partir do .env.

1. MARIADB_DATABASE: O valor foi aquele declarado na variável de ambiente.
2. MARIADB_ROOT_PASSWORD: mesmo que no CloudBeaver ainda esteja sendo utilizada a senha, antiga, o valor alterado em `.env` se registra aqui.
3. PORT (tanto no CloudBeaver quanto MariaDB): As portas são coletadas a partir desse arquivo, e se houver inconsistências, o sistema não vai ao ar.
