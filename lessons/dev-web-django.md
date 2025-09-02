# Treinamento Back-end Django

## Aula 01 - Preparação do Ambiente de Desenvolvimento

* Escolha do Sistema Operacional
* Windows
  * PowerShell
  * WSL2
  * Git bash
* Linux
  * Bash
  * Zsh
* Ambientes Virtuais
  * python-venv
  * asdf

### Links

* Vídeo Aula 01: https://drive.google.com/file/d/1wbyKQiK88UOoUHxJOAWJC6tEDfOlj5vI/view?usp=sharing
* Slides: https://docs.google.com/presentation/d/18VEhbn06Miho0XSAjUD27pZ2Xe3RMOjm9lWfGo9NjjM/edit?usp=sharing
* [35 Comandos Linux](https://www.hostinger.com.br/tutoriais/comandos-linux)
* [Comandos PowerShell](https://www.devmedia.com.br/solucoes-com-o-windows-powershell-revista-infra-magazine-6/24818)


## Aula 02 - Docker

* Docker
  * Docker é um conjunto de produtos de plataforma como serviço que usam virtualização de nível de sistema operacional para entregar software em pacotes chamados container
  * Os container são isolados uns dos outros e agrupam seus próprios softwares, bibliotecas e arquivos de configuração
  * O Docker Hub é o maior repositório de imagens de container com uma variedade de fontes de conteúdo

Para instalar o Docker isse esse tutorial [How To Install and Use Docker on Ubuntu 22.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-22-04). A versão anterior deste tutorial está em português [Como Instalar e Utilizar o Docker no Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-pt).

No nosso caso, usaremos docker para executar algum SGBD utilizado nos nossos projetos. 

* [Executando SGBDs utilizando Containers Docker](https://github.com/tacianosilva/bsi-tasks/blob/master/database/docker/README.md)

Além disso, iremos publicar, no caso fazer deploy, de nosso projeto usando docker (veremos isso depois). 

### Links

* Vídeo Aula 02: [O mínimo que você precisa saber sobre Docker!](https://www.youtube.com/watch?v=ntbpIfS44Gw)
* Slides: https://docs.google.com/presentation/d/18VEhbn06Miho0XSAjUD27pZ2Xe3RMOjm9lWfGo9NjjM/edit?usp=sharing
* Comandos básicos de docker: [Docker: Imagens, Containers, e seus principais comandos](https://dev.to/soutoigor/docker-imagens-containers-e-seus-principais-comandos-23p6)
* Vídeo GRANDE e bem completo do Jefferson/LiuxTips: [TUDO O QUE VOCÊ PRECISA SABER SOBRE DOCKER EM 2022](https://www.youtube.com/watch?v=MeFyp4VnNx0)
* Livro [Descomplicando o Docker](https://livro.descomplicandodocker.com.br/)

## Aula 03 - IDE

Uma IDE (do inglês integrated development environment ou ambiente de desenvolvimento integrado), é um programa de computador que reúne características e ferramentas de apoio ao desenvolvimento de software com o objetivo de agilizar este processo. Wikipédia é um programa de computador que reúne características e ferramentas de apoio ao desenvolvimento de software com o objetivo de agilizar este processo. [Wikipédia](https://pt.wikipedia.org/wiki/Ambiente_de_desenvolvimento_integrado).

Algumas IDEs muito conhecidas e utizadas: VSCode, Eclipse IDE, Intellij IDEA (Jet Brains), VIM.

### Dicas

* Escolha a melhor IDE para sua linguagem;
* A boa configuração da sua IDE é mais importante do que a IDE;
* Aprenda a usar as Ferramentas de Depuração da sua IDE;
* **Não traduza sua IDE!!! Deixe ela em Inglês!**

### Links

* Vídeo Aula 03: [Escolha bem sua IDE!](https://drive.google.com/file/d/1f020dmcWCfonD3BZlEVuRcOa2x2iNLGb/view?usp=sharing)
* [VSCode Linux: Como Instalar Da Forma Correta (Passo a Passo)](https://www.youtube.com/watch?v=5_6p8LmC8dQ)
* [COMO BAIXAR E CONFIGURAR O VISUAL STUDIO CODE PARA INICIANTES](https://www.youtube.com/watch?v=uxln1hT_Ev4)
* [5 TRUQUES DO VS CODE PRA VOCÊ USAR AINDA HOJE!](https://www.youtube.com/watch?v=qJ_M4W0u5rI)
* [5 EXTENSÕES para o VSCODE que irão AUMENTAR sua PRODUTIVIDADE](https://www.youtube.com/watch?v=HIxRDyFfnuc)
* [Emmet Cheat Sheet (comandos do emmet)](https://docs.emmet.io/cheat-sheet/)
* [Como Configurar VSCode Para Python em 2023[RÁPIDO]](https://www.youtube.com/watch?v=7Kpd6eprz4k)
* [Ambientes Back-End com Docker + VS Code // Mão no Código #3](https://www.youtube.com/watch?v=97jWpWp4Pnc)
* [Como usar o editor Vim, aprenda vim em 10 minutos!](https://www.youtube.com/watch?v=EscyTZSaHXA)

## Aula 04 - Git, GitHub e GitFlow

O [controle de versão](https://www.atlassian.com/br/git/tutorials/what-is-version-control), também conhecido como controle de fonte, é a prática de rastrear e gerenciar as alterações em um código de software. Os sistemas de controle de versão são ferramentas de software que ajudam as equipes de software a gerenciar as alterações ao código-fonte ao longo do tempo.

De longe, [o sistema de controle de versão moderno mais usado no mundo hoje é o Git](https://www.atlassian.com/br/git/tutorials/what-is-git). O Git é um projeto de código aberto maduro e com manutenção ativa desenvolvido em 2005 por Linus Torvalds, o famoso criador do kernel do sistema operacional Linux.

### Links

* Vídeo Aula 04: [Fluxo de Desenvolvimento com Git e GitHub](https://drive.google.com/file/d/11Ee4ZnA16i3CnFR5n7Wq5w4SImTve7eR/view?usp=sharing)
* [What is Git](https://www.atlassian.com/br/git/tutorials/what-is-git)
* [APRENDA GIT EM 30 MINUTOS - OS PRINCIPAIS COMANDOS DE GIT](https://www.youtube.com/watch?v=Zwv9qRyVeU4)
* [Descomplicando Branches no Git usando VS Code // Mão no Código #6](https://www.youtube.com/watch?v=oXMgyQt0ce0)
* [O QUE É GIT E GITHUB? - definição e conceitos importantes 1/2](https://www.youtube.com/watch?v=DqTITcMq68k&t=815s)
* [COMO USAR GIT E GITHUB NA PRÁTICA! - desde o primeiro commit até o pull request! 2/2](https://www.youtube.com/watch?v=UBAX-13g8OM&t=509s)
* [Comandos Git](https://github.com/tacianosilva/eng-software-2/blob/master/docs/github.md)
* [GitFlow](https://github.com/tacianosilva/eng-software-2/blob/master/docs/doc-gitflow.md)
* [12. Revertendo commit com git revert - Git e Github na Vida Real](https://www.youtube.com/watch?v=OH3_IJBfNlY)
* [13. Revertendo commit com reset - Git e Github na Vida Real](https://www.youtube.com/watch?v=ilZ_1WOgGBs)
* [Usando git/github direto pelo vscode](https://www.youtube.com/watch?v=qxxw9Xy4f84)

## Aula 05 - Tutorial Django Framework

Aula sobre o Framework Django onde apresentamos informações sobre sua organização e fizemos uma prática para construir um projeto e um app.

### Tutoriais

* [Tutorial Oficial Django](https://docs.djangoproject.com/pt-br/4.1/intro/tutorial01/)
* [Tutorial Django: Website da Biblioteca Local](https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django/Tutorial_local_library_website)

### Links

* Vídeo Aula 05: [Django Framework](https://drive.google.com/file/d/1rqq8dbzL6TT8HLcXuxXyYOR6txVDSEMx/view?usp=share_link)
* Slides: https://docs.google.com/presentation/d/1Mw4CnEgWRxcoPZTNmdstmyo9JE6EzbvBWD0p5tanJSU/edit?usp=sharing

## Aula 06 - Tutorial Django Rest Framework

Aula sobre o Django Rest Framework para o desenvolvimento de API Rest. Antes de assistir os vídeos leia a documentação oficial e faça o [tutorial oficial do DRF](https://docs.djangoproject.com/pt-br/4.1/intro/tutorial01/).

### Tutoriais

* [Tutorial Oficial DRF - Quickstart](https://docs.djangoproject.com/pt-br/4.1/intro/tutorial01/)
* [Turorial DRF by Marco André Mendes](https://github.com/marrcandre/django-drf-tutorial)

### Links

Na playlist pode assistir a partir do vídeo 8, os vídeos iniciais são de configuração.

* Playlist de Vídeo sobre DRF [Django DRF eCommerce Project](https://www.youtube.com/playlist?list=PLOLrQ9Pn6cawinBJbH5d9IfloO9RRPMiq)
