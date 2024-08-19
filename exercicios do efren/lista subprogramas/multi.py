def mult(m, n):
    if n ==0:
        return 0
    else:
        return m +mult(m,n-1)
    
print(mult(5,4))