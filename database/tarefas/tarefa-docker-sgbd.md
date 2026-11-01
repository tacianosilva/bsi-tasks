# Tarefa 03 - Docker Compose, MariaDB e Administração de SGBD (T3)

## 1. Identificação e Objetivos

Disciplina: DCT2201 - Banco de Dados  
Curso: Sistemas de Informação - CERES/UFRN  
Carga horária estimada: 4 horas  

### Objetivo de aprendizagem
Ao término deste laboratório, o discente será capaz de:
- Provisionar e orquestrar múltiplos serviços conteinerizados (SGBD MariaDB e interface administrativa CloudBeaver) utilizando Docker Compose.
- Gerenciar variáveis de ambiente e segredos locais via arquivos de configuração, garantindo boas práticas de segurança e versionamento de código.
- Compreender a dinâmica de volumes Docker e o ciclo de vida da inicialização de bancos de dados relacionais.
- Conectar interfaces de gerenciamento através da rede virtual interna do Docker.
- Executar instruções DDL para criação de esquemas, tabelas, tipos de dados, chaves primárias e restrições de integridade referencial (chaves estrangeiras).
- Aplicar o princípio do menor privilégio administrando contas de usuários, escopos de acesso por host e permissões DDL e DML com comandos administrativos nativos.
- Escrever e validar consultas relacionais com filtros, ordenação, junções (JOIN), agregações (GROUP BY, AVG) e subconsultas.
- Utilizar o fluxo Git/GitHub para versionamento de relatórios e isolamento de projetos de infraestrutura.

## 2. Pré-requisitos e Verificação do Ambiente

Para a realização desta atividade, é obrigatório possuir o **Git**, o **Docker Engine** e o plugin **Docker Compose** instalados no sistema operacional.

Abra um terminal e execute os comandos abaixo para verificar as ferramentas instaladas:

```bash
git --version
```

```bash
docker --version
```

```bash
docker compose version
```

Certifique-se de que o Git está configurado com seu nome e e-mail (`git config --global user.name` e `git config --global user.email`) e que o daemon do Docker está em execução ativa antes de prosseguir.

## 3. Repositório Pessoal e Variáveis de Ambiente

O gerenciamento de credenciais e parâmetros de infraestrutura em projetos de software deve seguir convenções rígidas para evitar o vazamento de senhas em repositórios públicos.

### 3.1 Repositório pessoal público para a disciplina

Para versionar os códigos, scripts e arquivos de configuração deste laboratório:
1. O discente deve **criar ou reutilizar um repositório pessoal público no GitHub** dedicado à disciplina (por exemplo, `dct2201-banco-de-dados` ou `tarefas-bd`).
2. No `README.md` desse repositório pessoal, inclua uma seção clara indicando onde estão localizados os arquivos da Tarefa 03 (por exemplo, na pasta `tarefa03/` ou na raiz do repositório), descrevendo a finalidade de cada arquivo.
3. O link deste repositório pessoal público (apontando para o `README.md` correspondente) deverá ser informado no relatório em Markdown e na submissão do SIGAA.
4. **Importante:** Os códigos de infraestrutura (`docker-compose.yml`, `.env.example`, `setup.sql`, etc.) devem ficar **exclusivamente no seu repositório pessoal público**. Para o repositório da turma (`bsi-tasks`), só deve ser enviado o arquivo Markdown de resposta na branch do seu Pull Request vinculado à issue criada.

### 3.2 Criação do arquivo modelo (.env.example)

O arquivo `.env.example` serve como documentação técnica do contrato de configuração da aplicação. Ele deve ser versionado no seu repositório pessoal e conter apenas valores genéricos ou descritivos, nunca credenciais reais de produção ou segredos.

Crie na pasta da Tarefa 03 o arquivo `.env.example` com o seguinte conteúdo exato:

```text
MARIADB_ROOT_PASSWORD=troque_por_uma_senha_forte
MARIADB_DATABASE=labdb
MARIADB_PORT=3306
CLOUDBEAVER_PORT=8978
```

### 3.3 Criação do arquivo de ambiente local (.env)

O arquivo `.env` contém os valores reais utilizados na sua máquina local durante o desenvolvimento. Este arquivo **nunca** deve ser adicionado ao controle de versão Git.

Crie o arquivo `.env` na mesma pasta com o seguinte conteúdo:

```text
MARIADB_ROOT_PASSWORD=RootLab2026!aB
MARIADB_DATABASE=labdb
MARIADB_PORT=3306
CLOUDBEAVER_PORT=8978
```

Regras fundamentais sobre o arquivo `.env`:
- O arquivo deve se chamar exatamente `.env` (sem extensões como `.txt` ou prefixos adicionais).
- Deve estar localizado obrigatoriamente no mesmo diretório em que o comando `docker compose` for executado.

