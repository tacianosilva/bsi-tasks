# Tarefa 02 - Modelo Relacional e Regras de Conversão

**Nome:** Victor Ryan

**Github:** https://github.com/VictorRyan3612

**Email:** vitorsilva3612@gmail.com
##



### Questão 7a
A aparencia do modelo relacional é parecida com tabelas e planhilhas do excel, porem a sua diferença está nas relações entre colunas linhas e outras tabelas.

### Questão 7b
Integridade de Chave:
Cada linha, ou tupla, da tebela, ou relação, tem um conjunto único de atributos que a identifica, não podendo ter outra tupla com o mesmo conjunto de atributos.

Integridade de Entidade:
As chaves primárias, atributos importantissimos das relações, não podem ser nulas.

Integridade Referencial:
Uma certa Chave primária de uma certa relação, pode ser chamada de chave estrangueira em outras tebelas, permitindo assim, uma conexão entre tabelas.



## Questão 7c
As regras de conversões para Modelo Entidade-Relacionamento (MER) para Modelo Relacional (MR).

### Regra 1 Entidade Regulares:
Cada entidade vira uma tabela
Chave primária MER vira chave primária MR
atributos viram atributos.


### Regra 2 Entidades fracas
entidade Fraca [W] e entidade forte [E]
A tabela de [W] recebe: 
Chave primária própria composta das duas chaves primárias;
atributos simples de [W]; chave estrangeira [E].


### Regra 3 1:1
Escolhemos duas entidades [S] E [T] 
De preferencia e se possível [S] deve ser a entidade de participação total no relacionamento (1,1), e [T] a não total (0,1)

A Entidade [S] recebe chave estrangeira de [T]
Atributos: atributos de [S] e Atributos do relacionamento entre ambas.


## Regra 4 1:n sem entidades fracas

Tabela com a entidade n chama-se [S], recebe chave estrangeira da entidade com cardinalidade 1 [T].

Tabela [S] recebe atributos do relacionamento.


## Regra 5 n:m

Cria-se uma nova tabela para representar esse relacionamento, Vira uma tabela nova [S] com atributos: 

As chaves primárias das duas entidades que participam do relacionamento, viram chaves estrangeiras em [S], em seguida a junção dessas duas chaves vira a chave primária de [S].


## Regra 6 Atributos multivalorados 
Cria-se uma nova tabela [R]
Identifica a entidade ou relacionamento [S] que contém o atributo multivalorado [A] e chave primária [K]

Nova tabela [R] terá os atributos:

Chave primária composta [A_K], Chave primária da tabela [S]([K]), atributo multivalorado [A]

Se o atributo multivalorado é composto => incluir seus componentes atômicos.

## Regra 7 Herença

o primeiro passo é converter cada especialização com m
subclasses {S1,S2,...,Sm} e superclasse C, cujos
atributos são {k, a1,..., an} onde k é a chave
primária, em esquemas de relações usando uma
das seguintes opções:

### A: 
Fazer tabela C usando a regra 1, tendo seus atributos
Fazer uma tabela para cada subclasse usando a regra 1, tendo seus atributos 
a chave primária da tabela C e demais será a chave primária da entidade C.

### B:
Não terá a relação C
Tabela para cada subclasse [Si]
Atributos: chave primária de C, atributos de C, atributos de Si.

### C:
Uma única tabela com todos os campos de C e Si, com tais atributos podendo serem vazios

Atributos: chave, todos os atributos de C, todos os atributos das subclasses
há o caso excepcional das subclasses serem disjuntas, nesse caso, terá um atributo que indica o tipo da subclasse.

### D:
Única tabela com todos os atributos das subclasses
atributos: chave, todos os atributos de C, todos os atributos das subclasses e um atributo boolean para cada subclasse

Essa opção é usada para especialização cujas subclasses são sobrepostas.




# Questão 7D

### i

