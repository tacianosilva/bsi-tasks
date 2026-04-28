# Tarefa: ODBC e ORM

Este documento apresenta uma visão técnica sobre as tecnologias de integração de banco de dados utilizadas no desenvolvimento de software, com foco na linguagem **Python**.


## 1. ODBC (Open Database Connectivity) em Python

O **ODBC** é um padrão de interface de programação de aplicações (API) para acessar sistemas de gerenciamento de banco de dados (SGBD). Ele foi projetado para ser independente de linguagens de programação e de sistemas operacionais.

Na linguagem **Python**, a utilização de ODBC permite que a aplicação se conecte a diversos bancos de dados (como PostgreSQL, SQL Server ou MySQL) de forma uniforme, desde que o driver correspondente esteja instalado. A biblioteca mais comum para essa finalidade é a `pyodbc`.

**Principais características:**
* **Abstração de Driver:** O desenvolvedor interage com uma interface comum, enquanto o driver cuida das especificidades do SGBD.
* **Desempenho:** Por ser uma interface de nível mais baixo, oferece excelente performance para operações em lote.
* **Compatibilidade:** Essencial para integrar sistemas Legados ou ambientes onde múltiplos SGBDs coexistem.

---

O **ORM** é uma técnica que permite mapear objetos de uma linguagem de programação (como Python) para tabelas de um banco de dados relacional. Isso permite que o desenvolvedor manipule os dados utilizando a sintaxe da linguagem em vez de escrever SQL puro diretamente.

**Vantagens do ORM:**
* **Produtividade:** Reduz a quantidade de código repetitivo (*boilerplate*).
* **Segurança:** Protege naturalmente contra ataques de SQL Injection.
* **Manutenibilidade:** As alterações no esquema do banco são refletidas diretamente nas classes/modelos.

---

## 3. Framework Utilizado: Django ORM

O framework escolhido para a implementação desta tarefa foi o **Django ORM**. Por ser um framework *batteries-included*, o Django oferece uma camada de abstração poderosa e integrada para o PostgreSQL.

**Por que o Django ORM?**
O Django ORM facilita a criação de consultas complexas através de métodos como `.filter()`, `.exclude()` e `.annotate()`. Além disso, o sistema de **Migrations** automatiza a evolução do banco de dados, garantindo que a estrutura das tabelas esteja sempre em sincronia com o código Python.

---

## 4. Arquivos Desenvolvidos na Tarefa:

### 4.1. Repositório do Projeto

O código-fonte completo da aplicação desenvolvida para esta tarefa, utilizando o framework Django e banco de dados, está disponível no repositório abaixo:

* [Acessar o Repositório do Projeto Django](https://github.com/ariadnyD/BD.git)

---

### 4.2. Scripts e Programas Criados

Os arquivos de testes específicos solicitados na atividade podem ser visualizados diretamente pelos links abaixo:

* [Script de execução via Driver/SQL (`teste_driver.py`)](https://github.com/ariadnyD/BD.git/tarefa02/teste_driver.py)
* [Script de execução via Django ORM (`teste_orm.py`)](https://github.com/ariadnyD/BD.git/tarefa02/teste_orm.py)

### 4.3 Resultados

Abaixo estão os resultados das execuções dos scripts realizados dentro do ambiente virtual (`venv`), utilizando o banco de dados SQLite.

* **Execução via Driver SQL (`teste_driver.py`)**

Nesta etapa, o script realizou a conexão direta, inseriu uma nova atividade e atualizou o líder do projeto utilizando comandos SQL puros.

```text
(venv) ariadny@linuxmint:~/tarefa02$ python3 teste_driver.py
Projeto: APF | Atividade: Nova Atividade Driver
```

* **Execução via Django ORM (`teste_orm.py`)**

Nesta etapa, o framework Django foi utilizado para manipular os objetos. O resultado abaixo confirma que a listagem está funcionando corretamente, exibindo tanto a atividade criada anteriormente pelo Driver quanto a nova atividade criada via ORM.

```text
(venv) ariadny@linuxmint:~/tarefa02$ python3 teste_orm.py
Projeto: APF
  - Nova Atividade Driver
  - Nova Atividade ORM
```

---

## 5. Conclusão dos Requisitos
Com base nas saídas acima, confirma-se o cumprimento de todos os requisitos solicitados:
1. **Inserção:** Realizada com sucesso em ambos os métodos.
2. **Atualização:** O líder do projeto foi atualizado via código antes da listagem.
3. **Listagem:** O programa percorreu os projetos e suas respectivas atividades relacionadas, exibindo-as no terminal.

---
