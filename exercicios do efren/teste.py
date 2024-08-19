# Lê as quatro notas do aluno
N1, N2, N3, N4 = map(float, input().split())

# Calcula a média ponderada com os pesos 2, 3, 4 e 1
media = (N1*2 + N2*3 + N3*4 + N4*1) / 10

# Exibe a média com uma casa decimal
print(f"Media: {media:.1f}")

# Verifica a situação do aluno
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    
    # Lê a nota do exame
    nota_exame = float(input())
    
    # Calcula a nova média considerando o exame
    nova_media = (media + nota_exame) / 2
    
    print(f"Nota do exame: {nota_exame:.1f}")
    
    if nova_media >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    
    print(f"Media final: {nova_media:.1f}")