# Plano de Teste para API Rest Spring Boot
## Objetivos do teste
O objetivo do teste é garantir que a API Rest de gerenciamento de funcionários e departamentos funcione corretamente e de acordo com os requisitos.

## Escopo do teste
O escopo do teste inclui os seguintes recursos da API:
- CRUD completo para funcionários e departamentos
- Relacionamento de um para muitos entre funcionários e departamentos

## Critérios de aceitação
Os testes serão considerados bem-sucedidos se a API atender aos seguintes critérios:
-   Todos os endpoints devem retornar respostas válidas.
-   Todos os dados devem ser armazenados e recuperados corretamente.
-   O relacionamento de um para muitos deve funcionar corretamente.

## Metodologia de teste
Os testes serão realizados utilizando as seguintes técnicas:
- Testes unitários
- Testes de integração
- Testes de aceitação

## Cronograma do teste
Os testes serão realizados em duas etapas:
- Etapa 1: Testes unitários e de integração (1 semana)
- Etapa 2: Testes de aceitação (1 semana)

## Recursos necessários
Os recursos necessários para a execução dos testes são os seguintes:
-   Computador com Java 17 instalado
-   IDE de desenvolvimento
-   Ferramentas de teste, como JUnit e Postman

## Cenários de teste
Os seguintes cenários de teste serão executados:
- Testes unitários
- Criação de funcionário
- Atualização de funcionário
- Exclusão de funcionário
- Consulta de funcionário
- Listar funcionários de um departamento
- Criação de departamento
 - Atualização de departamento
 - Exclusão de departamento
 - Consulta de departamento
 - Testes de integração
 - Criação de relacionamento entre funcionário e departamento
 - Atualização de relacionamento entre funcionário e departamento
 - Exclusão de relacionamento entre funcionário e departamento
 - Consulta de relacionamentos entre funcionário e departamento
 - Testes de aceitação
 - Usuário deve ser capaz de criar um funcionário com sucesso.
 - Usuário deve ser capaz de atualizar um funcionário com sucesso.
 - Usuário deve ser capaz de excluir um funcionário com sucesso.
 - Usuário deve ser capaz de consultar um funcionário com sucesso.
 - Usuário deve ser capaz de criar um departamento com sucesso.
 - Usuário deve ser capaz de atualizar um departamento com sucesso.
 - Usuário deve ser capaz de excluir um departamento com sucesso.
 - Usuário deve ser capaz de consultar um departamento com sucesso.
 - Usuário deve ser capaz de criar um relacionamento entre funcionário e departamento com sucesso.
 - Usuário deve ser capaz de atualizar um relacionamento entre funcionário e departamento com sucesso.
 - Usuário deve ser capaz de excluir um relacionamento entre funcionário e departamento com sucesso.
 - Usuário deve ser capaz de consultar relacionamentos entre funcionário e departamento com sucesso.

## Conclusão
Este plano de teste fornece uma visão geral dos testes que serão realizados para garantir a qualidade da API Rest de gerenciamento de funcionários e departamentos. Os testes serão realizados de forma sistemática e abrangente, utilizando uma variedade de técnicas.
