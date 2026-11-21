# Respostas das Tarefas — Banco de Dados (2026.2)

Este diretório reúne as **respostas das tarefas** da disciplina de Banco de Dados do semestre 2026.2.

## Estrutura

Cada discente deve criar uma pasta com o seu **nome de usuário do GitHub** dentro deste diretório, seguindo o padrão:

- `database/20262/<username>/`

Dentro dela, são colocados os arquivos **Markdown** de resposta de cada tarefa, como por exemplo:

- `tarefa01.md`
- `tarefa02.md`

## Observação

Este diretório contém, em geral, **apenas arquivos Markdown de resposta** das tarefas. Os enunciados das tarefas, materiais, links e tutoriais ficam na pasta `database/tarefas/` deste repositório.

Cada resposta deve ser entregue por meio de um **pull request** da sua **feature branch (fork)** para a **branch main (bsi-tasks)**, conforme instruções de cada tarefa.

### 📌 Boas Práticas de Branches (Importante)

- **Ramificação sempre a partir da `main`:** Ao iniciar qualquer tarefa (`tarefa01`, `tarefa02`, etc.), sincronize seu fork com o repositório original (`upstream/main`), posicione-se na branch `main` e crie a branch da tarefa a partir dela:
  ```bash
  git checkout main
  git pull upstream main
  git checkout -b tarefa02/<username>
  ```
- **Nunca ramifique em cascata:** Nunca crie uma branch de nova tarefa sobre a branch de uma tarefa anterior que ainda esteja aguardando avaliação. Cada tarefa é autocontida e deve ter sua branch criada a partir da `main` limpa para não acumular commits ou arquivos de tarefas distintas no mesmo Pull Request.
- Para mais detalhes sobre o fluxo de trabalho e boas práticas de Git/GitHub, consulte o [Guia de Git e GitHub](https://github.com/tacianosilva/engenharia-software/blob/main/docs/github.md#boas-pr%C3%A1ticas-de-git-para-tarefas-acad%C3%AAmicas-gitflow-simplificado).
