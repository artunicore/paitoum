a, b, c =map(float, input().split())

a_triangulo= (a * c)/2
a_circulo = 3.14159 * (c ** 2)
a_trapezio = ((a+b)*c)/2
a_quadrado = b**2
a_ret = a * b

print(f'TRIANGULO: {a_triangulo:.3f}')
print(f'CIRCULO: {a_circulo:.3f}')
print(f'TRAPEZIO: {a_trapezio:.3f}')
print(f'TRAPEZIO: {a_quadrado:.3f}')
print(f'TRAPEZIO: {a_ret:.3f}')