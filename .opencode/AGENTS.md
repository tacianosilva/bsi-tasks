# bsi-tasks — Repositório de Apoio Didático

Este repositório contém materiais de aula, tutoriais e tarefas para as
disciplinas do curso de Bacharelado em Sistemas de Informação da UFRN/CERES:

- **Banco de Dados** (DCT2201, DCT2202)
- **Engenharia de Software**
- **Teste de Software**
- **Programação Web**

## Stacks principais

| Camada | Tecnologias |
|---|---|
| Backend | Python / Django / Django REST Framework |
| Backend | Java / Spring Boot / Spring Data JPA / WebFlux |
| Frontend | Vue 3 / Vite / Vitest |
| Database | PostgreSQL, MySQL, MariaDB, MongoDB |
| Testing | Selenium, JUnit 5, pytest, unittest |
| Infra | Docker, Git / GitHub |

## Skills disponíveis

Skills do opencode específicas para as stacks usadas nas disciplinas.
Localizadas em `.opencode/skills/<nome>/SKILL.md`.

- **django-backend** — desenvolvimento Django/DRF (ES, Testes, PW)
- **spring-boot-backend** — desenvolvimento Spring Boot (BD, ES)
- **vue-frontend** — desenvolvimento Vue 3 + Vite + Vitest (PW)
- **docker-sgbd** — execução de SGBDs com Docker (BD, PW)
- **selenium-testing** — testes de UI com Selenium (Testes)
- **git-github-workflow** — fluxo Git/GitHub (todas)

## Convenções

- Seguir as boas práticas e padrões de código adotados em cada disciplina.
- Sempre consultar o material de aula e tutoriais em `lessons/` e `database/`.
- Para testes, verificar os exemplos em `languages/java/testes/` e
  `languages/python/testes_unitarios/`.
- Manter a consistência com o estilo de código definido em `.editorconfig`.
- **Commits devem seguir o padrão [Conventional Commits](https://www.conventionalcommits.org/).**
  Usar `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`, etc.
