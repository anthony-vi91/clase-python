inventario = {"manzana": 4, "pera": 5, "naranja": 10, "mandarina":4}
print(inventario)
#Agregar un nuevo producto
nuevo_producto = input("Ingresa el nombre del nuevo producto: ")
cantidad = int(input("Ingresa la cantidad en stock: "))

inventario[nuevo_producto] = cantidad  # Se agrega al diccionario

print("Producto agregado correctamente.\n")

#Actualizar la cantidad de un producto existente
producto_actualizar = input("Ingresa el nombre del producto a actualizar: ")

if producto_actualizar in inventario:
    nueva_cantidad = int(input("Ingresa la nueva cantidad: "))
    inventario[producto_actualizar] = nueva_cantidad
    print("Cantidad actualizada correctamente.\n")
else:
    print("Ese producto no existe en el inventario.\n")

# Mostrar productos con stock menor a 5
print("Productos con stock bajo (menor a 5):")

for producto, stock in inventario.items():
    if stock < 5:
        print(producto, "-", stock)