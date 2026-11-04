# Tarefa 03 - Docker e SGBD

## Identificação e repositório

- **Discente:** Isaac Vilton
- **Usuário no GitHub:** Isaac-Ribeiro
- **E-mail acadêmico:** isaac.ribeiro.018@ufrn.edu.br
- **Repositório pessoal:** https://github.com/Isaac-Ribeiro/Banco_de_Dados_UFRN.git

## Perguntas Discursivas

## Pergunta Discursiva 1

Criar uma tabela é uma operação de **DDL** (Data Definition Language), pois define a estrutura do banco de dados: o nome da tabela, suas colunas, tipos de dados, chaves e restrições. Já inserir registros é uma operação de **DML** (Data Manipulation Language), pois adiciona dados nas estruturas que foram previamente criadas.

Ao executar `DROP TABLE`, a tabela é excluída juntamente com todos os registros armazenados nela. Essa operação remove tanto a estrutura quanto os dados e, por isso, deve ser utilizada com cuidado. Em geral, os dados não podem ser recuperados por comandos SQL comuns após a exclusão da tabela, a menos que exista um backup ou outro mecanismo de recuperação.

## Pergunta Discursiva 2

Ao tentar executar `DROP TABLE autores` com a conta `app_biblioteca`, o MariaDB recusou a operação e retornou o erro 1142, informando que esse usuário não possui permissão para executar o comando `DROP`. Isso aconteceu porque a conta foi criada com privilégios de `SELECT`, `INSERT`, `UPDATE` e `DELETE`, mas não recebeu privilégios de DDL, como `DROP`, `CREATE` ou `ALTER`.

Essa restrição protege a integridade do banco de dados porque impede que uma aplicação web, mesmo em caso de invasão ou falha de programação, exclua tabelas e estruturas importantes. Assim, a conta da aplicação pode manipular os registros necessários para o funcionamento do sistema, mas não pode destruir ou modificar a estrutura do banco. A administração das tabelas deve ser realizada separadamente por uma conta com privilégios elevados.

## Pergunta Discursiva 3

Os usuários foram criados com o host `'%'` porque o MariaDB precisa aceitar conexões originadas de outros contêineres, como o CloudBeaver, e não apenas conexões locais no próprio contêiner do banco. O símbolo `%` funciona como curinga e permite que o usuário se autentique a partir de diferentes endereços de rede.

Se fosse utilizado `'localhost'`, o acesso ficaria restrito ao próprio contêiner do MariaDB, e as conexões vindas do CloudBeaver seriam recusadas. A rede interna criada pelo Docker Compose permite que os contêineres se comuniquem usando o nome do serviço, como `mariadb`. Por isso, o host `%` é necessário para que as contas possam ser utilizadas nessa comunicação entre contêineres.

## Pergunta Discursiva 4

Antes da carga expandida, a base possuía 4 autores e 5 livros. A execução do script adicionou mais 10 autores e 26 livros. Portanto, ao final da carga, ficaram cadastrados **14 autores e 31 livros** no total.

Se fosse inserido um livro com `autor_id = 999`, o MariaDB recusaria a operação, pois não existe um autor com esse identificador na tabela `autores`. A regra que impede essa inserção é a **restrição de chave estrangeira** (`FOREIGN KEY (autor_id) REFERENCES autores(id)`), que garante a integridade referencial entre as tabelas `livros` e `autores`.

## Pergunta Discursiva 5

As Consultas 4 e 5 mostram como as tabelas `autores` e `livros` podem ser relacionadas por meio da chave estrangeira `autor_id`. A principal vantagem de manter essas informações em tabelas separadas é evitar a repetição do nome e do país do autor em todos os livros escritos por ele.

Essa organização reduz a duplicação de dados e o espaço utilizado, além de facilitar atualizações. Se o país de um autor mudar ou tiver sido cadastrado incorretamente, basta alterar essa informação em um único registro da tabela `autores`. A separação também evita inconsistências, pois a chave estrangeira garante que cada livro esteja associado a um autor existente. Esse modelo segue o princípio da normalização e torna as consultas e a manutenção do banco mais confiáveis.

## Desafios Práticos

