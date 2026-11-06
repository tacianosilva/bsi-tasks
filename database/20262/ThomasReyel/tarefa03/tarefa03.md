## Identificação
Nome: Thomas Reyel da Silva Morais
link: https://github.com/ThomasReyel/bsi-tasks-thomas/tree/tarefa03/arquivos/database/20262/ThomasReyel/tarefa03
## 1. Respostas às Perguntas Discursivas dos Passos Práticos

### Pergunta Discursiva 1
**Diferença entre DDL e DML, e impacto de um `DROP TABLE`.**

A diferença está no que cada grupo de comandos altera. A DDL define e modifica esquemas de relações e criação de índices usando CREATE, ALTER, DROP e etc. A DML trabalha com os dados dentro dessas estruturas, nas tuplas, usando: INSERT, UPDATE, DELETE e SELECT. O DROP TABLE, que é um DDL, tem seu impacto muito maior que o de um DELETE. O DELETE remove linhas e mantém a tabela existindo, enquanto o DROP TABLE remove a tabela inteira: estrutura, todos os dados, índices e os privilégios associados a ela.

### Pergunta Discursiva 2
**Análise do erro 1142 ao tentar `DROP TABLE` com usuário restrito e relação com o princípio do menor privilégio.**

O usuário app_biblioteca possui apenas a permissão de usar comandos DML dentro de biblioteca, por isso ele não pode usar um drop em nenhuma tabela. Isso é o princípio do menor privilégio: cada usuário recebe só o necessário para sua função. Assim, mesmo que a conta seja mal usada ou vazada, ela não consegue apagar causar um grande estrago.

### Pergunta Discursiva 3
**Justificativa técnica para o uso do host `'%'` em vez de `'localhost'` na arquitetura conteinerizada do Docker.**

No MariaDB, a conta depende do host de origem da conexão. O 'localhost' vale só para conexões feitas de dentro da própria máquina do servidor.
No Docker, o CloudBeaver é outro container e se conecta pela rede interna, com um IP próprio. Por isso o usuário precisa ser criado com '%', que aceita qualquer origem. Em produção, o ideal é restringir à sub-rede do Docker.

### Pergunta Discursiva 4
**Relato sobre o povoamento expandido gerado com IA (quantidade final de registros) e o que ocorre ao tentar associar livro a autor inexistente (integridade referencial).**

Após o povoamento expandido, o banco ficou com 14 autores e 30 livros.

Ao tentar cadastrar um livro com um autor que não existe, o MariaDB recusa o INSERT com o erro 1452 (violação de chave estrangeira). Isso é a integridade referencial: um livro só pode apontar para um autor existente, o que evita registros órfãos.
### Pergunta Discursiva 5
**Análise das consultas relacionais e vantagens de normalizar dados em tabelas separadas (`autores` e `livros`) em vez de duplicar textos.**

As consultas relacionais usam JOIN para juntar tabelas (por exemplo, o título do livro com o nome do autor) e GROUP BY com HAVING para contar livros por autor.

Separar autores e livros é melhor do que repetir o nome do autor em cada livro, porque o dado fica guardado uma só vez, uma correção é feita em um só lugar, não há grafias diferentes para o mesmo autor, e a chave estrangeira garante a consistência.

---

## 2. Respostas Dissertativas Conceituais

### Questão a
**Por que uma aplicação comercial nunca deve se conectar ao banco de dados utilizando o usuário `root`? O que pode ocorrer com o servidor de banco de dados caso as credenciais do usuário da aplicação sejam vazadas?**

O root tem poder total sobre o servidor: acessa e apaga qualquer banco e cria ou remove usuários. A aplicação precisa de muito menos, e uma falha dela (como injeção de SQL) herdaria todo esse poder.

Se as credenciais da aplicação vazarem, o atacante faz o que aquele usuário pode fazer. Com o root, isso é o comprometimento total do servidor. Com um usuário restrito, o dano fica limitado aos dados daquele banco.

### Questão b
**Qual é a diferença fundamental entre privilégios DDL (Data Definition Language) e DML (Data Manipulation Language)? Por que é uma boa prática de segurança separá-los em contas de usuários distintas?**

DDL (CREATE, ALTER, DROP) altera a estrutura do banco, e DML (SELECT, INSERT, UPDATE, DELETE) trabalha com os dados.

Separá-los em contas distintas é uma boa prática porque a aplicação só precisa de DML. Se essa conta for comprometida, o atacante não consegue apagar tabelas nem alterar o esquema, e as mudanças estruturais ficam restritas a uma conta administrativa.

### Questão c
**Por que o arquivo `.env.example` deve ser commitado no repositório de código enquanto o arquivo `.env` nunca deve ser versionado? Quais são os riscos e consequências práticas de comitar credenciais reais em um repositório público no GitHub?**

O .env contém as senhas reais, por isso não deve ser versionado. O .env.example é um modelo com os nomes das variáveis e valores fictícios, e deve ser commitado para mostrar quais variáveis são necessárias.

Comitar credenciais reais em um repositório público é perigoso, porque robôs varrem o GitHub e as encontram em minutos. Isso pode levar a vazamento ou destruição de dados e a custos indevidos. Como o Git guarda o histórico, apagar o arquivo depois não basta: é preciso trocar as senhas.

### Questão d
**O uso do arquivo `.env` e a inclusão no `.gitignore` eliminam por completo todos os riscos de segurança de credenciais em um ambiente de desenvolvimento e produção? Justifique sua resposta considerando que o arquivo permanece armazenado em texto puro no sistema de arquivos do servidor.**

