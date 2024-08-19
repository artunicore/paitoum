sec = int(input(''))
horas = sec//3600
sec = sec%3600
minutos = sec //60
s = sec%60
print(f'{horas}:{minutos}:{s}')