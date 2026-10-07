# Tarefa 01 - Conceitos de BD, ACID e SGBD

**Conceitos de Git e GitHub**

* **Branches:** São tipo universos paralelos do seu código. Você cria uma branch para testar um widget novo em Flutter ou fazer uma feature sem risco de quebrar o código oficial (a branch `main`).
* **Pull Request (Merge Request):** O famoso PR. É você sinalizando no GitHub: "terminei as alterações aqui na minha branch, avalia aí se podemos juntar com o projeto principal".
* **Merge:** É a costura final. O Git pega a sua branch e une o histórico dela com a branch principal.
* **Rebase:** Faz algo parecido com o merge, mas reescreve a história. Ele puxa seus commits e os joga lá na ponta da branch principal, deixando o histórico reto, sem aquelas curvas visuais de merge.
* **Conflitos:** A dor de cabeça clássica. Acontece quando duas pessoas mexem na exata mesma linha de um arquivo. O Git trava e manda você escolher manualmente qual versão deve ficar.

**Q1. Banco de Dados vs. SGBD**

* **Banco de Dados (BD):** São os dados puros armazenados de forma estruturada. Pense nas informações de clientes e funcionários que você organizava naquelas structs em C no projeto SIG-Bike, só que guardadas em larga escala e interligadas.
* **SGBD (Sistema Gerenciador de Banco de Dados):** É o software parrudo que faz o meio de campo. Ele gerencia as regras de negócio, a segurança e a forma como a gente consulta esses dados.

**Exemplos:**
* **SGBDs:** PostgreSQL, MySQL, Oracle, MongoDB.
* **Bancos de Dados:** O banco acadêmico do SIGAA, o banco de um app de delivery, ou um dataset de clima no Kaggle pronto pra ser minerado em Python.


**Q2. O problema de usar Sistemas de Arquivos**

Se a gente guarda tudo em arquivos soltos pelo sistema, surgem vários problemas graves:
* **Redundância:** A mesma informação fica duplicada em vários cantos.
* **Inconsistência:** Você altera o dado em um arquivo, esquece do outro, e a base passa a apresentar informações divergentes.
* **Acesso difícil:** Para criar um filtro ou uma busca diferente, muitas vezes você precisa programar um script do zero só para ler o texto.
* **Zero segurança:** Qualquer processo ou usuário com acesso à pasta pode corromper o arquivo inteiro.

**Q3. Propriedades ACID (com exemplo de Transferência Bancária)**

* **Atomicidade (Tudo ou Nada):** A operação não pode parar na metade. Se você manda 50 reais de transferência pra sua mãe, o dinheiro tem que sair da sua conta e cair na dela. Se falhar, tem que desfazer tudo; senão, o dinheiro sumiria no limbo.
* **Consistência:** O banco precisa respeitar as regras matemáticas e lógicas. Se você não tem limite de cheque especial, uma transferência não pode deixar sua conta negativa.
* **Isolamento:** Duas requisições simultâneas não podem bater cabeça. Se você passar o cartão duas vezes no exato mesmo milissegundo, o sistema não pode ler o saldo antigo para aprovar as duas, ignorando que o dinheiro só dava pra uma.
* **Durabilidade:** Viu a tela de "Sucesso"? Tá salvo de verdade. Se o servidor da TIM ou do banco reiniciar um segundo depois, o dado já tem que estar gravado no disco físico e não pode se perder.


**Q4. Qual propriedade ACID falhou?**

* **a) Queda de energia e dinheiro sumiu:** Falhou a **Atomicidade**. Fez o débito, não fez o crédito e não teve a capacidade de desfazer a metade que já tinha rodado.
* **b) Atendentes debitando o mesmo saldo:** Falhou o **Isolamento**. As transações atropelaram umas às outras, lendo dados desatualizados porque aconteceram ao mesmo tempo.
* **c) Sistema reiniciou e o dado sumiu:** Falhou a **Durabilidade**. O commit informou que salvou, mas a gravação não resistiu à reinicialização.
* **d) Transferência bloqueada por limite de saldo:** A **Consistência** funcionou perfeitamente aqui. O SGBD interveio e barrou a operação para proteger a regra de negócio.

**Q5. Como o SGBD cuida da base**

* **Recuperação:** É o plano de resgate. O SGBD anota tudo num arquivo de log à parte. Deu erro de hardware? Ele lê o log e refaz (redo) ou desfaz (rollback) as transações incompletas.
* **Integridade:** São as rédeas do sistema. O SGBD usa *constraints* para garantir que ninguém coloque uma string num campo de data, ou cadastre um CPF inválido.
* **Redundância:** O SGBD estimula a normalização. Em vez de escrever todos os dados do cliente em cada venda, ele guarda só um ID e cruza as tabelas na hora da consulta.
* **Inconsistência:** É curada cortando a redundância na raiz. Se o CPF existe em uma tabela só, é impossível ele estar diferente em outro lugar.


**Q6. Mini-projeto da Empresa de Software**

**a) Entidades Principais:**
Cliente, Projeto, Squad, Membro, Sprint, Tarefa, Release.

**b) Atributos:**
* **Cliente:** ID_Cliente, Nome, CNPJ.
* **Projeto:** ID_Projeto, Titulo, Escopo.
* **Squad:** ID_Squad, Nome_Equipe.
* **Membro:** ID_Membro, Nome, Cargo (Dev, QA, Tech Lead, etc).
* **Sprint:** ID_Sprint, Iteracao, Data_Inicio, Data_Fim.
* **Tarefa:** ID_Tarefa, Descricao, Status (To Do, Doing, Done).
* **Release:** ID_Release, Versao.

**c) Relacionamentos:**
* O **Cliente** é dono de *vários* **Projetos** (1:N).
* O **Projeto** é assumido por *uma* **Squad** (1:1).
* A **Squad** contém *vários* **Membros** (1:N).
* O **Projeto** é dividido em *várias* **Sprints** (1:N).
* A **Sprint** engloba *várias* **Tarefas** (1:N).
* O **Projeto** gera *várias* **Releases** (1:N).
* A **Release** empacota *várias* **Tarefas** (1:N).

**d) Regras de Integridade Lógica:**
* "Cada squad só pode ter um único Tech Lead alocado."
* "Toda tarefa criada precisa, obrigatoriamente, ser jogada em alguma sprint."
* "As datas das sprints de um mesmo projeto não podem encavalar ou se sobrepor."
* "Uma release só aceita o vínculo de tarefas que estejam com o status cravado em 'Done/Concluído'."


