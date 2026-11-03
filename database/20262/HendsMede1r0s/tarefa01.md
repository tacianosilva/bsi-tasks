# Q1 - Descreva o que é um Banco de Dados e o que é um Sistema Gerenciador de Banco de Dados. Cite exemplos de Bancos de Dados e seus SGBDs.

* Um __Banco de Dados__ é um lugar onde é armazenados dados e informações com um certo propósito.
* Já o __Sistema Gerenciador de Banco de Dados__ é um sistema onde pegamos o banco de dados e fazemos operações de CRUD, como cadastrar, visualizar, excluir ou editar alguma informação do banco de dados.
* Um exemplo de como os dois trabalham juntos pode ser um banco. Cada banco tem sua base de dados de seus clientes, ou seja, suas informações, como seu cpf, nome, contato, senhas, etc. Todas essas informações são guardadas num banco de dados, e com ajuda dos SGBDs os funcionários do banco podem cadastrar um cliente novo ao banco de dados, puxar informações específicas, mudar algum dado de alguém, ou excluir alguma informação do BD.e para fazer esses procesos podem ser usados MySQL, Oracle e outros.



# Q2. Quais os principais problemas de utilizar Sistemas de Arquivos para armazenagem de dados?

* Em um sistemas de arquivo comum, podendo ser sistemas físicos ou digitais, há um grande perigo quando estamos falando de admnistrar esses dados que lá estão nesses sistemas. Pois não há nenhum tipo de proibição ou limite para quem esteja usando, ou seja, uma pessoa pode mexer no que quiser e pode acabar sem querer fazendo operações que danifiquem uma ou mais informação, como a exclusão de informações importantes, adição de informações repetidas e maior probabilidade de corromper os dados que estão naqueles arquivos. Os dados não são protegidos da mesma forma que um Banco de Dados é. Além da baixa proteção dos dados, o Sistema de Arquivos é muitas vezes mais lento que os BDs, pois é tudo feito manualmente, você próprio deve ir no diretório e adicionar linha por linha, caso você esteja cadastrando muitas coisas ao mesmo tempo, isso se tornará muito desgastante, e nada fácil.

# Q3. Explique as propriedades ACID: atomicidade, consistência, isolamento e durabilidade. Para cada propriedade, descreva um exemplo prático no contexto de uma transferência bancária e explique o que aconteceria se o SGBD não garantisse essa propriedade.

1. __Atomicidade:__ A atomicidade diz que uma operação ou processo só poderá ser finalizada e completa caso nenhum erro aconteça durante. se qualquer erro acontece, o processo será cancelado, e o funcionária terá que refazer a operação para que os dados e informações do BD não sejam corrompidos. Sem a atomicidade os dados seriam corrompidos 
    * __Ex:__ Em um aplicativo de banco, caso um cliente vá fazer um pix, e a internet caia durante a transação, ou o QR-code do pix expira, essa transação será obrigatoriamente cancelada e desfeita. O cliente terá que refazer o pix.

2. __Consistência:__ São as regras dos bancos de dados, cada um tem suas próprias regras que devem ser respeitadas, caso não sejam, a operação é desfeita ou cancelada. Sem essa concistência de regras dados errados ou faltantes entrariam no armazenamneto do banco de dados gerando confusões futuras. 
    * __Ex:__ Se um cliente, em seu cadastro no sistema bancário, não colocar algum dado obrigatório, como cpf, ou pôr um número, sem querer, em algum dado que só pode ter letras, como no nome, o sistema vai dar erro, pedir para ele digitar novamente e corrigir o erro ou desfazer o processo. 

3. __Isolamento:__ Dita que um processo feito ao mesmo tempo por mais de um usuário, deve ser feita isoladamente, sem ter nenhum cruzamento entre elas, evitando a corrupção dos dados. Se são feitas várias operações o sistema deve trata-las como se elas estivessem sendo feitas separadamente, sem mistura-las em momento algum.
    * __Ex:__ Quando vários clientes fazem transações ao mesmo tempo, o sistema isola cada uma para que nenhuma cruze com a outra, sendo possivel vários clientes diferentes fazeram transações em paralelo sem nenhum erro.

