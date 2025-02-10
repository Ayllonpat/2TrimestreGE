#Utiliza una comprensión de lista anidada para encontrar todos los 
# números del 1 al 1000 que sean divisibles por cualquier dígito 
# excepto 1 (2-9)

def numero_divisible(limite_inferior, limite_superior):

    lista = []
    

    for n in range(limite_inferior, limite_superior + 1):
        if n % 2 == 0:
            resultado.append(n)
        if n % 3 == 0:
            resultado.append(n)
        if n % 4 == 0:
            resultado.append(n)
        if n % 5 == 0:
            resultado.append(n)
        if n % 6 == 0:
            resultado.append(n)
        if n % 7 == 0:
            resultado.append(n)
        if n % 8 == 0:
            resultado.append(n)
        if n % 9 == 0:
            lista.append(n)
        
        resultado= list(set(lista))
        
    return resultado

print(numero_divisible(1, 1000))