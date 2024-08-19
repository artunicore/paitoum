a = [None] * 5

for i in range(len(a)):
    a[i] = int(input())

print(a)

for i in range(len(a)):
    a[i]*= 2
    
print(a)