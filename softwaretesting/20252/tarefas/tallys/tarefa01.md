# Tarefa 01 - Teste de Unidade
### Nome: Tallys Aureliano Dantas dos Santos
### github: tallysdev
### email: tallys.santos.017@ufrn.edu.br

[Repositório do Projeto](https://github.com/tallysdev/software-testing.git)

## Testes de Software e Ambiente de Desenvolvimento

### Testes de Unidade
Os **Testes de Unidade** são uma prática fundamental em Engenharia de Software que visam validar partes específicas do código, geralmente funções ou métodos isolados. O objetivo é garantir que cada unidade de código se comporte conforme o esperado, reduzindo erros e facilitando a manutenção do sistema. Essa abordagem contribui para identificar falhas de forma rápida durante o desenvolvimento, antes da integração com outros módulos.

### Linguagem Escolhida: Node.js com TypeScript
O projeto da disciplina será desenvolvido utilizando **Node.js** em conjunto com **TypeScript**. Essa combinação proporciona um ambiente moderno e robusto, unindo a performance do Node com os recursos de tipagem estática do TypeScript, o que aumenta a confiabilidade e a produtividade no desenvolvimento.

### Framework de Testes de Unidade: Jest
Para os testes de unidade, foi escolhido o **Jest**. Ele é um dos frameworks mais populares para a linguagem JavaScript/TypeScript, desenvolvido pelo Facebook.  
Principais características:
- Configuração simples e intuitiva.  
- Suporte nativo para TypeScript (com ts-jest).  
- Permite a criação de **mocks**, **spies** e **testes assíncronos** com facilidade.  
- Relatórios de cobertura de código integrados.  

📌 Link: [Jest Documentation](https://jestjs.io/)  
📌 Link TypeScript + Jest: [ts-jest](https://kulshekhar.github.io/ts-jest/)

### IDE Utilizada: Visual Studio Code
A IDE utilizada é o **Visual Studio Code (VSCode)**, que oferece suporte extensivo para desenvolvimento em Node.js e TypeScript.  
Recursos de **Debug integrados**:
- **Breakpoints** (pontos de parada no código).  
- **Watch** (observação de variáveis em tempo real).  
- **Step Over / Step Into / Step Out** (execução passo a passo).  
- **Call Stack** (visualização da pilha de chamadas).  
- Integração com **configurações de debug personalizadas** via `launch.json`.  

Essas ferramentas permitem inspecionar a execução da aplicação em tempo real, ajudando a identificar erros de lógica e comportamento inesperado.

### Tutorial de CRUD com Testes
Um tutorial recomendado para CRUD com Node.js + TypeScript, que também inclui testes com Jest:  
📌 Link: [Building a CRUD API with Node.js, Express, TypeScript and Jest](https://www.section.io/engineering-education/node-express-typescript/)  

Resumo: O tutorial ensina a criar uma API CRUD com **Node.js, Express e TypeScript**, abordando desde a configuração inicial do projeto até a implementação de testes unitários com Jest. Mostra na prática como estruturar rotas, controllers e modelos, além de aplicar testes para garantir o bom funcionamento do sistema.

### Mock Objects em Testes de Unidade
**Mock Objects** são objetos simulados que imitam o comportamento de dependências reais em um sistema. Eles são usados em testes de unidade para isolar o código testado, evitando a necessidade de acessar bancos de dados, APIs externas ou outros módulos complexos. Com isso, os testes se tornam mais rápidos, previsíveis e fáceis de manter.  
Por exemplo, ao testar uma função que faz requisições HTTP, pode-se usar um mock que retorna respostas pré-definidas em vez de realmente acessar a rede.

---
