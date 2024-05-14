n = int(input())

arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

cnt = 0

for i in range(len(arr)):
    for j in range(i-1, -1,-1):
        if arr[i][0] == arr[j][0]:
            if arr[i][1] != arr[j][1]:
                cnt+=1
            break
        
print(cnt)