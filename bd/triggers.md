# Exemplos de Gatilhos (Triggers)

## PostgreSQL

Pessoal, tivemos nosso encontro de reposição hoje e falamos sobre **trigger** no **postgresql**. 
Que é dividido em duas partes:

1) Criação de uma função do tipo **trigger**;
```postgresql
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
```postgresql
CREATE TRIGGER criar_cartao 
AFTER INSERT ON usuarios
    FOR EACH ROW 
    EXECUTE FUNCTION inserir_cartao();
```

Na imagem, é apresentado a visão do pgAdmin, onde podemos ver a associação do gatilho na tabela e a função do tipo trigger que será chamada.

![image](https://user-images.githubusercontent.com/2486325/166718849-c7d59d2c-aa64-4f7d-aa4e-255ace3b4662.png)

## MariaDB
