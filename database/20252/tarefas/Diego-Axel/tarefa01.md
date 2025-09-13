<h1 align="center">Tarefa 01 - Conceitos BD e MER</h1>

| Nome do Aluno:| Usuário no Github| E-mail |
|------|---------|--------|
| Diêgo Axel Bernardo Santos Rodrigues | [Diego-Axel](https://github.com/Diego-Axel) | [Acadêmico](diego.axel.bernardo.097@ufrn.edu.br) |

<br>

# Atividade para a matéria de Banco de Dados da faculdade de Sistemas de Informação - UFRN.

# Questões: 

## Letra 🅰️: Descreva o que é um Banco de Dados e o que é um Sistema Gerenciador de Banco de Dados. Cite exemplos de Bancos de Dados e seus SGBDs.

Um **Banco de Dados** é uma **coleção organizada de dados** que podem ser acessados, gerenciados e atualizados facilmente. Pense nele como uma planilha ou um armário de arquivos. Ele apenas armazena a informação.

Já um **Sistema Gerenciador de Banco de Dados(SGBD)** É o programa (software) que você usa para controlar o banco de dados. Ele permite criar, ler, atualizar e apagar os dados, além de gerenciar a segurança e o acesso. Exemplos: MySQL, PostgreSQL, Oracle, SQL Server.

Em resumo: O **BD** é o conjunto de dados, e o **SGDB** é a ferramente que gerencia esses dados

### Exemplo de dados em um banco de dados:

| ID | Produto         | Quantidade |
|----|-----------------|------------|
| 1  | Macarrão        | 23         |
| 2  | Pacote de Arroz | 35         |
| 3  | Pipoca Doritos  | 26         |
| 4  | Pacote de Arroz | 35         |

---

## Letra  🅱️: Quais os principais problemas de utilizar Sistemas de Arquivos para armazenagem de dados.

Utilizar **sistemas de arquivos** (como pastas e arquivos .txt, .csv, ou .json) para armazenar dados em vez de um SGBD causa problemas sérios de:

1. Dificuldade de Acesso aos Dados.

2. Falta de Integridade.

3. Segurança e Controle de Acesso.

4. Problemas de Atomicidade.

Entre outros... Mas em resumo, sistemas de arquivos não oferecem mecanismos robustos para garantir que os dados sejam consistentes, seguros, íntegros e fáceis de acessar, especialmente em ambientes com múltiplos usuários e regras complexas.

---

## Letra C: O modelo de dados entidade-relacionamento foi desenvolvido para facilitar o projeto de banco de dados, permitindo especificação de um esquema que representa a estrutura lógica geral de um banco de dados. Descreva os três elementos básicos de um Modelo Entidade Relacionamento (MER)

1. **Entidades**: São os objetos ou conceitos do mundo real sobre os quais se deseja guardar informações. Pense nelas como os substantivos do sistema.
    - Exemplos: ```CLIENTE```, ```PRODUTO```, ```ALUNO```, ```PEDIDO```, ```MÉDICO```

2. **Atributos**: São as propriedades ou características que descrevem uma entidade. Pense neles como os adjetivos ou os dados específicos de uma entidade.
    - Exemplos: Para a entidade ```CLIENTE```, os atributos poderiam ser ```Nome```, ```CPF```, ```Endereço``` e ```Telefone```.

3. **Relacionamentos**: Representam a associação ou a interação que existe entre duas ou mais entidades. Pense neles como os verbos que conectam as entidades.
    - Exemplos:
        - Um ```CLIENTE``` faz um ```PEDIDO```. (Relacionamento entre as entidades ```CLIENTE``` e ```PEDIDO```).
        - Um ```ALUNO``` se matricula em uma ```TURMA```. (Relacionamento entre ```ALUNO``` e ```TURMA```).
        
---