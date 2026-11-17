 # Tarefa 01 \- Teste de Unidade, Integração, Cobertura e CI
 nome: 
luis felipe linhares pereira
 Usuario Github: 
luisfelipelinhares
 E-mail:
luis.felipe.linhares.701@ufrn.edu.br
 link:
https://github.com/pauloandrehxh/arena-ufrn

 ## 1\. Testes de Software e Testes de Unidade

 Testes de software são procedimentos realizados para verificar se um sistema funciona conforme o esperado e para encontrar erros antes que eles cheguem aos usuários. Entre os diferentes tipos de testes, os **testes de unidade** verificam pequenas partes isoladas do sistema, como funções, métodos ou serviços.

 No projeto Arena UFRN, os testes de unidade podem ser utilizados, por exemplo, para verificar as regras presentes nos serviços de usuários e quadras sem depender diretamente da interface ou de outros componentes.

 **Resumo:** testes de unidade permitem verificar componentes individualmente, tornando a identificação de erros mais rápida e facilitando a manutenção e evolução do sistema.

 ## 2\. Linguagem de programação e stack

 Para o projeto, a stack escolhida é:

 - **Linguagem:** JavaScript.
- **Runtime:** Node.js.
- **Backend:** Express.
- **Frontend:** React + Vite.
- **Banco de dados:** SQLite.
- **ORM:** Prisma.
- **Testes:** Jest.
- **Testes HTTP:** Supertest.
- **Gerenciador de pacotes:** pnpm.

 Essa escolha também está alinhada à implementação atual do repositório Arena UFRN, que já possui frontend em React/Vite, backend em Node.js/Express, SQLite com Prisma e testes com Jest e Supertest.  GitHub

  ## 3\. Framework de Testes de Unidade — Jest

 O **Jest** é um framework de testes para JavaScript, desenvolvido com foco em simplicidade. Ele permite criar testes, fazer asserções com `expect`, utilizar mocks e executar os testes de maneira isolada. A documentação oficial disponibiliza suporte para projetos JavaScript, Node.js, React e outras tecnologias.  Jest+1

 No Arena UFRN, o Jest já está sendo utilizado para os testes automatizados do backend.  GitHub

 **Resumo:** Jest fornece uma estrutura completa para escrever e executar testes automatizados em JavaScript, sendo adequado para testar funções, serviços e outras partes do backend.

 **Links:**

 - Documentação oficial do Jest
- Site oficial do Jest

## 4\. IDE e ferramentas de Debug

 A IDE utilizada para o desenvolvimento pode ser o **IntelliJ IDEA**, que possui suporte a JavaScript e Node.js por meio de seus recursos e plugins.

 O debugger integrado permite executar o programa passo a passo e investigar o estado da aplicação. Entre seus recursos estão **breakpoints**, execução linha a linha, inspeção de variáveis, avaliação de expressões e acompanhamento do ponto atual de execução.  JetBrains+1

 Esses recursos são úteis para encontrar erros na lógica dos serviços e controladores da API sem precisar adicionar vários `console.log()` ao código.

 **Link:**  Documentação do Debugger do IntelliJ IDEA


 ## 5\. Tutorial de CRUD e testes

 Um material relacionado diretamente à stack escolhida é o exemplo oficial do Prisma para criação de uma API REST com **Node.js, Express e Prisma**. O tutorial apresenta a construção de uma aplicação REST e suas operações de acesso aos dados.  Prisma 1

 Além disso, o próprio projeto oficial de exemplos do Prisma possui um exemplo de **Express + Prisma + Jest + Supertest**, mostrando como realizar testes automatizados em uma API.  GitHub+1

 **Links:**

 - Tutorial de API REST com Express e Prisma  — apresenta a construção de uma API utilizando Node.js, Express e Prisma.
- Exemplo oficial de testes com Express, Prisma, Jest e Supertest  — mostra testes automatizados de uma aplicação Express utilizando Prisma e Supertest.

 Esses materiais são particularmente relacionados ao Arena UFRN porque o projeto também utiliza Express, Prisma, CRUD e testes automatizados.  GitHub

 ## 6\. Mock Objects em Testes de Unidade

 **Mock Objects** são objetos simulados utilizados durante os testes para substituir dependências reais. Em vez de um teste acessar diretamente um banco de dados, uma API externa ou outro serviço, podemos criar um mock que imita o comportamento dessa dependência.

 Por exemplo, ao testar o serviço de usuários, podemos simular uma resposta do Prisma sem realmente consultar o SQLite. Dessa forma, o teste fica mais rápido, previsível e isolado.

 O Mockito é um exemplo de framework de mocking bastante utilizado no ecossistema Java. No JavaScript/Jest, o próprio Jest possui recursos de mock, e a documentação do Prisma também apresenta estratégias para criar mocks do Prisma Client durante testes unitários.  GitHub+1

 **Resumo:** mocks substituem dependências reais durante o teste, permitindo testar apenas o comportamento do componente que está sendo analisado. No Arena UFRN, isso pode ser útil principalmente para testar os serviços sem depender diretamente do banco SQLite.\
 :::
 Abaixo está um roteiro **passo a passo, pensado para terceiros**, para cumprir os itens 3–8 no projeto `arena-ufrn`, assumindo **Node.js + Jest**. Como o repositório é externo, os comandos devem ser executados na cópia local do projeto.

 ## 1\. Clonar e preparar o projeto

```
git clone https://github.com/pauloandrehxh/arena-ufrn.git
cd arena-ufrn
npm install
```

 Confirme que o projeto executa normalmente:

```
npm test
```

 Se ainda não existir Jest:

```
npm install --save-dev jest
```

 No `package.json`, deixe um script semelhante a:

```
"scripts": {
  "test": "jest",
  "test:coverage": "jest --coverage"
}
```
## 2. Executar os testes

Execute o comando abaixo no terminal:

npm test


Após a execução, guarde a saída real apresentada pelo terminal.

Um exemplo de saída é:

Test Suites: 1 passed, 1 total
Tests:       7 passed, 7 total
Snapshots:   0 total
Time:        0.385 s, estimated 1 s
Ran all test suites.

## 3 Gerar cobertura

Execute o comando abaixo:

pnmp test:covarage


A execução apresentará os dados de cobertura, como no exemplo abaixo:

File      | % Stmts | % Branch | % Funcs | % Lines | Uncovered Line #s
All files |   77.77 |      100  |      75 |   77.77 |
app.js    |   77.77 |      100  |      75 |   77.77 | 11,17,54-56,74-76,98-100,118-120

Test Suites: 1 passed, 1 total
Tests:       7 passed, 7 total
Snapshots:   0 total
Time:        1.148 s
Ran all test suites.