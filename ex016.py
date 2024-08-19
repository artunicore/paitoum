a= int(input('digite um numero '))
b= int(input('digite um numero '))
c= int(input('digite um numero '))
if a==b and  b==c:
    print('é equilatero')
elif (a==b and c!=b) or ( b==c and c!=a) or (c== a and a!=b):
    print('é isosceles')
elif a!=b and  b!=c:
    print('escalaeni')
    
