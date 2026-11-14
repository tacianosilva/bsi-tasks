# Tarefa 01 - Conceitos de BD, ACID e SGBD

**Aluno:** Daniel Mariz da Silva  
**GitHub Username:** danielmrz7  

---

## 📌 Guia de Conceitos do Git e GitHub

- **Branchs:** Linhas paralelas de desenvolvimento. Permitem criar, testar e isolar novas funcionalidades sem afetar o código principal (`main`).
- **Pull Request (ou Merge Request):** Solicitação formal para integrar as alterações de uma branch (ou fork) para o repositório/branch de destino. Permite revisão de código (*code review*) e execução de testes automatizados.
- **Merge:** Operação que combina o histórico e os commits de duas branchs, criando tipicamente um commit de mesclagem (*merge commit*).
- **Rebase:** Reescreve o histórico de commits, aplicando as alterações de uma branch no topo de outra. Resulta num histórico linear e sem commits de merge adicionais.
- **Conflitos:** Ocorrem quando o Git não consegue mesclar automaticamente alterações feitas no mesmo trecho de um ficheiro em branchs diferentes. Exigem resolução manual por parte do desenvolvedor.

---

## Q1. Conceito de BD, SGBD e Exemplos

- **Banco de Dados (BD):** Coleção organizada de dados inter-relacionados que representam aspectos do mundo real e são armazenados eletronicamente para posterior consulta, processamento e recuperação.
- **Sistema Gerenciador de Banco de Dados (SGBD):** Software ou conjunto de programas encarregado de criar, gerenciar, manipular, consultar e controlar o acesso de segurança ao banco de dados, atuando como interface entre as aplicações e os dados físicos.

### Exemplos de BDs e seus SGBDs

| Tipo de Banco de Dados | Exemplo de BD | SGBD Correspondente |
| :--- | :--- | :--- |
| **Relacional (RDBMS)** | Sistema de Gestão Acadêmica | PostgreSQL / MySQL / Oracle Database |
| **NoSQL (Documentos)** | Catálogo de Produtos E-commerce | MongoDB |
| **NoSQL (Chave-Valor)** | Sessões de Usuário em Cache | Redis |
