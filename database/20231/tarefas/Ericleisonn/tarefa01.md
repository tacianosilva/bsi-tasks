# Tarefa 01 - Conceitos BD e MER

Nome: Ericleison Camilo Silva de Holanda
Usuário github: Ericleisonn
E-mail: ericleison.camilo.124@ufrn.edu.br

Um banco de dados é uma seleção de informações organizados estruturalmente, normalmente armazenadas eletronicamente em um sistema de computador. Um sistema de gerenciamento de banco de dados (DBMS) serve como uma interface entre o banco de dados e seus usuários ou programas. Permitindo assim um gerenciamento organizado e otimizado do banco de dados, além de facilitar a supervisão e o controle do mesmo.
Como exemplo de bancos de dados, temos: Banco de dados relacional, essas são os mais presentes no mercado, utilizando o SQL
Banco de dados não-relacional: utilizando o NoSQL, dentre outros

Dentre as desvantagnens do uso de arquivos como banco de dados, temos: Impossibilidade de realizar acesso simultâneo aos dados, Inconsistência nos dados, problema com a integridade dos arquivos, dentre outros.

Os elementos básicos de um Modelo Entidade Relacionamento são: Um objeto do mundo real e que possuem uma existência independente, como: pessoas, empresa, carro, casa, entre outras coisas que podem ser representadas por uma entidade.

Relacionamentos: Uma vez que as entidades são identificadas, deve-se então definir como se dá o relacionamento entre elas. De acordo com a quantidade de objetos envolvidos em cada lado do relacionamento, podemos classifica-los de três formas: Relacionamento 1..1 (um para um) ; Relacionamento 1..n ou 1..* (um para muitos) ; Relacionamento n..n ou *..* (muitos para muitos).

Atributos: São as características que descrevem cada entidade dentro do domínio. Por exemplo, um cliente possui nome, endereço e telefone. 

Quanto as notações possíveis para Diagramas ER, podemos citar: Cardinalidade refere-se ao número máximo de vezes que a instância em uma entidade pode ser relacionada a instâncias de outra entidade.

Ordinalidade: É o número mínimo de vezes que uma instância em uma entidade pode ser associada a uma instância em uma entidade relacionada.

Entidade subordinada: Representa uma especializacao de entidade no modelo de dados onde uma entidade supertipo possui várias entidades subordinada que são especializadas com atributos especíicos.

[![](https://mermaid.ink/img/pako:eNptUstuwjAQ_BVrzzQKedDgax9SD1WpyqGqIkVbbMBqYiPHQdCEf-8mgZZAc7G9MzuzE7uGhRESOEh7r3BlsUg1eyg2Vq5QGNY0ntc0j7ncqa3MGWdrY9Eqk-Vqa2Wq_5g19dGntGOkqFamP5fOKr1i2hRyUJAFqjzVh1SfxM8EWpPy4pgVSlfOlAOV18o4zNDRXgkcQM9Kq8JkRynyIaen95d2vYzHWuAs21LtTMsTCjOBWUmzaqwH6n3EjBhXMfsiGc4rq019jbu2ftV6MpfaWRT_YyV2KX_D9PPXbDAoBZlb_MR8jRcRTvRusJYmi1ZpZrQzZ3__bi0XaI82PffY2DE5m1m5UCWyVMMICmnpKgW9oE4iBbeWdNfAaSvQfqVASsRDury3vV4Ad7aSI6g2Ap08vjngS8xLqm5QA69hBzyIIy_2p37gB0k0DZM4GMEe-M2tF43HYegnt_4kmiRxfBjBtzEkMfaScTiZxtOYgDDuxD46pHU8_AAfUQDi?type=png)](https://mermaid.live/edit#pako:eNptUstuwjAQ_BVrzzQKedDgax9SD1WpyqGqIkVbbMBqYiPHQdCEf-8mgZZAc7G9MzuzE7uGhRESOEh7r3BlsUg1eyg2Vq5QGNY0ntc0j7ncqa3MGWdrY9Eqk-Vqa2Wq_5g19dGntGOkqFamP5fOKr1i2hRyUJAFqjzVh1SfxM8EWpPy4pgVSlfOlAOV18o4zNDRXgkcQM9Kq8JkRynyIaen95d2vYzHWuAs21LtTMsTCjOBWUmzaqwH6n3EjBhXMfsiGc4rq019jbu2ftV6MpfaWRT_YyV2KX_D9PPXbDAoBZlb_MR8jRcRTvRusJYmi1ZpZrQzZ3__bi0XaI82PffY2DE5m1m5UCWyVMMICmnpKgW9oE4iBbeWdNfAaSvQfqVASsRDury3vV4Ad7aSI6g2Ap08vjngS8xLqm5QA69hBzyIIy_2p37gB0k0DZM4GMEe-M2tF43HYegnt_4kmiRxfBjBtzEkMfaScTiZxtOYgDDuxD46pHU8_AAfUQDi)