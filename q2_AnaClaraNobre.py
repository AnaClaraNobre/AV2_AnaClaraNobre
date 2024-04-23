import unittest
from q1_AnaClaraNobre import *

class TestBanco(unittest.TestCase):
    def setUp(self):
        self.banco = Banco()
        criar_conta(self.banco, "Alice", "1234", 1500)

    test_criar_conta = lambda self: self.assertEqual(len(self.banco['contas']), 1)

    test_logar_conta = lambda self: self.assertIsNotNone(logar_conta(self.banco, "Alice", "1234"))

    test_sacar = lambda self: self.assertTrue(sacar(logar_conta(self.banco, "Alice", "1234"), 500))
    # test_sacar_Error = lambda self: self.assertTrue(sacar(logar_conta(self.banco, "Alice", "1234"), 1600)) # Caso queira sacar um valor maior que o saldo

    test_credito = lambda self: self.assertIsNotNone(credito(logar_conta(self.banco, "Alice", "1234"), 1000))
    

    test_transferencia = lambda self: transferencia(logar_conta(self.banco, "Alice", "1234"), "Carol", 1000, pessoas, self.banco['contas'])
    # test_transferencia_Error1 = lambda self: transferencia(logar_conta(self.banco, "Alice", "1234"), "Carol", 1600, pessoas, self.banco['contas'])# caso queira transferir um valor maior do que o seu saldo
    # test_transferencia_Error2 = lambda self: transferencia(logar_conta(self.banco, "Alice", "1234"), "Pedro", 1000, pessoas, self.banco['contas'])# caso queira transferir um valor para alguem que não existe

if __name__ == '__main__':
    unittest.main()
