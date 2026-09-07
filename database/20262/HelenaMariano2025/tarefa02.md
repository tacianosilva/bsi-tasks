# Tarefa 02 - MER e Projeto de Banco de Dados Relacional

## Q1. Elementos básicos do Modelo Entidade-Relacionamento

O Modelo Entidade-Relacionamento (MER) é utilizado para representar, de forma conceitual, a estrutura de um banco de dados. Seus três elementos básicos são entidades, atributos e relacionamentos.

### Entidades

Entidades representam objetos, pessoas, conceitos ou elementos do mundo real que são relevantes para o sistema e sobre os quais se deseja armazenar informações.

No cenário de uma empresa de desenvolvimento de software, exemplos de entidades são CLIENTE, FUNCIONARIO, SQUAD, PROJETO, TAREFA, SPRINT e RELEASE.

### Atributos

Atributos são as características que descrevem uma entidade. Cada entidade possui atributos que representam as informações que devem ser armazenadas sobre ela.

Por exemplo, a entidade CLIENTE pode possuir os atributos código, nome e e-mail.

### Relacionamentos

Relacionamentos representam as associações existentes entre as entidades.

Por exemplo, um CLIENTE possui PROJETOS. Nesse caso, existe um relacionamento entre as entidades CLIENTE e PROJETO.

Os relacionamentos também podem possuir restrições de cardinalidade, indicando quantas ocorrências de uma entidade podem estar associadas a ocorrências de outra entidade.