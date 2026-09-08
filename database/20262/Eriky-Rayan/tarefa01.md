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