### 3.4 Configuração do .gitignore

Para assegurar que o arquivo com credenciais locais nunca seja enviado ao repositório acidentalmente, declare-o no `.gitignore`.

Crie ou edite o arquivo `.gitignore` na raiz do seu projeto pessoal:

```text
.env
```

### 3.5 Verificação de segurança e interpolação

Execute o comando do Git para comprovar que o arquivo `.env` está sendo corretamente ignorado pelo versionador:

```bash
git check-ignore -v .env
```

A saída esperada deve indicar o arquivo `.gitignore` e a linha correspondente que bloqueia o `.env`.

Em seguida, teste a resolução das variáveis no Docker Compose antes de iniciar qualquer contêiner:

```bash
docker compose config
```

O comando `docker compose config` valida a sintaxe do arquivo de composição, resolve e substitui todas as variáveis de ambiente a partir do `.env` e exibe no terminal a estrutura final que será aplicada. Sempre faça essa conferência antes de subir os serviços.

## 4. Definição da Infraestrutura com Docker Compose

Crie o arquivo `docker-compose.yml` na raiz do seu projeto com o conteúdo integral apresentado a seguir:

```yaml
services:
  mariadb:
    image: mariadb:11
    container_name: lab-mariadb
    environment:
      MARIADB_ROOT_PASSWORD: ${MARIADB_ROOT_PASSWORD:?defina MARIADB_ROOT_PASSWORD no arquivo .env}
      MARIADB_DATABASE: ${MARIADB_DATABASE:-labdb}
    ports:
      - "${MARIADB_PORT:-3306}:3306"
    volumes:
      - mariadb_data:/var/lib/mysql

  cloudbeaver:
    image: dbeaver/cloudbeaver:latest
    container_name: lab-cloudbeaver
    ports:
      - "${CLOUDBEAVER_PORT:-8978}:8978"
    depends_on:
      - mariadb

volumes:
  mariadb_data:
```

### Explicação detalhada da estrutura e da sintaxe de interpolação:

- `services`: Define o conjunto de contêineres que fazem parte da aplicação.
  - `mariadb`: Serviço de banco de dados baseado na imagem oficial `mariadb:11`.
  - `cloudbeaver`: Interface web de gerenciamento baseada na imagem `dbeaver/cloudbeaver:latest`.
- `container_name`: Atribui um nome fixo e legível para cada contêiner (`lab-mariadb` e `lab-cloudbeaver`), facilitando comandos manuais e inspeções.
- `environment`: Configura variáveis internas repassadas aos processos dentro do contêiner.
- `ports`: Realiza o mapeamento de portas no formato `PORTA_HOST:PORTA_CONTAINER`. O MariaDB escuta internamente na porta `3306` e o CloudBeaver na `8978`.
- `volumes`: O mapeamento `mariadb_data:/var/lib/mysql` garante a persistência física dos dados do banco. Sem esse volume nomeado, todos os bancos, tabelas e registros seriam destruídos caso o contêiner fosse removido.
- `depends_on`: Indica ao Docker Compose que o serviço `cloudbeaver` deve aguardar a criação do serviço `mariadb`.

### Modificadores de interpolação de variáveis:
- `${VAR}`: Interpola diretamente o valor definido no arquivo `.env`.
- `${VAR:-padrao}`: Utiliza o valor de fallback especificado após `:-` caso a variável `VAR` não esteja definida ou esteja vazia no `.env` (exemplo: `MARIADB_DATABASE` assume `labdb` caso omitida; `MARIADB_PORT` assume `3306`).
- `${VAR:?mensagem}`: Validação estrita obrigatória. Se a variável não estiver definida ou estiver vazia no `.env`, a execução do Docker Compose é abortada imediatamente exibindo a mensagem descrita. Esta regra é aplicada na senha de root (`MARIADB_ROOT_PASSWORD`) para impedir a subida de um banco de dados inseguro sem senha explicitamente configurada.

Importante sobre o ciclo de vida do volume: A variável `MARIADB_ROOT_PASSWORD` só é lida e configurada pelo script de entrypoint do contêiner durante a **primeira inicialização** do volume de dados. Alterar o valor dessa variável no `.env` com o ambiente já em execução e os dados já gravados no volume não alterará a senha do root existente. Para reiniciar o ambiente do zero e aplicar novas credenciais iniciais, o volume precisa ser explicitamente destruído e recriado com `docker compose down -v`.

## 5. Subida do Ambiente

Com os arquivos `.env` e `docker-compose.yml` devidamente preparados na mesma pasta, inicialize os serviços em segundo plano (modo detached):

```bash
docker compose up -d
```

Em seguida, verifique o estado dos contêineres criados:

