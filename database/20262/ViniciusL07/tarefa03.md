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

