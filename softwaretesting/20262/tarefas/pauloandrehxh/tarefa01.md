# Tarefa 01 - Teste de Unidade, Integração, Cobertura e CI

**Discente:** Paulo André Alves de Moura

**GitHub:** @pauloandrehxh

**E-mail:** paulo.moura.701@ufrn.edu.br

**Repositório do projeto:** [Arena UFRN](https://github.com/pauloandrehxh/arena-ufrn)

**Issue da atividade:** [Issue da Tarefa 01](https://github.com/tacianosilva/bsi-tasks/issues/457)

## 1. Testes de Software e Testes de Unidade

Testes de software são utilizados para verificar se uma aplicação apresenta o comportamento esperado e para identificar erros antes que eles cheguem ao usuário final.

Entre os diferentes níveis de teste, os **Testes de Unidade** têm como objetivo verificar pequenas partes do sistema de maneira isolada, como funções, métodos ou serviços.

Uma das principais características dos testes unitários é a redução de dependências externas. Elementos como bancos de dados, APIs e outros serviços podem ser substituídos por objetos simulados, permitindo que apenas a unidade desejada seja testada.

Entre os benefícios dos testes unitários estão:

* identificação rápida de erros;
* maior segurança durante refatorações;
* documentação do comportamento esperado do código;
* execução rápida dos testes;
* isolamento das regras de negócio;
* redução de regressões durante o desenvolvimento.

## 2. Linguagem e Stack Utilizada

A linguagem escolhida para o desenvolvimento do projeto foi **JavaScript**.

O projeto utilizado nesta atividade é o **Arena UFRN**, uma aplicação web para gerenciamento e reserva de quadras.

A stack utilizada atualmente é:

### Backend

* Node.js;
* Express;
* JavaScript com ES Modules;
* Prisma ORM;
* SQLite;
* Better SQLite3.

### Frontend

* React;
* Vite;
* Tailwind CSS;
* JavaScript.

### Testes e qualidade

* Jest;
* Supertest;
* SonarQube;
* GitHub Actions.

### Gerenciamento e versionamento

* pnpm;
* Git;
* GitHub.

## 3. Framework de Testes de Unidade

O framework escolhido foi o **Jest**.

O Jest é um framework de testes para JavaScript que fornece recursos para criação, organização e execução de testes automatizados.

Entre os principais recursos utilizados no projeto estão:

* `describe()` para agrupar testes relacionados;
* `test()` para definir casos de teste;
* `expect()` para realizar verificações;
* `jest.fn()` para criar funções mock;
* `mockResolvedValue()` para simular retornos assíncronos;
* `mockRejectedValue()` para simular erros;
* geração automática de relatórios de cobertura.

No projeto também é utilizado o **Supertest**, que permite realizar requisições HTTP diretamente contra uma aplicação Express durante os testes, sem a necessidade de iniciar o servidor em uma porta real.

### Links

* Documentação oficial do Jest: [Link Jest](https://jestjs.io/docs/getting-started)
* Documentação do Supertest: [Link Supertest](https://www.npmjs.com/package/supertest)

## 4. Ambiente de Desenvolvimento e Debug

A IDE/editor utilizado durante o desenvolvimento é o **Visual Studio Code**.

O VS Code possui suporte integrado para depuração de aplicações JavaScript e Node.js.

Entre os recursos utilizados ou disponíveis estão:

* breakpoints;
* execução passo a passo;
* inspeção de variáveis;
* call stack;
* watch expressions;
* Debug Console;
* execução e depuração através do terminal integrado;
* Auto Attach para processos Node.js;
* configuração de depuração através do arquivo `launch.json`.

Essas ferramentas facilitam a identificação de problemas durante o desenvolvimento sem depender apenas de mensagens adicionadas através de `console.log()`.

### Link

* Documentação de Debug do VS Code: [Link Docs Debug](https://code.visualstudio.com/docs/debugtest/debugging)

## 5. Tutorial de CRUD e Testes

Como referência para o desenvolvimento e estudo dos testes foi utilizado um tutorial sobre criação e teste de APIs CRUD utilizando Node.js, Express, Jest e Supertest.

O tutorial apresenta conceitos relacionados a:

* criação de endpoints REST;
* operações de criação, consulta, atualização e exclusão;
* configuração do Jest;
* utilização do Supertest;
* testes dos endpoints da aplicação;
* verificação dos códigos de status HTTP;
* validação das respostas da API.

**Tutorial:** [Link Tutorial](https://www.youtube.com/watch?v=vDLE8hqzA8I)

Como material complementar, também foi utilizada a documentação do Prisma sobre testes, especialmente os conteúdos relacionados a testes unitários, mocks e testes de integração.

**Documentação Testes do Prisma**: [Link Prisma Docs](https://www.prisma.io/blog/series/testing-with-prisma)

## 6. Mock Objects

Mock Objects são objetos simulados utilizados durante os testes para substituir dependências reais de uma unidade de código.

Por exemplo, um service pode depender do Prisma para realizar uma consulta ao banco de dados. Em um teste unitário, não é necessário acessar o banco real. Em vez disso, é possível substituir o Prisma por um mock.

Um exemplo simplificado é:

```javascript
const prismaMock = {
    usuario: {
        findMany: jest.fn(),
        findUnique: jest.fn(),
        create: jest.fn(),
        update: jest.fn(),
        delete: jest.fn()
    }
};
```

Dessa forma, o teste pode determinar previamente o comportamento da dependência.

Por exemplo:

```javascript
prismaMock.usuario.findMany.mockResolvedValue([
    {
        id: 1,
        name: 'Paulo'
    }
]);
```

O uso de mocks ajuda a:

* isolar a unidade testada;
* evitar alterações no banco de dados real;
* simular diferentes situações;
* simular erros;
* tornar os testes mais rápidos;
* tornar os testes mais previsíveis.

No Arena UFRN, a arquitetura baseada em injeção de dependência facilita a utilização de mocks do Prisma nos testes.
