class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class ListaDoblementeEnlazada:
    def __init__(self):
        self.head = None

    def agregar(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def eliminar(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next

    def insertar_despues_de(self, data, new_data):
        new_node = Node(new_data)
        current = self.head
        while current:
            if current.data == data:
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                return
            current = current.next

    def imprimir(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

lista = ListaDoblementeEnlazada()

lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
lista.imprimir()  # Output: 1 2 3

lista.eliminar(2)
lista.imprimir()  # Output: 1 3

lista.insertar_despues_de(1, 4)
lista.imprimir()  # Output: 1 4 3


"""
¿Cómo sabrías si tienes una lista enlazada circular?
Para saber que tiengo una lista enlazada circular, tomare como ejemplo utilizar el algoritmo del "runner" o "tortuga y liebre". Este algoritmo implica tener dos punteros, uno que se mueve a una velocidad de un nodo por iteración (la tortuga) y otro que se mueve a una velocidad de dos nodos por iteración (la liebre). Si la lista es circular, en algún momento la liebre alcanzará a la tortuga y ambos punteros coincidirán. Si la liebre llega al final de la lista (es decir, encuentra un nodo nulo), entonces la lista no es circular.

¿Cómo llegarías a la mitad de la lista enlazada?
Para llegar a la mitad de una lista enlazada, puedes utilizar el algoritmo del "runner" mencionado anteriormente. En este caso, la tortuga se mueve a una velocidad de un nodo por iteración y la liebre se mueve a una velocidad de dos nodos por iteración. Cuando la liebre llega al final de la lista (o alcanza un nodo nulo), la tortuga estará en la mitad de la lista.

¿Cómo eliminarías los valores duplicados de la lista?
Para eliminar los valores duplicados de una lista enlazada, puedes utilizar un diccionario para realizar un seguimiento de los valores que ya has encontrado. Recorre la lista enlazada y, para cada nodo, verifica si su valor ya está presente en el diccionario. Si lo está, elimina el nodo de la lista. Si no está presente, agrega el valor al diccionario y continúa recorriendo la lista.

¿Cómo invertirías los valores de la lista?
Para invertir los valores de una lista enlazada, puedes utilizar un enfoque iterativo o recursivo. Enfoquémonos en el enfoque iterativo aquí. Puedes utilizar tres punteros: prev, current y next. Inicialmente, prev se establece en None, current se establece en el primer nodo de la lista y next se establece en el siguiente nodo de current. Luego, para cada nodo, cambia los enlaces next y prev del nodo actual y mueve los punteros prev, current y next al siguiente nodo. Al final, establece el nodo actual como la nueva cabeza de la lista.


"""