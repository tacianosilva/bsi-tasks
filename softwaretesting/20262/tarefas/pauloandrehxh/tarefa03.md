# Tarefa 03 - Implementação do User Story da Iteração 2 e Atuação como QA

**Discente:** Paulo André Alves de Moura

**GitHub:** @pauloandrehxh

**E-mail:** paulo.moura.701@ufrn.edu.br

**Projeto:** [Arena UFRN](https://github.com/pauloandrehxh/arena-ufrn)
**Issue da disciplina:** [#498](https://github.com/tacianosilva/bsi-tasks/issues/498)

## User Story

**US03 — Cancelar reserva:** Como aluno, quero cancelar uma reserva para liberar
um horário que não utilizarei. História da Iteração 2 definida na P1.

Issue do projeto: [#14](https://github.com/pauloandrehxh/arena-ufrn/issues/14).
PR da implementação: [arena-ufrn #15](https://github.com/pauloandrehxh/arena-ufrn/pull/15)
(**integrado à `main`**). Branch de entrega na disciplina: `task/498`.

## Implementação da US03

- PATCH `/api/reservas/:id/cancelamento`: 200 com o mesmo registro CANCELADA.
- DELETE delega ao cancelamento lógico e retorna 204, sem apagar histórico.
- CANCELADA é idempotente; inexistente 404; ID inválido 400.
- CONCLUIDA ou início já alcançado retornam 409. Fuso: America/Fortaleza.
- PUT não altera estado/campos internos nem dados de reserva cancelada, concluída
  ou iniciada. Gravação condicionada a ATIVA evita reativação concorrente.
- Cancelamento valida e altera estado na mesma transação, sem mudança de schema.
- Falhas inesperadas retornam 500 genérico. Autenticação depende da US05;
  incremento destinado à homologação restrita.

Especificação e Gherkin: [User Stories no projeto](https://github.com/pauloandrehxh/arena-ufrn/blob/main/docs/user-stories.md).
Casos de teste: `docs/iteracoes/iteracao02.md`, I2-CT01–CT07. O resultado da
automação não substitui o QA que Luis deve executar sobre a US03.

## Testes e cobertura

Execução final real em 09/10/2026, Node v22.12.0, pnpm 12.3.4, Prisma Client 7.10.0:

```bash
pnpm prisma generate --config prisma7.config.ts
pnpm test:coverage --runInBand --coverageDirectory=/tmp/opencode/arena-ufrn-t3-final-coverage
```

**192 testes passaram em nove suítes**. Unitários com mocks e integração real
com SQLite temporário e relógio controlado. Exercitados: preservação do histórico,
liberação do horário, idempotência, rejeições, fuso, falha real de UPDATE/rollback,
proteções do PUT e concorrência no mesmo client.

| Escopo | Statements | Branches | Functions | Lines |
|---|---:|---:|---:|---:|
| Backend | 80,92% | 74,86% | 91,54% | 80,86% |
| Service de reservas | 100% | 97,67% | 100% | 100% |

Evidência: [execução da US03](https://github.com/pauloandrehxh/arena-ufrn/blob/main/docs/evidencias/t3-us03-testes-20261008.md).
Os números são da revisão `5e5e36e` do PR #15, hoje integrado à `main`,
e não comprovam concorrência entre múltiplas instâncias.

## QA de Paulo sobre a US04 de Luis Felipe

Alvo: [PR #16 de Luis](https://github.com/pauloandrehxh/arena-ufrn/pull/16),
revisão `725274c`. A janela **08:00–22:00** e slots de **60 minutos** foram
confirmados para este QA pelo responsável pela T3. Os oito casos planejados
I2-CT09–CT16 **Passaram**. Um caso adicional de erro da dependência
**Falhou**: a rota devolve HTTP 400 com mensagem interna (`SEGREDO_QA_US04`)
quando o banco falha; o esperado é HTTP 500 sem dados internos. **8 Passou /
1 Falhou**. Correção pelo dev e reteste pendentes; US04 não aprovada sem ressalvas.
O PR avançou depois para `270402f`, alterando apenas a documentação de
evidências; o código testado não mudou. Se houver novas mudanças de código,
o resultado precisará de reteste.

Relatório reproduzível: `arena-ufrn/docs/qa/t3-us04-disponibilidade.md`, na
branch local `docs/t3-qa-us04` (link público pendente de publicação). Runner:
`backend/tests/acceptance/disponibilidade.qa.js`. Testes com Supertest,
SQLite temporário e dados sintéticos, sem alterar o PR do colega. O
[CI do PR #16](https://github.com/pauloandrehxh/arena-ufrn/actions/runs/38014945803)
passou 201 testes/10 suítes; cobertura global: 83,37% statements,
77,72% branches, 92,68% functions, 83,29% lines.

## Resultado da T3 e links de entrega

**Atuação de desenvolvimento e QA executada.** A US03 foi entregue no PR #15;
os oito cenários planejados de aceitação da US04 foram executados no PR #16
e passaram, mas o caso adicional QA09 falhou. **Não se afirma aprovação da
US04.** A falha não impede documentar e entregar o QA; sua correção e o reteste
ficam com o ciclo de revisão do PR #16. Não se afirma Quality Gate aprovado.

| Item | Situação |
|---|---|
| PR da US03 no projeto | [#15 integrado](https://github.com/pauloandrehxh/arena-ufrn/pull/15); falta vincular o relatório de QA depois de publicá-lo |
| QA de Paulo da US04 de Luis | Executado na revisão `725274c` do [PR #16](https://github.com/pauloandrehxh/arena-ufrn/pull/16); relatório e runner locais pendentes de publicação; 1 falha pendente |
| QA de Luis da US03 | [Modelo de relatório na `main`](https://github.com/pauloandrehxh/arena-ufrn/blob/main/docs/qa/t3-us03-cancelamentos.md), com resultados condicionados à confirmação prática; evidência independente de execução ainda não comprovada |
| SonarQube LABENS | Scanner do [CI da US03](https://github.com/pauloandrehxh/arena-ufrn/actions/runs/37988121948) e do [CI da US04](https://github.com/pauloandrehxh/arena-ufrn/actions/runs/38014945803) enviou análises; API do Quality Gate retornou 401, prints/problemas do dashboard pendentes |
| PR da tarefa na disciplina | Ainda não aberto |

O **relatório de QA exigido no enunciado já foi produzido e executado**; o
endereço público desse arquivo só poderá ser informado após a publicação da
branch `docs/t3-qa-us04`. Nesta revisão local, consulte o caminho
`arena-ufrn/docs/qa/t3-us04-disponibilidade.md`. Não substituir esse caminho
por um URL de arquivo ainda não publicado.

US04 é responsabilidade de Luis Felipe (@Luisfelipelinhares), com QA de Paulo.
O relatório da US03 publicado por Luis atribui pareceres "aprovado no modelo"
sem respostas/consultas efetivas por caso e menciona autorização de titular que
depende da US05. Não converter esse modelo em aprovação comprovada da US03.
Êxito do scanner não equivale a aprovação do Quality Gate.

O prazo escrito em T3.md é 06/10/2026, anterior ao início desta implementação.
Não se declara entrega retroativa nem prorrogação sem confirmação.
