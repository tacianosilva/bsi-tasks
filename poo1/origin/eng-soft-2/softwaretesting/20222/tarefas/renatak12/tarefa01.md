# Tarefa 01 - Teste de Unidade

## Informações Pessoais

* Renata Karla Araújo dos Santos
* @renatak12
* renata.araujo.094@ufrn.edu.br

## Teste de Software - Testes de Unidade

Testes de software é um conjunto de processos com os quais se pretende validar um sistema ou aplicação, em momentos diferentes, para verificar seu correto funcionamento. Este tipo de teste cobre qualquer etapa do desenvolvimento do sistema, desde sua criação até a implantação. São uma série de procedimentos que visam encontrar possíveis bugs, reportar erros, identificar problemas de usabilidade, bem como assegurar que todos os requisitos solicitados pelo cliente sejam atendidos.

Existem vários tipos de teste, e um dos principais e mais comum é o teste de unidade que é utilizado para validar se um pedaço do código está funcionando corretamente. Uma unidade é a menor parte testável em um sistema.

## Linguagem de programação escolhida

- Go

Go é uma linguagem de programação criada pela Google e lançada em código livre em novembro de 2009. É uma linguagem compilada e focada em produtividade e programação concorrente, baseada em trabalhos feitos no sistema operacional chamado Inferno.

## Framework de testes de unidade 

- Gin Web Framework

Gin is a HTTP web framework written in Go (Golang). It features a Martini-like API with much better performance -- up to 40 times faster. If you need smashing performance, get yourself some Gin.

* https://github.com/gin-gonic/gin
* https://gin-gonic.com/
* [Playlist tutorial](https://www.youtube.com/watch?v=qR0WnWL2o1Q&list=PL3eAkoh7fypr8zrkiygiY1e9osoqjoV9w)

#
- Insomnia

Insomnia é um framework Open Source para desenvolvimento/teste de API Clients. Ele pode ser usado para envio de requisições REST, SOAP, GraphQ e GRPC. Com esta ferramenta torna-se possível realizar a documentação, automação e com a sua versão CLI tools é possível implementar testes em pipeline.

* https://insomnia.rest/download
* [Insomnia REST Client Tutorial](https://www.youtube.com/watch?v=H16GUC9Svyk)

## IDE - Visual Studio Code

Trata-se de uma ferramenta leve e multiplataforma que esta disponível para Windows, Mac OS e Linux, sendo executado nativamente em cada plataforma. O VSCode atende uma quantidade enorme de projetos (ASP .NET, Node.js) e oferece suporte a mais de 30 linguagens de programação como JavaScript, C#, C++, PHP, Java, HTML, R, CSS, SQL, Markdown, TypeScript, JSON, XML e Python assim como muitos outros formatos de arquivos comuns. 

Ele é gratuito e open source, com seu código disponibilizado no GitHub, e isso permite que você contribua com seu desenvolvimento, alem de ser integrado com o mesmo, possibilitando fazer commits, dar push, pull, merge, criar pull requests, ets. 

Você pode baixar a versão correspondente do VSCode para a sua plataforma neste link : [download](https://code.visualstudio.com/download).

Algumas das ferramentas de debug do Visual Studio Code:

* DataTip: É de longe o mais utilizado, pela natureza da sua facilidade. Basta parar em um breakpoint, passar o mouse sobre alguma variável e ele estará lá para ajudar o programador.
* QuickWatch: Uma janela é aberta com todos os detalhes das variaveis, facilitando a navegação.
* Parallel Watch Window: O objetivo é auxiliar o debug de processos que estão em paralelo. Ela identifica e monitora uma variável através de várias Threads.
* Locals Window: Exibe automaticamente uma lista de variáveis e seus valores, que estejam dentro do escopo do método. Ao parar em um breakpoint a janela Locals vai exibir o nome da variável juntamente com seu valor.

Entre muitas outras.

## Tutorial CRUD

Iniciando banco de dados com Docker e Postgres [CRUD] - Backend com Golang, Postgres e Docker.

* [CRUD Videos](https://www.youtube.com/watch?v=EYgnlMWhrnM&list=PLcE-9cucnhqW7g8Uw6j1-QAgSbPpeZ6p8&index=1)

## Repositório e implementação

OBS: Tentando algo diferente. Não deu muito certo!

* [Repositório](https://github.com/renatak12/go-products)
* [testes](https://github.com/renatak12/go-products/tree/main/bd/sqlc)

## Mocks Objects

O termo "Mock Objects" é utilizado para descrever um caso especial de objetos que imitam objetos reais para teste. Esses Mock Objects atualmente podem ser criados através de frameworks que facilitam bastante a sua criação. Praticamente todas as principais linguagens possuem frameworks disponíveis para a criação de Mock Objects. Os Mock Objects são mais uma forma de objeto de teste.

Existem diversas razões para utilizarmos Mock Objects em nossos sistemas. Nos testes unitários podemos simular o comportamento de objetos reais complexos, principalmente quando estes objetos são difíceis de serem incorporados nos testes de unidade. Um exemplo disso é uma chamada remota que pode ser simulada com Mock Objects.
