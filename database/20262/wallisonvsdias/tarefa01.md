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

---

## Q1. Banco de Dados vs. SGBD

### Banco de Dados (BD)
É uma coleção logicamente coerente e estruturada de dados relacionados, projetada para representar um aspecto específico do mundo real (minimundo) e atender às necessidades operacionais ou analíticas de usuários e sistemas. Os dados são organizados de modo a facilitar seu armazenamento, consulta e atualização, podendo estar centralizados em um servidor ou distribuídos por múltiplos nós.

### Sistema Gerenciador de Banco de Dados (SGBD / DBMS)
É o conjunto de softwares responsáveis por definir, construir, manipular, compartilhar e proteger as bases de dados. O SGBD atua como intermediário entre as aplicações usuárias e o armazenamento físico, fornecendo abstração de dados, mecanismos de controle de concorrência, recuperação após falhas, garantia de integridade e controle rígido de acesso e segurança.

### Exemplos de Bancos de Dados e seus respectivos SGBDs

| Categoria | SGBD | Exemplos Típicos de Bases de Dados |
| :--- | :--- | :--- |
| **Relacional (RDBMS)** | **PostgreSQL** | Base cadastral e financeira de um e-commerce |
| **Relacional (RDBMS)** | **MySQL / MariaDB** | Base transacional de um portal de notícias em WordPress |
| **Relacional Corporativo** | **Oracle Database** | Sistema contábil e de faturamento de uma multinacional |
| **NoSQL (Documentos)** | **MongoDB** | Catálogo de produtos com esquemas flexíveis e logs |
| **NoSQL (Chave-Valor)** | **Redis** | Armazenamento de sessões de usuários e cache de alta velocidade |