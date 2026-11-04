1. **Identificação e Repositório:**
   - **Nome completo:** Lucas da Costa Santos
   - **Usuário no GitHub:** [lucascsantos07](https://github.com/lucascsantos07)
   - **E-mail acadêmico:** lucas.costa.123@ufrn.edu.br
   - **Repositório pessoal público:** https://github.com/lucascsantos07/dct2201-banco-de-dados.git

2. **Respostas às Perguntas Discursivas dos Passos Práticos:**
   - **Pergunta Discursiva 1:** DDL é a linguagem utilizada para definir e modificar a estrutura do banco de dados, como criar, alterar ou excluir tabelas. Já a DML é utilizada para manipular os dados armazenados nessas tabelas, permitindo inserir, atualizar e excluir registros. O comando DROP TABLE pertence à DDL e seu impacto é excluir completamente uma tabela, removendo sua estrutura e todos os dados armazenados nela.
   - **Pergunta Discursiva 2:** O comando DROP TABLE autores foi recusado porque o usuário app_biblioteca possui apenas privilégios de manipulação de dados (DML), como inserir, consultar, atualizar e excluir registros, mas não possui permissões para alterar a estrutura do banco de dados (DDL). Por isso, o MariaDB retornou o erro 1142. Essa restrição protege a integridade do banco de dados, impedindo que uma invasão ou falha na aplicação web provoque a exclusão de tabelas e a perda de sua estrutura e dos dados armazenados.