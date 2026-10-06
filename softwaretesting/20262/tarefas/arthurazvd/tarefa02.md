# Tarefa 02 - Implementação do User Story da Iteração 1 e Atuação como QA

## 1. Identificação

**Nome:** Arthur Azevêdo  
**Usuário GitHub:** `arthurazvd`  
**E-mail:** azvd.arthur@gmail.com
**Projeto:** Comercializa  
**Grupo:** G3 — Comercializa  
**Issue da disciplina:** #477  
**User Story implementada:** US14 — Ampliar testes automatizados dos modelos e regras de negócio

## 2. Links de Entrega

- **Repositório do projeto:** https://github.com/arthurazvd/comercializa
- **Pull Request da implementação:** https://github.com/arthurazvd/comercializa/pull/3
- **Relatório de Testes de Aceitação (QA):** https://github.com/arthurazvd/comercializa/blob/main/docs/qa/relatorio-qa-us14.md
- **Dashboard do SonarQube LABENS:** https://labens.dct.ufrn.br/sonarqube/dashboard?id=comercializa
- **Issue da disciplina:** https://github.com/tacianosilva/bsi-tasks/issues/477

## 3. User Story Implementada

### US14 — Ampliar testes automatizados dos modelos e regras de negócio

**Como** equipe de desenvolvimento,  
**quero** ampliar os testes automatizados dos modelos e regras de negócio,  
**para** reduzir regressões e aumentar a confiabilidade do sistema.

A US14 faz parte da Iteração 1 do projeto Comercializa e tem como objetivo ampliar a cobertura das regras de domínio, incluindo caminhos principais, casos limites e situações de erro.

A especificação da User Story foi detalhada no documento de User Stories do projeto, incluindo os cenários de Testes de Aceitação utilizando BDD/Gherkin.

## 4. Cenários de Aceitação

Foram definidos e executados cenários de aceitação para verificar as principais regras relacionadas à US14.

### CT-A01 — Faturamento nunca deve ser negativo

```gherkin
Dado que existem vendas no período analisado
E o valor total dos descontos é superior ao valor bruto vendido
Quando o dashboard calcular o faturamento
Então o faturamento apresentado deve ser igual a zero
E nunca deve ser apresentado um valor negativo
```

**Resultado:** PASSOU.

### CT-A02 — Produto no estoque mínimo deve gerar recomendação de reposição

```gherkin
Dado que existe um produto ativo
E seu estoque atual é igual ou inferior ao estoque mínimo configurado
Quando o dashboard analisar a situação do estoque
Então o produto deve ser classificado como estoque crítico
E deve existir uma recomendação de reposição para o produto
```

**Resultado:** PASSOU.

### CT-A03 — Venda deve atualizar estoque e dashboard

```gherkin
Dado que existe um produto ativo com estoque disponível
Quando uma venda desse produto for registrada pela API
Então a venda deve ser persistida
E o estoque do produto deve ser reduzido
E a quantidade de vendas apresentada no dashboard deve aumentar
E o faturamento do dashboard deve considerar a nova venda
```

**Resultado:** PASSOU.

## 5. Implementação

Durante a implementação da US14, foram realizadas alterações no serviço responsável pelas regras utilizadas pelo dashboard.

As regras de cálculo de faturamento e cálculo da quantidade sugerida para reposição foram separadas em funções específicas, permitindo que fossem verificadas isoladamente através de testes unitários.

Foram implementadas e utilizadas as funções:

- `calculate_revenue`;
- `calculate_restock_quantity`.

A função `dashboard_data` passou a utilizar essas funções para realizar os respectivos cálculos.

Essa alteração facilitou a criação de testes unitários para regras de negócio que anteriormente estavam concentradas dentro do serviço do dashboard.

## 6. Testes Unitários

Foi criado o arquivo:

`backend/tests/test_services_unit.py`

Foram adicionados testes automatizados para verificar, entre outros cenários:

- cálculo de faturamento sem desconto;
- cálculo de faturamento com desconto;
- garantia de que o faturamento nunca seja negativo;
- cálculo de reposição considerando o estoque mínimo;
- cálculo de reposição considerando a velocidade de vendas;
- garantia de sugestão mínima de uma unidade para reposição.

