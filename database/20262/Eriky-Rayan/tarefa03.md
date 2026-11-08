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

    - Resposta: Se os dados do autor estivessem na tabela de livros e um autor mudasse de país ou tivesse seu nome corrigido, seria necessário alterar múltiplos registros (um para cada livro escrito por ele). Se algum registro não fosse atualizado por falha, o banco ficaria com dados contraditórios. Com as tabelas separadas, o autor é cadastrado uma única vez na tabela `autores`, e qualquer alteração é feita em um único lugar, refletindo automaticamente em todos os seus livros. Alem disso, em vez de repetir textos como o nome e o país do autor em cada linha da tabela `livros`, a tabela armazena apenas um número inteiro (`autor_id`), reduzindo drasticamente o tamanho do banco de dados e o uso de memória.

## 3. Respostas Dissertativas Conceituais

 - **Questão a:** Por que uma aplicação comercial nunca deve se conectar ao banco de dados utilizando o usuário `root`? O que pode ocorrer com o servidor de banco de dados caso as credenciais do usuário da aplicação sejam vazadas?
    - Resposta: Uma aplicação comercial nunca deve se conectar usando o usuário `root` porque ele possui privilégios totais e irrestritos no SGBD (`ALL PRIVILEGES`). Isso viola o princípio que determina que um componente de software deve possuir apenas os acessos estritamente necessários para executar suas funções. Se as credenciais vazadas forem as de uma conta dedicada da aplicação (como `app_biblioteca`), o impacto no servidor fica contido. O invasor não conseguirá assumir o controle do SGBD, acessar outros bancos de dados no mesmo servidor ou modificar configurações do sistema. O dano fica restrito aos dados da própria aplicação, onde ele poderá apenas ler ou alterar registros permitidos pelas licenças DML (`SELECT, INSERT, UPDATE, DELETE`) concedidas a essa conta. O servidor de banco de dados em si permanece preservado. O invasor não consegue derrubar a instância do SGBD, alterar configurações globais, acessar bancos de dados de outras aplicações no mesmo servidor ou executar comandos no sistema operacional.
- **Questão b:** Qual é a diferença fundamental entre privilégios DDL (Data Definition Language) e DML (Data Manipulation Language)? Por que é uma boa prática de segurança separá-los em contas de usuários distintas?
    - Resposta: Privilégios DDL permitem criar, alterar, renomear ou excluir a estrutura e o esquema dos objetos do banco de dados (como tabelas, índices e visões), utilizando comandos como `CREATE`, `ALTER` e `DROP`. Já os privilégios DML permitem consultar, inserir, atualizar ou remover os dados contidos dentro dessas estruturas, utilizando comandos como `SELECT, INSERT, UPDATE e DELETE`. Separalos é uma boa pratica pois se a aplicação utilizar uma conta restrita a DML, a exploração de uma falha permitirá que um atacante manipule registros, mas o impedirá de apagar tabelas (`DROP TABLE`) ou alterar colunas (`ALTER TABLE`), limitando o impacto da invasão. A conta com privilégios DDL fica restrita a rotinas controladas de manutenção, pipelines automatizados de migration ou ao administrador do banco (DBA), reduzindo o risco de alterações acidentais na estrutura do sistema.
- **Questão c:** Por que o arquivo `.env.example` deve ser commitado no repositório de código enquanto o arquivo `.env` nunca deve ser versionado? Quais são os riscos e consequências práticas de comitar credenciais reais em um repositório público no GitHub?
    - Resposta: `.env.example` funciona como um modelo estrutural e documentação do projeto. Ele lista todas as variáveis de ambiente necessárias para a aplicação funcionar, mas preenchidas apenas com valores genéricos ou vazios. Ele deve ser versionado para que qualquer desenvolvedor que clone o repositório saiba quais configurações precisa definir em seu ambiente local. Já o `.env` contém os valores reais e sigilosos das variáveis (senhas de banco de dados, chaves privadas, tokens de API). Ele deve ser mantido exclusivamente na máquina local/servidor e adicionado ao arquivo `.gitignore` para evitar seu versionamento em qualquer repositório (público ou privado). Existem bots e scripts maliciosos varrendo repositórios e uma informação sigilosa pode ser obtida e explorada rapidamente caso seja exposta. As informações também podem ser usadas para acessar o banco de dados e vazar informações dos clientes.
- **Questão d:** O uso do arquivo `.env` e a inclusão no `.gitignore` eliminam por completo todos os riscos de segurança de credenciais em um ambiente de desenvolvimento e produção? Justifique sua resposta considerando que o arquivo permanece armazenado em texto puro no sistema de arquivos do servidor.
    - Resposta: Não. A combinação do arquivo .env com o .gitignore resolve exclusivamente o risco de vazamento de credenciais através do repositório de código (Git). Contudo, ela não elimina todos os riscos de segurança, pois o arquivo continua armazenado em texto puro (plaintext) no disco do servidor. Como as credenciais estão em texto puro, qualquer usuário local do servidor, com privilégios de leitura inadequados ou script malicioso rodando na máquina terá acesso irrestrito às senhas contidas no arquivo.
