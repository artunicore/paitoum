N= 5
lista = []
for _ in range(N):
    #append adciona algo a uma variavel, nesse caso, ta adicionando um input
    lista.append(int(input()))
    
s=0

for i in lista:
    s+=1
    
print(f'{lista}')
print(f'{s}')
print(f'{s/N}')