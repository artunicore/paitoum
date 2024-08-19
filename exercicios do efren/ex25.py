h_i, h_f = map(int, input().split())

if h_i < h_f:
    tempo = h_f - h_i
else:
    tempo = 24 - h_i + h_f
    
print(f'O JOGO DUROU {tempo} HORA(S)')