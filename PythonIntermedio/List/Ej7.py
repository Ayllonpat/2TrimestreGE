#Obtén solamente los números en una oración como 'En 1984 hubo 13 casos
#  de protesta con más de 1000 asistentes'

cadena = "En 1984 hubo 13 casos de protesta con más de 1000 asistentes"

numeros = "1234567890"

lista = []

for n in cadena:
    if n in numeros:
        lista.append(n)

print(lista)