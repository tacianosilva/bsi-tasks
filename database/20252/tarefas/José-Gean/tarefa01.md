# Tarefa 01 – Conceitos BD e MER

| Nome                        | GitHub   | E-mail                        |
|-----------------------------|----------|-------------------------------|
| José Gean de Macêdo Alves   | [JGean09](https://github.com/jGean09) | jose.gean.706@ufrn.edu.br |

---

## Questões

### Questão 7.A: Descreva o que é um Banco de Dados e o que é um Sistema Gerenciador de Banco de Dados. Cite exemplos de Bancos de Dados e seus SGBDs.

#### Resposta
Um **Banco de Dados** é uma coleção organizada de dados que podem ser acessados, gerenciados e atualizados facilmente.  
Ele apenas armazena a informação. Exemplos: planilhas, tabelas de produtos, registros de alunos etc.

Já um **Sistema Gerenciador de Banco de Dados (SGBD)** é o software que permite criar, consultar, atualizar e apagar dados, além de gerenciar segurança e acesso.  
Exemplos: **MySQL, PostgreSQL, Oracle, SQL Server**.

O banco de dados é o conjunto de dados, e já SGDB é a ferramente que gerencia esses dados

Exemplo de dados em um banco de dados:

| ID | Produto        | Quantidade |
|----|----------------|------------|
| 1  | Celular        | 3          |
| 2  | Notebook Dell  | 5          |
| 3  | Memória Ram    | 8          |
| 4  | SDD 256G       | 10        |

---

### Questão 7.B: Quais os principais problemas de utilizar Sistemas de Arquivos para armazenagem de dados?

#### Resposta
Utilizar sistemas de arquivos (como pastas e arquivos no Windows ou Linux) para guardar dados apresenta vários problemas, principalmente quando comparado a um SGBD. Entre eles:

- **Redundância e inconsistência**: os mesmos dados podem ser armazenados em vários arquivos diferentes, gerando duplicação e risco de estarem desatualizados ou contraditórios.
- **Dificuldade de acesso**: localizar e consultar informações exige criar programas específicos ou percorrer manualmente os arquivos.
- **Falta de segurança**: não há controle de acesso detalhado, qualquer pessoa que tenha acesso ao sistema pode manipular os arquivos.
- **Ausência de integridade**: não existem mecanismos que garantam regras de consistência (como tipos de dados, chaves primárias ou relacionamentos).
- **Dificuldade em manipular grandes volumes de dados**: sistemas de arquivos não são otimizados para lidar com consultas complexas em grandes bases de dados.
- **Baixa escalabilidade e concorrência**: não existe controle eficiente quando vários usuários tentam acessar e alterar os dados ao mesmo tempo.

logo o sistemas de arquivos funcionam para armazenar dados simples, mas se tornam inviáveis quando a aplicação cresce e exige segurança, integridade e múltiplos acessos simultâneos.

---