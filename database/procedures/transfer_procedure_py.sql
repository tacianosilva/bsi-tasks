create or replace procedure transfer_py(
    sender int,
    receiver int,
    amount dec
)
language plpython3u
as $$
    # 1. Busca o saldo do remetente
    # plpy.prepare e plpy.execute são usados para interagir com o banco
    plan = plpy.prepare("SELECT balance FROM accounts WHERE id = $1", ["int"])
    rv = plpy.execute(plan, [sender])

    if not rv:
        plpy.notice(f"Conta {sender} não encontrada.")
        return

    current_balance = rv[0]["balance"]

    # 2. Validação do saldo
    if current_balance < amount:
        plpy.notice(f"Transferência cancelada: Saldo insuficiente para o remetente {sender}.")
        return

    # 3. Executa as atualizações
    try:
        # Subtraindo do sender
        plpy.execute(
            plpy.prepare("UPDATE accounts SET balance = balance - $1 WHERE id = $2", ["dec", "int"]),
            [amount, sender]
        )

        # Adicionando ao receiver
        plpy.execute(
            plpy.prepare("UPDATE accounts SET balance = balance + $1 WHERE id = $2", ["dec", "int"]),
            [amount, receiver]
        )

        plpy.notice(f"Transferência de {amount} realizada com sucesso via Python.")

    except Exception as e:
        plpy.error(f"Erro ao processar transferência: {e}")
$$;
