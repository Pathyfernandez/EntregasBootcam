class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.id = None

    def actualizar_precio(self, cambio_porcentaje, esta_elevado):
        if esta_elevado:
            self.precio += self.precio * cambio_porcentaje / 100
        else:
            self.precio -= self.precio * cambio_porcentaje / 100

    def print_info(self):
        print("Nombre:", self.nombre)
        print("Categoría:", self.categoria)
        print("Precio:", self.precio)