```bash
docker ps
```

Certifique-se de que ambos os contêineres (`lab-mariadb` e `lab-cloudbeaver`) estão listados com o status `Up`.

Atenção ao tempo de inicialização: O MariaDB requer aproximadamente de 20 a 30 segundos em sua primeira execução para inicializar o diretório de dados em `/var/lib/mysql`, executar scripts internos de esquema e configurar as permissões. Caso tente conectar antes do término desse processo, a conexão será recusada. Para acompanhar o progresso em tempo real, utilize:

```bash
docker compose logs -f mariadb
```

Pressione `Ctrl + C` para sair dos logs quando a mensagem `mysqld: ready for connections` for exibida.

## 6. Configuração e Conexão via CloudBeaver

O CloudBeaver é uma ferramenta de administração de banco de dados relacional executada inteiramente pelo navegador web.

### 6.1 Assistente inicial de configuração
1. Abra seu navegador web e acesse o endereço: `http://localhost:8978`
2. No primeiro acesso, será apresentado o assistente de configuração (Setup Wizard).
3. Avance pelas etapas iniciais mantendo as configurações padrão.
4. Na tela de criação de credenciais do administrador do CloudBeaver, crie uma conta administrativa local (por exemplo, usuário `admin` e defina uma senha segura para o portal).
5. Conclua o assistente e faça login no CloudBeaver.

### 6.2 Criando a conexão com o MariaDB
1. Clique no botão de nova conexão (ícone de tomada ou botão "Create" -> "Connection").
2. Selecione o driver **MariaDB** (ou MySQL caso MariaDB não esteja em destaque direto).
3. Preencha os campos de conexão com extrema atenção:
   - **Host:** `mariadb`
   - **Port:** `3306`
   - **Database:** `labdb` (ou deixe em branco neste momento, pois criaremos o banco `biblioteca`)
   - **User name:** `root`
   - **Password:** `RootLab2026!aB` (a senha configurada no `.env`)
4. Ponto conceitual obrigatório: O CloudBeaver está sendo executado dentro de seu próprio contêiner isolado na rede virtual compartilhada criada pelo Docker Compose. Portanto, para o CloudBeaver alcançar o MariaDB, o endereço de rede (Host) deve ser obrigatoriamente o nome do serviço definido no compose (`mariadb`), e **nunca** `localhost`. O termo `localhost` referenciaria o próprio contêiner do CloudBeaver, onde não existe nenhum SGBD escutando.
5. Clique em **Test Connection** para validar os parâmetros. Com o teste bem-sucedido, salve a conexão.
6. Abra o editor de SQL (botão "SQL" na barra superior) vinculado a essa conexão para executar os scripts a seguir.

## 7. Introdução Prática a DDL: Modelagem e Criação do Banco

> **Nota Didática — Para quem está começando com Bancos de Dados:**  
> Você ainda estudará a linguagem SQL em detalhes nas próximas aulas. Por enquanto, guarde esta distinção fundamental:
> - **DDL (Data Definition Language — Linguagem de Definição de Dados):** São os comandos responsáveis por criar, alterar ou excluir as **estruturas** onde as informações serão guardadas (é como projetar gavetas, pastas e prateleiras). Exemplos: `CREATE DATABASE` (cria o banco de dados) e `CREATE TABLE` (cria as tabelas e define suas colunas e regras).
> - **DML (Data Manipulation Language — Linguagem de Manipulação de Dados):** São os comandos que lidam com o **conteúdo** dentro dessas estruturas (colocar novos dados com `INSERT`, consultar o que existe com `SELECT`, atualizar dados com `UPDATE` ou remover dados com `DELETE`).

Conectado como usuário `root` no editor SQL do CloudBeaver, execute os comandos DDL abaixo para criar o banco de dados `biblioteca` e as tabelas `autores` e `livros`:

```sql
CREATE DATABASE IF NOT EXISTS biblioteca
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_general_ci;

USE biblioteca;

CREATE TABLE IF NOT EXISTS autores (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  pais VARCHAR(50),
  ano_nascimento INT
);

CREATE TABLE IF NOT EXISTS livros (
  id INT AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR(150) NOT NULL,
  ano_publicacao INT,
  preco DECIMAL(10,2),
  autor_id INT,
  FOREIGN KEY (autor_id) REFERENCES autores(id)
);
```

