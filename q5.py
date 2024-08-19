from math import pi

d = float(input('Diametro: '))
r = d/2
a = pi * r**2
p = 2 * pi * r

print(f'Perimetro: {p:.2f}')
print(f'Area: {a:.2f}')
