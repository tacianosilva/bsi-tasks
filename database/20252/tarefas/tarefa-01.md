# Tarefa 01 - Conceitos BD e MER
## Riam Stefesom - riamxpp - riamstefeson616@gmail.com

*** a)  Banco de dados ***
  1. É uma relação de dados relacionados e armazenados em algum dispositivo. 
  2. Ele é independente dos sistemas de informção para os quais fornece dados.
*** Sistema Gerente de Banco de Dados (SGBD) *** 
  1. É um software utilizado para armazenar, organizar e manipular dados de maneiras eficiente e segura.

*** b)  Sistema de arquivos *** 
  1. Vários aplicações feitas por diferentes programadores realizavam acesso aos dados, eram criados novos arquivos de acordo com a necessidades que surgissem. 
  2. Inconsistência de redudância de dados.
    * Informações podem ser repetidas em diferentes arquivos;
    * As cópias podem divergir ao longo do tempo.
  3. Dificuldade de acesso aos dados. 
    * Uma solicitação de dados não prevista no sistema implica em separar dados manualmente ou solicitar ao departamento de PD uma nova aplicação.
  4. Isolamento de dados. 
    * Os vários arquivos de dados podem estar em formatos diferentes, isso dificulta a construção de aplicações.
  5. Problemas de integridades. 
    * Os valores armazenados devem obedecer restrições para manutenção de consistência;
    * Programadores poem essas restrições no código das aplicações, difícil adiconar novas retrições ou modificar restrições existentes.
  6. Problemas de atomicidade.
    * Determinadas operações devem acontecer em conjuntos;
    * A não realização de uma das operações implica na não relização de nenhuma delas (operação atômica);
    * Em caso de falha, deve-se garantir que o banco volte estado anterior da realização da operação.
  7. Anomalias no acesso concorrente.
    * Sistemas devem permitir atualizações simultâneas dos dados para melhorar o desempenho, no sistema de arquivos a interação entre essas atualizações concorrentes podem gerar incosistência de dados.
    * Supervisionar os dados com vários programas tendo acesso se torna uma tarefa difícil.
  8. Problemas de segurança.
    * Nem todos os usuários estão autorizados a acessar todos os dados.
    * Cada pessoa só deve ter acesso aos dados de sua função, é difícil garantir isso em um sistema de arquivos.
  
