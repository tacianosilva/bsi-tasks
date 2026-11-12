## Tarefa 03 - Docker Compose, MariaDB e Administração de SGBD

Os arquivos de configuração e scripts SQL da Tarefa 03 estão localizados na pasta `tarefa03/`:

- `docker-compose.yml`: Orquestração dos contêineres do SGBD MariaDB 11 e da interface administrativa web CloudBeaver com persistência via volume nomeado.
- `.env.example`: Modelo de variáveis de ambiente exigidas pelo projeto (sem credenciais sensíveis).
- `.gitignore`: Configuração do Git para impedir o versionamento do arquivo local `.env`.
- `povoamento.sql`: Script DML contendo a carga expandida de autores e livros gerada com auxílio de IA generativa.
- `setup.sql`: Script SQL idempotente para recriação completa do banco `biblioteca`, tabelas, usuários, privilégios e registros iniciais.