4. __Durabilidade:__ Os processos feitos com os dados e informações do banco de dados, se feitos sem nenhum problema, são salvos pra sempre no banco de dados. e mesmo, que depois, ocorra problema de internet ou energia, os dados continuarão salvos no BD. Sem ter o perigo de perda. Sem essa durabilidade, dados e informações importantes seriam perdidos. 
    * __Ex:__ Caso o cliente faça uma transação, e essa transação for completa, o sistema vai cadastrar uma nova transação, no histórico de transações linkada ao perfil daquela pessoa, no banco dados onde esse pagamento do cliente será salvo permanentemente no armazenamento do BD, e mesmo que ocorra erros futuros, esse dado continuará lá sem ser corrompido.



# Q4. Para cada cenário abaixo, indique qual(is) propriedade(s) ACID está(ão) em jogo e justifique sua resposta: 

## a) Queda de energia no meio de uma transferência deixou o valor debitado da conta de origem, mas não creditado na conta de destino. 

__Atomicidade__, que não foi respeitada, pois foi feito uma operação, e por causa de um erro, ou seja, a queda de energia, o processo ainda assim foi concluido, não debitando o dinheiro na conta destino, além da perda de dinheiro da conta de origem, o dinheiro foi perdido. 

## b) Dois atendentes debitam, ao mesmo tempo, o mesmo saldo de uma conta. 

__Isolamento__, pois há a operação em conjunto e ao mesmo tempo de de duas transações, e as duas são feitas sem problemas, tambem ao mesmo tempo, sem cruzamento entre elas, ocorrendo o isolamento entre elas, para que uma não corrompa o processo da outra.

## c) O sistema confirma a operação, mas após reiniciar o servidor o dado foi perdido. 

__Durabilidade__, pois nesse caso, os dados não foram realmente salvos no armazenamento do banco de dados, ou seja, mesmo com a operação confirmada, se os dados não foram salvos eles irão sumir.

## d) Uma transferência que levaria o saldo abaixo do limite permitido é rejeitada pelo banco.

__Consistência__, pois o sistema impõe que para fazer uma transação, essa mesma transação não podia deixar a conta abaixo do saldo mínimo, caso a pessoa coloque um valor que leve sua conta ao abaixo do saldo mínimo, o sistema nega a transação. 



# Q5. Um SGBD trata dos seguintes aspectos: recuperação, integridade, redundância e inconsistência. Explique cada um deles e descreva como o SGBD os gerencia.
1. __Recuperação:__ Quando o sistema, mesmo após um erro, não corrompa. ou seja, a capicidade do sistema não perder nada e recuperar dados mesmo após algum acaso. Nos SGBDs todos os dados e informações estão guardados no armazenamento e quando ocorre algum erro, os dados voltam a ser como eram antes.
2. __Integridade:__ É o fato do sistema ter restrições para qualquer operação, para manter toda a literal integralidade. Em um SGBD por exemplo, quando estamos cadastrando uma nova informação ou dado, é preciso que o usuário o coloque de forma correta com base nas regras do SGBD, como um nome só podendo ter letras, e um número de telefone só podendo ter números, onde caso essas regras sejam quebradas, o sistema irá detectar e impedir o processo. 
3. __Redundância:__ A redundância ocorre quando há dados literalmente iguais em diferentes lugares do banco de dados. Em um SGBD por exemplo, é de suma impotância que não ocora nenhuma redundância nos dados, pois dois ou mais perfis da mesma pessoa com mesmo email, cpf ou número de telefone pode dar erros no futuro quanto ao encontro dessa pessoa no banco de dados, além de gastar armazenamento inutilmente.
4. __Inconsistência:__ A inconsistência ocorre quando há informações redundantes, mas com algum dado inconsistente ou diferente. No SGBD, para não ocorrer inconsistências, quando um dado muda, o sistema muda todas as cópias junto.


