#Generar una lista de tuplas que consten únicamente de los números 
# coincidentes en estas listas list_a = 1, 2, 3,4,5,6,7,8,9, 
# list_b = 2, 7, 1, 12. El resultado se vería así (4,4), (12,12)

lista_a = (1,2,3,4,5,6,7,8,9)
lista_b = (2, 7, 1, 12)

def comprobar_numeros(lista_a, lista_b):

    lista_tuplas = []

    for n in lista_a:
        if (n in lista_b):
            lista = n,n
            lista_tuplas.append(lista)           
    return lista_tuplas

resultado = comprobar_numeros(lista_a, lista_b)
            
print(resultado)