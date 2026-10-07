# Q1. Descreva o que é um Banco de Dados e o que é um Sistema Gerenciador de Banco de Dados. Cite exemplos de Bancos de Dados e seus SGBDs.

Um banco de dados é uma forma de armazenar dados diferentes do gerenciador de arquivos. Ele não se baseia em hierarquia como o explorador e tem diversas funções a mais, como possibilidade de haver backups; ser capaz de fazer buscas por um dado específico dentro de sua base, assim como alterações, inserções e remoções em qualquer lugar; todos os dados se enxergam ao mesmo tempo, interagindo e conversando entre si; é capaz de facilmente lidar com de redundâncias e dados faltantes; por possibilitar dar permissões ao usuários, quem pode acessar que parte do banco, ele é extremamente seguro e confiável.

Seguindo essa linda, um Sistema Gerenciador de Banco de Dados é um software auxiliar que facilita o uso de um BD. Assim como o Explorador de Arquivos do Windows nos permite ver como estão organizados nossos arquivos dentro da máquina, os SGBDs conseguem interpretar o banco de dados e nos dar uma interface mais enxuta para nosso uso. Por meio deles podemos rapidamente fazer comandos e interpretar dados que estão guardados ali dentro. Alguns exemplos de Bancos de Dados e seus respectivos SGBDs são o MySQL, com o Workbench e o PostgreSQL, e o NoSQL, com o MongoDB e o Redis.

---

# Q2. Quais os principais problemas de utilizar Sistemas de Arquivos para armazenagem de dados?

Em grande escala, o fato da organização ser hierarquica pode tornar o processo de busca extremamente demorado e complicado de se fazer, já que a busca deve ser feita em cada diretório individualmente, e então retornar para entrar no próximo. Ademais, arquivos em diretórios diferentes não "se enxergam", e não podem interagir diretamente uns com os outros a não ser que uma declaração física seja feita, o problema disso é que caso o arquivo no destino mude de lugar, nada será encontrado e uma falha será gerada. Um outro grande fator é a alta taxa de redundância gerada, as vezes um dado é gerado numa pasta e usado ali, então é gerado novamente num outro lugar, e uma terceira vez num lugar distinto, sendo difícil de encontrar onde as repetições acontecem. Além disso, existe o problema de backup, ou no caso, a falta dele. Num sistema de arquivos não há backups automáticos e os mesmos são feitos pelos usuários, se algum erro ou falha acontecer, não há como recuperar de forma automática como nos Banco de Dados.

---

# Q3. Explique as propriedades ACID: atomicidade, consistência, isolamento e durabilidade. Para cada propriedade, descreva um exemplo prático no contexto de uma transferência bancária e explique o que aconteceria se o SGBD não garantisse essa propriedade.

* **Atomicidade** se refere ao fato de que cada operação é "inteira", no sentido ser vista pelo sistema como uma única instrução, não a soma de pequenas partes, o que ajuda a lidar com erros. Um exemplo prático disso seria uma transferência PIX: na prática ocorrem duas etapas, descontar de quem enviou, e adicionar na de quem recebeu. O fato dessa operação ser atômica garante que se ouver um erro em qualquer etapa, toda a operação será cancelada, já que ela é "uma só". Caso isso não existisse, após o dinheiro ser removido da conta, poderia acontecer um erro, o segundo usuário não receberia seu dinheiro, e ele seria "perdido", causando inconsistências no banco e problemas no mundo real.
* **Consistência** é o que garante que o banco de dados esteja sempre válido dentro de suas próprias regras, "consistente" com o que promete. Se um serviço bancário tem uma regra que proíbe saldos negativos, é impossível efetuar uma transferência dee R$50000 tendo apenas R$10 na conta. Se isso não existisse, muitas regras de negócio seriam desrespeitadas.
* **Isolamento** faz com que transações concorrentes não interfiram indevidamente umas nas outras, mesmo sendo executadas ao mesmo tempo. Desse modo, o resultado final se torna o mesmo que o entregue por uma operação enfileirada, que executa em ordem. Um exemplo é se uma conta faz dois pagamentos de R$1000 ao mesmo tempo, tendo apenas R$1500 na conta, eles iniciciam ao mesmo tempo, mas o isolamento garante que apenas um deles seja efetuado, e o outro receba uma mensagem de "Saldo insuficiente", por exemplo.
* **Durabilidade** assegura que após uma operação ter sido confirmada, ela fica permanentemente salva no banco, mesmo que um erro aconteça logo em seguida. Continuando o exemplo do PIX, a partir do momento que a a mensagem de "transferência bem sucedida" é enviada, tudo já foi devidamente salvo e registrado no banco de modo a não haver mais perigo de se perder.

---

# Q4. Para cada cenário abaixo, indique qual(is) propriedade(s) ACID está(ão) em jogo e justifique sua resposta:

### a) Queda de energia no meio de uma transferência deixou o valor debitado da conta de origem, mas não creditado na conta de destino.

Falta de atomicidade, a primeira etapa da operação foi efetuada (debitar) mas a segunda não. Caso a mesma tivesse sido implementada, ambas teriam sido canceladas.

### b) Dois atendentes debitam, ao mesmo tempo, o mesmo saldo de uma conta.

