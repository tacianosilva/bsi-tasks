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
  
*** c) *** Entidade, atributo e relacionamentos.
*** d) Notações possíveis para Diagramas ER. *** 
  1. *** Notação Chen. *** É uma das notações mais tradicionais e detalhadas, popularizada em ambientes acadêmicos.
    * *** Entidade: *** Retângulo.
    * *** Atributo: *** Oval, conectado à entidade.
    * *** Relacionamento: *** Losango, conectando entidades.
    * *** Cardinalidade: *** A cardinalidade é escrita com números e letras (1, N, M) ao lado do losango de relacionamento.
    * *** Entidade fraca: *** Retângulo com borda dupla.
    * *** Atributo multivalorado: *** Oval com borda dupla.
    * *** Atribudo derivado: *** Oval com linha pontilhada.
  2. *** Notação Pé de Galinha (Crow's Foot). *** É a notação mais popular em projetos de banco de dados por ser mais intuitiva e concisa. Em vez de usar losangos para relacionamentos, ela usa a linha de conexão e símbolos nas extremidades para indicar a cardinalidade. Símbolos para cardinalidade nas extremidades da linha de relacionamento:
    * *** Um: *** traço vertical (|)
    * *** Zero ou mais: *** Círcuito seguido de um pé de galinha (O<).
    * *** Um ou mais: *** Traço vertical seguido de um pé de galinha (|<).
    * *** Zero ou um: *** Círculo e um traço vertical (O|). 
  3. *** Notação UML (Unified Modeling Language) *** A notação de Diagramas de Classe da UML pode ser adaptada para modelar conceitos de ER. 
    * *** Entidade: *** Classe, representada por um retângulo dividido.
    * *** Atributo: *** Listado na seção central da classe.
    * *** Relacionamento: *** Linhas que conectam as classes.
    * *** Multiplicidade (Cardinalidade): *** É indicada por números e asteriscos nas extremidades das linhas de relacionamento.
      - 1: Um.
      - *: Zero ou muitos.
      - 1..*: Um ou muitos.
      - 0..1: Zero ou um. 
*** e) Diagrama ER para projetar uma base de dados de um Sistema de Controle de Freqüência de Empregados de uma organização ***
``` mermaid
---
config:
  theme: dark
---
erDiagram
    Empregado {
        string codigo PK
        string nome
        string email
    }
    Empregado_Hora_Livre {
        string horas_a_trabalhar_no_mes
        string menor_perio_de_trabalho
    }
    Empregado_Hora_Fixa {
    }
    Turno {
        string cod PK
        string inicio
        string fim
    }
    Dia_Da_Semana {
        string cod PK
        string nome
    }
    Ponto {
        string cod PK
        string entrada
        string saida
    }
    
    Empregado ||--|| Empregado_Hora_Fixa : "é um"
    Empregado ||--|| Empregado_Hora_Livre : "é um"
    Empregado_Hora_Fixa ||--o{ Turno : "trabalha em"
    Turno ||--|| Dia_Da_Semana : "tem"
    Empregado ||--o{ Ponto : "tem"
