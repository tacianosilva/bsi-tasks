<h1>Tarefa 01 - Conceitos BD e MER
</h1>
° Leonardo Alves </br>
° leonardobezrr </br>
° leonardobezerra05@gmail.com</br></br>
a) Descreva o que é um Banco de Dados e o que é um Sistema Gerenciador de Banco de Dados. Cite exemplos de Bancos de Dados e seus SGBDs.
</br><strong>
    Um banco de dados pode ser considerado um conjunto de dados organizados, com o intuito de promover facilidade para o usuário na hora de buscar por algum dado.</br>
    Um SGBD é um software desenvolvido para manipular, gerenciar e criar bancos de dados. Ele é utilizado para garantir que o acesso aos dados sejam seguros, eficientes e precisos. O SGBD permite que o usuário altere, pesquise ou até mesmo recupere infomações do banco de dados.</br>
    Ex.:</br>
    ° MySQL</br>
    ° Oracle</br>
    ° Microsoft, Microsoft SQL server
</strong></br></br>

b)Quais os principais problemas de utilizar Sistemas de Arquivos para armazenagem de dados.</br><strong>
    Um dos principais problemas em usar os de Sistemas de Arquivos para armazenagem de dados é a redundância dos mesmos, pois cada arquivo é tratado separadamente, implicando em uma grande possibilidade dos dados serem replicados. Além disso, qualquer pessoa que possua acesso ao sistema de arquivos pode visualizar, editar e excluir os mesmos, ou seja, há um falta de segurança. Ademais, eles possuem uma escalabilidade limitada.
</strong></br></br>
c)O modelo de dados entidade-relacionamento foi desenvolvido para facilitar o projeto de banco de dados, permitindo especificação de um esquema que representa a estrutura lógica geral de um banco de dados. Descreva os três elementos básicos de um Modelo Entidade Relacionamento (MER).</br><strong>
Três elementos básicos de um Modelo Entidade Relacionamento:</br>
° Entidade -> Pode ser descrito como um objeto ou conceito no mundo real que pode ser descrito e identificado</br>
° Atributo -> Pode ser descrito como um característica ou propriedade de uma entidade que descreve as informações armazenadas sobre ela</br>
° Relacionamento -> Pode ser descrito como uma associação entre duas ou mais entidades que reflete a maneira como elas estão relacionadas entre si
</strong>
</br></br>
d)Pesquise sobre as várias notações possíveis para Diagramas ER, cite alguns exemplos de notações diferentes para o mesmo conceito (ex: Cardinalidade, Entidade Subordinada, etc).</br>
<strong>
° Notação de Peter Chen -> Utiliza de retângulos para representar entidades, diamantes para representar relacionamentos e setas para indicar a direção do relacionamento, sejam eles de grau binário (envolva duas entidades) ou de grau "n" (envolva várias entidades)</br>
° Notação de Bachman -> Utiliza de uma representação gráfica semelhante à um fluxograma. Enquanto as entidades são representadas com caixas retangulares, os relacionamentos são representados por linhas conectando as caixas. Essa noção também inclui símbolos para representar os tipos de relacionamentos.</br>
</strong>
</br>
e)Construa um Diagrama ER para projetar uma base de dados de um Sistema de Controle de Freqüência de Empregados de uma organização. A base de dados não deve conter redundância de dados. O modelo ER deve ser representado com um diagrama usando Mermaid.js. O modelo deve apresentar, ao menos, entidades, relacionamentos, atributos, identificadores e restrições de cardinalidade. O modelo deve ser feito no nível conceitual, sem incluir chaves estrangeiras 