### Explicação básica dos elementos DDL:
- `CREATE DATABASE` e `USE`: Criam o compartimento principal chamado `biblioteca` e ativam esse banco para os comandos seguintes.
- `utf8mb4`: Permite armazenar qualquer caractere Unicode (acentuação da língua portuguesa, caracteres internacionais e símbolos).
- `INT`: Define uma coluna numérica inteira (usada para anos e códigos identificadores).
- `VARCHAR(N)`: Define um campo de texto com limite máximo de N caracteres.
- `DECIMAL(10,2)`: Formato numérico exato com 2 casas decimais, ideal para valores monetários (preços).
- `AUTO_INCREMENT PRIMARY KEY`: Identificador único de cada linha. O banco gera números sequenciais automáticos (1, 2, 3...) a cada nova inserção, impedindo duplicidade de identificadores.
- `NOT NULL`: Obriga o preenchimento do campo (o dado não pode ficar vazio).
- `FOREIGN KEY (autor_id) REFERENCES autores(id)`: Chave estrangeira que conecta a tabela `livros` à tabela `autores`. Garante integridade referencial: um livro só pode ser cadastrado se o seu `autor_id` pertencer a um autor que já existe previamente na tabela `autores`.

**Pergunta Discursiva 1 (para responder no seu relatório):**  
*Explique com suas palavras a diferença entre criar uma tabela (DDL) e inserir registros nessa tabela (DML). Se apagarmos uma tabela com um comando DDL (`DROP TABLE`), o que acontece com os dados que estavam dentro dela?*

## 8. Gerenciamento de Usuários e Privilégios

A administração segura de bancos de dados exige a separação rigorosa de funções. Aplicações web e usuários humanos de consulta jamais devem operar sob a conta `root`.

### 8.1 Criação de usuários e concessão de privilégios (executar como root)

Execute as instruções abaixo para criar dois usuários com privilégios distintos:

```sql
CREATE USER 'app_biblioteca'@'%' IDENTIFIED BY 'AppBib2026!';
GRANT SELECT, INSERT, UPDATE, DELETE ON biblioteca.* TO 'app_biblioteca'@'%';

CREATE USER 'consulta'@'%' IDENTIFIED BY 'Consulta2026!';
GRANT SELECT ON biblioteca.* TO 'consulta'@'%';

FLUSH PRIVILEGES;
```

### Ponto conceitual obrigatório sobre o host '%'
No MySQL e MariaDB, as contas de usuário são identificadas pelo par `'usuario'@'host'`. Quando indicamos `'localhost'`, o SGBD apenas autoriza conexões originadas da própria máquina local via socket UNIX ou loopback. Como as aplicações (incluindo o CloudBeaver e serviços conteinerizados externos) conectam-se através da sub-rede virtual Docker, o endereço IP de origem não é `localhost`. O caractere curinga `'%'` autoriza a autenticação a partir de qualquer endereço de rede, sendo essencial para serviços que operam em contêineres distintos.

### 8.2 Inspeção de privilégios com SHOW GRANTS

Execute os comandos abaixo para inspecionar os privilégios concedidos a cada conta criada:

```sql
SHOW GRANTS FOR 'app_biblioteca'@'%';
SHOW GRANTS FOR 'consulta'@'%';
```

Observe que `app_biblioteca` possui apenas operações de manipulação de dados (DML), enquanto `consulta` possui apenas permissão de leitura (`SELECT`). Nenhum dos dois possui direitos DDL estruturais sobre o banco de dados.

### 8.3 Demonstração obrigatória do princípio do menor privilégio e erro 1142

1. No CloudBeaver, crie uma nova conexão apontando para o banco `biblioteca`, utilizando o usuário `app_biblioteca` e a senha `AppBib2026!`.
2. Abra um editor SQL sob esta conexão e tente executar uma operação DDL destrutiva:

```sql
DROP TABLE autores;
```

3. O MariaDB irá recusar a instrução e emitir a seguinte mensagem de erro:

```text
SQL Error [1142] [42000]: DROP command denied to user 'app_biblioteca'@'...' for table 'autores'
```

**Pergunta Discursiva 2 (para responder no seu relatório):**  
*Descreva com suas palavras o que aconteceu quando você tentou executar o comando `DROP TABLE autores` com a conta `app_biblioteca`. Por que o MariaDB recusou a operação com o erro 1142? De que forma essa restrição protege a integridade do banco de dados caso a aplicação web sofra uma invasão ou falha de programação?*

**Pergunta Discursiva 3 (para responder no seu relatório):**  
*Por que os usuários foram criados com o host `'%'` em vez de `'localhost'`? Qual é o papel da rede interna do Docker nessa decisão técnica?*

### 8.4 Operações de revogação e remoção (referência técnica)

Para gerenciar o ciclo de vida de privilégios, o SGBD disponibiliza os comandos `REVOKE` e `DROP USER`:

```sql
-- Exemplo para revogar um privilégio específico:
-- REVOKE INSERT ON biblioteca.* FROM 'app_biblioteca'@'%';

-- Exemplo para remover completamente um usuário:
-- DROP USER 'usuario_exemplo'@'%';
```

