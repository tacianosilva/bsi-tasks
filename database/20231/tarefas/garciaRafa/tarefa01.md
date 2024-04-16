# **Tarefa 01 - Conceitos BD e MER**

## Rafael da Silva Garcia / garciaRafa / rafael.garcia.113@ufrn.edu.br

### **7**
1.  **Banco de Dados** é uma coleção orgazinada de dados ou informações armazenadas em um computador, enquanto um **Sistema Gerenciador de Banco de Dados** é uma ferramentas que permitem criar, armazenar, modificar e extrair informações de um banco de dados. Por exemplo, existem os **Bancos de Dados Relacionais**, que organizam os dados em tabelas com linhas e colunas, algumas SGBDs para um banco de dados relacional são **MySQL**, **Oracle**, **SQL Server** e  **PostgreSQL**.
2. Com um grande número de arquivos se torna difícil organizar e localizar os dados, as informações podem ser repetidas em diferentes arquivos, o sistema de arquivo pode também não permitir que os usuários acessem todos os dados, tornando restrito a cada função exercida pelo funcionário.
3. **Entidade**: é um objeto ou conceito do mundo real que pode ser distinguido de outras coisas. Por exemplo, em um banco de dados para uma loja, as entidades poderiam ser clientes, produtos e pedidos. As entidades são representadas graficamente como retângulos com seus nomes no interior.<p/>
**Atributos**: Um atributo é uma característica ou propriedade de uma entidade. Por exemplo, o nome e o endereço seriam atributos de uma entidade Cliente. Os atributos são representados graficamente como elipses ligados às entidades que eles descrevem.<p/>
**Relacionamentos**:  Um relacionamento é uma conexão entre duas ou mais entidades. Por exemplo, em um banco de dados de uma loja, um relacionamento pode existir entre um cliente e um pedido, indicando que o cliente fez o pedido. Os relacionamentos são representados graficamente como linhas que conectam as entidades envolvidas, e podem ter rótulos para indicar a natureza do relacionamento (como "fez um pedido").
4. **Notação Chen**: Usa retângulos para representar entidades, diamantes para representar relacionamentos e linhas para representar cardinalidades. Por exemplo, uma cardinalidade 1:N é representada por uma linha que liga uma extremidade do diamante a um retângulo, e outra linha que liga a outra extremidade do diamante a um número "N" próximo ao retângulo.<p/>
**Notação Crow's Foot**: É uma notação popular para diagramas ER, amplamente usada em bancos de dados relacionais. Ela usa símbolos semelhantes a patas de corvo para representar cardinalidades. Por exemplo, uma cardinalidade 1:N é representada por um símbolo de pé-de-galinha que aponta para a entidade "1" e uma linha que liga a outra extremidade do símbolo ao retângulo "N".

```mermaid
erDiagram
    Empregado }|--|{ EmpregadoLivre : Horario
    Empregado }|--|{ EmpregadoFixo : Horario
    Empregado }|--|{ BaterPonto : BaterPonto
    DiaSemana }|--|{ Turno : DiaTrabalhado
    BaterPonto }|--|{ Turno: Turno

    Empregado{
        int matr
        string nome
        string email
    }

    EmpregadoLivre{
        int horasTotais
        int horasMinimas
    }

    EmpregadoFixo{
        String turno1
        String turno2
    }

    Turno{
        String manha
        String tarde
        String noite
    }

    DiaSemana{
        String dom "Domingo" 
        String seg "Segunda-feira"
        String ter "Terça-feira"
        String qua "Quarta-feira"
        String qui "Quinta-feira"
        String sex "Sexta-feira"
        String sab "Sábado"
    }

    BaterPonto{
        int baterEntrada
        int baterSaida
    }