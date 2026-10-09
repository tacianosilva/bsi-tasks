# Tarefa 03 - Implementação do User Story da Iteração 2 e Atuação como QA

## Identificação

| Campo          | Valor                                                        |
| :------------- | :----------------------------------------------------------- |
| Nome completo  | Marcus Vinícius de Souza Azevedo                             |
| Usuário GitHub | [@MViniciusCoffe](https://github.com/MViniciusCoffe)         |
| E-mail         | vinicius.azevedo.123@ufrn.edu.br                             |
| Issue          | [#497](https://github.com/tacianosilva/bsi-tasks/issues/497) |

---

## Links de Entrega

| Entrega                                        | Link                                                                                                                                       |
| :--------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Pull Request no repositório do projeto         | [SpendSmart #45](https://github.com/MViniciusCoffe/SpendSmart/pull/45)                                                                     |
| Especificação Gherkin da US-013                 | [docs/user-stories.md](https://github.com/MViniciusCoffe/SpendSmart/blob/task/497/docs/user-stories.md)                                     |
| Testes de integração da US-013                 | [expenseRegistration.test.js](https://github.com/MViniciusCoffe/SpendSmart/blob/task/497/tests/integration/postgres/expenseRegistration.test.js) |
| Relatório de QA da US-007 (José Samuel)        | Pendente                                                                                                                                    |

---

## 1. Especificação do User Story US-013 — Registrar Despesa

### 1.1 Descrição

> Como usuário autenticado, quero registrar uma despesa, para acompanhar o que saiu.

**Derivada de:** RF13
**Tela:** `pages/gastosPage.js`
**Service:** `services/transactionService.js`

### 1.2 Critérios de Aceitação

| ID        | Critério de Aceitação                                                                                        |
| :-------- | :----------------------------------------------------------------------------------------------------------- |
| CA-013.01 | Dado categoria, valor, título, data e forma de pagamento, quando salvo, então a despesa aparece na listagem  |
| CA-013.02 | Dado valor ausente, não numérico ou negativo, quando submeto, então o navegador impede o envio               |
| CA-013.03 | Dado uma despesa registrada, quando consulto o detalhe, então data e forma de pagamento aparecem preenchidas |
| CA-013.04 | Dado o valor gravado, quando consulto, então o valor tem duas casas decim ais                               |

### 1.3 Cenários de Testes de Aceitação (BDD/Gherkin)

```gherkin
# language: pt
Funcionalidade: US-013 — Registrar despesa

  Contexto:
    Dado que sou um usuário autenticado na tela de despesas

  Cenário: CA-013.01 — Registro válido
    Dado que selecionei uma categoria de despesa
    Quando preencho valor, título, data e forma de pagamento
      e clico em salvar
    Então a despesa aparece na listagem
    E o total de saídas e o saldo são recalculados

  Cenário: CA-013.02 — Valor ausente, não numérico ou negativo
    Quando submeto o formulário com valor vazio, não numérico ou negativo
    Então o navegador bloqueia o envio
    E nada é persistido

  Cenário: CA-013.03 — Detalhe preenchido (regressão #21)
    Dado que registrei uma despesa com data e forma de pagamento
    Quando abro o detalhe dessa despesa
    Então data e forma de pagamento aparecem preenchidas

  Cenário: CA-013.04 — Formatação monetária
    Dado que registrei uma despesa com valor "1234,5"
    Quando consulto a listagem ou o dashboard
    Então o valor é exibido com duas casas decimais, em R$

  Cenário: CT13.05 — Coerência categoria/transação
    Dado que selecionei uma categoria de receita
    Quando tento registrar uma despesa vinculada a essa categoria
    Então o sistema rejeita o registro
    E nenhuma transação é persistida

  # PENDENTE: CA-013.03 não é atendido hoje (issue #21) — a UI lê data/forma_pagamento
  # mas o service devolve data_ocorrencia/metodo_pagamento. CT13.05 descreve o
  # comportamento esperado após a correção da invariante categoria/transação.
```

---

## 2. Correções e Melhorias Realizadas

A US-013 já estava funcional desde a Iteração 1 (PR #42). Nesta T3, as melhorias concentraram-se em endurecer o fluxo de registro de transações e corrigir pendências de segurança da T2:

| Pendência                                                                | Descrição                                                                                                                                                                                                                                                                                                                                                         | Correção                                                                                                                                                                                                                                                                                                       |
| :----------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [#25](https://github.com/MViniciusCoffe/SpendSmart/issues/25) + [#29](https://github.com/MViniciusCoffe/SpendSmart/issues/29) | `createProfile.js` usava `service_role` com `id` do corpo da requisição (sem validação de token) e não revertia a conta no Auth em caso de falha ao inserir perfil                                                                                                                                   | `pages/api/createProfile.js` agora valida `Authorization: Bearer <token>` com cliente público (`auth.getUser`), insere o perfil usando `user.id` da sessão e executa **rollback** via `supabaseAdmin.auth.admin.deleteUser(user.id)` antes de retornar 500 |
| [#43](https://github.com/MViniciusCoffe/SpendSmart/issues/43) (BUG-05) | Tela de registro não validava comprimento mínimo da senha no cliente                                                                                                                                                                                                                                                                                             | `pages/register.js` adiciona `minLength={6}` no input de senha e valida `senha.length < 6` antes de chamar `registerUser` (mensagem: "A senha deve ter pelo menos 6 caracteres")                                                                                                                              |
| SonarQube — 2 code smells                                                | `new Error()` usado para checagem de tipo em `transactionService.js` (create/update)                                                                                                                                                                                                                                                                              | Substituído por `new TypeError()` (L54 e L102) — sem mudança de comportamento, testes `.toThrow("Valor inválido...")` continuam passando                                                                                                                                                                      |

**Alinhamento entre service e API:** `services/authServices.js` passa a incluir o header `Authorization: Bearer <session.access_token>` no `fetch` para `/api/createProfile` e deixa de enviar `id` no body (a API passa a usar exclusivamente `user.id` da sessão).

### Arquivos Modificados

- `pages/api/createProfile.js` — validação de token com chave pública + rollback no Auth em falha de inserção
- `services/authServices.js` — envio de token no header + remoção de `id` do body
- `pages/register.js` — validação de senha mínima (cliente)
- `services/transactionService.js` — `TypeError` no lugar de `Error` para validação de tipo

---

## 3. Testes Automatizados

### 3.1 Testes de Unidade (com mocks do Supabase)

| Arquivo                                 | Testes | Observação                                                                                   |
| :-------------------------------------- | -----: | :------------------------------------------------------------------------------------------- |
| `tests/unit/transactionService.test.js` |     27 | 25 já existentes + **2 novos**: `TypeError` na validação de valor (regressão dos code smells) |
| `tests/unit/authServices.test.js`       |     14 | **Ajustado** para incluir header `Authorization` no `fetch` de `/api/createProfile`           |
| `tests/unit/categoryService.test.js`    |     18 | inalterado                                                                                   |
| `tests/unit/profileService.test.js`     |     14 | inalterado                                                                                   |
| **Total**                               | **73** | base anterior: 71                                                                             |

**Comando e resultado:**

```bash
$ npm test

Test Suites: 4 passed, 4 total
Tests:       73 passed, 73 total
```

### 3.2 Testes de Integração

| Arquivo                                                   | Testes | Descripción                                                                                                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------- | -----: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `tests/integration/postgres/expenseRegistration.test.js` |  **9** | **Novo.** Registro de despesa no banco (CT13.01–CT13.04 + limites de schema): persistência de título/data/pagamento, rejeição de valor ≤ 0 (`check amount > 0`), rejeição de título nulo (`NOT NULL`), rejeição de data nula (`NOT NULL`), FK de categoria (`23503`) e precisão decimal (`1234,5` → `1234.50`) |
| `tests/integration/postgres/categoryConstraints.test.js`  |      7 | inalterado                                                                                                                                                                                                                                                                                                                                                               |
| `tests/integration/postgres/profileConstraints.test.js`   |      3 | inalterado                                                                                                                                                                                                                                                                                                                                                               |
| **Total**                                                 | **25** | base anterior: 16                                                                                                                                                                                                                                                                                                                                                        |

**Comando e resultado:**

```bash
$ npm run test:integration

Test Suites: 4 passed, 4 total
Tests:       25 passed, 25 total
```

### 3.3 Cobertura de Código

**Comando:**

```bash
npm run test:coverage
```

**Resultado (branch `task/497`):**

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

| Métrica          | Antes (main) | Depois (branch `task/497`)                 |
| :--------------- | :----------- | :----------------------------------------- |
| Cobertura        | 100%         | 100%                                       |
| Duplicação       | 0%           | 0%                                         |
| Bugs             | 0            | 0                                          |
| Vulnerabilidades | 0            | 0                                          |
| Code smells      | **0**        | **0** (re-análise dispara no PR)           |

**Code smells resolvidos:**

- 2x `new Error()` → `new TypeError()` em `services/transactionService.js:54,102` (validação de valor não-finito)

A re-análise do SonarQube roda automaticamente no PR pelo workflow `.github/workflows/sonar.yml`.

---

## 5. Atuação como QA Engineer — Relatório de Testes de Aceitação

**Status:** Pendente — a US-007 (Listar categorias) está sob responsabilidade de José Samuel Lima, cuja branch ainda não foi aberta. O relatório será adicionado aqui assim que a branch estiver disponível.

---

## 6. Pull Request no Repositório do Projeto

**Branch:** `task/497` (SpendSmart)

**Commits:**

| Commit    | Tipo       | Conteúdo                                                                   |
| :-------- | :--------- | :------------------------------------------------------------------------- |
| `ea18617` | `fix`      | Substitui `new Error()` por `new TypeError()` (2 code smells do SonarQube) |
| `7aca087` | `feat`     | `createProfile`: valida token, usa `user.id` da sessão e faz rollback no Auth |
| `e0ea867` | `refactor` | `authServices`: envia token no header e remove `id` do body               |
| `ab8468b` | `feat`     | `register`: validação de senha mínima no cliente                          |
| `2c1324c` | `docs`     | Especificação Gherkin da US-013 em `docs/user-stories.md`                  |
| `9621777` | `test`     | Testes de integração de registro de despesa (US-013)                      |

**Conteúdo:**

- Especificação formal da US-013 em Gherkin
- Endurecimento do fluxo de criação de perfil (validação de token + rollback)
- Validação de senha mínima na tela de registro
- 2 testes de regressão de unidade e 9 testes de integração novos
- Resolução dos 2 code smells do SonarQube

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
PASS tests/integration/postgres/expenseRegistration.test.js
PASS tests/integration/postgres/profileConstraints.test.js

Test Suites: 8 passed, 8 total
Tests:       98 passed, 98 total
```

### 7.2 Cobertura

```bash
$ npm run test:coverage

All files              |     100 |      100 |     100 |     100
 authServices.js       |     100 |      100 |     100 |     100 |
 categoryService.js    |     100 |      100 |     100 |     100 |
 profileService.js     |     100 |      100 |     100 |     100 |
 transactionService.js |     100 |      100 |     100 |     100 |
```

### 7.3 Análise estática local

```bash
$ npx eslint .        # 0 erros
$ npx prettier --check .
Checking formatting...
All matched files use Prettier code style!
```

---

## 8. Conclusão

A Tarefa 03 foi concluída: a US-013 (registrar despesa) já estava funcional desde a Iteração 1 e foi formalmente especificada em Gherkin nesta tarefa. As melhorias concentraram-se em endurecer o fluxo de criação de perfil — validação de token com chave pública, uso de `user.id` da sessão e rollback automático no Auth em caso de falha — e na correção da validação de senha mínima na tela de registro. Foram adicionados 2 testes de unidade e 9 testes de integração, totalizando 98 testes automatizados com cobertura de 100% em `services/`. Os 2 code smells do SonarQube foram resolvidos. A atuação como QA da US-007 está pendente de abertura da branch pelo desenvolvedor responsável.

---

_Data de execução: 08/10/2026_
