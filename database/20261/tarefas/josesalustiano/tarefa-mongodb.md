# Tarefa 03 - MongoDB

## 1. Scripts e Códigos Desenvolvidos
* **Script de inicialização do Banco de Dados:** [./app.py]
* **Programa de Operações CRUD (Python):** [./app.py]

---

## 2. Resumo: O MongoDB como SGBD NoSQL Orientado a Documentos
O MongoDB é um Sistema de Gerenciamento de Banco de Dados (SGBD) NoSQL de código aberto, líder de mercado, projetado para oferecer alta disponibilidade, performance escalável e flexibilidade na modelagem de dados. Diferente dos bancos de dados relacionais clássicos (como MySQL ou PostgreSQL), que organizam os dados em tabelas rígidas com linhas e colunas, o MongoDB baseia-se no modelo **Orientado a Documentos** (*Document Database*).

### A Natureza Orientada a Documentos e o Formato BSON
A principal característica arquitetônica do MongoDB é o armazenamento de registros na forma de **documentos**. Esses documentos são estruturas de dados compostas por pares de campo e valor, muito semelhantes aos objetos JSON (JavaScript Object Notation). Internamente, o MongoDB armazena esses dados em um formato chamado **BSON** (*Binary JSON*). 

O formato BSON não apenas torna a leitura e a escrita mais rápidas, mas também estende a especificação original do JSON para suportar tipos de dados adicionais, como datas (Date), identificadores nativos (ObjectId) e dados binários puros, essenciais para sistemas complexos.

### Principais Características e Vantagens

1. **Esquema Dinâmico (Schema-less):** Em bancos relacionais, todas as linhas de uma tabela devem obrigatoriamente seguir a mesma estrutura de colunas (esquema rígido). No MongoDB, os documentos pertencem a "Coleções" (*Collections*), mas os documentos dentro de uma mesma coleção não precisam ter exatamente os mesmos campos. Isso permite o polimorfismo de dados e uma adaptação extremamente ágil quando os requisitos do sistema mudam, sem a necessidade de paradas para migrações complexas de banco de dados (`ALTER TABLE`).

2. **Estruturas Aninhadas (Desnormalização):**
   O MongoDB permite que você coloque *arrays* (listas) e subdocumentos dentro de um único documento. Em um sistema relacional, representar os telefones ou endereços de um empregado exigiria a criação de tabelas separadas e o uso da operação `JOIN`. No MongoDB, todos os dados relacionados a um empregado podem ficar agrupados em um único documento, tornando as consultas (leituras) significativamente mais rápidas e reduzindo a complexidade computacional.

3. **Linguagem de Consulta Rica e Aggregation Framework:**
   Embora seja "NoSQL", o MongoDB não se limita a buscas simples de chave-valor. Ele possui uma linguagem de consulta poderosa que permite buscas por expressões regulares, intervalos de valores, consultas geoespaciais e buscas dentro de arrays. Além disso, conta com o *Aggregation Framework*, um pipeline robusto nativo para processamento de dados, agrupamentos, transformações e análises estatísticas complexas diretamente no lado do servidor.

4. **Escalabilidade Horizontal Nativa (Sharding):**
   Enquanto bancos de dados relacionais geralmente escalam verticalmente (comprando servidores com mais CPU e RAM, o que tem um limite e alto custo), o MongoDB foi construído desde o início para escalar horizontalmente. O recurso de *Sharding* distribui automaticamente coleções gigantescas de dados por múltiplos servidores (nós) menores e mais baratos, permitindo que o sistema suporte volumes massivos de dados sem perda de performance.

### A Sinergia entre MongoDB e Python (Linguagem Escolhida)

Para o desenvolvimento prático do CRUD nesta atividade, a linguagem escolhida foi o **Python**. A natureza orientada a documentos do MongoDB possui uma sinergia perfeita com as estruturas de dados nativas do Python. 

Através do driver oficial **PyMongo**, os documentos BSON do MongoDB são traduzidos automática e nativamente para **Dicionários em Python** (`dict`). Isso elimina o problema clássico de *Impedance Mismatch* (o conflito conceitual entre como um código orientado a objetos funciona e como um banco relacional armazena os dados). 

