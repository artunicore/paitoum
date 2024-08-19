N = int(input())

for _ in range(N):
    
    X,Y = map(int, input().split())
    
    soma= 0
    for i in range(X,Y +1):
        if i % 2 !=0:
            soma+=i
            
    print(soma)