**Tarefa 01 \- Conceitos de BD, ACID e SGBD**

**Q1.** Descreva o que é um Banco de Dados e o que é um Sistema Gerenciador de Banco de Dados. Cite exemplos de Bancos de Dados e seus SGBDs.

Um Banco de Dados é um conjunto organizado de dados relacionados entre si, armazenados de forma estruturada para representar informações de um contexto do mundo real, como os alunos e as notas de uma universidade ou os produtos e as vendas de uma loja. Já o Sistema Gerenciador de Banco de Dados é o software responsável por criar, manter e controlar o acesso ao banco de dados. Ele fica entre os usuários e os dados, armazenando e recuperando as informações com eficiência, permitindo consultas por meio de uma linguagem como o SQL.
Alguns exemplos dos bancos mais conhecidos de SGBD são MySQL, PostgreSQL, Oracle Database e SQL Server.

**Q2.** Quais os principais problemas de utilizar Sistemas de Arquivos para armazenagem de dados?

Nos sistemas de arquivos, cada aplicação guarda e manipula seus próprios arquivos, o que gera vários problemas. O principal é a redundância e inconsistência, já que a mesma informação fica repetida em vários arquivos e pode ser atualizada em um e esquecida em outro. Há também a dependência entre programas e dados, já que o formato do arquivo está embutido no código e qualquer mudança obriga a alterar todos os programas, além da dificuldade de acesso, pois cada nova consulta exige um programa específico, sem uma linguagem como o SQL.

**Q3.** Explique as propriedades **ACID**: atomicidade, consistência, isolamento e durabilidade. Para cada propriedade, descreva um exemplo prático no contexto de uma transferência bancária e explique o que aconteceria se o SGBD não garantisse essa propriedade.

A atomicidade, é o processo onde duas ou mais operações devem acontecer em conjunto, então ou todas as suas operações são executadas, ou nenhuma é. Se algo falhar no meio do caminho, o SGBD desfaz o que já tinha sido feito. Por exemplo, ao finalizar uma compra online, o sistema registra o pedido e reduz o estoque do produto. Sem atomicidade, uma falha entre as duas etapas poderia registrar o pedido sem baixar o estoque, ou o contrário.

A consistência garante que a transação leve o banco de um estado válido para outro estado válido, respeitando todas as regras definidas, como chaves, tipos de dados e restrições. Por exemplo, se existe a regra de que o estoque não pode ser negativo, o SGBD rejeita qualquer compra que o deixaria abaixo de zero. Sem consistência, o banco acumularia dados que violam as regras do negócio, como produtos com estoque negativo.

O isolamento garante que transações executadas ao mesmo tempo não interfiram umas nas outras, de modo que o resultado seja equivalente ao de executá-las uma após a outra. Por exemplo, se resta uma única unidade de um produto e dois clientes tentam comprá-la simultaneamente, o SGBD faz com que apenas um consiga e o outro seja informado de que acabou. Sem isolamento, os dois leriam “1 unidade disponível” e ambos teriam a compra aprovada, vendendo um produto que não existe mais.

A durabilidade garante que, depois que uma transação é confirmada, seus efeitos sejam permanentes, mesmo diante de queda de energia ou falha do sistema, pois o SGBD registra as alterações em log e em disco. Por exemplo, depois que o site informa que o pedido foi realizado, ele continua registrado mesmo que o servidor seja reiniciado logo em seguida. Sem durabilidade, o cliente receberia a confirmação, mas o pedido sumiria após a falha.