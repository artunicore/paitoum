s = float(input())


if s >0 and s <= 400.00:
    r = s * .15
    ns = s + r
    print(f'Novo salario: {ns:.2f}')
    print(f'Reajuste ganho: {r:.2f}')
    print('Em percentual: 15 %')
if s >400.00 and s <= 800.00:
    r = s * .12
    ns = s + r
    print(f'Novo salario: {ns:.2f}')
    print(f'Reajuste ganho: {r:.2f}')
    print('Em percentual: 12 %')
if s >800.00 and s <= 1200.00:
    r = s * .10
    ns = s + r
    print(f'Novo salario: {ns:.2f}')
    print(f'Reajuste ganho: {r:.2f}')
    print('Em percentual: 10 %')
if s >1200.00 and s <= 2000.00:
    r = s * .07
    ns = s + r
    print(f'Novo salario: {ns:.2f}')
    print(f'Reajuste ganho: {r:.2f}')
    print('Em percentual: 7 %')
if s>2000:
    r = s * .04
    ns = s + r
    print(f'Novo salario: {ns:.2f}')
    print(f'Reajuste ganho: {r:.2f}')
    print('Em percentual: 4 %')