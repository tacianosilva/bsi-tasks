
## Questão 01
**Resposta:** Um banco de dados é um conjunto de dados relacionados armazenados em um dispositivo seja ele eletrônico ou físico. Já um Sistema Gerenciador de Banco de Dados ou SGBD é um sistema de BD projetado para gerir grandes volumes de informações, facilitando as operações necessárias em um banco de dados digital. Existem os banco de dados relacionais que tem o MySQL como exemplo de SGBD, e os bancos não relacionais que tem o MongoDB como exemplo.

## Questão 02
**Resposta:** Sistema de arquivos possuem diversos problemas como falta de segurança (não pode garantir que pessoas vejam somente o que as compete), inconsistência e redundância de dados (Não possui ferramentas de controle que evite duplicidade de dados ou a sua inconsistência), dificuldade de realizar operações atômicas (várias operações ao mesmo tempo e dependentes uma das outras, é muito difícil de se garantir em sistemas de arquivos) e entre o outros problemas.

## Questão 03
**Resposta:** 
- **Atomicidade:** Evite a perda de dados, registros órfãos e operações atômicas. Um banco de dados com atomicidade fornece transações “tudo ou nada” para que você não perca dados se uma parte de uma transação falhar no meio da operação. Exemplo: No caso de uma transação bancária, primeiro o dinheiro é debitado da conta de quem está transferindo. Caso a operação falhe e o SGBD não possua a propriedade de atomicidade, quem está transferindo perde o dinheiro e a pessoa que receberia não o recebe.
- **Consistência:** As restrições de tabela nos bancos de dados ACID exigem que todas as transações armazenem dados em um formato uniforme. Exemplo: Na criação de uma conta, o CPF do titular tem que ser única (só ele pode ter esse cpf), caso uma outra pessoa vá fazer uma conta nesse banco e informe o mesmo cpf, um banco com a propriedade de consistência tem que cancelar a operação.
- **Isolamento:** Isolamento é uma garantia de que transações executadas simultaneamente não devam interferir umas nas outras. Exemplo: Em um caso de um conta com 500 reais, 2 operações de saque são realizadas ao mesmo tempo, uma com 50 e a outra com 100. Se o SGBD não tiver a características de isolamento a segunda operação pode atropelar a primeira. Assim no final a conta não ficaria com 350 mas com 400.
- **Durabilidade:** Durabilidade é uma garantia de que as alterações feitas por uma transação confirmada não devem ser perdidas. Todas as transações confirmadas devem ser persistidas em armazenamento durável e não volátil, ou seja, em disco. Exemplo: Caso a energia do banco caia, o SGBD com durabilidade tem que garantir que todas as operações que foram confirmadas estejam salvas.

## Questão 04
**Resposta:** 

A) Atomicidade, pois as operações são encadeadas e a falha de uma delas deveria resultar na falha do processo inteiro. Então em um SGBD competente, nesse tipo de situação apenas não teria completado a operação de débito da conta.

B) Isolamento, pois, em um SGBD as 2 operações não iriam interferir uma na outra até que uma fosse confirmada. Então assim que o primeiro débito fosse confirmado, a segunda operação ia ser cancelada.

C) Durabilidade, o SGBD do cenário em questão, deveria garantir que toda e qualquer operação confirmada esteja salva.

D) Consistência, pois, no cenário em questão o SGBD impediu que uma regra fosse quebrada, assim garantido a consistência do banco.

## Questão 05

**Resposta:**

- **Capacidade:** é a proficiência em restaurar o banco a um estado consistente após falhas (queda de energia, erro de hardware e etc). O SGBD gerencia isso através de logs de transações (write-ahead logging), pontos de verificação (checkpoints) e mecanismos de backup.

- **Integridade:** Ela garante que os dados armazenados sejam válidos e consistentes com as regras do negócio (ex.: um CPF não pode ser nulo, uma idade não pode ser negativa). O SGBD gerencia isso por meio de restrições (constraints) como chaves primárias, chaves estrangeiras, regras de domínio, triggers e validações definidas no esquema.

- **Redundância:** Ocorre quando o mesmo dado é armazenado em múltiplos lugares desnecessariamente, desperdiçando espaço e aumentando o risco de inconsistência. O SGBD reduz isso por meio de normalização do esquema, organizando os dados em tabelas relacionadas em vez de duplicá-los.

- **Inconsistência:** Acontece quando dados redundantes não são atualizados de forma sincronizada, gerando informações conflitantes (ex.: o mesmo endereço de cliente diferente em duas tabelas). O SGBD evita isso controlando a redundância (normalização) e aplicando integridade referencial, além de mecanismos de controle de concorrência (locks, transações ACID que já foram ditas) que garantem atualizações coordenadas.

## Questão 06
**Resposta:**

- **A empresa possui equipes**, essas equipes tem: departamento, código e quantidade de funcionários.
- **Uma equipe possui vários funcionários**, que tem: nome, cpf, data de nascimento, salário, email e função.
- **Uma equipe resolve várias tarefas**, essas tarefas possuem: tipo, código, data de início e data final programada.
- **Uma tarefa pertence a um sprint**, esse projeto tem: código data de início anterior à data de término.
- **Uma sprint pertence a uma release**, essas releases tem: código, nome e data de término
- **Uma release pertence a um projeto**, esse projeto tem: Código,orçamento,data de início e data final programada e data de término.
- **Um projeto tem um cliente**, esse cliente tem: Nome, tipo, cnpj (ou cpf, vai depender do tipo), email e telefone.

### Regras:

- Um funcionário só pode estar em uma equipe por vez
- Um cliente pode ter vários projetos
- Toda tarefa precisa estar vinculada a um projeto
- Um funcionário precisa estar vinculado a uma equipe
- As equipes podem trabalhar em tarefas de projetos diferentes
- Caso um cliente seja do tipo pessoa física, ela não pode ter CNPJ
- Toda squad deve ter exatamente um líder técnico, um supervisor e um gerente de produto.
- A função do funcionário pode ser desenvolvedores, testadores, líder técnico, supervisor e gerente de produto
