# Links para os códigos

# Resumo sobre ODBC
ODBC (Open Database Connectivity) é um padrão que permite que programas se conectem a diferentes bancos de dados usando uma interface comum agindo como uma ponte entre a aplicação e o banco de dados. Em Python, ele é usado para acessar bancos como MySQL, SQL Server, PostgreSQL,  entre outros, sem precisar mudar muito o código.
Para funcionar é necessário que o driver específico para o banco e uma biblioteca que use ODBC estejam instalados. No Python, temos a biblioteca "pyodbc" que permite a conexão e consultas SQL.
O ODBC se destaca quando é preciso reutilizar código para diferentes bancos e SGBDs.

# Resumo sobre ORM e framework escolhido
ORM (Object-Relational Mapping) em Python é uma técnica que permite trabalhar com banco de dados usando objetos e classes. As tabelas são mapeadas e viram classes, e registros viram objetos/instâncias, tornando o código mais organizado e orientado a objetos. O framework mais popular é o Django onde cada tabela vira uma classe Model, cada coluna da tabela vira um atributo da classe e cada linha da tabela é uma instância daquela classe Model. 