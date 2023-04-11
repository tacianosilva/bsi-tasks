<h1>Tarefa 01 - Conceitos BD e MER</h1>


<h3>
Anderson Azevedo da Silva </p>
AndersonAzeved </p>
andersonsilva14.2017@gmail.com </p>
</h3>

#
a. Descreva o que é um Banco de Dados e o que é um Sistema Gerenciador de Banco de Dados. Cite exemplos de Bancos de Dados e seus SGBDs. 

    
#
b. Quais os principais problemas de utilizar Sistemas de Arquivos para armazenagem de dados.


#
c. O modelo de dados entidade-relacionamento foi desenvolvido para facilitar o projeto de banco de dados, permitindo especificação de um esquema que representa a estrutura lógica geral de um banco de dados. Descreva os três elementos básicos de um Modelo Entidade Relacionamento (MER).


#
d. Pesquise sobre as várias notações possíveis para Diagramas ER, cite alguns exemplos de notações diferentes para o mesmo conceito (ex: Cardinalidade, Entidade Subordinada, etc).


#
e. Construa um Diagrama ER para projetar uma base de dados de um Sistema de Controle de Freqüência de Empregados de uma organização. A base de dados não deve conter redundância de dados. O modelo ER deve ser representado com um diagrama usando Mermaid.js. O modelo deve apresentar, ao menos, entidades, relacionamentos, atributos, identificadores e restrições de cardinalidade. O modelo deve ser feito no nível conceitual, sem incluir chaves estrangeiras.

i. A base de dados deve manter dados sobre empregados. Cada empregado é identificado por um código, um nome e um e-mail. Para fins de controle de frequência, há dois tipos de empregados.

ii. Um tipo de empregado é o que tem horário livre. Empregados deste tipo podem trabalhar em qualquer horário do dia. Para estes empregados queremos saber quantas horas devem trabalhar ao longo do mês, bem como, qual é o menor período em horas que devem trabalhar. Exemplificando, há alguns empregados que não devem trabalhar menos que duas horas por dia.

iii. Empregados de segundo tipo devem trabalhar em horários fixos. A semana de trabalho do empregado deste tipo está organizada em turnos. Um turno tem horário de início e horário de fim. O empregado pode trabalhar dois turnos no mesmo dia da semana. Cada dia da semana é identificado por um código (algo como “dom” "seg", "ter", . . . ) e tem um nome (algo como "domingo", "segunda-feira", . . . ).


iv. Todos os empregados devem bater o ponto, ou seja, informar o horário de entrada e saída do trabalho, em cada turno de cada dia da semana.

