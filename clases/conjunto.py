#set de datos que no se repite
frutas = {"manzana", "pera", "naranja", "manzana"}
print(frutas)

# print(frutas[0]) #Esto no se puede hacer en un conjunto

numeros = set({1,2,3,3,4})
print(numeros)

numeros.add(5)
print(numeros)

numeros.remove(2)
print(numeros)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)
print("Interseccion:", a & b)
print("Diferencia:", a - b) #Presenta la diferencia de "a" que no estan en "b"
print("Diferencia simetrica:", a ^ b)