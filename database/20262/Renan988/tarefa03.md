### Pergunta Discursiva 1

**Diferença entre DDL e DML:**
* **Criar uma tabela (DDL — Data Definition Language):** Trata-se da etapa de definição da estrutura. O comando DDL (`CREATE TABLE`) funciona como o projeto ou esqueleto do banco de dados: ele define o nome da tabela, quais colunas existirão, os tipos de dados aceitos (como texto, inteiros ou números decimais), quais campos são obrigatórios e as regras de relacionamento (chaves primárias e estrangeiras).
* **Inserir registros (DML — Data Manipulation Language):** Trata-se da etapa de manipulação do conteúdo. Com o comando DML (`INSERT INTO`), preenchemos a estrutura que já foi criada previamente com os dados reais. Em termos simples: o DDL constrói as "gavetas" e o DML coloca os "objetos" dentro delas.

**Impacto de apagar uma tabela com `DROP TABLE` (DDL):**
Quando executamos o comando DDL `DROP TABLE`, a estrutura completa da tabela é destruída no banco de dados. Como consequência, todos os registros e dados que estavam armazenados dentro dela são permanentemente apagados e perdidos, juntamente com suas definições de colunas e restrições.

