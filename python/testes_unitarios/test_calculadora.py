"""
    Testes de Unidade da calculadora.py.
"""
import unittest

import calculadora

class CalculadoraTest(unittest.TestCase):
    """
        Classe de Teste da calculadora.

    Args:
        unittest ([TestCase]): Testa as funções da calculadora.
    """

    def test(self):
        """
            Testa a função de soma para dois números.
        """
        self.assertEqual(calculadora.somar(3, 5), 8)

if __name__ == '__main__':
    unittest.main()
