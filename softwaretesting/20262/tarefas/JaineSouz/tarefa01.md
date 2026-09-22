# Tarefa 01 - Teste de Unidade, Integração, Cobertura e CI

**Nome:** Jaine Souza da Luz  
**GitHub:** JaineSouz  
**E-mail:** jainesouza1520@gmail.com
**Repositório do projeto:** https://github.com/HelenaMariano2025/projetoPNLD

---

## 1. Testes de Unidade

Testes de unidade são testes realizados em pequenas partes isoladas de um sistema, como funções ou métodos. O objetivo é verificar se cada parte funciona conforme o esperado, facilitando a identificação de erros e evitando que alterações no código quebrem funcionalidades já existentes.

No projeto, foram utilizados testes de unidade para verificar as operações do CRUD de alunos, mantendo essas operações isoladas das dependências externas por meio de mocks.

## 2. Linguagem e Stack

A linguagem escolhida para o projeto foi **PHP**.

A stack utilizada é composta por:

- PHP 8.3;
- MySQL;
- MySQLi para comunicação com o banco de dados;
- PHPUnit para testes;
- Docker para execução do ambiente;
- Xdebug para coleta de cobertura de código;
- GitHub Actions para Integração Contínua (CI).

## 3. Framework de Testes de Unidade

Foi utilizado o **PHPUnit**, um framework de testes para PHP que permite criar e executar testes automatizados.

O PHPUnit foi utilizado para testar as regras do sistema, as operações do CRUD e a integração com o banco de dados.

**Site oficial:** https://phpunit.de/

## 4. IDE e Ferramentas de Debug

A IDE utilizada no desenvolvimento foi o **Visual Studio Code (VS Code)**.

O VS Code possui recursos de depuração (debug), como execução passo a passo, pontos de interrupção (breakpoints), inspeção de variáveis e acompanhamento da execução do programa.

No projeto também foi utilizado o **Xdebug**, integrado ao ambiente Docker, principalmente para obter a cobertura de código dos testes.

## 5. Tutorial de CRUD e Testes

Foi utilizado o tutorial:

**PHP MySQL CRUD Application:**  
https://www.tutorialrepublic.com/php-tutorial/php-mysql-crud-application.php

O tutorial apresenta a construção de uma aplicação CRUD utilizando PHP e MySQL, abordando operações de inserção, consulta, atualização e exclusão de dados.

Ele serviu como referência para compreender a estrutura das operações CRUD utilizadas no projeto.


## 6. Mocks Objects

Mocks são objetos simulados utilizados nos testes para representar dependências reais do sistema. Eles permitem testar uma unidade de forma isolada, sem precisar utilizar diretamente recursos externos, como banco de dados ou outros componentes.

No projeto, os mocks foram utilizados nos testes unitários do `AlunoRepository`. Foram simulados objetos do MySQLi, como `mysqli`, `mysqli_stmt` e `mysqli_result`. Dessa forma, foi possível verificar as operações do CRUD sem depender de uma conexão real com o banco de dados durante os testes unitários.

---

# 10. CRUD e Testes

## 10.1 CRUD implementado

Foi utilizado o CRUD da entidade **Aluno**, desenvolvido em PHP e integrado ao MySQL.

As operações de **inserção/cadastro e consulta** de alunos já estavam implementadas no projeto. Para atender aos requisitos da Tarefa 01, foram implementadas as operações que ainda não estavam disponíveis:

- **Inserir/Cadastrar:** operação que já estava disponível no projeto e permite cadastrar um novo aluno;
- **Consultar:** operação que já estava disponível no projeto e permite consultar os alunos ativos;
- **Atualizar:** operação implementada para permitir a alteração dos dados de um aluno;
- **Deletar/Inativar:** operação implementada como inativação do aluno, alterando sua situação para `inativo`.

Dessa forma, o CRUD utilizado no trabalho passou a contemplar as quatro operações exigidas pela tarefa: inserir, consultar, atualizar e deletar/inativar.

A implementação das novas operações foi realizada na classe `AlunoRepository`.

