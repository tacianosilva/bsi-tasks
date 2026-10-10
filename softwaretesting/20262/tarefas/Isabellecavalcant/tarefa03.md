# Tarefa 03 - Implementação do User Story da Iteração 2 e Atuação como QA

## Identificação

- Nome: Isabelle Cavalcanti da Silva
- GitHub: Isabellecavalcant
- E-mail: isabelle.silva.712@ufrn.edu.br
- Issue: https://github.com/tacianosilva/bsi-tasks/issues/500
- Equipe: G1 — HBL Control / Projeto PNLD

## Projeto e links de entrega

- Repositório: https://github.com/HelenaMariano2025/projetoPNLD
- User Story implementada: US05 — Gerenciar livros
- Branch de desenvolvimento: feat/us05-gerenciar-livros
- Pull Request da implementação e testes: https://github.com/HelenaMariano2025/projetoPNLD/pull/16
- Relatório de Testes de Aceitação da US04: https://github.com/HelenaMariano2025/projetoPNLD/blob/docs/qa-us04-500/docs/qa/relatorio-aceitacao-jaineII.md
- Pull Request do relatório e evidências: https://github.com/HelenaMariano2025/projetoPNLD/pull/20
- Pull Request testado como QA: https://github.com/HelenaMariano2025/projetoPNLD/pull/19

## Especificação

A especificação da US05 e seus cenários de aceitação em Gherkin foram preparados anteriormente.

Também atuei como analista da US04 — Gerenciar turmas, utilizada na execução dos testes de aceitação desta entrega.

## Implementação da US05

Foram implementadas ou ajustadas as seguintes funcionalidades:

- Cadastro de livros com ISBN, título, autor, código da editora, ano, situação, edição e quantidade disponível.
- Validação dos dados de cadastro e edição por meio da classe LivroValidator.
- Consulta do acervo, incluindo livros inativos e sem estoque.
- Pesquisa de livros pelo título.
- Edição dos dados de livros.
- Exclusão de livros sem registros de empréstimo.
- Bloqueio da exclusão de livros com empréstimos vinculados, preservando o histórico.
- Verificação de autenticação nas telas de gerenciamento.
- Consultas parametrizadas e escape dos dados apresentados no HTML.
- Mensagens de confirmação e de erro nas operações.

### Arquivos principais

- add_livro.php
- editar_livro.php
- excluir_livro.php
- livros.php
- php/LivroRepository.php
- php/LivroValidator.php

### Arquivos de testes

- tests/LivroRepositoryTest.php
- tests/LivroRepositoryIntegrationTest.php
- tests/LivroExclusaoTest.php
- tests/LivroExclusaoIntegrationTest.php
- tests/LivroValidatorTest.php

### Commits registrados

- 95c493f — Validação dos dados de livros e testes unitários.
- c034214 — Integração das telas ao gerenciamento de livros.
- 56523de — Teste de integração do bloqueio de exclusão com vínculos.
- 6d7583b — Preparação e limpeza dos dados dos testes de integração.
- 9d460f4 — Relatório de aceitação da US04 e evidências.

Os commits utilizaram Conventional Commits com referência à issue tacianosilva/bsi-tasks#500.

## Testes automatizados

Os testes unitários utilizaram mocks para isolar as operações da conexão e dos statements MySQL. Os testes de integração utilizaram um banco MySQL real.

Foram verificados cadastro, consulta, atualização, exclusão, bloqueio de exclusão com vínculos e validação dos dados.

### Resultados registrados

| Execução | Testes | Asserções | Resultado |
| --- | ---: | ---: | --- |
| Filtro Livro | 19 | 94 | Passou |
| Suíte completa local | 53 | 268 | Passou, com quatro avisos do PHPUnit |

O filtro Livro também inclui testes cujo nome contém esse termo; os 19 testes não representam exclusivamente os cinco arquivos listados acima.

Comando utilizado para a execução dos testes relacionados a livros:

```bash
DB_HOST=localhost DB_USER=pnld DB_PASSWORD=123456 DB_NAME=SistemaHBL ./vendor/bin/phpunit --filter 'Livro'
```

Os arquivos add_livro.php, editar_livro.php, excluir_livro.php e livros.php também foram verificados com php -l, sem erros de sintaxe.

### Cobertura registrada

Uma execução do GitHub Actions com Xdebug apresentou:

| Componente | Cobertura de linhas |
| --- | ---: |
| LivroRepository | 97,18% — 69 de 71 linhas |
| LivroValidator | 91,67% — 33 de 36 linhas |
| Geral dos arquivos considerados | 67,45% — 230 de 341 linhas |

Esses valores foram obtidos em uma execução anterior que ainda apresentava falhas nos testes de administrador e empréstimo. Não correspondem necessariamente à cobertura final do commit 6d7583b.

Posteriormente, o workflow do PR #16 concluiu com sucesso no commit 6d7583b.

## Integração contínua

O workflow Testes e SonarQube configura PHP, MySQL e Xdebug, instala as dependências, prepara o banco, executa os testes e gera coverage.xml no formato Clover.

O relatório de cobertura é publicado como artefato e informado ao SonarQube.

