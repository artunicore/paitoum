sm = float(input('Qual seu consumo de agua?'))
l = float(input('Qual seu salario?'))

c = (sm * 0.02 * l) / 1000
d = c * 0.15
cd = c - d

print(f'conta = R$ {c:.2f}\n |\n conta com desconto = R$ {cd:.2f}')
