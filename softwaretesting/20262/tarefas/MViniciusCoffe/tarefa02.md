# Tarefa 02 - Implementação do User Story da Iteração 1 e Atuação como QA

## Identificação

| Campo | Valor |
|:------|:------|
| Nome completo | Marcus Vinícius de Souza Azevedo |
| Usuário GitHub | [@MViniciusCoffe](https://github.com/MViniciusCoffe) |
| E-mail | vinicius.azevedo.123@ufrn.edu.br |
| Issue | [#468](https://github.com/tacianosilva/bsi-tasks/issues/468) |

---

## Links de Entrega

| Entrega | Link |
|:--------|:-----|
| Pull Request no repositório do projeto | [SpendSmart PR #42](https://github.com/MViniciusCoffe/SpendSmart/pull/42) |
| Relatório de Testes de Aceitação (QA) | [acceptance-test-report-iteration-1.md](https://github.com/MViniciusCoffe/SpendSmart/blob/main/docs/acceptance-test-report-iteration-1.md) |

---

## 1. Especificação do User Story US-010 — Registrar Receita

### 1.1 Descrição

> Como usuário autenticado, quero registrar uma receita, para acompanhar o que entrou.

**Derivada de:** RF10
**Tela:** `pages/rendaPage.js`
**Service:** `services/transactionService.js`

### 1.2 Critérios de Aceitação

| ID | Critério de Aceitação |
|:---|:----------------------|
| CA-010.01 | Dado categoria, valor, título, data e forma de pagamento, quando salvo, então a receita aparece na listagem |
| CA-010.02 | Dado valor ausente, não numérico ou zero, quando submeto, então o navegador impede o envio |
| CA-010.03 | Dado uma receita registrada, quando consulto, então o título e a data aparecem preenchidos no detalhe |
| CA-010.04 | Dado o valor gravado, quando consulto, então o valor tem duas casas decimais e nunca é negativo |

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

| Bug | Descrição | Correção |
|:----|:----------|:---------|
| #10 | Receita salva sem título (input ligado a `nome`, envio usa `fonteRenda`) | Corrigido o vínculo do campo de título no formulário de receitas |
| #21 | Detalhe de transação sempre vazio (UI lê `data`/`forma_pagamento`, service devolve `data_ocorrencia`/`metodo_pagamento`) | Alinhado o contrato de DTO entre UI e service |

### 2.2 Arquivos Modificados

- `pages/rendaPage.js` — correção do vínculo do campo de título
- `services/transactionService.js` — alinhamento do contrato de DTO

---

## 3. Testes Automatizados

### 3.1 Testes de Unidade

| Arquivo | Testes | Cobertura |
|:--------|:-------|:----------|
| `tests/unit/transactionService.test.js` | 22 testes | 100% |

**Comando de execução:**
```bash
npm test
```

**Resultado:**
```
Test Suites: 4 passed, 4 total
Tests:       65 passed, 65 total
```

### 3.2 Testes de Integração

| Arquivo | Testes | Descrição |
|:--------|:-------|:----------|
| `tests/integration/postgres/transactionConstraints.test.js` | 3 testes | Valida constraints de transações no banco |

**Comando de execução:**
```bash
npm run test:integration
```

### 3.3 Cobertura de Código

**Comando:**
```bash
npm run test:coverage
```

**Resultado:**
```
All files              |     100 |      100 |     100 |     100
 authServices.js       |     100 |      100 |     100 |     100
 categoryService.js    |     100 |      100 |     100 |     100
 profileService.js     |     100 |      100 |     100 |     100
 transactionService.js |     100 |      100 |     100 |     100
```

---

## 4. Análise Estática — SonarQube

**Projeto:** [spendsmart no LABENS](http://labens.dct.ufrn.br/sonarqube/dashboard?id=spendsmart)

| Métrica | Valor |
|:--------|:------|
| Cobertura | 100% |
| Duplicação | 0% |
| Bugs | 0 |
| Vulnerabilidades | 0 |
| Code smells | 14 |

**Code smells identificados:**
- 12x `S2223` — catch só relança (em `services/`)
- 2x `Number.parseFloat` sobre `parseFloat` (em `transactionService.js`)

---

## 5. Atuação como QA Engineer — Relatório de Testes de Aceitação

### 5.1 Escopo

| Campo | Valor |
|:------|:------|
| QA Engineer | Marcus Vinícius — `@MViniciusCoffe` |
| Desenvolvedor da US | José Samuel — `@Jose-Samuel-Lima` |
| Escopo | US-001 — Criar conta (CT01.01 a CT01.04) |
| Branch testada | `main` |
| Data da execução | 2026-10-06 |

### 5.2 Resumo da Execução

| Status | Quantidade |
|:-------|:-----------|
| Passaram | 2 |
| Falharam | 2 |
| Não executados | 0 |
| Bloqueados | 0 |

### 5.3 Bugs Encontrados

| ID | Severidade | Descrição |
|:---|:-----------|:----------|
| BUG-01 | Crítica | `/api/createProfile` aceita escrita sem token |
| BUG-02 | Alta | Cadastro sem rollback deixa conta órfã |
| BUG-03 | Média | Registro não bloqueia senha com menos de 6 caracteres no cliente |
| BUG-04 | Alta | Tela de perfil nunca exibe os dados atuais |

### 5.4 Parecer do QA

**Resultado:** Reprovado (estado anterior à correção)

**Justificativa:** Os casos de regressão CT01.01 e CT01.04 falham pelos defeitos conhecidos #25 e #29. O aceite depende de:
1. Reteste aprovado de CT01.01 e CT01.04 sobre a branch de correção
2. Decisão do time sobre o BUG-01 (crítico, fora do plano original da I1)

---

## 6. Pull Request no Repositório do Projeto

**PR:** [#42 - Implementação da US-010 e QA da US-001](https://github.com/MViniciusCoffe/SpendSmart/pull/42)

**Conteúdo:**
- Implementação das correções dos bugs #10 e #21
- Testes de unidade e integração
- Relatório de Testes de Aceitação da US-001

---

## 7. Evidências

### 7.1 Execução dos Testes

```bash
$ npm test

PASS tests/unit/authServices.test.js
PASS tests/unit/categoryService.test.js
PASS tests/unit/profileService.test.js
PASS tests/unit/transactionService.test.js

Test Suites: 4 passed, 4 total
Tests:       65 passed, 65 total
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

---

## 8. Conclusão

A Tarefa 02 foi concluída com sucesso. A US-010 foi implementada e testada, os bugs conhecidos foram corrigidos, e o relatório de QA da US-001 foi elaborado e documentado no repositório do grupo.

---

_Data de execução: 06/10/2026_
