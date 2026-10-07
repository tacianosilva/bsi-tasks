CLIENTE

Codigo (Chave Primária - PK)
nome
email_contato

PROJETO

codigo (Chave Primária - PK)
nome
descricao
cliente_codigo (Chave Estrangeira - FK, referenciando CLIENTE)

SQUAD

codigo (Chave Primária - PK)
nome

FUNCIONARIO

codigo (Chave Primária - PK)
nome
email
papel
squad_codigo (Chave Estrangeira - FK, referenciando SQUAD)

SPRINT

codigo (Chave Primária - PK)
objetivo
data_inicio
data_fim
squad_codigo (Chave Estrangeira - FK, referenciando SQUAD)

TAREFA

codigo (Chave Primária - PK)
descricao
prioridade
situacao
estimativa_horas
projeto_codigo (Chave Estrangeira - FK, referenciando PROJETO)
sprint_codigo (Chave Estrangeira - FK, referenciando SPRINT)
squad_codigo (Chave Estrangeira - FK, referenciando SQUAD)

RELEASE

codigo (Chave Primária - PK)
versao
data_lancamento
cliente_codigo (Chave Estrangeira - FK, referenciando CLIENTE)
squad_codigo (Chave Estrangeira - FK, referenciando SQUAD)

TESTE_VALIDACAO

codigo (Chave Primária - PK)
tipo
resultado
release_codigo (Chave Estrangeira - FK, referenciando RELEASE)
RELEASE_TAREFA (Tabela Associativa gerada pelo relacionamento N:M entre RELEASE e TAREFA)
release_codigo (Chave Primária e Estrangeira - PK/FK, referenciando RELEASE)
tarefa_codigo (Chave Primária e Estrangeira - PK/FK, referenciando TAREFA)


