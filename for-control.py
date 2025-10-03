frutas = ("manzana","banana","cereza")
#lista
for fruta in frutas:
    print(fruta)
#rango lista
for i in range(5): # del 0 a 4
        print(i)
#dimension lista
for i in range(len(frutas)):
    print(frutas[i])

for i in range(4):
    
    if i == 5:
        break
    if i % 2 == 0:
        continue
    print(i)
else:
    print("El bucle termino sin break")