## 9. Carga de Dados e Povoamento com IA Generativa

Os comandos de inserção (`INSERT`) pertencem à categoria **DML** (Data Manipulation Language). Eles são usados para inserir tuplas (linhas de registros) nas tabelas que você criou.

### 9.1 Carga inicial mínima

Conectado como `root` ou como `app_biblioteca`, execute a inserção dos registros clássicos no banco `biblioteca`:

```sql
USE biblioteca;

INSERT INTO autores (nome, pais, ano_nascimento) VALUES
('Machado de Assis', 'Brasil', 1839),
('Clarice Lispector', 'Brasil', 1920),
('Gabriel García Márquez', 'Colômbia', 1927),
('Jane Austen', 'Inglaterra', 1775);

INSERT INTO livros (titulo, ano_publicacao, preco, autor_id) VALUES
('Dom Casmurro', 1899, 39.90, 1),
('Memórias Póstumas de Brás Cubas', 1881, 45.00, 1),
('A Hora da Estrela', 1977, 32.50, 2),
('Cem Anos de Solidão', 1967, 59.90, 3),
('Orgulho e Preconceito', 1813, 29.90, 4);
```

### 9.2 Povoamento expandido: Gerando mais dados com IA Generativa

Para testar consultas e operações com um volume mais realista de dados, você irá utilizar uma ferramenta de IA generativa (como ChatGPT, Claude ou Gemini) para gerar um lote adicional de autores e livros.

Copie e utilize o seguinte prompt na ferramenta de IA da sua escolha:

```text
Atue como um especialista em bancos de dados relacionais. 

Tenho duas tabelas no MariaDB com a seguinte estrutura DDL:

CREATE TABLE autores (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  pais VARCHAR(50),
  ano_nascimento INT
);

CREATE TABLE livros (
  id INT AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR(150) NOT NULL,
  ano_publicacao INT,
  preco DECIMAL(10,2),
  autor_id INT,
  FOREIGN KEY (autor_id) REFERENCES autores(id)
);

Já possuo 4 autores cadastrados (com IDs de 1 a 4). 
Por favor, gere comandos SQL 'INSERT INTO' para:
1. Mais 10 autores de diversas nacionalidades e épocas históricas (IDs a partir de 5).
2. Pelo menos 25 livros variados associados corretamente a esses novos autores (e também aos autores de IDs 1 a 4).
3. Preços realistas em formato numérico decimal (ex: 49.90) e anos de publicação consistentes com a época de nascimento do respectivo autor.

Retorne apenas o bloco de comandos SQL prontos para execução no MariaDB.
```

**Instruções de execução:**
1. Execute o script SQL gerado pela IA no editor SQL do CloudBeaver.
2. Salve os comandos gerados em um arquivo chamado `povoamento.sql` no seu repositório pessoal no GitHub.

**Pergunta Discursiva 4 (para responder no seu relatório):**  
*Quantos autores e livros no total ficaram cadastrados na sua base após a execução da carga expandida? O que aconteceria se você tentasse inserir um livro cujo `autor_id` fosse 999 (um autor inexistente)? Qual regra do banco impede essa ação?*

## 10. Consultas Obrigatórias (Leitura de Dados com SELECT)

As instruções de consulta são realizadas através do comando `SELECT`. Embora você ainda vá aprofundar os operadores de consulta ao longo da disciplina, execute individualmente cada uma das seis consultas abaixo no CloudBeaver para inspecionar os dados.

### Consulta 1: Seleção completa de livros
Recupera todos os registros e todas as colunas cadastradas na tabela de livros.
```sql
SELECT * FROM livros;
```

### Consulta 2: Projeção de atributos e ordenação descendente
Seleciona apenas as colunas de título e ano, exibindo as obras em ordem cronológica decrescente (do mais recente para o mais antigo).
```sql
SELECT titulo, ano_publicacao
FROM livros
ORDER BY ano_publicacao DESC;
```

### Consulta 3: Filtragem condicional (WHERE)
Filtra os livros aplicando uma condição temporal: apenas livros publicados antes do ano de 1900.
```sql
SELECT *
FROM livros
WHERE ano_publicacao < 1900;
```

### Consulta 4: Junção relacional (INNER JOIN) entre livros e autores
Combina dados de duas tabelas diferentes conectando a chave estrangeira (`livros.autor_id`) com a chave primária (`autores.id`), permitindo exibir o título do livro junto com o nome real do seu autor e o preço.
```sql
SELECT l.titulo, a.nome AS autor, l.preco
FROM livros l
JOIN autores a ON l.autor_id = a.id;
```

