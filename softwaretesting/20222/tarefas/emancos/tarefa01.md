# Tarefa 01 - Teste de Unidade
* Emanuel Costa
* [https://github.com/emancos](https://github.com/emancos)
* [emancos@gmail.com](emancos@gmail.com)

## Testes de Unidade.

O teste unitário consiste em verificar o comportamento das menores unidades em sua aplicação.<br>
Tecnicamente, isso seria uma classe ou até mesmo um método de classe em línguas orientadas a<br>
objetos, e seria um procedimento ou função em línguas processuais e funcionais.<br>
Os testes unitários precisam funcionar isoladamente porque precisam funcionar rapidamente.<br>
Todo o conjunto de testes unitários de uma aplicação precisa funcionar em minutos, de<br>
preferência em segundos. É por isso que os testes unitários não podem utilizar nenhum <br>
processo ou sistema externo.<br>
Nenhuma operação de E/S (input/output) de qualquer tipo (banco de dados, arquivo, console, rede)<br>
exceto o registro de falhas nos testes e talvez a leitura da configuração padrão de alternância<br>
de recursos no início de uma execução de teste.

## Linguagem de programação, Framework e Testes.
* Linguagem: JAVA.
* Spring Framework.
* JUnit.

### JUnit
JUnit é um framework que facilita o desenvolvimento e execução de testes em código Java.<br>
Ele Fornece uma completa API (conjunto de classes) para construir os testes e Aplicações gráficas e em<br>
modo console para executar os testes criados.
* [Veja mais sobre o JUnit](https://junit.org/junit5/)

### IDE - Spring Tools 4 for Eclipse
O Spring Tool Suite é uma IDE baseada em Eclipse que dá algumas facilidades para trabalhos com o Spring no geral.<br>
Por ser uma IDE com base no Eclipse, apenas com o adicional dos plugins do Spring Framework, a ferramenta de debug<br>
é a mesma utilizado pelo Eclipse em sua configução padrão

### Tutorial - Implementação CRUD com Spring Boot, JUnit e Mockito
* [Spring Boot Unit Testing CRUD REST API with JUnit and Mockito](https://www.javaguides.net/2022/03/spring-boot-unit-testing-crud-rest-api-with-junit-and-mockito.html)

No tutorial referenciado acima, é implementada um CRUD de funcionários.<br>
O objetivo do tutorial é demostrar como realizar teste unitário em uma<br>
API RESTful utilizando JUnit e Mockito.

De maneira bem objetiva, são mostradas as estapas de implementação das classes<br>
e interfaces da API, assim como os teste unitários.

### Mocks Objects
O termo **Mock Objects** é utilizado para descrever um caso especial de objetos que imitam<br>
objetos reais para teste. Esses Mock Objects atualmente podem ser criados através de<br>
frameworks que facilitam bastante a sua criação. Praticamente todas as principais<br>
linguagens possuem frameworks disponíveis para a criação de Mock Objects. Os Mock<br>
Objects são mais uma forma de objeto de teste.<br>

Mocks Objects são bastante difundidos na comunidade e na literatura de métodos ágeis<br>
**Extremme Programming (XP)**, visto que, utilizando o XP se faz uso constante de testes<br>
através da técnica **Test-Driven Development (TDD)** que prega teste antes da implementação.<br>
Com isso, devemos simular alguns objetos no intuito de conseguir testar o código.<br>
