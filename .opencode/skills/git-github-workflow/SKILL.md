---
name: git-github-workflow
description: Use ao realizar operações Git e GitHub nas disciplinas do BSI/UFRN que utilizam controle de versão.
---

# Git / GitHub Workflow

## Perfil

Fluxo de trabalho com Git e GitHub adotado nas disciplinas do BSI para
controle de versão de projetos e tarefas.

## Fluxo básico (GitFlow simplificado)

```bash
# Iniciar feature
git checkout -b feature/nome-da-feature

# Commits atômicos e descritivos
git add .
git commit -m "tipo: descrição concisa"

# Sincronizar
git pull --rebase origin main
git push origin feature/nome-da-feature

# Abrir Pull Request no GitHub
```

## Estrutura de branches

- `main` — branch principal, estável
- `feature/*` — desenvolvimento de novas funcionalidades
- `fix/*` — correção de bugs

## Convenções de commit

**Todos os commits neste repositório devem seguir o padrão
[Conventional Commits](https://www.conventionalcommits.org/).**

O formato é:

```
tipo(escopo opcional): descrição em português ou inglês

corpo opcional (quebras de linha a cada 72 caracteres)

rodapé opcional (ex.: BREAKING CHANGE, closes #123)
```

### Tipos

| Tipo | Uso |
|---|---|
| `feat` | Nova funcionalidade |
| `fix` | Correção de bug |
| `docs` | Documentação |
| `refactor` | Refatoração (sem mudar comportamento) |
| `test` | Adição ou correção de testes |
| `chore` | Tarefas de manutenção (build, dependências, CI) |
| `style` | Formatação, lint (sem mudar lógica) |
| `perf` | Melhoria de performance |

### Exemplos

```
feat: adiciona endpoint de login com JWT
fix: corrige validação de CPF no formulário
docs: atualiza README com instruções de instalação
refactor: extrai lógica de pagamento para serviço
test: adiciona testes unitários para o serializer UsuarioSerializer
chore: atualiza dependências do requirements.txt
```

## Referências

- `lessons/dev-web-django.md` — aula 04 sobre Git/GitHub
- [Conventional Commits](https://www.conventionalcommits.org/)
- [GitHub Flow Guide](https://docs.github.com/en/get-started/using-github/github-flow)
