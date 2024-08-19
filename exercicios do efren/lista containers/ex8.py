import random

lista1 = [random.randint(0,100) for x in range(25)]
lista2 = [random.randint(0,100) for x in range(25)]
lista3 = [None] * 50

print(lista1)
print(lista2)

for i in range(len(lista3)):
    if i%2 == 0:
        lista3[i]= lista1[i // 2]
    else:
        lista3[i]= lista2[i // 2]
    
print(lista3)