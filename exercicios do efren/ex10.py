a,b,c = map(int,input().split())

maiorAB= (a+b+abs(a-b))/2
maior = max(maiorAB,c)
print(f'{maior} eh o maior')