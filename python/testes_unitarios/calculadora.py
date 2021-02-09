#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Este módulo implementa métodos para uma calculadora básica.
Mostra vários tipos de documentação disponíveis para uso com pydoc.
Para gerar documentação HTML para este módulo, comando:

    pydoc -w calculadora

"""

def somar(x, y):
    """
        Soma dois números.

    Args:
        x ([int]): [valor inteiro]
        y ([int]): [valor inteiro]

    Returns:
        [int]: [retorna a soma dos dois números]
    """
    return x + y

def multiplicar(x, y):
    """
        Multiplica dois números.

    Args:
        x ([int]): [valor inteiro]
        y ([int]): [valor inteiro]

    Returns:
        [int]: [retorna o produto dos dois números]
    """
    return x + y

if __name__ == '__main__':
    print('Arquivo calculadora.py.')
