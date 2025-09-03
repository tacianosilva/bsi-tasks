# Tarefa 01 - Teste de Unidade

**Nome:** Cleomar Junior  
**Usuário GitHub:** @Cleomar-Junior  
**E-mail:** cl_jr@outlook.com  

[Repositório do Projeto](link-do-seu-repo)

---

## Testes de Software – Resumo
Testes de software são processos fundamentais para garantir a qualidade, a funcionalidade e a confiabilidade de um sistema. Dentre os diversos níveis de teste, os testes de unidade destacam-se por serem a base da pirâmide de testes. Eles focam em verificar o comportamento de unidades individuais do código — como funções, métodos ou classes — de forma isolada e rápida.

Seu objetivo é validar a lógica interna de cada componente, assegurando que ele funcione corretamente antes de ser integrado a outras partes do sistema. Para isso, utilizam-se ferramentas específicas (como JUnit, pytest ou Jest) e técnicas como mocks (simulações de dependências) para isolar o código testado.

## Linguagem / Stack
Para o projeto da disciplina, escolhi a stack Django + Django REST Framework (DRF) com Python, usando SQLite para desenvolvimento local. O Django oferece uma estrutura completa com ORM, autenticação e administração, enquanto o DRF facilita criar APIs REST, com serialização, validação e permissões prontas.

O SQLite permite testar o CRUD sem configuração extra, podendo ser substituído por PostgreSQL em produção. Para testes de unidade, usei Django TestCase e APIClient, garantindo que cada operação do CRUD funcione isoladamente, com suporte a Mocks quando necessário.

A IDE escolhida foi o VS Code, que fornece depurador integrado, breakpoints e inspeção de variáveis, otimizando o desenvolvimento e debug.

## Framework de Teste
Para os testes de unidade, escolhi o Django TestCase, que é integrado ao Django e funciona bem com o APIClient do DRF, permitindo testar cada operação do CRUD de forma isolada e com suporte a Mocks, garantindo simplicidade e confiabilidade nos testes.

## IDE
A IDE escolhida foi o VS Code, devido à minha familiaridade e facilidade de uso. Ela oferece debug integrado, breakpoints, inspeção de variáveis, autocompletar de código e suporte a extensões para Python, Django e REST Framework, o que torna o desenvolvimento e a execução de testes unitários mais ágeis e organizados.

## Tutorial CRUD
[Link do tutorial](https://www.youtube.com/watch?v=Z4Lw7oViMk4) – Tutorial rápido sobre como criar um CRUD com Django + DRF

## Mock Objects
Mock Objects são objetos simulados que imitam o comportamento de dependências externas ou componentes que ainda não foram implementados, permitindo testar funções ou métodos isoladamente. Eles ajudam a focar apenas na lógica da unidade que está sendo testada, sem depender de bancos de dados, APIs ou outros serviços, tornando os testes mais rápidos, confiáveis e previsíveis.

## Experiência com Testes
(O que achou implementando)
