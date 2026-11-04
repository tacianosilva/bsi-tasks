# Tarefa 03 - Docker e SGBD
 
**Disciplina:** DCT2201 - Banco de Dados | **Curso:** Sistemas de Informação - CERES/UFRN
 
---
 
## 1. Identificação e Repositório
 
- **Nome completo:** Flávia Juliana Araújo de Carvalho
- **Usuário no GitHub:** Flavia-Carvalho-1
- **E-mail acadêmico:** flavia.carvalho.124@ufrn.edu.br
- **Repositório pessoal público:** [dct2201-banco-de-dados (README.md)](https://github.com/Flavia-Carvalho-1/dct2201-banco-de-dados/blob/0678540454252b2874592d62be01a9fb74aab3f0/README.md)
Arquivos de infraestrutura (no repositório pessoal, pasta `tarefa03/`): `docker-compose.yml`, `.env.example`, `povoamento.sql`, `setup.sql`. O `.gitignore` fica na raiz do repositório e impede o versionamento do `.env`.
 
**Ambiente utilizado** (saídas reais):
 
```
git version 2.53.0.windows.3
Docker version 29.9.2, build a82e528
Docker Compose version v5.6.1
```
 
Imagens: `mariadb:11` (o log mostrou MariaDB 11.8.9) e `dbeaver/cloudbeaver:latest`. Terminal utilizado: PowerShell no Windows, com Docker Desktop.
 
Verificação de que o `.env` é ignorado pelo Git:
 
```
PS> git check-ignore -v .env
.gitignore:1:.env       .env
```
 
O log do MariaDB na primeira inicialização terminou com `mariadbd: ready for connections.`, e a conexão do CloudBeaver foi feita com host `mariadb` (nome do serviço no Compose) e porta `3306`.
 
---