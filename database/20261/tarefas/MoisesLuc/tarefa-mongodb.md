# Link de acesso

O link para o projeto encontra-se em: https://github.com/MoisesLuc/bsi-tasks/blob/main/database/20261/tarefas/MoisesLuc/proj_mongodb.py

# Resumo: MongoDB com Python

O MongoDB é um banco NoSQL orientado a documentos. Ele não usa tabelas como os bancos relacionais, mas coleções de documentos em formato parecido com JSON, o que deixa o armazenamento mais flexível.

Suas principais características são a escalabilidade, a flexibilidade de esquema e a facilidade para lidar com dados variados. Ele também oferece suporte a índices, consultas mais elaboradas e agregações, o que ajuda quando a aplicação precisa organizar ou filtrar grandes volumes de informação. Por isso, é bastante usado em sistemas que mudam com frequência.

No Python, o acesso ao MongoDB costuma ser feito com a biblioteca PyMongo, que permite conectar ao banco e executar operações de CRUD, aplicar filtros nas consultas, atualizar documentos de forma parcial e trabalhar com coleções de maneira bem flexível. Em aplicações mais robustas, também é comum usar recursos de agregação e bibliotecas assíncronas, como o Motor, para melhorar o desempenho e o controle das requisições.

## Replica Set no MongoDB

Um Replica Set é um conjunto de instâncias do MongoDB que mantém os mesmos dados sincronizados entre si. Ele é usado principalmente para aumentar a disponibilidade e dar mais segurança aos dados, já que, se o servidor principal falhar, outro membro pode assumir o controle.

O membro primário é o responsável por receber as escritas e centralizar as alterações feitas na base. Os membros secundários copiam esses dados a partir do primário e servem como redundância; em alguns casos, também podem ser usados para leituras, dependendo da configuração da aplicação. Já o arbiter não armazena dados, mas participa apenas da votação em caso de eleição de um novo primário.
