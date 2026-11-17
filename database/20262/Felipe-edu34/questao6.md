Mini-Projeto Conceitual: Empresa de Desenvolvimento de Software
a) Principais Entidades
Cliente: Organização que contrata a empresa de desenvolvimento para a criação ou manutenção de sistemas.

Projeto: Iniciativa de software desenvolvida para atender às demandas de um cliente específico.

Squad: Equipe multidisciplinar alocada para realizar o trabalho nos projetos.

Membro: Colaborador da empresa (desenvolvedores, testadores, líderes técnicos, supervisores e gerentes de produto) integrante de um squad.

Sprint: Iteração com tempo determinado para o planejamento e execução de um conjunto de atividades do projeto.

Tarefa (Issue): Unidade básica de trabalho resolvida pelos membros dentro de uma sprint.

Release: Versão entregue e disponibilizada do software gerada a partir do progresso do projeto.

b) Principais Atributos de Cada Entidade
Cliente: ID do Cliente, Nome, CNPJ, E-mail de Contato, Telefone.

Projeto: ID do Projeto, Nome do Projeto, Descrição, Data de Início, Data de Término Prevista, Status.

Squad: ID do Squad, Nome da Equipe, Especialidade/Foco.

Membro: ID do Membro, Nome Completo, E-mail, Papel/Cargo (ex: Desenvolvedor, Testador, Líder Técnico, Supervisor, Gerente de Produto).

Sprint: ID da Sprint, Número/Nome da Sprint, Data de Início, Data de Término, Meta da Sprint.

Tarefa: ID da Tarefa, Título, Descrição, Status (ex: A Fazer, Em Progresso, Concluído), Prioridade, Estimativa de Horas.

Release: ID da Release, Versão, Data de Lançamento, Notas de Versão (Release Notes).

c) Relacionamentos e Cardinalidade
Cliente e Projeto (1:N): Um cliente pode possuir vários projetos ao longo do tempo, mas cada projeto pertence obrigatoriamente a um único cliente.

Projeto e Sprint (1:N): Um projeto é dividido em várias sprints, mas cada sprint está vinculada a um único projeto.

Projeto e Release (1:N): Um projeto pode gerar várias releases ao longo do seu ciclo de vida, mas cada release pertence a um único projeto.

Squad e Projeto (N:M): Um squad pode atuar em múltiplos projetos, assim como um projeto pode ser atendido por um ou mais squads ao longo do tempo.

Squad e Membro (1:N): Um squad é composto por vários membros, mas cada membro está alocado em um único squad de cada vez.

Sprint e Tarefa (1:N): Uma sprint contém várias tarefas planejadas, mas cada tarefa pertence a uma única sprint.

Membro e Tarefa (1:N): Um membro pode ser responsável por várias tarefas, mas cada tarefa possui um único membro responsável principal.

d) Regras de Integridade (Restrições) em Linguagem Natural
Apenas um membro com o papel de líder técnico (ou supervisor/gerente) pode estar associado a essa função de liderança ativa dentro de um mesmo squad.

Toda tarefa criada precisa estar obrigatoriamente vinculada a uma sprint válida e a um projeto correspondente.

Todo projeto deve estar associado obrigatoriamente a um cliente cadastrado e ativo no sistema.

A data de término de uma sprint nunca pode ser anterior ou igual à sua data de início.

Uma tarefa não pode ser atribuída a um membro que pertença a um squad diferente daquele que está executando a sprint correspondente.