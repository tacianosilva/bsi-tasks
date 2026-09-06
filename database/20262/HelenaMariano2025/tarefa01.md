## Q1. Banco de Dados e SGBD

### Banco de Dados

Um Banco de Dados é uma coleção organizada de dados que são armazenados de forma estruturada, permitindo que as informações sejam consultadas, atualizadas e gerenciadas de maneira eficiente.

Por exemplo, um sistema de uma universidade pode possuir um banco de dados contendo informações sobre alunos, cursos, professores, disciplinas e matrículas.

### Sistema Gerenciador de Banco de Dados (SGBD)

Um Sistema Gerenciador de Banco de Dados (SGBD) é um software responsável por permitir a criação, armazenamento, consulta, alteração e gerenciamento dos dados de um banco de dados. Ele também fornece recursos para controlar o acesso aos dados, garantir sua integridade, segurança e realizar operações de forma confiável.

Alguns exemplos de SGBDs são:

- PostgreSQL;
- MySQL;
- Oracle Database;
- Microsoft SQL Server;
- SQLite.

### Exemplos de Bancos de Dados e seus SGBDs

| Banco de Dados | SGBD |
|---|---|
| Banco de dados de uma universidade | PostgreSQL |
| Banco de dados de uma loja virtual | MySQL |
| Banco de dados de uma instituição financeira | Oracle Database |
| Banco de dados de uma empresa | Microsoft SQL Server |
| Banco de dados de um aplicativo | SQLite |

## Q2. Problemas dos Sistemas de Arquivos

A utilização de sistemas de arquivos para armazenar dados pode apresentar diversos problemas, principalmente quando há uma grande quantidade de informações ou vários usuários acessando os dados simultaneamente.

Os principais problemas são:

- **Redundância de dados:** as mesmas informações podem ser armazenadas em diferentes arquivos, causando duplicação desnecessária.
- **Inconsistência dos dados:** quando uma informação duplicada é alterada em um arquivo, mas não em outro, os dados podem ficar diferentes entre si.
- **Dificuldade de acesso:** encontrar e consultar informações pode ser mais trabalhoso, principalmente quando os dados estão espalhados em vários arquivos.
- **Problemas de segurança:** pode ser difícil controlar quais usuários podem visualizar ou modificar determinadas informações.
- **Dificuldade de compartilhamento:** vários usuários ou programas podem ter dificuldade para acessar e modificar os mesmos dados de forma segura.
- **Problemas de concorrência:** quando duas pessoas ou sistemas tentam alterar o mesmo arquivo ao mesmo tempo, podem ocorrer conflitos ou perda de informações.
- **Dificuldade de recuperação:** em caso de falhas, como queda de energia ou corrupção de arquivos, pode ser difícil recuperar os dados corretamente.
- **Falta de integridade:** o sistema de arquivos não possui mecanismos próprios suficientes para garantir que os dados armazenados sigam regras e sejam válidos.

Os SGBDs foram desenvolvidos para solucionar grande parte desses problemas, oferecendo mecanismos de controle de acesso, integridade, concorrência, recuperação e gerenciamento dos dados.