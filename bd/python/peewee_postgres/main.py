from models import Funcionario


def connect():
    funcionarios = Funcionario.select()
    for funcionario in funcionarios:
        print(funcionario.codigo, funcionario.nome, funcionario.supervisor, funcionario.coddepto)
        print(funcionario.supervisor)
        print(funcionario.coddepto)

if __name__ == '__main__':
    connect()
