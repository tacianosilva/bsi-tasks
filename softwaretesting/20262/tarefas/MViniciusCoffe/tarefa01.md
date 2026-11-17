# Tarefa 01 - Teste de Unidade, Integração, Cobertura e CI
### Aluno: Marcus Vinícius de Souza Azevedo.
### User: MViniciusCoffe
### E-mail: vinicius.azevedo.123@ufrn.edu.br
### Link do repositório: https://github.com/MViniciusCoffe/SpendSmart
---

## Questões objetivas:
1. Quando colocamos uma aplicação no mundo real, na maioria das vezes não conseguimos prever quais serão todas as interações o usuário terá com ele, o sistema pode não conseguir responder como deveria a partir de um uso inesperado, causando falhas catastróficas de segurança, quebra da integridade das informações, corrupção de arquivos e entre outros bugs. Os testes surgiram justamente para mitigar esse "tiro no escuro" no lançamento de seu software, pois é a partir dele que testamos quais entradas devem ser possíveis ou não (inputs), e quais saídas são esperadas (outputs) ou não, fazemos isso tanto de forma automatizada como manual, onde a forma automatizada simula várias interações, corretas ou incorretas (caixa preta/partição) ou simula também de forma a testar cada linha do código individualmente (caixa branca/estrutural). Esses testes se subdividem em 3 categorias principais, testes de unidade, integração e de sistemas, como forma de pirâmide (Ou troféu em versões mais atualizadas), onde os testes de unidade ficam na base, e os testes de sistema no topo. Os testes de unidade servem para testar a menor unidade do sistema: Os módulos (como funções/métodos de classes, ou as próprias classes específicas), servindo como base das funcionalidades mais avançadas que iremos montar. Testes de unidade podem ser tanto caixa branca ou de caixa preta, e devem ser automatizados ao máximo, dependências externas devem ser "mockadas". Para isso foram criados frameworks de testes, como Jest. A partir dos testes de unidade, testamos como eles se integram em uma funcionalidade maior por meio de testes de integração.
2. A linguagem de programação escolhida foi Javascript, principalmente por ser o padrão global para desenvolvimento web e pelos seus frameworks flexíveis e poderosos. O Javascript é acompanhado de uma stack formada por:
- Frontend:
  - React
  - Vercel (Hospedagem)
- Backend:
  - Cors
  - Express
  - dotEnv
  - jsonWebToken
  - pg
  - postgreSQL (Via supabase)
  - Node.js
  - Vercel (Hospedagem, antes era AWS por meio do AWS RDS)
- Testes:
  - Jest
- Monitoramento:
  - Github Actions (Pipeline ci/cd)
  - Sonar (Monitoramento da cobertura de testes)
- DevDependencies
  - Nodemon
  - Prettier
3. O framework escolhido foi o jest. Sua escolha foi motivada pelo fato de ser um framework de testes criado pela Meta para ser usado com o React, assim oferecendo uma maior integração com o framework web. Além disso, o Jest oferece uma série de ferramentas, como a utilização de mocks por padrão, foco na simplicidade (zero-config), flexibilidade e em sua ampla utilização no mercado. Para mais informações: [Jest](https://jestjs.io/pt-BR/)
4. Utilizo o VSCode pelo GitHub Codespaces diretamente no navegador, ou seja, uma versão completa do Visual Studio Code diretamente na nuvem. Sendo a versão completa, todos os recursos que tem no desktop também estão disponíveis no codespaces (Só alterando algumas teclas de atalho), incluindo os de testes, como gerenciamento e breakpoints, painéis de inspeção laterais, controle de depuração (Debug console), além de configurações adicionais no launch.json
- Gerenciamento de breakpoints: Clicando a margem esquerda dos números das linhas
  - Breakpoints comuns pausam o código assim que a linha é atingida
  - Breakpoints condicionais só pausam se uma condição for verdadeira
  - Hit count breakpoints pausam a linha após ser executadas um número x de vezes
  - Logpoints não pausam a aplicação, apenas imprimem uma mensagem no menu
- Painéis de inspeção geral: Quando seu código atinge um breakpoint, um painel a esquerda é desbloqueado para analise o estado da aplicação, aqui você avalia:
  - Variáveis: Seu valor no escopo atual, permitindo alterar seus valores inclusive
  - Vigia: Permite adicionar variáveis e expressões que você quer monitorar ao longo de todo fluxo
  - Pilhas de chamadas: Mostra o caminho que seu código percorreu (teste estrutural de fato)
- Controles:
  - f5: Continua até o próximo breakpoint
  - alt f10: executa próxima linha sem entrar em funções internas
  - alt f11: Entra na função que está na linha atual para debugar seu interior
  - shift f11: Sai da função e volta para quem chamou
  - ctrl shift f5: Reinicia a sessão do zero
- Console: No terminal inferior, é possível encontrar um debug console onde você pode digitar qualquer código de linguagem válido enquanto o programa está pausado para analisar variáveis, testar o tempo e rodar funções de teste
5. O vídeo escolhido foi [Testes no React com Jest & Testing Library | Guia Completo](https://www.youtube.com/watch?v=0hVXjqHwvI0) do canal Felipe Rocha, eu achei um tutorial bem interessante e completo, com um conteúdo e linguagem fáceis de serem absorvidos, apesar do vídeo ser longo. O conteúdo do vídeo primeiramente se passa na explicação teórica do que são testes e como eles funcionam, quais as suas utilidades, os seus tipos entre outros, depois, é mostrado um exemplo no repositório [react-testing-video](https://github.com/felipemotarocha/react-testing-video). Apesar dele focar mais na aplicação dos testes do que no CRUD em si, ainda assim trabalha temas muito importantes para a nossa disciplina, como:
- Conteúdo teórico básico para testes
- Prática usando react, passando por algumas das etapas de testes (Unitário e Integração)
- Testes de requisições com API e usa alguns mocks (através do MSW e do jest.fn)
- Apresenta o Jest e RTL (react testing library)
- Mostra como testar operações assíncronas e como forçar erros para testar se as mensagens saem corretamente

Como complemento ao tutorial de testes, este é um tutorial sobre como fazer um CRUD rapidamente pelo React usando o comando `$ yarn create vite`: https://www.youtube.com/watch?v=FqbgZ3lwGnM do canal Will Dev. Juntos, os dois tutoriais apresentam a construção de um CRUD e a aplicação de testes de software. Um resumo dos principais pontos dos vídeos inclui:
- Construção de uma tela básica de listagem de usuários com nome e e-mail, com botões de atualização e exclusão, com um modal para os dois e validação de duplicidade
- Setup com vite e template react, com chakra UI
- Construção do componente com mudanças de estado e persistência com LocalStorage
- Listagem responsiva e demonstração da remoção de itens

6. Mock Objects (Ou apenas mocks) são objetos que simulam o como objetos reais devem se comportar de forma controlada, sendo usados principalmente para isolar a unidade que você está testando de suas dependências externas. Existem 4 motivos principais para usarmos mocks:
- Isolamento: Garante que o código não quebre só por que a API está fora do ar ou que o banco caiu
- Velocidade: Conectar a bancos as vezes consome mais tempo, e testes de unidade precisam ser rápidos
- Previsibilidade: Você consegue forçar um mock a simular cenários difíceis no mundo real
- Stateless: Um teste nunca deve salvar dados reais, ou enviar e-mails de verdade, ou descontar de cartões de crédito de verdade.
