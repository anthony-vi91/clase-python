#Las tuplast son inmutables (no se cambian los elementos de la lista)
#listas que no se pueden modificar
ciudades = ("Quito", "Guayaquil", "Cuenca")

print("Segunda Ciudad: ", ciudades[1])
#Para impimir el error
#de todo el error dice el especifico
try:
    ciudades[0] = "Ambato"
except TypeError as o:
    print("Error:", o)
    
#agregar un item a tupla transformando en lista y de vuelta en tupla
ciudades_listas = list(ciudades)
ciudades_listas.append("Ambato")
#transforma a tupla
ciudades = tuple(ciudades_listas)
print("Nueva tupla: ",ciudades)