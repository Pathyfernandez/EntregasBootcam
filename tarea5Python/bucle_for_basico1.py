
#Básico: imprime todos los números enteros del 0 al 150.
for i in range(0,151):
    print(i)

#Múltiplos de cinco: imprime todos los múltiplos de 5 entre 5 y 1,000.
for i in range(5,1001,5):
    print(i)

#Contar, a la manera del Dojo: imprime números enteros del 1 al 100. Si es divisible por 5, imprime #"Coding” en su lugar. Si es divisible por 10, imprime "Coding Dojo" 

def printNumbers(x):
    for i in range(1,x):
        if i % 10 == 0:
            print("Coding Dojo")
        elif i % 5 == 0:
            print("Coding")
        else:
            print(i)
printNumbers(101)


# Whoa. Es un gran idiota: agrega los enteros impares del 0 al 500,000, e imprime la suma final.

def suma_impares():
    suma = 0
    for i in range(1, 500001, 2):
        suma += i
    print("La suma final de los enteros impares del 0 al 500,000 es:", suma)
suma_impares()

# Cuenta regresiva de a 4: imprime números positivos comenzando desde el 2018, en cuenta regresiva de 4 en 4.
def cuenta_regresiva():
    numero = 2018
    while numero >= 0:
        print(numero)
        numero -= 4
cuenta_regresiva()


#Contador flexible: establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, imprime solo los enteros que sean múltiplos de mult. Por ejemplo, si lowNum=2, highNum=9 y mult=3. El bucle debe imprimir 3, 6, 9 (en líneas sucesivas)

lowNum = 8
highNum = 32
mult = 3
for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)




