### Link para o README:
##### <https://github.com/GuilhermeAngelo/bsi-tasks/blob/master/softwaretesting/20222/GuilhermeAngelo/README.md>

# Tarefa 01 - Teste de Unidade

##### nome: Guilherme Angelo de Medeiros 
##### Usuário github: GuilhermeAngelo 
##### e-mail: guilhermeangelo2001@gmail.com

## Testes de Unidade
##### O Teste de software é uma forma de avaliar a qualidade da aplicação e reduzir o risco de falhas. Testar não consiste apenas em executar testes, mas também, em planejar, analisar, modelar e implementar. Ele também abrange as etapas de verificação(se os requisitos foram atendidos) e validação(Se o sistema atenderá às necessidades do usuário e de outras partes interessadas)  do desenvolvimento da aplicação.

##### Com isso, podemos observer que o teste de software é constituído por diversas áreas, com funções distintias, entretanto, com o mesmo objetivo(Manter a qualidade da aplicação). Entre os tipos de testes existentes temos  o teste de unidade. ELe Consiste em validar dados válidos e inválidos sendo aplicado por desenvolvedores ou analistas de teste. Uma unidade é a menor parte testável de um programa de computador(uma classe por exemplo no paradigma de orientação a objetos). Em programação procedural, uma unidade pode ser uma função individual ou um procedimento. Idealmente, cada teste de unidade é independente dos demais, o que possibilita ao programador testar cada módulo isoladamente.
    
## Linguagem de programação

#### A tarefa foi realiza usando o Django. O Django é um framework escrito em python para desenvolvimento web. O teste serão realizados no próprio Django, pois o mesmo fornece um framework de teste com uma baixa hierarquia de classes construida na biblioteca padrão unittest de Python. 

##### ![Python](https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/community/logos/python-logo-only.png)

## Framework de teste

##### Como foi citado anteriormente, Usaremos o as prórias ferramentas de de testes já integradas ao Django. Apesar do nome, o framework oferece métodos capazes de realizar teste de unidade e integração. Permitindo a simulação de entrada de dados, inspeções e saidas da sua aplicação. Além disso, ele oferece uma API e ferramentas para usar em diferentes frameworks de testes.

### Links

#### <https://developer.mozilla.org/pt-BR/docs/Learn/Server-side/Django/Testing>
#### <https://docs.djangoproject.com/pt-br/1.11/internals/contributing/writing-code/unit-tests/>
#### <https://imasters.com.br/back-end/realizando-testes-em-seus-aplicativos-django>
#### <http://waltercruz.github.io/django-l10n-portuguese/topics/testing.html>

## Ferramentas de debug

### VISUAL STUDIO CODE
#### A IDE que utilizo é o VISUAL STUDIO CODE. Ela é uma ótima interface de desenvolvimento, pois fornece multiplos recursos que auxiliam o desenvilvedor a produzir de forma mais dinâmica e fácil. Além disso, esse editor de código tem suporte para as principais plataforma ou sistemas operacionais, e oferece ferramentas de depuração, controle de versionamento git, complementação de código, entre outras funcionalidades.

#### O VS Code oferece ótimas ferramentas de debug, entre elas o DataTip, QuickWatch dialog,Parallel Watch Window, entre outras funcionalidades. O DataTip serve para inspecionar variáveis, entretanto, pode deixar a desejar nos casos que a mesmas possuem muitas propriedades. Para esses cenários o QuickWatch é recomendado. Uma janela é aberta com todos os detalhes das variaveis. O da Parallel Watch Window objetivo é auxiliar o debug de processos que estão em paralelo. Ela identifica e monitora uma variável através de várias Threads. O visual studio code oferece outras ferramentas que não foram citadas.

## Links Crud e Testes

### Link para o tutorial - crud: 

#### Webdesign em Foco: <https://www.youtube.com/watch?v=-vrXnewHrwA&list=PLbnAsJ6zlidvszSXnxplfYgtB6KQ-fZ-N>

#### Esse link nos direciona para um playlist do canal Webdesign em Foco. Ela é composta por um conjunto de videos que nos ensina desde de como iniciar nosso projeto e app usando o Django e de como criarmos um Crud de um sistema de automóveis, usando o sqlite ou o mySql para realizarmos o armazenamento dos dados, e de como interagir com os respectivos banco de dados. O tutorial também ensina um pouco de funciona o Django, por exemplo de como criar templates, views e urls nas nossas aplicações web. Além de como usar um pouco o bootstrap para estilização das nossas páginas do crud. Também nos ensina como passar e utilizar parâmetros vindos de requisições.

### Links para o tutorial - testes no Django: 

#### pythonando: <https://www.youtube.com/watch?v=cEXt8hDyKQw>
#### Cryce Truly: <https://www.youtube.com/watch?v=Ob8_UAgEK5w>
#### The Dumbfounds: <https://www.youtube.com/playlist?list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM>

## Experiência na implementação do crud e testes:

#### Foi uma experiência desafiadora, porem bem satisfatória. Nunca havia possuido nenhum contado com o Django, mas gostei bastante por sua simplicidade e funcionalidade. O Django apresenta uma abordagem diferente para o desenvolvimento das aplicações web, e pela falta de experiêcia o processo acabou sendo um pouco demorado, tanto no desenvolvimento do crud, quanto dos testes. Em relação aos teste, inicialmente, não sabia o que e como testar as funcionalidades, mas com os tutoriais e textos na internet as coisas se esclareceram um pouco. Um ponto positivo do Django em relação aos teste é que nativamente ele já possui uma "ferramenta de testes" baseada na biblioteca padrão unittest, o que para facilita para realização de alguns testes, sem necessitar de outro framework para realizar os mesmos.

### LinK para o repositório: <https://github.com/GuilhermeAngelo/Crud_Django>

## Moks Objects:

### O moks objects são objetos que imitam objetos reais para testes, e eles podem ser criados através de frameworks. Em relação aos testes unitários, os moks objects eles podem simular o comportamento de objetos reais com maior complexidade, principalmente quando os objetos são difíceis de serem incorporados dentro dos testes de unidade. Eles também são usados em objetos com geram resultados variados, objetos com estado difíceis de serem produzidos ou reproduzidos, objetos que necessitam de uma inicialização previa, entre outros tipos que objetos que podem ter seus comportamentos alterados. Uma das limitações dos Mocks é quando é o excesso de objetos Mocks como parte de um conjuto testes, pois quando há modificações no código é preciso fazer um grande número de modificações nos testes, além disso, manutenções incorretas podem gerar erros que podem passar dispercebidos. Isso ocorre pois os Moks não respeitam muito um dos princípios GRASP, chamado baixo acoplamento, aumentando o número de dependências com a implementação atual do objeto e isso pode ocasionar com uma futura modificação do mesmo a quebra do teste já implementado.