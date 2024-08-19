import random

n=10

a = [None] *n

i = 0

while i<n:
    a[i] = random.randint(1,20)
    i+=1
    
print(a)