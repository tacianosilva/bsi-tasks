# Relatório de Execução - Tarefa 03 (Docker, MariaDB e Administração de SGBD)

## 1. Identificação e Repositório

- **Nome Completo:** Vinícius Linhares Queiroz
- **Usuário GitHub:** ViniciusL07
- **E-mail Acadêmico:** vinicius.linhares.702@ufrn.edu.br
- **Repositório Pessoal Público:** https://github.com/ViniciusL07/tarefas-bd

---

## 2. Respostas às Perguntas Discursivas dos Passos Práticos

### Pergunta Discursiva 1
Comandos **DDL** (*Data Definition Language*) manipulam a **estrutura** dos dados (criação, alteração ou exclusão de bancos, tabelas e colunas). Comandos **DML** (*Data Manipulation Language*) operam sobre os **dados contidos** nessas estruturas (inserção, alteração, remoção e consulta de registros). Se apagarmos uma tabela com `DROP TABLE` (comando DDL), o esquema e a tabela inteira são excluídos do sistema gerenciador, e **todos os dados** contidos dentro dela são destruídos permanentemente.

### Pergunta Discursiva 2
Ao tentar executar `DROP TABLE autores` com a conta `app_biblioteca`, o MariaDB rejeitou a instrução emitindo o erro `1142` porque a essa conta só foram concedidas permissões DML (`SELECT`, `INSERT`, `UPDATE`, `DELETE`). O princípio do menor privilégio garante que a aplicação execute apenas as operações cotidianas estritamente necessárias. Caso a aplicação web passe por uma vulnerabilidade (como SQL Injection), um invasor não conseguirá alterar a estrutura nem apagar tabelas do banco de dados.

### Pergunta Discursiva 3
Os usuários foram criados com o host `'%'` porque, na arquitetura conteinerizada do Docker Compose, a aplicação cliente (como a interface web CloudBeaver) executa dentro de seu próprio contêiner, possuindo um IP diferente na sub-rede virtual. Se o usuário fosse criado como `'localhost'`, o MariaDB aceitaria conexões originadas apenas de dentro de seu próprio contêiner via socket interno, bloqueando o acesso de outros contêineres e serviços na rede virtual.

### Pergunta Discursiva 4
Após a execução da carga expandida via IA generativa, a base ficou com um total de **14 autores** e **30 livros** cadastrados. Se tentássemos inserir um livro cujo `autor_id` fosse `999` (inexistente), o SGBD recusaria a operação exibindo erro de integridade referencial. A regra que impede isso é a **Chave Estrangeira (Foreign Key)** declarada na tabela `livros`, garantindo que todo registro em `livros.autor_id` corresponda a um `id` válido previamente existente na tabela `autores`.

### Pergunta Discursiva 5
A grande vantagem da normalização (separar em tabelas relacionais `autores` e `livros`) é eliminar a redundância e impedir anomalias de atualização. Se guardássemos nome e país do autor em cada linha da tabela de livros, qualquer mudança no país de um autor exigiria atualizar centenas de registros duplicados, abrindo margem para inconsistências de dados e desperdício de espaço em memória/disco.

---

## 3. Respostas Dissertativas Conceituais

### Questão A
Uma aplicação comercial jamais deve utilizar a conta `root` porque essa conta possui controle irrestrito e privilégios administrativos globais (como apagar bases, criar usuários, alterar esquemas ou até executar comandos no sistema). Se as credenciais da aplicação vazarem, um invasor ganhará controle total sobre o servidor e todas as bases de dados hospedadas nele.

### Questão B
Privilégios DDL administram o esquema e a arquitetura das estruturas (ex: `CREATE`, `ALTER`, `DROP`), enquanto DML gerencia os registros contidos nas tabelas (ex: `SELECT`, `INSERT`, `UPDATE`, `DELETE`). A separação garante o princípio do menor privilégio, garantindo que usuários operacionais e microsserviços não alterem ou destruam acidentalmente o modelo de dados.

