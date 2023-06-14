from animal import Animal, Leon, Tigre

class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def agregar_leon(self, name, age):
        self.animals.append(Leon(name, age))

    def agregar_tigre(self, name, age):
        self.animals.append(Tigre(name, age))

    def imprimir_toda_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.mostrar_info()
