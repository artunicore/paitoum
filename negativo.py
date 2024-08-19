nota = float(input('Digite um numero:'))

if nota < 0 or nota > 10:
    print('invalida')
else:
    if nota >= 9.0:
        print('excelente')
    elif nota >=8.0:
        print('otimo')
    elif nota >=7.0:
        print('bom')
    elif nota >=6.0:
        print('regular')
    else:
        print('reprovado')