Em Python, inserir um dado no MongoDB é tão simples quanto declarar um dicionário e passá-lo para a função `insert_one()`. Isso resulta em um código mais limpo, expressivo, rápido de desenvolver e fácil de dar manutenção.

## 3. Alta Disponibilidade e Configuração Avançada (Replica Sets)

No ecossistema corporativo, bancos de dados críticos não podem ter um "ponto único de falha" (*Single Point of Failure*). Para garantir alta disponibilidade, redundância de dados e tolerância a falhas, o MongoDB implementa uma arquitetura nativa e robusta chamada **Replica Sets**.

### a. O que é um Replica Set e a Anatomia dos seus Membros

Um **Replica Set** é um cluster (grupo) de instâncias do servidor MongoDB (processos `mongod`) que mantêm exatamente o mesmo conjunto de dados. O mecanismo de replicação funciona lendo as operações de modificação de dados (armazenadas em um log especial de alta performance chamado **oplog**) e aplicando essas mesmas operações nos outros nós do cluster.

Dentro dessa topologia, cada membro assume um papel (*role*) específico para manter o sistema coeso:

1. **Primário (Primary):**
   * É o nó principal e o **único** autorizado a receber operações de escrita (Create, Update, Delete) da aplicação.
   * Ele registra todas as alterações feitas nos dados em seu `oplog`.
   * Em uma arquitetura de Replica Set padrão, só pode existir um nó primário ativo por vez.

2. **Secundário (Secondary):**
   * Atua como uma cópia de segurança em tempo real. Ele espelha o nó Primário, aplicando as operações do `oplog` de forma assíncrona para manter seu próprio conjunto de dados idêntico.
   * **Escalabilidade de Leitura:** Embora não aceitem escritas, os secundários podem ser configurados pela aplicação para responder a consultas de leitura (*Read Preferences*), distribuindo a carga e aliviando o tráfego do servidor Primário.
   * **Failover Automático:** Se o nó Primário cair (devido a falhas de hardware, rede ou manutenção), os nós Secundários percebem a queda através de *heartbeats* (pulsos de rede) e iniciam instantaneamente uma **eleição** para promover um deles a novo Primário, mantendo o sistema no ar sem intervenção humana.

3. **Árbitro (Arbiter):**
   * É um nó especial que **não armazena dados** e nunca pode se tornar um nó Primário.
   * Sua única função no cluster é **votar nas eleições**. 
   * É uma estratégia inteligente e econômica: garante que o cluster tenha um número ímpar de membros votantes (evitando empates na eleição) sem o custo de hardware necessário para manter um servidor extra replicando gigabytes de dados.

### b. Etapas e Comandos para Configuração Avançada via Docker

Para provisionar esse ambiente (simulando três servidores físicos) utilizando Docker para o banco `Atividades_Proj`, as etapas técnicas de configuração seriam:

**Passo 1: Ajuste no orquestrador (`docker-compose.yml`)**
Precisamos definir três serviços (contêineres) distintos. O passo crucial é iniciar o processo interno do banco passando a flag `--replSet` com o nome do nosso cluster.
*Exemplo prático de inicialização no YAML:*
`command: ["mongod", "--replSet", "rs-atividades", "--bind_ip_all"]`

**Passo 2: Subir a Infraestrutura**
No terminal, executamos o comando para o Docker baixar as imagens, criar a rede interna e rodar os três contêineres em segundo plano:
`docker-compose up -d`

**Passo 3: Acesso via Mongo Shell (`mongosh`)**
Mesmo com os três contêineres rodando, eles ainda atuam como servidores isolados. É necessário entrar no terminal do contêiner que desejamos que seja o líder:
`docker exec -it nome_do_container_primario mongosh`

**Passo 4: O Comando de Inicialização (`rs.initiate`)**
Dentro do shell do MongoDB, executamos o comando que injeta a configuração, fazendo com que os nós se reconheçam, formem o cluster e elejam o Primário:

```javascript
rs.initiate(
  {
    _id: "rs-atividades",
    members: [
      { _id: 0, host: "mongo1:27017" }, // Será eleito Primário
      { _id: 1, host: "mongo2:27017" }, // Secundário
      { _id: 2, host: "mongo3:27017" }  // Secundário
    ]
  }
) 