nome_vendedor = input()

salario = float(input())
total_vendas = float(input())

comissao = total_vendas * .15

s_total = salario + comissao

print(f'TOTAL = R$ {s_total:.2f}')