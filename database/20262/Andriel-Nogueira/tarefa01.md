# Tarefa 01 - Conceitos de BD, ACID e SGBD

**Aluno:** Andriel Pereira Nogueira  
**Usuário GitHub:** @Andriel-Nogueira  
**Disciplina:** Banco de Dados  
**Issue Relacionada:** #416

---

## Questão 01: Banco de Dados vs. SGBD

* **Banco de Dados (BD):** É uma coleção organizada de dados logicamente relacionados entre si, estruturados para representar entidades, atributos e relacionamentos do mundo real de forma a permitir o armazenamento, consulta e manipulação eficiente das informações.
* **Sistema Gerenciador de Banco de Dados (SGBD):** É o conjunto de softwares responsáveis por gerenciar o acesso, a segurança, a integridade, a concorrência e a persistência dos dados contidos no Banco de Dados, servindo como uma interface intermediária entre as aplicações/usuários e os arquivos físicos.

### Exemplos de Bancos de Dados e seus SGBDs:
1. **Banco de Dados Relacional da Loja Virtual:** Gerenciado pelo **PostgreSQL** ou **MySQL**.
2. **Banco de Dados Documental (NoSQL) de Redes Sociais:** Gerenciado pelo **MongoDB**.
3. **Banco de Dados em Memória para Caching:** Gerenciado pelo **Redis**.

---

## Questão 02: Problemas do uso de Sistemas de Arquivos para Armazenamento

A utilização de arquivos convencionais (como `.txt`, `.csv` ou planilhas) para gerenciar dados corporativos apresenta severas limitações:

1. **Redundância e Inconsistência de Dados:** As mesmas informações podem ser duplicadas em arquivos diferentes por departamentos distintos, levando a divergências quando atualizadas em um local e não no outro.
2. **Dificuldade no Acesso aos Dados:** Para realizar consultas personalizadas ou relatórios complexos, é necessário escrever novos programas específicos para ler e filtrar os arquivos.
3. **Isolamento de Dados:** Dados espalhados em diferentes arquivos e formatos tornam difícil a integração e extração de métricas consolidadas.
4. **Problemas de Concorrência e Acesso Múltiplo:** Se dois usuários tentarem alterar o mesmo arquivo simultaneamente, pode haver perda de dados ou corrupção do arquivo por falta de controle de travamento (*locking*).
5. **Anomalias de Atomicidade:** Se o sistema falhar no meio de uma gravação em arquivo, o estado intermediário fica gravado sem opção de *rollback* automático.
6. **Problemas de Segurança e Integridade:** É difícil aplicar regras de integridade (ex: proibir valores negativos) e restrições de segurança refinadas por usuário/tabela em nível de sistema operacional.

---