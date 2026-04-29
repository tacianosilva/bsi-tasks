# Tarefa 01 - Conceitos BD e MER

**Nome:** Leandro Isaac  
**Usuário GitHub:** lelebiglove  
**E-mail:** isaac.brito.136@ufrn.edu.br

---

## Respostas
## Seção A

Banco de Dados (BD)  
É uma coleção organizada de dados persistentes, estruturados de forma a permitir armazenamento, recuperação e atualização com eficiência. Um BD oferece representação dos dados (estrutura) e garante integridade, independência e consistência dos dados.

Sistema Gerenciador de Banco de Dados (SGBD)  
É o software responsável por criar, ler, atualizar e apagar dados em um BD. O SGBD providencia interfaces (SQL, APIs), mecanismos de controle de concorrência, recuperação de falhas, segurança e gerenciamento de transações.

Exemplos  
- Bancos de Dados relacionais: esquema de tabelas (RDBMS). Exemplos de SGBDs: MySQL, PostgreSQL, MariaDB, Oracle Database,Microsoft SQL Server.


## seção B
1. Redundância e inconsistência — sem um SGBD, dados são frequentemente duplicados (vários arquivos contém a mesma informação) e fica difícil mantê-los consistentes.  
2. Ausência de controle de concorrência — vários usuários/processos não conseguem acessar/alterar de forma segura ao mesmo tempo; risco de sobrescrita e corrupção.  
3.Recuperação de falhas limitada — sistemas de arquivos simples não oferecem logs de transação e mecanismos robustos de rollback/recovery.  
4. Dificuldade de consultar dados — consultas complexas (joins, filtros compostos) exigem lógica de aplicação cara de manter; não há otimização de consultas.  
5. Segurança e integridade limitada — validação e regras de integridade (ex.: constraints, foreign keys) precisam ser implementadas na aplicação.  
6.Escalabilidade e desempenho — conforme o volume cresce, gerenciamento fica ineficiente; SGBDs têm índices e otimizações que sistemas de arquivos não têm.  
7. Independência de dados — mudança na estrutura dos arquivos exige alteração na aplicação; SGBDs oferecem camadas de abstração.

## seção C 


1.Entidade — representa um objeto do mundo real que possui existência distinta e cujas informações serão armazenadas. Ex.: *Empregado*, *Departamento*.  
   - Entidades têm atributos (ex.: nome, código, e-mail).  
2.Relacionamento — representa associação entre duas ou mais entidades. Ex.: *Empregado* trabalha_em Departamento. Relacionamentos têm grau (binário, ternário), opcionalidade e cardinalidade.  
3. Atributo — propriedade que descreve uma entidade ou relacionamento. Atributos podem ser simples, compostos, multivalorados ou derivados. Além disso, existem identificadores (chave/PK) que distinguem instâncias de uma entidade.

## Seção D 
Várias notações e variantes são usadas para desenhar Diagramas ER. Exemplos de diferentes notações para conceitos comuns:

- **Cardinalidade**
  - **Chen (1976)**: usa rombos para relacionamentos, retângulos para entidades e expressões como 1:N, M:N escritas ao lado.  
  - **Notação (Crow’s Foot)**: usa "pé-de-coruja" (crow’s foot) para representar “muitos”, linha simples para “um”, círculo para “zero/um” (opcional), barra para “um obrigatório”.  
  - **Bachman / UK**: usa símbolos distintos (setas, barras) para indicar (1,0..1,1..N).
- **Identificador (chave)**
  - Sublinhado do atributo (Chen).  
  - Sufixo `PK` ou `*` junto ao atributo (algumas notações orientadas a modelos lógicos).  
- **Entidade subordinada / entidade fraca**
  - **Chen**: entidade fraca desenhada como retângulo com borda dupla; relacionamento identificador com rombo de borda dupla.  
  - **Crow’s Foot**: usa notação onde a dependência é indicada e a chave parcial é mostrada com sublinhado ou anotação.
- **Atributos compostos / multivalorados**
  - **Chen**: atributos compostos desenhados com ramificações; multivalorado com elipse duplo.  
  - **Outras notações**: listam atributos entre parênteses ou com marcador `[]` para multivalorados.

  ## Seção E 

  ```mermaid
erDiagram
    EMPREGADO {
        string codigo PK "código único do empregado"
        string nome
        string email
    }

    TIPO_EMPREGADO {
        string tipo_id PK "id do tipo (ex: livre, fixo)"
        string descricao
        boolean horario_livre "true = horário livre, false = horário fixo"
        integer horas_mes "aplica-se se horario_livre = true"
        integer min_horas_dia "aplica-se se horario_livre = true"
    }

    DIA_SEMANA {
        string codigo PK "ex: dom, seg, ter, ..."
        string nome "ex: domingo, segunda-feira, ..."
    }

    TURNO {
        string turno_id PK
        time inicio
        time fim
        string descricao "turno associado a um dia da semana"
    }

    PONTO {
        string ponto_id PK
        date data
        time entrada
        time saida
        string observacao
    }

    %% Relacionamentos (cardinalidades conceituais)
    TIPO_EMPREGADO ||--o{ EMPREGADO : "classifica"
    DIA_SEMANA ||--o{ TURNO : "possui"
    EMPREGADO ||--o{ PONTO : "registra"
    TURNO ||--o{ PONTO : "tem"
    EMPREGADO ||--o{ TURNO : "possui_agendamento" 

    %% Observações e restrições (não implementadas como chaves, são regras conceituais)
    %% - Empregados com horario_livre armazenam horas_mes e min_horas_dia em TIPO_EMPREGADO.
    %% - Empregados com horario fixo têm agendamento de TURNO por DIA_SEMANA; podem ter até 2 TURNOs no mesmo dia.
    %% - Cada PONTO refere-se a um EMPREGADO e a um TURNO (registro de entrada/saída).