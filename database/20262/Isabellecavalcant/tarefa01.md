# Tarefa 01 - Conceitos de BD, ACID e SGBD

## Q1. Banco de Dados e Sistema Gerenciador de Banco de Dados

Um Banco de Dados (BD) é uma coleção organizada de dados relacionados, armazenados de forma que possam ser consultados, inseridos, alterados e excluídos de maneira eficiente. Ele permite que informações sejam armazenadas de forma estruturada e utilizadas por diferentes aplicações e usuários.

Um Sistema Gerenciador de Banco de Dados (SGBD) é o software responsável por criar, armazenar, organizar, consultar e gerenciar os dados de um banco de dados. Além disso, o SGBD controla aspectos como segurança, integridade, concorrência, recuperação de falhas e transações.

Alguns exemplos de bancos de dados e seus respectivos SGBDs são:

- Banco de dados relacional utilizando PostgreSQL → SGBD PostgreSQL.
- Banco de dados relacional utilizando MySQL → SGBD MySQL.
- Banco de dados relacional utilizando Oracle Database → SGBD Oracle Database.
- Banco de dados relacional utilizando SQL Server → SGBD Microsoft SQL Server.
- Banco de dados utilizando MongoDB → SGBD MongoDB.

É importante diferenciar o banco de dados do SGBD: o banco de dados corresponde aos dados armazenados, enquanto o SGBD é o software utilizado para gerenciar esses dados.

---

## Q2. Problemas do armazenamento em sistemas de arquivos

O armazenamento de dados diretamente em arquivos pode causar diversos problemas quando o sistema cresce. Entre eles estão a **redundância de dados**, quando a mesma informação é armazenada em vários arquivos; a **inconsistência**, quando essas cópias possuem valores diferentes; a dificuldade de controlar o **acesso e a segurança** das informações; e a dificuldade de realizar consultas e alterações de forma eficiente.

Além disso, sistemas baseados apenas em arquivos apresentam dificuldades para garantir a **integridade dos dados** e para recuperar informações após falhas. Também pode haver problemas quando vários usuários tentam acessar ou modificar os mesmos dados simultaneamente. Os SGBDs foram desenvolvidos para solucionar esses problemas, oferecendo mecanismos de segurança, controle de concorrência, integridade, recuperação e gerenciamento centralizado dos dados.

---

## Q3. Propriedades ACID

As propriedades ACID garantem que as transações realizadas em um banco de dados sejam executadas de forma confiável. ACID é formado por **Atomicidade, Consistência, Isolamento e Durabilidade**.

### Atomicidade

Uma transação deve ser executada completamente ou não ser executada. Por exemplo, em uma transferência bancária, o valor deve ser retirado da conta de origem e depositado na conta de destino. Se ocorrer uma falha depois do débito, a operação deve ser desfeita para que o dinheiro não desapareça.

### Consistência

A transação deve manter o banco de dados em um estado válido, respeitando suas regras e restrições. Em uma transferência, por exemplo, não deve ser permitido que uma operação deixe o saldo ou outros dados em uma situação proibida pelas regras do sistema. Sem consistência, poderiam surgir dados inválidos ou que não obedecem às regras do banco.

### Isolamento

Transações executadas simultaneamente não devem interferir umas nas outras de maneira incorreta. Por exemplo, se duas transferências forem realizadas ao mesmo tempo sobre a mesma conta, cada operação deve trabalhar com dados controlados para evitar que uma transação utilize informações incorretas produzidas pela outra.

### Durabilidade

Depois que uma transação é confirmada, seus efeitos devem permanecer registrados mesmo que ocorra uma falha no sistema. Assim, após uma transferência ser concluída e o servidor reiniciar, o débito e o crédito realizados devem continuar registrados. Sem durabilidade, uma transação confirmada poderia ser perdida após uma falha.

---

## Q4. Identificação das propriedades ACID nos cenários

### a) Falha de energia após o débito e antes do crédito

A propriedade envolvida é a **Atomicidade**. A transferência deve ser tratada como uma única transação: ou o débito e o crédito acontecem, ou nenhum dos dois permanece registrado. Caso contrário, o dinheiro poderia ser retirado da conta de origem sem ser depositado na conta de destino.

### b) Dois funcionários debitam o mesmo saldo simultaneamente

A propriedade envolvida é o **Isolamento**. As transações simultâneas devem ser controladas para que uma não interfira incorretamente na outra. Sem isolamento, os dois funcionários poderiam consultar o mesmo saldo inicial e realizar débitos que ultrapassassem o valor realmente disponível.

### c) Operação confirmada, mas dados perdidos após reinicialização do servidor

A propriedade envolvida é a **Durabilidade**. Depois que a transação é confirmada, seus efeitos devem permanecer armazenados mesmo após uma falha ou reinicialização do servidor. Sem essa propriedade, uma operação que já havia sido concluída poderia desaparecer.

### d) Transferência rejeitada porque deixaria o saldo abaixo do limite permitido

A propriedade envolvida é a **Consistência**. O banco de dados deve impedir operações que violem as regras e restrições definidas pelo sistema. Nesse caso, a transferência é rejeitada porque deixaria a conta em um estado inválido.

---

## Q5. Recuperação, integridade, redundância e inconsistência

