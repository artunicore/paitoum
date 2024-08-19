def menor(*numeros):
    m = float('inf')
    for n in numeros:
        if n <m:
            m = n
            
        return m


N= 12
lista = [None] * N

for i in range(N):
    lista[i] = int(input())
 
a = menor(lista)
 
print(a)