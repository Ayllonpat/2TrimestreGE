#Obtén el índice y el valor como una tupla para los elementos de la lista
#  “hi”, 4, 8.99, 'apple', ('t,b','n'). El resultado se vería así (índice,
#  valor), (índice, valor)

lista = ["hi", 4, 8.99, 'apple', ('t,b','n')]

lista_valor= []

for n in lista:
    lista_valor.append((lista.index(n), n))

print(lista_valor)

