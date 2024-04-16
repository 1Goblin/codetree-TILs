n, m = tuple(map(int, input().split()))

def pr(n, m):
    if n>m:
        for i in range(m,1,-1):
            if n%i==0 and m%i==0:
                print(i)
                break
    elif n<=m:
        for i in range(m,1,-1):
            if n%i==0 and m%i==0:
                print(i)
                break


pr(n,m)