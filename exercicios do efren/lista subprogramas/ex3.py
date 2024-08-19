def fat(n:int):
    f=1
    for i in range(1, n+1):
        f*= i
    return f


f = fat(5)
print(f)