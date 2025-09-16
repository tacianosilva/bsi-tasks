# Tarefa 01 – Conceitos BD e MER

| Nome                        | GitHub   | E-mail                        |
|-----------------------------|----------|-------------------------------|
| José Gean de Macêdo Alves   | [JGean09](https://github.com/jGean09) | jose.gean.706@ufrn.edu.br |

---

## Questões

### Questão 7.A: Descreva o que é um Banco de Dados e o que é um Sistema Gerenciador de Banco de Dados. Cite exemplos de Bancos de Dados e seus SGBDs.

#### Resposta
Um **Banco de Dados** é uma coleção organizada de dados que podem ser acessados, gerenciados e atualizados facilmente.  
Ele apenas armazena a informação. Exemplos: planilhas, tabelas de produtos, registros de alunos etc.

Já um **Sistema Gerenciador de Banco de Dados (SGBD)** é o software que permite criar, consultar, atualizar e apagar dados, além de gerenciar segurança e acesso.  
Exemplos: **MySQL, PostgreSQL, Oracle, SQL Server**.

O banco de dados é o conjunto de dados, e já SGDB é a ferramente que gerencia esses dados

Exemplo de dados em um banco de dados:

| ID | Produto        | Quantidade |
|----|----------------|------------|
| 1  | Celular        | 3          |
| 2  | Notebook Dell  | 5          |
| 3  | Memória Ram    | 8          |
| 4  | SDD 256G       | 10        |

---

### Questão 7.B: Quais os principais problemas de utilizar Sistemas de Arquivos para armazenagem de dados?

#### Resposta
Utilizar sistemas de arquivos (como pastas e arquivos no Windows ou Linux) para guardar dados apresenta vários problemas, principalmente quando comparado a um SGBD. Entre eles:

- **Redundância e inconsistência**: os mesmos dados podem ser armazenados em vários arquivos diferentes, gerando duplicação e risco de estarem desatualizados ou contraditórios.
- **Dificuldade de acesso**: localizar e consultar informações exige criar programas específicos ou percorrer manualmente os arquivos.
- **Falta de segurança**: não há controle de acesso detalhado, qualquer pessoa que tenha acesso ao sistema pode manipular os arquivos.
- **Ausência de integridade**: não existem mecanismos que garantam regras de consistência (como tipos de dados, chaves primárias ou relacionamentos).
- **Dificuldade em manipular grandes volumes de dados**: sistemas de arquivos não são otimizados para lidar com consultas complexas em grandes bases de dados.
- **Baixa escalabilidade e concorrência**: não existe controle eficiente quando vários usuários tentam acessar e alterar os dados ao mesmo tempo.

logo o sistemas de arquivos funcionam para armazenar dados simples, mas se tornam inviáveis quando a aplicação cresce e exige segurança, integridade e múltiplos acessos simultâneos.

---

### Questão 7.C : O modelo de dados entidade-relacionamento foi desenvolvido para facilitar o projeto de banco de dados, permitindo especificação de um esquema que representa a estrutura lógica geral de um banco de dados. Descreva os três elementos básicos de um Modelo Entidade Relacionamento (MER). 

#### Resposta
Um **Modelo Entidade-Relacionamento (MER)** é usado para representar de forma conceitual como os dados estão organizados em um banco.  
Seus três elementos básicos são:

- **Entidades**: representam objetos do mundo real ou conceitos que precisam ser armazenados no banco de dados.  
  Exemplos: `Aluno`, `Curso`, `Produto`.  
  Cada entidade possui atributos que a descrevem.

- **Relacionamentos**: representam as associações entre entidades.  
  Exemplos: um `Aluno` **está matriculado em** um `Curso`; um `Cliente` **faz** um `Pedido`.

- **Atributos**: são as propriedades ou características que descrevem as entidades e os relacionamentos.  
  Exemplos: `nome`, `data_nascimento`, `preço`, `quantidade`.

Logo  **Entidades** são os objetos principais, **Relacionamentos** mostram como eles se conectam, e **Atributos** guardam suas características.

---

### Questão 7.D: Pesquise sobre as várias notações possíveis para Diagramas ER, citando exemplos de notações diferentes para o mesmo conceito (ex: Cardinalidade, Entidade Subordinada, etc.)

As mais populares são:

- **Notação de Chen**: Criada por Peter Chen em 1976, é a notação original e mais clássica. Muito usada em ambientes acadêmicos por ser detalhada, mas visualmente pode ser mais complexa.
- **Notação "Pé de Galinha" (Crow's Foot)**: A mais popular no mercado e em ferramentas CASE. É considerada mais intuitiva e limpa para diagramas grandes. Variações incluem as notações de Information Engineering (IE) e Barker.
- **Notação UML (Unified Modeling Language)**: Usada em engenharia de software para modelar sistemas orientados a objetos. Diagramas de classes podem representar conceitos de dados, de forma similar aos ER tradicionais.

Abaixo, alguns exemplos de como essas notações representam os mesmos conceitos de formas diferentes:

1. **Cardinalidade do Relacionamento**  
A cardinalidade define o número de instâncias de uma entidade que podem se relacionar com instâncias de outra entidade. Exemplo: *“Um CLIENTE pode fazer um ou muitos PEDIDOS”*.

- **Notação de Chen**:  
Usa números ou letras (1, N, M) próximos à linha que conecta a entidade ao relacionamento (losango).  

(1) (N)
+---------+ +-----------+ +---------+
| CLIENTE |------| FAZ |------| PEDIDO |
+---------+ +-----------+ +---------+

Leitura: Um CLIENTE pode ter N PEDIDOS.

- **Notação Pé de Galinha (Crow's Foot)**:  
Usa símbolos gráficos na linha de relacionamento para representar cardinalidade e opcionalidade.  

| representa "um"
O representa "zero"
< (pé de galinha) representa "muitos"

+---------+ +---------+
| CLIENTE | | PEDIDO |
| |<-----| |
+---------+ +---------+


2. **Entidade Fraca (ou Subordinada)**  
Uma entidade fraca depende da existência de outra entidade (entidade forte). Exemplo: *“ITEM_PEDIDO só existe se o PEDIDO ao qual ele pertence existir”*.

- **Notação de Chen**: Entidade fraca desenhada com retângulo duplo, conectada à entidade forte via relacionamento identificador.
- **Crow's Foot / Barker**: Entidade subordinada representada com linhas duplas ou símbolos de dependência para indicar que não existe sem a entidade forte.

Logo, **Entidades** representam os elementos principais do sistema, **Relacionamentos** mostram como eles se conectam, e **Atributos** guardam suas características.

---