**Arquivo principal:**  
[AlunoRepository.php](https://github.com/HelenaMariano2025/projetoPNLD/blob/main/php/AlunoRepository.php)

## 10.2 Repositório do projeto

O projeto utilizado para a realização desta tarefa está disponível no GitHub:

**Repositório:** https://github.com/HelenaMariano2025/projetoPNLD

## 10.3 Tutorial de CRUD e testes no projeto

O README do projeto possui uma seção específica sobre o CRUD de alunos, contendo o tutorial utilizado como referência para a implementação das operações CRUD e informações sobre os testes realizados.

O tutorial utilizado foi:

**PHP CRUD Tutorial – Create, Read, Update & Delete:**  
https://www.tutorialrepublic.com/php-tutorial/php-mysql-crud-application.php

No README também são descritos os testes realizados com **PHPUnit**, incluindo os testes unitários do `AlunoRepository` e o teste de integração com o banco de dados MySQL.

**README do projeto:**  
https://github.com/HelenaMariano2025/projetoPNLD/blob/main/README.md

## 10.4 Testes de Unidade do CRUD

Foi implementado pelo menos um teste de unidade para cada operação do CRUD de alunos.

Os testes utilizam PHPUnit e Mock Objects para manter as operações isoladas do banco de dados.

Foram testadas as seguintes operações:

- inserção de aluno;
- consulta de alunos;
- atualização de aluno;
- inativação de aluno.

**Arquivo dos testes:**  
[AlunoRepositoryTest.php](https://github.com/HelenaMariano2025/projetoPNLD/blob/main/tests/AlunoRepositoryTest.php)

### Experiência

Como as operações de inserção e consulta já estavam implementadas no projeto, o trabalho envolveu inicialmente compreender essas funcionalidades e, posteriormente, implementar as operações de atualização e inativação. Em seguida, foram criados testes unitários para as quatro operações do CRUD, utilizando mocks para manter os testes isolados do banco de dados.

## 10.5 Teste de Integração

Também foi implementado um teste de integração para verificar a comunicação entre o código PHP e o banco de dados MySQL.

Diferentemente do teste de unidade, que isola uma parte do sistema utilizando mocks, o teste de integração verifica a interação entre componentes reais. Neste caso, o teste utiliza uma conexão real com o MySQL.

**Arquivo do teste:**  
[AlunoRepositoryIntegrationTest.php](https://github.com/HelenaMariano2025/projetoPNLD/blob/main/tests/AlunoRepositoryIntegrationTest.php)

## 10.6 Execução dos testes

A ferramenta escolhida para execução dos testes foi o **PHPUnit**.

Os testes foram executados no ambiente Docker utilizando o seguinte comando:

```bash
docker compose exec app php vendor/phpunit/phpunit/phpunit tests

```
A execução completa apresentou:

PHPUnit 12.5.35
Runtime: PHP 8.3.33

10 / 10 (100%)

Tests: 10, Assertions: 20

Foram executados testes relacionados às regras de negócio, às operações do CRUD de alunos e um teste de integração com o banco de dados.

Os testes foram concluídos com sucesso. O PHPUnit apresentou uma notificação durante a execução, mas ela não impediu a execução nem a aprovação dos testes.

## 10.7 Cobertura de código

Para calcular a cobertura de código foi utilizado o Xdebug, integrado ao ambiente Docker, juntamente com o PHPUnit.

Foi utilizado o seguinte comando:

```bash
docker compose exec -e XDEBUG_MODE=coverage app php vendor/phpunit/phpunit/phpunit tests --coverage-text --coverage-clover coverage.xml
```

O resultado obtido foi:

- Classes: 100.00% (1/1)
- Methods: 100.00% (5/5)
- Lines: 85.71% (42/49)

A cobertura de linhas obtida foi de 85,71%.

Também foi gerado o arquivo coverage.xml no formato Clover XML, compatível com ferramentas de análise de cobertura, como o SonarQube.

Arquivo de configuração:
phpunit.xml

## 10.8 Integração Contínua (CI)

Foi configurado um workflow do GitHub Actions para automatizar a execução dos testes e a geração da cobertura.

O workflow realiza as seguintes etapas:

1. Baixa o código do repositório;
2. Configura o PHP 8.3;
3. Instala as dependências com Composer;
4. Configura um banco de dados MySQL para os testes;
5. Importa a estrutura do banco de dados;
6. Executa os testes automatizados;
7. Calcula a cobertura utilizando Xdebug;
8. Gera o arquivo coverage.xml;
9. Publica o relatório de cobertura como artefato da execução.

**Arquivo do workflow:**

`.github/workflows/testes.yml`