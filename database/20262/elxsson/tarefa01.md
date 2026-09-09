# Tarefa 01 - Conceitos de BD, ACID e SGBD

## Q1. Banco de Dados e SGBD

Um Banco de Dados é um conjunto organizado de dados relacionados entre si, que representam informações sobre um domínio específico. Pode ser o cadastro de clientes de uma empresa, os registros acadêmicos de uma universidade, o histórico de vendas de uma loja, enfim, qualquer conjunto de dados que precise ser armazenado, consultado e atualizado de forma estruturada.

Já o Sistema Gerenciador de Banco de Dados, ou SGBD, é o software que fica responsável por criar, manter, organizar e controlar o acesso a esse banco de dados. Ele atua como uma camada entre a aplicação e os dados propriamente ditos, cuidando de aspectos como segurança, integridade, controle de concorrência e recuperação em caso de falhas.

Alguns exemplos de bancos de dados e dos SGBDs que costumam gerenciá-los:

| Banco de Dados (exemplo) | SGBD utilizado |
|---|---|
| Cadastro de clientes de um e-commerce | MySQL ou PostgreSQL |
| Registros de um sistema bancário | Oracle Database |
| Posts e usuários de uma rede social | MongoDB |
| Sessões de usuários de um sistema web | Redis |
| Dados locais de um aplicativo mobile | SQLite |

## Q2. Problemas de usar Sistemas de Arquivos para armazenagem de dados

Antes de os SGBDs se popularizarem, os dados eram armazenados diretamente em arquivos manipulados por programas específicos. Essa abordagem trazia vários problemas:

- **Redundância e inconsistência de dados**. O mesmo dado podia acabar armazenado em vários arquivos diferentes, cada um mantido por um programa distinto. Se um fosse atualizado e o outro esquecido, os dados ficavam divergentes.
- **Dificuldade de acesso aos dados**. Não existia uma linguagem de consulta genérica como o SQL, então cada nova pergunta sobre os dados exigia escrever um programa novo, sob medida.
- **Isolamento dos dados**. As informações ficavam espalhadas em arquivos com formatos diferentes, o que tornava trabalhoso combinar dados de fontes distintas numa mesma aplicação.
- **Falta de integridade**. Regras de negócio, como "o saldo não pode ficar negativo", precisavam ser codificadas manualmente em cada programa. Não havia garantia de que todos os programas aplicariam essa regra da mesma forma.
- **Falta de atomicidade**. Se o sistema falhasse no meio de uma operação, não existia um mecanismo automático para desfazer as alterações que já tinham sido feitas parcialmente.
- **Problemas de acesso concorrente**. Quando dois usuários acessavam e alteravam o mesmo arquivo ao mesmo tempo, um podia sobrescrever as mudanças do outro sem perceber.
- **Segurança limitada**. Era difícil restringir o acesso a partes específicas dos dados, já que a proteção dependia apenas das permissões do sistema operacional, sem um controle mais granular.

## Q3. Propriedades ACID

Para os exemplos abaixo, vamos usar uma transferência de R$ 100 da Conta A para a Conta B.

### Atomicidade

A transação é tratada como uma unidade indivisível. Ou todas as suas operações são executadas, ou nenhuma delas é.

Na prática, a transferência envolve duas operações: debitar R$ 100 da Conta A e creditar R$ 100 na Conta B. A atomicidade garante que essas duas operações aconteçam juntas, como se fossem uma só.

Se essa propriedade não fosse garantida, o sistema poderia debitar o valor da Conta A e, por conta de uma falha no meio do caminho, nunca chegar a creditar na Conta B. O dinheiro simplesmente sumiria do sistema.

### Consistência

A transação leva o banco de dados de um estado válido para outro estado igualmente válido, respeitando as regras e restrições definidas, sejam elas de integridade referencial, de domínio ou regras de negócio.

Um exemplo prático é que a soma dos saldos de todas as contas antes e depois da transferência precisa ser exatamente a mesma. Nenhuma regra, como um limite mínimo de saldo, pode ser desrespeitada.

Se a consistência falhasse, seria possível, por exemplo, uma transferência deixar uma conta com saldo abaixo do limite permitido, ou o valor total de dinheiro no sistema mudar sem motivo nenhum, o que quebraria as regras do negócio.

### Isolamento

Transações concorrentes não devem interferir umas nas outras. O resultado final precisa ser equivalente ao que se teria se cada transação fosse executada em sequência, uma de cada vez.

Um exemplo prático: se duas transferências envolvendo a Conta A acontecem ao mesmo tempo, uma delas não pode enxergar um estado intermediário e incompleto da outra.

Sem isolamento, dois atendentes poderiam ler o mesmo saldo da Conta A ao mesmo tempo e ambos debitarem R$ 100, gerando um saldo final errado. É a chamada condição de corrida.

### Durabilidade

Uma vez que a transação é confirmada, suas alterações persistem mesmo diante de falhas que aconteçam depois, como uma queda de energia ou um travamento do sistema.

Na prática, depois que a transferência é confirmada e o sistema avisa que a operação foi concluída com sucesso, os novos saldos precisam estar salvos de forma permanente.

Se a durabilidade não fosse garantida, o sistema poderia confirmar a transação e, se o servidor reiniciasse logo em seguida, a alteração se perderia. O cliente acharia que fez uma transferência que, na verdade, nunca aconteceu de fato.


## Q4. Cenários e propriedades ACID envolvidas

**a) Queda de energia no meio de uma transferência deixou o valor debitado da conta de origem, mas não creditado na conta de destino.**

Propriedade envolvida: atomicidade.

A transação era composta por duas operações, débito e crédito, que deveriam ser tratadas como uma unidade só. Como apenas uma parte foi concluída, o princípio de tudo ou nada da atomicidade foi violado.

**b) Dois atendentes debitam, ao mesmo tempo, o mesmo saldo de uma conta.**

Propriedade envolvida: isolamento.

O problema acontece porque as duas transações concorrentes leram o mesmo saldo inicial sem estarem devidamente isoladas uma da outra, causando uma condição de corrida em que uma sobrescreve o efeito da outra. Um controle de isolamento adequado impediria que a segunda leitura ocorresse antes de a primeira transação terminar.

**c) O sistema confirma a operação, mas após reiniciar o servidor o dado foi perdido.**

Propriedade envolvida: durabilidade.

Depois que uma transação é confirmada, ela deveria persistir independentemente de qualquer falha que aconteça em seguida. O fato de o dado ter sido perdido após o commit mostra que a garantia de durabilidade não foi cumprida.

**d) Uma transferência que levaria o saldo abaixo do limite permitido é rejeitada pelo banco.**

Propriedade envolvida: consistência.

Nesse caso o SGBD está funcionando corretamente. Ele impediu que uma regra de negócio, o limite mínimo de saldo, fosse violada, garantindo que o banco de dados continue num estado válido antes e depois da transação.
