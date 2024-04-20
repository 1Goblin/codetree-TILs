n = int(input())

def add(n):
    if n==1:
        return 1
    
    return add(n-1)+n

print(add(n))