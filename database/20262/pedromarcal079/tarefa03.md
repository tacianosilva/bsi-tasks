# Tarefa 03

## Identificação e repositório
* Nome: Pedro William Azevedo Marçal de Araujo
* Usuário GitHub: pedromarcal079
* E-mail acadêmico: pedro.marcal.079@ufrn.edu.br
* Link repositório pessoal: https://github.com/pedromarcal079/tarefas-bd

## Perguntas discursivas

### Pergunta Discursiva 1: Diferença entre DDL e DML, e impacto de um DROP TABLE.

Comandos DDL (como `CREATE TABLE`) servem para definir a estrutura do banco de dados, criando a "planta" ou o "molde" onde as informações serão guardadas. Já os comandos **DML** (como `INSERT`) servem para manipular os dados concretos armazenados dentro dessa estrutura. 
Se executarmos o comando `DROP TABLE`, a estrutura da tabela é destruída e todos os dados que estavam salvos nela são eliminados permanentemente, junto com os seus índices e dependências.

### Pergunta Discursiva 2: Análise do erro 1142 ao tentar DROP TABLE com usuário restrito e relação com o princípio do menor privilégio.

O MariaDB recusou o comando `DROP TABLE` com o Erro 1142 porque a conta `app_biblioteca` recebeu privilégios limitados apenas para manipulação de dados (`SELECT`, `INSERT`, `UPDATE`, `DELETE`), sem permissão para alterar a estrutura do banco (como `DROP` ou `ALTER`).
Essa restrição segue o princípio do menor privilégio. Se a aplicação web for invadida por uma vulnerabilidade ou sofrer um erro de programação, o atacante ou a falha não conseguirá apagar tabelas inteiras ou derrubar o banco de dados, protegendo a integridade da aplicação.

### Pergunta Discursiva 3: Justificativa técnica para o uso do host '%' em vez de 'localhost' na arquitetura conteinerizada do Docker.

No MariaDB, o host `'localhost'` permite conexões apenas vindas de dentro do próprio contêiner do banco. Como a aplicação e o CloudBeaver rodam em outros contêineres separados dentro da rede do Docker, a conexão chega ao MariaDB com um IP virtual de rede.
O caractere curinga `'%'` permite que o usuário se conecte a partir de qualquer endereço IP da rede. A rede interna do Docker conecta esses contêineres de forma isolada do mundo externo, garantindo que o banco aceite as conexões das aplicações vizinhas com segurança.

### Pergunta Discursiva 4: Relato sobre o povoamento expandido gerado com IA (quantidade final de registros) e o que ocorre ao tentar associar livro a autor inexistente (integridade referencial).

Após a carga expandida, o banco ficou com um total de 14 autores (4 iniciais + 10 novos) e 25 livros cadastrados.
Se tentarmos inserir um livro com `autor_id = 999`, o MariaDB rejeitará a inserção com um erro. A regra que impede essa ação é a restrição de Chave Estrangeira (Foreign Key), que garante a integridade referencial exigindo que todo `autor_id` informado na tabela de livros já exista previamente na tabela de autores.

### Pergunta Discursiva 5: Análise das consultas relacionais e vantagens de normalizar dados em tabelas separadas (autores e livros) em vez de duplicar textos.

A principal vantagem de separar os dados é **evitar a duplicidade e facilitar a manutenção** (normalização). Se o nome ou o país de um autor mudarem, a alteração precisa ser feita em apenas **uma linha** na tabela de autores, em vez de atualizar centenas de registros duplicados na tabela de livros. 
Além disso, economiza-se espaço de armazenamento e evita-se incoerências nos dados (como um mesmo autor ter o país escrito de formas diferentes em livros distintos).

---
## Respostas Dissertativas Conceituais

### Questão a: Por que uma aplicação comercial nunca deve se conectar ao banco de dados utilizando o usuário root? O que pode ocorrer com o servidor de banco de dados caso as credenciais do usuário da aplicação sejam vazadas?

Uma aplicação comercial jamais deve utilizar a conta `root` porque esse usuário possui privilégios irrestritos sobre o servidor de banco de dados. 
Caso as credenciais da aplicação sejam vazadas (seja por SQL Injection, vazamento de código ou invasão do servidor web), um atacante com acesso `root` ganha controle total. Ele pode apagar todos os bancos de dados, criar novos usuários maliciosos, modificar configurações globais do sistema e até executar comandos no sistema operacional hospedeiro, causando perda catastrófica de dados ou paralisação completa dos serviços.

