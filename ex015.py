import random
a1 = str(input('digite um nome: '))
a2 = str(input('digite um nome: '))
a3 = str(input('digite um nome: '))
a4 = str(input('digite um nome: '))
lista_alunos= [a1,a2,a3,a4]
random.shuffle(lista_alunos)
print('A ordem de apresentação será')
print(lista_alunos)