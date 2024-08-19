data = input()

dd, mm, aa = data.split('/')

if mm == '1':
    mm_saida = 'jan'
if mm == '2':
    mm_saida = 'fev'
if mm == '3':
    mm_saida = 'mar'
if mm == '4':
    mm_saida = 'abr'
if mm == '5':
    mm_saida = 'mai'
if mm == '6':
    mm_saida = 'jun'
if mm == '7':
    mm_saida = 'jul'
if mm == '8':
    mm_saida = 'ago'
if mm == '9':
    mm_saida = 'set'
if mm == '10':
    mm_saida = 'out'
if mm == '11':
    mm_saida = 'nov'
if mm == '12':
    mm_saida = 'dez'
    
data = dd + 'de ' + mm_saida + 'de' + aa

print(data)
