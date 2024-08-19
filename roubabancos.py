import itertools

# Defina os números disponíveis
numeros_disponiveis = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Gere todas as combinações possíveis de quatro dígitos
todas_combinacoes = list(itertools.product(numeros_disponiveis, repeat=6))

# Exiba todas as combinações
for comb in todas_combinacoes:
    print(comb)
