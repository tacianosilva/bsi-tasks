# Tarefa 02 - Modelo Relacional e Regras de Conversão

**Nome:** Victor Ryan
**Github:** https://github.com/VictorRyan3612
**Email:** vitorsilva3612@gmail.com
##



### 7a
A aparencia do modelo relacional é parecida com tabelas e planhilhas do excel, porem a sua diferença está nas relações entre colunas linhas e outras tabelas.

### 7b
Integridade de Chave:
Cada linha, ou tupla, da tebela, ou relação, tem um conjunto único de atributos que a identifica, não podendo ter outra tupla com o mesmo conjunto de atributos.

Integridade de Entidade:
As chaves primárias, atributos importantissimos das relações, não podem ser nulas.

Integridade Referencial:
Uma certa Chave primária de uma certa relação, pode ser chamada de chave estrangueira em outras tebelas, permitindo assim, uma conexão entre tabelas.



## 7c
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