### Bloco A - Docker e infraestrutura de ambiente

#### 1. Alteração de porta do SGBD

Para alterar a porta publicada pelo MariaDB, a variável `MARIADB_PORT` do arquivo `.env` deve ser ajustada:

```env
MARIADB_PORT=3307
```

Em seguida, os serviços devem ser recriados:

```powershell
cd "Tarefa 03"
docker compose down
docker compose up -d
docker ps
```

O arquivo `docker-compose.yml` mapeia a porta do computador para a porta interna do MariaDB:

```yaml
ports:
  - "${MARIADB_PORT:-3306}:3306"
```

Assim, a conexão externa deve utilizar a porta `3307`, enquanto a porta interna do MariaDB continua sendo `3306`. No CloudBeaver, a conexão deve usar:

- **Host:** `mariadb`
- **Porta:** `3306`, quando a conexão é feita entre contêineres pela rede interna do Docker.

A porta `3307` é necessária apenas para conexões originadas no computador hospedeiro.

#### 2. Dois ambientes simultâneos

Para executar dois ambientes em paralelo, cada projeto deve possuir uma configuração independente. É necessário utilizar portas publicadas diferentes, volumes distintos e nomes de contêineres diferentes. Por exemplo:

| Ambiente | MariaDB | CloudBeaver | Volume |
|---|---:|---:|---|
| Tarefa 03 | 3307 | 8978 | `tarefa03_mariadb_data` |
| Ambiente 2 | 3308 | 8979 | `ambiente2_mariadb_data` |

Além disso, os `container_name` devem ser exclusivos, como `lab-mariadb` e `lab2-mariadb`. Dessa forma, não há conflito entre portas, nomes dos contêineres ou dados persistidos nos volumes.

#### 3. Persistência do volume e alteração da senha root

Alterar `MARIADB_ROOT_PASSWORD` no `.env` e executar novamente `docker compose up -d` não altera a senha existente quando o volume `mariadb_data` já foi inicializado. A imagem do MariaDB utiliza essa variável apenas durante a primeira inicialização do diretório de dados. Depois disso, a senha fica armazenada no próprio banco de dados persistido.

Existem dois caminhos para aplicar uma nova senha:

1. Manter o volume e alterar a senha diretamente no MariaDB, conectado como root:

   ```sql
   ALTER USER 'root'@'localhost' IDENTIFIED BY 'NovaSenhaSegura';
   FLUSH PRIVILEGES;
   ```

2. Destruir o ambiente e o volume, recriando o banco com a senha do `.env`:

   ```powershell
   docker compose down -v
   docker compose up -d
   ```

   O segundo caminho apaga permanentemente os dados armazenados no volume e só deve ser usado quando isso for intencional ou quando houver backup.

#### 4. Validação estrita da senha

O serviço MariaDB usa a interpolação obrigatória:

```yaml
MARIADB_ROOT_PASSWORD: ${MARIADB_ROOT_PASSWORD:?defina MARIADB_ROOT_PASSWORD no arquivo .env}
```

Se o arquivo `.env` for removido ou a variável for deixada vazia, o Docker Compose interrompe a operação antes de criar o serviço e informa que `MARIADB_ROOT_PASSWORD` precisa ser definida no arquivo `.env`.

O modificador `:?` é importante porque impede que o ambiente seja iniciado sem uma senha explicitamente configurada. Em um ambiente profissional, essa validação evita configurações incompletas e reduz o risco de iniciar um banco de dados com credenciais inseguras ou inválidas.

#### 5. Inspeção das variáveis interpoladas

Com o arquivo `.env` presente, o comando abaixo foi executado dentro da pasta da tarefa:

```powershell
docker compose config
```

As seguintes variáveis foram resolvidas pelo Compose:

- `MARIADB_ROOT_PASSWORD` -> valor definido localmente no `.env`;
- `MARIADB_DATABASE` -> `labdb`;
- `MARIADB_PORT` -> `3306`;
- `CLOUDBEAVER_PORT` -> `8978`.

O resultado também confirmou os mapeamentos `3306:3306` e `8978:8978`, o volume nomeado `mariadb_data` e os serviços `mariadb` e `cloudbeaver`.
