# opencode

[opencode](https://opencode.ai) é um assistente de codificação interativo
que roda diretamente no terminal. Ele ajuda a navegar pelo código, escrever
testes, refatorar, entender materiais didáticos e muito mais.

## Instalação

```bash
npm install -g @opencode-ai/opencode
```

Ou baixe o binário em [opencode.ai/download](https://opencode.ai/download).

## Usando neste repositório

Ao iniciar o opencode na raiz do repositório, as Skills específicas das
disciplinas ficam disponíveis automaticamente.

Invoque uma Skill mencionando seu nome ou descrição durante a conversa
(ex.: "use a skill django-backend para me ajudar com este CRUD").

## Skills disponíveis

| Skill | Stack | Disciplinas | Localização |
|---|---|---|---|
| [django-backend](/.opencode/skills/django-backend/SKILL.md) | Python / Django / DRF | ES, Testes, PW | `.opencode/skills/django-backend/` |
| [spring-boot-backend](/.opencode/skills/spring-boot-backend/SKILL.md) | Java / Spring Boot / JPA / WebFlux | BD, ES | `.opencode/skills/spring-boot-backend/` |
| [vue-frontend](/.opencode/skills/vue-frontend/SKILL.md) | Vue 3 / Vite / Vitest | PW | `.opencode/skills/vue-frontend/` |
| [docker-sgbd](/.opencode/skills/docker-sgbd/SKILL.md) | Docker / PostgreSQL / MySQL / MongoDB | BD, PW | `.opencode/skills/docker-sgbd/` |
| [selenium-testing](/.opencode/skills/selenium-testing/SKILL.md) | Selenium WebDriver | Testes | `.opencode/skills/selenium-testing/` |
| [git-github-workflow](/.opencode/skills/git-github-workflow/SKILL.md) | Git / GitHub | Todas | `.opencode/skills/git-github-workflow/` |

## Links úteis

- [Documentação oficial do opencode](https://opencode.ai/docs)
- [Configuração e schema](https://opencode.ai/config.json)
- [GitHub do opencode](https://github.com/anomalyco/opencode)
- [Guia de Skills](https://opencode.ai/docs/skills)
- [Skills avançadas (repositório vuejs-ai)](https://github.com/vuejs-ai/skills)
- [Guia de Agentes](https://opencode.ai/docs/agents)

## Arquivos de configuração

- `.opencode/AGENTS.md` — instruções gerais do repositório
- `.opencode/skills/*/SKILL.md` — Skills por stack
- `.opencode/agents/` — agentes (futuro)
