class Usuario:
    nombre_banco = "Primer Dojo Nacional"

    def __init__(self, name, email_address):
        self.nombre = name
        self.email = email_address
        self.cuentas = []

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)
        print("Cuenta agregada:", cuenta.numero_cuenta)

    def hacer_deposito(self, numero_cuenta, cantidad):
        for cuenta in self.cuentas:
            if cuenta.numero_cuenta == numero_cuenta:
                cuenta.deposito(cantidad)
                print("Depósito realizado en la cuenta", numero_cuenta)
                break
        else:
            print("El usuario no tiene una cuenta con el número especificado.")

    def hacer_retiro(self, numero_cuenta, cantidad):
        for cuenta in self.cuentas:
            if cuenta.numero_cuenta == numero_cuenta:
                cuenta.retiro(cantidad)
                print("Retiro realizado de la cuenta", numero_cuenta)
                break
        else:
            print("El usuario no tiene una cuenta con el número especificado.")

    def mostrar_balance_usuario(self):
        print("Nombre del usuario:", self.nombre)
        for cuenta in self.cuentas:
            print("Número de cuenta:", cuenta.numero_cuenta)
            print("Saldo actual:", cuenta.saldo)

# Clase CuentaBancaria (sin cambios)
class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo_inicial):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo_inicial

    def deposito(self, cantidad):
        self.saldo += cantidad

    def retiro(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Saldo insuficiente para realizar el retiro.")

# Crear instancias de Usuario y CuentaBancaria
usuario1 = Usuario("Rodrigo", "rodrigo@codingdojo.com")
usuario2 = Usuario("Jesus", "jesus@codingdojo.com")

cuenta1 = CuentaBancaria("123456789", 3000)
cuenta2 = CuentaBancaria("987654321", 5000)

# Agregar cuentas a los usuarios
usuario1.agregar_cuenta(cuenta1)
usuario2.agregar_cuenta(cuenta2)

# Realizar depósitos y retiros en las cuentas
usuario1.hacer_deposito("123456789", 1000)
usuario1.hacer_retiro("123456789", 500)
usuario2.hacer_deposito("987654321", 2000)

# Mostrar balances de los usuarios
usuario1.mostrar_balance_usuario()
usuario2.mostrar_balance_usuario()


