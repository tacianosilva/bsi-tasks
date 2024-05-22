# Tarefa 01 - Teste de Unidade

👩🏻‍💻 Wanessa da Silva Bezerra  
:email: wanessaparelhas68@gmail.com  
:octocat:  [wanessabezerra](https://github.com/wanessabezerra)  

## Testes de Unidade  

Os testes de software, segundo Harrold, consistem na execução do produto de
software visando verificar a presença de erros e
aumentar a confiança de que tal produto esteja correto.  

<h1 align="center"><img src="softwaretesting/20222/tarefas/wanessabezerra/testes.gif"/></h1>  

Figure 1. Testes de Unidade  
Testes de unidade são a menor parte testável de um programa de computador. Na figura 1 podemos observar como funciona os testes de unidade  
Algumas caracterísicas destes testes:  

* Testar classes individuais;  
* Feito pelo próprio programador da classe;  
* Testa toda a interface da classe;  
* Necessidade de automação;  
* Clica um botão a qualquer momento para testar tudo;  
* Pelo menos um teste por dia (frequentemente vários testes por hora);
* Uso de um framework de testes  
* Desenvolvimento e testes de unidade feitos em paralelo
* Absolutamente necessário ter testes de unidade, principalmente se fizer refactoring de código
* Testar as classes da menos acoplada para a mais acoplada.

## Tecnologias Utilizadas

A tecnologia escolhida foi o Django, um framework de web server-side extremamente popular e repleto de características, escrito em Python.

## Framework de Teste

## Ambiente de Desenvolvimento  

O Visual Studio Code é um editor de código-fonte desenvolvido pela Microsoft. Funciona em diversos sistemas operacionais, como o Windows e Linux. Possui diversas funções interessantes para os desenvolvedores como realce de sintaxe, complementação inteligente do código, snippets, git incorporado e refatoração de código. Além disso, o VS Code ainda conta com suporte à plugins criados pela comunidade, fazendo com que se torne ainda mais completo.  

Uma das principais características do Visual Studio Code é o seu grande suporte à depuração. O depurador embutido do VS Code ajuda a acelerar seu loop de edição, compilação e depuração.  

### Extensões do depurador

O VS Code tem suporte de depuração integrado para o runtime do Node.js e pode depurar JavaScript, TypeScript ou qualquer outra linguagem traduzida para JavaScript.  

Para depurar linguagens e tempos de execução adicionais (incluindo PHP, Ruby, Go, C#, Python, C++, PowerShell etc.), procure a extensão Debuggers no VS Code Marketplace ou selecione Instalar Depuradores Adicionais no menu de tempo de execução de nível superior.  

## Tutorial

[Django](https://medium.com/djangotube/django-rest-api-curd-example-61c3a29b22ed)  

[Testes automatizados](https://www.youtube.com/watch?v=B-zcHhcTtH4)

[Link do Repositório](https://github.com/wanessabezerra/Django-Tests)
## Mocks Objects em Testes de Unidade

As ideias e conceitos por trás dos Mock Objects surgiram através de muita experimentação, discussão e colaboração entre diversos desenvolvedores que tinham uma ideia e a evoluíram para algo mais profundo resultando em algo extremamente útil para os desenvolvedores de software.  

Mocks Objects são bastante difundidos na comunidade e na literatura de métodos ágeis Extremme Programming (XP), visto que, utilizando o XP se faz uso constante de testes através da técnica Test-Driven Development (TDD) que prega teste antes da implementação.

Ainda assim, os Mock Objects possuem pouca literatura de forma geral e muitas vezes são confundidos com outras coisas como stubs que são objetos que auxiliam testes de ambientes.
Nos testes unitários podemos simular o comportamento de objetos reais complexos, principalmente quando estes objetos são difíceis de serem incorporados nos testes de unidade.  

Os Mock Objects também são muito utilizados quando temos objetos que geram resultados variáveis (por exemplo: tempo), objetos com estados difíceis de serem criados ou reproduzidos, objetos lentos como banco de dados que precisam ser inicializados antes do teste, objetos que ainda não existem ou podem ter comportamentos alterados, objetos que necessitem de informações e métodos adicionais exclusivos para os testes, entre outros.

## Referências  

[Testes de Unidade](http://www.dsc.ufcg.edu.br/~jacques/cursos/apoo/html/impl/impl3.htm)  
[Debugging](https://code.visualstudio.com/docs/editor/debugging)
