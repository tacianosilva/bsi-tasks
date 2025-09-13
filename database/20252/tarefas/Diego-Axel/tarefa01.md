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