A **recuperação** é o conjunto de mecanismos utilizados pelo SGBD para restaurar o banco de dados a um estado consistente após falhas, como quedas de energia ou problemas no servidor. Isso pode ser realizado por meio de logs, backups e mecanismos de recuperação de transações.

A **integridade** está relacionada à garantia de que os dados permaneçam corretos e de acordo com as regras definidas pelo sistema. O SGBD utiliza restrições, como chaves primárias, chaves estrangeiras e regras de validação, para evitar dados inválidos.

A **redundância** ocorre quando a mesma informação é armazenada desnecessariamente em diferentes locais. O SGBD ajuda a reduzir esse problema por meio da organização dos dados e da normalização, evitando duplicações desnecessárias.

A **inconsistência** acontece quando existem diferentes versões de uma mesma informação e elas apresentam valores divergentes. O SGBD utiliza transações, controle de concorrência e regras de integridade para manter os dados consistentes, mesmo quando vários usuários acessam ou modificam as informações simultaneamente.

---

## Q6. Mini-projeto conceitual de um sistema para uma empresa de software

O sistema proposto tem como objetivo gerenciar clientes, projetos, squads, tarefas, releases, testes e sprints de uma empresa de desenvolvimento de software.

### Entidades e principais atributos

**Cliente**
- id_cliente
- nome
- email
- telefone

**Projeto**
- id_projeto
- nome
- descrição
- data_inicio
- status

**Squad**
- id_squad
- nome
- área de atuação

**Membro**
- id_membro
- nome
- email
- cargo

O cargo pode assumir valores como desenvolvedor, tester, tech lead, supervisor ou product manager.

**Tarefa**
- id_tarefa
- título
- descrição
- prioridade
- status
- data_criacao

**Sprint**
- id_sprint
- nome
- data_inicio
- data_fim
- objetivo

**Release**
- id_release
- versão
- data_lancamento
- status

**Teste**
- id_teste
- tipo
- resultado
- data_execucao

### Relacionamentos e cardinalidades

- Um **Cliente** pode possuir vários **Projetos**, enquanto cada Projeto pertence a um único Cliente. Portanto, a relação é **1:N**.
- Um **Projeto** pode possuir vários **Squads**, e cada Squad está associado a um Projeto. Relação **1:N**.
- Uma **Squad** possui vários **Membros**, enquanto cada Membro pertence a uma Squad. Relação **1:N**.
- Um **Projeto** pode possuir várias **Tarefas**, e cada Tarefa pertence a um Projeto. Relação **1:N**.
- Uma **Squad** pode ser responsável por várias Tarefas, enquanto cada Tarefa possui uma Squad responsável. Relação **1:N**.
- Um **Projeto** pode possuir várias **Sprints**, enquanto cada Sprint pertence a um único Projeto. Relação **1:N**.
- Uma **Sprint** pode conter várias Tarefas, enquanto uma Tarefa pode estar associada a uma Sprint. Relação **1:N**.
- Um **Projeto** pode possuir várias **Releases**, enquanto cada Release pertence a um Projeto. Relação **1:N**.
- Uma **Release** pode possuir vários **Testes**, enquanto cada Teste está associado a uma Release. Relação **1:N**.
- Um **Membro** pode ser responsável por várias Tarefas, enquanto cada Tarefa possui um responsável. Relação **1:N**.

### Regras de integridade

O sistema deve garantir que cada entidade possua um identificador único. Um Projeto deve estar associado a um Cliente existente e uma Tarefa deve estar associada a um Projeto existente. As datas de início e fim de uma Sprint devem ser válidas, sendo que a data de início não pode ser posterior à data de fim.

O status de Projetos, Tarefas, Sprints e Releases deve utilizar apenas valores previamente definidos pelo sistema. Uma Tarefa não pode ser atribuída a um Membro inexistente, e uma Release não pode ser considerada concluída sem que os testes necessários tenham sido executados.

### Diagrama conceitual

```mermaid
erDiagram
    CLIENTE ||--o{ PROJETO : possui
    PROJETO ||--o{ SQUAD : possui
    SQUAD ||--o{ MEMBRO : possui
    PROJETO ||--o{ TAREFA : possui
    SQUAD ||--o{ TAREFA : responsavel
    MEMBRO ||--o{ TAREFA : executa
    PROJETO ||--o{ SPRINT : possui
    SPRINT ||--o{ TAREFA : contem
    PROJETO ||--o{ RELEASE : possui
    RELEASE ||--o{ TESTE : possui

    CLIENTE {
        int id_cliente PK
        string nome
        string email
        string telefone
    }

    PROJETO {
        int id_projeto PK
        string nome
        string descricao
        date data_inicio
        string status
    }

    SQUAD {
        int id_squad PK
        string nome
        string area_atuacao
    }

    MEMBRO {
        int id_membro PK
        string nome
        string email
        string cargo
    }

    TAREFA {
        int id_tarefa PK
        string titulo
        string descricao
        string prioridade
        string status
        date data_criacao
    }

    SPRINT {
        int id_sprint PK
        string nome
        date data_inicio
        date data_fim
        string objetivo
    }

    RELEASE {
        int id_release PK
        string versao
        date data_lancamento
        string status
    }

    TESTE {
        int id_teste PK
        string tipo
        string resultado
        date data_execucao
    }