# Link do repositório com os scripts e programas criados
https://github.com/oguiaraujo/BD2.git

# ODBC (Open Database Connectivity)
É uma interface que permite que aplicações se conectem a diversos sistemas de gerenciamento de banco de dados (SGBD) de forma uniforme. Em Python, ele é amplamente utilizado quando você precisa integrar sua aplicação com bancos de dados como Oracle, PostgreSQL ou MySQL através de um único padrão de código.

O ODBC atua como uma camada de tradução (middleware). Em vez de o Python falar diretamente a "língua" específica do SQL Server ou do Oracle, ele fala com o Driver ODBC, que então traduz os comandos para o banco de dados.

# ORM (Object-Relational Mapping)
É uma técnica que permite mapear as tabelas de um banco de dados para classes em Python. Isso significa que, em vez de escrever SQL manualmente, você manipula dados como se fossem objetos comuns da linguagem.

O ORM funciona como uma ponte: ele traduz as linhas e colunas de uma tabela para objetos e atributos.

O framework escolhido foi o Django-ORM, que já vem imbutido no Django-Framework. A principal característica do Django ORM é o padrão Active Record. Nele, cada classe representa uma tabela e cada instância dessa classe representa uma linha específica no banco de dados. O próprio objeto possui os métodos para se salvar, deletar ou atualizar.