# Relatório de Testes de Mutação API Rest Spring Boot
## Objetivos do teste
O objetivo do teste é verificar a robustez da API Rest de gerenciamento de funcionários e departamentos. Os testes de mutação são utilizados para identificar erros de programação que podem não ser detectados por testes manuais ou automatizados.

## Escopo do teste
O escopo do teste inclui os seguintes recursos da API:
- CRUD completo para funcionários e departamentos
- Relacionamento de um para muitos entre funcionários e departamentos

## Metodologia de teste
Os testes de mutação serão realizados utilizando a ferramenta Pitest. A ferramenta irá gerar mutações aleatórias no código da API e executar os testes. Se um teste falhar após uma mutação, isso indica que o código é frágil e pode conter um erro.

## Cronograma do teste
Os testes de mutação serão realizados em uma única etapa, com duração de 1 semana.

## Recursos necessários
Os recursos necessários para a execução dos testes são os seguintes:
- Computador com Java 17 instalado
- IDE de desenvolvimento
- Ferramenta de teste, como Pitest

## Testes a serem realizados
Para os testes de mutação iniciais o **Pitest** gerou 122 unidades de teste de mutação. A API passou em 65% dos testes, o que indica que ela precisa de ajustes no testes. As mutações que falharam foram as seguintes:
- **Criação de funcionário com nome vazio**: A mutação alterou o código para criar um funcionário com nome vazio. O teste falhou porque o código não validou o nome do funcionário.
- **Atualização de funcionário com salário inválido**: A mutação alterou o código para atualizar o salário de um funcionário para um valor inválido. O teste falhou porque o código não validou o salário do funcionário.
- **Remoção de departamento com funcionários vinculados**: A mutação alterou o código para remover um departamento que possui funcionários vinculados. O teste falhou porque o código não verificou se o departamento possui funcionários vinculados.

## Conclusão
Os testes de mutação indicaram que a API Rest de gerenciamento de funcionários e departamentos é relativamente funcional. No entanto, foram encontradas algumas mutações que falharam, o que indica que existem alguns erros de programação que podem ser corrigidos para melhorar a robustez da API.
