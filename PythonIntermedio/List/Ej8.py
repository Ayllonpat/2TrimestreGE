#Dado numbers = range(20), se genera una lista que contiene la palabra 
# "par" si un número en los números es par, y la palabra "impar" si el 
# número es impar. El resultado se vería así: "impar", "impar", "par".

numbers = range(1,20)

lista = []

for n in numbers:
    if n  % 2 == 0:
        lista.append("par")
    else:
        lista.append("impar")

print(lista)