### Questão b: Qual é a diferença fundamental entre privilégios DDL (Data Definition Language) e DML (Data Manipulation Language)? Por que é uma boa prática de segurança separá-los em contas de usuários distintas?

A diferença fundamental é a abrangência de ação: comandos DDL (`CREATE`, `ALTER`, `DROP`) modificam a estrutura e a arquitetura do banco, enquanto comandos DML (`SELECT`, `INSERT`, `UPDATE`, `DELETE`) apenas consultam e manipulam os dados contidos dentro das tabelas existentes.
Separar esses privilégios em contas distintas garante que a conta usada no dia a dia da aplicação tenha permissão estritamente para operar dados (DML). Dessa forma, mesmo que uma brecha de segurança ocorra no código da aplicação, o atacante não terá autorização para alterar ou apagar a estrutura das tabelas (DDL).

### Questão c: Por que o arquivo .env.example deve ser commitado no repositório de código enquanto o arquivo .env nunca deve ser versionado? Quais são os riscos e consequências práticas de comitar credenciais reais em um repositório público no GitHub?

O arquivo `.env.example` serve como um modelo que documenta quais variáveis de ambiente o projeto precisa para rodar, contendo apenas valores genéricos e sem dados sensíveis. Por isso, ele deve ser versionado no repositório. Já o arquivo `.env` contém as credenciais reais e secretas de um ambiente específico e nunca deve ir para o controle de versão.
Vazar credenciais reais em repositórios públicos no GitHub expõe a infraestrutura a bots que varrem a rede em busca de senhas expostas. As consequências variam desde o roubo e sequestro de dados (ransomware) até o uso indevido de recursos em nuvem, gerando altos prejuízos financeiros e violações de privacidade (como a LGPD).

### Questão d: O uso do arquivo .env e a inclusão no .gitignore eliminam por completo todos os riscos de segurança de credenciais em um ambiente de desenvolvimento e produção? Justifique sua resposta considerando que o arquivo permanece armazenado em texto puro no sistema de arquivos do servidor.

Não, o uso do `.env` e do `.gitignore` não elimina todos os riscos de segurança. O `.gitignore` apenas impede que as senhas sejam enviadas para o repositório Git, mas o arquivo `.env` continua armazenado em texto puro (*plain text*) no sistema de arquivos do servidor.
Se um invasor conseguir acesso direto ao servidor (via acesso SSH comprometido, leitura indevida de arquivos por brechas na aplicação web ou backups desprotegidos), ele poderá ler as senhas no `.env` facilmente. Em ambientes de produção de alta segurança, recomenda-se utilizar cofres de segredos (*Secret Managers* como HashiCorp Vault, AWS Secrets Manager ou Azure Key Vault) em vez de arquivos de texto simples

### Questão e: O que é um contêiner e quais são as principais vantagens de utilizar o Docker para provisionar ambientes de banco de dados em atividades didáticas de graduação em comparação com a instalação manual do SGBD diretamente no sistema operacional do computador do aluno?

Um contêiner é uma unidade padronizada de software que empacota o código de uma aplicação junto com todas as suas dependências e bibliotecas necessárias, rodando de forma isolada sobre o sistema operacional.
Em atividades didáticas, as principais vantagens de usar o Docker em vez da instalação manual são:
* Padronização do ambiente: Todos os alunos utilizam exatamente a mesma versão do banco e a mesma configuração, eliminando o clássico problema do "na minha máquina funciona".
* Isolamento e facilidade de limpeza: Não polui o sistema operacional do aluno com serviços pesados rodando em segundo plano.
* Agilidade no provisionamento: Permite subir ou destruir um banco de dados completo em poucos segundos via terminal, sem a necessidade de passar por instaladores complexos ou ajustar variáveis de ambiente do sistema operacional manualmente.

---

## Desafios Realizados

### Bloco A - Docker e Infraestrutura de Ambiente

### 1. Alteração de porta do SGBD: Altere a variável MARIADB_PORT no .env para a porta 3307. Reinicie o serviço e explique como você reconfigurou a conexão do CloudBeaver para acessar o banco na porta alterada.
Após alterar a variável `MARIADB_PORT=3307` no arquivo `.env`, o serviço foi reiniciado com os seguintes comandos:

