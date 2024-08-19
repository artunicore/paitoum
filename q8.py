import math
co = float(input('digite o seu cateto oposto: '))
ca= float(input('digite o seu cateto adjascente: '))
hi= math.hypot(co, ca)
print('a hipotenusa entre {} e {} é {:.2f}'.format(co,ca,hi))