### Questão C
O arquivo `.env.example` funciona como uma documentação de contrato técnico, contendo apenas o nome das variáveis necessárias e valores genéricos/fictícios, sendo seguro versioná-lo. Já o `.env` guarda credenciais reais da máquina local ou produção. Versionar o `.env` em um repositório público expõe dados sensíveis a robôs de varredura (ciberataques), comprometendo a segurança da infraestrutura.

### Questão D
Não, usar `.env` e `.gitignore` isola apenas o versionamento via Git. O arquivo continua salvo em texto puro no sistema de arquivos do servidor. Se o servidor sofrer acesso indevido, leitura local de arquivos por falha de aplicação (LFI) ou permissões de leitura incorretas no SO, as credenciais ainda poderão ser lidas. Em produção, utilizam-se cofres de segredos (*Secret Managers* ou *Docker Secrets*).

### Questão E
Um contêiner é um ambiente isolado em nível de processo que empacota uma aplicação e todas as suas dependências. A vantagem em disciplinas acadêmicas em relação à instalação manual é a portabilidade e a padronização do ambiente: evita divergências de versões entre sistemas operacionais dos alunos, dispensa a poluição do SO com instalações nativas e permite subir/destruir um banco completo via linha de comando sem conflitos.

---

## 4. Desafios Realizados

### Bloco A: Docker e Infraestrutura de Ambiente

1. **Alteração de porta do SGBD:**
   - **Procedimento:** A variável `MARIADB_PORT` no arquivo `.env` foi alterada para `3307`. Em seguida, executou-se o comando:
     ```bash
     docker compose up -d
     ```
   - **Reconfiguração no CloudBeaver:** Na interface do CloudBeaver (que opera dentro da rede virtual interna do Docker), o host e a porta de conexão permaneceram como `mariadb:3306`, pois os contêineres continuam se comunicando pela porta interna. A porta `3307` passa a ser exigida apenas para conexões diretas vindas do sistema operacional host (`localhost:3307`).

2. **Dois ambientes simultâneos:**
   - **Solução:** Foram criadas duas pastas independentes no sistema operacional. Para evitar conflitos de portas e nomes de contêineres, definiram-se portas distintas no host (ex.: `MARIADB_PORT=3306` na pasta A e `MARIADB_PORT=3307` na pasta B) e nomes explícitos no `container_name` do `docker-compose.yml` de cada projeto, permitindo a execução simultânea dos 4 contêineres.

3. **Persistência do volume e alteração de senha de root:**
   - **Causa da falha:** O script de *entrypoint* da imagem oficial do MariaDB só processa a variável `MARIADB_ROOT_PASSWORD` durante a **primeira inicialização** do volume de dados (`/var/lib/mysql`). Como os dados já estavam gravados no volume `mariadb_data`, alterar a variável no `.env` não altera a senha de um banco existente.
   - **Caminhos para aplicação da nova senha:**
     1. Executar a alteração manual via SQL com usuário root conectado:
        ```sql
        ALTER USER 'root'@'%' IDENTIFIED BY 'NovaSenha2026!';
        FLUSH PRIVILEGES;
        ```
     2. Recriar o volume do zero limpando a persistência antiga:
        ```bash
        docker compose down -v
        docker compose up -d
        ```

4. **Comportamento da validação estrita (`:?`):**
   - **Erro emitido:**
     ```text
     required variable MARIADB_ROOT_PASSWORD is missing: defina MARIADB_ROOT_PASSWORD no arquivo .env
     ```
   - **Importância:** O modificador `:?` garante que a execução do Docker Compose seja abortada imediatamente se a variável de senha de root não for fornecida. Em ambientes profissionais, isso previne o provisionamento acidental de bancos de dados desprotegidos ou com senhas em branco.

5. **Inspeção de variáveis no Compose:**
   - **Comando executado:**
     ```bash
     docker compose config
     ```
   - **Três variáveis resolvidas a partir do `.env`:**
     - `MARIADB_ROOT_PASSWORD` resolvida para `RootLab2026!aB`
     - `MARIADB_DATABASE` resolvida para `labdb`
     - `MARIADB_PORT` resolvida para `3306`

