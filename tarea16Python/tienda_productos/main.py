from tienda import Tienda
from producto import Producto

# Creamos una instancia de Tienda
tienda = Tienda("La Tienda")

# Creamos algunas instancias de Producto
producto1 = Producto("Manzana", 1000, "Fruta")
producto2 = Producto("Melon", 3000, "Fruta")
producto3 = Producto("Zapallo", 5000, "Vegetal")

# Agregamos los productos a la tienda
tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)
tienda.agregar_producto(producto3)

# Imprimimos la información de los productos en la tienda
print("----Imprimimos la información de los productos en la tienda----")
for producto in tienda.productos:
    producto.print_info()

# Vendemos un producto por su ID
print("----Vendemos un producto por su ID----")
tienda.vender_producto(1)

# Aplicamos una inflación del 10% a los productos en la tienda
print("----Aplicamos una inflación del 10% a los productos en la tienda----")
tienda.inflacion(10)
for producto in tienda.productos:
    producto.print_info()

# Aplicamos una liquidación a los productos de la categoría "Fruta" con un descuento del 50%
print("----Aplicamos una liquidación a los productos de la categoría 'Fruta' con un descuento del 50%----")
tienda.hacer_liquidacion("Fruta", 20)
for producto in tienda.productos:
    producto.print_info()
