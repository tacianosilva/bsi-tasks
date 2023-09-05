# Tarefa 01 - Teste de Unidade

Repositório utilizado para as tarefas do componente curricular 'Testes de Software'. #72
 
Discente: Raquel Lima Fernandes  
Matrícula: 20190012546   
E-mail: raquel.lima.072@ufrn.edu.br  
Repositório do projeto: https://github.com/fernandesraquel/PetControl.git

# Testes de Software

Os testes de software são uma parte fundamental do desenvolvimento de software, e entre os diversos tipos de testes, os testes de unidade são essenciais. Os testes de unidade são um nível de teste que se concentra em avaliar individualmente pequenas partes do código, como funções ou métodos, para garantir que eles funcionem corretamente e produzam os resultados esperados. 

# Tecnologias utilizadas

<details>
    <summary>
        <font style="vertical-align: inherit;"> </font>
        <font style="vertical-align: inherit;">Dart e Flutter</font>  
    </summary>
    <br>
    <p>
Dart é uma linguagem de programação versátil e dinâmica, desenvolvida pela Google. Ela oferece um equilíbrio entre simplicidade e flexibilidade, o que a torna acessível tanto para desenvolvedores iniciantes quanto experientes. Uma característica notável é o sistema de tipagem estática, que verifica os tipos de dados em tempo de compilação, evitando muitos erros comuns antes mesmo da execução.

Dart é especialmente conhecida pelo seu suporte à programação assíncrona, permitindo que os desenvolvedores criem aplicativos responsivos e eficientes que lidam de maneira eficaz com operações de entrada/saída, como chamadas de rede e acesso a bancos de dados. A flexibilidade de Dart também permite que você adote diferentes paradigmas de programação, tornando-a uma escolha robusta para uma variedade de projetos.

Flutter é um framework de código aberto baseado em Dart, desenvolvido pela Google. Ele revoluciona a maneira como aplicativos são construídos, oferecendo uma abordagem única para o desenvolvimento de interfaces de usuário, compartilhando um código-base entre diferentes plataformas. Com Flutter, os desenvolvedores podem criar aplicativos móveis nativos, web e desktop, tudo a partir da mesma base de código.

A característica distintiva do Flutter é a sua arquitetura de widgets personalizáveis e altamente flexíveis. Os widgets no Flutter não são apenas elementos visuais, mas também componentes funcionais que representam a estrutura e o comportamento do aplicativo. Isso permite uma personalização profunda e a criação de interfaces de usuário altamente interativas e dinâmicas.

Além disso, o Flutter oferece ferramentas de teste robustas e um ecossistema em crescimento de pacotes e plugins, que facilitam tarefas como a integração de APIs, gerenciamento de estado e muito mais. Sua capacidade de compilação Just-in-Time (JIT) para desenvolvimento rápido e Ahead-of-Time (AOT) para desempenho otimizado também fazem dele uma escolha poderosa para criar aplicativos de alta qualidade.

Aqui estão algumas das principais ferramentas de teste para Dart:
    </p>
    <ul dir="auto">
        <li>
             Test: A própria biblioteca de testes "test" é fornecida com o Dart SDK. Ela oferece suporte para testes unitários e de integração, permitindo que você escreva e execute testes para verificar a funcionalidade das partes individuais do seu código.
        </li>
        <li>
            Flutter Test: Se você estiver desenvolvendo com o Flutter, a biblioteca de teste "flutter_test" é a escolha natural. Ela estende a biblioteca "test" e oferece recursos específicos para testar widgets e interações do Flutter.
        </li>
        <li>
            Mockito: O "mockito" é uma biblioteca de mocks para Dart que ajuda a criar objetos simulados (mocks) de dependências externas durante os testes. Isso é útil para isolar o comportamento da unidade sendo testada.
        </li>
        <li>
        Integration_test: Para testes de integração mais complexos e de ponta a ponta, você pode usar a biblioteca "integration_test". Ela permite simular interações do usuário e testar o fluxo completo do aplicativo.
        </li>
        <li>
        BLoC Test: Se você estiver usando o padrão BLoC para gerenciamento de estado em seu aplicativo Flutter, a biblioteca "bloc_test" oferece utilitários específicos para testar BLoCs.
        </li>
        <li>
        Golden Toolkit: O "golden_toolkit" é uma ferramenta que ajuda a fazer testes de regressão visual em widgets Flutter. Isso é útil para garantir que as alterações no layout não causem problemas visuais indesejados.
        </li>
    </ul>
</details>


# IDE que será utilizada

A IDE utilizada será o VISUAL STUDIO CODE. O Visual Studio Code, ou simplesmente VS Code é um editor de código-fonte desenvolvido pela Microsoft para Windows, Linux e macOS. Ele inclui suporte para depuração, controle de versionamento Git incorporado, realce de sintaxe, complementação inteligente de código, snippets e refatoração de código.

# Ferramentas de debug

Debug é o processo que envolve identificar, isolar e corrigir os erros ou anormalidades de um software. A priore a ferramenta de debug utilizada será uma extensão do prórrio vscode o DataTip pela natureza da sua facilidade. Basta parar em um breakpoint, passar o mouse sobre alguma variável e ele mostrará.