<h1>"Tarefa 02 - Modelo Relacional e Regras de Conversão"
Nome: Ericleison Camilo Silva de Holanda
GitHub: github.com/Ericleisonn
E-mail: ericleison.camilo.124@ufrn.edu.br



No Modelo Relacional, os dados são organizados em tabelas(relações). Cada tabela é composta por linhas e colunas. As linhas, também conhecidas como tuplas, representam as instâncias ou registros dos dados, enquanto as colunas representam os atributos ou campos dos dados. Cada tabela no Modelo Relacional possui um nome exclusivo, e é composta por uma ou mais colunas. Cada coluna tem um nome único e define o tipo de dados que pode ser armazenado nela, como números, strings ou datas.

No Modelo Relacional, as restrições de integridade são utilizadas para garantir a consistência e a validade dos dados armazenados em um banco de dados. Essas restrições ajudam a preservar a integridade dos relacionamentos entre as tabelas, bem como a precisão e a coerência dos dados.

    1.Restrição de Chave Primária: Essa restrição garante que a chave primária de uma tabela seja única e não nula. Ela evita a duplicação de dados e garante que cada tupla da tabela seja identificada de forma exclusiva.
    2. Restrição de Chave Estrangeira: Essa restrição estabelece a integridade referencial entre duas tabelas relacionadas. Ela garante que os valores da chave estrangeira em uma tabela correspondam aos valores existentes na chave primária da tabela referenciada.
    3. Restrição de Integridade de Domínio: Essa restrição define os domínios de valores válidos para os atributos de uma tabela. 
    4.Restrição de Integridade de Valor Único: Essa por sua vez, garante que os valores de uma coluna, ou combinação de colunas, sejam exclusivos em uma tabela. Ela impede a existência de duplicação de valores nessas colunas (causando redundância).


Conjunto de regras para efetuar o mapeamento entre modelo ER e modelo Relacional:
Regra 1: Entidades Regulares 
    Para cada entidade regular E no esquema E-R, criamos uma relação R que inclui os atributos simples de E
    Para cada atributo composto de E incluímos somente os seus atributos simples
    Escolhemos uma das chaves candidatas de E para ser a chave primária de R

Regra 2: Entidades Fracas
    Para cada entidade fraca W,  com entidade forte E, no esquema E-R, criamos  uma relação R e incluímos todos os atributos simples de W como atributos de R
    Incluímos como atributos da chave estrangeira de R os atributos que compõem a chave primária da entidade forte E
    A chave primária de R é a combinação da chave primária da entidade forte E e a chave da entidade fraca W

Regra 3: Relacionamentos 1:1 == (1,1) : (1,1)
    Identificamos as relações S e T que correspondem às entidades que participam do relacionamento
    Escolhemos uma das relações, digamos S, e incluímos como chave estrangeira em S a chave primária de T. É melhor escolher para desempenhar o papel de S, a entidade que tenha participação total no relacionamento
    Incluímos todos os atributos simples do relacionamento 1:1 como atributos de S

Regra 4: Relacionamentos 1:N que não envolvem entidades fracas
    Identificamos a relação S que representa a entidade que participa do lado N do relacionamento
    Incluímos como chave estrangeira em S, a chave primária da relação T que representa a outra entidade (lado 1) que participa do relacionamento
    Incluímos qualquer atributo simples do relacionamento 1:N em S

Regra 5: Relacionamento N:M
    Criamos uma nova relação S para representar o relacionamento
    Incluímos como chave estrangeira em S as chaves primárias das relações que participam do relacionamento. A combinação destas chaves formará a chave primária da relação S
    Incluímos qualquer atributo do relacionamento N:M em S
    Nota: Podemos mapear um relacionamento 1:1 ou 1:N de maneira similar ao M:N. Isto é usado quando existem poucas instâncias do relacionamento, evitando valores nulos nas chaves estrangeiras

Regra 6: Atributos Multivalorados
    Criamos uma nova relação R que inclui o atributo multivalorado A mais a chave primária K da relação que representa a entidade (ou relacionamento) que tem A como atributo
    A chave primária de R é a combinação de A e K
    Se o atributo multivalorado é composto => incluir seus componentes atômicos

===========================================================================================






