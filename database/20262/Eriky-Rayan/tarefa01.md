## Q1.
**Enunciado:** Descreva o que é um Banco de Dados e o que é um Sistema Gerenciador de Banco de Dados. Cite exemplos de Bancos de Dados e seus SGBDs.

### Resposta
Banco de Dados: Um banco de dados é uma coleção organizada de dados relacionados, armazenados em algum dispositivo.

Sistema Gerenciador de Banco de Dados: Um SGBD é o software responsável por intermediar o acesso entre os usuários (ou aplicações) e o banco de dados. Ele fornece recursos para definir, criar, consultar e atualizar os dados, além de garantir a segurança, o controle de acesso concorrente e a integridade das informações.

## Q2.
**Enunciado:** Quais os principais problemas de utilizar Sistemas de Arquivos para armazenagem de dados?

### Resposta

#### Inconsistência e redundância de dados:
- A mesma informação inserida em diferentes arquivos;
- Se um dado for atualizado, as demais copias não seram alteradas.
#### Dificuldade de Acesso e Consulta:
- Para buscar dados específicos em um sistema de arquivos é necessário escrever programas ou scripts customizados para cada tipo de consulta;;
- Filtrar, cruzar e relacionar dados distribuídos em múltiplos arquivos exige um esforço computacional alto e implementação manual complexa.
#### Isolamento e Fragmentação dos Dados:
- Os dados ficam espalhados em formatos distintos, estruturados de maneiras diferentes e sob estruturas de pastas independentes.
#### Problemas de Integridade dos Dados:
- É extremamente difícl impor regras de validção no sistema de arquivos;
- Qualquer validação precisa ser feita diretamente no codigo.
#### Problemas de Atomicidade:
- Se uma operação que manipula vários arquivos for interrompida, alguns arquivos vão ser modificados e outros não, deixando o sistema em um estado corrompido;
- Em caso de falha, deve-se garantir que o banco volte ao estado anterior da realização das operações. Difícil fazer isso em um sistema de arquivos.
#### Anomalias no Acesso Concorrente:
- Varios acessos a um mesmo arquivo podem acabar gerando incosistência nos dados;
- Os dados podem sofrer acessos de diferentes programas e supervizionar isso é difícil.
#### Segurança:
- Não é possível aplicar restrições no nível do dado (por exemplo, permitir que um funcionário veja a coluna "Nome", mas não a coluna "Salário" dentro do mesmo documento).

## Q3.
**Enunciado:** Explique as propriedades **ACID**: atomicidade, consistência, isolamento e durabilidade. Para cada propriedade, descreva um exemplo prático no contexto de uma transferência bancária e explique o que aconteceria se o SGBD não garantisse essa propriedade.

### Resposta

#### Atomicidade:
Cada transação é tratada como uma unica unidade, ou todas as operações que a envolvem são executadas com sucesso ou nenhum é aplicada ("Tudo ou nada").

**Exemplo:** O dinheiro é debitado da Conta A (o valor é descontado), mas o sistema falha antes de creditar na Conta B. Sem a Atomocidade para fazer o rollback (desfazer o débito), o dinheiro simplesmente "some" do sistema. A Conta A perdeu o valor e a Conta B nunca o recebeu.

#### Consistência:
Assegura que uma transação leve o banco de um estado válido para outro estado válido, respeitando todas as regras, restrições e integridades estruturais antes e depois da execução.

**Exemplo:** O cliente tenta transferir R$ 500, mas só possui R$ 200. Sem a consistência, o sistema aceitaria a transação, gravaria um saldo de -R$ 300 e deixaria o banco de dados em um estado inválido, quebrando as regras e invariantes definidas no sistema.

#### Isolamento:
Determina que transações concorrentes ocorram de forma isolada umas das outras. O resultado de uma transação executada simultaneamente deve ser o mesmo se fossem rodadas de forma sequencial. Nenhuma transação em andamento pode interferir ou ver dados intermediários não confirmados de outra transação.

**Exemplo:** O saldo inicial do cliente seja R$ 100, e duas transferências de R$ 50 tentam ler esse saldo exatamente ao mesmo tempo. Se a propriedade do isolamento não for garantida, o sistema pode acabar debitando o valor da primeira transferência e salvar o saldo como R$ 50 e a mesma coisa acontecer para a segunda deixando o saldo final em R$ 50 e não R$ 0 como o esperado, pois uma tranferência interferiu na leitura da outra.

#### Durabilidade:
Significa que, uma vez que uma transação é confirmada (committed), os dados gravados permanecem salvos de maneira permanente no sistema, mesmo em casos de falhas de energia, quedas de sistema ou erros inesperados.

**Exemplo:** Um cliente realiza uma transferência e logo após isso o sistema cai. Se a propriedade de durabilidade não fosse garantida, a transação poderia ser perdida.