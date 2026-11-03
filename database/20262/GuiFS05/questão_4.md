## Q4. Propriedades ACID na prática

### a) Queda de energia durante uma transferência

Propriedade: Atomicidade.

A transferência deveria ser totalmente concluída ou totalmente desfeita. Como o débito ocorreu, mas o crédito não, a transação ficou parcialmente executada.

### b) Dois atendentes debitam simultaneamente o mesmo saldo

Propriedade: Isolamento.

As transações concorrentes precisam ser controladas para que uma não utilize ou sobrescreva incorretamente os dados modificados pela outra.

### c) Operação confirmada, mas dado perdido após reiniciar o servidor

Propriedade: Durabilidade.

Depois do commit, os dados devem permanecer armazenados mesmo após uma falha ou reinicialização.

### d) Transferência que deixaria o saldo abaixo do limite é rejeitada

Propriedade: Consistência.

A operação é rejeitada porque violaria uma regra de integridade do banco. O banco deve permanecer em um estado válido.