### Consulta 5: Agrupamento e cálculo de média (GROUP BY e AVG)
Agrupa as linhas por autor e calcula a média aritmética de preço das obras de cada escritor.
```sql
SELECT a.nome AS autor, AVG(l.preco) AS preco_medio
FROM autores a
JOIN livros l ON a.id = l.autor_id
GROUP BY a.id, a.nome;
```

### Consulta 6: Subconsulta comparativa
Usa uma consulta interna para calcular a média geral de preço de todos os livros e, em seguida, lista apenas os livros cujo preço individual seja superior a essa média.
```sql
SELECT *
FROM livros
WHERE preco > (SELECT AVG(preco) FROM livros);
```

**Pergunta Discursiva 5 (para responder no seu relatório):**  
*Analise as Consultas 4 e 5. Em linguagem simples, qual é a vantagem prática de dividir os dados em duas tabelas relacionadas (`autores` e `livros`) em vez de guardar o nome e o país do autor repetido dentro de cada linha da tabela de livros?*

## 11. Desafios Práticos

Realize os 15 desafios descritos abaixo. No seu arquivo `tarefa03.md`, documente o código SQL utilizado, os comandos no terminal e as respostas discursivas solicitadas para cada desafio (não é necessário anexar capturas de tela; as evidências são o código e as explicações conceituais).

### Bloco A: Docker e Infraestrutura de Ambiente

1. **Alteração de porta do SGBD:** Altere a variável `MARIADB_PORT` no `.env` para a porta `3307`. Reinicie o serviço e explique como você reconfigurou a conexão do CloudBeaver para acessar o banco na porta alterada.
2. **Dois ambientes simultâneos:** Configure duas pastas distintas no seu computador com arquivos `docker-compose.yml` e portas/volumes desacoplados. Explique como você garantiu que quatro contêineres rodassem em paralelo sem conflito de portas ou nomes.
3. **Persistência do volume e alteração de senha de root:** Altere o valor de `MARIADB_ROOT_PASSWORD` no arquivo `.env` para uma nova senha qualquer. Execute `docker compose up -d` e observe que a autenticação antiga continua válida enquanto a nova falha. Explique detalhadamente por que isso ocorre e quais são os dois caminhos possíveis para aplicar uma nova senha de root.
4. **Comportamento da validação estrita (:?):** Apague temporariamente o arquivo `.env` (ou comente a linha da senha de root) e execute `docker compose up -d`. Documente a mensagem de erro emitida pelo Compose e explique discursivamente a importância do modificador `:?` em ambientes profissionais.
5. **Inspeção de variáveis no compose:** Execute `docker compose config` no terminal e liste três variáveis de ambiente que foram resolvidas e interpoladas a partir do `.env`.

### Bloco B: Modelagem e Consultas SQL Básicas

6. **Criação da tabela de empréstimos:** Escreva o comando DDL para criar a tabela `emprestimos` contendo os campos `id` (INT AUTO_INCREMENT PRIMARY KEY), `livro_id` (INT), `data_emprestimo` (DATE) e `devolvido` (BOOLEAN), com restrição de chave estrangeira referenciando `livros(id)`.
7. **Carga da tabela empréstimos:** Escreva as instruções `INSERT` para cadastrar três registros de empréstimos, sendo dois com status não devolvido (`FALSE` ou `0`) e um devolvido (`TRUE` ou `1`).
8. **Consulta de pendências:** Escreva uma consulta que liste todos os empréstimos pendentes (não devolvidos), trazendo o título do livro, a data de empréstimo e o nome do autor do livro.
9. **Filtragem de grupos com HAVING:** Escreva uma consulta que agrupe os livros por autor e retorne a contagem total de obras de cada um, filtrando exclusivamente autores que possuem mais de 1 livro cadastrado (`HAVING COUNT(*) > 1`).
10. **Atualização proporcional (UPDATE):** Execute uma instrução DML para reajustar o preço de um livro específico em 10% de acréscimo. Transcreva a consulta `UPDATE` utilizada e comente o resultado.
11. **Remoção condicional (DELETE):** Cadastre um novo autor sem nenhum livro associado e, em seguida, execute a instrução `DELETE` para removê-lo da tabela `autores`. Explique por que essa remoção foi aceita sem violar a restrição de chave estrangeira.

### Bloco C: Administração e Privilégios Avançados

12. **Criação de usuário restrito para relatórios:** Crie um usuário chamado `relatorios` com senha `Relatorios2026!`, concedendo privilégio de `SELECT` exclusivamente sobre a tabela `livros` do banco `biblioteca`.
13. **Teste de restrição de visibilidade:** Conecte-se com o usuário `relatorios`, tente consultar a tabela `autores` e transcreva a mensagem de erro emitida pelo SGBD, explicando o motivo do bloqueio.
14. **Concessão e revogação dinâmica de privilégios:** Conectado como `root`, conceda privilégio de `INSERT` na tabela `livros` para o usuário `relatorios`. Realize uma inserção de teste com sucesso e, em seguida, revogue o privilégio via `REVOKE`. Descreva discursivamente o resultado de tentar inserir novamente após a revogação.
15. **Script idempotente de automação (setup.sql):** Desenvolva um script SQL completo chamado `setup.sql` que recrie do zero todo o banco de dados `biblioteca`, suas tabelas, restrições, usuários (`app_biblioteca`, `consulta`) com privilégios e a carga de dados. Versiona esse arquivo no seu repositório pessoal no GitHub.

