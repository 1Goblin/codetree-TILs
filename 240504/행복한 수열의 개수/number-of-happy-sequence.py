def check(arr, m):
    c = 0

    for i in range(len(arr)-m+1):
        for j in range(i+1,i+m):
            if arr[i]!=arr[j]:
                break
            return True
        

n, m = tuple(map(int, input().split()))
cnt = 0

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

for i in range(n):

    carr = [cal[i] for cal in arr]

    if check(arr[i], m):
        cnt+=1

    if check(carr, m):
        cnt+=1


print(cnt)