Isso é um caso de isolamento, já que duas operações distintas modificam uma mesma coisa ao mesmo tempo. Se ele foi aplicado corretamente ou não depende de como o sistema responde: se o saldo era suficiente e o sistema permitiu, o isolamento foi usado corretamente; se não era suficiente e mesmo assim a operação foi bem sucedida, então é uma falha.

### c) O sistema confirma a operação, mas após reiniciar o servidor o dado foi perdido.

Falta de durabilidade, já que após a confirmação, o dado não deveria mais ser perdido e sim estar permanantemente salvo no servidor.

### d) Uma transferência que levaria o saldo abaixo do limite permitido é rejeitada pelo banco.

Consistência sendo aplicada, se a regra proíbe saldos negativos, a operação foi corretamente rejeitada para manter a regra como verdadeira.

---

# Q5. Um SGBD trata dos seguintes aspectos: recuperação, integridade, redundância e inconsistência. Explique cada um deles e descreva como o SGBD os gerencia.

* **Recuperação** é a capacidade do sistema de se recuperar após alguma falha, voltando o banco à um estado consistente e seguro, com todas as operações confirmadas salvas e nenhuma das operações que estavam em andamento pela metade (atomicidade). Ele faz isso por meio de vários logs a cada operação, esse log fala até onde todos os dados estão seguros e funcionais, e a partir de que ponto dados falhos começaram a aparecer devido ao problema, então ele salva o que está bom, e desfaz o que não está.
* **Integridade** se refere aos dados salvos no banco e se o mesmo segue o padrão esperado. Por meio de diversas restrições e regras de funcionamento, os campos seguem esse padrão e se mantém corretos para o uso e leitura dos dados. O banco checa isso por meio de diversos constraints, como chaves primárias únicas, chaves estrangeiras e verificação de domínios.
* **Redundância** trata-se de lidar com dados repetidos ao longo do sistema. Por se tratar uma organização de relações, os dados não precisam se repetir diversas vezes em lugares diferentes, basta criar uma nova relação onde o uso é requisitado. Há casos que a redundância não é ruim, como manter um banco de pé em diferentes servidores por segurança, e em casos como esse, os SGBDs garantem que os dados repetidos estejam todos sincronizados e a par uns com os outros.
* **Inconsistência** lida com um dado repetido, mas diferente. Geralmente vem de um caso de redundância não proposital, há duas versões do mesmo dado em lugares diferentes do sistema, e a leitura acaba sendo confusa. O sistema lida com isso por meio das restrições anteriormente sitadas, previnindo que esses dados cheguem até mesmo a existir, mas também por meio da normalização de dados.

---



# Q6. Considere o cenário de uma empresa de desenvolvimento de softwareque atende outras empresas como clientes. A empresa organiza seu trabalho em squads (equipes) compostas por desenvolvedores, testadores, líder técnico, supervisor e gerente de produto. Cada squad resolve tarefas (issues) e planeja releases, testes e o cronograma de sprints (iterações) dos projetos de cada cliente.

## Sem utilizar SQL, elabore um mini-projeto conceitual do banco de dados dessa empresa, deixando claro:

### a) As principais entidades envolvidas (clientes, squads, membros, tarefas, projetos, sprints, releases).

Clientes, Projeto, Squad, Sprint, Issue, Membro, Release.

### b) Os principais atributos de cada entidade.

* **Cliente**: ID, nome, CNPJ (como é empresa, melhor isso que CPF) e email
* **Projeto**: ID, id_cliente (chave estrangeira), nome, descricao, inicio, fim, situacao (em andamento, finalizado, cancelado)
* **Squad**: ID, nome, id_membro (chave estrangeira)
* **Sprint**: ID, id_squad (chave estrangeira), numero, descricao, inicio e fim
* **Issue**: ID, id_projeto (chave estrangeira), id_sprint (chave estrangeira), nome, descricao, situacao (em andamento, finalizado, cancelado)
* **Membro**: ID, nome, email, funcao
* **Release**: ID, versao, cricao (data) e publicao (data)

### c) Os relacionamentos entre as entidades (com a cardinalidade, ex.: "um cliente pode ter vários projetos").

* Um cliente tem vários projetos
* Um projeto só pertence à um cliente
* Um squad tem vários membros
* Um membro só faz parte de um squad
* Um squad tem varios sprints
* Um sprint só pertence à um squad
* Um projeto dura varios sprints
* Um sprint pertence a um projeto
* Um projeto tem varias issues
* Uma issue pertence à um projeto
* Um sprint tem varias issues
* Uma issue pertence a um sprint
* Um membro trabalha em várias issues
* Uma issue pode varios membros
* Uma release pode ter varios projetos
* Um projeto faz parte de uma release

### d) Em linguagem natural, as regras de integridade (restrições) que o banco de dados deveria garantir, ex.: "apenas um líder por squad", "toda tarefa precisa estar vinculada a um projeto".

* Toda tarefa tem que pertencer à um projeto
* Todo projeto tem que pertencer à um cliente
* Um squad tem que ter exatamente um membro na função "Líder Técnico" e um na função "Supervisor"
* Um membro só pode estar em um squad
* Um sprint so pode ter um projeto e pertencer à um squad
* Uma release só pode ser publicada se todas suas tarefas tiverem sido concluídas
* As datas de início e fim não podem se contradizer (Uma data de "início" ser depois da de "fim")
* Não podem haver dois sprints do mesmo squad acontecendo durante um mesmo período
