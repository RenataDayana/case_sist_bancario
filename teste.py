import unittest
from decimal import Decimal
from seu_arquivo import ContaBancaria  # Substitua 'seu_arquivo' pelo nome do seu arquivo

class TestContaBancaria(unittest.TestCase):

    def setUp(self):
        """Configura o ambiente de teste."""
        self.conta1 = ContaBancaria(Decimal('100.00'))
        self.conta2 = ContaBancaria(Decimal('200.00'))

    def test_depositar(self):
        self.conta1.depositar(Decimal('50.00'))
        self.assertEqual(self.conta1.saldo, Decimal('150.00'))

    def test_sacar(self):
        self.conta1.sacar(Decimal('30.00'))
        self.assertEqual(self.conta1.saldo, Decimal('70.00'))

    def test_sacar_saldo_insuficiente(self):
        with self.assertRaises(ValueError):
            self.conta1.sacar(Decimal('200.00'))

    def test_transferir(self):
        self.conta1.transferir(self.conta2, Decimal('50.00'))
        self.assertEqual(self.conta1.saldo, Decimal('50.00'))
        self.assertEqual(self.conta2.saldo, Decimal('250.00'))

    def test_transferir_saldo_insuficiente(self):
        with self.assertRaises(ValueError):
            self.conta1.transferir(self.conta2, Decimal('200.00'))

    def test_depositar_valor_negativo(self):
        with self.assertRaises(ValueError):
            self.conta1.depositar(Decimal('-10.00'))

    def test_sacar_valor_negativo(self):
        with self.assertRaises(ValueError):
            self.conta1.sacar(Decimal('-10.00'))

    def test_transferir_valor_negativo(self):
        with self.assertRaises(ValueError):
            self.conta1.transferir(self.conta2, Decimal('-10.00'))

if __name__ == "__main__":
    unittest.main()
