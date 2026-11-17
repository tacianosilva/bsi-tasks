# Tarefa 02 — Implementação do User Story da Iteração 1 e Atuação como QA

## 1. Identificação

- **Discente:** Hildemberg Eling de Araújo Lucena
- **Usuário GitHub:** [@Hildemberg986](https://github.com/Hildemberg986)
- **E-mail:** hildembergeling@gmail.com
- **Projeto de Grupo:** G5 — Comercializa
- **Colega de Equipe Auditado:** Arthur José dos Santos Azevedo ([@arthurazvd](https://github.com/arthurazvd))
- **Issue da Disciplina:** [#601](https://github.com/tacianosilva/bsi-tasks/issues/601)

---

## 2. Links de Entrega

- **Pull Request no Repositório do Projeto (Código + Testes):**  
  [https://github.com/arthurazvd/comercializa/pull/14](https://github.com/arthurazvd/comercializa/pull/14)
- **Relatório de Testes de Aceitação (QA) realizado para o Colega:**  
  [https://github.com/arthurazvd/comercializa/blob/task/t02-hildemberg/docs/qa/relatorio-qa-us14-arthur.md](https://github.com/arthurazvd/comercializa/blob/task/t02-hildemberg/docs/qa/relatorio-qa-us14-arthur.md)
- **SonarQube LABENS:**  
  [https://labens.dct.ufrn.br/sonarqube/dashboard?id=comercializa](https://labens.dct.ufrn.br/sonarqube/dashboard?id=comercializa)

---

## 3. Descrição das Atividades Realizadas

### 3.1 Papel de Analista e Desenvolvedor (User Story US15)

Na Iteração 1, foi implementada a **US15 — Ampliar testes de API e integração com Mock Objects e persistência**.

1. **Especificação BDD / Gherkin:**
   - Formalização de 4 cenários de aceitação em sintaxe Gherkin no documento `docs/11-user-stories.md` e documento de arquitetura em `docs/plans/2026-11-17-us15-api-integration-design.md`.
2. **Implementação de Testes Unitários com Mock Objects:**
   - Isolamento de serviços externos e persistência utilizando `unittest.mock.patch` e `MagicMock` em `backend/tests/test_us15_api_mocks.py`.
   - Simulação de exceções de integridade (`ProtectedError`) e validação da resposta tratada pelo viewset sem tocar no banco de dados.
   - Validação isolada de serializadores e cálculo de margem.
3. **Testes de Integração Funcional:**
   - Criação e validação de produtos e categorias via endpoints REST utilizando `APIClient`.
   - Validação de persistência real, códigos HTTP (201, 200, 400, 409), validação de schema e bloqueio de exclusão de produto com vendas vinculadas.
4. **Qualidade e Cobertura:**
   - Suíte com 163 testes passando com 100% de sucesso, 94% de cobertura no backend core e Quality Gate do SonarQube aprovado (0 bugs, 0 vulnerabilidades).

---

### 3.2 Papel de QA Engineer / Testador

Foi realizada a auditoria cruzada de aceitação sobre a implementação da **US14 (Ampliar testes automatizados dos modelos e regras de negócio)** do colega de equipe **Arthur Azevêdo** na Iteração 1.

- **Cenários Auditados:** Faturamento nunca negativo sob descontos extremos, produto em estoque mínimo gerando recomendação explicável de reposição no SAD e reflexo consistente de vendas no dashboard e estoque.
- **Evidências:** Relatório detalhado com metodologia, testes automatizados executados e parecer favorável documentado em `docs/qa/relatorio-qa-us14-arthur.md`.
