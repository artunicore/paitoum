s = float(input())

if s >= 0 and s <=2000.00:
    print(f'Isento')
if s > 2000.00 and s <=3000.00:
    r = (s - 2000.00) * .08
    print(f'R$ {r:.2f}')
if s > 3000.00 and s <=4500.00:
    r = 1000.00 * .08 + (s -3000.00) * .18
    print(f'R$ {r:.2f}')
if s > 4500.00:
    r = 1000.00 * .08 + 1500.00 *.18 + ( s - 4500.00) * .28
    print(f'R$ {r:.2f}')