## 12. Fluxo de Entrega e Estrutura do Relatório

O formato de entrega da Tarefa 03 combina o fluxo do repositório de tarefas da disciplina (`bsi-tasks`) com um repositório pessoal do discente para a infraestrutura do projeto.

### 12.1 Criação ou reutilização do repositório pessoal
1. Crie ou reutilize um **repositório pessoal público** no seu GitHub para a disciplina (ex.: `dct2201-banco-de-dados`).
2. No `README.md` desse repositório pessoal, inclua uma seção indicando onde estão os arquivos da Tarefa 03 (por exemplo, dentro de uma pasta `tarefa03/` ou na raiz), descrevendo os artefatos:
   - `.env.example`
   - `docker-compose.yml`
   - `.gitignore` (garantindo que `.env` não seja versionado)
   - `setup.sql` (quando implementado no desafio)
3. **ATENÇÃO:** Os códigos e arquivos de infraestrutura (`docker-compose.yml`, `.env.example`, etc.) **NÃO** devem ser enviados para o repositório `bsi-tasks`. Eles pertencem exclusivamente ao seu repositório pessoal público.

### 12.2 Fluxo no repositório bsi-tasks
1. **Crie uma issue** no repositório original `tacianosilva/bsi-tasks` com o título padronizado:  
   `Tarefa 03 - Docker e SGBD - <username>`  
   (onde `<username>` é o seu usuário no GitHub). Guarde o número da issue para citar nos commits (`#<id_issue>`).
2. Crie uma branch específica da tarefa no seu fork do `bsi-tasks` (ex.: `tarefa03/<username>` ou `feature/tarefa03`).
3. Crie e edite **apenas** o seu arquivo de resposta em Markdown localizado em:  
   `database/20262/<username>/tarefa03.md`  
   **Lembre-se:** o Pull Request para o `bsi-tasks` deve conter estritamente esse arquivo Markdown com as respostas e evidências; nenhum outro arquivo deve ser commitado no `bsi-tasks`.
4. Faça commits pequenos contendo a referência à issue (`#<id_issue>`) e abra o Pull Request da sua branch para a `main` do `bsi-tasks`.

### 12.3 Conteúdo obrigatório do arquivo tarefa03.md
O arquivo `tarefa03.md` deve ser organizado nas seguintes seções:

1. **Identificação e Repositório:**
   - Nome completo do discente, usuário no GitHub e e-mail acadêmico.
   - Link direto e clicável para o **repositório pessoal público no GitHub** contendo os arquivos de configuração (`docker-compose.yml`, `.env.example`, `.gitignore`, `povoamento.sql` e `setup.sql`), com o `README.md` orientativo.

2. **Respostas às Perguntas Discursivas dos Passos Práticos:**
   - **Pergunta Discursiva 1:** Diferença entre DDL e DML, e impacto de um `DROP TABLE`.
   - **Pergunta Discursiva 2:** Análise do erro 1142 ao tentar `DROP TABLE` com usuário restrito e relação com o princípio do menor privilégio.
   - **Pergunta Discursiva 3:** Justificativa técnica para o uso do host `'%'` em vez de `'localhost'` na arquitetura conteinerizada do Docker.
   - **Pergunta Discursiva 4:** Relato sobre o povoamento expandido gerado com IA (quantidade final de registros) e o que ocorre ao tentar associar livro a autor inexistente (integridade referencial).
   - **Pergunta Discursiva 5:** Análise das consultas relacionais e vantagens de normalizar dados em tabelas separadas (`autores` e `livros`) em vez de duplicar textos.

