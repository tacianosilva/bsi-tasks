from orm_atividades import db, Projeto, Atividade, initialize

def main():
    initialize()

    try:
        # Inserir uma atividade em algum projeto
        print("Inserindo uma atividade em um projeto...")
        # Assumindo que o projeto com código 1 existe (inserido anteriormente)
        projeto = Projeto.get_or_none(Projeto.codigo == 1)
        if projeto:
            atividade = Atividade.create(
                descricao="Atividade 2 do Projeto A via ORM",
                codprojeto=projeto,
                datainicio='2024-03-01',
                datafim='2024-03-31'
            )
            print(f"Atividade inserida: {atividade.descricao}")
        else:
            print("Projeto não encontrado.")

        # Atualizar o líder de algum projeto
        print("\nAtualizando o líder de um projeto...")
        projeto = Projeto.get_or_none(Projeto.codigo == 1)
        if projeto:
            # Assumindo funcionário com código 3 (Maria)
            from orm_atividades import Funcionario
            lider = Funcionario.get_or_none(Funcionario.codigo == 3)
            if lider:
                projeto.codresponsavel = lider
                projeto.save()
                print(f"Líder do projeto '{projeto.nome}' atualizado para {lider.nome}")
            else:
                print("Líder não encontrado.")
        else:
            print("Projeto não encontrado.")

        # Listar todos os projetos e suas atividades
        print("\nListando todos os projetos e suas atividades:")
        projetos = Projeto.select()
        for proj in projetos:
            print(f"Projeto: {proj.nome} - {proj.descricao}")
            atividades = Atividade.select().where(Atividade.codprojeto == proj)
            if atividades:
                for atv in atividades:
                    print(f"  Atividade: {atv.descricao}")
            else:
                print("  Nenhuma atividade.")

    except Exception as e:
        print(f"Erro: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    main()