Foram corrigidos problemas na preparação dos dados dos testes de integração que impediam a conclusão da suíte. Também foi atualizada a ação de análise do SonarQube após uma falha relacionada a uma dependência obsoleta de cache.

## Análise estática — SonarQube

- Servidor: http://labens.dct.ufrn.br/sonarqube
- Projeto: Projeto PNLD
- Chave: pnldkey
- Dashboard: http://labens.dct.ufrn.br/sonarqube/dashboard?id=pnldkey
- Commit analisado: 6d7583b3f1854ca7349e5a7e36d6d7297f1188d7

O log do GitHub Actions confirmou a geração e o envio da análise:

```text
SCM revision ID '6d7583b3f1854ca7349e5a7e36d6d7297f1188d7'
Analysis report uploaded
ANALYSIS SUCCESSFUL
SonarScanner Engine completed successfully
EXECUTION SUCCESS
```

O envio da análise da US05 está comprovado pelo log. A aprovação do Quality Gate dessa análise histórica não foi comprovada.

O dashboard compartilhado recebeu análises posteriores de outros integrantes. O estado atual do projeto não foi atribuído à análise da US05.

A aprovação do Quality Gate e a conferência dos apontamentos específicos dessa revisão permanecem pendentes. A conclusão do scanner não significa aprovação do Quality Gate.

### Evidências

- Execução do workflow: aba Checks do PR https://github.com/HelenaMariano2025/projetoPNLD/pull/16
- Log do envio: [Log do SonarQube da US05](evidencias/sonar-us05-log.md)
- Print do workflow: [Execução concluída no PR #16](evidencias/actions-us05.png)
- Histórico consultado: [Atividade do projeto no SonarQube](evidencias/sonar-historico.png)

O print do histórico não comprova o Quality Gate da revisão analisada.

## Atuação como QA — US04

- Desenvolvedora: Jaine Souza
- User Story: US04 — Gerenciar turmas
- Pull Request testado: https://github.com/HelenaMariano2025/projetoPNLD/pull/19
- Branch local: qa/us04-pr19
- Commit testado: 05cd7efbbf008e854f7d449c8d1a3387cda99319
- Data: 09/10/2026
- Ambiente: Ubuntu, Firefox, servidor local PHP e MySQL.
- Endereço base: http://localhost:8000

### Casos executados

| Caso | Cenário | Resultado |
| --- | --- | --- |
| TA04.01 | Cadastrar turma | Passou |
| TA04.02 | Consultar turma | Passou |
| TA04.03 | Alterar turma | Passou |
| TA04.04 | Excluir turma sem alunos vinculados | Passou, conforme confirmação da testadora |
| TA04.05 | Pesquisar turmas pelo curso | Passou, conforme confirmação da testadora |
| TA04.06 | Pesquisar curso sem turmas | Passou |
| TA04.07 | Impedir cadastro com código duplicado | Bloqueio passou; falhou na correspondência literal da mensagem |
| TA04.08 | Impedir operação com alunos vinculados | Bloqueio passou; falhou na correspondência literal da mensagem |

Foram executados oito cenários. Seis passaram sem divergências identificadas e dois apresentaram diferenças no texto das mensagens previstas no Gherkin.

Não foram reproduzidas falhas nas regras funcionais dos fluxos executados. Foram anexados dez prints ao relatório.

O resultado final da busca por curso e a ausência da turma após exclusão foram confirmados pela testadora, sem prints específicos dessas verificações finais. Não foram realizadas consultas diretas ao banco.

O cenário TA04.08 menciona inativação, enquanto a interface apresenta o botão Excluir. Foi testada a operação disponível por esse botão; não foi avaliado um fluxo separado de inativação.

### Melhorias sugeridas

- Alinhar as mensagens da interface com a especificação.
- Esclarecer a diferença entre exclusão e inativação no TA04.08.
- Manter o termo pesquisado no campo após a busca.
- Ocultar ou desabilitar as setas quando não houver resultados ou existir apenas um.
- Documentar os campos adicionais Sigla e Situação.
- Preservar os campos preenchidos após a rejeição de um cadastro duplicado.

### Relatório e evidências

- Relatório: https://github.com/HelenaMariano2025/projetoPNLD/blob/docs/qa-us04-500/docs/qa/relatorio-aceitacao-jaineII.md
- Pull Request: https://github.com/HelenaMariano2025/projetoPNLD/pull/20
- Evidências: https://github.com/HelenaMariano2025/projetoPNLD/tree/docs/qa-us04-500/docs/qa/evidencias

## Revisão de código — US06

Também foi realizada a revisão estática das alterações fornecidas da US06 — Registrar empréstimos:

https://github.com/HelenaMariano2025/projetoPNLD/pull/17

Foram sugeridos ajustes na limpeza dos dados de testes, verificação do bloqueio de empréstimos de livros inativos e inclusão de testes unitários com mocks.

Essa revisão é uma atividade separada dos testes de aceitação da US04.

## Situação da entrega

- Implementação e testes da US05: entregues no PR #16.
- Relatório de QA da US04 e evidências: entregues no PR #20.
- Envio da análise da US05 ao SonarQube: confirmado.
- Aprovação do Quality Gate da análise da US05: não comprovada.
- Conferência e resolução dos apontamentos específicos dessa análise: pendentes.