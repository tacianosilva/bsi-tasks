# Tarefa 01 - Conceitos de Banco de Dados

### Q1. Descreva o que é um Banco de Dados e o que é um Sistema Gerenciador de Banco de Dados. Cite exemplos de Bancos de Dados e seus SGBDs.
* **Banco de Dados (BD):** É a coleção organizada de dados logicamente relacionados, armazenados de forma estruturada (geralmente em arquivos físicos no disco) para permitir fácil acesso, gerenciamento e atualização.
* **Sistema Gerenciador de Banco de Dados (SGBD):** É o software (ou conjunto de softwares) que serve como interface entre o banco de dados, os usuários e as aplicações. Ele gerencia o armazenamento, a segurança, a integridade e o acesso aos dados.
* **Exemplos:** 
  * *SGBDs:* MySQL, PostgreSQL, Oracle Database, Microsoft SQL Server.
  * *Bancos de Dados:* O arquivo físico de dados gerado por um sistema de RH, o arquivo `.mdf` do SQL Server de um sistema de vendas, ou o banco de dados interno de um aplicativo de celular (gerenciado via SQLite).

### Q2. Quais os principais problemas de utilizar Sistemas de Arquivos para armazenagem de dados?
Antes dos SGBDs, os dados eram salvos em sistemas de arquivos comuns do sistema operacional. Os principais problemas eram:
1. **Redundância e inconsistência de dados:** O mesmo dado (ex: endereço de um cliente) salvo em vários arquivos diferentes, correndo o risco de ser atualizado em um e esquecido no outro.
2. **Dificuldade de acesso:** Cada nova consulta exigia que um programador escrevesse um código específico para ler o arquivo.
3. **Isolamento de dados:** Dados espalhados em diferentes arquivos e formatos, dificultando o cruzamento de informações.
4. **Problemas de integridade:** Dificuldade em aplicar regras de negócio (ex: "o saldo não pode ser negativo") diretamente no arquivo.
5. **Acesso concorrente:** Se dois usuários tentassem editar o mesmo arquivo de texto simultaneamente, os dados de um deles seriam sobrescritos e perdidos.
6. **Falta de atomicidade:** Se o sistema caísse no meio de uma gravação, o arquivo poderia corromper e ficar pela metade.
