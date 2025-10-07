#Numeros Primos
def es_primo(num):
#Calculo para saber si el numero es primo
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
#ingreso de numero y presentar mensaje de resultado
try:
    numero = (5)
    if es_primo(numero):
        print(f"El numero {numero} es primo.")
    else:
        print(f"El numero {numero} no es primo.")
except ValueError:
    print("Por favor, ingrese un numero entero valido.")