# Archivo: ninja.py

class Ninja:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.mascotas = []
        self.premio = None
        self.comida_mascota = None

    def caminar(self):
        print(f"{self.nombre} está caminando.")

    def alimentar(self):
        if self.comida_mascota:
            for mascota in self.mascotas:
                mascota.comer()
        else:
            print("No se ha asignado comida para las mascotas.")

    def bañar(self):
        for mascota in self.mascotas:
            mascota.limpiar()