- **Questão e:** O que é um contêiner e quais são as principais vantagens de utilizar o Docker para provisionar ambientes de banco de dados em atividades didáticas de graduação em comparação com a instalação manual do SGBD diretamente no sistema operacional do computador do aluno?
    - Resposta: Um contêiner é uma unidade padronizada de software que empacota o código de uma aplicação e todas as suas dependências (bibliotecas, arquivos de configuração e executáveis). O contêiner utiliza virtualização em nível de sistema operacional, compartilhando o kernel do sistema hospedeiro. Isso garante que ele seja extremamente leve, rápido para inicializar e isolado do restante do sistema. As vantagens do Docker são a padronização e reprodutabilidade do ambiente, garantindo que os alunos utilizem a mesma versão do SGBD, configurações de charset e dados iniciais, independentemente do SO o que elimina incompatibilidades.E permitir que o estudante pratique em um cenário realista.

## 4. Desafios Realizados

### Bloco A: Docker e Infraestrutura de Ambiente

1. **Alteração de porta do SGBD:** Altere a variável `MARIADB_PORT` no `.env` para a porta `3307`. Reinicie o serviço e explique como você reconfigurou a conexão do CloudBeaver para acessar o banco na porta alterada.
    - Resposta: Acessando as configurações da conexão no painel do CloudBeaver e alterando o campo Port de 3306 para 3307.

2. **Dois ambientes simultâneos:** Configure duas pastas distintas no seu computador com arquivos `docker-compose.yml` e portas/volumes desacoplados. Explique como você garantiu que quatro contêineres rodassem em paralelo sem conflito de portas ou nomes.
    - Resposta: A execução em paralelo sem conflitos é garantida por três isolamentos:
        - Nomes de projeto/contêiner: Usar nomes diferentes dos contêiners orginais.
        - Portas no host: Mapeamento de portas distintas para cada pasta (ex.: 3306 e 8978 no primeiro ambiente vs 3307 e 8979 no segundo).
        - Volumes: Declaração de volumes nomeados independentes para a gravação dos dados de cada banco.

3. **Persistência do volume e alteração de senha de root:** Altere o valor de `MARIADB_ROOT_PASSWORD` no arquivo `.env` para uma nova senha qualquer. Execute `docker compose up -d` e observe que a autenticação antiga continua válida enquanto a nova falha. Explique detalhadamente por que isso ocorre e quais são os dois caminhos possíveis para aplicar uma nova senha de root.
    - Resposta:

4. **Comportamento da validação estrita (:?):** Apague temporariamente o arquivo `.env` (ou comente a linha da senha de root) e execute `docker compose up -d`. Documente a mensagem de erro emitida pelo Compose e explique discursivamente a importância do modificador `:?` em ambientes profissionais.
    - Resposta:

5. **Inspeção de variáveis no compose:** Execute `docker compose config` no terminal e liste três variáveis de ambiente que foram resolvidas e interpoladas a partir do `.env`.
    - Resposta:

### Bloco B: Modelagem e Consultas SQL Básicas

6. **Criação da tabela de empréstimos:** Escreva o comando DDL para criar a tabela `emprestimos` contendo os campos `id` (INT AUTO_INCREMENT PRIMARY KEY), `livro_id` (INT), `data_emprestimo` (DATE) e `devolvido` (BOOLEAN), com restrição de chave estrangeira referenciando `livros(id)`.
    - Resposta:
7. **Carga da tabela empréstimos:** Escreva as instruções `INSERT` para cadastrar três registros de empréstimos, sendo dois com status não devolvido (`FALSE` ou `0`) e um devolvido (`TRUE` ou `1`).
    - Resposta:
8. **Consulta de pendências:** Escreva uma consulta que liste todos os empréstimos pendentes (não devolvidos), trazendo o título do livro, a data de empréstimo e o nome do autor do livro.
    - Resposta:
9. **Filtragem de grupos com HAVING:** Escreva uma consulta que agrupe os livros por autor e retorne a contagem total de obras de cada um, filtrando exclusivamente autores que possuem mais de 1 livro cadastrado (`HAVING COUNT(*) > 1`).
    - Resposta:
10. **Atualização proporcional (UPDATE):** Execute uma instrução DML para reajustar o preço de um livro específico em 10% de acréscimo. Transcreva a consulta `UPDATE` utilizada e comente o resultado.
    - Resposta:
11. **Remoção condicional (DELETE):** Cadastre um novo autor sem nenhum livro associado e, em seguida, execute a instrução `DELETE` para removê-lo da tabela `autores`. Explique por que essa remoção foi aceita sem violar a restrição de chave estrangeira.
    - Resposta:

### Bloco C: Administração e Privilégios Avançados

12. **Criação de usuário restrito para relatórios:** Crie um usuário chamado `relatorios` com senha `Relatorios2026!`, concedendo privilégio de `SELECT` exclusivamente sobre a tabela `livros` do banco `biblioteca`.
    - Resposta:
13. **Teste de restrição de visibilidade:** Conecte-se com o usuário `relatorios`, tente consultar a tabela `autores` e transcreva a mensagem de erro emitida pelo SGBD, explicando o motivo do bloqueio.
    - Resposta:
14. **Concessão e revogação dinâmica de privilégios:** Conectado como `root`, conceda privilégio de `INSERT` na tabela `livros` para o usuário `relatorios`. Realize uma inserção de teste com sucesso e, em seguida, revogue o privilégio via `REVOKE`. Descreva discursivamente o resultado de tentar inserir novamente após a revogação.
    - Resposta:
15. **Script idempotente de automação (setup.sql):** Desenvolva um script SQL completo chamado `setup.sql` que recrie do zero todo o banco de dados `biblioteca`, suas tabelas, restrições, usuários (`app_biblioteca`, `consulta`) com privilégios e a carga de dados. Versiona esse arquivo no seu repositório pessoal no GitHub.
    - Resposta:
