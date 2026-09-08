# Tarefa01 - Conceitos de BD, ACID, SGBD

**Aluno** Leonardo Relva   
**Usuário do GitHub** leonardorelva-ufrn

---

## Questão da Atividade

### Q1. Banco de Dados e SGBD

* **Banco de Dados (BD):** É uma coleção organizada de dados estruturados, que estão relacionados entre si, armazenados eletronicamente para facilitar o acesso, busca e atualização.
* **Sistema Gerenciador de Banco de Dados (SGBD):** É o software responsável por intermediar a comunicação entre as aplicações/usuários e o Banco de Dados físico. Ele gerencia a criação, leitura, atualização, exclusão de dados, além de garantir a segurança, concorrência e integridade.

**Exemplos de BDs e SGBDs:**
1. **SGBD Relacional:** PostgreSQL, MySQL, Oracle Database, Microsoft SQL Server.
2. **SGBD NoSQL (Documentos/Chave-Valor):** MongoDB, Redis, Cassandra.

---

### Q2. Problemas do uso de Sistemas de Arquivos
A utilização de arquivos comuns de sistema operacional (como arquivos de texto ou planilhas) para armazenar dados traz diversos problemas:
1. **Redundância e Inconsistência:** O mesmo dado pode ser duplicado em vários arquivos, gerando discrepâncias se um for atualizado e o outro não.
2. **Dificuldade de Acesso:** Necessidade de escrever código customizado para cada nova consulta ou relatório desejado.
3. **Isolamento e Formatos Incompatíveis:** Dados espalhados em arquivos com formatos diferentes tornam a integração complexa.
4. **Anomalias de Acesso Concorrente:** Múltiplos usuários editando o mesmo arquivo simultaneamente podem sobrescrever e perder dados.
5. **Problemas de Segurança:** Dificuldade em restringir o acesso a partes específicas dos dados por nível de permissão do usuário.

---