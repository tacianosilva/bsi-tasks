# Tarefa 01 - Conceitos BD e MER
Nome: Eduardo Nascimento Santos <br>
usuario git-hub: Eduardo-NSantos <br>
e-mail: eduardoshw123@gmail.com <br>

## O que é um Banco de Dados?
Um Banco de Dados (BD) é uma coleção organizada de dados que podem ser facilmente acessados, gerenciados e atualizados. Esses dados são estruturados de forma a representar informações significativas sobre um determinado domínio, como alunos de uma escola, produtos de uma loja, ou contas bancárias.
Os dados são armazenados com integridade, segurança e podem ser acessados por múltiplos usuários.

## O que é um Sistema Gerenciador de Banco de Dados (SGBD)?
Um Sistema Gerenciador de Banco de Dados (SGBD) é um software que permite a criação, manipulação, consulta e gerenciamento de bancos de dados. Ele serve como intermediário entre os usuários e o banco de dados, oferecendo recursos como: Controle de acesso, Garantia de integridade dos dados, Backup e recuperação, Linguagens para consulta (como SQL)

## Exemplos de Bancos de Dados e seus SGBDs
*Relacional:*	MySQL, PostgreSQL, Oracle, SQL Server <br>
*Não Relacional (NoSQL):*	MongoDB, Cassandra, Redis, CouchDB <br>
*Orientado a Grafos:*	Neo4j, Amazon Neptune <br>
*Em memória*	Redis, Memcached <br>

## Problemas de Utilizar Sistemas de Arquivos para Armazenamento de Dados
Antes dos SGBDs, os dados eram armazenados em sistemas de arquivos simples (como arquivos .txt, .csv, etc.). Isso trazia diversos problemas, como redundância de Dados, informações repetidas em vários arquivos, inconsistência de Dados, dificuldade de Acesso, isolamento de Dados, problemas de Segurança, concorrência Limitada, backup e Recuperação Difíceis.

## Elementos Básicos do Modelo Entidade-Relacionamento (MER)
O Modelo Entidade-Relacionamento (ER) é uma forma de representar graficamente a estrutura lógica de um banco de dados. Seus três elementos básicos são: <br>
*Entidades:* <br>
Representam objetos do mundo real (ex: Aluno, Produto). <br>
Representadas por retângulos no diagrama ER. <br>

*Atributos:*
São as propriedades ou características das entidades (ex: nome, idade). <br>
Representados por elipses. <br>

*Relacionamentos:*
Indicam associações entre duas ou mais entidades (ex: Aluno “matricula-se em” Disciplina). <br>
Representados por losangos. <br>

## Notações Diferentes em Diagramas ER
Existem várias notações para representar Diagramas ER, sendo as mais comuns: <br>
*Notação de Chen:* Clássica, com retângulos (entidades), losangos (relacionamentos), e elipses (atributos). <br>
*Notação de Crow's Foot (Pé de Galinha):* Popular em ferramentas modernas. Usa símbolos específicos para indicar cardinalidade. <br>
*Notação UML (Unified Modeling Language):* Usa classes e associações para representar entidades e relacionamentos. <br>
