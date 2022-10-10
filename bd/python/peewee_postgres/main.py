from models import Funcionario


def connect():
    funcionarios = Funcionario.select()
    for funcionario in funcionarios:
        print(funcionario.codigo, funcionario.nome)

if __name__ == '__main__':
    connect()
