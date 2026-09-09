## Q5. Aspectos gerenciados por um SGBD

### Recuperação

É a capacidade de restaurar o banco de dados após falhas, como quedas de energia ou erros do sistema.

O SGBD utiliza mecanismos como logs, backups e recuperação de transações para restaurar os dados a um estado consistente.

### Integridade

É a garantia de que os dados permaneçam válidos e de acordo com as regras definidas.

O SGBD utiliza restrições, como chaves primárias, chaves estrangeiras, valores obrigatórios e regras de domínio, para impedir dados inválidos.

### Redundância

É a existência de dados repetidos desnecessariamente.

O SGBD reduz a redundância principalmente por meio da organização adequada dos dados e da normalização, evitando que a mesma informação seja armazenada várias vezes.

### Inconsistência

Ocorre quando existem diferentes versões ou valores conflitantes para a mesma informação.

O SGBD ajuda a evitá-la por meio de restrições de integridade, controle de concorrência e transações, garantindo que as alterações sejam realizadas de forma controlada.