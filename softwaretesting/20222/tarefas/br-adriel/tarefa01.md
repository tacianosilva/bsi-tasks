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
