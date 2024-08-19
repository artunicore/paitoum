def fib(n):
    if n ==0:
        return 0
    if n==1:
        return 1
    else:
        return fib(n-2) + fib(n-1)
        print(n)
    

def fib_interativo(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    
    fib_sequence = [0, 1]

    for i in range(2, n + 1):
        fib_sequence = fib_sequence + [fib_sequence[i - 1] + fib_sequence[i - 2]]

    return fib_sequence

g = fib_interativo(40)

print(g)

