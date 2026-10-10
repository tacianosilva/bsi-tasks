# Tarefa 01 - Teste de Unidade, Integração, Cobertura e CI

## 1. Teste Unitário

O teste unitário é utilizado para verificar uma pequena parte isolada do sistema, normalmente uma função, método ou classe. O objetivo é verificar se essa unidade apresenta o comportamento esperado sem depender de outras partes do sistema.

No projeto PNLD, foram desenvolvidos testes unitários para a classe `TurmaRepository`, responsável pelas operações relacionadas às turmas.

Foram testadas as seguintes operações:

* Inserção de uma turma;
* Consulta de turmas ativas;
* Atualização de uma turma;
* Inativação de uma turma.

Para evitar a dependência do banco de dados durante os testes unitários, foram utilizados mocks do PHPUnit para simular as classes `mysqli` e `mysqli_stmt`.

### Framework utilizado

Foi utilizado o **PHPUnit**, framework de testes para PHP.

Versão utilizada:

```text
PHPUnit 12.5.35
```

Os testes foram executados utilizando PHP 8.4.8.

### Mocks

Os mocks foram utilizados para simular a conexão e as operações com o banco de dados. Dessa forma, os testes unitários verificam o comportamento do `TurmaRepository` sem precisar acessar o banco de dados real.

Por exemplo, no teste de inserção, o mock verifica se o método `prepare()` é chamado, se os parâmetros são vinculados corretamente com `bind_param()` e se o comando `execute()` retorna `true`.

### Resultado dos testes unitários

A execução dos testes unitários apresentou:

```text
Tests: 4, Assertions: 30
```

Os 4 testes foram executados com sucesso.

## 2. Teste de Integração

O teste de integração verifica se diferentes partes do sistema funcionam corretamente quando utilizadas em conjunto. Diferentemente do teste unitário, ele pode utilizar dependências reais, como banco de dados, arquivos ou serviços externos.

No projeto PNLD, foi criado um teste de integração para o `TurmaRepository`, utilizando uma conexão real com o banco de dados MariaDB.

O teste realiza as seguintes etapas:

1. Conecta ao banco de dados real;
2. Insere uma turma de teste;
3. Consulta as turmas ativas;
4. Verifica se a turma inserida foi encontrada;
5. Remove a turma de teste ao final da execução.

A turma utilizada no teste possui o código `9999`, sendo removida posteriormente para não deixar dados de teste no banco.

### Diferença entre teste unitário e teste de integração

O teste unitário verifica uma unidade do sistema de forma isolada, utilizando mocks para substituir suas dependências.

Já o teste de integração verifica a comunicação entre diferentes componentes utilizando suas dependências reais.

No projeto:

* **Teste unitário:** `TurmaRepositoryTest.php`, utilizando mocks e sem acesso ao banco real.
* **Teste de integração:** `TurmaRepositoryIntegrationTest.php`, utilizando o MariaDB real.

### Resultado do teste de integração

A execução apresentou:

```text
Tests: 1, Assertions: 2
OK
```

O teste confirmou que a turma foi inserida no banco e posteriormente encontrada pela consulta de turmas ativas.

## 3. Cobertura de Código

A cobertura de código foi realizada utilizando o **Xdebug** em conjunto com o PHPUnit.

O Xdebug foi instalado no ambiente PHP e utilizado para gerar um relatório de cobertura no formato **Clover XML**.

O comando utilizado foi:

```bash
XDEBUG_MODE=coverage ./vendor/bin/phpunit tests/TurmaRepositoryTest.php tests/TurmaRepositoryIntegrationTest.php --coverage-clover coverage.xml
```

A execução apresentou:

```text
Tests: 5, Assertions: 32
```

Todos os 5 testes foram executados com sucesso.

### Resultado da cobertura do TurmaRepository

O relatório `coverage.xml` apresentou os seguintes resultados para o `TurmaRepository`:

```text
Methods: 5
Covered methods: 5

Statements: 37
Covered statements: 37
```

Isso representa:

* **100% dos métodos cobertos**;
* **100% das instruções cobertas**.

O relatório foi gerado no arquivo:

```text
coverage.xml
```

Esse arquivo utiliza o formato **Clover XML**, permitindo seu uso por ferramentas de análise de qualidade de código, como o SonarQube.

### Configuração do SonarQube

No arquivo `sonar-project.properties`, foi configurado o caminho do relatório de cobertura:

```text
sonar.php.coverage.reportPaths=coverage.xml
```

Dessa forma, o SonarQube pode utilizar os dados gerados pelo PHPUnit para analisar a cobertura do código.

## 4. Integração Contínua (CI)

Foi configurado um workflow do GitHub Actions para executar automaticamente os testes do projeto. O workflow é executado quando ocorre um `push` nas branches `main` e `task/**`, ou quando é aberto um Pull Request direcionado para a branch `main`.

O ambiente utilizado pelo workflow é o `ubuntu-latest`, com um serviço MySQL 8.4 executado em um container. O banco de dados de testes utiliza as seguintes configurações:

* Banco: `SistemaHBL`
* Usuário: `pnld`
* Senha: `pnld_local`
* Porta: `3306`

O serviço MySQL possui uma verificação de saúde para garantir que o banco esteja disponível antes da execução das etapas seguintes.

O workflow realiza as seguintes etapas:

1. Baixa o código do repositório utilizando `actions/checkout@v4`.
2. Configura o PHP 8.3 utilizando `shivammathur/setup-php@v2`, com as extensões `mysqli` e `xdebug`.
3. Instala as dependências do projeto com o Composer.
4. Instala o cliente MySQL e executa o arquivo `sql/bancoPNLD.sql` para preparar o banco de dados de testes.
5. Executa os testes do PHPUnit com o Xdebug habilitado para gerar cobertura de código.
6. Gera o arquivo `coverage.xml` no formato Clover.
7. Publica o arquivo de cobertura como um artefato chamado `coverage-report`.

O comando utilizado para executar os testes e gerar a cobertura é:

```bash
php vendor/phpunit/phpunit/phpunit tests \
  --coverage-text \
  --coverage-clover coverage.xml
```

As variáveis de ambiente utilizadas durante essa etapa são:

```text
XDEBUG_MODE=coverage
DB_HOST=127.0.0.1
DB_USER=pnld
DB_PASSWORD=pnld_local
DB_NAME=SistemaHBL
```

Dessa forma, o GitHub Actions automatiza a instalação do ambiente, a preparação do banco de dados, a execução dos testes e a geração do relatório de cobertura, permitindo verificar automaticamente se os testes continuam funcionando a cada alteração no projeto.
