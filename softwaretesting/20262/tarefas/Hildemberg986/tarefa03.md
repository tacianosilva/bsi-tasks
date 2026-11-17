# Tarefa 03 — Implementação do User Story da Iteração 2 e Atuação como QA

## 1. Identificação

- **Discente:** Hildemberg Eling de Araújo Lucena
- **Usuário GitHub:** [@Hildemberg986](https://github.com/Hildemberg986)
- **E-mail:** hildembergeling@gmail.com
- **Projeto de Grupo:** G5 — Comercializa
- **Colega de Equipe Auditado:** Arthur José dos Santos Azevedo ([@arthurazvd](https://github.com/arthurazvd))
- **Issue da Disciplina:** [#599](https://github.com/tacianosilva/bsi-tasks/issues/599)

---

## 2. Links de Entrega

- **Pull Request no Repositório do Projeto (Código + Testes):**  
  [https://github.com/arthurazvd/comercializa/pull/13](https://github.com/arthurazvd/comercializa/pull/13)
- **Relatório de Testes de Aceitação (QA) realizado para o Colega:**  
  [https://github.com/arthurazvd/comercializa/blob/task/t03-hildemberg/docs/qa/relatorio-qa-it2-arthur.md](https://github.com/arthurazvd/comercializa/blob/task/t03-hildemberg/docs/qa/relatorio-qa-it2-arthur.md)
- **SonarQube LABENS:**  
  [https://labens.dct.ufrn.br/sonarqube/dashboard?id=comercializa](https://labens.dct.ufrn.br/sonarqube/dashboard?id=comercializa)

---

## 3. Descrição das Atividades Realizadas

### 3.1 Papel de Analista e Desenvolvedor (User Story US09)

Na Iteração 2, foi implementada a **US09 — Alertas inteligentes de produtos próximos do vencimento e análise de risco financeiro**.

1. **Especificação BDD / Gherkin:**
   - Formalização de 4 cenários de aceitação em sintaxe Gherkin no documento `docs/11-user-stories.md` e elaboração do documento de design de arquitetura em `docs/plans/2026-11-17-us09-expiration-alerts-design.md`.
2. **Implementação de Código:**
   - Criação do serviço de domínio `backend/core/expiration_service.py` com classificação por faixas de severidade (`vencido`, `critico`, `alerta` e `atencao`), cálculo do montante monetário de capital em risco financeiro (`quantidade × custo`) e ações recomendadas para apoio à decisão (SAD).
   - Criação da view REST `ExpirationAlertsView` em `backend/core/views.py` e rota `/api/alerts/expiration/` em `backend/core/urls.py`, suportando filtros e validações de parâmetros.
3. **Testes Automatizados:**
   - Implementação de 25 testes automatizados (unitários para partição de equivalência e valores-limite de datas, além de testes de integração via `APIClient`) em `backend/tests/test_expiration_alerts.py`.
   - **Resultados:** 181 testes passando com 100% de sucesso, 94% de cobertura no módulo core do backend e 100% de cobertura no novo serviço.
4. **Qualidade e SonarQube:**
   - Quality Gate aprovado, 0 bugs, 0 vulnerabilidades e ausência de code smells impeditivos.

---

### 3.2 Papel de QA Engineer / Testador

Foi realizada a auditoria cruzada de aceitação sobre a implementação da **US04 (Atualização automática de estoque após venda e integridade transacional)** do colega de equipe **Arthur Azevêdo** na Iteração 2.

- **Cenários Auditados:** Baixa regular de estoque, bloqueio de estoque negativo, atomicidade em vendas com múltiplos itens, recomposição de estoque e lotes em estorno e proteção de idempotência.
- **Evidências:** Relatório detalhado com metodologia, testes executados e parecer favorável documentado em `docs/qa/relatorio-qa-it2-arthur.md`.
