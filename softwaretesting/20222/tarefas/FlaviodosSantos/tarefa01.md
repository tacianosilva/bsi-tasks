# Tarefa 01 - Teste de Unidade

- Nome: Flavio Roberto
- Github: FlaviodosSantos
- e-mail: flaviovorthrox@yahoo.com.br

---

<br>

## Testes unitários, o que são ?

Os testes unitários são essenciais. Sem eles, você está pisando sobre casca de ovos o tempo todo.

O teste unitário consiste em verificar o comportamento das menores unidades em sua aplicação.

Tecnicamente, isso seria uma classe ou até mesmo um método de classe em línguas orientadas a objetos, e seria um procedimento ou função em línguas processuais e funcionais.

Os testes unitários precisam funcionar isoladamente porque precisam funcionar rapidamente.

Todo o conjunto de testes unitários de uma aplicação precisa funcionar em minutos, de preferência em segundos. Você verá o porquê mais tarde.

É por isso que os testes unitários não podem utilizar nenhum processo ou sistema externo. Nenhuma operação de E/S (input/output) de qualquer tipo (banco de dados, arquivo, console, rede) exceto o registro de falhas nos testes e talvez a leitura da configuração padrão de alternância de recursos no início de uma execução de teste.

Se seu código de teste (ou as bibliotecas que utiliza) fizer E/S ou acessar qualquer coisa fora de seu processo, não é um teste unitário, e sim um teste de integração.

[link](https://www.digite.com/pt-br/agile/testes-unitarios/#:~:text=O%20que%20%C3%A9%20Teste%20de%20Unit%C3%A1rio%3F,em%20l%C3%ADnguas%20processuais%20e%20funcionais.)

<br>

## Linguagem escolhida : Javascript

JavaScript é uma linguagem de programação que permite a você implementar itens complexos em páginas web — toda vez que uma página da web faz mais do que simplesmente mostrar a você informação estática — mostrando conteúdo que se atualiza em um intervalo de tempo, mapas interativos ou gráficos 2D/3D animados, etc. — você pode apostar que o JavaScript provavelmente está envolvido. É a terceira camada do bolo das tecnologias padrões da web, junto com HTML e CSS.

- HTML é a linguagem de marcação que nós usamos para estruturar e dar significado para o nosso conteúdo web. Por exemplo, definindo parágrafos, cabeçalhos, tabelas de conteúdo, ou inserindo imagens e vídeos na página.

- CSS é uma linguagem de regras de estilo que nós usamos para aplicar estilo ao nosso conteúdo HTML. Por exemplo, definindo cores de fundo e fontes, e posicionando nosso conteúdo em múltiplas colunas.

- JavaScript é uma linguagem de programação que permite a você criar conteúdo que se atualiza dinamicamente, controlar múltimídias, imagens animadas, e tudo o mais que há de intessante. Ok, não tudo, mas é maravilhoso o que você pode efetuar com algumas linhas de código JavaScript.

[link](https://developer.mozilla.org/pt-BR/docs/Learn/JavaScript/First_steps/What_is_JavaScript)

<br>

## Framework de teste: QUnit

QUnit é uma estrutura de teste JavaScript poderosa e fácil de usar. Ele foi originalmente desenvolvido para o projeto jQuery e desde então evoluiu para ser uma dependência de muitas bibliotecas e aplicativos JavaScript modernos, inclusive sendo a estrutura de teste padrão para o ecossistema Ember.js .

### Filosofia

A filosofia do QUnit como uma estrutura de teste se resume a três locatários principais: Easy , Universal e Extensible .

### Fácil

O QUnit deve ser fácil de usar do início ao fim. Configurar seu primeiro teste com deve ser super simples, exigindo o mínimo de sobrecarga possível. Então, enquanto você está desenvolvendo, quando um teste ou afirmação falha, o QUnit deve fornecer feedback o mais rápido possível, com detalhes suficientes para descobrir rapidamente o problema subjacente. E deve fazê-lo sem interromper ou corromper outros testes.

Além disso, o QUnit deve ser rápido para facilitar aos desenvolvedores a confiança de que colocar seus testes em seu caminho crítico não os atrasará.

### universal

O QUnit deve ser universalmente aplicável para testar o código JavaScript e oferecer suporte a muitos ambientes diferentes. JavaScript pode ser executado no navegador, em threads de trabalho e no servidor, assim como o QUnit para que você possa testar seu código no mesmo ambiente em que ele será executado; o ambiente onde você precisa ter confiança de que funciona.

### Extensível

O QUnit deve ser opinativo com uma API enxuta para oferecer suporte a ser fácil de usar, mas altamente extensível. Existem muitas abordagens diferentes para testes e muitos tipos diferentes de testes que os usuários podem querer escrever e, embora não possamos oferecer suporte a todos eles, podemos oferecer suporte a APIs para permitir que a comunidade estenda o QUnit para atender às suas necessidades.

[link](https://qunitjs.com/)
