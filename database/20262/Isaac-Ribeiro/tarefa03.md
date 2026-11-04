# Tarefa 03 - Docker e SGBD

## Identificação e repositório

- **Discente:** Isaac Vilton
- **Usuário no GitHub:** Isaac-Ribeiro
- **E-mail acadêmico:** isaac.ribeiro.018@ufrn.edu.br
- **Repositório pessoal:** https://github.com/Isaac-Ribeiro/Banco_de_Dados_UFRN.git

## Perguntas Discursivas

## Pergunta Discursiva 1

Criar uma tabela é uma operação de **DDL** (Data Definition Language), pois define a estrutura do banco de dados: o nome da tabela, suas colunas, tipos de dados, chaves e restrições. Já inserir registros é uma operação de **DML** (Data Manipulation Language), pois adiciona dados nas estruturas que foram previamente criadas.

Ao executar `DROP TABLE`, a tabela é excluída juntamente com todos os registros armazenados nela. Essa operação remove tanto a estrutura quanto os dados e, por isso, deve ser utilizada com cuidado. Em geral, os dados não podem ser recuperados por comandos SQL comuns após a exclusão da tabela, a menos que exista um backup ou outro mecanismo de recuperação.

## Pergunta Discursiva 2

Ao tentar executar `DROP TABLE autores` com a conta `app_biblioteca`, o MariaDB recusou a operação e retornou o erro 1142, informando que esse usuário não possui permissão para executar o comando `DROP`. Isso aconteceu porque a conta foi criada com privilégios de `SELECT`, `INSERT`, `UPDATE` e `DELETE`, mas não recebeu privilégios de DDL, como `DROP`, `CREATE` ou `ALTER`.

Essa restrição protege a integridade do banco de dados porque impede que uma aplicação web, mesmo em caso de invasão ou falha de programação, exclua tabelas e estruturas importantes. Assim, a conta da aplicação pode manipular os registros necessários para o funcionamento do sistema, mas não pode destruir ou modificar a estrutura do banco. A administração das tabelas deve ser realizada separadamente por uma conta com privilégios elevados.