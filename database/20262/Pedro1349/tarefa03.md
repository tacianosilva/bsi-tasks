# 1 - Indentificação
 - **Nome Completo:** Pedro Lucas da Silva Araújo;
 - **Usuário no GitHub:** Pedro1349;
 - **Email Acadêmico:** pedro.araujo.716@ufrn.edu.br;
 - **Repositório pessoal:** [DCT2201 — Banco de Dados](https://github.com/Pedro1349/bsi-tasks-Pedro1349);


# 2 - Perguntas Discursivas:
## Pergunta Discursiva 1: Diferença entre DDL e DML, e impacto de um DROP TABLE
  ### Resposta:
  Criar uma tabela é uma instrução DDL de "CREATE", ou seja, é um comando que cria uma estrutura no banco de dados (tabela). Inserir registros é uma instrução DML de "INSERT", ou seja, é um comando usado para inserir dados em uma tabela no banco de dados.
  Se apagar uma tabela com um comando DDL, os dados que estavam nela são deletados também

## Pergunta Discursiva 2: Análise do erro 1142 ao tentar DROP TABLE com usuário restrito e relação com o princípio do menor privilégio.
  ### Resposta:
  O MariaDB recusou a operação e deu o seguinte erro: "SQL Error [1142] [42000]: DROP command denied to user 'app_biblioteca'@'...' for table 'autores'".
  A operação foi recusada, pois o usuário "app_biblioteca" não tem permissão para executar comandos DDL
  Em caso de invasão na conta do "app_biblioteca", o impacto ao sistema é limitado, pois se o hacker tentar executar comandos DDL, o MariaDB rejeitará a ação automaticamente. Da mesma forma, essa restrição funciona como uma camada de proteção contra falhas de programação e erros humanos, impedindo que scripts de testes mal escritos executem exclusões irreversíveis e causem a perda de tabelas inteiras de produção.

## Pergunta Discursiva 3: Justificativa técnica para o uso do host '%' em vez de 'localhost' na arquitetura conteinerizada do Docker.
  ### Resposta:
  porque ao usar "localhost", o MariaDB só aceitaria conexões que nascessem dentro do próprio container dele. Como o CloudBeaver está rodando em outro container separado, o banco de dados enxerga a requisição vindo de um IP externo, e não do localhost.
  Por isso o "%" é usado, já que ele permite conexões vindas de qualquer endereço IP.

## Pergunta Discursiva 4: Relato sobre o povoamento expandido gerado com IA (quantidade final de registros) e o que ocorre ao tentar associar livro a autor inexistente (integridade referencial).
  ### Resposta:
  total de autores é 14, já o total de livros é 32 (5 antigos + 28 criados).
  Se eu tentasse inserir um livro cujo autor_id é 999, O MariaDB rejeitaria a inserção e apresentaria um erro de violação de chave estrangeira (autor não existe). A regra do banco que garante esse comportamento é a integridade referencial, implementada por meio de uma restrição de chave estrangeira

## Pergunta Discursiva 5: Análise das consultas relacionais e vantagens de normalizar dados em tabelas separadas (autores e livros) em vez de duplicar textos.
  ### Resposta:
  A principal vantagem de dividir os dados em duas tabelas relacionadas é evitar a repetição desnecessária de informações. Em vez de armazenar o nome e o país do autor em cada registro de livro, essas informações ficam cadastradas apenas uma vez na tabela autores, enquanto a tabela livros utiliza o campo "autor_id" para identificar a qual autor cada obra pertence. Dessa forma, essa divisão reduz a duplicação de dados, economiza espaço de armazenamento, facilita atualizações e evita inconsistências. Por exemplo, se o nome de um autor precisar ser alterado, basta modificar seu cadastro na tabela autores, sem precisar atualizar todos os seus livros. Além disso, o relacionamento por chave estrangeira garante a integridade dos dados, impedindo que sejam cadastrados livros associados a autores inexistentes.
