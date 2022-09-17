# Tarefa 01 - Teste de Unidade :test_tube:

:man_technologist: Adriel Faria dos Santos

:octocat: [br-adriel](https://github.com/br-adriel)

:envelope: adriel.fsantos@outlook.com

## Testes de software

Os testes representam a etapa de asseguração da qualidade de um software,
são eles que irão verificar se o que foi construído está se comportando como
deveria, se os objetos, métodos e funções são resistentes a inputs inesperados
do usuário e se a lógica de negócio está sendo atendida, ou seja, os testes
são os responsáveis por garantir a segurança e a integridade do software.

Com a evolução dos processos de produção de software e a adoção dos modelos
ágeis de desenvolvimento, a testagem dos sistemas deixou de ser uma fase
engessada, na qual os testes eram executados apenas após o fim do
desenvolvimento do software, e se tornou um processo contínuo e recorrente
ao longo de todo o ciclo de construção do software, algumas vezes sendo
adotada até como um pré-requisito para o início de desenvolvimento de
novas funções, como é o caso da abordagem Test Driven Development (TDD).

Essa maior valorização dos testes acabou trazendo também um maior enfoque
a modalidade de testes automatizados pelo fato de serem mais baratos e
rápidos de executar quando comparados a testes manuais.

Assim como cada software tem um propósito específico, os testes também
possuem características próprias que nos permite classificá-los em diferentes
tipos. Uma dessas classificações é a pirâmide de testes, que os dividem em
três classificações: testes de sistema, testes de integração e testes de unidade.

Testes de sistema são aqueles que tentam simular da forma mais fiel possível
o uso de um usuário final, o que torna esse tipo de teste o mais caro e demorado
entre os três.

Testes de integração são os responsáveis por verificar a execução de uma
funcionalidade do sistema, geralmente eles envolvem algum componente externo
como banco de dados. Esse tipo de teste não é tão custoso e demorado como os
de sistema, mas ainda assim demandam um esforço considerável.

Testes de Unidade são os responsáveis por verificar partes pequenas e isoladas
do código total, normalmente se resumindo ao teste de métodos de uma classe. Eles
são os mais baratos de se construir e rápidos de executar.

É devido a isso que essa mesma classificação sugere que os testes de unidade
atuem como base da "pirâmide" dos testes, sendo assim os mais ambundantes no
desenvolvimento de software, seguido dos testes de integração, que deveriam
ser implementados em menor quantidade formando o meio da pirâmide, e dos
testes de sistemas, que deveriam ser os menos numerosos, representando o topo
da pirâmide.

### Teste de Unidade

De forma prática, um teste de unidade nada mais é do quê um pequeno programa
que vai testar um pedaço do código "real", chamando seus métodos e funções
e verificando se a saída obtida, ou a execução observada, corresponde ao esperado
para sua execução.

O que determina o número de testes de unidade que um pedaço de software terá
é o seu grau de importância na lógica do projeto e a sua propensão a provocar
resultados diferentes a cada execução, de forma que uma método simples, como o
getNome de uma classe Pessoa não receba nenhum teste de unidade, enquanto um
método de validarCPF receba múltiplos, para que a testagem sob diferentes
contextos seja possível.

## Liguagem de programação escolhida

Para a realização dessa atividade foi escolhido o uso do framework Django,
que é escrito em Python, e possuí uma suíte de testes própria, que é baseada
na biblioteca unittest.

## O framework de testes do Django

O Django traz consigo um framework de testes muito parecido com a biblioteca
padrão de testagem do python, a unittest, que apesar de ter um nome que remete
apenas à testes de unidade, também funciona muito bem para testes de integração.

A principal diferença entre a biblioteca padrão do python e a oferecida pelo Django
é que a segunda adiciona ferramentas a primeira que nos permite testar aspectos
próprios do framework de desenvolvimento, como a simulação de requisições.

Por padrão, para o framework entender que um arquivo é uma suíte de testes, ele
deverá ser nomeado começando com `test`, dessa forma, ao executar o comando de
testagem, todos os arquivos que seguem esse padrão serão encontrados e executados
automaticamente.

#### Para mais informações...

[MDN web docs](https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django/Testing)

[Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-add-unit-testing-to-your-django-project-pt)

[Documentação do Django](https://docs.djangoproject.com/en/4.1/topics/testing/overview/)

## Visual Studio Code

O Visual Studio Code, ou VSCode, é um editor de código que oferece suporte a
integração com repositórios git, realce de sintax para várias linguagens de
programação, e uma variedade de plugins instaláveis que englobam desde a customização
com temas personalizados e pacotes de ícones, até uma maior integração com
as linguagens.

Com a instalação de plugins de suporte a Python o VSCode viabiliza a depuração
de diferentes tipos de aplicações python, entre elas as aplicações Django,
permitindo visualizar variáveis, executar linha a linha, e definir pontos de
parada conforme desejado pelo usuário.

## Tutoriais de CRUD e Testes em Django

Os tutoriais a seguir mostram uma visão geral de como funciona uma apliacação
Django, seua estrutura de arquivo, e dão o passo a passo de como implementar as
funcionalidades de criação, adição, leitura e exclusão de dados salvos em uma
base de dados.

Além disso, os tutoriais também explicam a implementação dos testes,
e as particularidades para o seu funcionamento correto, como a criação de um arquivo
\_\_init\_\_.py e a nomeclatura dos métodos de teste.

### Tutoriais de desenvolvimento de CRUD Django

[Build a Django CRUD App by Using Class-Based Views :page_facing_up: :us:](https://towardsdatascience.com/build-a-django-crud-app-by-using-class-based-views-12bc69d36ab6)

[Django 4 CRUD completo em \~30minutos\~ :clapper: :brazil:](https://www.youtube.com/watch?v=GGBzMpIAgz4)

[Django CRUD (Create, Retrieve, Update, Delete) Function Based Views :page_facing_up: :us:](https://www.geeksforgeeks.org/django-crud-create-retrieve-update-delete-function-based-views/)

### Tutoriais sobre Testes de Software em Django

[Como adicionar o teste de unidade ao seu projeto Django :page_facing_up: :brazil:](https://www.digitalocean.com/community/tutorials/how-to-add-unit-testing-to-your-django-project-pt)

[Introdução a testes unitários com Python e Django :clapper: :brazil:](https://www.youtube.com/watch?v=cEXt8hDyKQw)

[Tutorial Django Parte 10: Testando uma aplicação web Django :page_facing_up: :brazil:](https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django/Testing)

[Writing your first Django app, part 5 :page_facing_up: :us:](https://docs.djangoproject.com/en/4.1/intro/tutorial05/)

## Minha experiência implementando um CRUD e os testes

Para praticar o desenvolvimento de testes de unidade eu criei uma aplicação
Django com apenas um model de Tarefa e seu CRUD.

Buscando maior praticidade e velocidade no desenvolvimento, eu optei por
utilizar as Class Based Views que o Django disponibiliza, entretanto o precesso
acabou não sendo tão rápido devido a documentação escassa que essas views
tem, tendo inclusive uma abrodagem bastante superficial na documentação
oficial do Django.

A implementação dos testes me deixou bastante perdido a príncipio,
porém após alguns testes implementados o processo se tornou natural.

Entretanto é relevante ressaltar que a interface de execução de testes
oferecida pelo VS Code não se integrou bem com os testes Django: apesar
de serem listados na interface e poderem ser executados, sua execução
aponta para testes reprovados mesmo com eles passando sem problemas
no terminal ao executar `python manage.py test`.

De acordo com minha pesquisa acerca desse problema, a causa seria que
o VS Code se integra apenas com unittest e pytest, apesar os testes do
Django serem baseados na biblioteca unittest, as funções adicionais
agregadas a essa biblioteca de base faz com que esse comportamento
estranho no VS Code ocorra.

[Link para o repositorio com o CRUD desenvolvido](https://github.com/br-adriel/django-atarefado)

## Mock objects

Enquanto os testes unitários, focam em apenas uma pequena parte
isolada do código geral, os softwares em que eles estão inseridos
interagem e necessitam de muitos outros recursos para seu pleno
funcionamento, como banco de dados, uma api, ou uma unidade de
código diferente daquela em que o teste atua.

Por causa dessa dependência de outras partes, alguns testes de
unidades precisam implementar de alguma forma esse aspecto para
que a testagem opere sobre os métodos conforme eles foram pensados.

Porém, se fossem utilizados recursos reais, como a realização de
consultas a uma api externa durante o teste, o aspecto unitário
do teste, seu isolamento, seria perdido, o tornando um teste de
integração.

Para contornar essa problemática há adocão de Mock objects, que
são uma espécie de imitação de um recurso real, utilizado apenas
para a finalidade de testes.

Por exemplo, para testar um método que tem como entrada uma
chamada na api, ao invés de se realizar a chamada de fato, o que
necessitaria o uso de recursos externos, é feita criação de
objetos que simulam o dado que aquele método precisa para ser
executado, ou seja, é criado uma imitação do objeto que viria
daquela api em questão.