# Q6. Considere o cenário de uma empresa de desenvolvimento de software que atende outras empresas como clientes. A empresa organiza seu trabalho em squads (equipes) compostas por desenvolvedores, testadores, líder técnico, supervisor e gerente de produto. Cada squad resolve tarefas (issues) e planeja releases, testes e o cronograma de sprints (iterações) dos projetos de cada cliente.
## Sem utilizar SQL, elabore um mini-projeto conceitual do banco de dados dessa empresa, deixando claro:
### a) As principais entidades envolvidas (clientes, squads, membros, tarefas, projetos, sprints, releases). 
### b) Os principais atributos de cada entidade. 


* __Cliente:__
    * 'id_cliente'
    * 'nome_empresa'
    * 'cnpj'
    * 'email'
    * 'telefone'


* __Squad:__
    * 'id_squad'
    * 'nome_squad'


* __Membros:__
    * 'cpf'
    * 'nome'
    * 'email'
    * 'telefone'
    * 'especialidade'

* __Tarefas:__
    * 'id_tarefa'
    * 'nome'
    * 'descricao'


* __Projeto:__
    * 'id_projeto'
    * 'nome'
    * 'descricao'
    * 'data_inicio'
    * 'data_fim'


* __Sprint:__
    * 'id_sprint'
    * 'nome'
    * 'descricao'
    * 'data_inicio'
    * 'data_fim'


* __Releases:__
    * 'id_release'
    * 'versao'
    * 'descricao'
    * 'data'


### c) Os relacionamentos entre as entidades (com a cardinalidade, ex.: "um cliente pode ter vários projetos"). 


* __Cliente/Projeto:__ __Um cliente__ pode ter __Vários projetos__, mas __Um projeto__ só pode ter __Um cliente__. __(1:N)__
* __Squad/Membros:__ __Um Squad__ pode ter __vários Membros__, mas __Um Membro__ só pode estar em __Um Squad__. __(1:N)__
* __Squad/Tarefas:__ __Um Squad__ pode ter __várias tarefas__, mas __Uma tarefa__ só pode ser feita por __Um Squad__. __(1:N)__
* __Squad/projeto:__ __Um Squad__ pode estar em __Vários Projetos__, e __Um projeto__ pode ter __Vários Squads__. __(N:M)__
* __Membros/Tarefas:__ __Um Membro__ pode ter __várias Tarefas__, mas __uma tarefa__ é feita por apenas __um membro__. __(1:N)__
* __Membros/Projeto:__ __Um membro__ pode estar em __vários projetos__, e __um projeto__ pode ter __vários membros__. __(N:M)__
* __Tarefa/Projeto:__ __Uma Tarefa__ está vinculada a apenas __um projeto__, mas __um projeto__ pode ter __várias tarefas__. __(1:N)__
* __Projeto/Sprint:__ __Um projeto__ pode ter __vários sprints__, mas __um sprint__ pode ser de apenas __um projeto__. __(1:N)__
* __Projeto/Releases:__ __Um projeto__ pode ter __varias releases__, mas __uma release__ é de apenas um __projeto__


### d) Em linguagem natural, as regras de integridade (restrições) que o banco de dados deveria garantir, ex.: "apenas um líder por squad", "toda tarefa precisa estar vinculada a um projeto".

1. Um Squad deve ter apenas um lider/representante.
2. Cada Squad devem ter números iguais de membros.
3. Todo Squad deve ter suas próprias tarefas vinculadas ao grupo.
4. Toda Tarefa deve estar vinculada a um projeto.
5. Todo Projeto deve ter um cliente vinculado.
6. Todo Membro deve fazer parte de apenas um Squad.
7. Um Membro deve ser vinculado a uma tarefa por vez.
8. Qualquer atributo de email, cnpj e cpf não podem ser duplicados.
9. O id de uma entidade não pode ser igual ao id de uma mesma entidade. Projeto1 obrigatoriamente tem id diferente do projeto2.