# Tarefa 02: Integração de Banco de Dados com Python (Driver/ODBC e ORM)

Este documento detalha as abordagens teóricas e as implementações práticas exigidas para a integração entre aplicações backend e bancos de dados relacionais, utilizando a linguagem **Python**.

---

## 1. A Abordagem Tradicional: Conexão Direta e Padrões (ODBC / DB-API)

O **ODBC** (Open Database Connectivity) é um padrão histórico estabelecido para criar uma interface de comunicação uniforme entre aplicações e Sistemas de Gerenciamento de Banco de Dados (SGBDs). A sua premissa é permitir que o código da aplicação seja independente do banco de dados utilizado, delegando as especificidades para um "driver" intermediário.

No ecossistema **Python**, a comunicação de baixo nível com bancos de dados é regida por um padrão oficial chamado **PEP 249 (Python Database API Specification v2.0)**. Em vez de usar bibliotecas ODBC genéricas, a comunidade Python frequentemente adota drivers específicos que seguem essa especificação DB-API para cada SGBD (como `psycopg2` para PostgreSQL ou `sqlite3` para SQLite).

**Características da implementação via Driver direto:**
* **Controle Granular:** O desenvolvedor escreve os comandos em SQL puro (DML, DDL, DQL) diretamente no código da aplicação.
* **Alta Performance:** Por não ter camadas de tradução complexas, é a abordagem mais rápida, sendo ideal para *bulk inserts* (inserções em massa) ou consultas analíticas extremamente complexas.
* **Desvantagens:** Exige a escrita de muito código repetitivo (gerenciamento de cursores, aberturas e fechamentos de transações) e deixa a aplicação vulnerável a falhas de segurança, como *SQL Injection*, se os dados não forem devidamente sanitizados.

Para a implementação da Questão 4, utilizou-se o banco de dados **SQLite** através do seu driver nativo na linguagem (`sqlite3`), simulando o acesso direto como pedido na atividade.

---

## 2. A Abordagem Moderna: ORM (Object-Relational Mapping)

O **ORM** (Mapeamento Objeto-Relacional) é um padrão de arquitetura de software projetado para resolver um problema clássico conhecido como *Impedance Mismatch* — a diferença fundamental de paradigmas entre a orientação a objetos (usada no Python) e o modelo relacional (usado nos SGBDs).

Com o ORM, as tabelas do banco de dados são representadas como **Classes** na linguagem de programação, e os registros das tabelas tornam-se **Instâncias** (objetos) dessas classes.

**Principais benefícios da adoção de um ORM:**
* **Produtividade e Abstração:** O desenvolvedor não precisa escrever consultas em SQL. Funções nativas da linguagem (como `.save()`, `.create()`, `.filter()`) são convertidas automaticamente para SQL em tempo de execução.
* **Agnosticismo de Banco de Dados:** A troca do SGBD (por exemplo, migrar de SQLite para PostgreSQL) exige apenas a alteração de uma linha de configuração, sem necessidade de reescrever as *queries*.
* **Segurança Embutida:** Os ORMs modernos realizam o escape automático de variáveis, protegendo a aplicação contra *SQL Injection*.

---

## 3. O Framework Escolhido: Django ORM

O framework escolhido para fazer esta tarefa foi o **Django**. 

O Django possui um dos ORMs mais maduros e completos do mercado. Ele utiliza o padrão *Active Record* e destaca-se pelo seu ecossistema de **Migrations**. No escopo desta atividade, o Django foi capaz de ler as classes definidas no arquivo `models.py` (como `Projeto` e `Atividade`) e gerar toda a estrutura física do banco de dados (DDL) de forma totalmente automatizada. 

Além disso, a sintaxe de consultas do Django permite percorrer relações entre tabelas (como buscar as atividades pertencentes a um projeto) de maneira extremamente fluida e legível.

---

## 4. Código-Fonte

Todos os códigos solicitados para a execução desta atividade encontram-se no repositório abaixo:

* 🔗 **[Clique aqui para acessar o Repositório do Projeto no GitHub](https://github.com/josesalustiano/Banco_de_dados)**

**Mapeamento dos Arquivos Principais:**
* `core/models.py`: Definição do esquema do banco de dados em classes Python.
* `povoar.py`: Script responsável por limpar e popular o banco de dados com os dados iniciais requeridos.
* `teste_driver.py`: Script que resolve as **Questões 4 e 5** (Conexão e operações via Driver `sqlite3`).
* `teste_orm.py`: Script que resolve a **Questão 6** (Operações utilizando o Django ORM).

---

## 5. Evidências de Execução e Validação dos Requisitos

Os testes foram executados com sucesso de forma sequencial no mesmo banco de dados, comprovando que ambas as abordagens (Driver e ORM) interagem corretamente com a base de dados centralizada.

### 5.1. Saída do script via Driver direto (`teste_driver.py`):
Nesta execução, a inserção e a atualização de líder foram feitas usando SQL DML.

```text
--- INICIANDO TESTE VIA DRIVER (SQLITE3) ---
[OK] Nova atividade inserida com sucesso (Driver).
[OK] Líder do projeto atualizado com sucesso (Driver).

--- LISTA DE PROJETOS E ATIVIDADES (DRIVER) ---
Projeto: APF | Atividade: APF - Atividade 1
Projeto: APF | Atividade: Nova Atividade via Driver
Projeto: Monitoria | Atividade: Monitoria - Atividade 1
```
---


### 6. Considerações Finais:

Os resultados no terminal confirmam que a atividade cumpriu tudo o que foi pedido na prática. As duas formas de conexão funcionaram perfeitamente:

* **Inserção (INSERT):** Novas atividades foram salvas e vinculadas aos projetos corretamente.
* **Atualização (UPDATE):** A troca do líder do projeto aconteceu direitinho e já estava salva no banco na hora da listagem.
* **Consulta (SELECT):** O código cruzou os dados com sucesso, gerando aquela lista organizada no terminal com cada projeto e suas respectivas atividades.