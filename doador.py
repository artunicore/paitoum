idade = int(input('Qual a sua idade?'))


if idade >= 18 and idade <= 67:
    print('voce pode doar sangue meu comparsa')
elif idade < 18 :
    print('espera so um tico')
else:
    if idade > 67:
      print('ce ta vei fir, so na outra vida agora')