# Tarefa 02 - Implementação do User Story da Iteração 1 e Atuação como QA

**Discente:** Paulo André Alves de Moura

**GitHub:** @pauloandrehxh

**E-mail:** paulo.moura.701@ufrn.edu.br

**Projeto:** [Arena UFRN](https://github.com/pauloandrehxh/arena-ufrn)

**Issue da disciplina:** [#471](https://github.com/tacianosilva/bsi-tasks/issues/471), com título ajustado para o nome completo do discente.

**Situação:** implementação, testes e QA publicados e integrados à main no [PR #11](https://github.com/pauloandrehxh/arena-ufrn/pull/11). CI da revisão final e da main concluídos com sucesso, incluindo envio ao SonarQube LABENS. Evidências reais abaixo; verificação autenticada de Quality Gate/issues e prints do dashboard continuam explicitamente pendentes.

Entrega individual baseada na US01 da Iteração 1, com QA da contribuição histórica de Luis Felipe na US02. Não são declarados resultados de testes, datas, análises ou aprovação de QA sem evidência.

## 1. Links de entrega

| Entrega | Situação |
|---|---|
| Pull Request da implementação no arena-ufrn | [PR #11](https://github.com/pauloandrehxh/arena-ufrn/pull/11), integrado à main |
| Relatório de Testes de Aceitação / QA da US02 de Luis Felipe | [Relatório na main, incluindo reteste](https://github.com/pauloandrehxh/arena-ufrn/blob/main/docs/qa/t2-us02-quadras.md) |
| Análise SonarQube LABENS | [Dashboard](https://labens.dct.ufrn.br/sonarqube/dashboard?id=arena-ufrn) e [evidência textual de CI/scanner](./evidencias/t2-ci-sonarqube.md); prints/Quality Gate autenticado ainda não obtidos |
| Issue da US01 no projeto | [#12](https://github.com/pauloandrehxh/arena-ufrn/issues/12), cadastrada retrospectivamente para rastreabilidade |
| CI da revisão integrada | [Run 37555641340](https://github.com/pauloandrehxh/arena-ufrn/actions/runs/37555641340), success |

Branch utilizada no projeto: `feature/us01-reservas`. Commits principais: `0b5f74f` (US01), `a6d4fc4` (QA), `344ce75` (correções de quadras), `65db27c` (integração das correções de Luis) e `89ac25f` (ajustes apontados pelo Sonar). PR #11 integrado em `3a5393ffbdf3fc292060276f5eae12e060c74a0c`. Branch da disciplina: `task/471`, atualizada com upstream/main `281a0dd`. A issue #12 foi criada após o desenvolvimento; não se presume cadastro anterior nem branch originalmente numerada pela issue.

## 2. User Story e especificação

**US01 — Reservar quadra (Iteração 1):** Como aluno, quero reservar uma quadra disponível para garantir meu horário de uso.

Analista/desenvolvedor: Paulo André. QA da minha história: Luis Felipe. A distribuição foi definida na regularização da P1, não apresentada como atribuição histórica.

Especificação, critérios e cenários BDD/Gherkin: [User Stories na main](https://github.com/pauloandrehxh/arena-ufrn/blob/main/docs/user-stories.md). Planejamento: [Iteração 1](https://github.com/pauloandrehxh/arena-ufrn/blob/main/docs/iteracoes/iteracao01.md). Documentos e relatório de QA estão publicados na main.

Contrato temporal aprovado: API recebe data `YYYY-MM-DD` e horários `HH:mm`, interpretados em `America/Fortaleza`. O dia é armazenado à meia-noite UTC por convenção de calendário, não como instante local do agendamento. Início deve estar no futuro, inclusive no dia atual.

## 3. Implementação realizada

Foi reutilizado o módulo de reservas existente, complementando:

- IDs inteiros positivos compatíveis com Prisma Int e calendário estrito, sem aceitar normalização silenciosa de datas como 30 de fevereiro.
- Formato/faixa dos horários, ordem início/fim e comparação com relógio local da UFRN.
- Normalização do dia e estado ATIVA fixado na criação; campos internos enviados não controlam o registro.
- Consulta apenas de conflitos ATIVA e transação envolvendo validação de usuário/quadra, conflito e criação.
- Respostas 400 para validação e 500 genérico para falhas inesperadas, sem exposição de detalhes internos.
- Regressões da atualização afetada pelas validações compartilhadas, sem implementar antecipadamente a US03 de cancelamento.
- Geração de Prisma no workflow com config explícita para viabilizar a nova suíte de persistência; execução remota verificada no run 37555641340.
- Correção por Paulo das validações de quadras encontradas no QA: IDs e nomes inválidos agora retornam 400, sem alterar dados; falhas inesperadas permanecem 500 genérico. Não atribuir essas correções a Luis Felipe.

Arquivos principais no arena-ufrn:

```text
backend/src/lib/reserva.validation.js
backend/src/services/reserva.service.js
backend/src/controllers/reserva.controller.js
backend/tests/unit/reserva.service.test.js
backend/tests/integration/reservas.integration.test.js
backend/tests/integration/reservas.persistencia.test.js
backend/tests/helpers/banco-teste.js
.github/workflows/backend-ci.yaml
```

O frontend não efetua reservas e a API ainda não tem autenticação: usar homologação restrita. Políticas de funcionamento, duração máxima e limites de uso não foram inventadas.

## 4. Testes, mocks e integração

Os unitários usam `jest.fn()`, retornos/erros simulados do Prisma e callback de transação mockado. O relógio é controlado para testar data passada, minuto corrente e diferença de dia entre UTC e Fortaleza.

A nova integração usa Supertest contra `createApp`, Prisma Client e SQLite temporário exclusivo. Aplica as migrations existentes, prepara dados sintéticos e remove apenas seu banco temporário. Não usa o banco de desenvolvimento.

Casos exercitados: criação/consulta real, tipos de sobreposição, intervalos contíguos, reservas CANCELADA, quadras/datas distintas, usuário/quadra inativos e duas requisições simultâneas. Na concorrência testada, uma respondeu 201, outra 400 e persistiu uma única reserva ATIVA. Isso não comprova múltiplos processos nem reagendamento concorrente.

## 5. Execução e cobertura

Ambiente: Linux, Node.js v22.12.0, pnpm 12.3.4 e Prisma Client 7.10.0.

Comandos executados durante o desenvolvimento, em `arena-ufrn/backend`:

```bash
pnpm prisma generate --config prisma7.config.ts
pnpm test:unit --runInBand
pnpm test:integration --runInBand
pnpm test:coverage --runInBand --coverageDirectory=/tmp/opencode/arena-ufrn-t2-coverage
```

A execução anterior passou 107 testes em sete suítes. Após corrigir as validações de quadras e acrescentar regressões, a execução atual passou **134 testes em sete suítes**. O QA é separado dessas contagens. A primeira tentativa atual falhou por falta de Prisma Client gerado; após `pnpm prisma generate --config prisma7.config.ts`, as suítes passaram. Os resultados históricos foram preservados.

| Escopo | Statements | Branches | Functions | Lines |
|---|---:|---:|---:|---:|
| Global backend na main | 77,99% | 71,25% | 90,32% | 77,99% |
| Service de reservas | 98% | 92% | 100% | 98% |
| Validação de reservas | 100% | 100% | 100% | 100% |

Evidência histórica transcrita: `docs/evidencias/t2-us01-execucao-testes-20261006.md`, produzida antes dos commits e mantida com seu contexto original. Na auditoria posterior, em 06/10/2026, os **107 testes em sete suítes passaram novamente** sobre a base publicada `da3f16a`, com as mesmas métricas. Comando: `pnpm test:coverage --runInBand --coverageDirectory=/tmp/opencode/arena-ufrn-t2-auditoria-coverage`. Evidência nova: `docs/evidencias/t2-auditoria-sonarqube.md`. LCOV/HTML não sobrescreveram o histórico. A execução de QA é separada e não está incluída nessas 107 contagens.

Na revisão integrada à main, os logs do CI confirmam **70 unitários + 64 de integração = 134 testes**, todos aprovados. A execução conjunta de cobertura repetiu os mesmos 134 testes; não somar as execuções como testes distintos. [Evidência final transcrita](./evidencias/t2-ci-sonarqube.md).

## 6. SonarQube

Configuração: scanner no GitHub Actions, projeto `arena-ufrn`, análise de backend/frontend e importação de LCOV. Os logs reais da revisão final do PR e da main registram **ANALYSIS SUCCESSFUL** e **EXECUTION SUCCESS**, com URL do dashboard LABENS. [Evidências, revisão analisada e transcrição](./evidencias/t2-ci-sonarqube.md).

Luis corrigiu CORS/catches e escopo das antigas validações no [PR #10](https://github.com/pauloandrehxh/arena-ufrn/pull/10), integrado à main e conciliado com a US01. Posteriormente o usuário informou apontamentos do LABENS sobre `responderErro` e `javascript:S7735`; Paulo moveu a função para o escopo do módulo e inverteu o ternário para condição positiva no commit `89ac25f`. Os 134 testes e o scanner passaram após essas correções.

O sucesso do scanner comprova envio da análise, **não aprovação do Quality Gate**. As APIs anônimas de métricas retornam 401; não foram obtidos prints do dashboard ou confirmação autenticada de ausência de issues remanescentes. Essa limitação fica explícita, sem inventar resultado SonarQube.

## 7. Atuação como QA

História planejada para avaliação: **US02 — Manter quadras**, de **Luis Felipe (@Luisfelipelinhares)**.

Foi obtida a branch histórica `origin/test/teste-de-quadras`, commit `51f6c381dba4a6d5aa00697f9f9e23d8394512db`, de Luis Felipe, associada ao [PR #3](https://github.com/pauloandrehxh/arena-ufrn/pull/3). Ela adiciona testes das rotas existentes, não todo o CRUD. Não foi localizada uma entrega posterior declarada como US02 refinada; confirmar com o colega. O QA executado é explicitamente retrospectivo contra os critérios atuais, sem inventar uma atribuição histórica.

Executei os sete testes originais da branch (todos passaram), depois **13 casos de aceite** contra seu `createApp`, usando Prisma e migrations atuais em SQLite temporário. Resultado: **7 Passou / 6 Falhou**. Repeti contra a aplicação atual e reproduzi os mesmos desvios. QA13 usa falha de dependência injetada; os demais usam banco real. O teste de preservação de reservas usa schema atual, pois a branch histórica não possuía esse modelo.

O QA histórico encontrou quatro grupos de bugs: ID não numérico retornava 500; cadastro aceitava nome vazio/espaços; nome ausente/numérico retornava 500; atualização persistia nome vazio. A contribuição histórica não foi aceita. Com autorização do usuário, **Paulo corrigiu esses bugs na branch atual** e executou novamente os 13 casos: **13 Passou, zero Falhou**, exit code 0. Isso não atribui as correções a Luis nem substitui o QA dele sobre a US01. O relatório mantém a avaliação histórica e uma seção separada de reteste.

Relatório: [Testes de Aceitação da US02 na main](https://github.com/pauloandrehxh/arena-ufrn/blob/main/docs/qa/t2-us02-quadras.md), com casos, evidências, reprodução e reteste publicado. Runner: `backend/tests/acceptance/quadras.qa.js`, comando `pnpm qa:quadras`. O runner retorna 1 quando há falhas e 0 quando todos passam; expectativas não foram alteradas para ocultar bugs.

Luis também publicou [seu relatório sobre a US01](https://github.com/pauloandrehxh/arena-ufrn/blob/main/docs/qa/t2-us01-reservas.md), commit `04357eb`. O documento lista expectativas e aprovação condicionada; ele ainda deve incluir resultados Passou/Falhou, observações e evidências por caso. Não foi alterado nem preenchido com resultados inventados por Paulo. Esse relatório é responsabilidade da entrega individual dele; o relatório de QA exigido na minha entrega é o que produzi sobre a US02.

## 8. Checklist de conclusão

- [x] Issue da disciplina identificada e branch local `task/471` existente.
- [x] User Story da I1, critérios e Gherkin documentados no projeto.
- [x] Implementação inicial da US01 em branch local própria.
- [x] Testes unitários com mocks e integração com persistência real implementados.
- [x] Testes e cobertura executados, com evidência registrada.
- [x] Página da T2 e link no README pessoal preparados.
- [x] Ajustar título da issue #471 e criar vínculo retrospectivo da US01 na issue #12 do projeto.
- [x] Atualizar main local e task/471 por fast-forward com upstream/main (`281a0dd`), preservando alterações locais.
- [x] Corrigir os apontamentos informados pelo discente e comprovar reexecução do scanner por logs do CI.
- [ ] Anexar prints/exportação autenticada de métricas/issues e verificar Quality Gate; não comprovado por logs do scanner.
- [x] Executar QA da contribuição histórica da US02 e criar relatório real; confirmar eventual branch refinada com Luis Felipe.
- [x] Publicar relatório histórico de QA e incluir link permanente de entrega.
- [x] Corrigir por Paulo os bugs de validação na branch atual e executar reteste com 13 casos aprovados.
- [x] Publicar correções e seção nova de reteste.
- [x] Documentos e implementação da US01 já publicados na branch do projeto.
- [x] Abrir PR da US01 no projeto incluindo relatório de QA: #11, integrado à main.

A entrega desta página utiliza a branch `task/471` no fork `pauloandrehxh/bsi-tasks`,
com commits Conventional Commits referenciando #471 e PR para a main do
`tacianosilva/bsi-tasks`. A publicação não comprova aprovação das pendências
de SonarQube indicadas acima nem o aceite pelo professor.
