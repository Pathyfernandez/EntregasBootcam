# 1. TAREA: imprime "Hola, mundo"
print( "Hola, mundo" )


# 2. imprime "Hola, Noelle" con el nombre en una variable
name = "Noelle"
print( "Hola", name)	# con una coma
print( "Hola" + " " + name)	# con un +


# 3. imprimir "Hola 42!" con el número en una variable
name = 42
print( "Hola", name )	# con una coma
#print( "Hola" + " " + name )	# con una +	-- este debería arrojar un error!
print("Hola" + " " + str(name ))


# 4. imprimir "Amo comer sushi y pizza" con las comidas en variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print ( "Amo comerm {} y {}".format(fave_food1, fave_food2)) # con .format()
print (f"Amo comer {fave_food1} y {fave_food2}") # con una cadena f

# 5. listas

cajón = ['documentos', 'sobres', 'lápices']
# acceder al cajón con índice 0 y valor print
print(cajón[0])  # imprime documentos
# acceder al cajón con índice 1 y  valor print
print(cajón[1]) # imprime sobres
# acceder al cajón con índice 2 y valor print
print(cajón[2]) # imprime lápices

# Agregar elementos

x = [1,2,3,4,5]
x.append(99)
print(x)


