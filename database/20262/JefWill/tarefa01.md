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

## Q3. Propriedades ACID

O conceito de transação em bancos de dados representa uma unidade lógica de processamento que inclui uma ou mais operações de acesso e modificação (como leituras e gravações). Para que o sistema garanta confiabilidade e precisão mesmo diante de falhas ou acessos concorrentes, as transações devem respeitar as propriedades **ACID** (**A**tomicidade, **C**onsistência, **I**solamento e **D**urabilidade):

### Atomicidade (Atomicity)
A atomicidade determina que a transação é indivisível e funciona sob a regra do "tudo ou nada". Ou todas as operações que compõem a transação são executadas com êxito (*commit*), ou nenhuma alteração é aplicada ao banco, revertendo qualquer modificação parcial já realizada (*rollback*).

- **Exemplo prático (transferência bancária):** Uma transferência de R$ 200,00 da Conta A para a Conta B exige duas etapas: subtrair R$ 200,00 do saldo da Conta A e adicionar R$ 200,00 ao saldo da Conta B. As duas etapas precisam ser concluídas juntas.
- **Se o SGBD não garantisse:** Se o sistema sofrer uma pane logo após subtrair o valor da Conta A, mas antes de somar na Conta B, o dinheiro seria retirado de A sem jamais chegar a B, sumindo do sistema.

### Consistência (Consistency)
A consistência assegura que a execução de uma transação leve o banco de dados de um estado válido a outro estado igualmente válido, respeitando todas as regras de integridade, restrições e regras de negócio predefinidas.

- **Exemplo prático (transferência bancária):** Se a Conta A possui saldo de R$ 100,00 e o banco proíbe saldo negativo (sem cheque especial), uma tentativa de transferência de R$ 200,00 deve ser barrada. Além disso, a soma total dos saldos do banco antes da transferência deve ser exatamente a mesma após a operação (conservação do valor monetário).
- **Se o SGBD não garantisse:** A transação poderia deixar a Conta A com saldo negativo não permitido ou gerar discrepâncias na soma total das contas, corrompendo a integridade contábil do banco.

### Isolamento (Isolation)
O isolamento garante que transações executadas simultaneamente não interfiram umas nas outras. O resultado obtido com transações concorrentes deve ser exatamente o mesmo que seria obtido se elas fossem executadas de forma sequencial (uma após a outra).

- **Exemplo prático (transferência bancária):** Suponha que a Conta A tenha R$ 300,00 de saldo. Ao mesmo tempo, um cliente tenta transferir R$ 200,00 pelo aplicativo enquanto um débito automático de R$ 200,00 é processado. O SGBD deve isolar as operações para que a segunda transação veja o saldo atualizado após o término da primeira.
- **Se o SGBD não garantisse:** As duas transações poderiam ler o mesmo saldo de R$ 300,00 ao mesmo tempo. Ambas autorizariam a saída de R$ 200,00, permitindo a retirada de R$ 400,00 de uma conta que possuía apenas R$ 300,00 (anomalia de perda de atualização ou leitura inconsistente).

### Durabilidade (Durability)
A durabilidade garante que, assim que uma transação for confirmada (*commit*), as alterações realizadas tornam-se permanentes e não serão perdidas por nenhuma falha posterior do sistema (como queda de energia ou travamento do servidor).

- **Exemplo prático (transferência bancária):** Uma vez que a transferência é finalizada e o comprovante é emitido na tela do cliente, os dados do débito e do crédito já foram gravados de forma segura em armazenamento persistente (disco e logs de transação).
- **Se o SGBD não garantisse:** Uma queda de energia logo após a confirmação da operação poderia apagar os dados da memória volátil, fazendo com que a transferência "desaparecesse" e o saldo retornasse ao valor anterior à transação após a reinicialização do servidor.

## Q4. Cenários envolvendo ACID

### a) Queda de energia no meio de uma transferência deixou o valor debitado da conta de origem, mas não creditado na conta de destino.

A propriedade diretamente envolvida é a **atomicidade**.

A transferência precisa ser tratada como uma única operação indivisível (tudo ou nada). O débito e o crédito precisam acontecer juntos. Como a energia caiu no meio do processo, a transação foi concluída apenas pela metade. Nesse caso, o SGBD deve desfazer o débito (*rollback*) para não deixar a operação incompleta. 

