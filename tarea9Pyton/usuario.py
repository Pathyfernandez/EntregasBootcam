class Usuario:
    nombre_banco = "Primer Dojo Nacional"

    def __init__(self, name, email_address, saldo):
        self.nombre = name
        self.email = email_address
        self.saldo = saldo

    def hacer_depósito(self, cantidad):
        self.saldo += cantidad
        print("Depósito realizado. Saldo actual:", self.saldo)

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print("Retiro realizado. Saldo actual:", self.saldo)
        else:
            print("Saldo insuficiente para realizar el retiro.")

    def transferir(self, cantidad, destino):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            destino.hacer_depósito(cantidad)
            print("Transferencia realizada. Saldo actual:", self.saldo)
        else:
            print("Saldo insuficiente para realizar la transferencia.")

    def mostrar_balance_usuario(self):
        print("Nombre del usuario:", self.nombre)
        print("Saldo actual:", self.saldo)


# Crear instancias de Usuario
usuario1 = Usuario("Rodrigo", "rodrigo@codingdojo.com", 30000)
usuario2 = Usuario("Jesus", "jesus@codingdojo.com", 5000)
usuario3 = Usuario("Pepita", "papita@codingdojo.com", 1000)

# Realizar depósitos en la cuenta del usuario
usuario1.hacer_depósito(1000)
usuario1.hacer_depósito(2000)
usuario1.hacer_depósito(500)
usuario2.hacer_depósito(500)
usuario3.hacer_depósito(10000)

# Realizar retiros en la cuenta del usuario
usuario1.retirar(6000)
usuario2.retirar(1000)
usuario3.retirar(5000)
usuario3.retirar(500)
usuario3.retirar(800)

# Transferir dinero del primer usuario al tercer usuario
usuario1.transferir(600, usuario3)

# Mostrar los balances de los usuarios
usuario1.mostrar_balance_usuario()
usuario2.mostrar_balance_usuario()
usuario3.mostrar_balance_usuario()






