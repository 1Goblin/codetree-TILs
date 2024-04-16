n, m = tuple(map(int,input().split()))

def pr(x, y):
    n = x
    m = y
    for i in range(n):
        for j in range(m):
            if n==m or n>m:
                break
            else:
                n=n+x
        if n==m:
            break
        else:
            m=m+y
    print(n)


pr(n, m)