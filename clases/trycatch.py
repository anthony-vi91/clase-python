#try catch se usa para controlar errores
#try catch basisco
try:
    numero = int(input("Ingrese un numero: "))
    resultado = 10/numero
    print("l resultado es: ",resultado)
except ZeroDivisionError:
    print("No se puede dividir entre cero.")

#ValueError
try:
    edad = int(input("Ingrese su edad: "))
    print("Su edad es: ",edad)
except ValueError:
    print("Error: Debe ingresar un numero entero valido")

#Multiples exception
try: 
    a = int(input("Ingrese el numerador: "))
    b = int(input("Ingrese el denominador: "))
    resulado = a / b
    print("El resultado es: ",resulado)
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero")
except ValueError:
    print("Error: Debe ingresar un numero entero valido")

#else y finaly
try:
    numero = int(input("Ingrese un numero positivo: "))
    if numero <= 0:
        raise ValueError("Debe ser positivo")
        #raise es para lanzar un error
except ValueError as e:
    print("Error: ",e)
else:
    print("No hubo errores")
finally:
    print("Fin del programa")