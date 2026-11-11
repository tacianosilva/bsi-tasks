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

**Q4.** Para cada cenário abaixo, indique qual(is) propriedade(s) ACID está(ão) em jogo e **justifique** sua resposta:
a) A propriedade em jogo é a atomicidade. A transferência é composta por duas operações que deveriam ser tratadas como uma unidade só. Com a queda de energia, apenas o débito foi concluído, deixando a transação pela metade. Se o SGBD garantisse a atomicidade, ao reiniciar ele desfaria o débito (rollback), voltando ao estado anterior à transferência.

b) A propriedade em jogo é o isolamento. Os dois atendentes executam transações simultâneas sobre o mesmo saldo, e sem controle de concorrência ambos podem ler o mesmo valor inicial e gravar resultados que se sobrescrevem, fazendo um dos débitos ser perdido ou o saldo ficar incorreto. Com isolamento, o SGBD faz as transações se comportarem como se fossem executadas uma após a outra, e a segunda parte do saldo já atualizado pela primeira.

c) A propriedade em jogo é a durabilidade. O sistema já havia confirmado a operação, então seus efeitos deveriam ser permanentes, mesmo com a reinicialização do servidor. A perda do dado indica que a alteração não foi gravada de forma persistente, o que um SGBD durável evita registrando as mudanças em log e em disco antes de confirmar a transação.

d) A propriedade em jogo é a consistência. O limite mínimo de saldo é uma regra de integridade do banco, e a transferência que a violaria levaria o banco a um estado inválido. Ao rejeitar a operação, o SGBD garante que o banco passe apenas de um estado válido para outro estado válido, mantendo as regras do negócio.

**Q5.** Um SGBD trata dos seguintes aspectos: **recuperação, integridade, redundância e inconsistência**. Explique cada um deles e descreva como o SGBD os gerencia.

A recuperação é a capacidade de restaurar o banco de dados a um estado correto depois de uma falha, como queda de energia, erro de software ou defeito no disco. O SGBD gerencia isso principalmente por meio de logs de transações, que registram todas as alterações antes de elas serem gravadas definitivamente. Após uma falha, ele usa o log para refazer as transações já confirmadas e desfazer as que estavam incompletas. Além disso, ele permite backups e pontos de restauração, que reduzem o trabalho necessário para voltar ao estado correto.

A integridade diz respeito à exatidão e à validade dos dados, ou seja, à garantia de que eles respeitam as regras definidas para o banco. O SGBD a gerencia por meio de restrições de integridade declaradas no esquema, como chave primária (que impede registros duplicados), chave estrangeira (que impede referências a registros inexistentes), tipos de dados, restrições de valores (como saldo não negativo), campos obrigatórios e gatilhos. Toda operação que viole essas regras é rejeitada automaticamente.

A redundância é a repetição desnecessária dos mesmos dados em vários lugares, o que desperdiça espaço e dificulta a manutenção. O SGBD ajuda a controlá-la ao centralizar os dados em um único banco compartilhado por todas as aplicações, e o projeto do esquema, com a normalização, organiza os dados em tabelas de modo que cada informação seja armazenada uma só vez e as demais tabelas apenas a referenciem por chaves. Quando alguma redundância é mantida de propósito, o SGBD a controla e a mantém sincronizada.

A inconsistência ocorre quando a mesma informação aparece com valores diferentes em partes distintas do banco, ou quando os dados contradizem as regras do negócio. Ela costuma ser consequência da redundância descontrolada e de falhas durante atualizações. O SGBD a evita ao reduzir a redundância, ao aplicar as restrições de integridade e ao executar as operações como transações com propriedades ACID, garantindo que as atualizações sejam feitas por completo e sem interferência entre usuários, de modo que o banco passe sempre de um estado consistente para outro.