md = MathDojo()

# Llamadas a add()
x = md.add(2).add(2, 5, 1).subtract(3, 2).result
print(x)  # debería imprimir 5

# Llamadas a subtract()
y = md.subtract(10, 2).subtract(3).subtract(5).result
print(y)  # debería imprimir -15

# Encadenamiento de métodos
z = md.add(3, 7).subtract(2, 1).add(5).subtract(4, 2, 1).result
print(z)  # debería imprimir 10
