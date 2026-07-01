create or replace procedure transfer(
   sender int,
   receiver int,
   amount dec
)
language plpgsql
as $$
declare
    current_balance dec;
begin
    -- 1. Obtém o saldo atual do sender
    select balance into current_balance
    from accounts
    where id = sender;

    -- 2. Verifica se o saldo é suficiente
    if current_balance < amount then
        raise notice 'Transferência cancelada: Saldo insuficiente para o remetente %.', sender;
        return; -- Interrompe a execução
    end if;

    -- 3. Executa a transferência
    update accounts
    set balance = balance - amount
    where id = sender;

    update accounts
    set balance = balance + amount
    where id = receiver;

    -- Nota: O 'commit' em procedures PL/pgSQL encerra a transação atual.
    commit;

    raise notice 'Transferência de % concluída com sucesso.', amount;
end;
$$;
