# Tarefa 02 - Implementação do User Story da Iteração 1 e Atuação como QA

## Identificação

| Campo          | Valor                                                        |
| :------------- | :----------------------------------------------------------- |
| Nome completo  | Marcus Vinícius de Souza Azevedo                             |
| Usuário GitHub | [@MViniciusCoffe](https://github.com/MViniciusCoffe)         |
| E-mail         | vinicius.azevedo.123@ufrn.edu.br                             |
| Issue          | [#468](https://github.com/tacianosilva/bsi-tasks/issues/468) |

---

## Links de Entrega

| Entrega                                                                  | Link                                                                                                                                       |
| :----------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Pull Request no repositório do projeto                                   | [SpendSmart — branch `task/468` (`main...task/468`)](https://github.com/MViniciusCoffe/SpendSmart/compare/main...task/468)                 |
| Pull Request desta Tarefa (bsi-tasks)                                    | [#490](https://github.com/tacianosilva/bsi-tasks/pull/490)                                                                                 |
| Relatório de Testes de Aceitação (QA da US-001)                          | [acceptance-test-report-us-001.md](https://github.com/MViniciusCoffe/SpendSmart/blob/task/468/docs/acceptance-test-report-us-001.md)       |
| Relatório de QA da Iteração 1 (escrito pelo colega sobre a minha US-010) | [acceptance-test-report-iteration-1.md](https://github.com/MViniciusCoffe/SpendSmart/blob/main/docs/acceptance-test-report-iteration-1.md) |

---

## 1. Especificação do User Story US-010 — Registrar Receita

### 1.1 Descrição

> Como usuário autenticado, quero registrar uma receita, para acompanhar o que entrou.

**Derivada de:** RF10
**Tela:** `pages/rendaPage.js`
**Service:** `services/transactionService.js`

### 1.2 Critérios de Aceitação

| ID        | Critério de Aceitação                                                                                       |
| :-------- | :---------------------------------------------------------------------------------------------------------- |
| CA-010.01 | Dado categoria, valor, título, data e forma de pagamento, quando salvo, então a receita aparece na listagem |
| CA-010.02 | Dado valor ausente, não numérico ou zero, quando submeto, então o navegador impede o envio                  |
| CA-010.03 | Dado uma receita registrada, quando consulto, então o título e a data aparecem preenchidos no detalhe       |
| CA-010.04 | Dado o valor gravado, quando consulto, então o valor tem duas casas decimais e nunca é negativo             |

### 1.3 Cenários de Testes de Aceitação (BDD/Gherkin)

```gherkin
# language: pt
Funcionalidade: US-010 — Registrar receita

  Contexto:
    Dado que estou autenticado
    E estou na tela "Receitas", aba "Adicionar"

  Cenário: CA-010.01 — Registro válido aparece na listagem
    Quando preencho a categoria "Salário", o valor "2500,00", o título "Pagamento",
      a data "05/10/2026" e a forma de pagamento "Pix"
    E aciono "Salvar Renda"
    Então a receita é gravada vinculada ao meu usuário
    E ela passa a aparecer na listagem de receitas
    E o total de entradas do dashboard é recalculado

  Cenário: CA-010.02 — Valor vazio, não numérico ou zero
    Quando deixo o valor em branco
    Então o botão "Salvar Renda" permanece desabilitado
    E nenhuma requisição é enviada ao servidor

  Cenário: CA-010.03 — Detalhe preenchido
    Dado que registrei uma receita com título "Pagamento" e data "05/10/2026"
    Quando abro o detalhe dela
    Então o título "Pagamento" é exibido
    E a data "05/10/2026" é exibida

  Cenário: CA-010.04 — Formatação monetária
    Dado que registrei uma receita com valor "1234,5"
    Quando consulto o valor na listagem
    Então o valor é exibido como "R$ 1.234,50"
    E nunca é negativo
```

---

## 2. Implementação da Funcionalidade

### 2.1 Correções Realizadas

| Bug                                                           | Descrição                                                                                                                                                    | Correção                                                                                                                                                                                                                                                                                                                                                           |
| :------------------------------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [#10](https://github.com/MViniciusCoffe/SpendSmart/issues/10) | Receita salva sem título: o input "Nome da Renda" alimentava o estado `nome`, mas o envio usava `fonteRenda` — estado sem input, que nasce `""` e nunca muda | `pages/rendaPage.js` agora envia `titulo: nome` (estado `fonteRenda` removido); além disso `createTransaction`/`updateTransaction` **validam a fronteira**: título vazio ou só espaços é rejeitado antes de tocar o banco (regressão garantida por teste de unidade)                                                                                               |
| [#21](https://github.com/MViniciusCoffe/SpendSmart/issues/21) | Detalhe de transação sempre vazio: a UI lia `data`/`forma_pagamento`, que não existem no DTO — o service devolve `data_ocorrencia`/`metodo_pagamento`        | Três acessos corrigidos (`pages/rendaPage.js` e `pages/gastosPage.js`); contrato tornou-se simétrico: `get`, `create` e `update` devolvem **exatamente as mesmas chaves**, todas definidas em um único lugar (`transactionTypeMap` em `services/transactionService.js` e `categoryTypeMap` em `services/categoryService.js`) — critérios de conclusão da issue #21 |

### 2.2 Arquivos Modificados

- `pages/rendaPage.js` — envio do título pelo campo correto (#10) e leitura do detalhe por `data_ocorrencia` (#21)
- `pages/gastosPage.js` — detalhe lê `data_ocorrencia` e `metodo_pagamento` (#21)
- `services/transactionService.js` — validação de título (#10), contrato documentado (#21) e limpeza de code smells
- `services/categoryService.js`, `services/authServices.js`, `services/profileService.js` — limpeza de code smells (Seção 4)
- `tests/unit/transactionService.test.js` — 6 testes de regressão novos (#10 e #21)
- `tests/integration/postgres/incomeRegistration.test.js` — nova suíte de integração da US-010

---

## 3. Testes Automatizados

### 3.1 Testes de Unidade (com mocks do Supabase)

| Arquivo                                 | Testes | Observação                                                                                                                                                                               |
| :-------------------------------------- | -----: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `tests/unit/transactionService.test.js` |     25 | 19 já existentes + **6 novos**: validação de título vazio (regressão #10) e simetria do DTO (`data_ocorrencia`/`metodo_pagamento` existem, `data`/`forma_pagamento` não — regressão #21) |
| `tests/unit/authServices.test.js`       |     14 | inalterado                                                                                                                                                                               |
| `tests/unit/categoryService.test.js`    |     18 | inalterado                                                                                                                                                                               |
| `tests/unit/profileService.test.js`     |     14 | inalterado                                                                                                                                                                               |
| **Total**                               | **71** | base anterior: 65                                                                                                                                                                        |

**Comando e resultado:**

```bash
$ npm test

Test Suites: 4 passed, 4 total
Tests:       71 passed, 71 total
```

### 3.2 Testes de Integração

| Arquivo                                                  | Testes | Descrição                                                                                                                                                                                                                                                                                                                                 |
| :------------------------------------------------------- | -----: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `tests/integration/postgres/incomeRegistration.test.js`  |  **6** | **Novo.** Registro de receita no banco (CT10.01/CT10.02): persistência de título/data/pagamento (regressão #21), soma de `type = 'income'`, rejeição de valor ≤ 0 (`check amount > 0`), rejeição de título nulo (`NOT NULL`), documentação do limite do banco (`''` passa no NOT NULL — por isso o serviço valida, #10) e FK de categoria |
| `tests/integration/postgres/categoryConstraints.test.js` |      7 | inalterado                                                                                                                                                                                                                                                                                                                                |
| `tests/integration/postgres/profileConstraints.test.js`  |      3 | inalterado                                                                                                                                                                                                                                                                                                                                |
| **Total**                                                | **16** | base anterior: 10                                                                                                                                                                                                                                                                                                                         |

**Comando e resultado:**

```bash
$ npm run test:integration

Test Suites: 3 passed, 3 total
Tests:       16 passed, 16 total
```

### 3.3 Cobertura de Código

**Comando:**

```bash
npm run test:coverage
```

**Resultado (branch `task/468`):**

```
-----------------------|---------|----------|---------|---------|
File                   | % Stmts | % Branch | % Funcs | % Lines |
-----------------------|---------|----------|---------|---------|
All files              |     100 |      100 |     100 |     100 |
 authServices.js       |     100 |      100 |     100 |     100 |
 categoryService.js    |     100 |      100 |     100 |     100 |
 profileService.js     |     100 |      100 |     100 |     100 |
 transactionService.js |     100 |      100 |     100 |     100 |
-----------------------|---------|----------|---------|---------|
```

---

## 4. Análise Estática — SonarQube

**Projeto:** [spendsmart no LABENS](http://labens.dct.ufrn.br/sonarqube/dashboard?id=spendsmart)

| Métrica          | Antes (main) | Depois (branch `task/468`)                 |
| :--------------- | :----------- | :----------------------------------------- |
| Cobertura        | 100%         | 100%                                       |
| Duplicação       | 0%           | 0%                                         |
| Bugs             | 0            | 0                                          |
| Vulnerabilidades | 0            | 0                                          |
| Code smells      | **14**       | **0 no código** (re-análise dispara no PR) |

**Code smells resolvidos:**

- 12x `S2223` — `try { } catch (e) { throw e; }` removidos dos quatro arquivos de `services/` (o catch só relançava; comportamento preservado, suíte verde após a mudança)
- 2x `parseFloat` → `Number.parseFloat` em `services/transactionService.js`

**Verificação local:**

```bash
$ grep -rn "catch (error)" -A1 services/ | grep -c "throw error"
0
$ npx eslint .   # 0 erros (apenas warnings pré-existentes de no-alert/exhaustive-deps)
$ npx prettier --check .   # All matched files use Prettier code style!
```

A re-análise do SonarQube roda automaticamente no PR pelo workflow `.github/workflows/sonar.yml`
(ao menos um push em `main` ou uma PR); o dashboard passa a mostrar 0 code smells após essa
execução. Registro da configuração e das 14 ocorrências originais:
[docs/sonarqube.md](http://github.com/MViniciusCoffe/SpendSmart/blob/main/docs/sonarqube.md).

---

## 5. Atuação como QA Engineer — Relatório de Testes de Aceitação

Relatório completo: [docs/acceptance-test-report-us-001.md](https://github.com/MViniciusCoffe/SpendSmart/blob/task/468/docs/acceptance-test-report-us-001.md)

### 5.1 Escopo

| Campo                    | Valor                                                  |
| :----------------------- | :----------------------------------------------------- |
| QA Engineer              | Marcus Vinícius — `@MViniciusCoffe`                    |
| Desenvolvedor da US      | José Samuel Lima — `@Jose-Samuel-Lima`                 |
| Escopo                   | US-001 — Criar conta (CA-001.01 a CA-001.04 + CT01.04) |
| Branch / commit testados | `main` / `b7a0a28`                                     |
| Data da execução         | 2026-10-07                                             |

### 5.2 Resumo da Execução

| Status            | Quantidade                                  |
| :---------------- | :------------------------------------------ |
| ✅ Passaram       | 2 (CA-001.02, CA-001.04)                    |
| ❌ Falharam       | 2 (CA-001.03, CT01.04)                      |
| ⏭️ Não executados | 1 (CA-001.01 — exige backend Supabase real) |
| 🚫 Bloqueados     | 0                                           |

### 5.3 Bugs Encontrados

| ID    | Severidade | Descrição                                                                                                                                                                                                                                         |
| :---- | :--------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| QA-01 | Média      | Registro não bloqueia senha com menos de 6 caracteres no cliente — `pages/register.js:23-26, 86-96` (é o BUG-05 já apontado pelo QA da I1; issue a abrir — o token de automação do ambiente não tem permissão de escrita em issues)               |
| QA-02 | **Alta**   | A issue [#25](https://github.com/MViniciusCoffe/SpendSmart/issues/25) (rollback do cadastro) foi fechada como COMPLETED, mas **não existe código de rollback em `main` nem em nenhuma branch** — CT01.04 continua reprovado; recomenda reabertura |

### 5.4 Parecer do QA

**Resultado:** ☒ Reprovado (2 de 5 casos aprovados)

**Justificativa:** o entregável central da US-001 na Iteração 1 — o rollback do cadastro da
issue #25 — não está implementado em `main`, embora a issue apareça fechada; e CA-001.03 segue
falhando. O aceite depende de:

1. Implementação e teste do rollback (#25), com reabertura da issue
2. Validação de senha mínima no cliente (QA-01)
3. Execução manual de CT01.01–CT01.03 em navegador com `.env.development` válido

---

## 6. Pull Request no Repositório do Projeto

**PR:** [SpendSmart — `compare/main...task/468`](https://github.com/MViniciusCoffe/SpendSmart/compare/main...task/468)
(branch `task/468`, 4 commits — o PR é aberto a partir deste compare)

**Commits:**

| Commit    | Tipo       | Conteúdo                                                           |
| :-------- | :--------- | :----------------------------------------------------------------- |
| `0934937` | `fix`      | Grava título da receita e alinha o detalhe ao DTO (#10, #21)       |
| `4493f14` | `test`     | Regressões de unidade (#10, #21) + suíte de integração da US-010   |
| `7cf8eb4` | `refactor` | Remove catch só relança e usa `Number.parseFloat` (14 code smells) |
| `50d4cf7` | `docs`     | Relatório de QA da US-001                                          |

**Conteúdo:**

- Implementação das correções dos bugs #10 e #21 com validação de fronteira
- 6 testes de unidade de regressão e 6 testes de integração novos (87/87 no total)
- Limpeza dos 14 code smells apontados pelo SonarQube
- Relatório de Testes de Aceitação (QA) da US-001

---

## 7. Evidências

### 7.1 Execução da suíte completa (unidade + integração)

```bash
$ npx jest tests/unit tests/integration/postgres --runInBand

PASS tests/unit/authServices.test.js
PASS tests/unit/categoryService.test.js
PASS tests/unit/profileService.test.js
PASS tests/unit/transactionService.test.js
PASS tests/integration/postgres/categoryConstraints.test.js
PASS tests/integration/postgres/incomeRegistration.test.js
PASS tests/integration/postgres/profileConstraints.test.js

Test Suites: 7 passed, 7 total
Tests:       87 passed, 87 total
```

### 7.2 Cobertura

```bash
$ npm run test:coverage

All files              |     100 |      100 |     100 |     100
 authServices.js       |     100 |      100 |     100 |     100
 categoryService.js    |     100 |      100 |     100 |     100
 profileService.js     |     100 |      100 |     100 |     100
 transactionService.js |     100 |      100 |     100 |     100
```

### 7.3 Análise estática local (pré-condição do SonarQube limpo)

```bash
$ npx eslint .        # 0 erros
$ npx prettier --check .
Checking formatting...
All matched files use Prettier code style!
```

---

## 8. Conclusão

A Tarefa 02 foi concluída: a US-010 foi implementada na branch `task/468` do SpendSmart (correções
#10 e #21 com validação de fronteira), ampliada com 6 testes de regressão de unidade e uma suíte
de integração de 6 casos, cobertura de 100% em `services/` e os 14 code smells do SonarQube
resolvidos no código. Atuei como QA da US-001 de José Samuel Lima com relatório publicado em
`docs/acceptance-test-report-us-001.md` — parecer reprovado, com os achados QA-01 (senha mínima no
cliente) e QA-02 (issue #25 fechada sem a correção no código) registrados para o fechamento da
Iteração 1.

---

_Data de execução: 07/10/2026_
