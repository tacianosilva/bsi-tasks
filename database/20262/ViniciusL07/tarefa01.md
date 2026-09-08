# Tarefa 01 - Conceitos de BD, ACID e SGBD

## Questão 01 - Banco de Dados vs. SGBD

### Definições

* **Banco de Dados (BD):** Uma coleção organizada, lógica e estruturada de dados relacionados entre si, projetada para armazenar informações que representam um domínio do mundo real.
* **Sistema Gerenciador de Banco de Dados (SGBD):** Pacote de software com ferramentas especializadas para criar, manipular, consultar, gerenciar a integridade e controlar o acesso a esses bancos de dados.

### Exemplos de Aplicação e SGBDs

| Domínio do Banco de Dados | Tipo de Banco | SGBD Utilizado |
| :--- | :--- | :--- |
| **E-commerce / Vendas** | Relacional (SQL) | `PostgreSQL` ou `MySQL` |
| **Prontuário Hospitalar** | Relacional Corporativo | `Oracle Database` ou `SQL Server` |
| **Catálogo de Streaming** | Não-Relacional (NoSQL Documentos) | `MongoDB` |

---

## Questão 02 - Problemas dos Sistemas de Arquivos

O uso de sistemas de arquivos convencionais (pastas e arquivos como `.txt`, `.csv` ou `.dat`) para armazenar informações críticas gera problemas graves:

1. **Redundância e Inconsistência:** O mesmo dado acaba duplicado em formatos ou locais diferentes. Se um arquivo for atualizado e o outro não, os dados entram em desacordo.
2. **Dificuldade de Acesso:** Qualquer relatório ou busca nova exige a criação de um novo script ou programa de computador para ler e filtrar os dados.
3. **Isolamento dos Dados:** Arquivos gravados em formatos e extensões distintas dificultam cruzamentos e junções de informações.
4. **Problemas de Integridade:** Regras de negócio (ex.: *saldo nunca pode ser menor que zero*) precisam ser programadas manualmente dentro de cada sistema, abrindo brechas para gravações incorretas.
5. **Anomalias de Acesso Concorrente:** Se dois usuários ou programas abrirem e tentarem gravar no mesmo arquivo ao mesmo tempo, dados serão sobrescritos ou corrompidos.
6. **Problemas de Segurança:** Faltam permissões granulares; o sistema geralmente só permite liberar ou bloquear o arquivo inteiro, não permitindo filtrar colunas ou registros confidenciais.