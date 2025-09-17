# Tarefa 01- Conceitos de BD e MER <h1>
#### Nome: Júlia Lilian Prudêncio da Costa <h4>
#### Usuário Github: julia2000-git <h4> 
#### Email: julia.lilian.706@ufrn.edu.br <h4>

## Resolução dos Itens da Tarefa 01 <h2>

#### Item a. <h4>
# Um banco de dados é um conjunto organizado e estruturado de dados que possuem certas relações entre si, geralmente armazenado de forma eletrônica em um computador, podendo possuir dados em diferentes formatos, como texto, números, imagem e vídeos. Já um gerenciador de banco de dados é um software que permite realizar a criação, acesso, gerenciamento e manipulação de um banco de dados, funcionando como um intermediário entre o banco de dados e o usuário, garantindo a integridade dos dados e o seu armazenamento de forma segura. 
# Um exemplo bastante comum de banco de dados são os relacionais, que organizam dados inter-relacionados em tabelas estruturadas. Outro exemplo são os bancos de dados não-relacionais, que não armazenam os dados em tabelas, mas em outras estruturas, como grafos, pares de chave-valor, documentos etc.
# Como exemplos de SGBD, existem os relacionais, como o Oracle, muito utilizado em empresas de grande porte; MySQL, ideal para aplicações web; PostgresSQL, que possui código aberto; e existem não-relacionais, como o MongoDB, utilizado para armazenar dados em documentos; ou o Redis, para armazenar pares de chave-valor.

#### Item b. <h4>
# Existem problemas significativos na utilização de sistemas de arquivos para armazenar dados: permissão de acesso simultâneo de usuários aos dados bastante limitado, o que pode gerar o bloqueio do arquivo; a carência de propriedades importantes para a integridade das transações dos dados, como a atomicidade, a consistência, o isolamento e a durabilidade, ocasionando a perda ou inconsistência de dados; dificuldade para gerenciamento de backups em casos de grandes volumes de dados, podendo haver riscos de corrupção dos dados durante o processo, o que não o torna vantajoso para o aumento da escalabilidade dos dados; dificuldades na recuperação dos dados, por não estarem estruturados ou semiestruturados dentro dos arquivos; menor segurança, com maior risco de corrupções nos dados e de acesso não autorizado a dados sensíveis.

#### Item c. <h4>
# Os 3 elementos básicos de um MER são: Entidades, Atributos e Relacionamentos. As entidades são representações de objetos ou de conceitos do mundo real, sobre as quais se deseja guardar dados ou informações. Já os atributos são as características ou propriedades de uma entidade. Os relacionamentos, por sua vez, são as interações, relações ou associações existentes entre duas ou mais entidades.

#### Item d. <h4>
#  Em um diagrama ER, existem diferentes notações para representar os seus  elementos. As entidades são representadas por retângulos, sendo um retângulo normal para entidades fortes (independentes de outras e mais utilizadas), um retângulo dentro de outro para entidades fracas (dependentes de outras) e um losango dentro de um retângulo para entidades associativas (realizam associações entre as instâncias de diferentes entidades); os atributos normalmente são representados por figuras ovais, mas dependendo do tipo de atributo, as figuras ovais se diferenciam: um oval dentro de outro indica um atributo multivalorado (assume mais de 1 valor), e um oval tracejado indica um atributo derivado (cujo valor pode ser obtido a partir de outros atributos relacionados); os relacionamentos costumam ser representados por losangos e/ou linhas entre as entidades: um relacionamento comum (forte) é representado por um losango já um relacionamento fraco é representado por um losango dentro de outro; a cardinalidade pode ser representada por numerações, símbolos ou letras, como 0-1, 1-1, 0-N, 1-N, N-N. Também pode ser representada pela notação do desenho de "pés de galinha": o 1 é uma linha reta com um pequeno traço perpendicular à ela, o "muitos" (n) é uma linha com 3 "pés" no final, somente 1 é uma linha com dois traços perpendiculares, zero ou 1 é uma bolinha e um traço perpendicular à linha, 1 ou muitos é uma linha com o traço perpendicular e 3 traços formando os pés de galinha, zero para muitos é uma linha com a bolinha e os 3 pés. Esses são alguns exemplos das diferentes notações existentes.



