# Archivo: mascota.py

class Mascota:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.golosinas = 0
        self.salud = 100
        self.energia = 100

    def dormir(self):
        self.energia = 100
        print(f"{self.nombre} ha dormido y recuperado energía.")

    def comer(self):
        if self.golosinas > 0:
            self.golosinas -= 1
            self.salud += 10
            print(f"{self.nombre} ha comido y aumentado su salud.")
        else:
            print("No hay golosinas para la mascota.")

    def jugar(self):
        if self.energia >= 10:
            self.energia -= 10
            print(f"{self.nombre} está jugando y gastando energía.")
        else:
            print("La mascota no tiene suficiente energía para jugar.")

    def sonido(self):
        print("La mascota no emite sonido.")

    def limpiar(self):
        print(f"{self.nombre} ha sido bañado.")


class Perro(Mascota):
    def __init__(self, nombre):
        super().__init__(nombre, "perro")

    def sonido(self):
        print("¡Guau!")


class Gato(Mascota):
    def __init__(self, nombre):
        super().__init__(nombre, "gato")

    def sonido(self):
        print("¡Miau!")
