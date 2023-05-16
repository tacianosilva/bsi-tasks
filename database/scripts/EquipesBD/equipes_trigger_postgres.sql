-- Criação da função que será chamada no Gatilho
CREATE FUNCTION aumenta_salario()
RETURNS trigger LANGUAGE 'plpgsql'
AS $BODY$
BEGIN
UPDATE funcionario f
SET salario = salario * 1.01
WHERE f.codigo = (SELECT m.codfuncionario FROM membro m
                  WHERE m.codigo = NEW.codmembro);
RETURN NEW;
END;
$BODY$;

-- Criação do Gatilho para execução depois do INSERT na tabela atividade_membro
CREATE TRIGGER aumenta_salario_nova_atividade
    AFTER INSERT
    ON public.atividade_membro
    FOR EACH ROW
    EXECUTE PROCEDURE public.aumenta_salario();
