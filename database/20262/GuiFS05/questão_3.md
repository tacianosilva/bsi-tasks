## Q3. Propriedades ACID

As propriedades ACID garantem que uma transação seja executada de maneira confiável.

### Atomicidade

Uma transação deve ser completamente executada ou completamente desfeita.

Exemplo: em uma transferência de R$ 500, o sistema deve debitar R$ 500 da conta A e creditar R$ 500 na conta B.

Se não houver atomicidade, pode ocorrer apenas o débito, fazendo o dinheiro desaparecer da conta de origem sem chegar ao destino.

### Consistência

A transação deve levar o banco de dados de um estado válido para outro estado válido, respeitando suas regras e restrições.

Exemplo: uma transferência não pode fazer uma conta ficar com saldo abaixo do limite permitido.

Sem consistência, o banco poderia aceitar operações que violassem suas regras, deixando dados inválidos.

### Isolamento

Transações executadas simultaneamente não devem interferir incorretamente umas nas outras. Cada transação deve funcionar como se estivesse sendo executada de maneira isolada.

Exemplo: dois atendentes tentam realizar operações simultaneamente na mesma conta. O SGBD deve controlar o acesso para evitar que uma operação sobrescreva incorretamente o resultado da outra.

Sem isolamento, poderiam ocorrer erros como perda de atualização ou utilização de um saldo incorreto.

### Durabilidade

Depois que uma transação é confirmada, seus resultados devem permanecer armazenados mesmo após falhas.

Exemplo: após o banco confirmar uma transferência, o débito e o crédito devem permanecer registrados mesmo que ocorra uma queda de energia.

Sem durabilidade, a operação poderia ser confirmada para o usuário e posteriormente desaparecer após uma falha do servidor.