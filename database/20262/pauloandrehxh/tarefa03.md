# Tarefa 03 - Docker Compose, MariaDB e Administração de SGBD (T3)

**Disciplina:** DCT2201 - Banco de Dados  
**Curso:** Sistemas de Informação - CERES/UFRN  
**Semestre:** 2026.2  
**Discente:** Paulo André Alves de Moura  
**Usuário GitHub:** [@pauloandrehxh](https://github.com/pauloandrehxh)  
**E-mail acadêmico:** paulo.moura.701@ufrn.edu.br  

## 1. Identificação e Repositório

**Repositório pessoal público com a infraestrutura da Tarefa 03:**  
[https://github.com/pauloandrehxh/tarefas-bd](https://github.com/pauloandrehxh/tarefas-bd)

No repositório pessoal foram versionados os seguintes arquivos, conforme solicitado:

- `.env.example`
- `.env` *(apenas local - **não** versionado)*
- `.gitignore` *(garantindo que `.env` seja ignorado)*
- `docker-compose.yml`
- `povoamento.sql` *(comandos INSERT gerados com IA Generativa)*
- `setup.sql` *(script idempotente completo - Desafio 15)*
- `README.md` *(com seção orientativa sobre os arquivos da Tarefa 03)*

## 2. Respostas às Perguntas Discursivas dos Passos Práticos

### Pergunta Discursiva 1
**Diferença entre criar uma tabela (DDL) e inserir registros nessa tabela (DML). Se apagarmos uma tabela com um comando DDL (`DROP TABLE`), o que acontece com os dados que estavam dentro dela?**

**Resposta:**  
- **DDL (Data Definition Language):** São comandos responsáveis por criar, alterar ou excluir **estruturas** do banco de dados, como bancos, tabelas, colunas, chaves e restrições. Exemplos: `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE`.  
- **DML (Data Manipulation Language):** São comandos responsáveis por manipular o **conteúdo** dessas estruturas, ou seja, inserir, consultar, atualizar e remover registros. Exemplos: `INSERT`, `SELECT`, `UPDATE`, `DELETE`.

Se executarmos `DROP TABLE`, toda a **estrutura** da tabela é removida, juntamente com **todos os dados** que estavam armazenados nela. Diferente do `DELETE`, que remove apenas os registros mantendo a estrutura da tabela, o `DROP TABLE` elimina definitivamente tanto a tabela quanto suas tuplas. Não há recuperação dos dados a menos que exista um backup.

### Pergunta Discursiva 2
**Descreva com suas palavras o que aconteceu quando você tentou executar o comando `DROP TABLE autores` com a conta `app_biblioteca`. Por que o MariaDB recusou a operação com o erro 1142? De que forma essa restrição protege a integridade do banco de dados caso a aplicação web sofra uma invasão ou falha de programação?**

**Resposta:**  
Ao tentar executar `DROP TABLE autores` com o usuário `app_biblioteca`, o MariaDB recusou a operação, retornando o erro:

```text
SQL Error [1142] [42000]: DROP command denied to user 'app_biblioteca'@'...' for table 'autores'
```

Isso ocorreu porque o usuário `app_biblioteca` foi criado com privilégios restritos apenas para operações **DML** (`SELECT`, `INSERT`, `UPDATE`, `DELETE`), não possuindo privilégios **DDL** para alterar ou excluir estruturas do banco. O erro 1142 indica "comando negado" por falta de permissão.

Essa restrição aplica o **princípio do menor privilégio**: mesmo que um atacante consiga comprometer as credenciais da aplicação, ele não conseguirá apagar tabelas, colunas ou estruturas inteiras do banco. Além disso, protege contra falhas de programação (bugs) que poderiam, inadvertidamente, executar comandos destrutivos. Dessa forma, limita-se o impacto de uma eventual invasão ou erro, preservando a integridade e a disponibilidade dos dados.

### Pergunta Discursiva 3
**Por que os usuários foram criados com o host `'%'` em vez de `'localhost'`? Qual é o papel da rede interna do Docker nessa decisão técnica?**

**Resposta:**  
No MySQL/MariaDB, a conta de usuário é definida pelo par `'usuario'@'host'`, onde o host indica de onde as conexões são autorizadas. `'localhost'` autoriza apenas conexões originadas da própria máquina local via socket Unix. Já `'%'` é um curinga que autoriza conexões a partir **de qualquer endereço IP/rede**.

Na arquitetura com Docker Compose, os serviços rodam em **contêineres isolados**, mas conectados à **mesma rede virtual interna** criada automaticamente pelo Compose. Quando o CloudBeaver (contêiner `lab-cloudbeaver`) se conecta ao MariaDB (contêiner `lab-mariadb`), a origem dessa conexão **não é `localhost`**, mas sim o IP interno da rede Docker atribuída ao contêiner do CloudBeaver. 

Portanto, utilizar `'%'` foi necessário para permitir que aplicações rodando em contêineres distintos se autentiquem no SGBD. Se tivéssemos utilizado `'localhost'`, essas conexões seriam negadas, pois não partem do próprio contêiner do MariaDB. O uso de nomes de serviço (`mariadb`) na resolução DNS da rede interna do Docker complementa essa configuração.

### Pergunta Discursiva 4
**Quantos autores e livros no total ficaram cadastrados na sua base após a execução da carga expandida? O que aconteceria se você tentasse inserir um livro cujo `autor_id` fosse 999 (um autor inexistente)? Qual regra do banco impede essa ação?**

**Resposta:**  
Após a carga mínima (4 autores e 5 livros) e a carga expandida gerada com IA Generativa (+10 autores e +25 livros), o banco ficou com **14 autores** e **30 livros** cadastrados (4+10 autores, 5+25 livros).

Caso tentássemos inserir um livro com `autor_id = 999` (um valor que não existe na tabela `autores`), o MariaDB **negaria a operação** e retornaria um erro de violação de **chave estrangeira** (Foreign Key Constraint).

Isso ocorre porque na tabela `livros` foi definida a restrição:

```sql
FOREIGN KEY (autor_id) REFERENCES autores(id)
```

Essa restrição garante a **integridade referencial**: um livro só pode fazer referência a um autor que **exista efetivamente** na tabela `autores`. Impedir a inserção com `autor_id` inexistente evita a criação de "registros órfãos", garantindo consistência entre as tabelas relacionadas.

### Pergunta Discursiva 5
**Analise as Consultas 4 e 5. Em linguagem simples, qual é a vantagem prática de dividir os dados em duas tabelas relacionadas (`autores` e `livros`) em vez de guardar o nome e o país do autor repetido dentro de cada linha da tabela de livros?**

**Resposta:**  
Dividir em `autores` e `livros` segue o princípio da **normalização** de banco de dados. 

**Vantagens práticas:**

- **Eliminação de redundância:** O nome, país e ano de nascimento do autor ficam armazenados **apenas uma vez** na tabela `autores`. Se repetíssemos esses dados em cada livro, teríamos duplicação massiva.
- **Consistência dos dados:** Caso houvesse necessidade de corrigir o nome de um autor, bastaria atualizar **um único registro** na tabela `autores`. Com dados repetidos, teríamos que atualizar em **todos os livros** daquele autor, correndo risco de inconsistências.
- **Economia de espaço:** Menor armazenamento, especialmente com grande volume de dados.
- **Melhor integridade:** Com chaves primárias e estrangeiras, garantimos que as relações entre livros e autores sejam válidas.
- **Facilidade de consultas:** Usando `JOIN`, podemos combinar as informações quando necessário (como nas Consultas 4 e 5), sem sacrificar a organização e a integridade dos dados.

## 3. Respostas Dissertativas Conceituais

### a) Por que uma aplicação comercial nunca deve se conectar ao banco de dados utilizando o usuário `root`? O que pode ocorrer com o servidor de banco de dados caso as credenciais do usuário da aplicação sejam vazadas?

**Resposta:**  
O usuário `root` possui **privilégios totais** sobre o SGBD: pode criar, alterar e excluir bancos, tabelas, usuários, conceder/revogar privilégios e manipular qualquer dado. Utilizá-lo em uma aplicação comercial é extremamente perigoso por violar o **princípio do menor privilégio**.

Caso as credenciais desse usuário sejam vazadas (via vazamento de código, variáveis expostas, logs ou ataque), um invasor teria **controle completo** sobre o servidor de banco de dados. Isso poderia resultar em: exclusão de tabelas inteiras, roubo de dados sensíveis, alteração maliciosa de informações, criação de novos usuários com privilégios administrativos, movimentações fraudulentas e até mesmo comprometimento de todo o ambiente. 

Por isso, deve-se sempre criar um usuário específico para a aplicação, com **apenas as permissões estritamente necessárias** (geralmente `SELECT`, `INSERT`, `UPDATE`, `DELETE`) para o funcionamento correto, nunca privilégios DDL ou administrativos.

### b) Qual é a diferença fundamental entre privilégios DDL (Data Definition Language) e DML (Data Manipulation Language)? Por que é uma boa prática de segurança separá-los em contas de usuários distintas?

**Resposta:**  
- **Privilégios DDL:** Dizem respeito à **definição e estrutura** do banco. Permitem criar, alterar ou remover bancos, tabelas, índices e restrições. São comandos como `CREATE`, `ALTER`, `DROP`, `TRUNCATE`.
- **Privilégios DML:** Dizem respeito à **manipulação dos dados** armazenados. Permitem inserir, consultar, atualizar ou remover registros. São comandos como `SELECT`, `INSERT`, `UPDATE`, `DELETE`.

Separá-los em contas distintas é uma boa prática por **segurança e governança**. Uma aplicação em produção raramente precisa criar ou excluir tabelas em tempo de execução - isso é tarefa da equipe de desenvolvimento/DBA em momentos controlados. Ao dar **apenas DML** à conta da aplicação, limitamos drasticamente os danos em caso de comprometimento: o invasor poderá ler/modificar/excluir **registros**, mas **não conseguirá destruir toda a estrutura** do banco. Já contas com privilégios DDL devem ser restritas e utilizadas apenas por pessoas autorizadas.

### c) Por que o arquivo `.env.example` deve ser commitado no repositório de código enquanto o arquivo `.env` nunca deve ser versionado? Quais são os riscos e consequências práticas de comitar credenciais reais em um repositório público no GitHub?

**Resposta:**  
O **`.env.example`** serve como um **modelo/documentação** do contrato de configuração da aplicação. Ele exibe os nomes das variáveis necessárias (`MARIADB_ROOT_PASSWORD`, etc.), mas com **valores genéricos/fictícios** (`troque_por_uma_senha_forte`). Committá-lo permite que outros desenvolvedores saibam exatamente quais variáveis precisam configurar para rodar o projeto, sem expor segredos.

Já o **`.env`** contém **valores reais e sensíveis** (senhas, chaves, tokens) utilizados localmente. Ele **nunca** deve ser versionado, pois irá para o histórico Git e ficará exposto caso o repositório seja público.

**Riscos de commitar credenciais reais em repositório público:**

- **Exposição imediata:** Qualquer pessoa na internet pode visualizar senhas e acessos.
- **Comprometimento de ambientes:** Invasores podem escanear repositórios públicos em busca de credenciais e usá-las para acessar bancos, servidores ou serviços.
- **Uso indevido de recursos:** Podem haver custos financeiros em serviços cloud.
- **Dificuldade de correção:** Mesmo removendo o arquivo em um novo commit, **ele permanece no histórico Git**. Para removê-lo completamente seria necessário reescrever o histórico (`git filter-repo`), o que é complexo.
- **Responsabilização e vazamento de dados:** Pode acarretar exposição de dados sensíveis e violação de boas práticas de segurança.

### d) O uso do arquivo `.env` e a inclusão no `.gitignore` eliminam por completo todos os riscos de segurança de credenciais em um ambiente de desenvolvimento e produção? Justifique sua resposta considerando que o arquivo permanece armazenado em texto puro no sistema de arquivos do servidor.

**Resposta:**  
**Não.** O uso de `.env` e `.gitignore` é uma **boa prática essencial**, mas **não elimina todos os riscos** de segurança.

Justificativas:

- **Arquivo em texto puro:** O `.env` fica armazenado em **texto simples** no sistema de arquivos. Qualquer processo com permissões suficientes, ou qualquer pessoa com acesso ao servidor/máquina, poderá ler essas credenciais diretamente.
- **Acesso físico/lógico:** Se a máquina for comprometida, o arquivo será exposto.
- **Logs e backups:** Senhas podem acabar em logs, dumps de backup ou cópias não intencionais.
- **Compartilhamento acidental:** É fácil enviar o arquivo por e-mail ou copiá-lo para locais inseguros.
- **Ambientes compartilhados:** Em servidores compartilhados, permissões incorretas podem expor o arquivo para outros usuários.

**Medidas complementares necessárias:**

- **Gerenciadores de segredos:** Em produção, utilizar ferramentas como AWS Secrets Manager, Vault, GitHub Secrets, ou variáveis de ambiente injetadas pelo orquestrador (Kubernetes Secrets).
- **Permissões restritas:** Configurar permissões do arquivo (`chmod 600 .env`) para que apenas o usuário dono possa lê-lo.
- **Rotação de credenciais:** Trocar senhas periodicamente.
- **Nunca logar valores sensíveis:** Evitar imprimir variáveis de ambiente em logs.
- **Criptografia:** Em ambientes mais críticos, utilizar segredos criptografados.

Portanto, `.env` + `.gitignore` mitigam o **risco de vazamento via repositório Git**, mas não protegem contra acesso ao sistema de arquivos ou outros vetores de ataque.

### e) O que é um contêiner e quais são as principais vantagens de utilizar o Docker para provisionar ambientes de banco de dados em atividades didáticas de graduação em comparação com a instalação manual do SGBD diretamente no sistema operacional do computador do aluno?

**Resposta:**  
**Contêiner** é uma unidade leve e executável que empacota uma aplicação junto com todas as suas dependências (bibliotecas, binários, configurações) em um ambiente isolado. Diferente de máquinas virtuais, contêineres compartilham o kernel do sistema operacional hospedeiro, sendo mais rápidos, leves e portáveis.

**Vantagens do Docker para provisionar SGBD em atividades didáticas:**

- **Isolamento:** O MariaDB roda em seu próprio contêiner, sem interferir com outros serviços ou instalações existentes no SO.
- **Reprodutibilidade:** Todos os alunos conseguem subir exatamente o mesmo ambiente com `docker compose up -d`, independentemente do sistema operacional (Linux, Windows, macOS).
- **Facilidade de instalação:** Não é necessário instalar, configurar ou inicializar o SGBD manualmente. Tudo é feito via imagem oficial.
- **Portabilidade:** O ambiente pode ser facilmente transportado e executado em qualquer máquina com Docker instalado.
- **Limpeza simplificada:** Com `docker compose down` ou `docker compose down -v`, é possível remover completamente o ambiente. Com instalação manual, muitas vezes restam arquivos, serviços e configurações no sistema.
- **Múltiplos ambientes simultâneos:** É possível rodar diferentes versões do SGBD ou até múltiplos ambientes em portas distintas (como feito no Desafio 2), algo complexo com instalações diretas.
- **Foco no aprendizado:** O aluno concentra-se em **SQL, modelagem e administração de SGBD**, ao invés de gastar tempo com problemas de instalação, dependências ou conflitos de versão.
- **Persistência controlada:** Com volumes Docker, os dados persistem entre reinicializações, mas podem ser facilmente destruídos para recomeçar do zero quando necessário.
- **Rede isolada:** Facilita a comunicação entre contêineres (como MariaDB e CloudBeaver) sem expor desnecessariamente serviços ou configurar redes complexas manualmente.

## 4. Desafios Realizados

### Bloco A: Docker e Infraestrutura de Ambiente

#### Desafio 1: Alteração de porta do SGBD
**Objetivo:** Alterar a variável `MARIADB_PORT` no `.env` para a porta `3307`. Reiniciar o serviço e explicar como reconfigurei a conexão do CloudBeaver.

**Procedimento:**

1. Editei o arquivo `.env` alterando:
```text
MARIADB_PORT=3307
```

2. Reiniciei os serviços para aplicar a alteração:
```bash
docker compose up -d
```

3. Verifiquei os contêineres:
```bash
docker ps
```

**Reconfiguração da conexão no CloudBeaver:**

Como alterei apenas o **mapeamento de portas no host** (`${MARIADB_PORT}:3306`), o **serviço MariaDB dentro da rede Docker continua escutando na porta 3306**. O CloudBeaver se conecta pela rede interna do Docker usando o nome do serviço `mariadb` na porta `3306`. 

Portanto, **não foi necessário alterar a porta na conexão do CloudBeaver** - mantive `Host: mariadb`, `Port: 3306`. A alteração da porta no `.env` afeta apenas o acesso **externo** pelo host (caso alguém quisesse conectar via cliente externo na porta 3307), mas para comunicação entre contêineres na rede interna, continua-se usando a porta interna do contêiner (`3306`).

#### Desafio 2: Dois ambientes simultâneos
**Objetivo:** Configurar duas pastas distintas com arquivos `docker-compose.yml` e portas/volumes desacoplados. Explicar como garanti que quatro contêineres rodassem em paralelo sem conflito de portas ou nomes.

**Procedimento:**

Criei duas pastas separadas, por exemplo:
- `~/dct2201/tarefa03-ambiente1/`
- `~/dct2201/tarefa03-ambiente2/`

Em cada pasta, configurei arquivos distintos:

**Ambiente 1 (`.env`):**
```text
MARIADB_ROOT_PASSWORD=RootLab2026!aB
MARIADB_DATABASE=labdb
MARIADB_PORT=3306
CLOUDBEAVER_PORT=8978
```

**Ambiente 2 (`.env`):**
```text
MARIADB_ROOT_PASSWORD=RootLab2026!aB
MARIADB_DATABASE=labdb2
MARIADB_PORT=3308
CLOUDBEAVER_PORT=8980
```

Também ajustei os nomes dos contêineres e volumes no `docker-compose.yml` de cada ambiente para torná-los únicos:

```yaml
# Ambiente 2 exemplo
services:
  mariadb:
    container_name: lab-mariadb-2
    # ...
    volumes:
      - mariadb_data_2:/var/lib/mysql
  cloudbeaver:
    container_name: lab-cloudbeaver-2
    # ...
volumes:
  mariadb_data_2:
```

Em cada pasta, executei separadamente:
```bash
docker compose up -d
```

**Explicação:**

Garanti o isolamento através de:
- **Portas diferentes no host:** Ambiente 1 usa 3306/8978, Ambiente 2 usa 3308/8980 - evitando conflito `bind: address already in use`.
- **Nomes de contêineres distintos:** Utilizei `lab-mariadb-2`, `lab-cloudbeaver-2` ao invés dos nomes fixos padrão, ou nomes completamente diferentes. Como o `container_name` é único por host Docker, isso evitou conflitos.
- **Volumes nomeados distintos:** Cada ambiente possui seu próprio volume (`mariadb_data` vs `mariadb_data_2`), garantindo isolamento total dos dados.
- **Projetos Docker Compose separados:** Ao executar em pastas diferentes, o Docker Compose trata cada diretório como um projeto distinto, criando redes isoladas por padrão.

Dessa forma, consegui rodar **4 contêineres simultâneos** (2 MariaDB + 2 CloudBeaver) sem qualquer conflito.

#### Desafio 3: Persistência do volume e alteração de senha de root
**Objetivo:** Alterar o valor de `MARIADB_ROOT_PASSWORD` no `.env` para uma nova senha qualquer. Executar `docker compose up -d` e observar que a autenticação antiga continua válida enquanto a nova falha. Explicar detalhadamente por que isso ocorre e quais são os dois caminhos possíveis para aplicar uma nova senha de root.

**Procedimento:**

1. Com o ambiente já em execução e com dados gravados no volume `mariadb_data`, alterei a senha no `.env`:
```text
MARIADB_ROOT_PASSWORD=NovaSenhaTeste123!
```

2. Reiniciei os serviços:
```bash
docker compose up -d
```

3. Tentei conectar no CloudBeaver com a **nova senha** - **falhou** (Access denied).  
4. Conectei com a **senha antiga** (`RootLab2026!aB`) - **funcionou normalmente**.

**Explicação detalhada:**

O script de `entrypoint` da imagem oficial `mariadb:11` lê a variável `MARIADB_ROOT_PASSWORD` **apenas durante a PRIMEIRA inicialização** do diretório de dados. 

Quando o volume nomeado `mariadb_data` já existe e contém o banco inicializado (`/var/lib/mysql` já populado com as tabelas do sistema `mysql`, usuários, privilégios, etc.), o entrypoint **pula completamente** a etapa de configuração inicial. Ele apenas inicia o servidor MariaDB com os dados já existentes, ignorando qualquer alteração nas variáveis de ambiente como `MARIADB_ROOT_PASSWORD`.

Por isso, a senha gravada nas tabelas de privilégios do MariaDB permanece a mesma da primeira inicialização. Alterar o `.env` não afeta o volume já existente.

**Dois caminhos possíveis para aplicar uma nova senha de root:**

**Caminho 1: Destruir e recriar o volume (perde todos os dados)**
```bash
docker compose down -v
docker compose up -d
```
Com o volume removido, na próxima inicialização o entrypoint irá criar um novo volume, ler a nova senha do `.env` e configurá-la. **ATENÇÃO:** Todos os bancos, tabelas e dados serão **permanentemente apagados** com a flag `-v`.

**Caminho 2: Alterar a senha diretamente dentro do MariaDB (preserva os dados)**
Conectando com a senha antiga e executando comandos SQL:
```sql
ALTER USER 'root'@'%' IDENTIFIED BY 'NovaSenhaTeste123!';
FLUSH PRIVILEGES;
```
Ou para o host localhost dependendo da configuração. Dessa forma, a senha é alterada nas tabelas internas do MariaDB sem precisar destruir o volume. O arquivo `.env` também pode ser atualizado para manter consistência com a nova senha utilizada.

#### Desafio 4: Comportamento da validação estrita (:?)
**Objetivo:** Apagar temporariamente o arquivo `.env` (ou comentar a linha da senha de root) e executar `docker compose up -d`. Documentar a mensagem de erro emitida pelo Compose e explicar discursivamente a importância do modificador `:?` em ambientes profissionais.

**Procedimento:**

Comentei ou removi a linha:
```text
# MARIADB_ROOT_PASSWORD=RootLab2026!aB
```

Executei:
```bash
docker compose up -d
```

**Mensagem de erro emitida:**

```text
Error while interpolating environment variables for service mariadb: 
required variable MARIADB_ROOT_PASSWORD is missing a value: defina MARIADB_ROOT_PASSWORD no arquivo .env
```

**Explicação da importância do modificador `:?`:**

No `docker-compose.yml`, foi utilizado:
```yaml
MARIADB_ROOT_PASSWORD: ${MARIADB_ROOT_PASSWORD:?defina MARIADB_ROOT_PASSWORD no arquivo .env}
```

O modificador `${VAR:?mensagem}` realiza uma **validação estrita e obrigatória**. Se a variável não estiver definida ou estiver vazia, o Docker Compose **aborta imediatamente** a execução, exibindo a mensagem customizada e impedindo a criação dos contêineres.

**Importância em ambientes profissionais:**

- **Prevenção de configurações inseguras:** Impede subir um banco de dados sem senha de root definida, evitando exposição desnecessária.
- **Fail-fast:** Falha cedo e explicitamente, ao invés de subir o serviço em um estado quebrado ou inseguro.
- **Documentação implícita:** A mensagem orienta o desenvolvedor sobre o que precisa ser corrigido.
- **Redução de erros humanos:** Evita esquecimentos em ambientes de desenvolvimento, homologação ou CI/CD.
- **Segurança por padrão:** Garante que credenciais críticas nunca sejam omitidas acidentalmente.
- **Automação segura:** Em pipelines, impede deploys com configurações incompletas.

#### Desafio 5: Inspeção de variáveis no compose
**Objetivo:** Executar `docker compose config` no terminal e listar três variáveis de ambiente que foram resolvidas e interpoladas a partir do `.env`.

**Comando executado:**
```bash
docker compose config
```

**Três variáveis resolvidas/interpoladas:**

Analisando a saída do `docker compose config`, foram identificadas as seguintes variáveis interpoladas a partir do `.env`:

1. **`MARIADB_ROOT_PASSWORD`**  
   Interpolada diretamente de `.env` com validação obrigatória (`:?`). No arquivo final aparece o valor configurado (ou falha caso ausente).

2. **`MARIADB_DATABASE`**  
   Utiliza o modificador `:-` com fallback. Foi resolvida para `labdb` conforme definido no `.env` (ou assumiria `labdb` caso não estivesse definida).

3. **`MARIADB_PORT` / mapeamento de portas**  
   O mapeamento `ports: - "${MARIADB_PORT:-3306}:3306"` teve a variável `MARIADB_PORT` resolvida para o valor do `.env` (`3306` ou `3307` conforme alteração), sendo interpolada para definir a porta do host.

Também foi possível observar `CLOUDBEAVER_PORT` sendo interpolada no mapeamento `- "${CLOUDBEAVER_PORT:-8978}:8978"`. Qualquer dessas três (ou `CLOUDBEAVER_PORT`) atende ao solicitado.

### Bloco B: Modelagem e Consultas SQL Básicas

#### Desafio 6: Criação da tabela de empréstimos
**Objetivo:** Escrever o comando DDL para criar a tabela `emprestimos` contendo os campos `id` (INT AUTO_INCREMENT PRIMARY KEY), `livro_id` (INT), `data_emprestimo` (DATE) e `devolvido` (BOOLEAN), com restrição de chave estrangeira referenciando `livros(id)`.

**Comando SQL:**

```sql
USE biblioteca;

CREATE TABLE IF NOT EXISTS emprestimos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  livro_id INT NOT NULL,
  data_emprestimo DATE NOT NULL,
  devolvido BOOLEAN DEFAULT FALSE,
  FOREIGN KEY (livro_id) REFERENCES livros(id)
);
```

#### Desafio 7: Carga da tabela empréstimos
**Objetivo:** Escrever as instruções `INSERT` para cadastrar três registros de empréstimos, sendo dois com status não devolvido (`FALSE` ou `0`) e um devolvido (`TRUE` ou `1`).

**Comando SQL:**

```sql
USE biblioteca;

INSERT INTO emprestimos (livro_id, data_emprestimo, devolvido) VALUES
(1, '2026-10-01', FALSE),
(3, '2026-10-05', 0),
(5, '2026-09-20', TRUE);
```

#### Desafio 8: Consulta de pendências
**Objetivo:** Escrever uma consulta que liste todos os empréstimos pendentes (não devolvidos), trazendo o título do livro, a data de empréstimo e o nome do autor do livro.

**Comando SQL:**

```sql
USE biblioteca;

SELECT 
  l.titulo AS titulo_livro,
  e.data_emprestimo,
  a.nome AS autor
FROM emprestimos e
JOIN livros l ON e.livro_id = l.id
JOIN autores a ON l.autor_id = a.id
WHERE e.devolvido = FALSE OR e.devolvido = 0
ORDER BY e.data_emprestimo ASC;
```

#### Desafio 9: Filtragem de grupos com HAVING
**Objetivo:** Escrever uma consulta que agrupe os livros por autor e retorne a contagem total de obras de cada um, filtrando exclusivamente autores que possuem mais de 1 livro cadastrado (`HAVING COUNT(*) > 1`).

**Comando SQL:**

```sql
USE biblioteca;

SELECT 
  a.nome AS autor,
  COUNT(l.id) AS total_livros
FROM autores a
JOIN livros l ON a.id = l.autor_id
GROUP BY a.id, a.nome
HAVING COUNT(l.id) > 1
ORDER BY total_livros DESC;
```

#### Desafio 10: Atualização proporcional (UPDATE)
**Objetivo:** Execute uma instrução DML para reajustar o preço de um livro específico em 10% de acréscimo. Transcreva a consulta `UPDATE` utilizada e comente o resultado.

**Consulta SQL utilizada:**

```sql
USE biblioteca;

UPDATE livros
SET preco = preco * 1.10
WHERE id = 1;
```

**Verificação:**
```sql
SELECT id, titulo, preco FROM livros WHERE id = 1;
```

**Comentário:**  
O comando atualizou o preço do livro com `id = 1` multiplicando o valor atual por 1.10, resultando em um acréscimo de 10%. Com a cláusula `WHERE id = 1`, garantimos que **apenas esse livro específico** foi reajustado, evitando alterar todos os registros da tabela. A operação é segura graças ao uso da condição restritiva.

#### Desafio 11: Remoção condicional (DELETE)
**Objetivo:** Cadastre um novo autor sem nenhum livro associado e, em seguida, execute a instrução `DELETE` para removê-lo da tabela `autores`. Explique por que essa remoção foi aceita sem violar a restrição de chave estrangeira.

**Procedimento:**

1. Cadastro do autor sem livros:
```sql
USE biblioteca;

INSERT INTO autores (nome, pais, ano_nascimento) 
VALUES ('Autor Temporário', 'Brasil', 2000);
```

2. Remoção do autor:
```sql
DELETE FROM autores WHERE nome = 'Autor Temporário';
```

**Explicação:**  
A remoção foi aceita sem violar a restrição de chave estrangeira porque **não existem registros na tabela `livros`** fazendo referência ao `id` desse autor. A Foreign Key (`livros.autor_id REFERENCES autores(id)`) protege contra a exclusão de um autor que **ainda possui livros associados**. Como não há dependências, o `DELETE` é permitido normalmente. Caso houvesse pelo menos um livro com esse `autor_id`, o MariaDB negaria a operação com erro de violação de chave estrangeira, a menos que a restrição fosse definida com `ON DELETE CASCADE` (não foi o caso aqui).

### Bloco C: Administração e Privilégios Avançados

#### Desafio 12: Criação de usuário restrito para relatórios
**Objetivo:** Crie um usuário chamado `relatorios` com senha `Relatorios2026!`, concedendo privilégio de `SELECT` exclusivamente sobre a tabela `livros` do banco `biblioteca`.

**Comandos SQL (executados como root):**

```sql
CREATE USER 'relatorios'@'%' IDENTIFIED BY 'Relatorios2026!';
GRANT SELECT ON biblioteca.livros TO 'relatorios'@'%';
FLUSH PRIVILEGES;
```

#### Desafio 13: Teste de restrição de visibilidade
**Objetivo:** Conecte-se com o usuário `relatorios`, tente consultar a tabela `autores` e transcreva a mensagem de erro emitida pelo SGBD, explicando o motivo do bloqueio.

**Teste executado (conexão com usuário `relatorios`):**

```sql
USE biblioteca;
SELECT * FROM autores;
```

**Mensagem de erro emitida:**

```text
SQL Error [1142] [42000]: SELECT command denied to user 'relatorios'@'...' for table 'autores'
```

**Explicação do motivo:**  
O usuário `relatorios` recebeu privilégios apenas para `SELECT` na tabela **específica** `biblioteca.livros`. Não foi concedido nenhum privilégio sobre a tabela `autores` nem sobre todo o banco `biblioteca.*`. Por isso, ao tentar acessar `autores`, o MariaDB nega o acesso, aplicando rigorosamente o **princípio do menor privilégio**. O usuário só consegue visualizar exatamente o que foi explicitamente autorizado.

#### Desafio 14: Concessão e revogação dinâmica de privilégios
**Objetivo:** Conectado como `root`, conceda privilégio de `INSERT` na tabela `livros` para o usuário `relatorios`. Realize uma inserção de teste com sucesso e, em seguida, revogue o privilégio via `REVOKE`. Descreva discursivamente o resultado de tentar inserir novamente após a revogação.

**Procedimento:**

1. **Concessão (como root):**
```sql
GRANT INSERT ON biblioteca.livros TO 'relatorios'@'%';
FLUSH PRIVILEGES;
```

2. **Teste com INSERT (conectado como relatorios):**
```sql
USE biblioteca;
INSERT INTO livros (titulo, ano_publicacao, preco, autor_id) 
VALUES ('Livro Teste Relatorios', 2026, 19.90, 1);
```
**Resultado:** Inserção realizada com **sucesso**.

3. **Revogação (como root):**
```sql
REVOKE INSERT ON biblioteca.livros FROM 'relatorios'@'%';
FLUSH PRIVILEGES;
```

4. **Teste novamente com INSERT (conectado como relatorios):**
```sql
INSERT INTO livros (titulo, ano_publicacao, preco, autor_id) 
VALUES ('Outro Livro Teste', 2026, 24.90, 1);
```

**Resultado após revogação:**  
A inserção foi **negada** pelo MariaDB, retornando erro de permissão (sem privilégio `INSERT` para essa tabela). Após a revogação, o usuário `relatorios` voltou a ter **apenas** o privilégio `SELECT` em `biblioteca.livros`, exatamente como foi originalmente concedido. Isso demonstra a **flexibilidade e o controle granular** que o SGBD oferece para gerenciar privilégios dinamicamente, sem necessidade de recriar o usuário.

#### Desafio 15: Script idempotente de automação (setup.sql)
**Objetivo:** Desenvolva um script SQL completo chamado `setup.sql` que recrie do zero todo o banco de dados `biblioteca`, suas tabelas, restrições, usuários (`app_biblioteca`, `consulta`) com privilégios e a carga de dados. Versiona esse arquivo no seu repositório pessoal no GitHub.

**Arquivo versionado em:** [https://github.com/pauloandrehxh/tarefas-bd/blob/main/setup.sql](https://github.com/pauloandrehxh/tarefas-bd/blob/main/setup.sql)

O script foi desenvolvido com comandos idempotentes (`DROP DATABASE IF EXISTS`, `CREATE DATABASE IF NOT EXISTS`, `DROP USER IF EXISTS`, `CREATE USER IF NOT EXISTS`, etc.), recriando todo o ambiente do zero de forma automatizada e segura.

## 5. Considerações Finais

Toda a tarefa foi executada seguindo rigorosamente o enunciado `tarefa-docker-sgbd.md`. 

**Destaques da prática:**

- Ambiente provisionado com **Docker Compose** (MariaDB 11 + CloudBeaver)
- Comunicação entre contêineres via **rede interna Docker** utilizando o nome do serviço `mariadb`
- Aplicação do **princípio do menor privilégio** com usuários restritos
- Demonstração prática do **erro 1142** e da **integridade referencial**
- Uso de **IA Generativa** para povoamento expandido
- Todos os **15 desafios** dos Blocos A, B e C foram realizados
- Infraestrutura versionada **exclusivamente** no repositório pessoal público
- Relatório entregue **apenas** neste arquivo `database/20262/pauloandrehxh/tarefa03.md` no fork do `bsi-tasks`

**Repositório pessoal com infraestrutura:** [https://github.com/pauloandrehxh/tarefas-bd](https://github.com/pauloandrehxh/tarefas-bd)
