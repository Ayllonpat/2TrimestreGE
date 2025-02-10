#Crea una lista de todas las consonantes de la cadena “A los yaks 
# amarillos les gusta gritar y bostezar y ayer cantaban mientras comían 
# ñames asquerosos”

cadena = "A los yaks  amarillos les gusta gritar y bostezar y ayer cantaban mientras comían ñames asquerosos"

consonantes = "bcdfghjklmnñpqrstvxzwyBCDFGHJKLMNÑPQRSTVXZWY"

lista = []

for n in cadena:
    if n in consonantes:
        lista.append(n)

print(lista)
    