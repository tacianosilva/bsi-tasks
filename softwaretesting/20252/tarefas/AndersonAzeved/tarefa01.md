# Tarefa 01 - Teste de Unidade
* Anderson Azevedo da Silva
* [GitHub](https://github.com/AndersonAzeved/)
* [Email](andersonsilva14.2017@gmail.com)
* [Projeto - Visse](https://github.com/AndersonAzeved/Visse)
#

a) Pesquise e fale um pouco sobre Testes de Software com foco em Testes de Unidade. Coloque um pequeno resumo.
* Testes de unidade são uma abordagem de teste de software que verifica o funcionamento correto de pequenas partes do código, como funções ou métodos, de forma isolada. Eles ajudam a identificar erros precocemente, facilitam a manutenção, aumentam a confiabilidade do sistema e incentivam boas práticas de programação, sendo suportados por ferramentas como JUnit, pytest, NUnit e Jest.

b) Defina uma linguagem de programação, uma stack para desenvolver o projeto da disciplina.
* Linguagem de programação: JavaScript / TypeScript (Next.js)

* Stack Tecnológica

| Camada               | Tecnologia                                                                 |
|----------------------|---------------------------------------------------------------------------|
| **Frontend**         | Next.js + React (componentes, páginas, rotas, estado local)               |
| **Estilização**      | Tailwind CSS                           |
| **Banco de Dados**   | SQLite ou JSON local para protótipo rápido (pode evoluir para PostgreSQL) |
| **Autenticação**     | NextAuth.js                     |
| **Testes de Unidade**| Jest + React Testing Library (testes de componentes e funções)           |


c) Busque um framework de Testes de Unidade para a linguagem escolhida  e fale um pouco sobre um framework escolhido. Coloque um pequeno resumo sobre o framework de testes e links para ele.

**Jest** é um framework de testes para **JavaScript/TypeScript**, muito usado em projetos **React** e **Next.js**. Ele permite testar funções, componentes e lógica da aplicação de forma simples e eficiente.

Principais características:
- Fácil de configurar e usar.
- Suporte a testes assíncronos.
- Geração de relatórios de cobertura de código.
- Permite criar mocks de funções e módulos.
- Integração perfeita com **React Testing Library**.

Links
- [Site oficial do Jest](https://jestjs.io/)
- [Guia Jest + Next.js](https://nextjs.org/docs/app/guides/testing/jest)


d) Fale um pouco da IDE que você utiliza. Fale sobre as ferramentas de debug que ela tem integrada.
* IDE: Visual Studio Code (VS Code): é uma IDE leve, gratuita e altamente customizável, muito utilizada no desenvolvimento de aplicações **JavaScript**, **TypeScript** e **Next.js**. Ela oferece suporte a extensões, integração com Git e diversas linguagens de programação.

**Ferramentas de Debug Integradas**
- **Depuração passo a passo**: permite executar o código linha a linha para identificar erros.
- **Breakpoints**: possibilita pausar a execução em pontos específicos do código.
- **Watch**: monitora variáveis ou expressões durante a execução do programa.
- **Console de depuração**: exibe logs, valores de variáveis e mensagens de erro.
- **Integração com Node.js e browsers**: facilita o debug de aplicações server-side e client-side.
- **Extensões adicionais**: como Debugger for Chrome e React Developer Tools, que aumentam a capacidade de depuração.


e) Busque pelo menos um Tutorial para fazer um CRUD na tecnologia escolhida e que mostre a construção de Testes de Software. Apresente o link e descreva em poucas palavras o conteúdo do tutorial.

**Tutorial CRUD com Next.js e Testes de Software**

* **Link:** [Step-by-Step: How to Unit Test your Next.js App with Jest and TypeScript](https://medium.com/@maishaChow/step-by-step-how-to-unit-test-your-next-js-app-with-jest-and-typescript-24c610ef06a0)

* **Resumo:**
Este tutorial ensina a criar uma aplicação **Next.js com TypeScript** com um **CRUD básico**. Além disso, mostra como configurar o **Jest** e a **React Testing Library** para escrever **testes de unidade**, incluindo a instalação de dependências, configuração do ambiente e testes de componentes e funções.


f) Pesquise sobre Mocks Objects em Testes de Unidade e faça um pequeno resumo.
* Mocks são objetos simulados que imitam o comportamento de objetos reais de forma controlada, permitindo testar unidades de código de maneira isolada. Eles são especialmente úteis quando dependemos de componentes externos, como APIs, bancos de dados ou serviços de terceiros, que podem ser difíceis de configurar ou lentos para uso em testes.
