## Tarefa 01 - Teste de Unidade
### Joan de Azevedo Medeiros
### @joanmdrs
### joan.medeiros.130@ufrn.edu.br

## Teste de Software - Testes de Unidade 

Teste de Software é um processo que faz parte do #desenvolvimento de software, e tem como principal objetivo revelar falhas/bugs para que sejam corrigidas até que o produto final atinja a qualidade desejada / acordada.


Profissionais que trabalham com testes (denominados analistas de testes, técnicos de testes, homologador, ou simplesmente testes) estão habituados a realizar uma bateria de testes de diferentes naturezas e propósitos, envolvendo não apenas os testes funcionais da aplicação, mas diversas outras atividades como:

- avaliação da especificação de requisitos,
- avaliação de projeto técnico,
- verificações em outros documentos,
- testes de performance e capacidade,
- avaliação de interface,

Existem vários tipos de teste, e um deles é o teste de unidade que se trata de testar funções simples e de resultado constante. A Unidade é a menor parte testável de um sistema. Como exemplo uma função de soma entre dois números, o resultado da soma de 1 e 2 deve sempre ser 3. Esse teste é muito importante para assegurar que a “base” do sistema, que será utilizado nas requisições, está em perfeito funcionamento.

## Linguagem escolhida - TypeScript

TypeScript é uma linguagem de programação fortemente tipada que se baseia em JavaScript, oferecendo melhores ferramentas em qualquer escala. O TypeScript adiciona sintaxe adicional ao JavaScript para oferecer suporte a uma integração mais estreita com seu editor. O código TypeScript é convertido em JavaScript, que é executado em qualquer lugar que o JavaScript;

## Framework de teste escolhido - Jest

Jest é um framework de teste unitário de código aberto em JavaScript criado pelo Facebook a partir do framework Jasmine. Jest é uma das ferramentas de teste unitário mais difundidas dentro da comunidade de JavaScript. Funciona com projetos usando: Babel, TypeScript, Node, React, Angular, Vue entre outros.

* [Site oficial](https://jestjs.io/pt-BR/)
* [Introdução ao Jest](https://jestjs.io/pt-BR/docs/getting-started)
* [Configurando o Jest](https://jestjs.io/docs/configuration)

## IDE utilizada - Visual Studio Code

A IDE utilizada para o desenvolvimento do projeto será o Visual Studio Code, muito usada em todo o mundo e com bastantes extensões. Dentro do VSCode, existe uma guia para testes na qual é possível depurar o código, adicionar breakpoints e verificar se as funções estão corretas.

Além disso, o VSCode possui integração com o GitHub, ou seja, é possível fazer commits, dar push, pull, merge, criar pull requests de dentro do software. É uma plataforma que oferece diversas vantagens e acelera o processo de desenvolvimento.

Com relação a ferramentas de Debug, o VsCode possui diversas ferramentas que auxiliam este processo, como por exemplo, o DataTip que permite adicionar breakpoints nas linhas de código. Também há o QuickWatch dialog que permite inspecionar os detalhes das variaveis, facilitando a navegação, permitindo a alteração de variáveis entre outros.

Além dessas duas ferramentas, também existe o Locals Window que exibe automaticamente uma lista de variáveis e seus valores, que estejam dentro do escopo de um método. Ao parar em um breakpoint a janela Locals vai exibir o nome da variável juntamente com seu valor entre outras funcionalidades. 

Estas são apenas algumas das ferramentas de debug do Visual Studio Code, pois existem muitas outras que trazem outros tipos de funcionalidades.

## Tutorial

O link abaixo mostra a criação de uma API REST em TypeScript com NodeJs, Postgres e TypeORM. No entanto, para a criação do CRUD eu não segui os passos descritos nos vídeos da playlist, eu criei minha aplicação por conta própria a partir dos meus conhecimentos e da consulta a documentação das tecnologias utilizadas. 

Eu desenvolvi uma aplicação Express em TypeScript com NodeJS, MongoDB utilizando Docker e Mongoose que se trata de uma biblioteca de Modelagem de Dados de Objeto (ODM) para MongoDB e NodeJS. Para a criação dos testes, utilizei o Jest como framework de testes de unidade em conjunto com a biblioteca Supertest que permite criar simulações de requisições HTTP. 

Dessa forma, eu segui os passos do último vídeo da playlist abaixo para fazer a configuração do Jest e criação dos testes de unidade. 

* [Building a REST API, TypeScript, TypeORM & Postgres](https://youtube.com/playlist?list=PLdk2EmelRVLpIdCFolrwdLhCTHyeefU6W)

## Implementação

Implementar os testes foi uma boa experiência, a criação do CRUD envolveu alguns conhecimentos que eu ainda não possuía e portanto encarei isso como um desafio e coloquei à prova minhas habilidades de programador. Esta experiência me proporcionou adquirir novos conhecimentos e subir mais um degrau na minha jornada enquanto programador. Além disso, pude passar por várias etapas do desenvolvimento de software, indo desde a concepção do projeto até a implementação de testes. 

* [Repositório](https://github.com/joanmdrs/crud-unid-test)

## Mock objects

Um mock object é um objeto falso no sistema que decide se o teste de unidade passou ou falhou. Ele faz isso verificando se o objeto em teste chamou o objeto falso conforme o esperado. Geralmente não há mais de uma simulação por teste.O uso de Mock Objects para testes de unidade melhora tanto código de domínio quanto suítes de teste. Eles permitem que testes de unidade sejam escritos para tudo, simplificam o teste estrutural e evita poluir o código de domínio com infraestrutura de teste.