# Tupla de entrada
numeros = (5, 8, 12, 3, 9, 5, 2)

#Mostrar el valor máximo y mínimo
maximo = max(numeros)
minimo = min(numeros)

print("Valor máximo:", maximo)
print("Valor mínimo:", minimo)

#Calcular el promedio de todos los valores
suma = 0
contador = 0

for n in numeros:
    suma = suma + n
    contador = contador + 1

promedio = suma / contador

print("Promedio:", promedio)

#Verificar si un número está dentro de la tupla

numero_usuario = 9
print("numero ingresado es: 9")
if numero_usuario in numeros:
    print("El número", numero_usuario, "sí está en la tupla.")
else:
    print("El número", numero_usuario, "no está en la tupla.")