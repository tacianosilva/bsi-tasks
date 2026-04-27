# 📊 Sistema de Gestão de Projetos e Atividades - Tarefa 02

Repositório destinado à implementação da segunda tarefa da disciplina de Projeto e Administração de Banco de Dados.

## 👤 Identificação
* **Nome:** Kaique Vieira Soares
* **Matrícula:** 20240019677
* **Email:** kaique.vieira.168@ufrn.edu.br

---

## 🏗️ Estrutura do Projeto
O projeto foi desenvolvido utilizando uma arquitetura **Multi-module Maven**, garantindo o isolamento das dependências entre as abordagens JDBC e ORM:

* **Módulo `jdbc/`**: Persistência nativa de baixo nível.
* **Módulo `orm/`**: Persistência de alto nível com Spring Data JPA.

## 📄 Documentação da Atividade
Todas as questões, resumos teóricos (ODBC/ORM) e links para os códigos-fonte estão documentados no link abaixo:

👉 **[RELATÓRIO TÉCNICO E RESPOSTAS (tarefa-orm.md)](./database/20252/tarefas/kaiquevieirasoares/tarefa-orm.md)**

---

## ⚙️ Inicialização Rápida
1. Suba o banco de dados: `docker compose up -d`
2. O script de inicialização (`01-init.sql`) será executado automaticamente.