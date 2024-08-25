# Documento de Visão: Sistema CRUD de Funcionário

## Introdução

O objetivo deste documento é fornecer uma visão geral do sistema CRUD de funcionário, que será desenvolvido pela equipe. O sistema permitirá a gestão de funcionários em uma organização, permitindo a criação, leitura, atualização e exclusão de registros de funcionários.

## Requisitos Funcionais

### Entidade: Funcionários

1. **Cadastro de Funcionário**
   - Os usuários devem ser capazes de adicionar informações sobre um novo funcionário, incluindo nome, sobrenome, data de nascimento, cargo, e-mail e número de telefone.

2. **Visualização de Funcionário**
   - Os usuários devem poder visualizar detalhes de um funcionário específico e suas informações cadastradas.

3. **Atualização de Funcionário**
   - Os usuários autorizados devem poder atualizar as informações de um funcionário, como cargo, e-mail e número de telefone.

## Requisitos Não Funcionais

1. **Desempenho**
   - O sistema deve ser responsivo e manter um tempo de resposta aceitável, mesmo quando o banco de dados crescer.

2. **Usabilidade**
   - A interface do usuário deve ser intuitiva e de fácil utilização, com um design amigável.

## Perfis de Usuários

1. **Administrador**
   - Responsável por todas as operações CRUD em funcionários, departamentos e salários.

2. **Gerente de Departamento**
   - Pode visualizar e atualizar informações de funcionários em seu departamento, bem como gerar relatórios de salários.

3. **Usuário Comum**
   - Pode visualizar informações de funcionários e departamentos, mas não possui permissão para atualizar ou excluir registros.

## Tabela de Risco

| Risco                               | Impacto       | Probabilidade | Ação de Mitigação                   |
|-------------------------------------|---------------|---------------|-------------------------------------|
| Perda de dados de funcionários      | Alto          | Baixo         | Realizar backups regulares.         |
| Acesso não autorizado               | Médio         | Médio         | Implementar autenticação segura.     |
| Desempenho insatisfatório           | Médio         | Médio         | Otimizar consultas ao banco de dados.|


