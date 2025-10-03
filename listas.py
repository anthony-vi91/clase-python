#lista
numeros = [1, 2, 3, 4, 5]
print("Tercer elemento: ",numeros[2])

#agrega algo al final de la lista
numeros.append(6)
print("Despues del append: ", numeros)

#remueve especificamente el item del cuadro no la posicion
numeros.remove(3)
print("Despues del remove(3): ", numeros)

#ordenamiento de lista 
#ascendente de menor a mayor
numeros.sort()
print("Ordenados ascendente: ",numeros)
#descendente demayor a menor
numeros.sort(reverse=True)
print("Ordenados descendente: ",numeros)
#accede a los 2 primeros numeros de la lista
print("Dos primeros elementos:", numeros[:2])

#mostrar dimension de la lista
print("Dimension de la lista: ", len(numeros))