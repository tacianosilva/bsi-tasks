# Tarefa 03 - Docker Compose, MariaDB e Administração de SGBD

**Nome:** Thiago Gomes
**GitHub:** thiagogomes1805
**Repositório Pessoal:** [Insira aqui o link do seu repositório público com o docker-compose]

## Respostas às Perguntas Discursivas

**Pergunta Discursiva 1:** Diferença entre DDL e DML, e impacto de um DROP TABLE.
**Resposta:** A DDL (Data Definition Language) é responsável por criar, alterar ou excluir a estrutura do banco de dados, como definir as tabelas e suas colunas (ex: `CREATE TABLE`). Funciona como a construção das prateleiras de uma estante. Já a DML (Data Manipulation Language) serve para manipular e consultar as informações dentro dessas estruturas (ex: `INSERT`). É o ato de colocar os livros nas prateleiras. Se executarmos um `DROP TABLE` (comando DDL destrutivo), a própria estrutura da tabela é eliminada, o que significa que todos os dados e registos guardados nela são perdidos permanentemente junto com a estrutura.

**Pergunta Discursiva 2:** Análise do erro 1142 ao tentar `DROP TABLE` com utilizador restrito e relação com o princípio do menor privilégio.
**Resposta:** O MariaDB bloqueou o comando e gerou o erro 1142 porque a conta `app_biblioteca` foi configurada exclusivamente com permissões de manipulação de dados (DML: SELECT, INSERT, UPDATE e DELETE). A conta não possui privilégios estruturais (DDL) para apagar tabelas. A aplicação deste princípio do menor privilégio garante que, caso a aplicação web sofra uma invasão ou falha grave, o invasor estará limitado a alterar os dados das tabelas permitidas, não conseguindo destruir a arquitetura fundamental do banco de dados.

**Pergunta Discursiva 3:** Justificativa técnica para o uso do host `'%'` em vez de `'localhost'` na arquitetura conteinerizada do Docker.
**Resposta:** O uso do caractere curinga `'%'` é necessário porque o CloudBeaver e o SGBD MariaDB operam em contentores isolados. Eles comunicam entre si através de uma rede virtual interna criada pelo Docker. Se utilizássemos `'localhost'`, o MariaDB esperaria que a conexão tivesse origem de dentro do seu próprio contentor (loopback). Com `'%'`, autorizamos o acesso a partir de qualquer IP da rede, o que permite que serviços externos dentro da arquitetura Docker se consigam autenticar.

**Pergunta Discursiva 4:** Relato sobre o povoamento expandido gerado com IA e a integridade referencial.
**Resposta:** Considerando o roteiro da atividade, a base ficaria com um total de 14 autores e 31 livros (os 4 autores e 6 livros iniciais, somados aos 10 autores e 25 livros gerados pela IA). Se tentássemos inserir um livro com o `autor_id` 999, o MariaDB rejeitaria a inserção com um erro. A regra que impede esta ação é a restrição de Chave Estrangeira (Foreign Key), que garante a integridade referencial: o banco de dados só permite cadastrar um livro se o identificador do autor já existir previamente na tabela de autores.

**Pergunta Discursiva 5:** Vantagens de normalizar dados em tabelas separadas.
**Resposta:** A principal vantagem de dividir os dados em duas tabelas (normalização) é evitar a repetição desnecessária de informações (redundância). Se o nome e o país estivessem na tabela de livros, teriam de ser digitados repetidamente para cada obra do mesmo autor. Ao separar, poupamos espaço de armazenamento e evitamos inconsistências. Além disso, facilita a manutenção: se for preciso corrigir o nome ou o país de um autor, basta fazer a alteração num único registo na tabela `autores`, e a atualização aplica-se logicamente a todos os livros ligados a ele.

## Respostas Dissertativas Conceituais

**Questão a:** Por que uma aplicação comercial nunca deve se conectar usando o usuário `root`?
**Resposta:** O utilizador `root` possui privilégios absolutos e irrestritos sobre todo o SGBD. Se uma aplicação utilizar o `root` e sofrer uma invasão (ou o seu código fonte for exposto), o atacante obterá o controlo total do servidor de banco de dados. Isto significa que o invasor poderá apagar bancos de dados inteiros (`DROP DATABASE`), criar novos utilizadores maliciosos, conceder permissões e comprometer completamente a segurança de todos os sistemas hospedados naquele servidor.

**Questão b:** Diferença entre privilégios DDL e DML e a prática de separá-los.
**Resposta:** Privilégios DDL (Data Definition Language) permitem modificar a estrutura do banco (criar, alterar ou apagar tabelas e esquemas). Privilégios DML (Data Manipulation Language) permitem apenas interagir com o conteúdo das tabelas (inserir, consultar, atualizar e excluir registos). É uma boa prática separá-los para garantir que a aplicação web comum apenas consiga manipular dados diários (DML), impedindo que falhas de código ou ataques de injeção destruam acidentalmente ou intencionalmente a arquitetura do banco (DDL). O acesso DDL deve ser restrito aos administradores de banco de dados (DBAs) em momentos específicos de manutenção.

**Questão c:** O papel do `.env.example` vs `.env` e os riscos de versionar credenciais.
**Resposta:** O ficheiro `.env.example` serve como documentação técnica e um contrato de configuração, mostrando quais variáveis o sistema precisa para funcionar, mas apenas com valores fictícios ou vazios. O `.env` contém as senhas, chaves e credenciais reais do ambiente. Versionar o `.env` num repositório público no GitHub expõe imediatamente dados sensíveis a robôs e atacantes cibernéticos, o que pode resultar no roubo de dados, sequestro da infraestrutura e invasão direta dos sistemas da empresa.

