# TAREFA 01 - CONCEITOS DE BD, ACID E SGBD
---
**Nome:** Gleydson Henrique Dantas da Silva  
**Github:** Gleydson-HDS  
---
**QUESTÃO 01 - Descreva o que é um Banco de Dados e o que é um Sistema Gerenciador de Banco de Dados. Cite exemplos de Bancos de Dados e seus SGBDs.**  
- Um Banco de Dados representa um sistema organizado para armazenar, gerenciar e recuperar dados de um progama. Um exemplo é o Banco de Dados de uma escola, que pode armazenar informações sobre alunos, professores, funcionários, disciplinas, etc. O SGBD (Sistema de Gerenciamento de Banco de Dados) representam os softwares que irão realizar a manipulação dessas informações, como por exemplo o PostgreSQL e o Oracle.
---
**QUESTÃO 02 - Quais os principais problemas de utilizar Sistemas de Arquivos para armazenagem de dados?**  
- Um dos principais problemas em utilizar Sistemas de Arquivos para o armazenamento de dados está na sua ineficiência de busca, sua falta de integridade, dificuldade de acesso, falta de segurança, redundância de dados e dificuldade de compartilhamento e recuperação dos mesmos. 
---
**QUESTÃO 03 - Explique as propriedades ACID: atomicidade, consistência, isolamento e durabilidade. Para cada propriedade, descreva um exemplo prático no contexto de uma transferência bancária e explique o que aconteceria se o SGBD não garantisse essa propriedade.**  

- Atomicidade: Transações são executadas totalmente ou desfeitas, como um conjunto. Em uma transferência bancária o valor debitado da conta de origem deve ser creditado na conta destino, ocorrendo a transferência de uma para a outra. Se essa propriedade não fosse garantida, o dinheiro poderia ser retirado da primeira conta sem chegar à segunda.
  
- Consistência: Mudança para um estado válido, íntegro, após a realização de uma transição. Após uma transferência, ambos os saldos da conta de origem e de destino devem ser atualizados. Sem essa propriedade, os saldos poderiam ficar incorretos.

- Isolamento: Transações são tratadas de forma independente, de forma que não haja conflitos por concorrência. Se duas transferências forem realizadas ao mesmo tempo, o SGBD deve garantir que cada operação seja processada corretamente sem interferir na outra. Sem isolamento, uma transferência poderia utilizar um saldo desatualizado e causar erros.

- Durabilidade: Transações que já persistiram na base não serão desfeitas por erros futuros. Depois que uma transferência for confirmada, ela deve continuar registrada no banco de dados mesmo após uma falha ou queda de energia. Sem essa propriedade, a transferência poderia ser perdida mesmo tendo sido confirmada.
---
**QUESTÃO 04 - Para cada cenário abaixo, indique qual(is) propriedade(s) ACID está(ão) em jogo e justifique sua resposta: a) Queda de energia no meio de uma transferência deixou o valor debitado da conta de origem, mas não creditado na conta de destino. b) Dois atendentes debitam, ao mesmo tempo, o mesmo saldo de uma conta. c) O sistema confirma a operação, mas após reiniciar o servidor o dado foi perdido. d) Uma transferência que levaria o saldo abaixo do limite permitido é rejeitada pelo banco.**  
- a) Atomicidade, pois devido a queda de energia a transição ficou incompleta, a atomicidade garante que o débito seja desfeito nesse caso.  

- b) Isolamento, pois representa o controle para que transações simultâneas não interfiram entre si.
  
- c) Durabilidade, pois é necessário que os dados sejam armazenados em caso de interrupção na operação.  

- d) Consistência, pois garante que o banco de dados permaneça de acordo com suas regras e restrições.
---
**QUESTÃO 05 - Um SGBD trata dos seguintes aspectos: recuperação, integridade, redundância e inconsistência. Explique cada um deles e descreva como o SGBD os gerencia.**  
- Recuperação: permite recuperar os dados após falhas, usando backup e registros do sistema.
- Integridade: garante que os dados estejam corretos e válidos, usando regras e restrições.
- Redundância: evita a repetição desnecessária dos mesmos dados, economizando espaço.
- Inconsistência: evita que existam dados diferentes ou conflitantes. O SGBD controla as alterações para manter os dados corretos e iguais quando necessário.
---
**QUESTÃO 06 - Considere o cenário de uma empresa de desenvolvimento de software que atende outras empresas como clientes. A empresa organiza seu trabalho em squads (equipes) compostas por desenvolvedores, testadores, líder técnico, supervisor e gerente de produto. Cada squad resolve tarefas (issues) e planeja releases, testes e o cronograma de sprints (iterações) dos projetos de cada cliente.**

**Sem utilizar SQL, elabore um mini-projeto conceitual do banco de dados dessa empresa, deixando claro: a) As principais entidades envolvidas (clientes, squads, membros, tarefas, projetos, sprints, releases). b) Os principais atributos de cada entidade. c) Os relacionamentos entre as entidades (com a cardinalidade, ex.: "um cliente pode ter vários projetos"). d) Em linguagem natural, as regras de integridade (restrições) que o banco de dados deveria garantir, ex.: "apenas um líder por squad", "toda tarefa precisa estar vinculada a um projeto".**  

- a) Entidades  
    Cliente: empresa que contrata o serviço.  
    Projeto: projeto desenvolvido para um cliente.  
    Squad: equipe responsável pelo projeto.  
    Membro: pessoa que trabalha em uma squad.  
    Tarefa (Issue): atividade que precisa ser realizada.  
    Sprint: período de trabalho da equipe.  
    Release: versão do projeto que será entregue.  

- b) Atributos  
    Cliente: código_cliente, nome, CNPJ, contato.  
    Projeto: código_projeto, nome, descrição, status.  
    Squad: código_squad, nome.  
    Membro: código_membro, nome, e-mail, cargo.  
    Tarefa: código_tarefa, título, descrição, prioridade, status.  
    Sprint: código_sprint, nome, data inicial, data final.  
    Release: código_release, versão, data de entrega, status.  

- c) Relacionamentos e cardinalidades  
    Um cliente pode ter vários projetos, mas cada projeto pertence a um cliente.  
    Um projeto pode ter uma ou mais squads, e uma squad pode trabalhar em vários projetos.  
    Uma squad possui vários membros, e um membro pertence a uma squad.  
    Um projeto possui várias tarefas, e cada tarefa pertence a um projeto.  
    Uma sprint possui várias tarefas, e uma tarefa pode participar de uma sprint.  
    Um projeto possui várias releases, e cada release pertence a um projeto.  
    Uma squad planeja várias sprints e releases.  

- d) Regras de integridade  
    Todo projeto deve estar vinculado a um cliente.  
    Toda tarefa deve estar vinculada a um projeto.  
    Toda sprint deve ter uma data inicial anterior à data final.  
    Uma squad deve ter pelo menos um desenvolvedor.  
    Cada squad deve ter apenas um líder técnico.  
    Um membro não pode pertencer a duas squads ao mesmo tempo.  
    Toda release deve estar vinculada a um projeto.  
    Os códigos de clientes, projetos, squads, membros, tarefas, sprints e releases devem ser únicos.  
    Uma tarefa não pode ser concluída sem estar vinculada a uma sprint.  
---

