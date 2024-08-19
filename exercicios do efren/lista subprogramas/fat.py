def fat(n):
    if n<=1 :
        return 1
    else:
        return n * fat(n-1)
    

g = fat(6)

print(g)