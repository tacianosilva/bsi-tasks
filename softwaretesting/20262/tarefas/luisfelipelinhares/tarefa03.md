# US03 — Cancelamento de Reservas

## 1. Identificação

- **Projeto:** Arena UFRN
- **User Story:** US03 — Cancelar Reservas
- **Iteração:** 2
- **Branch de referência:** `feature/14-cancelamento-reservas`
- **Repositório:** [arena-ufrn](https://github.com/pauloandrehxh/arena-ufrn)

## 2. Descrição

Como usuário que possui uma reserva, quero cancelar uma reserva previamente realizada, para liberar o horário reservado caso não possa mais utilizá-lo.

## 3. Critérios de Aceitação

### CA01 — Cancelamento de reserva ativa

O sistema deve permitir o cancelamento de uma reserva ativa, atualizando seu status para cancelada.

### CA02 — Atualização do status

Após o cancelamento, a reserva deve permanecer registrada no sistema, com seu status atualizado, preservando o histórico.

### CA03 — Reserva inexistente

Ao tentar cancelar uma reserva que não existe, o sistema deve informar que a reserva não foi encontrada.

### CA04 — Reserva já cancelada

Ao tentar cancelar novamente uma reserva cancelada, o sistema deve tratar a solicitação de forma apropriada, sem produzir alterações indevidas.

### CA05 — Disponibilização do horário

Após o cancelamento, o horário da reserva deve deixar de ser considerado ocupado, desde que não exista outra reserva ativa no mesmo período.

*Observação: os critérios acima constituem a especificação proposta para os testes. Devem ser comparados com as regras oficiais da US03 e com a implementação da branch.*

## 4. Cenários de Testes de Aceitação — BDD/Gherkin

### Cenário 1 — Cancelar uma reserva ativa

**Dado que** existe uma reserva ativa pertencente ao usuário  
**Quando** o usuário solicita o cancelamento dessa reserva  
**Então** o sistema deve cancelar a reserva e atualizar seu status.

### Cenário 2 — Preservar o registro da reserva

**Dado que** uma reserva foi cancelada com sucesso  
**Quando** o sistema consulta o registro dessa reserva  
**Então** a reserva deve continuar registrada com o status de cancelada.

### Cenário 3 — Tentar cancelar uma reserva inexistente

**Dado que** não existe uma reserva com o identificador informado  
**Quando** o usuário solicita seu cancelamento  
**Então** o sistema deve informar que a reserva não foi encontrada.

### Cenário 4 — Tentar cancelar uma reserva já cancelada

**Dado que** uma reserva já possui status de cancelada  
**Quando** o usuário solicita novamente seu cancelamento  
**Então** o sistema deve tratar a solicitação sem alterar indevidamente os dados da reserva.

### Cenário 5 — Liberar o horário após o cancelamento

**Dado que** uma reserva ativa ocupa determinado horário  
**Quando** a reserva é cancelada com sucesso  
**Então** o horário deve voltar a ser considerado disponível, desde que não haja outra reserva ativa ocupando o período.

### Cenário 6 — Impedir cancelamento de reserva de outro usuário

**Dado que** existe uma reserva pertencente a outro usuário  
**Quando** um usuário sem autorização tenta cancelá-la  
**Então** o sistema deve impedir a operação e retornar uma resposta apropriada.

*Este cenário deve ser validado conforme as regras de autenticação e autorização implementadas no projeto.*

## 5. Plano de Testes

Os testes devem verificar:

- O cancelamento bem-sucedido de uma reserva ativa.
- A atualização do status da reserva.
- A preservação do histórico.
- O tratamento de identificadores inexistentes.
- O tratamento de solicitações repetidas.
- A liberação do horário após o cancelamento.
- A autorização para cancelar a reserva.

## 6. Resultado da Execução

O resultado dos testes de aceitação deve ser preenchido após a execução da branch `feature/14-cancelamento-reservas`.

- **Total de cenários:** 6.
- **Aprovados:** Pendente de execução.
- **Reprovados:** Pendente de execução.
- **Bloqueados:** Pendente de execução.

## 7. Conclusão

A US03 tem como objetivo garantir que o cancelamento de reservas seja realizado de forma consistente, preservando o histórico e evitando que reservas canceladas continuem bloqueando horários. A aprovação definitiva depende da execução dos cenários e da comparação dos resultados com a especificação oficial.