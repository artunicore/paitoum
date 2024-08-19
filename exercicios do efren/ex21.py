n_a,n_b,n_c,n_d = map(float, input().split())

media1 = (n_a* 2 + n_b*3 + n_c*4 + n_d*1)/(2+3+4+1)

print(f'Media: {media1:.1f}')

if media1 >= 7.0:
    print('Aluno aprovado.')
elif media1 <5.0:
    print('Aluno reprovado.')
else:
    if media1>=5.0 and media1 <7.0:
         print('Aluno em exame.')
         n_exame = float(input())
         media2 = (n_exame + media1)/2

         if media2 >=5.0:
            print('Aluno aprovado.')
            print(f'Media final: {media2}')
    else:
        print('Aluno reprovado.')