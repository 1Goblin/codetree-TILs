a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = list(map(int, input().split()))

cnt = 0

def aaa(a,b,c,d,e):
    
    for i in range(a+1000,c+1000):
        for j in range(b+1000,d+1000):
            arr[i][j] += e

arr = [
    [0 for _ in range(2000)]
    for _ in range(2000)
]

aaa(a[0],a[1],a[2],a[3],1)
aaa(b[0],b[1],b[2],b[3],2)
aaa(m[0],m[1],m[2],m[3],3)

for i in range(2000):
    for j in range(2000):
        if arr[i][j] == 1 or arr[i][j] == 2:
            cnt+=1



print(cnt)