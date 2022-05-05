# Exemplos de Gatilhos (Triggers)

## PostgreSQL

A criação de **trigger** no **postgresql**, tem uma sintaxe diferente da utilizada no _MySQL_ e _MariaDB_. Considere o seguinte esquema relacional:

```plpgsql
CREATE TABLE usuario ( 
	id SERIAL,
	nome VARCHAR(500) NOT NULL, 
	email VARCHAR(100) NOT NULL,
	PRIMARY KEY (id) 
);

CREATE TABLE fidelidade ( 
	id SERIAL,
	user_id SERIAL NOT NULL, 
	pontos INT NOT NULL DEFAULT '0',
	PRIMARY KEY (id),
	FOREIGN KEY (user_id) REFERENCES usuario(id) 
);

CREATE TABLE venda ( 
	id SERIAL,
	produto VARCHAR(250) NOT NULL, 
	valor MONEY NOT NULL,
	user_id SERIAL NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (user_id) REFERENCES usuario(id)
);
```

A criação é dividida em duas partes:

1) Criação de uma função do tipo **trigger**;
```PLpgSQL
CREATE FUNCTION inserir_cartao() 
RETURNS trigger AS $$
BEGIN
  INSERT INTO fidelidade(user_id, pontos) 
  values (NEW.id, 0);
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

2) Criação do **trigger** no evento do banco de dados;
```PLpgSQL
CREATE TRIGGER criar_cartao 
AFTER INSERT ON usuario
    FOR EACH ROW 
    EXECUTE FUNCTION inserir_cartao();
```

Na imagem, é apresentado a visão do pgAdmin, onde podemos ver a associação do gatilho na tabela e a função do tipo trigger que será chamada.

![image](https://user-images.githubusercontent.com/2486325/166718849-c7d59d2c-aa64-4f7d-aa4e-255ace3b4662.png)

## MariaDB
