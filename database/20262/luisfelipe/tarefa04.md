# Tarefa 04 – DevOps, Integração e Entrega Contínua (CI/CD) com Testes Automatizados

## 1. Identificação

- **Nome:** Luis Felipe Linhares Pereira
- **GitHub:** [@Luisfelipelinhares](https://github.com/Luisfelipelinhares)
- **E-mail acadêmico:** luis.felipe.linhares701@ufrn.edu.br
- **Curso:** Bacharelado em Sistemas de Informação
- **Instituição:** Universidade Federal do Rio Grande do Norte (UFRN)
- **Projeto utilizado:** Arena UFRN

## 2. Links da atividade

- **Repositório individual:** https://github.com/Luisfelipelinhares/arena-ufrn
- **PR principal da implementação:** https://github.com/Luisfelipelinhares/arena-ufrn/pull/3
- **Aplicação publicada – API:** https://arena-ufrn-2.onrender.com
- **Endpoint de saúde:** https://arena-ufrn-2.onrender.com/health


O projeto Arena UFRN foi utilizado como base para implementar e demonstrar os conceitos de integração contínua, entrega contínua, testes automatizados e monitoramento da aplicação.

## 3. Fundamentação teórica

### 3.1. O que é DevOps?

DevOps é uma cultura e um conjunto de práticas que aproximam as equipes de desenvolvimento de software (Development) e operações (Operations). Seu objetivo é melhorar a colaboração, automatizar processos e permitir entregas de software mais frequentes, seguras e confiáveis.

Entre seus principais benefícios estão:

- Maior agilidade no desenvolvimento.
- Redução de erros durante a implantação.
- Automatização de tarefas repetitivas.
- Melhor comunicação entre desenvolvimento e operações.
- Maior confiabilidade das aplicações.

### 3.2. Testes contínuos (Continuous Testing)

Testes contínuos consistem na execução frequente e automatizada de testes durante o ciclo de desenvolvimento do software.

Essa prática permite identificar defeitos antes que cheguem ao ambiente de produção, reduzindo custos de correção e aumentando a qualidade do sistema.

No projeto Arena UFRN, foram utilizados testes automatizados com Jest e testes de integração com Supertest.

### 3.3. Shift-Left e Shift-Right

**Shift-Left** é a prática de antecipar atividades de qualidade, segurança e testes para as etapas iniciais do desenvolvimento. Assim, problemas são identificados antes de chegarem à produção.

**Shift-Right** consiste em observar e validar o comportamento do software depois da implantação, utilizando monitoramento, testes em produção e verificações de disponibilidade.

No Arena UFRN, o Shift-Left foi aplicado por meio dos testes automatizados e da análise estática do SonarCloud durante o processo de CI.

O Shift-Right foi aplicado por meio do Smoke Test, que verifica se a API publicada está respondendo corretamente.

### 3.4. Integração Contínua (CI) e Entrega Contínua (CD)

A Integração Contínua (CI) é uma prática em que alterações realizadas no código são integradas frequentemente ao repositório principal, passando por verificações automatizadas.

A Entrega Contínua (CD) amplia esse processo, preparando o software para publicação e automatizando as etapas necessárias para disponibilizá-lo em um ambiente de execução.

No projeto, o GitHub Actions foi utilizado para executar o pipeline de integração contínua. A publicação da API foi realizada no Render, que está configurado para realizar a implantação após alterações na branch principal.

### 3.5. Quality Gate, pirâmide de testes e Fail Fast

O Quality Gate é um conjunto de critérios utilizados para determinar se o software atende aos requisitos mínimos de qualidade.

A pirâmide de testes organiza os testes em diferentes níveis:

- **Testes unitários:** verificam pequenas unidades do sistema isoladamente.
- **Testes de integração:** verificam a comunicação entre diferentes partes do sistema.
- **Testes de ponta a ponta:** verificam fluxos completos de utilização.

A estratégia Fail Fast busca identificar e interromper rapidamente processos que apresentam falhas, evitando que alterações problemáticas avancem para as próximas etapas.

No Arena UFRN, o pipeline utiliza os resultados dos testes automatizados e da análise do SonarCloud como critérios de validação. A proteção da branch principal exige que a verificação de CI seja aprovada antes do merge.

### 3.6. Estratégias de implantação

Existem diferentes estratégias de implantação de software:

- **Recreate:** substitui a versão anterior pela nova versão.
- **Rolling Update:** atualiza gradualmente as instâncias da aplicação.
- **Blue-Green Deployment:** mantém dois ambientes, permitindo alternar entre a versão atual e a nova.
- **Canary Release:** disponibiliza a nova versão inicialmente para uma pequena parcela dos usuários.

No projeto Arena UFRN, foi utilizada a implantação automática do serviço no Render após alterações na branch principal. Não foi implementada uma estratégia Blue-Green ou Canary.

### 3.7. Gerenciamento de segredos

Segredos são informações sensíveis utilizadas pelas aplicações, como tokens, senhas e chaves de acesso.

Essas informações não devem ser inseridas diretamente no código-fonte ou compartilhadas publicamente.

O GitHub Actions disponibiliza o recurso GitHub Secrets, que permite armazenar variáveis sensíveis e utilizá-las durante a execução dos workflows.

No projeto, foram utilizados segredos para configurar a integração com o SonarCloud e o endereço da aplicação publicada.

## 4. Tecnologias utilizadas

| Tecnologia | Finalidade |
|---|---|
| Git e GitHub | Versionamento e colaboração |
| GitHub Actions | Automação do pipeline CI |
| Node.js | Ambiente de execução do backend |
| Express | Desenvolvimento da API |
| Jest | Testes automatizados |
| Supertest | Testes de integração HTTP |
| SonarCloud | Análise estática e Quality Gate |
| Render | Hospedagem e implantação da API |
| SQLite | Banco de dados da aplicação |

## 5. Implementação da Integração Contínua (CI)

Foi criado o workflow `.github/workflows/backend-ci.yaml`, utilizando GitHub Actions.

O workflow é executado nos seguintes eventos:

- Push na branch `main`.
- Abertura ou atualização de Pull Requests direcionados à branch `main`.
- Execução manual por meio de `workflow_dispatch`.

### 5.1. Etapas do pipeline

O processo automatizado realiza as seguintes etapas:

1. Obtém o código do repositório.
2. Configura o ambiente Node.js.
3. Configura o gerenciador de pacotes pnpm.
4. Instala as dependências do backend.
5. Gera o Prisma Client.
6. Executa os testes unitários.
7. Executa os testes de integração.
8. Executa os testes com cobertura.
9. Realiza a análise de código pelo SonarCloud.
10. Verifica a disponibilidade da API publicada quando a execução ocorre na branch principal.

A análise estática é realizada pelo SonarCloud. Não foi configurado um comando independente de lint no projeto.

### 5.2. Quality Gate e proteção da branch

O SonarCloud foi integrado ao pipeline para analisar a qualidade do código e verificar o resultado do Quality Gate.

Também foi configurada a proteção da branch `main`, exigindo que o Pull Request passe pela verificação obrigatória de CI antes de ser integrado.

Essa configuração reduz o risco de alterações com testes reprovados chegarem à branch principal.

## 6. Entrega Contínua e publicação da aplicação (CD)

### 6.1. Plataforma de publicação

A API do Arena UFRN foi publicada na plataforma Render.

O serviço foi configurado para utilizar o diretório `backend` como diretório principal e executar os comandos de instalação, geração do Prisma Client e migração do banco de dados.

O comando de inicialização utilizado foi:

```bash
pnpm start
```

A implantação está configurada para ocorrer automaticamente após alterações na branch `main`.

A publicação utilizada foi realizada como serviço Node.js no Render, sem a criação de uma imagem Docker para essa implantação.

### 6.2. Configurações e segredos

Foram utilizadas variáveis de ambiente para configurar a aplicação e suas integrações.

Entre as configurações utilizadas estão:

- `DATABASE_URL`: endereço de conexão com o banco de dados.
- `CORS_ORIGIN`: configuração das origens permitidas.
- `RENDER_URL`: endereço da API publicada, utilizado no Smoke Test.
- `SONAR_TOKEN`: token de autenticação do SonarCloud.
- `SONAR_HOST_URL`: endereço do serviço SonarCloud.

Os valores sensíveis utilizados pelo GitHub Actions foram armazenados em GitHub Secrets, evitando sua exposição direta nos arquivos do repositório.

### 6.3. Limitação de persistência

A implantação utiliza SQLite no ambiente do Render.

Como o armazenamento local de um serviço gratuito pode ser efêmero, os dados podem ser perdidos após reinicializações ou novas implantações. Para um ambiente de produção que exija persistência confiável, seria necessário utilizar armazenamento persistente ou um banco de dados gerenciado.

## 7. Health Check e Smoke Test

Foi implementado o endpoint:

```http
GET /health
```

Esse endpoint permite verificar se a API está funcionando.

Quando acessado corretamente, retorna HTTP 200 e uma resposta JSON semelhante a:

```json
{
  "status": "ok",
  "message": "Arena UFRN API funcionando!"
}
```

Também foi implementado um Smoke Test no GitHub Actions para verificar a disponibilidade da API publicada.

O teste realiza requisições ao endpoint `/health`, aguardando entre as tentativas caso a aplicação ainda não esteja disponível.

A verificação é executada após o pipeline principal na branch `main`. Em execuções de Pull Requests, essa etapa é ignorada, pois a aplicação ainda não foi implantada por aquela alteração.

O endpoint foi validado com resposta HTTP 200 no ambiente publicado.

**Endereço utilizado para validação:**

https://arena-ufrn-2.onrender.com/health

## 8. Demonstração de falha no CI

Para demonstrar que o pipeline consegue identificar falhas e impedir a integração de código com testes reprovados, foi criada uma branch temporária chamada `teste/falha-ci`.

Nessa branch, foi adicionado um teste propositalmente incorreto:

```javascript
describe('Demonstração de falha no CI', () => {
    test('deve falhar propositalmente', () => {
        expect(true).toBe(false);
    });
});
```

O teste foi criado com o objetivo de provocar uma falha controlada no Jest.

### 8.1. Resultado da execução

Na execução local, o Jest identificou a falha proposital e retornou código de saída diferente de zero.

No GitHub Actions, o Pull Request também apresentou falha na etapa de testes automatizados.

O Pull Request utilizado para a demonstração foi:

https://github.com/Luisfelipelinhares/arena-ufrn/pull/9

O PR foi fechado sem merge.

### 8.2. Correção da falha

Após a demonstração, o arquivo de teste temporário foi removido e as alterações foram enviadas novamente para a branch.

Com a remoção do teste propositalmente incorreto, o pipeline voltou a executar com sucesso.

O SonarCloud também concluiu a análise e apresentou resultado aprovado no Quality Gate.

Essa demonstração comprovou que uma falha nos testes automatizados impede a aprovação da verificação obrigatória do CI.

## 9. Evidências

As evidências da implementação serão organizadas na pasta:

`tarefa04-617#/evidencias/`

As imagens devem demonstrar os seguintes resultados:

1. Workflow do GitHub Actions executando com sucesso.
2. Testes automatizados aprovados.
3. Análise do SonarCloud e resultado do Quality Gate.
4. API publicada no Render.
5. Endpoint `/health` retornando HTTP 200.
6. Demonstração da falha proposital no CI.
7. Pull Request de demonstração com a verificação reprovada.
8. Execução posterior com os testes corrigidos e pipeline aprovado.

Os nomes dos arquivos de imagem serão adicionados após a organização das evidências.

## 10. Conclusão

A realização desta atividade permitiu aplicar conceitos de DevOps, integração contínua, entrega contínua e testes automatizados em um projeto real de desenvolvimento.

A implementação do GitHub Actions automatizou as verificações do backend, incluindo a execução dos testes unitários e de integração, a geração de cobertura e a análise de código pelo SonarCloud.

A publicação da API no Render permitiu demonstrar a disponibilização do serviço em um ambiente externo. Além disso, o endpoint `/health` e o Smoke Test possibilitaram verificar a disponibilidade da aplicação após a implantação.

A demonstração de falha proposital comprovou a importância dos testes automatizados e da proteção da branch principal, mostrando como o pipeline pode impedir que alterações com problemas avancem no processo de integração.

Dessa forma, a atividade demonstrou como a automação pode contribuir para melhorar a qualidade, a confiabilidade e a organização do processo de desenvolvimento e entrega de software.

## 11. Referências

- GITHUB. **GitHub Actions Documentation**. Disponível em: https://docs.github.com/en/actions
- GITHUB. **About protected branches**. Disponível em: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- SONAR. **SonarQube Cloud Documentation**. Disponível em: https://docs.sonarcloud.io/
- RENDER. **Render Documentation**. Disponível em: https://render.com/docs
- JEST. **Jest Documentation**. Disponível em: https://jestjs.io/docs/getting-started
- NODE.JS. **Node.js Documentation**. Disponível em: https://nodejs.org/docs/latest/api/
- MICROSOFT. **DevOps**. Disponível em: https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-devops

**Data de acesso às referências:** 23 de novembro de 2026.