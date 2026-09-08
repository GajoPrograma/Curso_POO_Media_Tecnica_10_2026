import unittest


class Cuenta:
    def __init__(self, saldo):
        if type(saldo) is not int or saldo < 0:
            raise ValueError("Saldo inválido")
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    def retirar(self, monto):
        if type(monto) is not int or monto <= 0 or monto > self.saldo:
            raise ValueError("Retiro inválido")
        self._saldo -= monto


class PruebasCuenta(unittest.TestCase):
    def test_retiro_valido(self):
        cuenta = Cuenta(10)
        cuenta.retirar(3)
        self.assertEqual(cuenta.saldo, 7)

    def test_rechazo_conserva_saldo(self):
        cuenta = Cuenta(10)
        with self.assertRaises(ValueError):
            cuenta.retirar(-2)
        self.assertEqual(cuenta.saldo, 10)


if __name__ == "__main__":
    unittest.main()
