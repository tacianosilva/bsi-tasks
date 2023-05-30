
# Tarefa 02 - Modelo Relacional e Regras de Conversão

Aluno: Thomas Almeida
GitHub: tgo-mas
E-mail: talmeidasf@gmail.com

a. O modelo Relacional é a primeira representação do projeto de banco de dados no nível lógico. Organizado em tabelas representando as entidades e os relacionamentos do projeto, o modelo Conceitual também introduz ao projeto as chaves primárias e estrangeiras, que são de importância fundamental no funcionamento do Banco de Dados e as interações entre os dados em si.

b. As restrições de integridade do modelo Relacional podem ser de três tipos: a integridade de Chave garante que cada tupla do banco tenha atributos que a identifiquem e diferenciem do resto, sendo este geralmente uma chave primária; a integridade de Entidade garante que nenhum atributo de chave primária seja nulo; e a integridade Referencial diz respeito à capacidade de uma tabela referenciar outra, por meio de uma chave estrangeira, que corresponde ao valor de uma chave primária da tabela referenciada.

c. 1 - Toda entidade regular do modelo ER vira uma tabela, na qual seus atributos compostos serão convertidos em simples e uma chave estrangeira será criada baseada no atributo identificador da entidade.
2 - Para cada entidade fraca, é criada uma relação com todos os atributos da entidade da qual ela depende, mais seus próprios atributos. A chave da tabela da entidade fraca é a chave da entidade forte mais a chave da entidade fraca.
3 - Para relacionamentos 1:1, escolhe-se arbitrariamente uma das entidades para abrigar a chave estrangeira - composta da chave primária da outra entidade -, e demais atributos que este relacionamento pode originar.
4 - Para relacionamentos 1:N, identifica-se a relação com maior cardinalidade (o lado do N) para abrigar a chave estrangeira, que referencia a entidade que só possui uma ocorrência. Além disso, os atributos do relacionamento ficam nesta mesma relação.
5 - Para relacionamentos N:M, criamos uma nova tabela, na qual a chave primária será a combinação das chaves das duas tabelas envolvidas na relação. Nesta tabela também constam quaisquer atributos gerados deste relacionamento.
6 - Para atributos multivalorados, outra relação é criada, com uma chave estrangeira referenciando a entidade ou relacionamento ao qual pertence. Sua chave primária é a combinação da chave estrangeira mais o atributo multivalorado em si.
7 - Para relações de especialização existem várias técnicas de conversão para o modelo Relacional. Os casos podem depender, mas eu prefiro a criação de múltiplas relações, uma para cada tipo específico da entidade especificada.

d. Diagrama ER: [![](https://mermaid.ink/img/pako:eNqlVMFuozAQ_RXL57YfwI02VEqblIhkLyukamRcOlrwINtUWgX-fU2BEmISbXc5wZs3ZubNGx-5oEzygEu9Qsg1lKli7tmE93ESHuJkHbNjD3WPsRpVzlwO5sR2z17EYF6Ahyoq5QSuwEqWgYUHjSCAPHpF2oKLXYpn0giNSxGpMqml8AM_ks0erfQTSsCiR1u_86a5u2satop2YXIIt9HLIWYB-0Al6gIy8hPaLuHIttH2PumoFWiLAqtBkgEfj40f3IlRR3MzeDVSL7LW-2XarKorM2L_NKRvCdouVNTQWZOCSGdSwQK3Ped-oJC31xJ6nacEMIYEjtQePtGkIJWjsqwEV303vCXvLgswGeQEBS0htPXcnZOvSVkN1hftjXQ55YyqjQO-Vu__FCtqbea_7B3me-adtNu7k7q7GjrQ7N3RCtDMjtkl8VN0iL9zP7iGNugsxR6f_2atvyRdK7dGF7QWRW0W7gItTV3Sxd0eLDT08LldxtQ468z32dlCn_NOdnUiporf8FK60WPmbtpPuVJu36WbIA_cawb6V8pT1Toe1Jb2v5XggdW1vOF15bqUw93MgzcojEMrUD-Jxu_2Dxzdv9U?type=png)](https://mermaid.live/edit#pako:eNqlVMFuozAQ_RXL57YfwI02VEqblIhkLyukamRcOlrwINtUWgX-fU2BEmISbXc5wZs3ZubNGx-5oEzygEu9Qsg1lKli7tmE93ESHuJkHbNjD3WPsRpVzlwO5sR2z17EYF6Ahyoq5QSuwEqWgYUHjSCAPHpF2oKLXYpn0giNSxGpMqml8AM_ks0erfQTSsCiR1u_86a5u2satop2YXIIt9HLIWYB-0Al6gIy8hPaLuHIttH2PumoFWiLAqtBkgEfj40f3IlRR3MzeDVSL7LW-2XarKorM2L_NKRvCdouVNTQWZOCSGdSwQK3Ped-oJC31xJ6nacEMIYEjtQePtGkIJWjsqwEV303vCXvLgswGeQEBS0htPXcnZOvSVkN1hftjXQ55YyqjQO-Vu__FCtqbea_7B3me-adtNu7k7q7GjrQ7N3RCtDMjtkl8VN0iL9zP7iGNugsxR6f_2atvyRdK7dGF7QWRW0W7gItTV3Sxd0eLDT08LldxtQ468z32dlCn_NOdnUiporf8FK60WPmbtpPuVJu36WbIA_cawb6V8pT1Toe1Jb2v5XggdW1vOF15bqUw93MgzcojEMrUD-Jxu_2Dxzdv9U)

Modelo Relacional: <img src="Conceitual - BD(T2).png">

Laboratorio(**codDepartamento**) -> Departamento(<u>codigo</u>)

Laboratorio(**matCoord**) -> Docente(<u>matricula</u>)

Laboratorio(**matViceCoord**) -> Docente(<u>matricula</u>)

MembroLaboratorio(**matricula**) -> Docente(<u>matricula</u>)

MembroLaboratorio(**matricula**) -> Discente(<u>matricula</u>)

MembroLaboratorio(**codLaboratorio**) -> Laboratorio(<u>codigo</u>)

Docente(**codDepartamento**) -> Departamento(<u>codigo</u>)

Projeto(**matOrientador**) -> Docente(<u>matricula</u>)

Projeto(**codLaboratorio**) -> Laboratorio(<u>codigo</u>)

Participacao(**matricula**) -> Docente(<u>matricula</u>)

Participacao(**matricula**) -> Discente(<u>matricula</u>)

Participacao(**codProjeto**) -> Projeto(<u>codigo</u>)
