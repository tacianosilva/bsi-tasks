# Tarefa 01 - Teste de Unidade

- Nome: Flavio Roberto
- Github: FlaviodosSantos
- e-mail: flaviovorthrox@yahoo.com.br

- [Link do repositorio](https://github.com/FlaviodosSantos/bsi-tasks/tree/task/issue%2392/softwaretesting/20232/tarefas/FlaviodosSantos)

---

<br>

## Testes unitários, o que são ?

Os testes unitários são essenciais. Sem eles, você está pisando sobre casca de ovos o tempo todo.

O teste unitário consiste em verificar o comportamento das menores unidades em sua aplicação.

Tecnicamente, isso seria uma classe ou até mesmo um método de classe em línguas orientadas a objetos, e seria um procedimento ou função em línguas processuais e funcionais.

Os testes unitários precisam funcionar isoladamente porque precisam funcionar rapidamente.

Todo o conjunto de testes unitários de uma aplicação precisa funcionar em minutos, de preferência em segundos. Você verá o porquê mais tarde.

É por isso que os testes unitários não podem utilizar nenhum processo ou sistema externo. Nenhuma operação de E/S (input/output) de qualquer tipo (banco de dados, arquivo, console, rede) exceto o registro de falhas nos testes e talvez a leitura da configuração padrão de alternância de recursos no início de uma execução de teste.

Se seu código de teste (ou as bibliotecas que utiliza) fizer E/S ou acessar qualquer coisa fora de seu processo, não é um teste unitário, e sim um teste de integração.

[link](https://www.digite.com/pt-br/agile/testes-unitarios/#:~:text=O%20que%20%C3%A9%20Teste%20de%20Unit%C3%A1rio%3F,em%20l%C3%ADnguas%20processuais%20e%20funcionais.)

<br>

## Linguagem escolhida : Python e Django Rest Framework

### Python

Trata-se de uma linguagem de programação de uso geral, o que significa que pode ser usada para criar uma grande variedade de aplicações diferentes e não é especializada em nenhum problema determinado.

Essa versatilidade, juntamente com sua facilidade de uso para iniciantes, tornou-a uma das linguagens mais usadas atualmente.

[link](https://www.python.org/)

### Django

Em síntese, o Django é um framework gratuito de aplicativos web com código aberto escrito em Python. 

O site oficial do Django diz que ele é uma estrutura da web Python de alto nível. Além disso, o site também cita que esse framework é:

- Ridiculamente rápido: o Django é projetado para ajudar os desenvolvedores a levar as aplicações do conceito à conclusão o mais rápido possível;
- Com segurança garantida: ele leva a segurança a sério e ajuda os desenvolvedores a evitar muitos erros comuns de cibersegurança;
- Excessivamente escalável: muitos dos sites mais movimentados da web utilizam o Django para escalar de forma rápida e flexível.

Ademais, muitos desenvolvedores Django concordam que o framework cuida da parte “chata” de desenvolvimento da web, para que o programador possa ter foco total na escrita do aplicativo sem ter que pensar em grandes invenções.

[link] (https://www.djangoproject.com/)

### Django Rest Framework

Django REST Framework ou DRF é uma biblioteca que permite a construção de APIs REST utilizando a estrutura do Django. Lançado em Fevereiro de 2011, o DRF, por funcionar sob a estrutura do Django, permite a construção de APIs em qualquer plataforma, seja Windows, macOS ou Linux.

Alguns motivos pelos quais você pode querer usar a estrutura REST:

- A API navegável na Web é uma grande vantagem em termos de usabilidade para seus desenvolvedores.
- Políticas de autenticação incluindo pacotes para OAuth1a e OAuth2 .
- Serialização que suporta fontes de dados ORM e não ORM .
- Totalmente personalizável - basta usar visualizações regulares baseadas em funções se não precisar dos recursos mais poderosos .
- Documentação extensa e excelente suporte da comunidade .
- Usado e confiável por empresas reconhecidas internacionalmente, incluindo Mozilla , Red Hat , Heroku e Eventbrite .

[link](https://www.django-rest-framework.org/)

---
