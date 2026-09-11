# Tarefa 01 - Conceitos de Banco de Dados, ACID e SGBD

## Fundamentos de Controle de Versão (Git e GitHub)

### Branches
São ramificações independentes da linha do tempo do projeto. Permitem isolar o desenvolvimento de novas funcionalidades, experimentos ou correções de bugs sem interferir diretamente na branch principal (`main`). Isso possibilita que múltiplos desenvolvedores trabalhem em paralelo de forma segura.

### Pull Request (ou Merge Request)
Mecanismo de colaboração em plataformas como GitHub ou GitLab pelo qual um desenvolvedor solicita que as alterações realizadas em sua branch (ou fork) sejam revisadas e incorporadas à branch de destino. O Pull Request é o espaço central para code review, debates técnicos, execução de testes automatizados (CI) e validações antes da integração.

### Merge
Operação do Git que combina o histórico de duas branches distintas. Ao executar o merge, o Git junta os conjuntos de commits. Quando há divergências de histórico, ele gera um novo commit de junção (chamado de *merge commit*), preservando a história exata de como as branches foram desenvolvidas paralelamente.

### Rebase
Processo alternativo de integração que move ou reaplica uma sequência de commits de uma branch sobre a ponta mais recente de outra branch. Em vez de criar um commit de junção como o merge, o rebase reescreve o histórico de forma linear, facilitando a leitura da linha do tempo do projeto.

### Conflitos
Situação que ocorre quando dois desenvolvedores (ou branches) alteram as mesmas linhas de um mesmo arquivo — ou quando um arquivo é excluído em uma branch e modificado em outra — e o Git tenta uni-los. Como o sistema não pode decidir automaticamente qual alteração é a correta sem risco de perda de lógica, ele suspende a operação e solicita que o desenvolvedor resolva manualmente as seções conflitantes antes de concluir a integração.