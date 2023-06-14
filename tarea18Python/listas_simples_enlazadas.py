class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self

    def print_values(self):
        runner = self.head
        while runner is not None:
            print(runner.value)
            runner = runner.next
        return self

    def add_to_back(self, val):
        if self.head is None:
            self.add_to_front(val)
            return self

        new_node = SLNode(val)
        runner = self.head
        while runner.next is not None:
            runner = runner.next
        runner.next = new_node
        return self

    def remove_from_front(self):
        if self.head is None:
            return None

        current_head = self.head
        self.head = current_head.next
        current_head.next = None
        return current_head.value

    def remove_from_back(self):
        if self.head is None:
            return None

        if self.head.next is None:
            return self.remove_from_front()

        runner = self.head
        while runner.next.next is not None:
            runner = runner.next
        current_tail = runner.next
        runner.next = None
        return current_tail.value

    def remove_val(self, val):
        if self.head is None:
            return None

        if self.head.value == val:
            return self.remove_from_front()

        runner = self.head
        while runner.next is not None:
            if runner.next.value == val:
                removed_node = runner.next
                runner.next = runner.next.next
                removed_node.next = None
                return removed_node.value
            runner = runner.next

        return None

    def insert_at(self, val, n):
        if n <= 0:
            return self.add_to_front(val)

        runner = self.head
        for _ in range(n - 1):
            if runner.next is None:
                return self.add_to_back(val)
            runner = runner.next

        new_node = SLNode(val)
        new_node.next = runner.next
        runner.next = new_node
        return self
# Creamos una instancia de SList
my_list = SList()

# Agregamos nodos al frente
my_list.add_to_front("son").add_to_front("Las listas enlazadas").add_to_back("divertidas!")

# Imprimimos los valores de la lista
print("Valores de la lista:")
my_list.print_values()
print()

# Eliminamos el primer nodo y mostramos el valor eliminado
removed_value = my_list.remove_from_front()
print("Valor eliminado:", removed_value)
print("Nueva lista:")
my_list.print_values()
print()

# Eliminamos el último nodo y mostramos el valor eliminado
removed_value = my_list.remove_from_back()
print("Valor eliminado:", removed_value)
print("Nueva lista:")
my_list.print_values()
print()

# Eliminamos un nodo con un valor específico y mostramos el valor eliminado
removed_value = my_list.remove_val("Las listas enlazadas")
print("Valor eliminado:", removed_value)
print("Nueva lista:")
my_list.print_values()
print()

# Insertamos un nuevo nodo en la posición 1
my_list.insert_at("nuevo nodo", 1)
print("Lista después de insertar en la posición 1:")
my_list.print_values()
