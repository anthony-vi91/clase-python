numeros = [4, 7, 2, 4, 9, 2, 8, 6, 7]

#Eliminar los duplicados
sin_duplicados = []  
for n in numeros:             
    if n not in sin_duplicados:  
        sin_duplicados = sin_duplicados + [n]

print("Lista sin duplicados:", sin_duplicados)

#Ordenar de menor a mayor
for i in range(len(sin_duplicados) - 1):
    for j in range(len(sin_duplicados) - 1 - i):
        if sin_duplicados[j] > sin_duplicados[j + 1]:
            # Intercambiamos los valores
            temp = sin_duplicados[j]
            sin_duplicados[j] = sin_duplicados[j + 1]
            sin_duplicados[j + 1] = temp

print("Lista ordenada:", sin_duplicados)

# Mostrar solo los números pares
pares = []  
for n in sin_duplicados:
    if n % 2 == 0:  
        pares = pares + [n]

print("Números pares:", pares)