Também existe relação com a **consistência**, pois a soma total dos valores no sistema ficaria incorreta enquanto a operação não fosse desfeita.

### b) Dois atendentes debitam, ao mesmo tempo, o mesmo saldo de uma conta.

A propriedade diretamente envolvida é o **isolamento**.

As duas transações estão acontecendo de forma simultânea e precisam ser controladas pelo SGBD para que uma não interfira na outra. Sem o devido isolamento, os dois atendentes poderiam ler o mesmo saldo antes que o outro debitasse, provocando uma atualização perdida (*lost update*) e permitindo uma retirada de valor maior do que o saldo realmente disponível.

### c) O sistema confirma a operação, mas após reiniciar o servidor o dado foi perdido.

A propriedade diretamente envolvida é a **durabilidade**.

A partir do momento em que o sistema confirma para o usuário que a transação foi concluída (*commit*), as alterações devem ser salvas de forma permanente em disco. Se o servidor for reiniciado e a alteração for perdida, significa que o SGBD falhou em garantir a durabilidade da transação.

### d) Uma transferência que levaria o saldo abaixo do limite permitido é rejeitada pelo banco.

A propriedade diretamente envolvida é a **consistência**.

O banco possui uma regra de negócio que determina que o saldo não pode ficar abaixo de determinado limite. A função da consistência é garantir que o banco só passe de um estado válido para outro estado válido, fazendo com que o SGBD rejeite qualquer operação que viole essas regras.

## Q5. Recuperação, integridade, redundância e inconsistência

### Recuperação

A recuperação diz respeito à capacidade do SGBD de restaurar o banco de dados para um estado consistente e correto após a ocorrência de alguma falha (como pane no sistema operacional, erro de software ou queda repentina de energia).

O SGBD gerencia a recuperação utilizando logs de transação (*write-ahead logging*), pontos de controle (*checkpoints*) e backups periódicos. Quando o sistema reinicia após uma falha, o SGBD analisa os logs para desfazer as transações que não foram concluídas (*undo*) e reaplicar as alterações daquelas que já haviam sido confirmadas (*redo*).

### Integridade

A integridade está relacionada à garantia de que as informações armazenadas no banco sejam precisas, válidas e sigam as regras estabelecidas pelo modelo de dados e pelo domínio da aplicação.

O SGBD gerencia a integridade através de restrições (*constraints*), como:
- **Chaves primárias:** garantem que cada registro seja único e identificável;
- **Chaves estrangeiras:** garantem a integridade referencial entre tabelas relacionadas;
- **Restrições de tipo e domínio:** impedem valores nulos indevidos (`NOT NULL`), valores repetidos (`UNIQUE`) ou dados fora de um padrão aceito (`CHECK`).

### Redundância

Redundância acontece quando o mesmo dado é armazenado de forma repetida e desnecessária em vários locais do banco de dados, o que causa desperdício de espaço de armazenamento e aumenta o risco de falhas em atualizações.

O SGBD e os projetistas gerenciam e minimizam a redundância por meio de uma boa modelagem conceitual e relacional, aplicando técnicas de **normalização** de dados. Nos casos em que a redundância é necessária (como em replicações para distribuição de carga e alta disponibilidade), o próprio SGBD se encarrega de sincronizar os dados entre os servidores.

### Inconsistência

Inconsistência ocorre quando existem informações divergentes ou contraditórias sobre um mesmo fato ou entidade dentro do banco de dados. Ela é quase sempre consequência da redundância descontrolada (por exemplo, o telefone de um cliente ser alterado em uma tabela de pedidos, mas permanecer antigo no seu cadastro geral).

O SGBD gerencia a inconsistência aplicando o controle de concorrência entre transações simultâneas, garantindo as propriedades ACID e exigindo o cumprimento das restrições de integridade referencial. Com isso, nenhuma alteração parcial é permitida e os dados mantêm a sua coerência.

## Q6. Mini-projeto conceitual

O modelo conceitual a seguir descreve a estrutura de banco de dados para uma empresa de desenvolvimento de software que atende outras empresas como clientes e organiza o trabalho por meio de equipes multidisciplinares (*squads*).

### a) Entidades

As principais entidades envolvidas são:

