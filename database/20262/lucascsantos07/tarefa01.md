**Q1.** Um banco de dados é uma coleção organizada de dados relacionados, armazenados de forma que possam ser consultados
utilizados. Já o Sistema Gerenciador de Banco de Dados (SGBD) é um conjunto de programas que permite criar, armazenar,
consultar, alterar e gerenciar os dados de um banco de dados.

Exemplos de bancos de dados são um banco de dados de uma biblioteca, contendo informações sobre livros e usuários, e um banco de
dados de uma loja, contendo informações sobre produtos e clientes. Exemplos de SGBDs são PostgreSQL, MySQL, Oracle Database e
Microsoft SQL Server.

**Q2.** Os principais problemas são:

* **Inconsistência e redundância de dados:** Informações podem ser repetidas em diferentes arquivos, e as cópias dos dados podem
divergir ao longo do tempo.

* **Dificuldade de acesso aos dados:** É necessário desenvolver programas específicos para realizar consultas e acessar os
dados, tornando o processo mais trabalhoso.

* **Isolamento de dados:** Os dados podem estar armazenados em diferentes arquivos e formatos, dificultando a construção de
aplicações que precisem acessar essas informações.

* **Problemas de integridade:** É difícil garantir e adicionar novas restrições de integridade, pois essas regras precisam ser
implementadas diretamente no código das aplicações.

* **Problemas de atomicidade:** É difícil garantir que uma operação seja realizada completamente ou que o sistema retorne ao seu
estado anterior caso alguma etapa da operação falhe.

* **Anomalias no acesso concorrente:** Como os dados podem ser acessados simultaneamente por diferentes programas ou usuários, é
difícil controlar possíveis conflitos entre esses acessos.

* **Problemas de segurança:** Como nem todos os usuários devem ter acesso a todos os dados, é necessário controlar as permissões
de acesso. Em sistemas de arquivos, esse controle pode ser mais difícil de implementar e gerenciar.