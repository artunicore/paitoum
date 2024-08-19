cod, espec = map(int, input().split())

hd = 4.00
xs = 4.50
xb = 5.00
ts = 2.00
refri = 1.50

if cod == 1:
    print(f'Total: R$ {hd*espec:.2f}')
if cod == 2:
    print(f'Total: R$ {xs*espec:.2f}')
if cod == 3:
    print(f'Total: R$ {xb*espec:.2f}')
if cod == 4:
    print(f'Total: R$ {ts*espec:.2f}')
if cod == 5:
    print(f'Total: R$ {refri*espec:.2f}')