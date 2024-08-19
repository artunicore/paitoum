codigo_peca1, numero_peca1, valor_unitario_peca1 = map(float, input().split())

codigo_peca2, numero_peca2, valor_unitario_peca2 = map(float, input().split())

valor_total = (numero_peca1 * valor_unitario_peca1) + (numero_peca2 * valor_unitario_peca2)

print(f'VALOR A PAGAR: R$ {valor_total:.2f}')