- **Cliente:** empresas que contratam os serviços de desenvolvimento de software.
- **Projeto:** projetos de software contratados pelos clientes.
- **Squad:** equipes responsáveis pelo planejamento e execução técnica.
- **Membro:** profissionais que compõem as squads (desenvolvedores, testadores, líderes técnicos, supervisores e gerentes de produto).
- **Tarefa:** demandas, issues, novas funcionalidades ou correções de bugs a serem implementadas.
- **Sprint:** períodos ou iterações de tempo fixo para execução das tarefas de um projeto.
- **Release:** versões entregáveis de software disponibilizadas para o cliente.

### b) Principais atributos

#### Cliente
- `id_cliente`
- `razao_social`
- `nome_fantasia`
- `cnpj`
- `email_contato`
- `telefone`

#### Projeto
- `id_projeto`
- `nome`
- `descricao`
- `data_inicio`
- `data_previsao_fim`
- `status` (ex.: em planejamento, em andamento, concluído)

#### Squad
- `id_squad`
- `nome`
- `data_criacao`
- `ativa`

#### Membro
- `id_membro`
- `nome`
- `email`
- `cargo` (ex.: desenvolvedor, testador, líder técnico, supervisor, gerente de produto)
- `data_admissao`

#### Tarefa
- `id_tarefa`
- `titulo`
- `descricao`
- `tipo` (ex.: feature, bug, teste, documentação)
- `prioridade` (ex.: baixa, média, alta, crítica)
- `status` (ex.: a fazer, em andamento, em revisão, concluída)
- `pontos_estimados`
- `data_criacao`
- `data_conclusao`

#### Sprint
- `id_sprint`
- `numero_sprint`
- `objetivo`
- `data_inicio`
- `data_fim`
- `status` (ex.: planejada, em andamento, encerrada)

#### Release
- `id_release`
- `versao` (ex.: v1.0.0)
- `data_lancamento_planejada`
- `data_lancamento_real`
- `notas_da_versao`
- `status`

### c) Relacionamentos e cardinalidades

- **Um cliente pode ter vários projetos**, mas cada projeto pertence a um único cliente.
- **Um projeto pode ter várias squads atuando nele**, e uma squad pode atuar em múltiplos projetos ao longo do tempo.
- **Uma squad é composta por vários membros**, mas cada membro está alocado em uma única squad em determinado período.
- **Um projeto pode ter várias tarefas**, e cada tarefa está obrigatoriamente associada a um único projeto.
- **Um projeto é dividido em várias sprints**, mas cada sprint pertence a um único projeto.
- **Uma sprint agrupa várias tarefas**, enquanto uma tarefa pode estar associada a uma sprint (ou aguardar no backlog do projeto).
- **Um projeto pode gerar várias releases**, e cada release pertence a um único projeto.
- **Uma release reúne várias tarefas entregues**, indicando quais itens de trabalho foram publicados naquela versão.
- **Uma squad é responsável por várias tarefas**, e cada tarefa possui uma squad responsável por sua execução.
- **Um membro pode ser o responsável direto por várias tarefas**, enquanto uma tarefa pode ter um membro atribuído como responsável.

### d) Regras de integridade

Em linguagem natural, o banco de dados deve assegurar as seguintes regras e restrições:

1. Todo identificador principal (`id_cliente`, `id_projeto`, `id_squad`, `id_membro`, `id_tarefa`, `id_sprint`, `id_release`) deve ser único.
2. Campos essenciais de identificação e contato (como `cnpj` do cliente e `email` dos membros) não podem se repetir no sistema.
3. Todo projeto deve estar obrigatoriamente associado a um cliente existente.
4. Toda tarefa deve estar obrigatoriamente vinculada a um projeto e a uma squad responsável.
5. Uma tarefa só pode ser alocada em uma sprint que pertença ao mesmo projeto da tarefa.
6. Cada squad deve possuir obrigatoriamente apenas um membro com a função de Líder Técnico como responsável técnico da equipe.
7. A data de início de uma sprint deve ser obrigatoriamente anterior à sua data de término.
8. A data de previsão de fim de um projeto não pode ser anterior à sua data de início.
9. Em um mesmo projeto, não podem existir duas releases com o mesmo número de versão.
10. Uma tarefa não pode ser registrada com status de concluída sem que possua uma data de conclusão devidamente registrada.
