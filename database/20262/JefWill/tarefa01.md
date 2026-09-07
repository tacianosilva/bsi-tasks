# Tarefa 01 - Conceitos de BD, ACID e SGBD

## Q1. Banco de Dados e SGBD

Um **Banco de Dados (BD)** é uma coleção logicamente coerente de dados relacionados, com algum significado implícito, estruturada para representar fatos e entidades de um recorte do mundo real (frequentemente chamado de *mini-mundo* ou universo de discurso). O banco de dados armazena as informações necessárias para que diferentes usuários e sistemas possam consultá-las e atualizá-las.

Já um **Sistema Gerenciador de Banco de Dados (SGBD)** é um software geral que facilita o processo de definição, construção, manipulação e compartilhamento de bancos de dados entre vários usuários e aplicações. O SGBD é a camada de software responsável pelo controle de concorrência, recuperação após falhas, segurança, integridade e otimização das consultas físicas no disco.

A distinção fundamental é direta: o **banco de dados são os dados estruturados em si**, enquanto o **SGBD é o software que gerencia, protege e viabiliza o acesso a esses dados**.

### Exemplos reais com SGBDs utilizados

Abaixo estão exemplos de sistemas conhecidos, seus respectivos bancos de dados e os SGBDs empregados:

| Banco de Dados (Domínio / Sistema Real) | SGBD Utilizado | Tipo / Finalidade |
|---|---|---|
| **SIGAA (UFRN)** — Banco de dados acadêmico (alunos, notas, turmas, matrículas) | **PostgreSQL** | Relacional (RDBMS), utilizado na infraestrutura dos sistemas SIG da universidade |
| **Wikipédia (Wikimedia Foundation)** — Banco de dados de artigos, revisões e usuários | **MariaDB** | Relacional (fork do MySQL), operado em clusters com alta taxa de leitura |
| **Stack Overflow** — Banco de dados central de postagens, votos, tags e reputação | **Microsoft SQL Server** | Relacional corporativo, responsável pelo núcleo transacional da plataforma |
| **OpenStreetMap (OSM)** — Banco de dados geoespacial de mapas e coordenadas mundiais | **PostgreSQL (com PostGIS)** | Objeto-relacional com suporte espacial para armazenamento geográfico |
| **GitHub** — Banco de dados de metadados de repositórios, issues, pull requests e usuários | **MySQL** | Relacional, operado em clusters particionados de alta escala |

#### Referências dos exemplos:
- **SIGAA / UFRN:** Portal SINFO (Superintendência de Informática da UFRN) – documentação da arquitetura dos sistemas SIG utilizando PostgreSQL.
- **Wikipédia / Wikimedia:** *Wikimedia Foundation Server Architecture* (wikitech.wikimedia.org) – documentação sobre uso de MariaDB/MySQL nos clusters de produção.
- **Stack Overflow:** *Stack Overflow Architecture* (Nick Craver, blog oficial de engenharia) – detalha a infraestrutura central com MS SQL Server.
- **OpenStreetMap:** Documentação técnica da Wiki OpenStreetMap (*Servers/database*) – uso de PostgreSQL com extensão PostGIS.
- **Definições teóricas:** ELMASRI, Ramez; NAVATHE, Shamkant B. *Sistemas de Banco de Dados*. 6ª ed. São Paulo: Pearson, 2011; SILBERSCHATZ, Abraham; KORTH, Henry F.; SUDARSHAN, S. *Sistema de Banco de Dados*. 6ª ed. Elsevier, 2012.

## Q2. Problemas dos Sistemas de Arquivos

A utilização de sistemas de arquivos convencionais do sistema operacional para armazenar dados organizacionais traz diversas limitações, principalmente à medida que o volume de informações e a quantidade de usuários aumentam.

Os principais problemas são:

- **Redundância e inconsistência de dados:** Como diferentes setores da organização desenvolvem seus próprios programas e arquivos, a mesma informação acaba sendo duplicada em vários locais. Isso desperdiça armazenamento e leva a inconsistências, pois a atualização feita em um arquivo pode não se refletir nos demais.
- **Dificuldade no acesso aos dados:** No sistema de arquivos não existe uma linguagem declarativa de consulta (como o SQL). Qualquer nova necessidade de informação ou relatório exige que um programador escreva um programa específico do zero para recuperar os dados.
- **Isolamento de dados:** Os dados ficam dispersos em múltiplos arquivos que podem ter formatos e estruturas incompatíveis, tornando muito trabalhoso cruzar informações vindas de diferentes fontes.
- **Problemas de integridade:** As regras de negócio (por exemplo, impedir saldo negativo ou exigir dados obrigatórios) precisam ser escritas dentro do código de cada programa de aplicação. Se uma nova regra for criada, todos os programas precisam ser atualizados manualmente, aumentando o risco de erros.
- **Problemas de atomicidade:** Um sistema de arquivos não trata operações compostas como atômicas ("tudo ou nada"). Se ocorrer uma falha elétrica ou travamento no meio de uma gravação, o arquivo pode ficar corrompido ou gravado apenas pela metade, sem recurso nativo de reversão (*rollback*).
- **Anomalias no acesso concorrente:** Quando vários usuários tentam atualizar o mesmo arquivo simultaneamente, o sistema de arquivos não oferece controle transacional fino. Uma gravação pode sobrescrever a outra, causando perda de dados (*lost updates*).
- **Problemas de segurança:** O controle de permissões de sistemas de arquivos atua em nível de arquivo ou diretório, sendo muito difícil definir regras de segurança mais granulares (como restringir acesso a determinados campos ou registros sensíveis para certos usuários).

