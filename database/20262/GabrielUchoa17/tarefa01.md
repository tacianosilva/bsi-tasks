# Tarefa 01 - Conceitos de BD, ACID e SGBD

**Aluno (GitHub):** GabrielUchoa17
**Disciplina:** Banco de Dados - BSI
**Issue relacionada:** #393

---

## Sobre o fluxo de trabalho com Git e GitHub

Antes das respostas, um resumo dos conceitos de versionamento usados nesta entrega.

### Branches (ramos)

Uma **branch** é uma linha independente de desenvolvimento dentro do repositório. Ela
funciona como um ponteiro móvel para um commit; a cada novo commit na branch, o ponteiro
avança. A branch `main` guarda a versão estável do projeto, enquanto branches de
funcionalidade (ex.: `tarefa01/GabrielUchoa17`) isolam um trabalho em andamento sem afetar
a `main`. Isso permite desenvolver, revisar e testar mudanças de forma segura e paralela.

### Pull Request / Merge Request

O **Pull Request** (nome usado no GitHub) ou **Merge Request** (GitLab) é o pedido formal
para incorporar as mudanças de uma branch em outra (tipicamente da *feature branch* para a
`main`). Ele abre espaço para **revisão de código**, discussão, execução de CI/testes
automatizados e registro histórico da decisão. No fluxo com *fork*, o PR parte da branch do
fork do aluno e tem como destino a branch `main` do repositório oficial.

### Merge

O **merge** combina o histórico de duas branches. No *fast-forward*, quando a branch de
destino não avançou, o ponteiro apenas "anda para a frente". Quando as duas branches
divergiram, o Git cria um **commit de merge** com dois pais, preservando o histórico
original de ambas as linhas.

### Rebase

O **rebase** reaplica os commits da sua branch a partir da ponta atual de outra branch,
reescrevendo o histórico e deixando-o linear (sem commit de merge). É útil para atualizar a
feature branch com a `main` mantendo o log limpo. Regra prática: **não fazer rebase de
commits já publicados/compartilhados**, pois isso reescreve os hashes e quebra o histórico
de quem já baixou.

### Conflitos

Um **conflito** ocorre quando o merge ou o rebase encontram alterações incompatíveis na
mesma região de um arquivo (ou arquivo removido de um lado e editado do outro). O Git marca
o trecho com `<<<<<<<`, `=======` e `>>>>>>>`; o desenvolvedor precisa editar o arquivo
escolhendo/combinando as versões, remover os marcadores, dar `git add` no arquivo
resolvido e concluir com `git commit` (merge) ou `git rebase --continue` (rebase).

---
