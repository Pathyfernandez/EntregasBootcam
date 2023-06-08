

# 1.- Actualizar valores en diccionarios y listas

# a.-Cambia el valor 10 en x a 15.
x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
print ("x:", x)

#  Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].


# b.-Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.

estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

estudiantes[0]['last_name'] = 'Bryant'
print ("estudiantes:", estudiantes)



# c.- En el directorio_deportes, cambia "Messi" por "Andrés". 

directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}

directorio_deportes["fútbol"][0] = 'Andrés'
print ("directorio_deportes:", directorio_deportes)


# d.- Cambia el valor 20 en z a 30.


z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 30
print ("z:", z)

# 2.-Iterar a través de una lista de diccionarios: Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios, la función recorra cada diccionarios de la lista e imprima cada llave y el valor asociado. Por ejemplo, dada la siguiente lista:



def iterateDictionary(some_list):
    for dictionary in some_list:
        output = ""
        for key , value in dictionary.items():
            output += f"{key} - {value}, "
            print(output)

estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
iterateDictionary(estudiantes)



# debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;


# un bonus para que aparezcan exactamente como se muestra a continuación)

#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel


# 3.-Obtener valores de una lista de diccionarios: Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, la función imprima el valor almacenado en esa clave para cada diccionario. Por ejemplo, iterateDictionary2('name', estudiantes) debería generar:

def iterateDictionary2(key_name, some_list):
    for dictionary in some_list:
        if key_name in dictionary:
            print(dictionary[key_name])

estudiantes = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

iterateDictionary2('first_name', estudiantes)



# Y iterateDictionary2('last_name', estudiantes) debería generar:

def iterateDictionary2(last_name, some_list):
    for dictionary in some_list:
        if last_name in dictionary:
            print(dictionary[last_name])

estudiantes = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

iterateDictionary2('last_name', estudiantes)



# 4.- Iterar a través de un diccionarios con valores de lista:Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todos listas, imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores asociados dentro de la lista de cada clave. Por ejemplo:dojo = {
#'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
# 'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']}
#printInfo(dojo)
# salida:
#7 UBICACIONES
#San Jose
#Seattle
#Dallas
#Chicago
#Tulsa
#DC
#Burbank
    
#8 INSTRUCTORES
#Michael
#Amy
#Eduardo
#Josh
#Graham
#Patrick
#Minh
#Devon



def print_info(some_dict):
    for key in some_dict:
        print(len(some_dict[key]), key.upper())
        for value in some_dict[key]:
            print(value)


dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
    }
print_info(dojo)



