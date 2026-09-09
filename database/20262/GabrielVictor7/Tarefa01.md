## Q1. Descreva o que é um Banco de Dados e o que é um Sistema Gerenciador de Banco de Dados. Cite exemplos de Bancos de Dados e seus SGBDs. 

Um banco de dados é uma coleção de dados estruturados logicamente e inter relacionados, referente a algum aspecto do mundo real. 

SGBD é um sistema de software que permite gerenciar o banco de dados, essa gerência inclui a capacidade de, definição, manipulação, construção(organização das tabelas e dados), segurança, integridade,  e compartilhamento entre diferentes usuários e aplicações.

Exemplo: Um caixa de uma lanchonete vai efetuar uma venda de um produto x, venda essa que será registrada no banco de dados. Para esse processo acontecer, primeiro é preciso que exista uma banco de dados já estruturado de forma lógica, onde haveria um tabela para os produtos, relacionada a tabela de vendas, supondo que o SGBD seja o MYSQL ele vai vai ser responsável por fazer a ponte entre a aplicação e o banco de dados, processando e gerenciando esse novo dado, depois por fim, atualizando o banco de dados armazenado e o metadados.


## Q2. Quais os principais problemas de utilizar Sistemas de Arquivos para armazenagem de dados? 

Como o salvamento em arquivos não usufrui das funcionalidades do SGBD, ele apresenta diversos problemas. Dados duplicados em diferentes arquivos, arquivos podem apresentar diversos erros e inconsistências ao longo do tempo, conforme a aplicação cresce. Há falta de funcionalidades para aplicar filtros de pesquisa, edição e exclusão com filtros, sendo necessário que o desenvolvedor crie a lógica do zero, o que dá bem mais trabalho e consome tempo. Em casos em que as consultas já foram previamente estipuladas, no meio do desenvolvimento podem aparecer novos tipos de buscas que vão precisar ser implementadas toda vez, e em alguns casos é preciso criar uma aplicação nova para lidar com isso. Os arquivos de dados podem estar em formatos diferentes, e essa falta de padronização dificulta a construção de aplicações, pois o desenvolvedor precisa traduzi-los para que um se relacione com o outro. É difícil criar novas restrições ou editá-las, uma vez que estão diretamente inseridas dentro do código da aplicação, sendo preciso encontrar essa parte do código, modificá-la e depois testar toda vez que for necessário. Como os dados podem se repetir e diferentes pessoas podem manipulá-los sem restrições, isso por si só já é um problema de segurança, além de provocar divergências na hora de atualizar ou editar esses dados


