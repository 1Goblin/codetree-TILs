def check(arr, m):
    c = 1
    max_c = 1

    for i in range(1,len(arr)):
        if arr[i] == arr[i-1]:
            c+=1
        else:
            c = 1
        max_c = max(max_c, c)
    
    return max_c >= m
        

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