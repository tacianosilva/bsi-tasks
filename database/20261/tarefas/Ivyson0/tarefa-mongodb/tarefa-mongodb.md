# Resumo sobre MongoDB

O MongoDB é um Sistema Gerenciador de Banco de Dados NoSQL orientado a documentos. Diferente dos bancos relacionais tradicionais, ele utiliza documentos no formato BSON/JSON para armazenar dados de forma flexível e dinâmica.

Principais características do MongoDB:

* Modelo orientado a documentos;
* Estrutura flexível sem esquema rígido;
* Alta escalabilidade;
* Suporte a replicação e alta disponibilidade;
* Integração simples com aplicações modernas;
* Armazenamento em coleções e documentos.

Nesta atividade foi utilizada a linguagem Python juntamente com a biblioteca PyMongo para realizar a comunicação com o banco de dados.

---

# Configuração do MongoDB com Docker

Foi utilizado Docker para executar o servidor MongoDB localmente.

Imagem utilizada:

```bash
mongo
```

Porta configurada:

```text
27017
```

Usuário criado:

```text
Usuário: ivyson0
Senha: 12345
```

Banco criado:

```text
AtividadesProj
```

---

# Estrutura das Coleções

O sistema foi modelado utilizando as seguintes coleções:

## empregados

Armazena os dados dos empregados do departamento.

Campos principais:

* nome
* cargo
* idade
* salario

## projetos

Armazena os projetos cadastrados.

Campos principais:

* nome
* lider
* prazo_meses
* orcamento

## atividades

Armazena as atividades vinculadas aos projetos.

Campos principais:

* titulo
* status
* horas
* projeto

---

# Script de Inicialização

Arquivo:

```text
tarefa_mongo/init_mongo.py
```

O script realiza:

* conexão com MongoDB;
* criação das coleções;
* inserção de dados iniciais;
* limpeza de dados antigos.

---
