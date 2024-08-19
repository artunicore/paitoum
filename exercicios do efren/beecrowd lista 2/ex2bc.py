valor_maior = 0
posicao_maior = 0

for i in range(0,100):
    valor = int(input())
    
    if valor>valor_maior:
        valor_maior = valor
        posicao_maior = i
        
print(valor_maior)
print(posicao_maior)