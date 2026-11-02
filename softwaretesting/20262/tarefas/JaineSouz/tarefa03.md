# Tarefa 03 - Implementação do User Story da Iteração 2 e Atuação como QA

## Identificação

- **Nome:** Jaine Souza da Luz
- **GitHub:** JaineSouz
- **E-mail:** [jainesouza1520@gmail.com](mailto:jainesouza1520@gmail.com)

## Links de Entrega

- **Pull Request do projeto:** Implementação da US04 — Gerenciar Turmas: [https://github.com/HelenaMariano2025/projetoPNLD/pull/19].
- **Relatório de QA:** Testes de aceitação da US06 — Registrar Empréstimos, desenvolvida por Helena: [https://github.com/HelenaMariano2025/projetoPNLD/blob/task/qa-us06/docs/qa/relatorio-aceitacao-us06.md].

## Issue

- **Tarefa 03 - Implementação do User Story da Iteração 2 e Atuação como QA #504**

## User Story Implementada

### US04 — Gerenciar Turmas

**Como** administrador,

**quero** cadastrar, consultar, alterar, excluir e pesquisar turmas pelo curso,

**para** manter as informações acadêmicas organizadas e disponíveis para a associação dos alunos.

O cadastro contempla código, curso, período, série e matriz curricular.

**Requisitos envolvidos:** RF1, RF2, RF7 e RF12.

### Critérios de Aceitação

- **\*\*TA04.01 — Cadastrar turma:\*\*** o sistema deve salvar uma turma com dados válidos e apresentar uma mensagem de sucesso.
- **\*\*TA04.02 — Consultar turma:\*\*** o sistema deve apresentar os dados correspondentes à turma selecionada.
- **\*\*TA04.03 — Alterar turma:\*\*** o sistema deve persistir as alterações e apresentar os dados atualizados em uma nova consulta.
- **\*\*TA04.04 — Excluir turma sem alunos vinculados:\*\*** o sistema deve confirmar a exclusão e deixar de apresentar a turma nas consultas seguintes.
- **\*\*TA04.05 — Pesquisar turmas pelo curso:\*\*** o sistema deve apresentar somente as turmas correspondentes ao curso pesquisado.
- **\*\*TA04.06 — Pesquisa sem resultados:\*\*** o sistema deve informar quando não houver turmas correspondentes ao curso pesquisado.
- **\*\*TA04.07 — Impedir cadastro de turma com código duplicado:\*\*** o sistema deve impedir o cadastro de uma turma com código já existente e apresentar a mensagem “Este código já pertence a uma turma cadastrada.”
- **\*\*TA04.08 — Impedir inativação de turma com alunos vinculados:\*\*** o sistema deve impedir a inativação de uma turma que possua alunos vinculados e apresentar a mensagem “Esta turma não pode ser excluída, pois existem alunos matriculados nela.”

A especificação também apresenta cenários adicionais para impedir o cadastro de códigos duplicados e a exclusão de turmas com alunos vinculados. Esses comportamentos devem ser considerados conforme as regras efetivamente definidas para a implementação.

## BDD / Gherkin

A especificação da US04 foi elaborada por Isabelle e utilizada como referência para o desenvolvimento da funcionalidade.

```gherkin
Funcionalidade: Gerenciar Turmas

  Como administrador
  Quero gerenciar as turmas
  Para manter as informações acadêmicas organizadas

  Cenário: Cadastrar turma
    Dado que o administrador está autenticado e na tela Turmas
    Quando informar os dados válidos da turma
    E confirmar o cadastro
    Então o sistema deve salvar a turma
    E apresentar uma mensagem de sucesso

  Cenário: Consultar turma
    Dado que existe uma turma cadastrada
    Quando o administrador selecionar a turma para consulta
    Então o sistema deve apresentar os dados correspondentes

  Cenário: Alterar turma
    Dado que existe uma turma cadastrada
    Quando o administrador alterar os dados e salvar
    Então o sistema deve confirmar a alteração
    E apresentar os dados atualizados em uma nova consulta

  Cenário: Excluir turma sem alunos vinculados
    Dado que existe uma turma sem alunos vinculados
    Quando o administrador confirmar a exclusão
    Então o sistema deve excluir a turma
    E deixar de apresentá-la nas consultas seguintes

  Cenário: Pesquisar turmas pelo curso
    Dado que existem turmas cadastradas em cursos diferentes
    Quando o administrador pesquisar por um curso
    Então o sistema deve apresentar as turmas correspondentes

  Cenário: Pesquisar curso sem turmas
    Dado que não existem turmas correspondentes ao curso pesquisado
    Quando o administrador realizar a pesquisa
    Então o sistema deve informar que nenhuma turma foi encontrada

    Cenário TA04.07 — Impedir cadastro de turma com código duplicado

    Dado que já existe uma turma cadastrada com determinado código  
    Quando o administrador tentar cadastrar outra turma utilizando o mesmo código  
    Então o sistema deverá impedir o cadastro  
    E apresentar a mensagem: “Este código já pertence a uma turma cadastrada.”

    Cenário TA04.08 — Impedir inativação de turma com alunos vinculados

    Dado que existe uma turma com alunos vinculados  
    Quando o administrador solicitar a inativação dessa turma  
    Então o sistema deverá impedir a operação  
    E apresentar a mensagem: “Esta turma não pode ser excluída, pois existem alunos matriculados nela.”
```

## Implementação da US04

A implementação da US04 — Gerenciar Turmas foi realizada no projeto `projetoPNLD`, utilizando uma branch específica para a funcionalidade.

O desenvolvimento teve como referência a especificação elaborada por Isabelle, incluindo as regras de negócio, os critérios de aceitação e os cenários BDD.

A funcionalidade tem como objetivo permitir o gerenciamento das turmas do sistema, contemplando cadastro, consulta, alteração, exclusão e pesquisa pelo curso.

As informações previstas na especificação são:

- Código da turma.
- Curso.
- Período.
- Série.
- Matriz curricular.

A implementação deve manter a consistência entre as informações exibidas na interface e os dados persistidos no banco de dados, respeitando as regras de negócio relacionadas à exclusão e à associação de alunos.

**Pull Request da implementação:** [https://github.com/HelenaMariano2025/projetoPNLD/pull/19].

## Testes Automatizados da US04

Os testes automatizados relacionados à US04 devem verificar o comportamento das operações implementadas, incluindo as regras de validação e a persistência dos dados.

A documentação dos testes deve contemplar:

- Testes unitários das regras e validações, utilizando mocks quando necessário.
- Testes de integração com o banco de dados.
- Verificação do cadastro, consulta e alteração de turmas.
- Verificação da exclusão conforme as regras de negócio.
- Verificação da pesquisa pelo curso.
- Tratamento de entradas inválidas e pesquisas sem resultados.

### Resultado dos testes da US04
Os testes específicos da US04 — Gerenciar Turmas apresentaram os seguintes resultados:

Testes executados: 6
Asserções: 39
Falhas: 0 (não relatadas na revisão)
Erros: 0 (não relatados na revisão)

Os resultados foram compostos por:

Testes unitários: 5 testes, com 37 verificações.

Teste de integração: 1 teste, com 2 verificações.

## Cobertura de Código

Não foi possível confirmar o percentual de cobertura de código específico da US04 — Gerenciar Turmas, pois não foi consultado um relatório de cobertura correspondente ao estado da implementação no momento da entrega.


## Análise SonarQube da US04

Durante o desenvolvimento da US04, o SonarQube foi utilizado como ferramenta de análise estática da qualidade do projeto.

Entretanto, não foi possível recuperar os resultados específicos da análise referentes ao estado do código no momento da conclusão da implementação. Após a submissão do Pull Request da US04, outras alterações foram integradas ao projeto, de modo que os resultados atualmente disponíveis podem refletir uma versão posterior.

Por esse motivo, não serão atribuídos à US04 valores específicos de bugs, vulnerabilidades, code smells, cobertura ou Quality Gate sem evidências que comprovem que esses resultados correspondem ao estado do código naquele momento.

Essa limitação será registrada para preservar a confiabilidade das informações apresentadas.

## Atuação como Revisora — US05: Gerenciar Livros

Além da implementação da US04, foi realizada a revisão do Pull Request #16, referente à US05 — Gerenciar Livros, desenvolvida por Isabelle Cavalcanti da Silva.

A atividade consistiu na revisão da implementação submetida ao repositório do projeto e na execução da suíte de testes automatizados na branch do Pull Request.

A revisão foi realizada considerando a proposta da funcionalidade de gerenciamento de livros e as evidências obtidas durante a execução dos testes.

### Execução dos testes automatizados da US05

Os testes foram executados no ambiente Docker utilizando o PHPUnit.

Resultado registrado:

```text
Tests: 53
Assertions: 268
Failures: 0
Errors: 0
PHPUnit Notices: 4
```

Todos os 53 testes foram concluídos sem falhas, totalizando 268 asserções.

O PHPUnit apresentou quatro notices relacionados a mocks sem expectativas configuradas:

- Três notices em testes do arquivo `LoginTest.php`.
- Um notice em um teste do arquivo `TurmaRepositoryTest.php`.

Esses avisos foram registrados separadamente do resultado da execução. Não houve falhas ou erros na suíte executada.

A atividade corresponde à revisão do código e à execução dos testes automatizados do PR da US05. Não representa uma análise completa de cobertura nem substitui os testes de aceitação previstos para a funcionalidade.

## Atuação como QA — US06: Registrar Empréstimos

Foi realizada a atividade de QA da US06 — Registrar Empréstimos, desenvolvida por Helena, como parte da Tarefa 03 da disciplina de Teste de Software.

A especificação da US06 foi elaborada por Jaine Souza da Luz e utilizada como referência para a avaliação da funcionalidade, considerando as regras de negócio e os critérios de aceitação definidos em BDD/Gherkin.

A funcionalidade tem como objetivo permitir o registro de empréstimos de livros para alunos, mantendo a associação entre aluno, livro, administrador responsável, data do empréstimo e data prevista de devolução, além de garantir a consistência entre o registro do empréstimo e a quantidade disponível em estoque.

### Critérios de aceitação utilizados na avaliação

- **TA06.01 — Registrar empréstimo válido:** verificar se um empréstimo é registrado quando o aluno existe e o livro possui quantidade disponível.
- **TA06.02 — Associar os dados do empréstimo:** verificar a associação entre aluno, livro, administrador responsável e datas.
- **TA06.03 — Calcular data prevista:** verificar se a data de devolução prevista corresponde à data do empréstimo acrescida de 20 dias.
- **TA06.04 — Impedir empréstimo sem aluno:** verificar se o sistema rejeita o registro sem matrícula do aluno.
- **TA06.05 — Impedir empréstimo sem livro:** verificar se o sistema rejeita o registro sem identificação do livro.
- **TA06.06 — Impedir empréstimo de livro indisponível:** verificar se o sistema impede o empréstimo quando a quantidade disponível é zero.
- **TA06.07 — Atualizar quantidade disponível:** verificar se a quantidade disponível é reduzida em uma unidade após um empréstimo válido.
- **TA06.08 — Impedir quantidade negativa:** verificar se a quantidade disponível permanece não negativa.
- **TA06.09 — Tratar livro inexistente:** verificar se o sistema rejeita a identificação de um livro que não existe.
- **TA06.10 — Associar administrador responsável:** verificar se o empréstimo fica associado ao administrador autenticado.
- **TA06.11 — Integrar as regras à aplicação:** verificar se as regras de validação e disponibilidade são executadas pelo fluxo real da página.
- **TA06.12 — Manter consistência entre empréstimo e estoque:** verificar se o registro do empréstimo e a atualização da quantidade disponível permanecem consistentes.

### Procedimento dos testes de aceitação

Os testes manuais foram realizados no ambiente disponibilizado pelo projeto, utilizando a implementação da US06 e os critérios de aceitação definidos na especificação.

Durante a avaliação, foi identificada uma dificuldade de acesso à funcionalidade de consulta de livros. Ao selecionar a opção “Livros” e realizar a autenticação, o sistema retornou à página inicial em vez de abrir a tela correspondente. Essa situação impediu a consulta do estoque e a obtenção de um código de livro válido para concluir parte dos cenários.

### Resultados dos testes de aceitação

| Resultado | Quantidade |
|---|---:|
| Testes aprovados | 0 confirmados |
| Testes reprovados | 0 confirmados |
| Testes bloqueados | 11 |
| Testes parcialmente verificados | 1 |
| Total de critérios avaliados | 12 |

**Observação:** a classificação representa o estado da avaliação documentada. Os 11 cenários bloqueados não devem ser interpretados automaticamente como falhas da implementação, pois a impossibilidade de consultar os livros impediu a conclusão dos testes. O cenário parcialmente verificado corresponde ao tratamento de livro inexistente.

### Testes automatizados

A suíte automatizada foi executada no ambiente Docker utilizando o PHPUnit, com o seguinte resultado:

```text
Testes: 48
Asserções: 227
Falhas: 0
Erros: 1
```

O erro ocorreu no teste `EmprestimoRepositoryTest::testNaoPermiteRegistrarMesmaDevolucaoDuasVezes`. Durante a execução, houve conflito com a matrícula `20212021`, já existente no banco de dados, e uma falha na limpeza dos dados devido a uma restrição de chave estrangeira.

Esse resultado indica um problema relacionado aos dados de teste e à limpeza do ambiente. Não é suficiente, isoladamente, para concluir que a funcionalidade de registro de empréstimos está incorreta. A suíte precisa ser executada novamente em condições controladas para confirmar o resultado após a correção do problema de isolamento dos testes.

### Problemas e oportunidades de melhoria identificados

- Verificar o fluxo de autenticação e navegação da opção “Livros”, que impediu a continuidade dos testes manuais.
- Melhorar o isolamento dos testes automatizados, evitando conflitos com matrículas e empréstimos já existentes no banco de dados.
- Garantir que a limpeza dos dados de teste respeite as dependências e restrições de chave estrangeira.
- Reexecutar os cenários de aceitação após a resolução dos bloqueios para confirmar o comportamento do sistema.

### Relatório de QA

O relatório detalhado de testes de aceitação foi documentado em Markdown no repositório do projeto PNLD.

**Relatório:** [`docs/qa/relatorio-aceitação-us06.md`](https://github.com/HelenaMariano2025/projetoPNLD/blob/task/qa-us06/docs/qa/relatorio-aceitacao-us06.md)

**Pull Request da documentação de QA:** inserir o link do PR aberto para a branch [`PR documentação QA`](https://github.com/HelenaMariano2025/projetoPNLD/pull/21).

O relatório reúne os resultados observados, as limitações da avaliação e os problemas que precisam ser considerados na análise da funcionalidade.

## Considerações Finais

A Tarefa 03 contempla a implementação da US04 — Gerenciar Turmas, a revisão do código da US05 — Gerenciar Livros e a atuação como QA da US06 — Registrar Empréstimos.

Na implementação da US04, a especificação elaborada por Isabelle serviu como referência para o desenvolvimento da funcionalidade. 

Na revisão da US05, foram executados 53 testes automatizados, com 268 asserções e nenhuma falha ou erro. Quatro notices do PHPUnit foram registrados separadamente.

Na atuação como QA da US06 — Registrar Empréstimos, foram realizados testes manuais e executada a suíte automatizada do projeto. A avaliação manual foi limitada por um problema de navegação no acesso à tela de livros, enquanto a execução automatizada apresentou 48 testes, 227 asserções e um erro associado à duplicidade de dados e à limpeza do ambiente de testes. Os resultados e as limitações foram documentados no relatório de QA, sem atribuir à implementação defeitos que não puderam ser confirmados. O relatório foi submetido por meio de um Pull Request específico de documentação no repositório do projeto.
