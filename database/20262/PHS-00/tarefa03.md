# Tarefa 03 - Docker Compose, MariaDB e Administração de SGBD

## 1. Identificação e Repositório

- **Nome completo:** Pedro Henrique da Silva
- **Usuário no GitHub:** PHS-00
- **E-mail acadêmico:** pedro.silva.437@ufrn.edu.br
- **Repositório Pessoal Público:** [Link para o repositório](https://github.com/PHS-00/bsi-tasks/tree/tarefa03/PHS-00)

---

## 2. Respostas às Perguntas Discursivas dos Passos Práticos

### Pergunta Discursiva 1
**Diferença entre criar uma tabela (DDL) e inserir registros nessa tabela (DML), e o que ocorre com `DROP TABLE`:**  
Criar uma tabela por meio de **DDL** (*Data Definition Language*, como `CREATE TABLE`) significa definir a estrutura física e lógica do armazenamento: o nome da entidade, suas colunas, os tipos de dados suportados e as regras de integridade (chaves primárias e estrangeiras). Já inserir registros via **DML** (*Data Manipulation Language*, como `INSERT INTO`) consiste em manipular o conteúdo propriamente dito, preenchendo linhas (tuplas) dentro da estrutura previamente moldada. Caso uma tabela seja removida com o comando DDL `DROP TABLE`, tanto a estrutura quanto todos os registros armazenados nela são excluídos permanentemente do banco de dados (a menos que exista um backup externo).

### Pergunta Discursiva 2
**Execução de `DROP TABLE autores` com `app_biblioteca`, erro 1142 e princípio do menor privilégio:**  
Ao tentar executar `DROP TABLE autores` conectado com o usuário `app_biblioteca`, o MariaDB bloqueou a instrução e retornou o erro `SQL Error [1142] [42000]: DROP command denied to user 'app_biblioteca'@'...' for table 'autores'`. Isso ocorreu porque essa conta recebeu exclusivamente privilégios DML (`SELECT`, `INSERT`, `UPDATE` e `DELETE`), não possuindo direitos estruturais (DDL). Essa restrição aplica o **princípio do menor privilégio** e protege o banco de dados em cenários de falha de programação ou ataques de *SQL Injection*: mesmo que um invasor comprometa as credenciais usadas pela aplicação web, ele não conseguirá destruir tabelas, alterar esquemas ou derrubar a estrutura do banco.

### Pergunta Discursiva 3
**Uso do host `'%'` em vez de `'localhost'` na arquitetura conteinerizada do Docker:**  
No MariaDB e no MySQL, a identidade de um usuário é composta pelo par `'usuario'@'host'`. O host `'localhost'` restringe a autenticação apenas a conexões originadas internamente no próprio sistema operacional/contêiner do banco via loopback ou socket UNIX. Como o CloudBeaver e eventuais aplicações executam em contêineres isolados dentro de uma rede virtual bridge gerenciada pelo Docker Compose, cada contêiner possui seu próprio endereço IP interno nessa sub-rede. Assim, o uso do curinga `'%'` é necessário para autorizar que conexões vindas de outros contêineres da rede Docker sejam autenticadas pelo SGBD.

### Pergunta Discursiva 4
**Povoamento expandido com IA e tentativa de inserção com `autor_id = 999`:**  
Após a execução da carga inicial somada ao script `povoamento.sql` gerado com auxílio de IA generativa, a base de dados passou a contar com **14 autores** e **31 livros** cadastrados. Caso se tente inserir um livro com `autor_id = 999` (um identificador inexistente na tabela `autores`), o MariaDB rejeita a operação com erro de violação de chave estrangeira (`ERROR 1452: Cannot add or update a child row: a foreign key constraint fails`). A regra que impede essa ação é a **integridade referencial**, imposta pela restrição `FOREIGN KEY (autor_id) REFERENCES autores(id)`, que garante que todo livro esteja vinculado a um autor válido já existente.

### Pergunta Discursiva 5
**Vantagem de normalizar dados em tabelas relacionadas (`autores` e `livros`):**  
Dividir os dados em duas tabelas relacionadas evita a repetição redundante de informações textuais (como nome, país e ano de nascimento do autor) em cada linha da tabela `livros`. Na prática, essa modelagem economiza espaço de armazenamento, facilita a manutenção — pois a correção do nome ou nacionalidade de um autor precisa ser feita em apenas um único registro na tabela `autores` (evitando anomalias de atualização) — e garante consistência semântica nos agrupamentos e junções (`JOIN` e `GROUP BY`).

---

## 3. Respostas Dissertativas Conceituais

### Questão a
**Por que uma aplicação comercial nunca deve se conectar usando `root` e riscos do vazamento de credenciais:**  
O usuário `root` é o superadministrador do SGBD, possuindo controle irrestrito sobre todos os bancos de dados, tabelas, logs, configurações do servidor e gerenciamento de contas. Se uma aplicação comercial utilizar o `root` e suas credenciais vazarem (por falha de código, exposição de logs ou invasão do servidor web), o atacante terá acesso total para ler dados confidenciais de outros sistemas hospedados no mesmo servidor, adulterar registros financeiros, criar contas administrativas ocultas ou apagar irreversivelmente toda a base de dados da empresa.

### Questão b
**Diferença fundamental entre privilégios DDL e DML e importância de separá-los:**  
Privilégios **DDL** (`CREATE`, `ALTER`, `DROP`) concedem poder para criar, modificar ou destruir a arquitetura lógica do banco (bancos, tabelas, índices e restrições). Privilégios **DML** (`SELECT`, `INSERT`, `UPDATE`, `DELETE`) permitem apenas consultar e manipular os registros armazenados dentro das estruturas existentes. Separá-los em contas distintas é uma boa prática de segurança porque a aplicação em produção precisa apenas ler e gravar dados rotineiros (DML), enquanto alterações estruturais (DDL) devem ocorrer apenas durante janelas controladas de implantação (*deploy* ou *migrations*) sob contas administrativas específicas.

### Questão c
**Por que `.env.example` deve ser versionado, `.env` nunca deve ser versionado e riscos de expor credenciais no GitHub:**  
O arquivo `.env.example` funciona como documentação técnica para que outros desenvolvedores saibam quais variáveis de ambiente o sistema exige, contendo apenas valores fictícios. Já o `.env` guarda segredos reais da instância local ou de produção e jamais deve ser commitado. Comitar credenciais reais em um repositório público no GitHub expõe senhas e chaves de acesso imediatamente na internet; robôs automatizados varrem commits públicos em segundos para capturar credenciais, permitindo invasões, sequestro de dados (*ransomware*) ou uso indevido de recursos, além de o segredo permanecer registrado no histórico do Git mesmo após um commit posterior de remoção.

### Questão d
**O uso de `.env` + `.gitignore` elimina por completo todos os riscos de segurança de credenciais?**  
Não. Embora impeça o vazamento acidental via controle de versão Git, o arquivo `.env` permanece armazenado em **texto puro** (*plaintext*) no sistema de arquivos do servidor ou da máquina do desenvolvedor. Caso um invasor obtenha acesso de leitura ao sistema operacional (por falha em outra aplicação, permissões mal configuradas de diretório ou backup desprotegido), ele poderá ler diretamente o conteúdo do `.env`. Em ambientes corporativos de produção, recomenda-se complementar essa prática com cofres de segredos (*Secret Managers*, como HashiCorp Vault, AWS Secrets Manager ou Docker Secrets), criptografia em repouso e rotação periódica de senhas.

### Questão e
**O que é um contêiner e vantagens do Docker na graduação frente à instalação manual do SGBD:**  
Um contêiner é uma unidade leve e isolada de execução que empacota uma aplicação juntamente com suas bibliotecas, dependências e configurações, compartilhando o kernel do sistema operacional hospedeiro. Na graduação, o uso do Docker elimina problemas clássicos de incompatibilidade entre sistemas operacionais (Windows, Linux, macOS), evita conflitos de portas ou serviços residuais instalados na máquina pessoal do aluno, permite reproduzir exatamente o mesmo ambiente do professor em segundos com `docker compose up -d` e possibilita destruir e recriar bancos limpos sem poluir o sistema operacional.

---

## 4. Desafios Realizados

### Bloco A: Docker e Infraestrutura de Ambiente

#### Desafio 1 — Alteração de porta do SGBD
- **Alteração no `.env`:** `MARIADB_PORT=3307`, seguida de `docker compose up -d`.
- **Explicação da reconfiguração no CloudBeaver:** Como o CloudBeaver roda dentro da rede virtual interna do Docker Compose, a comunicação contêiner-a-contêiner continua ocorrendo pelo nome do serviço `mariadb` na porta interna `3306` (pois o mapeamento `"3307:3306"` altera apenas a porta exposta na máquina hospedeira). Já caso a conexão seja feita externamente a partir do host físico (ex.: DBeaver Desktop ou cliente CLI via `localhost`), a porta da conexão deve ser alterada de `3306` para `3307`.

#### Desafio 2 — Dois ambientes simultâneos
Para executar dois ambientes independentes em paralelo (quatro contêineres ao todo) sem conflitos, foram criadas duas pastas separadas (`ambiente1/` e `ambiente2/`), cada uma com seu próprio `docker-compose.yml` e `.env`, garantindo o desacoplamento em três níveis:
1. **Nomes de contêiner distintos:** `lab1-mariadb` / `lab1-cloudbeaver` no primeiro ambiente e `lab2-mariadb` / `lab2-cloudbeaver` no segundo.
2. **Portas de host exclusivas:** `MARIADB_PORT=3306` e `CLOUDBEAVER_PORT=8978` no ambiente 1; `MARIADB_PORT=3308` e `CLOUDBEAVER_PORT=8979` no ambiente 2.
3. **Volumes e redes isolados:** O Docker Compose isola automaticamente as redes e prefixa os volumes nomeados pelo diretório do projeto (`ambiente1_mariadb_data` e `ambiente2_mariadb_data`).

#### Desafio 3 — Persistência do volume e alteração de senha de root
- **Por que a senha antiga permanece ativa:** A variável `MARIADB_ROOT_PASSWORD` só é processada pelo script de inicialização (*entrypoint*) do contêiner na **primeira criação** do diretório de dados `/var/lib/mysql`. Como o volume `mariadb_data` já estava inicializado, os metadados de autenticação (`mysql.user`) já existiam gravados no volume e não são sobrescritos ao reiniciar o contêiner.
- **Dois caminhos para aplicar a nova senha:**
  1. **Destrutivo (reiniciando do zero):** Executar `docker compose down -v` para remover o volume persistente e subir novamente com `docker compose up -d` para aplicar a senha definida no `.env`.
  2. **Não-destrutivo (preservando os dados):** Conectar ao banco com a senha antiga e executar `ALTER USER 'root'@'%' IDENTIFIED BY 'NovaSenha'; ALTER USER 'root'@'localhost' IDENTIFIED BY 'NovaSenha'; FLUSH PRIVILEGES;`, atualizando em seguida o `.env`.

#### Desafio 4 — Comportamento da validação estrita (`:?`)
- **Comando executado:** `docker compose up -d` (com o `.env` removido ou `MARIADB_ROOT_PASSWORD` comentada).
- **Mensagem de erro emitida:**
  ```text
  error while interpolating services.mariadb.environment.MARIADB_ROOT_PASSWORD: required variable MARIADB_ROOT_PASSWORD is missing a value: defina MARIADB_ROOT_PASSWORD no arquivo .env
  ```
- **Importância em produção:** O modificador `:?` impõe o comportamento *fail-fast* (falha imediata), impedindo que o orquestrador suba serviços críticos com variáveis obrigatórias vazias, senhas em branco ou configurações inseguras por omissão.

#### Desafio 5 — Inspeção de variáveis no compose
- **Comando executado:** `docker compose config`
- **Três variáveis resolvidas e interpoladas a partir do `.env`:**
  1. `MARIADB_ROOT_PASSWORD: RootLab2026!aB`
  2. `MARIADB_DATABASE: labdb`
  3. Mapeamento de portas interpolado: `"3306:3306"` (a partir de `${MARIADB_PORT:-3306}:3306`) e `"8978:8978"` (a partir de `${CLOUDBEAVER_PORT:-8978}:8978`).

---

### Bloco B: Modelagem e Consultas SQL Básicas

#### Desafio 6 — Criação da tabela de empréstimos
```sql
USE biblioteca;

CREATE TABLE IF NOT EXISTS emprestimos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  livro_id INT,
  data_emprestimo DATE,
  devolvido BOOLEAN,
  FOREIGN KEY (livro_id) REFERENCES livros(id)
);
```

#### Desafio 7 — Carga da tabela empréstimos
```sql
INSERT INTO emprestimos (livro_id, data_emprestimo, devolvido) VALUES
(1, '2026-11-01', FALSE),
(4, '2026-11-05', FALSE),
(3, '2026-10-20', TRUE);
```

#### Desafio 8 — Consulta de pendências
```sql
SELECT l.titulo AS livro, e.data_emprestimo, a.nome AS autor
FROM emprestimos e
JOIN livros l ON e.livro_id = l.id
JOIN autores a ON l.autor_id = a.id
WHERE e.devolvido = FALSE;
```

#### Desafio 9 — Filtragem de grupos com HAVING
```sql
SELECT a.nome AS autor, COUNT(l.id) AS total_livros
FROM autores a
JOIN livros l ON a.id = l.autor_id
GROUP BY a.id, a.nome
HAVING COUNT(*) > 1;
```

#### Desafio 10 — Atualização proporcional (UPDATE)
```sql
UPDATE livros
SET preco = preco * 1.10
WHERE id = 1;
```
- **Comentário sobre o resultado:** A instrução reajustou em 10% o valor exclusivamente do livro com `id = 1` (*Dom Casmurro*), elevando seu preço de `39.90` para `43.89` (`1 row affected`). O uso da cláusula `WHERE` foi essencial para evitar o reajuste acidental de toda a tabela.

#### Desafio 11 — Remoção condicional (DELETE)
```sql
INSERT INTO autores (nome, pais, ano_nascimento)
VALUES ('Autor Temporário Teste', 'Brasil', 1985);

DELETE FROM autores
WHERE nome = 'Autor Temporário Teste';
```
- **Explicação conceitual:** A remoção foi aceita pelo SGBD sem violar a restrição de chave estrangeira (`FOREIGN KEY`) porque não existia nenhum registro na tabela `livros` referenciando o `id` desse autor recém-criado. A integridade referencial só bloqueia a exclusão de um registro pai quando existem registros filhos associados a ele.

---

### Bloco C: Administração e Privilégios Avançados

#### Desafio 12 — Criação de usuário restrito para relatórios
```sql
CREATE USER 'relatorios'@'%' IDENTIFIED BY 'Relatorios2026!';
GRANT SELECT ON biblioteca.livros TO 'relatorios'@'%';
FLUSH PRIVILEGES;
```

#### Desafio 13 — Teste de restrição de visibilidade
- **Consulta executada como `relatorios`:**
  ```sql
  SELECT * FROM biblioteca.autores;
  ```
- **Mensagem de erro emitida:**
  ```text
  SQL Error [1142] [42000]: SELECT command denied to user 'relatorios'@'...' for table 'autores'
  ```
- **Motivo do bloqueio:** Os privilégios do usuário `relatorios` foram concedidos em nível granular de tabela exclusivamente sobre `biblioteca.livros`. Como o SGBD nega acesso por padrão (*default deny*) a qualquer objeto não explicitamente autorizado, a leitura da tabela `autores` foi bloqueada.

#### Desafio 14 — Concessão e revogação dinâmica de privilégios
- **Comandos executados (como `root` e teste como `relatorios`):**
  ```sql
  -- 1. Concessão temporária (como root)
  GRANT INSERT ON biblioteca.livros TO 'relatorios'@'%';
  FLUSH PRIVILEGES;

  -- 2. Inserção de teste (como relatorios - executada com sucesso)
  INSERT INTO biblioteca.livros (titulo, ano_publicacao, preco, autor_id)
  VALUES ('Livro Teste Relatórios', 2026, 25.00, 1);

  -- 3. Revogação do privilégio (como root)
  REVOKE INSERT ON biblioteca.livros FROM 'relatorios'@'%';
  FLUSH PRIVILEGES;
  ```
- **Resultado ao tentar inserir novamente após o `REVOKE`:** Ao tentar executar um novo `INSERT` na tabela `livros` com o usuário `relatorios`, o MariaDB bloqueia imediatamente a operação e retorna `SQL Error [1142] [42000]: INSERT command denied to user 'relatorios'@'...' for table 'livros'`, comprovando que a revogação de privilégios tem efeito imediato sobre as sessões e transações subsequentes.

#### Desafio 15 — Script idempotente de automação (`setup.sql`)
O script completo e idempotente `setup.sql` foi versionado no repositório pessoal público no GitHub. Ele utiliza instruções `DROP DATABASE IF EXISTS biblioteca` e `DROP USER IF EXISTS` antes de recriar o esquema `biblioteca` com codificação `utf8mb4`, as tabelas `autores`, `livros` e `emprestimos` com suas chaves primárias e estrangeiras, os usuários `app_biblioteca` e `consulta` com seus respectivos privilégios e toda a carga de registros, permitindo restabelecer o ambiente limpo a qualquer momento sem erros de duplicidade.