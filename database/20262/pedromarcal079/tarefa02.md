# Q1 - O modelo de dados entidade-relacionamento foi desenvolvido para facilitar o projeto de banco de dados, permitindo especificação de um esquema que representa a estrutura lógica geral de um banco de dados. Descreva os três elementos básicos de um Modelo Entidade Relacionamento (MER). 

Os três elementos básicos do Modelo Entidade-Relacionamento (MER) são:

* **Entidades**: representam objetos, conceitos ou coisas do mundo real que possuem existência concreta ou abstrata e sobre os quais a organização precisa armazenar informações (ex.: Cliente, Aluno, Venda). No modelo, formam conjuntos de entidades com as mesmas propriedades.

* **Atributos**: são as características, propriedades ou dados específicos que qualificam e descrevem uma entidade ou um relacionamento (ex.: nome, CPF, data_nascimento). Entre eles, destaca-se o atributo identificador (chave), que distingue de forma única cada ocorrência.

* **Relacionamentos**: são as associações e conexões lógicas existentes entre duas ou mais entidades, representando como elas interagem dentro do contexto do negócio (ex.: o relacionamento Contrata entre a entidade Cliente e a entidade Projeto).

---

# Q2 - Pesquise sobre as várias notações possíveis para Diagramas ER e cite alguns exemplos de notações diferentes para o mesmo conceito (ex.: cardinalidade, entidade subordinada, etc.). 

As notações de Diagrama Entidade-Relacionamento mais comuns são a Notação de Chen, a Pé de Galinha (Crow’s Foot) e a UML. Embora usem símbolos visuais distintos, todas expressam os mesmos conceitos:

* **Cardinalidade**:

    * Chen: Usa números e letras nas pontas das linhas conectadas a um losango (1:N ou (0, n)).

    * Crow's Foot: Usa símbolos gráficos nas pontas das linhas, como traços duplos (exatamente um) ou pontas ramificadas (muitos/pé de galinha).

    * UML: Usa intervalos numéricos próximos às entidades (1..*, 0..1).

* **Entidade Fraca (Subordinada)**:

    * Chen: Retângulo com borda dupla conectado a um losango com borda dupla.

    * Crow's Foot: Linha contínua (relacionamento identificador) ligando a entidade pai à filha, contrapondo linhas tracejadas de entidades normais.

    * UML: Linha com um losango preto preenchido (Composição) na classe pai.

* **Atributos**:

    * Chen: Elipses (círculos/ovais) ligadas à entidade por linhas, com a chave sublinhada.

    * Crow's Foot e UML: Listados diretamente em compartimentos dentro da caixa da entidade, indicados com marcações como PK.