**Questão d:** O uso do `.env` e `.gitignore` elimina por completo todos os riscos?
**Resposta:** Não elimina. O `.gitignore` apenas protege o código no repositório remoto (GitHub). No entanto, o ficheiro `.env` continua a ser armazenado em texto simples (plain text) no disco rígido do servidor. Se um atacante conseguir aceder ao sistema de ficheiros do servidor (através de uma vulnerabilidade da aplicação, falha do sistema operativo ou má configuração de permissões locais), conseguirá ler as credenciais. Trata-se de uma camada de proteção fundamental, mas não exclui a necessidade de segurança no servidor hospedeiro.

**Questão e:** O que é um contêiner e vantagens do Docker em atividades didáticas.
**Resposta:** Um contentor é um pacote de software leve e portátil que contém todos os elementos necessários para executar uma aplicação (código, runtime, ferramentas do sistema e bibliotecas) de forma isolada do sistema operativo hospedeiro. Em aulas, usar o Docker permite padronizar o ambiente de todos os alunos instantaneamente, evitando o clássico "na minha máquina funciona" devido a diferenças de sistemas operativos ou versões. Além disso, evita a instalação de ficheiros complexos diretamente na máquina física, permitindo subir, apagar e recriar o SGBD de forma rápida, limpa e padronizada.

## Desafios Práticos

### Bloco A: Docker e Infraestrutura de Ambiente

**1. Alteração de porta do SGBD:**
Para acessar na porta 3307 pelo hospedeiro (host), o CloudBeaver não precisou de reconfiguração porque está na mesma rede virtual e continua conectando à porta interna 3306 do serviço `mariadb`. A alteração afeta apenas conexões externas.

**2. Dois ambientes simultâneos:**
Para evitar conflitos com quatro contêineres, garantimos o isolamento utilizando pastas de projeto diferentes e mapeamos portas externas diferentes nos arquivos `.env` (ex: 3306/3307 para o MariaDB e 8978/8979 para o CloudBeaver).

**3. Persistência do volume e alteração de senha de root:**
A autenticação antiga continua válida porque a variável `MARIADB_ROOT_PASSWORD` só atua na primeira inicialização do volume. Como os dados já estavam persistidos em `mariadb_data`, o Docker ignora a nova senha. Para aplicar a nova, precisamos destruir o volume com `docker compose down -v`.

**4. Comportamento da validação estrita (:?):**
O Compose abortou a execução e emitiu erro alertando que a variável estava vazia. Esse modificador é vital porque impede a inicialização acidental de bancos de dados vulneráveis sem senha configurada.

**5. Inspeção de variáveis no compose (`docker compose config`):**
Variáveis interpoladas a partir do `.env`: `MARIADB_ROOT_PASSWORD`, `MARIADB_DATABASE` e `MARIADB_PORT`.

### Bloco B: Modelagem e Consultas SQL Básicas

**6. Criação da tabela de empréstimos:**
```sql
CREATE TABLE IF NOT EXISTS emprestimos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  livro_id INT,
  data_emprestimo DATE,
  devolvido BOOLEAN,
  FOREIGN KEY (livro_id) REFERENCES livros(id)
);

INSERT INTO emprestimos (livro_id, data_emprestimo, devolvido) VALUES 
(1, '2026-10-10', FALSE),
(2, '2026-10-15', FALSE),
(4, '2026-11-01', TRUE);

SELECT l.titulo, e.data_emprestimo, a.nome AS autor
FROM emprestimos e
JOIN livros l ON e.livro_id = l.id
JOIN autores a ON l.autor_id = a.id
WHERE e.devolvido = FALSE;

SELECT a.nome AS autor, COUNT(l.id) AS total_livros
FROM autores a
JOIN livros l ON a.id = l.autor_id
GROUP BY a.id, a.nome
HAVING COUNT(l.id) > 1;

UPDATE livros SET preco = preco * 1.10 WHERE id = 1;

INSERT INTO autores (nome, pais) VALUES ('Autor Teste', 'Desconhecido');
DELETE FROM autores WHERE nome = 'Autor Teste';

### Bloco C: Administração e Privilégios Avançados

**12. Criação de usuário restrito para relatórios:**
```sql
CREATE USER 'relatorios'@'%' IDENTIFIED BY 'Relatorios2026!';
GRANT SELECT ON biblioteca.livros TO 'relatorios'@'%';
```

**13. Teste de restrição de visibilidade:**
Consulta executada para o teste:
```sql
SELECT * FROM autores;
```
*Mensagem de erro:* `SQL Error [1142] [42000]: SELECT command denied to user 'relatorios'@'...' for table 'autores'`  
*Motivo:* O bloqueio ocorre porque o usuário recebeu privilégios limitados ao nível da tabela (apenas na tabela `livros`), o que impede estritamente a visualização da tabela `autores`.

**14. Concessão e revogação dinâmica de privilégios:**
```sql
GRANT INSERT ON biblioteca.livros TO 'relatorios'@'%';
-- (Inserção de teste realizada com sucesso)
REVOKE INSERT ON biblioteca.livros FROM 'relatorios'@'%';
```
*Resultado:* Ao tentar inserir novamente um livro após o comando `REVOKE`, o banco rejeita a operação emitindo o erro "INSERT command denied", restaurando o perfil de acesso unicamente de leitura.

**15. Script idempotente de automação (setup.sql):**
O script completo foi consolidado no arquivo `setup.sql`, o qual foi devidamente versionado e encontra-se na raiz do meu repositório pessoal associado a esta entrega.
