#bloque de codigos reutilizable para organizar mejor el codigo
"""
asi se define una funcion
def nombre_de_funcion(parametros:):
    #codigo a ejecutar
    return resultdo
"""
#definicion de funcion
def saludar():
    print("Hola, Bienvenido a Python")

saludar()
#Parametros y valores de retorno
def sumar(a, b):
    resultado = a + b
    return resultado

#true toma el valor de 1
total = sumar(5.2, 3)
print("La suma es: ", total)

total = sumar(True, 3)
print("La suma es: ", total)

#funciones con parametros con defectos
def saludar(nombre = "invitado"):
    print (f"Hola, {nombre}")

saludar("Alex")
saludar()

#funcion scopeo alcanze
#variable local
def mostrar_numero():
    x = 10 #variable local
    print("Dentro de la funcion: ", x)

mostrar_numero()
#print(x) esta variable da error al imprimir porque esta en la funcion y no  se la puede usar

#variable global
x = 100
def mostrar():
    print("Dentro de la funcion:",x)

mostrar()
print("Fuera de la funcion:", x)