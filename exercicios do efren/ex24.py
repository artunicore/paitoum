a, b, c= map(float, input().split())


if a >= b + c:
    print('NAO FORMA TRIANGULO')
elif a**2 == b**2 + c**2:
    print('TRIANGULO RETANGULO')
elif a**2 > b**2 + c**2:
    print('TRIANGULO OBTUSANGULO')
elif a**2 < b**2 + c**2:
    print('TRIANGULO ACUTANGULO')
    
if a == b == c:
    print('TRIANGULO EQUILATERO')
elif a == b or a == c or b == c:
    print('TRIANGULO ISOSCELES')