Os testes unitários adicionados foram executados com sucesso.

## 7. Utilização de Mock Objects

Para atender ao requisito de isolamento de dependências, foi utilizado `unittest.mock.patch`.

O Mock Object foi utilizado durante os testes do serviço de dashboard para substituir temporariamente uma dependência responsável pelo cálculo do faturamento.

Dessa forma, foi possível verificar isoladamente o comportamento do serviço, incluindo tanto o resultado retornado quanto a interação realizada com a função mockada.

## 8. Teste de Integração

Também foi implementado um teste de integração no arquivo:

`backend/tests/test_api.py`

O teste:

`teste_venda_atualiza_estoque_e_dashboard`

valida o fluxo integrado:

**API de vendas → persistência → atualização de estoque → serviço de dashboard → resposta da API**

Durante a execução, foi verificado que:

1. a venda é registrada através da API;
2. os dados da venda são persistidos;
3. o estoque do produto é reduzido;
4. a quantidade de vendas do dashboard é atualizada;
5. o faturamento apresentado pelo dashboard considera a nova venda.

**Resultado:** PASSOU.

## 9. Execução dos Testes e Cobertura

Após as alterações, a suíte automatizada completa do projeto foi executada.

**Resultado obtido:**

- **77 testes aprovados**;
- nenhuma regressão identificada;
- cobertura gerada utilizando `pytest-cov`;
- relatório `coverage.xml` gerado para utilização pelo SonarQube.

Também foram executados individualmente os novos testes unitários e o teste de integração durante o desenvolvimento.

## 10. Integração Contínua

O projeto possui workflow do GitHub Actions configurado para executar automaticamente os testes, gerar o relatório de cobertura e realizar a análise no SonarQube.

A Pull Request da US14 acionou o workflow de integração contínua e os checks foram executados com sucesso.

**Pull Request:** https://github.com/arthurazvd/comercializa/pull/3

## 11. Análise no SonarQube

O projeto Comercializa está configurado no SonarQube do LABENS.

O pipeline utiliza o relatório de cobertura gerado durante a execução dos testes e envia os resultados para análise no servidor do LABENS.

**Projeto no SonarQube:**  
https://labens.dct.ufrn.br/sonarqube/dashboard?id=comercializa

A execução da integração contínua relacionada à implementação foi concluída com sucesso.

## 12. Atuação como QA Engineer

A atividade prevê que o discente realize os Testes de Aceitação sobre a implementação de outro integrante da equipe.

Entretanto, o **G3 — Comercializa é composto apenas por Arthur Azevêdo**, não existindo outro integrante no grupo para realização do QA cruzado.

Diante dessa limitação, os cenários de aceitação definidos para a US14 foram executados sobre a própria implementação e documentados formalmente no Relatório de Testes de Aceitação.

Os três cenários de aceitação executados foram aprovados e não foram identificados bugs funcionais durante a validação.

**Relatório de QA:**  
https://github.com/arthurazvd/comercializa/blob/main/docs/qa/relatorio-qa-us14.md

## 13. Evidências

As principais evidências da realização da atividade estão disponíveis no histórico de commits e na Pull Request do projeto.

Commits relacionados à implementação:

- `4f8c6fd` — `docs: detalha cenarios de aceitacao da US14 #477`
- `bc357ac` — `test: amplia testes unitarios com mocks da US14 #477`
- `533b4bc` — `test: adiciona teste de integracao da US14 #477`
- `d4c4906` — `docs: adiciona relatorio de QA da US14 #477`

A Pull Request contém a implementação, os testes automatizados e o relatório de QA, além da execução dos checks da integração contínua.

## 14. Resultado Final

A implementação da US14 ampliou a verificação automatizada das regras de negócio do Comercializa através da adição de testes unitários, utilização de Mock Objects e criação de um novo teste de integração.

Os cenários de aceitação definidos em BDD/Gherkin foram executados com sucesso e documentados no relatório de QA.

A suíte automatizada permaneceu sem regressões, com **77 testes aprovados**, e a Pull Request da implementação apresentou os checks da integração contínua executados com sucesso.