---

### Bloco B: Modelagem e Consultas SQL Básicas

6. **Criação da tabela de empréstimos (DDL):**
   ```sql
   CREATE TABLE emprestimos (
     id INT AUTO_INCREMENT PRIMARY KEY,
     livro_id INT,
     data_emprestimo DATE,
     devolvido BOOLEAN,
     FOREIGN KEY (livro_id) REFERENCES livros(id)
   );
   ```

7. **Carga da tabela empréstimos (DML):**
   ```sql
   INSERT INTO emprestimos (livro_id, data_emprestimo, devolvido) VALUES
   (1, '2026-03-01', FALSE),
   (2, '2026-03-02', FALSE),
   (3, '2026-02-15', TRUE);
   ```

8. **Consulta de pendências:**
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

9. **Filtragem de grupos com HAVING:**
   ```sql
   SELECT 
       a.nome AS autor, 
       COUNT(l.id) AS total_livros
   FROM autores a
   JOIN livros l ON a.id = l.autor_id
   GROUP BY a.id, a.nome
   HAVING COUNT(l.id) > 1;
   ```

10. **Atualização proporcional (UPDATE):**
    ```sql
    UPDATE livros 
    SET preco = preco * 1.10 
    WHERE id = 1;
    ```
    - **Resultado:** O valor da obra *Dom Casmurro* (`id = 1`) recebeu um reajuste de 10%, sendo alterado de R$ 39,90 para R$ 43,89.

11. **Remoção condicional (DELETE):**
    ```sql
    INSERT INTO autores (nome, pais, ano_nascimento) VALUES ('Autor Teste', 'Brasil', 1990);
    
    DELETE FROM autores WHERE nome = 'Autor Teste';
    ```
    - **Justificativa:** A instrução `DELETE` foi aceita sem erros porque o autor recém-criado não possuía nenhum livro associado na tabela `livros`, garantindo que nenhuma chave estrangeira fosse violada.

---

### Bloco C: Administração e Privilégios Avançados

12. **Criação de usuário restrito para relatórios:**
    ```sql
    CREATE USER 'relatorios'@'%' IDENTIFIED BY 'Relatorios2026!';
    GRANT SELECT ON biblioteca.livros TO 'relatorios'@'%';
    FLUSH PRIVILEGES;
    ```

13. **Teste de restrição de visibilidade:**
    - **Comando testado com o usuário `relatorios`:**
      ```sql
      SELECT * FROM autores;
      ```
    - **Mensagem de erro emitida:**
      ```text
      SQL Error [1142] [42000]: SELECT command denied to user 'relatorios'@'...' for table 'autores'
      ```
    - **Motivo do bloqueio:** O privilégio de leitura foi concedido de forma restrita apenas para o objeto `biblioteca.livros`. A conta não possui privilégios de acesso à tabela `autores`.

14. **Concessão e revogação dinâmica de privilégios:**
    - **Passo 1 (Concessão pelo root):**
      ```sql
      GRANT INSERT ON biblioteca.livros TO 'relatorios'@'%';
      FLUSH PRIVILEGES;
      ```
      *(Testado: inserção de registro efetuada com sucesso pelo usuário `relatorios`).*
    - **Passo 2 (Revogação pelo root):**
      ```sql
      REVOKE INSERT ON biblioteca.livros FROM 'relatorios'@'%';
      FLUSH PRIVILEGES;
      ```
    - **Resultado:** Ao tentar inserir um novo registro após o `REVOKE`, a operação foi imediatamente bloqueada pelo MariaDB emitindo novamente o erro `1142` (permissão negada).

15. **Script idempotente de automação (`setup.sql`):**
    - O script foi estruturado e versionado no repositório pessoal como `setup.sql`. Ele utiliza `DROP DATABASE IF EXISTS` e `DROP USER IF EXISTS` para garantir que o ambiente completo (banco, tabelas, FKs, usuários `app_biblioteca`, `consulta` e `relatorios`, concessão de permissões e dados iniciais) possa ser reconstruído do zero sem falhas de execução repetida.