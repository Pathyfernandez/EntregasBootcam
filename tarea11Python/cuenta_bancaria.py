class CuentaBancaria:
    def __init__(self, balance=0, tasa_interes=0):
        self.balance = balance
        self.tasa_interes = tasa_interes

    def deposito(self, amount):
        self.balance += amount

    def retiro(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5

    def mostrar_info_cuenta(self):
        print(f"Balance: ${self.balance}")

    def generar_interes(self):
        if self.balance > 0:
            self.balance += self.balance * self.tasa_interes


cuenta1 = CuentaBancaria(tasa_interes=0.02)
cuenta1.deposito(100)
cuenta1.deposito(200)
cuenta1.deposito(300)
cuenta1.retiro(50)
cuenta1.generar_interes()
cuenta1.mostrar_info_cuenta()

cuenta2 = CuentaBancaria(tasa_interes=0.03)
cuenta2.deposito(500)
cuenta2.deposito(300)
cuenta2.retiro(200)
cuenta2.retiro(100)
cuenta2.retiro(50)
cuenta2.retiro(50)
cuenta2.generar_interes()
cuenta2.mostrar_info_cuenta()


class CuentaBancaria:
    cuentas = []

    def __init__(self, balance=0, tasa_interes=0):
        self.balance = balance
        self.tasa_interes = tasa_interes
        self.cuentas.append(self)

    @classmethod
    def mostrar_info_cuentas(cls):
        for cuenta in cls.cuentas:
            cuenta.mostrar_info_cuenta()



CuentaBancaria.mostrar_info_cuentas()

