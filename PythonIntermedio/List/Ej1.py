##Encuentra todos los números del 1 al 1000 que sean divisibles por 7

def numero_divisible(limite_inferior, limite_superior):

    resultado = []

    for n in range(limite_inferior, limite_superior + 1):
        if n % 7 == 0:
            resultado.append(n)
    return resultado

print(numero_divisible(1, 1000))