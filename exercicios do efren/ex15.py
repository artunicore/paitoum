valor = int(input())

cem = 100
cinquenta = 50
vinte = 20
dez = 10
cinco = 5
dois = 2
um = 1

print(valor)

quantidade = valor//cem
valor %= cem
print(f"{quantidade} nota(s) de R$ 100,00")

quantidade = valor//cinquenta
valor %= cinquenta
print(f"{quantidade} nota(s) de R$ 50,00")

quantidade = valor//vinte
valor %= vinte
print(f"{quantidade} nota(s) de R$ 20,00")

quantidade = valor//dez
valor %= dez
print(f"{quantidade} nota(s) de R$ 10,00")

quantidade = valor//cinco
valor %= cinco
print(f"{quantidade} nota(s) de R$ 5,00")

quantidade = valor//dois
valor %= dois
print(f"{quantidade} nota(s) de R$ 2,00")

quantidade = valor//um
valor %= um
print(f"{quantidade} nota(s) de R$ 1,00")