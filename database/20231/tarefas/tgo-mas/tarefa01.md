# Tarefa 01 - Conceitos BD e MER

Aluno: Thomas Almeida de Souza Farias <br/>
Github: tgo-mas <br/>
Email: talmeidasf@gmail.com

<hr />

a. Banco de Dados são estruturas organizadas estrategicamente para armazenar dados de um ou mais sistemas de forma eficiente e em esquemas, por exemplo o MySql, mongoDB, ou um gerenciamento em arquivo, que não é o ideal mas não deixa de ser um Banco. Já os SGBDs são sistemas complexos para possibilitar a criação e manutenção dos Bancos de Dados. Exemplos de SGBDs são o PostgreSQL, Oracle, MySql Workbench, etc.

b. Os sistemas de arquivos dificultam muitos processos utilizados nos BDs, como a busca, necessitando de algoritmos complexos para realizar buscas eficientes. Além disso, a separação e integridade dos dados é comprometida, estando geralmente armazenados de forma aleatória. Além disso, os riscos aumentam, como por exemplo o de perder os dados em algum prejuízo físico do armazenamento utilizado.

c. O modelo ER funciona em torno de três conceitos principais: Entidade, Relacionamento e Atributos. As entidades são objetos físicos ou lógicos que fazem parte do domínio do sistema. Toda entidade possui atributos, que são características pontuais dessa entidade. Os relacionamentos se estabelecem entre as entidades de acordo com suas relações no mundo real. Eles podem ter atributos também, e possuem cardinalidade.

d. Alguns diagramas ER são construídos com formas um pouco diferentes entre si. A principal diferença notável é nos atributos: muitos diagramas representam-os dentro de uma elipse, e seus nomes podem ou não estar sublinhados, no caso de ser uma chave; outros, usam um círculo vazio para atributos comuns, com seu nome ao lado, e círculos preenchidos para chaves. Além disso, há diferenças de notação na cardinalidade, podendo ser representada graficamente, nas ligações entre o relacionamento e a entidade, ou por números, nas formas (N,1), (1,1), (0,1), ou ainda apenas N, 1, ou 0. As entidades fracas também possuem notações diferentes, podendo ser um retângulo duplo, ou uma entidade comum com uma ligação mais espessa.

e. [![](https://mermaid.ink/img/pako:eNqNkkFugzAQRa9ieZ3kAOyQoBVqAihJq6hCQlOYglWwqTGLCnP3GghJC0itV-bN158_g1uaiBSpRVE6DDIJZcSJOe4hPLqPthOQdgT9YVwRI2eZIOHTHddKMp4RLkpcQCyBFSPt5s5a73Zak4e9e_Fe3D2xSGWyxDXKUXkrzCLkQkK9guKS8T9aeZdg2aaHWm-3uiWOZ8cn92D7tpEpCW9Q5DDK7qV2MeV_ltLNbcZQLTk_H_0-VSK4wuv6B9auuv3qMs0eIzdpU1ip1MAm3v0wnyYOA__cd5f42UwbGdjK0m8uEacbWqI0Pzc1b2eQRlTlaIallrmmID8iGvHO6KBR4vTFE2op2eCGNlUKCq-vjVrvUNSGVsBfhZi-u29IpMa9?type=png)](https://mermaid.live/edit#pako:eNqNkkFugzAQRa9ieZ3kAOyQoBVqAihJq6hCQlOYglWwqTGLCnP3GghJC0itV-bN158_g1uaiBSpRVE6DDIJZcSJOe4hPLqPthOQdgT9YVwRI2eZIOHTHddKMp4RLkpcQCyBFSPt5s5a73Zak4e9e_Fe3D2xSGWyxDXKUXkrzCLkQkK9guKS8T9aeZdg2aaHWm-3uiWOZ8cn92D7tpEpCW9Q5DDK7qV2MeV_ltLNbcZQLTk_H_0-VSK4wuv6B9auuv3qMs0eIzdpU1ip1MAm3v0wnyYOA__cd5f42UwbGdjK0m8uEacbWqI0Pzc1b2eQRlTlaIallrmmID8iGvHO6KBR4vTFE2op2eCGNlUKCq-vjVrvUNSGVsBfhZi-u29IpMa9)