Não. O .gitignore só impede que o arquivo vá para o repositório. O .env continua em texto puro no servidor, então quem tiver acesso à máquina, a um backup ou ao docker inspect consegue ler as senhas.

Por isso ele é só uma primeira proteção. Em produção, é preciso combinar com permissões restritas no arquivo, gerenciadores de segredos, troca periódica de senhas e usuários com privilégio mínimo.

### Questão e
**O que é um contêiner e quais são as principais vantagens de utilizar o Docker para provisionar ambientes de banco de dados em atividades didáticas de graduação em comparação com a instalação manual do SGBD diretamente no sistema operacional do computador do aluno?**

Um contêiner é um ambiente isolado e leve que empacota a aplicação com tudo o que ela precisa para rodar, compartilhando o kernel do sistema operacional.

Em aulas, o Docker tem vantagens sobre a instalação manual: todos os alunos usam o mesmo ambiente, a instalação é rápida e descrita em código (docker-compose.yml), não deixa resíduos no computador e permite recomeçar do zero facilmente, além de rodar vários ambientes ao mesmo tempo sem conflito.

---

## 3. Passos Práticos

## Bloco A

### 1)

Alterei MARIADB_PORT para 3307 no .env e recriei os containers com docker compose down && docker compose up -d. A mudança afeta apenas a porta exposta no host (acesso externo via localhost:3307). Na rede interna do Docker o MariaDB segue na porta 3306, então a conexão do CloudBeaver permanece mariadb:3306. Para acessar de fora do Docker (cliente local), usa-se localhost:3307.

### 2)

Após criar as pastas distintas com arquivos de configurações diferentes, os 4 containers conseguem conversar com o lado externo sem conflito com os outros containers, pois foram colocadas em networks diferentes, usando portas externas diferentes e nomes diferentes, dessa forma ele não se enxergam e os conflitos não acontecem.

### 3)

Como já existia os dados da primeira conexão (senha antiga) ele ainda mantém esse arquivo então a senha continua sendo a antiga, enquanto a nova é apenas não sobrescreve a antiga. Em relação aos 2 caminhos para aplicar a nova senha, você pode recriar o volume de dados, dando compose down (com o -v para apagar o volume de dados) e depois o up. O outro caminho é alterar a senha dentro do banco de dados no container.

### 4)

O :? realiza um validação no arquivo de configuração, emitindo um erro caso a variável esteja vazia, assim impedindo que o banco fosse criado sem senha de root. O nosso caso deu erro por conta da docker compose que identificou o problema. Isso é importante por alguns motivos, como segurança, impede que suba o banco sem senha e diagnósticos rápidos, informa de forma clara qual e onde está o erro.

### 5)

A senha do banco

```yaml
MARIADB_ROOT_PASSWORD: RootLab2026!aB
```

A porta do cloudbeaver

(Cloudbeaver)

```yaml
    ports:
      - mode: ingress
        target: 8978
        published: "8978"
        protocol: tcp
```

E a porta do Mariadb

(MariaDB)

```yaml
    ports:
      - mode: ingress
        target: 3306
        published: "3307"
        protocol: tcp
```

---

## Bloco B

### 6)

```sql
CREATE TABLE IF NOT EXISTS emprestimos (
  id INT AUTO_INCREMENT PRIMARY KEY,
  livro_id INT,
  data_emprestimo DATE,
  devolvido BOOLEAN,
  FOREIGN KEY (livro_id) REFERENCES livros(id)
);
```

### 7)

```sql
INSERT INTO emprestimos (livro_id, data_emprestimo, devolvido) VALUES
(1,'2026-01-11',TRUE),
(1,'2026-03-11',FALSE),
(4,'2026-02-11',FALSE);
```

### 8)

```sql
SELECT l.titulo, a.nome AS autor, emp.data_emprestimo
FROM emprestimos AS emp
JOIN livros AS l ON emp.livro_id = l.id
JOIN autores AS a ON l.autor_id = a.id
WHERE emp.devolvido = FALSE;
```

### 9)

```sql
SELECT  a.id, a.nome, COUNT(*) AS total_livros FROM livros
JOIN autores AS a on a.id = autor_id
GROUP BY a.id
HAVING (COUNT(*) > 1)
```

### 10)

```sql
UPDATE livros 
SET preco = preco - (preco * 0.1)
WHERE id = 1;
```

o set está diminuindo de 10% do valor do livro que tem o id = 1

### 11)

```sql
INSERT INTO autores (nome, pais, ano_nascimento) VALUES
('H.P. Lovecraft', 'Estados Unidos', 1890);

DELETE FROM autores WHERE nome = 'H.P. Lovecraft'
```

Como ele não tem nenhum livro associado a ele, apagar sua existência do banco não irá criar nenhuma incosistência

---

## Bloco C

### 12)

```sql
CREATE USER 'relatorios'@'%' IDENTIFIED BY 'Relatorios2026!';
GRANT SELECT ON biblioteca.livros TO 'relatorios'@'%';
```

### 13)

```text
Error executing query:
SQL Error [1142] [42000]: (conn=7) SELECT command denied to user 'relatorios'@'172.21.0.3' for table `biblioteca`.`autores`
```

O usuário relatórios tem apenas a permissão de VER o conteúdo de livros, outras tabelas são bloqueadas pelo SGBD

### 14)

```sql
GRANT INSERT ON biblioteca.livros TO 'relatorios'@'%';
INSERT INTO livros (titulo, ano_publicacao, preco, autor_id) VALUES
('O Alienista',     1882, 79.90,  1);
REVOKE INSERT ON biblioteca.livros FROM 'relatorios'@'%';
```

Mesmo problema da questão anterior, com a revogação o usuário não tem mais permissão para inserir no livros