![Diagram_MER](https://uploaddeimagens.com.br/images/004/473/112/full/Chen_Erd.jpg?1684450370)



### ii

![Diagram_MER](https://uploaddeimagens.com.br/images/004/473/118/full/Chen_Erd.jpg?1684450653)



### iii
![Diagram_MER](https://uploaddeimagens.com.br/images/004/473/128/full/Chen_Erd.jpg?1684451277)


### iv

![Diagram_MER](https://uploaddeimagens.com.br/images/004/473/151/full/Chen_Erd.jpg?1684452142)



### v
![Diagram_MER](https://uploaddeimagens.com.br/images/004/473/180/full/Chen_Erd_v.jpg?1684452939)


### vi

![Diagram_MER](https://uploaddeimagens.com.br/images/004/473/187/full/Chen_Erd.jpg?1684453139)



### vii

![Diagram_MER](https://uploaddeimagens.com.br/images/004/473/190/full/Chen_Erd.jpg?1684453438)



### viii

![Diagram_MER](https://uploaddeimagens.com.br/images/004/473/211/full/Chen_Erd.jpg?1684454261)



## Final

![Diagram_MER](https://uploaddeimagens.com.br/images/004/473/294/full/Chen_Erd.jpg?1684459210)




## Questão 7d parte 2
* Como o markdawn do github e vscode não tem sublinhado, tomei a liberdade de substituir por italico


LABORATORIO(*codigo*, silga, nome, 
dataCriacao, portaria de criacao, descricao,
endereco, site, email, departamento, **ID_cordenador**, **ID_vice**,**cod_dep**,)

DEPARTAMENTO(*codigo*, sigla, nome, enredeco, site)

COORDENADOR(*ID*, dataInicio, dataFim, **matri_docente**)

VICE_COORDENADOR(*ID*, dataInicio, dataFim, **matri_docente**)

MEMBROS(*ID*, horarioSemanal, cargaHoraria)

MEMBRO_ALUN (*matriAlun_IdMembro* ,**matri_alun**, **ID_membro** )

MEMBRO_LAB(*IdMem_codLab*, **ID_membro**, **cod_lab**)

MEMBRO_DOC (*IdMem_matriDoc*, **ID_membro**, **matri_doc**)

ALUNOS(*matricula*, nome, email, curso)

DOCENTES(*matricula*, nome, areaAtuacao, dataContratacao, formacao, **cod_dep**)

PARTICIPACAO_PROJETO(*ID*, cargaHoraria, **cod_proj**, **matri_alun**, **matri_doc**)

PROJETO(*codigo*, sigla, nome, docenteLider, descricao, dataInicio, dataConclusao, resumo, **cod_lab**)

##
### Conexões entre relações
LABORATORIO(ID_cordenador) → COORDENADOR(ID)
LABORATORIO(ID_vice) → VICE_COORDENADOR(ID)
LABORATORIO(cod_dep) → DEPARTAMENTO(codigo)

COORDENADOR (matri_docente) → DOCENTES(matricula)
VICE_COORDENADOR(ID) → DOCENTES(matricula)


MEMBRO_ALUN(matri_alun) → ALUNOS(matricula)
MEMBRO_ALUN(ID_membro) → MEMBROS(ID)

MEMBRO_LAB(ID_membro) → MEMBROS(ID)
MEMBRO_LAB(ID_membro) → LABORATORIO(codigo)

MEMBRO_DOC(ID_membro) → MEMBROS(ID)
MEMBRO_DOC(ID_membro) → DOCENTES(matricula)


DOCENTES(cod_dep) → DEPARTAMENTO(codigo)
PARTICIPACAO_PROJETO(cod_proj) → PROJETO(codigo)
PARTICIPACAO_PROJETO(matri_alun) → ALUNOS(matricula)
PARTICIPACAO_PROJETO(matri_doc) → DOCENTES(matricula)

PROJETO(cod_lab) → LABORATORIO(codigo)
