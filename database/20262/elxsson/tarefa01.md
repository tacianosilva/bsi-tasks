# Tarefa 01 - Conceitos de BD, ACID e SGBD

## Q1. Banco de Dados e SGBD

Um Banco de Dados é um conjunto organizado de dados relacionados entre si, que representam informações sobre um domínio específico. Pode ser o cadastro de clientes de uma empresa, os registros acadêmicos de uma universidade, o histórico de vendas de uma loja, enfim, qualquer conjunto de dados que precise ser armazenado, consultado e atualizado de forma estruturada.

Já o Sistema Gerenciador de Banco de Dados, ou SGBD, é o software que fica responsável por criar, manter, organizar e controlar o acesso a esse banco de dados. Ele atua como uma camada entre a aplicação e os dados propriamente ditos, cuidando de aspectos como segurança, integridade, controle de concorrência e recuperação em caso de falhas.

Alguns exemplos de bancos de dados e dos SGBDs que costumam gerenciá-los:

| Banco de Dados (exemplo) | SGBD utilizado |
|---|---|
| Cadastro de clientes de um e-commerce | MySQL ou PostgreSQL |
| Registros de um sistema bancário | Oracle Database |
| Posts e usuários de uma rede social | MongoDB |
| Sessões de usuários de um sistema web | Redis |
| Dados locais de um aplicativo mobile | SQLite |

## Q2. Problemas de usar Sistemas de Arquivos para armazenagem de dados

Antes de os SGBDs se popularizarem, os dados eram armazenados diretamente em arquivos manipulados por programas específicos. Essa abordagem trazia vários problemas:

- **Redundância e inconsistência de dados**. O mesmo dado podia acabar armazenado em vários arquivos diferentes, cada um mantido por um programa distinto. Se um fosse atualizado e o outro esquecido, os dados ficavam divergentes.
- **Dificuldade de acesso aos dados**. Não existia uma linguagem de consulta genérica como o SQL, então cada nova pergunta sobre os dados exigia escrever um programa novo, sob medida.
- **Isolamento dos dados**. As informações ficavam espalhadas em arquivos com formatos diferentes, o que tornava trabalhoso combinar dados de fontes distintas numa mesma aplicação.
- **Falta de integridade**. Regras de negócio, como "o saldo não pode ficar negativo", precisavam ser codificadas manualmente em cada programa. Não havia garantia de que todos os programas aplicariam essa regra da mesma forma.
- **Falta de atomicidade**. Se o sistema falhasse no meio de uma operação, não existia um mecanismo automático para desfazer as alterações que já tinham sido feitas parcialmente.
- **Problemas de acesso concorrente**. Quando dois usuários acessavam e alteravam o mesmo arquivo ao mesmo tempo, um podia sobrescrever as mudanças do outro sem perceber.
- **Segurança limitada**. Era difícil restringir o acesso a partes específicas dos dados, já que a proteção dependia apenas das permissões do sistema operacional, sem um controle mais granular.
