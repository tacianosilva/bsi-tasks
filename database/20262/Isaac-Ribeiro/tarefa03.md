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

## Pergunta Discursiva 3

Os usuários foram criados com o host `'%'` porque o MariaDB precisa aceitar conexões originadas de outros contêineres, como o CloudBeaver, e não apenas conexões locais no próprio contêiner do banco. O símbolo `%` funciona como curinga e permite que o usuário se autentique a partir de diferentes endereços de rede.

Se fosse utilizado `'localhost'`, o acesso ficaria restrito ao próprio contêiner do MariaDB, e as conexões vindas do CloudBeaver seriam recusadas. A rede interna criada pelo Docker Compose permite que os contêineres se comuniquem usando o nome do serviço, como `mariadb`. Por isso, o host `%` é necessário para que as contas possam ser utilizadas nessa comunicação entre contêineres.

## Pergunta Discursiva 4

Antes da carga expandida, a base possuía 4 autores e 5 livros. A execução do script adicionou mais 10 autores e 26 livros. Portanto, ao final da carga, ficaram cadastrados **14 autores e 31 livros** no total.

Se fosse inserido um livro com `autor_id = 999`, o MariaDB recusaria a operação, pois não existe um autor com esse identificador na tabela `autores`. A regra que impede essa inserção é a **restrição de chave estrangeira** (`FOREIGN KEY (autor_id) REFERENCES autores(id)`), que garante a integridade referencial entre as tabelas `livros` e `autores`.

## Pergunta Discursiva 5

As Consultas 4 e 5 mostram como as tabelas `autores` e `livros` podem ser relacionadas por meio da chave estrangeira `autor_id`. A principal vantagem de manter essas informações em tabelas separadas é evitar a repetição do nome e do país do autor em todos os livros escritos por ele.

Essa organização reduz a duplicação de dados e o espaço utilizado, além de facilitar atualizações. Se o país de um autor mudar ou tiver sido cadastrado incorretamente, basta alterar essa informação em um único registro da tabela `autores`. A separação também evita inconsistências, pois a chave estrangeira garante que cada livro esteja associado a um autor existente. Esse modelo segue o princípio da normalização e torna as consultas e a manutenção do banco mais confiáveis.