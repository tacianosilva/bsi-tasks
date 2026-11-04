1. **Identificação e Repositório:**
   - **Nome completo:** Lucas da Costa Santos
   - **Usuário no GitHub:** [lucascsantos07](https://github.com/lucascsantos07)
   - **E-mail acadêmico:** lucas.costa.123@ufrn.edu.br
   - **Repositório pessoal público:** https://github.com/lucascsantos07/dct2201-banco-de-dados.git

2. **Respostas às Perguntas Discursivas dos Passos Práticos:**
   - **Pergunta Discursiva 1:** DDL é a linguagem utilizada para definir e modificar a estrutura do banco de dados, como criar, alterar ou excluir tabelas. Já a DML é utilizada para manipular os dados armazenados nessas tabelas, permitindo inserir, atualizar e excluir registros. O comando DROP TABLE pertence à DDL e seu impacto é excluir completamente uma tabela, removendo sua estrutura e todos os dados armazenados nela.
   - **Pergunta Discursiva 2:** O comando DROP TABLE autores foi recusado porque o usuário app_biblioteca possui apenas privilégios de manipulação de dados (DML), como inserir, consultar, atualizar e excluir registros, mas não possui permissões para alterar a estrutura do banco de dados (DDL). Por isso, o MariaDB retornou o erro 1142. Essa restrição protege a integridade do banco de dados, impedindo que uma invasão ou falha na aplicação web provoque a exclusão de tabelas e a perda de sua estrutura e dos dados armazenados.
   - **Pergunta Discursiva 3:** Os usuários foram criados com o host '%' para permitir conexões de diferentes endereços IP, e não apenas da própria máquina, como acontece com 'localhost'. Isso é necessário porque os serviços executados em contêineres Docker se comunicam por meio de uma rede interna virtual, utilizando endereços IP próprios. Assim, o host '%' permite que esses serviços se conectem ao banco de dados sem restringir a conexão ao endereço local.
   - **Pergunta Discursiva 4:** ficaram cadastrados 14 autores e 33 livros na base de dados. Caso fosse inserido um livro com autor_id igual a 999, o MariaDB recusaria a operação, pois esse autor não existe na tabela autores. Essa restrição é garantida pela chave estrangeira, que assegura a integridade referencial e impede que um livro seja associado a um autor inexistente.
   - **Pergunta Discursiva 5:** A principal vantagem é evitar a repetição de informações. Se os dados dos autores ficassem na tabela de livros, o nome e o país de um mesmo autor seriam repetidos em todos os seus livros. Separando as tabelas, cada autor precisa ser cadastrado apenas uma vez, e seus livros são relacionados a ele pela chave estrangeira. Isso também facilita a alteração e a exclusão de informações, além de evitar dados diferentes para um mesmo autor.

3. **Respostas Dissertativas Conceituais:**
   - **Questão a:** Uma aplicação comercial não deve utilizar o usuário root porque ele possui acesso total ao banco de dados, podendo alterar ou excluir informações e até remover tabelas. O ideal é utilizar um usuário próprio, com apenas as permissões necessárias. Caso as credenciais desse usuário sejam vazadas, alguém poderá acessar o banco e consultar, alterar ou excluir dados, causando prejuízos e perda de informações.
   - **Questão b:** DDL são comandos utilizados para criar, alterar ou excluir a estrutura do banco de dados. Já DML são comandos utilizados para inserir, consultar, atualizar e excluir os dados das tabelas. Separar esses privilégios em usuários diferentes é uma boa prática de segurança porque evita que um usuário que precisa apenas trabalhar com os dados consiga modificar ou excluir a estrutura do banco, reduzindo o risco de danos.
   - **Questão c:** O arquivo .env.example deve ser enviado ao GitHub porque mostra quais variáveis precisam ser configuradas, mas sem conter senhas reais. Já o .env não deve ser enviado porque armazena informações privadas, como senhas e credenciais de acesso. Se essas informações forem publicadas em um repositório público, outras pessoas poderão utilizá-las para acessar o banco de dados, roubar ou alterar informações e até causar danos ao sistema.
   - **Questão d:** Não. O uso do .env e do .gitignore reduz os riscos, mas não elimina todos eles. Isso porque o arquivo .env continua armazenado em texto puro no servidor e se alguém conseguir acessar esse arquivo, poderá visualizar as senhas e utilizar as credenciais para acessar o banco de dados. Por isso, também é importante restringir o acesso ao arquivo, proteger o servidor e utilizar outras medidas de segurança para evitar o vazamento dessas informações.
   - **Questão e:** Um contêiner é um ambiente isolado que reúne uma aplicação e tudo o que ela precisa para funcionar, como arquivos, configurações e dependências. O Docker permite criar e executar esses ambientes de forma rápida e padronizada, sem precisar instalar o SGBD diretamente no computador. Entre as principais vantagens estão a facilidade de instalação e configuração, a redução de conflitos com outros programas, a possibilidade de utilizar a mesma versão do banco de dados em diferentes computadores e a facilidade de remover ou recriar o ambiente quando necessário. Em atividades didáticas, isso facilita a preparação dos laboratórios e permite que todos os alunos trabalhem em ambientes semelhantes, independentemente das configurações de seus computadores.

4. **Desafios Práticos** 
   ### Bloco A: Docker e Infraestrutura de Ambiente
**Desafio 1**: A variável `MARIADB_PORT` no arquivo `.env` foi alterada de `3306` para `3307`. Em seguida, o serviço MariaDB foi reiniciado para aplicar a alteração. No Docker Compose, a porta externa `3307` foi direcionada para a porta interna `3306` do container. Como o CloudBeaver também está sendo executado em um container na mesma rede Docker, sua conexão foi mantida com o Host `mariadb` e a porta `3306`. Dessa forma, o acesso externo ao banco passou a utilizar a porta `3307`, enquanto a comunicação interna entre os containers continuou utilizando a porta `3306`.


**Desafio 2**: Foram criadas duas pastas distintas, cada uma contendo seu próprio arquivo `docker-compose.yaml` e um arquivo `.env` para armazenar as configurações do ambiente. Cada projeto possui dois contêineres: um **MariaDB**, responsável pelo banco de dados, e um **CloudBeaver**, utilizado para acessar e administrar o banco.

A estrutura ficou organizada da seguinte forma:

```text
tarefa-03/
├── ambiente-1/
│   ├── docker-compose.yaml
│   └── .env
│
└── ambiente-2/
    ├── docker-compose.yaml
    └── .env
```

## Configurações para evitar conflitos

Para permitir que os dois ambientes funcionassem simultaneamente, foram realizadas algumas configurações:

- **Nomes dos contêineres:** o primeiro ambiente manteve os nomes `lab-mariadb` e `lab-cloudbeaver`. No segundo, foram utilizados `lab2-mariadb` e `lab2-cloudbeaver`, evitando duplicidade de nomes.
- **Portas:** foram definidas portas externas diferentes para cada ambiente. O primeiro utiliza as portas `3307` (MariaDB) e `8978` (CloudBeaver), enquanto o segundo utiliza `3308` (MariaDB) e `8979` (CloudBeaver). As portas internas dos contêineres foram mantidas em `3306` para o MariaDB e `8978` para o CloudBeaver.
- **Volumes:** cada ambiente possui seu próprio volume para armazenar os dados do MariaDB. Dessa forma, as informações de um banco não interferem nas do outro.
- **Arquivos `.env`:** cada pasta possui seu próprio arquivo de configuração, permitindo definir senhas e portas de maneira independente.

## Inicialização dos ambientes

Após configurar os arquivos, os ambientes foram iniciados separadamente, utilizando os seguintes comandos no terminal:

**Primeiro ambiente:**

```powershell
cd ambiente-1
docker compose up -d
```

**Segundo ambiente:**

```powershell
cd ..\ambiente-2
docker compose up -d
```

## Verificação e teste de independência

Para verificar se os quatro contêineres estavam funcionando ao mesmo tempo, foi utilizado o comando:

```powershell
docker ps
```

O resultado confirmou que os dois contêineres do primeiro ambiente e os dois do segundo estavam ativos simultaneamente.

Também foi necessário utilizar endereços diferentes no navegador para acessar os dois CloudBeaver sem conflito entre as sessões:

- Primeiro ambiente: [http://localhost:8978](http://localhost:8978)
- Segundo ambiente: [http://127.0.0.1:8979](http://127.0.0.1:8979)

Por fim, foi realizado um teste de independência entre os bancos de dados, verificando que as tabelas criadas em um ambiente não apareciam no outro. Isso confirmou que os dados estavam separados e que os dois ambientes funcionavam de maneira independente.


Desafio 3: Para verificar o comportamento da variável `MARIADB_ROOT_PASSWORD`, foi utilizado o segundo ambiente (`ambiente-2`). Inicialmente, o valor dessa variável foi alterado no arquivo `.env`, definindo uma nova senha para o usuário `root`. Em seguida, foi executado o comando `docker compose up -d` para aplicar a configuração.

Após a inicialização, foram realizados dois testes de autenticação no MariaDB, utilizando o seguinte comando:

```powershell
docker exec -it lab2-mariadb mariadb -u root -p
```

No primeiro teste, foi informada a senha antiga, e a autenticação ocorreu normalmente, permitindo o acesso ao terminal do MariaDB:

```text
Welcome to the MariaDB monitor.
Your MariaDB connection id is 9
Server version: 11.8.9-MariaDB-ubu2404
```

No segundo teste, foi informada a nova senha definida no arquivo `.env`. Entretanto, a autenticação foi recusada, retornando o seguinte erro:

```text
ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)
```

Os resultados demonstraram que, mesmo após a alteração da variável no arquivo `.env` e a execução do Docker Compose, a senha antiga continuou válida, enquanto a nova não foi reconhecida.

Isso ocorre porque a variável `MARIADB_ROOT_PASSWORD` é utilizada durante a primeira inicialização do banco de dados, quando o usuário `root` é criado e sua senha é definida. Como os dados são armazenados em um volume persistente, nas inicializações seguintes o MariaDB identifica que o banco já foi configurado e não executa novamente o processo de criação dos usuários. Portanto, modificar o arquivo `.env` não altera automaticamente as credenciais já armazenadas no banco.

Existem dois caminhos para aplicar uma nova senha de root:

a) **Alterar a senha diretamente no MariaDB:** acessar o banco utilizando a senha antiga e executar o comando `ALTER USER 'root'@'localhost' IDENTIFIED BY 'NovaSenha2026';`. Essa alternativa preserva os dados existentes, sendo necessário também manter o arquivo `.env` atualizado com a nova senha.

b) **Remover o volume e inicializar o banco novamente:** executar `docker compose down -v` para remover os contêineres e o volume associado ao ambiente. Em seguida, executar `docker compose up -d` para inicializar o banco novamente, utilizando a senha atualmente definida no `.env`. Essa alternativa apaga os dados armazenados no volume.

Dessa forma, foi possível observar que a persistência dos volumes mantém não apenas os dados do banco, mas também as configurações de autenticação realizadas durante sua inicialização.


**Desafio 4**: Para verificar o comportamento da validação estrita do Docker Compose, foi utilizada a configuração do primeiro ambiente (`ambiente-1`). Inicialmente, a linha `MARIADB_ROOT_PASSWORD` foi comentada no arquivo `.env`, simulando a ausência de uma variável obrigatória.

Em seguida, foi executado o comando:

```powershell
docker compose up -d
```

O Docker Compose interrompeu a execução e apresentou a seguinte mensagem de erro:

```text
error while interpolating services.mariadb.environment.MARIADB_ROOT_PASSWORD:
required variable MARIADB_ROOT_PASSWORD is missing a value:
defina MARIADB_ROOT_PASSWORD no arquivo .env
```

O resultado demonstra que o modificador `:?` exige que a variável esteja definida e possua um valor. Quando essa condição não é atendida, o Compose interrompe o processamento da configuração e apresenta uma mensagem de erro, impedindo a inicialização dos serviços com parâmetros incompletos.

Em ambientes profissionais, esse mecanismo é importante para garantir maior segurança e confiabilidade na configuração das aplicações. Ele evita que contêineres sejam iniciados sem informações essenciais, como senhas e credenciais de acesso, reduzindo problemas de configuração e facilitando a identificação de erros durante a implantação.

Portanto, a validação estrita permite identificar a ausência de parâmetros obrigatórios antecipadamente, antes que os serviços sejam iniciados com configurações inadequadas.


**Desafio 5**: Para verificar a resolução das variáveis de ambiente definidas no arquivo `.env`, foi executado o seguinte comando no terminal, dentro da pasta `ambiente-1`:

```powershell
docker compose config
```

O comando apresentou a configuração final dos serviços, substituindo as referências às variáveis de ambiente pelos valores correspondentes. Entre as configurações identificadas, destacam-se:

- **`MARIADB_DATABASE`:** resolvida para `labdb`, indicando o nome do banco de dados que será utilizado.
- **`MARIADB_ROOT_PASSWORD`:** identificada na configuração e resolvida com o valor definido no arquivo .env, que foi ocultado na apresentação do resultado por segurança.
- **`MARIADB_PORT`:** utilizada para definir a porta externa `3307`, por meio do mapeamento para a porta interna `3306` do MariaDB.

Dessa forma, foi possível observar que o comando `docker compose config` permite visualizar como as variáveis são interpretadas e aplicadas à configuração dos serviços antes de sua execução, facilitando a identificação de valores ausentes ou incorretos.