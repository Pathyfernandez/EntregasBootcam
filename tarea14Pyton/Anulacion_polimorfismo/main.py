# BONUS NINJA: Usa módulos para separar las clases en diferentes archivos.

from ninja import Ninja
from mascota import Mascota

# Crear una instancia de Ninja y una instancia de Mascota
ninja = Ninja("Hiro", "Yamamoto")
mascota = Mascota("Max", "perro")

# Asignar la mascota al ninja
ninja.mascotas.append(mascota)

# Llamar a los métodos del ninja para alimentar, pasear y bañar a la mascota
ninja.alimentar()
ninja.caminar()
ninja.bañar()


# BONUS SENSEI: Usa la herencia para crear subclases de mascotas.

from mascota import Perro, Gato

perro = Perro("Max")
gato = Gato("Whiskers")

perro.sonido()  # Imprime: ¡Guau!
gato.sonido()   # Imprime: ¡Miau!

perro.comer()
gato.jugar()