3. **Respostas Dissertativas Conceituais:**
   - **Questão a:** Por que uma aplicação comercial nunca deve se conectar ao banco de dados utilizando o usuário `root`? O que pode ocorrer com o servidor de banco de dados caso as credenciais do usuário da aplicação sejam vazadas?
   - **Questão b:** Qual é a diferença fundamental entre privilégios DDL (Data Definition Language) e DML (Data Manipulation Language)? Por que é uma boa prática de segurança separá-los em contas de usuários distintas?
   - **Questão c:** Por que o arquivo `.env.example` deve ser commitado no repositório de código enquanto o arquivo `.env` nunca deve ser versionado? Quais são os riscos e consequências práticas de comitar credenciais reais em um repositório público no GitHub?
   - **Questão d:** O uso do arquivo `.env` e a inclusão no `.gitignore` eliminam por completo todos os riscos de segurança de credenciais em um ambiente de desenvolvimento e produção? Justifique sua resposta considerando que o arquivo permanece armazenado em texto puro no sistema de arquivos do servidor.
   - **Questão e:** O que é um contêiner e quais são as principais vantagens de utilizar o Docker para provisionar ambientes de banco de dados em atividades didáticas de graduação em comparação com a instalação manual do SGBD diretamente no sistema operacional do computador do aluno?

4. **Desafios Realizados:**
   - Apresentação dos códigos SQL desenvolvidos, transcrição dos comandos do terminal e justificativas conceituais para os desafios dos Blocos A, B e C que foram executados.

> **Observação:** Não é necessário anexar capturas de tela (prints). As evidências da sua prática serão avaliadas através da clareza e precisão das suas respostas discursivas e da conferência dos arquivos versionados no seu repositório pessoal público.

### 12.4 Envio no SIGAA
No portal SIGAA, na tarefa correspondente, o discente deve enviar textualmente:
1. O link do **Pull Request** aberto no repositório `bsi-tasks`.
2. O link do **Repositório Pessoal** do discente no GitHub contendo os arquivos e markdowns criados.

## 13. Encerramento do Laboratório

Ao concluir os testes e a coleta de evidências para o relatório, compreenda os três modos de encerramento do ambiente:

### Modo 1: Pausar e remover os contêineres mantendo os dados persistidos
Para parar e remover os contêineres sem perder o banco de dados criado:
```bash
docker compose down
```
Quando você executar `docker compose up -d` novamente no futuro, todos os bancos, tabelas e dados estarão intactos, pois foram armazenados no volume nomeado `mariadb_data`.

### Modo 2: Reiniciar os serviços
Para aplicar alterações pontuais de portas ou novas configurações de contêiner sem apagar volumes:
```bash
docker compose up -d
```

### Modo 3: Destruição completa do ambiente e dos dados
Para remover os contêineres, redes e apagar definitivamente todos os volumes de dados associados:
```bash
docker compose down -v
```
Atenção: A flag `-v` remove o volume `mariadb_data`. Utilize apenas quando quiser reiniciar completamente o banco do zero ou liberar espaço no disco.

## 14. Guia de Solução de Problemas Comuns

### Falha 1: Porta 3306 ocupada no computador do aluno
- **Sintoma:** Ao executar `docker compose up -d`, ocorre erro informando `bind: address already in use` na porta 3306.
- **Causa:** Há uma instância local do MySQL ou MariaDB instalada diretamente no sistema operacional e em execução ativa na máquina.
- **Solução:** Edite o arquivo `.env` e altere a variável `MARIADB_PORT=3307` (ou outra porta disponível). O Docker Compose mapeará a porta 3307 do host para a porta 3306 interna do contêiner sem necessidade de desinstalar o SGBD local.

### Falha 2: Contêiner fecha imediatamente após o início (Exited)
- **Sintoma:** O comando `docker ps` não lista o contêiner `lab-mariadb` e `docker ps -a` indica status `Exited (1)`.
- **Causa:** A variável `MARIADB_ROOT_PASSWORD` não foi definida no arquivo `.env` ou o `.env` não está no mesmo diretório em que o comando foi rodado.
- **Solução:** Verifique a presença do arquivo `.env` e confirme que a variável de senha está devidamente preenchida. Consulte o motivo exato com `docker compose logs mariadb`.

### Falha 3: Esquecimento ou erro na senha do usuário root
- **Sintoma:** Tentativa de login como root no CloudBeaver resulta em `Access denied for user 'root'@'...'`.
- **Causa:** O volume de dados já foi inicializado anteriormente com uma senha diferente da que está atualmente no arquivo `.env`.
- **Solução:** Caso não haja dados relevantes a preservar, remova completamente o volume com `docker compose down -v` e reinicie com `docker compose up -d` para que a nova senha do `.env` seja aplicada no momento da criação inicial do volume.

### Falha 4: Interface web do CloudBeaver não carrega ou conexão é recusada
- **Sintoma:** O navegador web informa que a página `http://localhost:8978` não pode ser encontrada ou exibe erro de conexão com o banco.
- **Causa:** O contêiner ainda está baixando imagens, compilando assets iniciais ou o MariaDB ainda está na fase de bootstrap de 30 segundos.
- **Solução:** Aguarde cerca de 30 segundos e acompanhe a prontidão através de `docker compose logs -f`. Verifique se o endereço no navegador não inclui `https://` indevidamente.
