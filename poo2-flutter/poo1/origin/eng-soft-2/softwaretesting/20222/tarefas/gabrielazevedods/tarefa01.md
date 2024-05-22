# Tarefa 01 - Teste de Unidade

> Gabriel Azevedo dos Santos  
> [gabrielazevedods](github.com/gabrielazevedods)  
> gabrielazevedo492@gmail.com   

## **Teste de Software e Teste de Unidade**

O teste de software tenta minimizar a ocorrência de falhas nos sistemas, identificando os riscos e problemas do produto que possam ameaçar a sua qualidade antes que o produto chegue ao cliente final. Tratando de identificar prováveis falhas durante seu funcionamento, os testes tentam garantir que as necessidades e expectativas do cliente sejam atendidas, e verificar se o software está cumprindo todos os requisitos desejados.  
O teste de unidade é realizado na menor unidade testável do código, afim de verificar se está cumprindo os requisitos. O objetivo é testar cada unidade do projeto individualmente e garantir que o código esteja funcionando como deveria, identificando possíveis defeitos na lógica do método.

## **Linguagem de programação e Framework de Testes de Unidade**
A linguagem de programação escolhida foi [Python](https://www.python.org/).  
Python possui uma ferramenta nativa para teste unitário, o [Unittest](https://docs.python.org/pt-br/dev/library/unittest.html).

## **Framework de Teste escolhido**
O [Unittest](https://docs.python.org/pt-br/dev/library/unittest.html) é uma ferramenta nativa para testes da linguagem Python, por fazer parte da biblioteca padrão não é necessário instalar nenhum módulo adicional. O Unittest foi inspirado no JUnit. Suporta a automação de testes, compartilhamento de configuração e código de desligamento para testes, agregação de testes em coleções e independência dos testes do framework de relatórios. 

Para criar um teste de unidade usando o Unittest temos que criar um novo arquivo de teste preferencialmente iniciando com *test_* antes do nome da unidade que vamos testar, assim reconhece automático que trata-se de um arquivo de teste. Em seguida, importar o Unittest e criar uma classe que estende a classe base *TestCase*. O ponto de cada teste é a invocação de um método **assertEqual()** para verificar se há um resultado esperado; **assertTrue()** ou **assertFalse()** para verificar uma condição; ou **assertRaises()** para verificar se uma exceção específica será levantada. Para rodar o teste na linha de comando chamamos **python -m unittest [test_name]**.

## **IDE utilizada**
A IDE utilizada é o [Visual Studio Code](https://code.visualstudio.com/). O Visual Studio Code é um editor de código de código aberto desenvolvido pela Microsoft, disponível para Windows, Mac e Linux. Possui um depurador de código integrado que dá suporte a depuração de algumas aplicações de maneira nativa, e permite a instalação de extensões para depuração de outras linguagens. Para debug do código, o Visual Studio Code permite adicionar Breakpoints em pontos específicos do código, basta clicar na margem esquerda do editor e eles são listados na barra de debug, com a indicação do arquivo e da linha onde está localizado, além de permitir que habilitar, desabilitar ou remover os pontos de parada do código na barra de debug.

## **Testes na tecnologia escolhida**
Aqui está o [link](https://youtu.be/WKD1hU7CNfw?list=PLbIBj8vQhvm2OT4MpkrsKDDVuZ_RlNzli) de um tutorial que mostra a construção de testes de unidade em Python. O tutorial mostra como realizar teste de unidade em funções de em um gerador de senhas aleatórias, usando TDD. Cada teste de unidade verifica se as senhas geradas estão de acordo com o que a função deve retornar, como por exemplo: se uma função que deve gerar apenas números, está retornando apenas números.

## **Implementação de Teste de Unidade**
Aqui está o [link](https://github.com/gabrielazevedods/python-unit-test) do repositório com a implementação do teste de unidade na tecnologia escolhida. A experiência de implementar os testes de unidade em Python foi bem tranquila, pois como a linguagem fornece uma ferramenta super simples de se utilizar, com poucas linhas de código já foi possível realizar os testes. Seguindo o tutorial encontrado, fui capaz de entender como funciona o processo de teste de unidade na prática, o que foi muito bom para o aprendizado sobre testes de software.

## **Mocks Objects em Testes de Unidade**
Mock Objects é uma maneira de imitar unidades falsas que simulam o comportamento de unidades reais. Podem ser criados através de frameworks, quase todas as principais linguagens de programação possuem frameworks que criam esses Mocks Objects. Nos testes unitários podemos simular o comportamento de objetos reais complexos, sendo muito utilizados quando temos objetos que geram resultados variados. Usamos o Mock Object quando queremos saber se uma função vai ser chamada corretamente, quantas vezes ela vai ser chamada, e se os parâmetros esperados são os corretos. Em Python, a biblioteca de Mocks Objects é *unittest.mock*, ela fornece uma maneira fácil de introduzir Mocks nos testes. O *unittest.mock* oferece uma classe base para objetos simulados chamada Mock. Os casos de uso do Mock são praticamente ilimitados porque o Mock é muito flexível.