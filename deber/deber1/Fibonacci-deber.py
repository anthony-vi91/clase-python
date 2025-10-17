#fibonacci
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        list_fib = [0, 1]
        while len(list_fib) < n:
            a = list_fib[-1] + list_fib[-2]
            list_fib.append(a)
        return list_fib

try:
    num = 8
    if num > 15:
        print("El numero no puede ser mayor a 15.")
    else:
        serie = fibonacci(num)
        print(f"La serie de Fibonacci hasta el numero {num} es:")
        print(serie)
except ValueError:
    print("Por favor, ingrese un numero entero valido.")