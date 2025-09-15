# Tarefa 01 - Conceitos BD e MER

## Nome: Luiz Henrique Felix Guedes
## Usuário Github: [LuizFelixDev](https://github.com/LuizFelixDev)
## E-mail: luiz.henrique.felix@ufrn.edu.br

### Banco de Dados(BD)
Um Banco de Dados é uma coleção organizada de dados inter-relacionados. Ele foi projetado para armazenar e gerenciar grandes volumes de dados de forma eficiente, permitindo fácil acesso, manipulação e atualização. Os dados são estruturados de maneira lógica para que possam ser consultados e utilizados por diferentes aplicações.

### Sistema Gerenciador de Banco de Dados (SGBD)
Um SGBD (Sistema Gerenciador de Banco de Dados) é um software que permite aos usuários interagir com um banco de dados. Ele gerencia o armazenamento, a recuperação e a segurança dos dados. O SGBD atua como uma interface entre o usuário (ou a aplicação) e o banco de dados, garantindo a integridade e a consistência dos dados.

ex:MySQL, PostgreSQL, Oracle, MongoDB e MariaDB.

### Problemas em sistemas de arquivos
Os principais problemas de utilizar sistemas de arquivos para armazenagem de dados são: dificuldade de acesso e consulta, já que não há uma linguagem estruturada; redundância e inconsistência, pois os mesmos dados podem se repetir em arquivos diferentes; falta de integridade e segurança, com ausência de mecanismos robustos de controle; e, por fim, dificuldade de escalabilidade e manutenção conforme o volume de dados cresce.


### Modelo Entidade-Relacionamento (MER)
O Modelo Entidade-Relacionamento (MER) é uma ferramenta de design que simplifica a criação de bancos de dados ao focar em seus componentes essenciais. Seus três elementos básicos são: entidades, que representam objetos ou conceitos do mundo real (ex: 'Cliente'); atributos, que são as propriedades que descrevem uma entidade (ex: 'nome' e 'endereço' do cliente); e relacionamentos, que conectam duas ou mais entidades, definindo como elas se interagem (ex: 'faz_pedido' entre 'Cliente' e 'Produto').

### Notações de Diagramas Entidade-Relacionamento
Os Diagramas Entidade-Relacionamento (ER) são essenciais para projetar bancos de dados, mas a forma como são desenhados pode mudar bastante dependendo da notação utilizada. As três notações mais comuns são a de Chen, a de Pé de Galinha (Crow's Foot) e a UML, cada uma com sua própria simbologia. A notação Chen é a clássica e acadêmica, usando retângulos para entidades, losangos para relacionamentos e elipses para atributos. Já a notação Pé de Galinha é a mais popular no mercado de desenvolvimento de software por ser concisa e visualmente clara, especialmente para mostrar a cardinalidade. Por fim, a UML (Linguagem de Modelagem Unificada) utiliza diagramas de classes que podem ser adaptados para o ER, representando entidades como classes e os relacionamentos como associações. Para a cardinalidade, por exemplo, a notação de Chen utiliza números (1, N), a de Pé de Galinha usa símbolos gráficos como o "pé de galinha" para o lado "muitos" do relacionamento, e a UML emprega anotações como 1 e *. Essa variedade de notações permite que os projetistas escolham a mais adequada para o contexto, seja para um projeto conceitual, uma implementação prática ou uma integração com o desenvolvimento orientado a objetos.