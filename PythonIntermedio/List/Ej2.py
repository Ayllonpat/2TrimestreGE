#Encuentra todos los números del 1 al 1000 que incluyan entre sus cifras al menos un 3.

numeros_con_3 = [] 

for n in range(1,1000):
    if '3' in str(n):
        numeros_con_3.append(n)   

print(numeros_con_3 )