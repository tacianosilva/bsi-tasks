from models import Departamento, Funcionario, initialize
import datetime


def main():
    departamentos = Departamento.select()
    for departamento in departamentos:
        print(departamento.codigo, departamento.sigla)

    funcionarios = Funcionario.select()
    for funcionario in funcionarios:
        print(funcionario.codigo, funcionario.nome, funcionario.supervisor, funcionario.depto)


def inserir():
    d1 = Departamento.create(
        sigla='DCT',
        descricao='Departamento de Computação e Tecnologia'
    )
    d1.save()

    f1 = Funcionario.create(
        nome='Carl Sagan',
        sexo='M',
        dtnasc=datetime.date(1934, 11, 9),
        salario=10000.00,
        depto=d1.codigo
    )
    f1.save()


if __name__ == '__main__':
    initialize()
    inserir()
    main()
