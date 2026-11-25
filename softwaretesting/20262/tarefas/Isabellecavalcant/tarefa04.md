# Tarefa 04 — DevOps, Integração e Entrega Contínua (CI/CD) com Testes Automatizados

## Identificação

- **Nome:** Isabelle Cavalcanti da Silva
- **GitHub:** [Isabellecavalcant](https://github.com/Isabellecavalcant)
- **E-mail:** isabelle.silva.712@ufrn.edu.br

## Links de entrega

- **Repositório da aplicação:** [projetoPNLD](https://github.com/HelenaMariano2025/projetoPNLD)
- **Pull Request com CI e Docker:** [PR #57](https://github.com/HelenaMariano2025/projetoPNLD/pull/57)
- **Workflow de CI:** [ci.yml](https://github.com/HelenaMariano2025/projetoPNLD/blob/main/.github/workflows/ci.yml)
- **Execução aprovada da CI:** [execução 45530297695](https://github.com/HelenaMariano2025/projetoPNLD/actions/runs/45530297695)
- **Quality Gate — execução com falha:** [execução 45531376568](https://github.com/HelenaMariano2025/projetoPNLD/actions/runs/45531376568)
- **Quality Gate — execução após correção:** [execução 45531820820](https://github.com/HelenaMariano2025/projetoPNLD/actions/runs/45531820820)
- **PR temporário da demonstração (fechado sem merge):** [PR #58](https://github.com/HelenaMariano2025/projetoPNLD/pull/58)
- **Aplicação publicada:** não realizada até a elaboração deste relatório. A implantação em nuvem e o smoke test remoto permanecem pendentes.
- **Pull Request desta entrega no repositório da disciplina:** será adicionado após sua abertura.

## 1. Cultura DevOps e testes contínuos

DevOps é uma cultura e um conjunto de práticas que aproximam desenvolvimento (Dev) e operações (Ops), promovendo colaboração, automação, integração frequente e responsabilidade compartilhada pelo ciclo de vida do software. Seu objetivo é reduzir o chamado “muro da confusão”: enquanto desenvolvimento tende a priorizar velocidade e novas funcionalidades, operações precisa preservar estabilidade, disponibilidade e segurança. Com processos compartilhados e feedback frequente, qualidade e confiabilidade deixam de ser responsabilidade isolada de uma equipe.

No modelo cascata tradicional, desenvolvimento, testes e implantação costumam ocorrer em fases separadas. Os testes podem ficar concentrados ao final do desenvolvimento, fazendo com que defeitos sejam descobertos tardiamente e tenham custo maior de correção. No paradigma DevOps, os testes são contínuos e automatizados, executados desde as primeiras alterações e repetidos ao longo do pipeline. O profissional de QA deixa de atuar somente como responsável por testar um produto pronto e passa a colaborar desde o planejamento, ajudando a definir critérios de qualidade, automatizar verificações, analisar riscos e acompanhar o comportamento do sistema.

**Shift-Left Testing** significa antecipar as atividades de qualidade para etapas iniciais: revisão de código, análise estática, testes unitários e verificações executadas a cada push ou Pull Request. Isso permite encontrar problemas antes que sejam integrados ou publicados. **Shift-Right Testing** amplia a verificação para depois da implantação, observando o sistema em seu ambiente real por meio de smoke tests, monitoramento, logs, métricas, alertas e testes controlados. As abordagens são complementares: uma reduz a chegada de defeitos à produção e a outra verifica o comportamento real do serviço.

## 2. Integração Contínua, Entrega Contínua e Implantação Contínua

**Integração Contínua (CI)** é a prática de integrar alterações frequentemente em um repositório compartilhado e executar automaticamente verificações, compilação e testes. O objetivo é identificar rapidamente incompatibilidades e regressões.

**Entrega Contínua (Continuous Delivery)** mantém o software validado e pronto para publicação. O pipeline automatiza construção, testes e preparação do artefato, mas a decisão de publicar em produção pode depender de aprovação manual.

**Implantação Contínua (Continuous Deployment)** vai além: toda alteração que passa pelos critérios automatizados é implantada automaticamente no ambiente de produção, sem uma aprovação manual entre a validação e o deploy. Portanto, CI trata da integração e validação; Continuous Delivery garante que a versão esteja pronta para entrega; Continuous Deployment automatiza também a publicação efetiva.

## 3. Testes de software e Quality Gate no pipeline

Um **Quality Gate** é um conjunto de critérios obrigatórios que uma alteração precisa satisfazer para avançar no processo de integração ou implantação. Pode incluir sintaxe válida, análise estática, testes aprovados, cobertura mínima e análise de qualidade. Se uma etapa obrigatória falha, o pipeline deve retornar resultado negativo e impedir o avanço. Uma esteira que apenas constrói e publica o sistema, sem testes, automatiza a entrega, mas não oferece evidência suficiente de que a alteração preserva o comportamento esperado.

A pirâmide de testes orienta a distribuição: testes unitários, rápidos e numerosos, ficam na base e devem executar primeiro; testes de integração verificam a comunicação entre componentes e dependências; testes de sistema e aceitação verificam fluxos completos e tendem a ser mais lentos, ficando em estágios posteriores. Essa ordem favorece o princípio **Fail-Fast**: falhas simples são detectadas cedo, com menor custo e feedback mais rápido para quem desenvolve.

## 4. Estratégias de deploy e gerenciamento de segredos

Na estratégia **Recreate**, as instâncias antigas são encerradas antes de as novas serem iniciadas; é simples, mas pode causar indisponibilidade. Em **Rolling Update**, as instâncias são substituídas gradualmente, reduzindo interrupções e permitindo atualização progressiva. Em **Blue/Green**, dois ambientes equivalentes são mantidos: a nova versão é preparada no ambiente inativo e o tráfego é redirecionado após validação, facilitando reversão.

O gerenciamento de segredos evita expor senhas, tokens e chaves em código-fonte, arquivos versionados ou logs. Em pipelines, credenciais devem ser armazenadas em mecanismos próprios, como GitHub Secrets, limitando permissões e evitando sua impressão durante a execução. Variáveis de ambiente devem fornecer configurações sensíveis ao processo sem incorporá-las à imagem ou ao repositório.

## 5. Implementação da Integração Contínua (CI)

Foi configurado o workflow `.github/workflows/ci.yml` no GitHub Actions, acionado em eventos de push e Pull Request direcionados à branch principal, conforme os filtros definidos no arquivo. O pipeline prepara um serviço MySQL para os testes, configura o PHP e instala as dependências do Composer com cache.

As etapas automatizadas incluem verificações de sintaxe PHP, análise estática com PHPStan, preparação do banco de testes, execução da suíte PHPUnit com geração de cobertura, publicação do relatório de cobertura como artefato e análise no SonarQube. A execução dos testes é bloqueante: se os testes falham, as etapas posteriores não são aprovadas e o workflow termina com falha. A execução [45530297695](https://github.com/HelenaMariano2025/projetoPNLD/actions/runs/45530297695) concluiu com sucesso todas as etapas, inclusive testes, cobertura e SonarQube.

## 6. Containerização e situação da Entrega/Implantação Contínua (CD)

A aplicação foi preparada com Docker por meio de um Dockerfile multi-stage, separando a etapa de construção/preparação da imagem final. Também foram definidos serviços no `compose.yaml` para a aplicação, banco MySQL e Selenium. O arquivo `.dockerignore` evita incluir arquivos desnecessários e arquivos sensíveis no contexto de construção.

Localmente, a aplicação foi iniciada em contêiner e o endpoint `/health` foi verificado com uma requisição HTTP. A resposta observada foi `HTTP 200`, com JSON indicando `status: healthy` e `database: connected`. Essa validação comprova o funcionamento local do endpoint, mas não equivale a um smoke test em uma aplicação publicada.

**Limitação da entrega:** até a elaboração deste relatório, não foi concluída a configuração de um provedor de hospedagem, das credenciais de banco de dados de produção e dos segredos necessários para disparar o deploy. Por isso, não há URL pública da aplicação e não foi possível implementar ou comprovar uma etapa de CD que dispare a implantação após merge na `main` e verifique o endpoint remoto. A containerização e a verificação local foram realizadas, mas a implantação em nuvem e o smoke test pós-deploy permanecem pendentes.

## 7. Simulação prática do Quality Gate

Para demonstrar o comportamento bloqueante, foi criada uma branch temporária e aberto o [PR #58](https://github.com/HelenaMariano2025/projetoPNLD/pull/58), contendo um teste PHPUnit propositalmente incorreto, que comparava os valores `1` e `2` como se fossem iguais. A execução [45531376568](https://github.com/HelenaMariano2025/projetoPNLD/actions/runs/45531376568) falhou na etapa de testes, demonstrando que o pipeline não aprovou a alteração.

Em seguida, a asserção foi corrigida para comparar valores iguais. A execução [45531820820](https://github.com/HelenaMariano2025/projetoPNLD/actions/runs/45531820820) concluiu com sucesso, incluindo sintaxe, PHPStan, preparação do banco, PHPUnit, cobertura e SonarQube. Após registrar as evidências, o PR demonstrativo #58 foi fechado sem merge para impedir que o teste temporário fosse incorporado à branch principal.

## 8. Considerações finais

A atividade permitiu configurar e validar uma esteira de CI com testes automatizados, análise estática, cobertura e análise de qualidade, além de preparar a aplicação em contêineres e validar localmente seu endpoint de integridade. A simulação prática evidenciou o papel do Quality Gate ao interromper uma execução com teste falho e aprovar a execução após a correção. A implantação em nuvem, a automação do deploy e o smoke test remoto não foram concluídos e são limitações ainda existentes nesta entrega.
