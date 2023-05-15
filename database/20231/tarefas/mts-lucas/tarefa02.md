# Tarefa 02 - Modelo Relacional e Regras de Conversão

**Nome:** Lucas Mateus da Silva

**Github:** git clone https://github.com/mts-lucas

**Email:** lmateus1067@outlook.com

##

# a) Descreva o Modelo Relacional.

O Modelo Relacional representa os dados num Banco de Dados como uma coleção de relações e seus relacionamentos. Cada relação contém um nome e um conjunto de atributos com seus respectivos nomes. Informalmente, as relações do Modelo Relacional são também chamadas de tabelas pela maioria dos desenvolvedores. Essas tabelas são conhecidas como relações e são compostas por atributos e tuplas. Cada atributo representa uma propriedade dos dados armazenados e cada tupla representa uma instância desses dados.
As relações são interconectadas por meio de chaves estrangeiras, que permitem estabelecer relacionamentos entre as tabelas. Esses relacionamentos podem ser de um-para-um, um-para-muitos ou muitos-para-muitos.

## b) Descreva as restrições de integridade do Modelo Relacional

**Restrições de integridade de domínio:** Essas restrições definem os valores válidos para um determinado atributo em uma tabela. Toda tupla tem um conjunto de atributos que a identifica de maneira única na relação.

**Integridade de Entidade:** Nenhum valor de chave primária poderá ser NULO.

**Integridade Referencial:** Essas restrições garantem que as referências entre tabelas sejam mantidas quando ocorrerem atualizações ou exclusões de registros. Por exemplo, se um registro em uma tabela referenciada for excluído, todos os registros em outras tabelas que fazem referência a ele também devem ser excluídos ou atualizados para refletir essa exclusão.

## c) Descreva as Regras de Conversão entre o Modelo Entidade-Relacionamento e o Modelo Relacional.

**Regra 1: Entidades Regulares**

1.1. Para cada entidade regular E no esquema E-R, criamos uma relação R que inclui os atributos simples de E

1.2. Para cada atributo composto de E incluímos somente os seus atributos simples

1.3. Escolhemos uma das chaves candidatas de E para ser a chave primária de R


