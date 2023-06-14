class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, nuevo_producto):
        self.productos.append(nuevo_producto)

    def vender_producto(self, id_producto):
        if id_producto < len(self.productos):
            producto = self.productos.pop(id_producto)
            producto.print_info()
        else:
            print("No se encontró el producto con el ID proporcionado.")

    def inflacion(self, porcentaje_aumento):
        for producto in self.productos:
            producto.actualizar_precio(porcentaje_aumento, True)

    def hacer_liquidacion(self, categoria, porcentaje_descuento):
        for producto in self.productos:
            if producto.categoria == categoria:
                producto.actualizar_precio(porcentaje_descuento, False)