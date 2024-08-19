#tempo em dias
t_dias= int(input('Digite o tempo em dias: '))

#variaveis
a = t_dias//365

t_dias = t_dias % 365
m = t_dias//30
d = t_dias % 30

#impressao
print(f'{a} ano(s),{m:2} mes(es),{d:2} dia(s)')
