# Tarefa 01 - Teste de Unidade
Nome: Felipe David Pereira dos Santos
Github: felipedavid
Email: felipedavid.huh@gmail.com

## A. Testes
Testes são uma maneira de confirmar que o sistema está se comportando da forma esperada, e inconsistências nos resultados previnem alguns errors de chegarem no sistema em produção. Testes de unidade se resumem a manter a qualidade de uma unidade atômica do sistema, geralmente sendo procedimentos.

## B. Linguagem e Framwork de testes
A linguagem de testes será Go e o framework de testes que já vem com o ambiente da linguagem.

## C. Testes
A linguagem já vem com sistema para testes. Para criar um teste unitário para um procedimento chamado "fazerCoisa" do arquivo x.go, basta criar um arquivo x_test.go, e dentro do arquivo de testes criar um procedimento com a assinatura TestfazerCoisa(t \*testing.T). E para rodar os testes, basta digitar "go test".

## D. IDE
Eu não utilizo ambientes de desenvolvimento integrado más sim uma ferramenta pra cada tipo de tarefa. Vim para edição de código e [Delve](https://github.com/go-delve/delve)/[GDB](https://github.com/bminor/binutils-gdb) com algum fron tend completinho como [Gdlv](https://github.com/aarzilli/gdlv)/[gf2](https://github.com/nakst/gf) para debugging (muito melhor que a itegração de baixa qualidade feita por TODAS as IDEs que suportam Go que e oferecem suporte para debugging).

## E. Tutorial
[Add a test](https://go.dev/doc/tutorial/add-a-test)

## F. [CRUD e testes](https://github.com/felipedavid/go_crud)
A experiência foi O.K. :)

## G. Mocks Objects
Mocks objects são objetos que contém dados semelhantes aqueles que serão processados por nossa aplicação em produção, e o seu único intuito é serem processados pelos testes para garantir que as funções de CRUD se comportem de maneira esperada quando forem receber os dados reais em produção.
