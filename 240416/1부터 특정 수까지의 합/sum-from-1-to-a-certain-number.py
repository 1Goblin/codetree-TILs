n = int(input())

def pr(n):
    m = 0
    for i in range(1,n+1):
        m+=i
    m = m//10
    return m

print(pr(n))