```bash
docker compose down -v
docker compose up -d
```

Inicialmente, a conexão no CloudBeaver falhou ao tentar utilizar a porta externa `3307`. 

Para investigar o motivo, foi executado o comando de inspeção dos contêineres:

```bash
docker compose ps
```

O retorno informou o mapeamento de portas: `0.0.0.0:3307->3306/tcp`.

A porta externa `3307` serve exclusivamente para conexões vindas de fora da rede Docker (como aplicações rodando no sistema operacional hospedeiro). Como o CloudBeaver está executando dentro de um contêiner na **mesma rede virtual do Docker Compose**, a comunicação entre os contêineres ocorre diretamente de forma interna.

Portanto, o CloudBeaver deve continuar se conectando à porta interna padrão do MariaDB (**`3306`**) utilizando o nome do serviço (`mariadb`) como Host. Ao manter a porta `3306` nas configurações da conexão no CloudBeaver, o acesso foi restabelecido com sucesso.

---
### 2. Dois ambientes simultâneos: Configure duas pastas distintas no seu computador com arquivos docker-compose.yml e portas/volumes desacoplados. Explique como você garantiu que quatro contêineres rodassem em paralelo sem conflito de portas ou nomes.
Para executar duas instâncias completas (totalizando 4 contêineres: 2 x MariaDB e 2 x CloudBeaver) em paralelo na mesma máquina, foi necessário garantir o desacoplamento de portas, nomes de contêineres e volumes entre os dois projetos.

#### Configurações Ajustadas

1. **Arquivo `.env` (Segundo Projeto):**
   * Redefinição das variáveis para evitar colisão de credenciais e portas no host:
     * `MARIADB_ROOT_PASSWORD`
     * `MARIADB_DATABASE`
     * `MARIADB_PORT` (ex: configurada para uma nova porta no host, como `3308`)
     * `CLOUDBEAVER_PORT` (ex: configurada para `9090`)

2. **Arquivo `docker-compose.yml` (Segundo Projeto):**
   * **Nomes dos Contêineres:** Alteração da diretiva `container_name` nos serviços para evitar nomes duplicados no Docker daemon.
   * **Mapeamento de Portas:**
     * **MariaDB:** Mapeada a nova porta externa definida no `.env`.
     * **CloudBeaver:** Ajustado o mapeamento da porta do host para evitar conflito com a porta padrão `8978`:
       ```yaml
       ports:
         - "${CLOUDBEAVER_PORT:-9090}:8978"
       ```
   * **Volumes:** Renomeados os volumes nomeados (ex: `mariadb_data_2`) para isolar a persistência de dados de cada banco.

Após aplicar esses ajustes e executar `docker compose up -d` na pasta do segundo projeto, ambos os ambientes subiram simultaneamente sem conflitos de portas ou nomes.
---
### 3. Persistência do volume e alteração de senha de root: Altere o valor de MARIADB_ROOT_PASSWORD no arquivo .env para uma nova senha qualquer. Execute docker compose up -d e observe que a autenticação antiga continua válida enquanto a nova falha. Explique detalhadamente por que isso ocorre e quais são os dois caminhos possíveis para aplicar uma nova senha de root.

A variável `MARIADB_ROOT_PASSWORD` é utilizada apenas durante o processo de inicialização inicial da imagem, quando o diretório do volume `/var/lib/mysql` ainda se encontra completamente vazio. Nesse momento, o script de entrypoint cria o banco de dados interno e armazena o hash da senha na tabela `mysql.user`.

Nas execuções subsequentes de `docker compose up -d`, o container identifica que os arquivos do banco de dados já existem no volume persistente (`mariadb_data`). Por razões de segurança e para evitar sobrescrever acidentalmente dados existentes, a imagem ignora qualquer nova variável de senha passada via ambiente e carrega as credenciais e estados persistidos anteriormente no volume.


1. Caminho 1: Recriação completa com perda de dados (Ambiente de Desenvolvimento)
   ```bash
   docker compose down -v
   docker compose up -d
   ```

2. Caminho 2: Atualização via SQL mantendo a persistência (Ambiente de Produção)
   ```sql
   ALTER USER 'root'@'%' IDENTIFIED BY 'nova_senha123';
   FLUSH PRIVILEGES;
   ```

