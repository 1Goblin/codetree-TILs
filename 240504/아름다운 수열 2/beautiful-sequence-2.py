n, m = tuple(map(int, input().split()))

a = list(map(int ,input().split()))
b = list(map(int, input().split()))

def check(arr, b):

    arr.sort()
    b.sort()
    if arr==b:
        return True

cnt = 0

for i in range(n-m+1):
    arr = []
    for j in range(i,i+m):
        arr.append(a[j])
    if check(arr,b):
        cnt+=1

print(cnt)