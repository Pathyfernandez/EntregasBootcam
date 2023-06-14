class Animal:
    def __init__(self, name, age, health=100, happiness=100):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    def mostrar_info(self):
        print("Nombre:", self.name)
        print("Salud:", self.health)
        print("Felicidad:", self.happiness)

    def alimentar(self):
        self.health += 10
        self.happiness += 10

class Leon(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.roar_power = 50

class Tigre(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.jump_height = 3
