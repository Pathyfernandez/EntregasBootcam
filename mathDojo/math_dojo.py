class MathDojo:
    def __init__(self):
        self.result = 0
    
    def add(self, num, *nums):
        self.result += num
        for n in nums:
            self.result += n
        return self
    
    def subtract(self, num, *nums):
        self.result -= num
        for n in nums:
            self.result -= n
        return self


# Crear una instancia
md = MathDojo()

# Prueba del método 'add'
print("---Sumar---")
x = md.add(2).add(2, 5, 1).add(10).result
print(x)  


# Prueba del método 'subtract'
print("---Restar---")
y = md.subtract(3, 2).subtract(1).result
print(y)  

# Prueba encadenando métodos
print("---Encadenar---")
z = md.add(5).subtract(3).add(10, 2).subtract(7, 2, 1).result
print(z)  
