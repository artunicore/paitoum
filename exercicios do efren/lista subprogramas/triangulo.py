def pascal_element(n, p):
    if p==0 or p==n:
        return 1
    return pascal_element(n-1, p-1) + pascal_element(n-1, p)
    
def pascal_line(n):
    return [pascal_element(n, p) for p in range(n+1)]

def pascal_triangle(n):
    return [ pascal_line(m) for m in range(n+1) ]

n = int(input())
tri = pascal_triangle(n)
for line in tri:
    print(line)
