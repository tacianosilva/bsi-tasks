**Q4.** Para cada cenário abaixo, indique qual(is) propriedade(s) ACID está(ão) em jogo e **justifique** sua resposta:

   a) Queda de energia no meio de uma transferência deixou o valor debitado da conta de origem, mas não creditado na conta de destino.

   **resposta:**: propriedade em jogo é a atomicidade, pois a situação descrita evidencia que a transação não foi tratada como uma unidade indivisível de "tudo ou nada", permitindo que apenas metade da operação fosse efetivada antes da queda de energia.


   b) Dois atendentes debitam, ao mesmo tempo, o mesmo saldo de uma conta.

    **resposta:**: a propriedade afetada é o isolamento, uma vez que a execução simultânea de duas operações sobre o mesmo saldo gerou interferência mútua por falta de controle adequado de concorrência.

   c) O sistema confirma a operação, mas após reiniciar o servidor o dado foi perdido.

    **resposta:**: a propriedade violada é a durabilidade, pois os dados de uma operação confirmada com sucesso deveriam ser mantidos de forma permanente, independentemente de reinícios ou falhas de hardware no servidor

   d) Uma transferência que levaria o saldo abaixo do limite permitido é rejeitada pelo banco.

   **resposta:**: a propriedade em ação é a consistência, já que o sistema rejeitou a transação para impedir a violação de uma regra de integridade do banco de dados, garantindo que a base permaneça sempre em um estado válido segundo as restrições definidas.