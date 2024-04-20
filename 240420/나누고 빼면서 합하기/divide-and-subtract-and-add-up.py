n, m = tuple(map(int, input().split()))
a = list(map(int, input().split()))

cnt = 0

def mpr():
    global m
    if m%2==0:
        m=m//2
    else:
        m-=1

while (m>0):
    cnt+=a[m-1]
    mpr()

print(cnt)