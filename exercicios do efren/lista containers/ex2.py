N=10
lista = [None] *N
lista_quad = []
for i in range(N):
    lista[i] = int(input())
 

for num in lista:
    quadrado = num **2
    lista_quad.append(quadrado)

print(lista)
print(lista_quad)