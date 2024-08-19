#tempo em segundos
t_em_segundos = int(input("Digite o tempo em segundos: "))

#variaveis
h = t_em_segundos // 3600 #<--- horas em segundos
t_em_segundos = t_em_segundos % 3600
m = t_em_segundos // 60
s = t_em_segundos % 60

#impressao
print(f"O tempo formatado é:{h:02}:{m:02}:{s:02}")
