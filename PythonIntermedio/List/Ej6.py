#Encuentra los números comunes en dos listas (sin usar una tupla o 
#conjunto) lista_a = 1, 2, 3, 4, lista_b = 2, 3, 4, 5

lista_a=[1,2,3,4]
lista_b=[2,3,4,5]

def comprobar_iguales(lista_a, lista_b):
    lista = []
    for n in lista_a:
        if (n in lista_b):
            lista.append(n)
    return lista

resultado = comprobar_iguales(lista_a, lista_b)
            
print(resultado)