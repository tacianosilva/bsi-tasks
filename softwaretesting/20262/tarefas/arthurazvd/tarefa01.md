# Tarefa 01 - Teste de Unidade, Integração, Cobertura e CI

**Nome:** Arthur Azevêdo  
**GitHub:** arthurazvd  
**E-mail:** azvd.arthur@gmail.com  
**Projeto:** [Comercializa](https://github.com/arthurazvd/comercializa)

## 1. Testes de Software e Testes de Unidade

Testes de software são procedimentos utilizados para verificar se um sistema se comporta conforme o esperado e para identificar falhas antes que elas cheguem ao usuário. Eles ajudam a aumentar a confiabilidade do código e facilitam futuras alterações.

Os testes de unidade verificam pequenas partes do sistema de forma isolada, como funções, métodos ou classes. Dependências externas, como banco de dados ou serviços, podem ser substituídas por mocks. Dessa forma, o teste fica mais rápido e permite identificar com precisão em qual unidade ocorreu uma falha.

## 2. Linguagem e stack

O projeto Comercializa utiliza **Python** no backend, com **Django**, **Django REST Framework** e banco de dados **SQLite**. No frontend são utilizados **JavaScript**, **Vue 3**, **Vite** e **Axios**. Para os testes do backend são utilizados **pytest**, **pytest-django**, **pytest-cov**, **factory-boy** e `unittest.mock`.

## 3. Framework de Testes de Unidade

O framework escolhido foi o **pytest**. Ele permite escrever testes de forma simples utilizando funções e instruções `assert`, possui descoberta automática dos arquivos de teste e oferece suporte a fixtures e plugins. Neste projeto, o `pytest-django` permite testar componentes do Django e o `pytest-cov` calcula a cobertura do código.

- [Documentação do pytest](https://docs.pytest.org/)
- [Documentação do pytest-django](https://pytest-django.readthedocs.io/)
- [Documentação do pytest-cov](https://pytest-cov.readthedocs.io/)

## 4. IDE e ferramentas de debug

Utilizo o **Visual Studio Code**. A IDE possui suporte à depuração de Python por meio de breakpoints, execução passo a passo, inspeção de variáveis, pilha de chamadas e console de depuração. Também permite executar e depurar testes individualmente pela interface de testes. Para o frontend, as ferramentas do navegador ajudam a inspecionar componentes, requisições HTTP e mensagens do console.

- [Documentação de depuração em Python no VS Code](https://code.visualstudio.com/docs/python/debugging)

## 5. Tutorial de CRUD com testes

Foi utilizado como referência o [Quickstart do Django REST Framework](https://www.django-rest-framework.org/tutorial/quickstart/). O tutorial apresenta a criação de uma API CRUD usando modelos, serializers, viewsets e rotas. Ele também mostra como executar testes automatizados da API utilizando as ferramentas de teste do Django.

## 6. Mock Objects

Mock Objects são objetos simulados que substituem dependências reais durante um teste. Eles podem representar, por exemplo, um banco de dados, uma API externa ou outro serviço. Com mocks, é possível definir o retorno esperado e verificar se determinados métodos foram chamados corretamente. No Comercializa, os mocks foram usados nos testes unitários do serviço de produtos para testar as quatro operações do CRUD sem acessar o banco de dados real.

## 7. Implementação do CRUD e dos testes

O Comercializa possui um CRUD de produtos com as operações de inserir, consultar, atualizar e excluir. A API foi implementada com um `ModelViewSet` do Django REST Framework.

- [Implementação do CRUD](https://github.com/arthurazvd/comercializa/blob/main/backend/core/views.py)
- [Testes unitários do CRUD](https://github.com/arthurazvd/comercializa/blob/main/backend/tests/test_product_service.py)
- [Testes de integração da API](https://github.com/arthurazvd/comercializa/blob/main/backend/tests/test_api.py)

Foi implementado um teste unitário para cada operação do CRUD. Os testes utilizam `unittest.mock` para substituir o gerenciador do modelo e os métodos de persistência. A experiência permitiu verificar cada operação isoladamente, com testes rápidos e sem dependência do banco de dados.

Também foram implementados testes de integração que fazem requisições HTTP usando o `APIClient` e utilizam o banco de testes do Django. A principal diferença é que o teste de unidade verifica uma função isolada com dependências simuladas, enquanto o teste de integração verifica o funcionamento conjunto de rotas, serializers, modelos e banco de dados.

## 8. Execução dos testes e cobertura

O comando utilizado foi:

```bash
cd backend
pytest
```

Resultado obtido:

```text
collected 73 items
73 passed in 1.31s

Name                              Stmts   Miss  Cover
-----------------------------------------------------
TOTAL                               252     50    80%

Coverage HTML written to dir htmlcov
Coverage XML written to file coverage.xml
```

O relatório HTML é gerado em `backend/htmlcov/index.html`. O arquivo `backend/coverage.xml` é gerado no formato XML compatível com o SonarQube.

## 9. Integração Contínua

O GitHub Actions foi configurado para executar a instalação das dependências, os testes e a geração dos relatórios de cobertura em cada push para as branches `main` e `task/**`, além dos pull requests direcionados à `main`.

- [Workflow do GitHub Actions](https://github.com/arthurazvd/comercializa/blob/main/.github/workflows/tests.yml)
- [Execuções do GitHub Actions](https://github.com/arthurazvd/comercializa/actions)

O relatório `coverage.xml` e a pasta `htmlcov` são publicados como artefatos da execução do workflow.