---
### 4. Comportamento da validação estrita (:?): Apague temporariamente o arquivo .env (ou comente a linha da senha de root) e execute docker compose up -d. Documente a mensagem de erro emitida pelo Compose e explique discursivamente a importância do modificador :? em ambientes profissionais.


```bash
mv .env .env.bak
docker compose up -d
```

#### Mensagem de Erro Emitida pelo Compose
```text
error while interpolating services.mariadb.environment.MARIADB_ROOT_PASSWORD: required variable MARIADB_ROOT_PASSWORD is missing a value: defina MARIADB_ROOT_PASSWORD no arquivo .env
```

O modificador `:?` é um operador de validação estrita no Docker Compose que exige a definição de um valor para a variável de ambiente, abortando a execução imediatamente com uma mensagem customizada caso a variável seja nula ou esteja ausente.

Em ambientes profissionais e pipelines de Integração Contínua / Implantação Contínua (CI/CD):
* **Princípio de Falha Rápida:** Impede que a infraestrutura seja provisionada em estado inconsistente ou sem parâmetros críticos de configuração.
* **Segurança:** Evita que contêineres de banco de dados iniciem com senhas padrão vazias ou fracas inadvertidamente.
* **Diagnóstico Claro:** Fornece um feedback direto e descritivo para os operadores de infraestrutura, eliminando horas de investigação sobre falhas silenciosas de aplicação.

--- 
### 5. Inspeção de variáveis no compose: Execute docker compose config no terminal e liste três variáveis de ambiente que foram resolvidas e interpoladas a partir do .env.


```bash
docker compose config
```

#### Variáveis Resolvidas a partir do `.env`

Abaixo estão listadas três variáveis de ambiente interpoladas e resolvidas após o processamento do arquivo `.env`:

1. **`MARIADB_ROOT_PASSWORD`**
   * **Valor Resolvido:** `sua_senha_configurada`
   * **Seção no Compose:** `services.mariadb.environment.MARIADB_ROOT_PASSWORD`
   * **Função:** Injeta a senha de administração do superusuário do MariaDB durante a primeira inicialização.

2. **`MARIADB_DATABASE`**
   * **Valor Resolvido:** `labdb` *(resolvido via valor padrão `:-labdb` ou especificado no `.env`)*
   * **Seção no Compose:** `services.mariadb.environment.MARIADB_DATABASE`
   * **Função:** Define o nome do banco de dados relacional que será criado automaticamente na subida inicial da instância.

3. **`MARIADB_PORT`**
   * **Valor Resolvido:** `3306` (ou `3307` conforme configurado para evitar conflitos na máquina host)
   * **Seção no Compose:** `services.mariadb.ports` (Mapeamento `3307:3306`)
   * **Função:** Determina a porta da máquina hospedeira (*host*) redirecionada para a porta interna do contêiner.


--- 

### Bloco B - Modelagem e Consultas SQL Básicas

6. 

```sql
CREATE TABLE emprestimos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    livro_id INT,
    data_emprestimo DATE,
    devolvido BOOLEAN,
    FOREIGN KEY (livro_id) REFERENCES livros(id)
);
```
7. 
```sql
INSERT INTO emprestimos (livro_id, data_emprestimo, devolvido) VALUES 
(1, '2026-10-15', FALSE),
(2, '2026-10-20', FALSE),
(3, '2026-10-25', TRUE);
```
8. 
```sql
SELECT
    l.titulo, 
    e.data_emprestimo, 
    a.nome AS autor
    FROM emprestimos e
    JOIN livros l ON e.livro_id = l.id
    JOIN autores a ON l.autor_id = a.id
    WHERE e.devolvido = FALSE;
```
9. 
```sql
SELECT 
    a.nome AS autor, 
    COUNT(l.id) AS total_livros
    FROM autores a
    JOIN livros l ON a.id = l.autor_id
    GROUP BY a.id, a.nome
    HAVING COUNT(l.id) > 1;
```
10. 
```sql
SELECT id, titulo, preco FROM livros WHERE id = 1;
UPDATE livros SET preco = preco * 1.10 WHERE id = 1;
SELECT id, titulo, preco FROM livros WHERE id = 1;
```
11. 
```sql
INSERT INTO autores (nome, pais, ano_nascimento) VALUES ('teste', 'brasil', 1999);
SELECT id, nome FROM autores WHERE nome = 'teste';
DELETE FROM autores WHERE nome = 'teste';
```