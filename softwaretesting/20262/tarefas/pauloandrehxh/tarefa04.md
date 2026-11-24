# Tarefa 04 - DevOps, Integração e Entrega Contínua (CI/CD) com Testes Automatizados

**Discente:** Paulo André Alves de Moura  
**GitHub:** @pauloandrehxh  
**E-mail:** paulo.moura.701@ufrn.edu.br  
**Projeto:** [Arena UFRN](https://github.com/pauloandrehxh/arena-ufrn)  
**Issue da disciplina:** [#619](https://github.com/tacianosilva/bsi-tasks/issues/619)  
**Branch da entrega:** `task/619-ci-cd`

## Links de entrega

| Item | Link / situação |
|---|---|
| PR com o workflow de CI/CD no projeto | [arena-ufrn #24](https://github.com/pauloandrehxh/arena-ufrn/pull/24) |
| Correção final do serving do React | [arena-ufrn #28](https://github.com/pauloandrehxh/arena-ufrn/pull/28) |
| Aplicação publicada em execução | [https://arena-ufrn-dbsz.onrender.com](https://arena-ufrn-dbsz.onrender.com) — `GET /health` verificado |
| PR da entrega no `bsi-tasks` | [#620](https://github.com/tacianosilva/bsi-tasks/pull/620) |
| Evidências de CI, Quality Gate e smoke | [docs/evidencias/t4-cicd.md](https://github.com/pauloandrehxh/arena-ufrn/blob/main/docs/evidencias/t4-cicd.md) |

O workflow técnico foi implementado em `ci/t4-cicd-render` e integrado à `main` pelo PR [arena-ufrn #24](https://github.com/pauloandrehxh/arena-ufrn/pull/24). Durante a verificação do deploy, foi identificada uma falha real no serving do React na raiz: a rota `GET /` da API era registrada antes do middleware estático. A correção foi publicada pelo PR [arena-ufrn #26](https://github.com/pauloandrehxh/arena-ufrn/pull/26) e, como o serviço criado manualmente na Render não recebeu `SERVE_STATIC`, foi consolidada no PR [arena-ufrn #28](https://github.com/pauloandrehxh/arena-ufrn/pull/28): o servidor passou a detectar o `index.html` automaticamente. Ao todo, 6 testes de integração cobrem o comportamento.

---

## 1. Fundamentação teórica

### 1.1 Cultura DevOps e testes contínuos

A cultura DevOps combina práticas, valores e ferramentas para reduzir o tempo entre uma mudança ser escrita e ela chegar ao uso, sem sacrificar estabilidade. A AWS define DevOps como a combinação de filosofias culturais, práticas e ferramentas que aumenta a capacidade de entregar aplicações em alta velocidade ([AWS, *What is DevOps?*](https://aws.amazon.com/devops/what-is-devops/)). O problema clássico é o "muro da confusão": desenvolvimento é cobrado por entregar mudanças rápidas, enquanto operações é cobrada por não quebrar o ambiente. DevOps dissolve esse muro com responsabilidade compartilhada, automação de build/test/deploy, infraestrutura como código e feedback rápido. O DORA reforça que entrega contínua é a capacidade de liberar mudanças de forma rápida, segura e sustentável, inclusive em horário comercial ([DORA, *Continuous delivery*](https://dora.dev/devops-capabilities/technical/continuous-delivery/)).

No modelo cascata, o teste é uma fase tardia, executada depois da implementação; uma falha descoberta nessa etapa exige retrabalho caro e próximo da entrega. No paradigma DevOps, o teste deixa de ser uma fase e passa a ser uma propriedade do fluxo: *Continuous Testing* executa verificações automatizadas a cada mudança, em vários níveis, e fornece sinal rápido antes do merge. O papel do testador/QA também muda: deixar de ser apenas um executor manual de casos no fim do ciclo e passar a desenhar cenários, escrever testes automatizados, definir critérios de qualidade, interpretar métricas e atuar como guardião do *Quality Gate* da esteira. Isso não elimina a exploração manual; ela se desloca para riscos que a automação não cobre bem, como usabilidade e cenários ambíguos.

**Shift-Left Testing** significa antecipar o teste para as fases iniciais: executar checagens estáticas e testes unitários no commit e no Pull Request, antes do merge. O objetivo é *fail-fast*: quanto antes o defeito é encontrado, menor o custo de correção e mais curto o feedback ao desenvolvedor. **Shift-Right Testing** complementa: observar e testar o sistema já em produção, com smoke tests, monitoramento, logs, métricas, testes de carga e experimentos controlados. Não é "testar menos antes"; é reconhecer que alguns comportamentos só existem com tráfego real, configuração real e dependências reais. Na entrega atual, o shift-left aparece nos jobs de lint, checagem estática, testes e cobertura do PR; o shift-right aparece no `GET /health` verificado pelo smoke test depois do deploy.

### 1.2 CI, Continuous Delivery e Continuous Deployment

- **Integração Contínua (CI):** cada mudança integrada à branch principal é construída e validada automaticamente. Fowler descreve a CI como uma prática em que os desenvolvedores integram trabalho frequentemente, com cada integração verificada por build e testes automatizados ([Fowler, *Continuous Integration*](https://martinfowler.com/articles/continuousIntegration.html)).
- **Continuous Delivery:** extensão da CI; o artefato aprovado está sempre pronto para publicação, mas esta exige decisão humana.
- **Continuous Deployment:** a publicação também é automatizada: se o pipeline passou, a mudança vai para produção sem intervenção humana.

A distinção prática está no gatilho final. Neste projeto, o job `deploy` só roda em `push` na `main` **depois** que o job de testes passou. Como a decisão de publicar está acoplada ao merge na branch principal e ao CI verde, a configuração se enquadra em *Continuous Delivery* com publicação automatizada condicionada; o deploy não ocorre em PR nem em branches de feature ([Atlassian, *CI vs. Delivery vs. Deployment*](https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deployment)).

### 1.3 Papel dos testes na esteira e Quality Gate

*Quality Gate* é o ponto do pipeline onde critérios objetivos decidem se o código avança. A suíte automatizada é o mecanismo do portão: se um teste unitário, de integração ou uma checagem estática falha, o job termina com erro e os jobs seguintes são ignorados. Uma esteira sem testes apenas transporta código; ela não oferece evidência de que a mudança preservou o comportamento, logo não é uma esteira de entrega segura.

A pirâmide de testes orienta a distribuição: muitos testes unitários rápidos na base, menos testes de integração no meio e poucos testes de sistema no topo ([Fowler, *The Practical Test Pyramid*](https://martinfowler.com/articles/practical-test-pyramid.html)). Temporalmente no pipeline: (1) lint, checagem estática e testes unitários, para *fail-fast*; (2) testes de integração com dependências controladas; (3) cobertura e análise estática antes do deploy; (4) smoke test no ambiente publicado. Nesta entrega, o job de CI executou 291 testes unitários e 313 de integração; o deploy e o smoke só são elegíveis depois desse job.

### 1.4 Estratégias de publicação e Secrets management

- **Recreate:** a versão antiga é encerrada antes de iniciar a nova. Simples, mas com janela de indisponibilidade.
- **Rolling Update:** instâncias substituídas gradualmente; reduz a indisponibilidade, mas versões diferentes convivem temporariamente.
- **Blue/Green:** duas versões completas convivem e o tráfego é direcionado da "blue" para a "green" após validação; permite rollback rápido, mas exige mais capacidade.

A Render realiza deploys com substituição de instâncias e health check da nova versão; a estratégia efetiva da conta gratuita é gerida pela plataforma, e o projeto não implementou Blue/Green próprio. Isso é limitação conhecida, não resultado inventado.

*Secrets management* é obrigatório porque URLs de deploy hook e tokens nunca devem aparecer no código versionado, em logs ou em variáveis de PR. O GitHub Actions permite registrar secrets em nível de repositório, ambiente ou organização; eles são criptografados e injetados apenas como variáveis de ambiente para steps autorizados ([GitHub Docs, *Using secrets in GitHub Actions*](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)). Aqui, o hook da Render é lido de `secrets.RENDER_DEPLOY_HOOK_URL || secrets.RENDER_DEPLOY_HOOK_URN` — o segundo nome existe porque o secret foi cadastrado com a grafia `URN`; a URL pública é variável não sensível (`vars.APP_URL`). O workflow não imprime nenhum dos dois valores e falha com `curl --fail` se o secret estiver ausente.

---

## 2. Implementação da CI e da CD no Arena UFRN

### 2.1 CI — `.github/workflows/backend-ci.yaml`

O workflow existente foi ampliado, mantendo o nome do arquivo para preservar o histórico. Gatilhos: `push` e `pull_request` para `main`. O job `test-and-sonar` executa: checkout com `fetch-depth: 0`; pnpm 12.3.4 e Node 22.12.0 com cache dos lockfiles; `pnpm install --frozen-lockfile` nos dois pacotes; checagem estática do backend e lint do frontend (com `globals.node` para `frontend/e2e/`); `pnpm prisma generate --config prisma7.config.ts`; testes unitários e de integração separados; `pnpm test:coverage`, upload do artifact `cobertura-backend` e SonarQube. Qualquer falha encerra o job com erro e bloqueia os seguintes.

### 2.2 CD — deploy e smoke test

- `deploy` depende de `test-and-sonar` e tem condição `github.event_name == 'push' && github.ref == 'refs/heads/main'`.
- O step usa `curl --fail` com `ref=${{ github.sha }}` no deploy hook da Render, garantindo que o commit publicado seja exatamente o testado. A Render documenta esse parâmetro e recomenda o secret `RENDER_DEPLOY_HOOK_URL` ([Render, *Deploy Hooks*](https://docs.render.com/deploy-hooks)). No repositório o secret foi registrado como `RENDER_DEPLOY_HOOK_URN`; o workflow aceita os dois nomes para não exigir a reinserção do valor sensível.
- `smoke` depende de `deploy` e faz `GET $APP_URL/health` com retries para absorver a inicialização do plano gratuito. O endpoint em `backend/src/app.js` retorna HTTP 200 com `status: "ok"`, `service` e `timestamp`.
- `render.yaml` descreve Web Service Docker, plano `free`, região `oregon`, `autoDeployTrigger: 'off'`, `healthCheckPath: /health` e variáveis de ambiente. O auto deploy foi desligado para que o único caminho de publicação seja o CI verde ([Render, *Blueprint YAML Reference*](https://docs.render.com/blueprint-spec)).

### 2.3 Container

O `Dockerfile` é multi-stage: `frontend-build` instala dependências e roda `pnpm build`; `backend-deps` compila `better-sqlite3` e gera o Prisma Client; `runner` copia `node_modules`, código do backend e o `dist` para `/app/public`, executa migrações e inicia em `PORT=10000`. O módulo `backend/src/static-app.js` monta um app externo que serve os estáticos e o fallback SPA antes de repassar `/api` e `/health` ao app da API. A função `temBuildDoFrontend` detecta a presença de `index.html` em `PUBLIC_DIR`, então o serving funciona mesmo sem `SERVE_STATIC`. Sem isso, a rota `GET /` da API interceptava a raiz e o navegador recebia JSON em vez do React; o comportamento é protegido por 6 testes de integração. O frontend passou a buscar `/api/quadras` de forma relativa; no desenvolvimento, o Vite faz proxy para `http://localhost:3000`. Backend e frontend saem no mesmo container e domínio, sem CORS entre origens diferentes. O `.dockerignore` exclui `.git`, `.github`, `docs`, `node_modules`, `coverage`, `dist`, `.env`, `.db` e logs.

---

## 3. Quality Gate — simulação prática

Branch `demo/falha-ci`, PR [arena-ufrn #25](https://github.com/pauloandrehxh/arena-ufrn/pull/25), encerrado sem merge.

| Momento | Commit | Run | Resultado |
|---|---|---|---|
| Teste propositalmente quebrado | `fcba0a8` | [45290753212](https://github.com/pauloandrehxh/arena-ufrn/actions/runs/45290753212) | CI falhou em 24s; 1 falha em 292 testes; `Expected: "valor esperado"`, `Received: "teste quebrado"` |
| Teste corrigido | `00eb36c` | [45290900985](https://github.com/pauloandrehxh/arena-ufrn/actions/runs/45290900985) | CI passou em 1m06s |

Nas duas execuções, `Deploy na Render` e `Smoke test pós-deploy` ficaram `skipped`: o evento era `pull_request`, não `push` em `main`, e o job de CI com falha terminou antes de qualquer publicação. Isso comprova que o portão de qualidade barra o deploy.

---

## 4. Resultados e evidências

Execução local em 23/11/2026, Node v22.12.0: 32 suítes e 610 testes aprovados após a correção final do serving estático (31 suítes e 604 testes antes dela); cobertura global de 83,65% statements, 77,56% branches, 92,94% functions e 83,57% lines. `pnpm lint` e `pnpm build` do frontend aprovados.

CI do PR técnico [#24](https://github.com/pauloandrehxh/arena-ufrn/pull/24): run [45290402011](https://github.com/pauloandrehxh/arena-ufrn/actions/runs/45290402011), job aprovado em 1m43s; 291 testes unitários e 313 de integração; a mesma cobertura global; artifact `cobertura-backend` gerado; deploy e smoke `skipped` por ser um PR.

**Deploy e smoke em produção: executados.** Após o merge do PR #24 na `main`, o run [45300024428](https://github.com/pauloandrehxh/arena-ufrn/actions/runs/45300024428) executou `deploy` (4s) e `smoke` (3s), ambos aprovados. Resposta manual de `GET /health`: `{"status":"ok","service":"arena-ufrn","timestamp":"2026-11-24T00:49:27.673Z"}`.

Após a correção final (PR #28), o run [45307236158](https://github.com/pauloandrehxh/arena-ufrn/actions/runs/45307236158) repetiu CI, deploy e smoke com sucesso, com 610 testes em 32 suítes. A verificação manual em produção confirmou: `GET /` entrega HTML com `<div id="root">`, `GET /health` retorna `{"status":"ok","service":"arena-ufrn","timestamp":"2026-11-24T01:46:46.612Z"}`, `GET /api/quadras` responde `[]` e o bundle JS retorna 200. Log completo: [docs/evidencias/t4-cicd.md](https://github.com/pauloandrehxh/arena-ufrn/blob/main/docs/evidencias/t4-cicd.md).

### Limitações conhecidas

- Docker CLI não está disponível localmente; a imagem foi construída pela Render, mas não foi possível validar o `Dockerfile` localmente.
- O banco é SQLite em `/data` no container, sem disco persistente; dados podem ser perdidos em redeploy.
- O plano gratuito da Render suspende serviços inativos; o smoke test usa retries, mas a primeira requisição de um usuário pode ser lenta.

---

## 5. Referências

- AWS. [*What is DevOps?*](https://aws.amazon.com/devops/what-is-devops/)
- DORA. [*Continuous delivery*](https://dora.dev/devops-capabilities/technical/continuous-delivery/)
- Fowler, Martin. [*Continuous Integration*](https://martinfowler.com/articles/continuousIntegration.html)
- Fowler, Martin. [*The Practical Test Pyramid*](https://martinfowler.com/articles/practical-test-pyramid.html)
- Atlassian. [*Continuous integration vs. delivery vs. deployment*](https://www.atlassian.com/continuous-delivery/principles/continuous-integration-vs-delivery-vs-deployment)
- GitHub Docs. [*Using secrets in GitHub Actions*](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)
- Render. [*Deploy Hooks*](https://docs.render.com/deploy-hooks)
- Render. [*Blueprint YAML Reference*](https://docs.render.com/blueprint-spec)

